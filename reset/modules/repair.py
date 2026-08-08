"""
repair.py — the self-healing generation loop.

generate_phase() replaces "call the API once and save whatever comes back". It calls, runs
the phase's spec checks (specs.py), and on failure sends the output back with a precise
corrective instruction, up to MAX_REPAIR_ATTEMPTS times.

Two properties that matter and are easy to get wrong:

1. The repair exchange is NOT left in the running conversation. Later phases receive only
   the FINAL corrected output, exactly as if it had been right the first time. Leaving the
   rejected draft and the scolding in context would teach the model that malformed output
   is acceptable-then-fixed, and would grow every subsequent request by the size of a whole
   failed phase.

2. A phase that still fails after the last attempt is SAVED anyway, and returned with its
   outstanding failures. Discarding it would throw away real research over a format problem
   a human (or a later mechanical pass) can fix cheaply; the project-level gate in
   validate.py is what stops it reaching the database.
"""
from . import config, specs
from .api import call_with_retries
from .logs import log_repair


def generate_phase(messages: list, num: int, key: str, project_name: str, base_url: str,
                   token: str, model: str, plog, max_tokens: int = None) -> tuple:
    """Generate one phase, repairing format failures in-place.

    `messages` is the running conversation; it is NOT mutated -- the caller decides what to
    append once the final text is known.

    Returns (text, remaining_failures). remaining_failures is a list of (Check, detail) and
    is empty when the phase is clean.
    """
    label = f"{project_name} phase {num:02d}-{key}"
    text = call_with_retries(messages, base_url, token, model, label, max_tokens=max_tokens)
    text = _ensure_header(text, project_name)

    if not config.REPAIR_ENABLED:
        return text, []

    failed = specs.run_checks(num, key, project_name, text)
    if not failed:
        return text, []

    for attempt in range(1, config.MAX_REPAIR_ATTEMPTS + 1):
        names = [c.name for c, _ in failed]
        details = "; ".join(f"{c.name}: {d}" for c, d in failed)
        plog(f"phase {num:02d}-{key}: ✗ spec check failed ({details}) -- "
             f"self-repair attempt {attempt}/{config.MAX_REPAIR_ATTEMPTS}")

        repair_prompt = specs.build_repair_prompt(num, key, project_name, failed)
        # Fresh list each round: the conversation the model sees is
        #   <running context> + <its rejected draft> + <what was wrong>
        # and never accumulates earlier rejected drafts on top of each other.
        repair_messages = messages + [
            {"role": "assistant", "content": text},
            {"role": "user", "content": repair_prompt},
        ]
        try:
            candidate = call_with_retries(repair_messages, base_url, token, model,
                                          f"{label} repair {attempt}", max_tokens=max_tokens)
        except Exception as e:  # noqa: BLE001 -- a failed repair keeps the draft we already have
            plog(f"phase {num:02d}-{key}: repair call failed ({e}) -- keeping previous draft")
            log_repair(project_name, num, key, attempt, names, "repair_call_failed")
            break

        candidate = _ensure_header(candidate, project_name)
        still_failed = specs.run_checks(num, key, project_name, candidate)

        if len(still_failed) < len(failed) or not still_failed:
            # Strictly better (or perfect) -- adopt it. A repair that fixes 2 of 3 checks is
            # still progress worth keeping.
            text, failed = candidate, still_failed
        else:
            # No improvement: keep whichever draft we already had rather than trading a known
            # state for an equally broken one, and stop -- a model that ignored an explicit
            # format correction once will not comply on attempt three. That is a prompt bug to
            # fix in reset/phase_NN_*.txt, which repairs.log makes visible.
            plog(f"phase {num:02d}-{key}: repair did not improve "
                 f"({len(still_failed)} check(s) still failing) -- stopping repair loop")
            log_repair(project_name, num, key, attempt, names, "no_improvement")
            break

        if not failed:
            plog(f"phase {num:02d}-{key}: ✓ self-repair succeeded on attempt {attempt}")
            log_repair(project_name, num, key, attempt, names, "repaired")
            break

        log_repair(project_name, num, key, attempt, names, "partially_repaired")

    if failed:
        plog(f"phase {num:02d}-{key}: ⚠ saved with {len(failed)} unresolved check(s): "
             f"{', '.join(c.name for c, _ in failed)} -- see reset/repairs.log")
    return text, failed


def _ensure_header(text: str, project_name: str) -> str:
    from .prompts import ensure_project_header
    return ensure_project_header(text, project_name)

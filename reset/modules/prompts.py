"""
prompts.py — loading and assembling the text sent to the model.

Nothing here makes a network call or validates a response; it only builds strings. Prompt
BODIES stay in reset/phase_NN_*.txt (editable without touching code) -- this module is the
plumbing that stitches them together with the shared rules block and the phase datasets.
"""
import re
from pathlib import Path

from . import config


def load_shared_format_rules() -> str:
    """The doc's "ATURAN FORMAT" block -- citations WAJIB per fact, Evidence Level tags, no
    fabrication, etc. docs/Protocol/Phased-Research-Prompts.md's "Shared rules" section is
    explicit: "Append this block to every phase prompt before sending it." Missing this
    entirely is what produced zero-citation output in an early version of this script
    (verified live, 2026-08-03: Aptos test phases had 0 (HIGH)/(MEDIUM)/(LOW) tags vs 24-254
    in the real data_project/Arbitrum/ phases) -- tools/ingest.py's validate_phase_content()
    would hard-reject that as the exact "empty citations" failure mode the doc's own "Known
    failure patterns" section warns about."""
    return (config.RESET_DIR / "shared_format_rules.txt").read_text(encoding="utf-8")


def load_phase_prompt(num: int, key: str) -> str:
    """reset/phase_NN_<key>.txt + the shared rules block appended."""
    body = (config.RESET_DIR / f"phase_{num:02d}_{key}.txt").read_text(encoding="utf-8")
    return body.rstrip() + "\n\n" + load_shared_format_rules().rstrip() + "\n"


def load_stage_prompt(prompt_file: str) -> str:
    """A Phase 11 stage prompt (reset/phase_11x_*.txt) + the shared rules block."""
    body = (config.RESET_DIR / prompt_file).read_text(encoding="utf-8")
    return body.rstrip() + "\n\n" + load_shared_format_rules().rstrip() + "\n"


def prompt_placeholder(num: int, key: str) -> str:
    """Stand-in for a COMPLETED phase's full prompt text once its real output is already in
    context. The instructions themselves add no new information once the phase they produced
    is sitting right below them (unmodified, in full) -- keeping them around just means
    re-sending the same ~2-8k chars of template/rules text on every later call for no
    benefit. By phase 11 this was the majority of the payload: summing reset/phase_*.txt +
    shared_format_rules.txt (which gets appended to every single phase prompt) came to ~58k
    chars of prompt text alone, repeated in full for every one of the 10 prior phases.
    Shrinking old prompts to this marker while leaving every real answer untouched cuts
    phase 11's total request size roughly in half without losing a single fact the model
    actually produced."""
    return (f"[Phase {num:02d}-{key} instructions were sent here; "
            f"see this phase's full output below.]")


def inject_phase_dataset(prompt: str, proj_dir: Path, phase_specs: list) -> str:
    """Appends the real saved content of the given (num, key) phases after the prompt's own
    instructional text, under a clearly labeled section. The model only ever sees what's
    physically included in the message it's sent -- the prompt's own "CONTEXT DEPENDENCIES"
    section is a description of what to expect, this is the actual data."""
    parts = [prompt.rstrip(), "\n\n---\n\nISI DATASET (baca dan audit seluruh isi berikut):\n"]
    for num, key in phase_specs:
        text = (proj_dir / f"{num:02d}-{key}.docx").read_text(encoding="utf-8")
        parts.append(f"\n=== {num:02d}-{key}.docx ===\n{text}")
    return "".join(parts)


_MANIFEST_RE = re.compile(r"(?is)(CIF MANIFEST v3\.0.*?```.*?```)")


def extract_manifest_block(text: str) -> tuple:
    """Pulls the 'CIF MANIFEST v3.0' heading + its fenced code block out of the final Phase 11
    stage's response so it can be moved to the front of the assembled Phase 11 file (matching
    the real Arbitrum dossier's structure: CIF VALIDATION REPORT v3.0 -> CIF MANIFEST v3.0 ->
    everything else) -- the prompt asks the model to compute it last but WRITE it first in its
    own response, so this is normally a no-op reordering, not a content change. Falls back to
    (None, text) unchanged if the expected fenced-block shape isn't found, rather than
    guessing at a malformed split."""
    m = _MANIFEST_RE.search(text)
    if not m:
        return None, text
    manifest = m.group(1).strip()
    rest = (text[: m.start()] + text[m.end():]).strip()
    return manifest, rest


def ensure_project_header(text: str, name: str) -> str:
    """Always prepend `PROJECT: <Name>` when absent -- tools/ingest.py's
    validate_phase_content() requires it, and the real Arbitrum files carry it on every phase
    regardless of what the prompt asked the model to include."""
    if re.match(r"(?im)^PROJECT:\s*" + re.escape(name), text.strip()):
        return text
    return f"PROJECT: {name}\n\n{text}"

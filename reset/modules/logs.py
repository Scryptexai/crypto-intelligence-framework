"""
logs.py — all console and file logging for the reset pipeline.

Three separate log files, each answering a different question after an unattended run:
  failures.log      an API call gave up after all retries          -> re-run needed
  needs_review.log  output arrived but failed the quality gate      -> prompt/data problem
  repairs.log       output failed a spec check and was auto-fixed   -> prompt drift signal

repairs.log is the one to read when deciding whether a phase prompt needs editing: a check
that repairs successfully on nearly every project is a prompt bug being papered over by
retries, and fixing it at the prompt saves a generation per project.

Credentials must never be passed to any function here.
"""
from datetime import datetime, timezone

from . import config


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    with config._print_lock:
        print(f"[{ts}] {msg}", flush=True)


def project_logger(name: str):
    """log() bound to one project, so parallel threads stay attributable."""
    def _log(msg: str) -> None:
        log(f"[{name}] {msg}")
    return _log


def _append(path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with config._failures_lock:
        with path.open("a", encoding="utf-8") as fh:
            fh.write(line if line.endswith("\n") else line + "\n")


def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()


def log_failure(project: str, num: int, key: str, err) -> None:
    """An API call for this phase exhausted every retry -- the project stopped here."""
    _append(config.FAILURES_LOG, f"{_ts()}\t{project}\tphase {num:02d}-{key}\t{err}")


def log_needs_review(project: str, report: dict) -> None:
    """Generation succeeded but the output failed the real-extractor quality gate."""
    _append(config.REVIEW_LOG, f"{_ts()}\t{project}\tverify_10_phases failed\t{report}")


def log_repair(project: str, num: int, key: str, attempt: int, checks: list, outcome: str) -> None:
    """One self-repair round: which checks failed, and whether the retry fixed them.

    `checks` is the list of failed check names, `outcome` one of repaired/still_failing/
    gave_up. Written per attempt (not just per phase) so a phase that needed two rounds is
    distinguishable from two phases that each needed one.
    """
    _append(config.REPAIR_LOG,
            f"{_ts()}\t{project}\tphase {num:02d}-{key}\tattempt {attempt}\t"
            f"failed={','.join(checks)}\t{outcome}")

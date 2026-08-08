"""
config.py — every path, constant, tunable and shared lock for the reset pipeline.

Single source of truth so no module hardcodes a path or re-reads an env var with a
different default. Import this; never re-derive.

Credentials are read from the environment ONLY, never stored here (see load_credentials).
"""
import os
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RESET_DIR = ROOT / "reset"
MODULES_DIR = RESET_DIR / "modules"
DATA_PROJECT_ROOT = ROOT / "data_project"
TMP_TEST_ROOT = RESET_DIR / "tmp_test"

FAILURES_LOG = RESET_DIR / "failures.log"
REVIEW_LOG = RESET_DIR / "needs_review.log"
REPAIR_LOG = RESET_DIR / "repairs.log"

# tools/ on sys.path so the real extractors can be imported directly (validate.py) rather
# than shelling out -- the whole point of the quality gate is to run the SAME code the
# database sync will run, not an approximation of it.
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

PHASES = [
    (1, "foundation"), (2, "entity"), (3, "history"), (4, "technology"),
    (5, "financial"), (6, "token"), (7, "ecosystem"), (8, "market"),
    (9, "behavioral"), (10, "knowledge"), (11, "conflict"),
]

# Phase 11 (Validation & QA) is handled as four smaller, sequential API calls instead of
# appending to the full 10-phase running conversation -- see phases.run_phase_11()'s
# docstring for the full rationale (started as 2 calls, but even the smaller of those two
# still hit gateway-side 504 timeouts -- the bottleneck is generation TIME on a slow
# backend, not request size, so each stage's ASK needed to shrink too, not just its input).
PHASE11_STAGES = [
    ("11a", "phase_11a_audit.txt", [(1, "foundation"), (2, "entity"), (3, "history")]),
    ("11b", "phase_11b_audit.txt", [(4, "technology"), (5, "financial")]),
    ("11c", "phase_11c_audit.txt", [(6, "token"), (7, "ecosystem"), (8, "market")]),
    ("11d", "phase_11d_scoring.txt", [(9, "behavioral"), (10, "knowledge")]),
]

# Phase 9 (Behavioral) is split into three sequential calls on the SAME running conversation,
# for the same reason Phase 11 is split into four: the gateway kills any single generation
# that runs past ~300s (measured twice on Lido, 2026-08-08: HTTP 504 at 310s and 306s). A
# complete Phase 9 averages ~27,500 chars / ~7,850 tokens of output across the 28 real
# dossiers on disk, which cannot finish in time on this backend. Splitting the OUTPUT ask
# three ways (input stays the same -- it is the phases 1-8 context and cannot shrink) puts
# each call comfortably under the limit. Ordered so each stage is roughly a third of the work.
PHASE9_STAGES = [
    ("9a", "phase_09a_objectives.txt"),
    ("9b", "phase_09b_patterns.txt"),
    ("9c", "phase_09c_risk.txt"),
]

MAX_TOKENS = int(os.environ.get("RESET_MAX_TOKENS", "14000"))
# Phase 11b alone carries almost everything the old single-call Phase 11 produced (the real
# Arbitrum Phase 11 section is ~38.9k chars, ~9.7k tokens estimated -- already over the old
# 8192 default). Its own constant so phases 1-10 aren't forced to allow bigger (and
# slower/costlier) completions than they need.
PHASE11_MAX_TOKENS = int(os.environ.get("RESET_PHASE11_MAX_TOKENS", "16000"))
REQUEST_TIMEOUT_SECONDS = int(os.environ.get("RESET_REQUEST_TIMEOUT_SECS", "900"))
PHASE_SLEEP_SECONDS = int(os.environ.get("RESET_PHASE_SLEEP_SECS", "60"))
PROJECT_SLEEP_SECONDS = int(os.environ.get("RESET_PROJECT_SLEEP_SECS", "300"))
MAX_PHASE_RETRIES = int(os.environ.get("RESET_MAX_RETRIES", "3"))
RETRY_BACKOFF_SECONDS = [30, 90, 180]
MIN_PHASE_CHARS = 400  # matches tools/ingest.py's own MIN_PHASE_CHARS

# Self-repair: how many times a phase whose output fails its spec checks may be sent back
# with a corrective instruction before the pipeline gives up and flags it for review.
# Deliberately small -- each attempt is a full generation, and a model that ignores an
# explicit format correction twice is not going to comply on the fifth try either; that is
# a prompt bug to fix in reset/phase_NN_*.txt, not something to brute-force.
MAX_REPAIR_ATTEMPTS = int(os.environ.get("RESET_MAX_REPAIR_ATTEMPTS", "2"))
# Set RESET_DISABLE_REPAIR=1 to get the old behaviour (accept whatever comes back, let the
# post-run quality gate catch it) -- useful when isolating whether a repair loop is itself
# the thing making output worse.
REPAIR_ENABLED = os.environ.get("RESET_DISABLE_REPAIR", "") != "1"

_print_lock = threading.Lock()
_failures_lock = threading.Lock()
# Guards pipeline.run_ingest_extract_sync()'s subprocess chain specifically -- it
# reads/writes shared files (examples/CaseStudies/*.md via ingest.py, poc/*.json via
# build_json.py and every extract_*.py) that aren't safe for two projects to touch
# concurrently under --parallel > 1. Phase GENERATION (the API calls) stays fully parallel
# across projects; only this chain is serialized.
_pipeline_lock = threading.Lock()


def load_credentials() -> tuple:
    """(base_url, token, model) from the environment. Never logged, never persisted.

    The ANTHROPIC_* names are historical: this gateway is OpenAI-compatible at
    /v1/chat/completions, not an Anthropic Messages API endpoint (see api.extract_text).
    """
    return (
        os.environ.get("ANTHROPIC_BASE_URL"),
        os.environ.get("ANTHROPIC_AUTH_TOKEN"),
        os.environ.get("ANTHROPIC_MODEL"),
    )


def load_projects(path: Path = None) -> list:
    """Project queue, one name per line; blank lines and #-comments ignored."""
    path = path or (RESET_DIR / "projects.txt")
    lines = path.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]

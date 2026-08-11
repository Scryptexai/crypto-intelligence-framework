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
    (9, "behavioral"), (10, "knowledge"), (11, "conflict"), (12, "airdrop"),
]

# Phase 12 runs AFTER the Phase 11 audit, which means the audit does not cover it. That is a
# real gap, accepted deliberately: renumbering would rename 11-conflict.docx in 29 projects
# and invalidate every dossier already assembled. Phase 11's coverage report should be
# extended to reach phase 12 once the airdrop phase has run on enough projects to be worth
# auditing.

# FALLBACK ONLY since 2026-08-09. Phase 11 normally goes out as ONE prompt
# (reset/phase_11_conflict.txt) like every other phase; these four stages are reached only
# when streaming is off and no heavy-capable provider is configured -- see the gate comment
# in runner.run_project.
#
# The split was built for gateway 504s that turned out to be an artifact of non-streaming
# requests, and it carries a cost the timing argument never accounted for: stage 11d is told
# to merge every earlier stage's findings, and a model restating prior findings rewords them.
# In a validation report a reworded finding is indistinguishable from a second real one.
PHASE11_STAGES = [
    ("11a", "phase_11a_audit.txt", [(1, "foundation"), (2, "entity"), (3, "history")]),
    ("11b", "phase_11b_audit.txt", [(4, "technology"), (5, "financial")]),
    ("11c", "phase_11c_audit.txt", [(6, "token"), (7, "ecosystem"), (8, "market")]),
    ("11d", "phase_11d_scoring.txt", [(9, "behavioral"), (10, "knowledge")]),
]

# Phase 9 (Behavioral) is split into three sequential calls on the SAME running conversation,
# for the same reason Phase 11 is split into four: the gateway kills any single generation
# past ~300s (measured twice on Lido, 2026-08-08: HTTP 504 at 310s and 306s).
#
# What actually decides this is OUTPUT SIZE, not input. Measured across the 8 projects this
# script generated end to end (Arbitrum/LayerZero excluded -- they were researched by hand in
# a chat UI and never went through this gateway):
#
#   phase 09-behavioral   input 38,983 tok   output 8,436 tok   -> 504
#   phase 10-knowledge    input 45,459 tok   output 7,721 tok   -> succeeds
#
# Phase 10 carries MORE input and still finishes, so prefill is not the discriminator. Phase 9
# simply has the largest output of any phase, and at this backend's throughput that lands just
# past the wall: the only generation rate consistent with both facts is ~26-28 tok/s, which
# puts Phase 9 at 301-324s (over) and Phase 10 at 276-297s (just under). Splitting the output
# three ways gives ~2,800 tok per call, ~100-110s each -- comfortably inside.
#
# (An earlier revision of this comment blamed the ~58k-token prefill. That was inferred from
# Arbitrum's phase sizes, which are not this gateway's output at all; the table above is.)
PHASE9_STAGES = [
    ("9a", "phase_09a_objectives.txt"),
    ("9b", "phase_09b_patterns.txt"),
    ("9c", "phase_09c_risk.txt"),
]

# Stream responses (SSE) rather than waiting for one complete JSON body. This is what lifts
# the gateway's ~300s ceiling: a non-streaming request sends nothing until generation is
# finished, so the proxy's "no bytes received" timer fires and returns 504 mid-generation
# (measured on Lido at 310s and 306s). Streaming keeps data flowing from the first token, so
# the timer never fires and a phase may take as long as it needs -- bounded only by this
# client's REQUEST_TIMEOUT_SECONDS. Set RESET_NO_STREAM=1 to reproduce the old behaviour.
STREAM_RESPONSES = os.environ.get("RESET_NO_STREAM", "") != "1"

MAX_TOKENS = int(os.environ.get("RESET_MAX_TOKENS", "32000"))
# 32000 since 2026-08-12 (was 14000). A ceiling costs nothing when unused -- generation stops
# when the model is done, not when the budget runs out -- and 32000 is verified accepted by
# this gateway (probed 8000/16000/24000/32000, all fine, 2026-08-09). The old 14000 default
# made every verbose phase pay the truncation escalation instead: Berachain phase 07
# (2026-08-11) cut off at 14000, regenerated, cut off again at 21000 (91,761 chars), and only
# completed at 31500 -- two full throwaway generations (~13 min plus their tokens) for one
# phase, on a queue where most projects have at least one verbose phase. The escalation in
# api.call_with_retries stays as the safety net for answers that outrun even 32000.
# Phase 11b alone carries almost everything the old single-call Phase 11 produced (the real
# Arbitrum Phase 11 section is ~38.9k chars, ~9.7k tokens estimated -- already over the old
# 8192 default). Kept as its own constant so Phase 11's budget can move independently of the
# phases 1-10 default (both are 32000 now; the split predates that convergence).
# 32000, arrived at in two steps on 2026-08-09 as real sizes came in. Measured Phase 11
# output, at ~3.3 chars/token:
#
#   Aave           30,707 chars   ~9,300 tok    39% of 24000
#   Arbitrum       38,900 chars  ~11,800 tok    49%
#   Aptos          53,164 chars  ~16,100 tok    67%   -- truncated under the original 16000
#   Axie Infinity  72,441 chars  ~22,000 tok    92%   -- first clean pass, but only just
#
# 16000 was the original and Aptos ran straight past it, stopping mid-field at "Evidence
# Count: 8" before CIF SCORE CALCULATION, which the prompt places at the very end. 24000 then
# let Axie Infinity through -- while consuming 92% of the budget. Reports vary 2.4x in length
# across four projects with no relationship to project size, so betting the next one stays
# under 24000 is a bet with 23 more chances to lose.
#
# A ceiling costs nothing when unused: generation stops when the model is done, not when the
# budget runs out. 32000 was verified accepted by this gateway (probed alongside 8000/16000/
# 24000, all four fine), so the higher value is free headroom rather than a guess.
PHASE11_MAX_TOKENS = int(os.environ.get("RESET_PHASE11_MAX_TOKENS", "32000"))
# Hard stop for api.call_with_retries' truncation escalation: a cut-off answer is retried
# with 1.5x the budget rather than the same one, but never past this. 48000 is one escalation
# step above the Phase 11 default of 32000 and 1.5x the largest value the gateway was probed
# with successfully (8000/16000/24000/32000 all accepted, 2026-08-09) -- far enough to rescue
# a long report, close enough that an endpoint which silently caps lower still gets a value
# it recognises.
MAX_TOKENS_CEILING = int(os.environ.get("RESET_MAX_TOKENS_CEILING", "48000"))
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


class Provider:
    """One model endpoint the pipeline can send a phase to.

    `heavy_capable` marks a provider that can complete a big single call -- roughly 60k input
    plus 8k output -- inside its own timeout. The shared gateway cannot (measured: it kills
    any generation past ~300s), which is why phases 9 and 11 are staged there. A provider with
    this flag gets the whole phase in ONE call instead, which is both faster and avoids
    re-paying the ~58k-token prefill once per stage.
    """

    def __init__(self, name, base_url, token, model, heavy_capable=False):
        self.name = name
        self.base_url = base_url
        self.token = token
        self.model = model
        self.heavy_capable = heavy_capable

    def __repr__(self):
        return f"<Provider {self.name} model={self.model} heavy={self.heavy_capable}>"


def load_credentials() -> tuple:
    """(base_url, token, model) for the PRIMARY provider. Never logged, never persisted.

    The ANTHROPIC_* names are historical: this gateway is OpenAI-compatible at
    /v1/chat/completions, not an Anthropic Messages API endpoint (see api.extract_text).
    """
    return (
        os.environ.get("ANTHROPIC_BASE_URL"),
        os.environ.get("ANTHROPIC_AUTH_TOKEN"),
        os.environ.get("ANTHROPIC_MODEL"),
    )


def load_providers() -> list:
    """The provider chain, in the order calls are attempted.

    [0] is always the primary gateway -- cheap/free, and the maintainer's explicit rule is to
    exhaust it before spending on anything else. A second provider is appended only when
    DEEPSEEK_API_KEY is set, and is used purely as an escape hatch: api.call_with_retries
    rotates to it when the primary returns a capacity-class failure (gateway timeout, payload
    too large, context length exceeded) -- the failures that retrying the same endpoint cannot
    fix. Ordinary transient errors never trigger a rotation.

    Set DEEPSEEK_BASE_URL / DEEPSEEK_MODEL to point at something other than the official API.
    """
    base_url, token, model = load_credentials()
    providers = [Provider("gateway", base_url, token, model, heavy_capable=False)]

    ds_key = os.environ.get("DEEPSEEK_API_KEY")
    if ds_key:
        providers.append(Provider(
            name="deepseek",
            base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
            token=ds_key,
            model=os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"),
            heavy_capable=True,
        ))
    return providers


# Which provider leads for a given phase. The shared gateway is free but slow and unstable
# (measured 2026-08-09: 62s for a one-word completion, connection aborts mid-generation), so
# the paid endpoint earns its place on the phases where a dropped connection is most
# expensive -- Phase 11 costs 6-17 minutes of generation to lose.
#
#   RESET_PAID_PHASES=11        (default) paid provider leads on Phase 11 only
#   RESET_PAID_PHASES=all       every phase -- what a cost-measurement run wants
#   RESET_PAID_PHASES=none      never; paid stays a capacity-failure fallback as before
#
# Only takes effect when DEEPSEEK_API_KEY is set. The other provider always remains in the
# chain as a fallback, so a lead provider failing still rotates rather than ending the phase.
PAID_PHASES = os.environ.get("RESET_PAID_PHASES", "11").strip().lower()


def providers_for_phase(num: int, providers: list) -> list:
    """The provider chain for one phase, most-preferred first.

    Reorders rather than filters: whichever provider does not lead is still available as a
    fallback. That matters because the two fail in different ways -- the free gateway drops
    connections, and a paid endpoint can run out of credit -- and neither should be able to
    end a phase on its own while the other is reachable.
    """
    if len(providers) < 2 or PAID_PHASES == "none":
        return providers
    if PAID_PHASES == "all":
        wanted = True
    else:
        try:
            wanted = num in {int(p) for p in PAID_PHASES.split(",") if p.strip()}
        except ValueError:
            wanted = False
    if not wanted:
        return providers
    paid = [p for p in providers if p.name != "gateway"]
    free = [p for p in providers if p.name == "gateway"]
    return paid + free if paid else providers


def load_projects(path: Path = None) -> list:
    """Project queue, one name per line; blank lines and #-comments ignored."""
    path = path or (RESET_DIR / "projects.txt")
    lines = path.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]

"""
costs.py — token accounting for a run, and the cost estimate derived from it.

Tokens are MEASURED (read off each response's `usage` block); money is DERIVED (tokens
multiplied by a per-million rate you set). The two are kept apart on purpose: the token
counts are facts from the API, the rates are a published price list that changes and that
this repo has no way to verify. Never present the dollar figure as anything but an estimate
computed from the rates in the environment.

Rates come from RESET_PRICE_IN / RESET_PRICE_OUT (USD per 1M tokens), per provider name via
RESET_PRICE_IN_<PROVIDER>. Set them to whatever the provider publishes today; leave them
unset and the report still gives exact token counts with no dollar column.

Written to reset/cost_report.json after every run, appended per (provider, model, phase) so
a later run adds to the picture rather than replacing it.
"""
import json
import os
import threading
from datetime import datetime, timezone

from . import config

_lock = threading.Lock()
_entries = []  # one dict per API call in THIS process


def _rate(kind: str, provider: str):
    """USD per 1M tokens for this provider, or None when not configured."""
    specific = os.environ.get(f"RESET_PRICE_{kind}_{provider.upper()}")
    generic = os.environ.get(f"RESET_PRICE_{kind}")
    value = specific or generic
    try:
        return float(value) if value else None
    except ValueError:
        return None


def record(provider: str, model: str, label: str, usage: dict, text_len: int) -> None:
    """Log one call's token use.

    `usage` is the API's own block when it sent one. Gateways that omit it leave us
    estimating from the response length, which is flagged as such in the report -- an
    estimate that says so is useful; one that pretends to be measured is not.
    """
    prompt_t = completion_t = None
    estimated = True
    if isinstance(usage, dict):
        prompt_t = usage.get("prompt_tokens")
        completion_t = usage.get("completion_tokens")
        estimated = prompt_t is None and completion_t is None
    if completion_t is None:
        # 2.95 chars/token, measured 2026-08-09: Blur hit a 24,000-token cap at exactly
        # 70,499 chars (2.94) and Axie Infinity finished at 72,441 under the same cap
        # (>=3.02). Only used when the provider sends no usage block.
        completion_t = round(text_len / 2.95)
    with _lock:
        _entries.append({
            "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "provider": provider, "model": model, "label": label,
            "prompt_tokens": prompt_t, "completion_tokens": completion_t,
            "chars": text_len, "estimated": estimated,
        })


def summary() -> dict:
    with _lock:
        entries = list(_entries)
    by_provider = {}
    for e in entries:
        key = f"{e['provider']}/{e['model']}"
        agg = by_provider.setdefault(key, {
            "provider": e["provider"], "model": e["model"], "calls": 0,
            "prompt_tokens": 0, "completion_tokens": 0, "chars": 0,
            "estimated_calls": 0,
        })
        agg["calls"] += 1
        agg["prompt_tokens"] += e["prompt_tokens"] or 0
        agg["completion_tokens"] += e["completion_tokens"] or 0
        agg["chars"] += e["chars"]
        agg["estimated_calls"] += 1 if e["estimated"] else 0

    total_usd = 0.0
    priced = False
    for agg in by_provider.values():
        rin, rout = _rate("IN", agg["provider"]), _rate("OUT", agg["provider"])
        if rin is None and rout is None:
            agg["usd"] = None
            continue
        priced = True
        agg["usd"] = round(agg["prompt_tokens"] / 1e6 * (rin or 0)
                           + agg["completion_tokens"] / 1e6 * (rout or 0), 4)
        total_usd += agg["usd"]

    return {
        "calls": len(entries),
        "by_provider": list(by_provider.values()),
        "total_usd": round(total_usd, 4) if priced else None,
        "note": ("token counts are measured from each response's usage block (or estimated "
                 "from length where the provider sent none -- see estimated_calls); the USD "
                 "figure is those counts multiplied by RESET_PRICE_IN/RESET_PRICE_OUT and is "
                 "only as current as the rates you set"),
    }


def write_report() -> dict:
    """Merge this process's calls into reset/cost_report.json and return the run summary."""
    run = summary()
    if not run["calls"]:
        return run
    path = config.RESET_DIR / "cost_report.json"
    try:
        history = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"runs": []}
    except (json.JSONDecodeError, OSError):
        history = {"runs": []}
    history.setdefault("runs", []).append(
        {"finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), **run})
    with _lock:
        history["last_run_calls"] = list(_entries)
    path.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return run


def format_summary(run: dict) -> str:
    if not run["calls"]:
        return "no API calls made -- nothing to cost"
    lines = [f"API usage this run: {run['calls']} call(s)"]
    for agg in run["by_provider"]:
        usd = f" ≈ ${agg['usd']}" if agg.get("usd") is not None else " (no rates set)"
        est = (f", {agg['estimated_calls']} without a usage block (length-estimated)"
               if agg["estimated_calls"] else "")
        lines.append(f"  {agg['provider']}/{agg['model']}: {agg['calls']} calls, "
                     f"in {agg['prompt_tokens']:,} tok, out {agg['completion_tokens']:,} tok"
                     f"{usd}{est}")
    if run["total_usd"] is not None:
        lines.append(f"  total ≈ ${run['total_usd']} "
                     f"(rates from RESET_PRICE_IN/RESET_PRICE_OUT)")
    else:
        lines.append("  set RESET_PRICE_IN / RESET_PRICE_OUT (USD per 1M tokens) for a "
                     "dollar figure; token counts above are exact")
    lines.append(f"  detail appended to {(config.RESET_DIR / 'cost_report.json')}")
    return "\n".join(lines)

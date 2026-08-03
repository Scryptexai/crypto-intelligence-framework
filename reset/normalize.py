#!/usr/bin/env python3
"""
normalize.py — convert a research model's answer into the PLAIN-TEXT shape the CIF
extractors (tools/extract_*.py) expect.

Why: the extractors were tuned to the original DeepSeek run's plain-text output
(examples: 'Core Insights' as a bare line, 'Insight 1:' items, '· Confidence: High').
Some model/proxy backends (e.g. nemotron served behind the DeepSeek-labelled proxy)
answer in Markdown ('## Core Insights', '### Knowledge 1:', '**Confidence**'), which
the extractors don't match — yielding 0 parsed items. This deterministic pass strips
Markdown decorations and realigns section item labels so the same content parses.
"""
from __future__ import annotations
import re

# Section header -> the item word the extractor expects under it (extract_knowledge.SECTIONS).
_ITEM_WORD = {
    "Core Insights": "Insight",
    "Strategic Principles": "Principle",
    "Success Factors": "Factor",
    "Failure Factors": "Factor",
    "Decision Framework": "Step",
    "Reusable Playbook": "Playbook",
    "Anti-patterns": "Anti-pattern",
}
_SECTION_HEADERS = list(_ITEM_WORD.keys()) + ["Lessons Learned", "Knowledge Summary"]


def strip_markdown(text: str) -> str:
    out = []
    for line in text.splitlines():
        s = line
        # headers: leading #..###### -> plain
        s = re.sub(r"^\s{0,3}#{1,6}\s+", "", s)
        # bold/italic markers
        s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
        s = re.sub(r"__(.+?)__", r"\1", s)
        s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"\1", s)
        # markdown bull[- *] at line start -> "· " (extractors read "·" bullets)
        s = re.sub(r"^\s{0,3}[-*]\s+", "· ", s)
        # trailing markdown table pipes / stray backticks
        s = s.replace("`", "")
        out.append(s)
    return "\n".join(out)


def realign_knowledge_labels(text: str) -> str:
    """Under each known section, rename generic 'Knowledge N:' / '<word> N:' items to the
    exact item word the extractor wants (e.g. 'Insight 1:' under 'Core Insights'). Only
    touches lines that are clearly item headers; leaves everything else untouched."""
    lines = text.splitlines()
    current = None
    item_re = re.compile(r"^\s*(?:Knowledge|Insight|Principle|Factor|Step|Playbook|Anti-?pattern|Item)\s+(\d+)\s*:\s*(.*)$", re.I)
    for i, ln in enumerate(lines):
        bare = ln.strip()
        if bare in _ITEM_WORD:
            current = bare
            continue
        if bare in ("Lessons Learned", "Knowledge Summary", "Open Threads"):
            current = None
            continue
        if current:
            m = item_re.match(ln)
            if m:
                word = _ITEM_WORD[current]
                lines[i] = f"{word} {m.group(1)}: {m.group(2)}".rstrip()
    return "\n".join(lines)


def normalize(text: str) -> str:
    return realign_knowledge_labels(strip_markdown(text)).strip() + "\n"

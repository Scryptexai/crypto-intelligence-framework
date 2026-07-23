#!/usr/bin/env python3
"""
build_json.py — CIF knowledge (markdown) -> structured data for apps/PoC.

Deterministic, no LLM/API. Reads the repo's source-of-truth markdown and emits:
  poc/projects.json   — project roster (from examples/DatasetIndex.md) + content-derived tags
  poc/patterns.json   — pattern catalogue (from examples/PatternRegistry.md)
  poc/data.js         — window.CIF = {projects, patterns, meta}  (for file:// PoC, no server)

Run from repo root:  python3 tools/build_json.py
"""
import json, re, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
INDEX = EXAMPLES / "DatasetIndex.md"
PATTERNS_MD = EXAMPLES / "PatternRegistry.md"
OUT = ROOT / "poc"

# ---- keyword -> tag map (scanned against each project's file content) ----
KEYWORD_TAGS = [
    (r"\bair ?drop\b|retroactive|retro-airdrop", "airdrop"),
    (r"\bpoints?\b|shards|sats\b", "points"),
    (r"incentiviz(ed|e) testnet|blockspace race|testnet incentive", "testnet-incentive"),
    (r"liquid restaking|\blrt\b|eeth|ezeth", "lrt"),
    (r"liquid restaking|\blrt\b", "liquid-restaking"),
    (r"restak", "restaking"),
    (r"liquid staking|steth|wsteth|\blsd\b|\blst\b", "liquid-staking"),
    (r"looping|collateral loop|rehypothec", "looping"),
    (r"multi-token|multi token|three token|3 token|hnt.*iot.*mobile", "multi-token"),
    (r"eip-1559|fee burn|\bburn\b", "fee-burn"),
    (r"first mover|first-mover|pioneer", "first-mover"),
    (r"\bamm\b|automated market maker|constant product", "amm"),
    (r"perpetual|\bperps?\b", "perps"),
    (r"modular|data availability|\bnmt\b|blobs?\b", "modular"),
    (r"\boracle\b", "oracle"),
    (r"bridge|interoper|omnichain|cross-chain", "bridge"),
    (r"stablecoin|\bcdp\b|soft-peg|delta-neutral", "stablecoin"),
    (r"delta-neutral|synthetic", "synthetic"),
    (r"\bmeme\b", "meme"),
    (r"\bnft\b", "nft-community"),
    (r"governance|\bdao\b|voting", "governance"),
    (r"sybil", "sybil"),
    (r"mining|proof-of-coverage|hotspot", "mining"),
    (r"\bdepin\b", "depin"),
    (r"monolithic|sealevel|proof of history", "monolithic"),
    (r"restaking|shared security|\bavs\b", "shared-security"),
    (r"pivot|reorganiz|rebrand", "pivot"),
    (r"migrat", "migration"),
    (r"op stack|rollup|layer 2|\bl2\b", "l2"),
    (r"layer 1|\bl1\b", "l1"),
]

CAT_TAGS = {
    "Layer 1": ["l1"], "Layer 0": ["l1"], "Layer 2": ["l2"], "DeFi": ["defi"],
    "Liquid Staking": ["liquid-staking", "efficiency"],
    "Restaking / LRT": ["restaking", "lrt", "efficiency"], "Infrastructure / Restaking": ["restaking", "efficiency"],
    "Modular / Data Availability": ["modular", "da"], "Modular / DA": ["modular", "da"],
    "Oracle": ["oracle", "infra"], "Bridge / Interoperability": ["bridge", "interop"],
    "Bridge / Interop": ["bridge", "interop"], "Stablecoin": ["stablecoin"],
    "Perps / DEX": ["defi", "perps"], "DePIN": ["depin"], "Social": ["social"],
    "NFT / Gaming": ["nft-community"], "Identity": ["identity"], "Wallet / Account Abstraction": ["wallet"],
}

def norm(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())

def cat_tags(cat):
    for key, tags in CAT_TAGS.items():
        if cat.strip().lower().startswith(key.lower()):
            return list(tags)
    # loose fallbacks
    c = cat.lower()
    out = []
    if "defi" in c: out.append("defi")
    if "layer 1" in c or "l1" in c: out.append("l1")
    if "layer 2" in c or "l2" in c: out.append("l2")
    return out

def derive_tags(text):
    t = text.lower()
    tags = []
    for pat, tag in KEYWORD_TAGS:
        if re.search(pat, t) and tag not in tags:
            tags.append(tag)
    return tags

def parse_index():
    """Parse examples/DatasetIndex.md tables into a de-duped project roster (Deep wins over Summary)."""
    rows = INDEX.read_text(encoding="utf-8").splitlines()
    projects = {}
    path_re = re.compile(r"([A-Za-z0-9_./-]+\.md)")
    for ln in rows:
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 4:
            continue
        idc = cells[0]
        # roster rows have an id like D1 / 1 / 12 in the first column
        if not re.match(r"^(D?\d+)$", idc):
            continue
        m = path_re.search(s)
        if not m:
            continue
        fpath = m.group(1)
        # only project files, not analyses
        if "Analysis" in fpath or "Registry" in fpath:
            continue
        if fpath.startswith("CaseStudies/"):
            tier = "Deep"
        elif fpath.startswith("Pioneer/"):
            tier = "Summary"
        else:
            continue
        name = cells[1]
        cat = cells[2] if len(cells) > 2 else ""
        era = cells[3] if len(cells) > 3 else ""
        key = norm(name)
        # Deep wins; don't overwrite a Deep with a Summary
        if key in projects and projects[key]["tier"] == "Deep":
            continue
        full = EXAMPLES / fpath
        tags = list(cat_tags(cat))
        if full.exists():
            content = full.read_text(encoding="utf-8")
            # Deep dossiers discuss the whole ecosystem; scan only the project's own
            # identity/innovation region (top of file) so tags describe THIS project,
            # not everything it mentions. Summaries are short → scan whole.
            scan = content[:2200] if tier == "Deep" else content
            for tg in derive_tags(scan):
                if tg not in tags:
                    tags.append(tg)
        projects[key] = {"n": name, "tier": tier, "file": f"examples/{fpath}",
                         "cat": cat, "era": era, "tags": tags}
    return list(projects.values())

def discover_dossiers(existing):
    """Filesystem discovery: any examples/CaseStudies/<Project>.md dossier is picked up
    automatically (so ingest.py never has to edit DatasetIndex.md). Index entries win
    for category/era; files only add projects the index missed."""
    cs = EXAMPLES / "CaseStudies"
    have = {norm(p["n"]) for p in existing}
    have_files = {p["file"] for p in existing}   # dedup by path — robust to H1/index name drift
    added = []
    for f in sorted(cs.glob("*.md")):
        nm = f.name
        if nm == "README.md" or "Analysis" in nm or "Registry" in nm:
            continue
        rel = f"examples/CaseStudies/{nm}"
        if rel in have_files:
            continue
        content = f.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", content, re.M)
        name = (m.group(1).strip() if m else f.stem)
        if norm(name) in have:
            continue
        # category: from a "Category:" line if present, else blank
        cm = re.search(r"\*\*Category:\*\*\s*(.+)", content)
        cat = cm.group(1).strip() if cm else ""
        tags = list(cat_tags(cat)) if cat else []
        for tg in derive_tags(content[:2200]):
            if tg not in tags:
                tags.append(tg)
        existing.append({"n": name, "tier": "Deep", "file": f"examples/CaseStudies/{nm}",
                         "cat": cat, "era": "", "tags": tags})
        have.add(norm(name)); added.append(name)
    return added


def discover_sentiment(projects):
    """Discover sentiment companion dossiers in examples/Sentiment/ and link them to projects."""
    sd = EXAMPLES / "Sentiment"
    out = []
    if not sd.exists():
        return out
    byname = {norm(p["n"]): p for p in projects}
    for f in sorted(sd.glob("*.md")):
        if f.name == "README.md":
            continue
        content = f.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", content, re.M)
        name = m.group(1).strip() if m else f.stem
        rel = f"examples/Sentiment/{f.name}"
        out.append({"project": name, "file": rel})
        p = byname.get(norm(name))
        if p is not None:
            p["sentiment"] = rel
    return out


def parse_patterns():
    txt = PATTERNS_MD.read_text(encoding="utf-8")
    pats = []
    blocks = re.split(r"^##\s+", txt, flags=re.M)[1:]
    for b in blocks:
        head, *rest = b.splitlines()
        m = re.match(r"(P\d+)\s*·\s*(.+)", head.strip())
        if not m:
            continue
        pid, nm = m.group(1), m.group(2).strip()
        fields = {}
        for line in rest:
            lm = re.match(r"-\s*([a-zA-Z]+):\s*(.*)", line.strip())
            if lm:
                fields[lm.group(1).lower()] = lm.group(2).strip()
        def clist(v, sep=","):
            return [x.strip() for x in v.split(sep) if x.strip()] if v else []
        inst = int(fields.get("instances", "1") or "1")
        pats.append({
            "id": pid, "nm": nm,
            "triggers": clist(fields.get("triggers", "")),
            "instances": inst,
            "confidence": "HIGH" if inst >= 3 else ("MEDIUM" if inst == 2 else "LOW"),
            "analogs": clist(fields.get("analogs", "")),
            "src": fields.get("source", ""),
            "val": fields.get("validated", "") or "",
            "pred": fields.get("prediction", ""),
            "watch": clist(fields.get("watch", ""), ";"),
            "scope": fields.get("scope", ""),
        })
    return pats

def main():
    if not INDEX.exists():
        sys.exit("DatasetIndex.md not found — run from repo root.")
    projects = parse_index()
    discovered = discover_dossiers(projects)
    sentiment = discover_sentiment(projects)
    patterns = parse_patterns()
    OUT.mkdir(exist_ok=True)
    meta = {
        "schema": "cif-export/1",
        "generated": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "projects": len(projects),
        "deep": sum(1 for p in projects if p["tier"] == "Deep"),
        "summary": sum(1 for p in projects if p["tier"] == "Summary"),
        "sentiment": len(sentiment),
        "patterns": len(patterns),
        "source": "examples/DatasetIndex.md + examples/PatternRegistry.md + examples/Sentiment/",
    }
    (OUT / "projects.json").write_text(json.dumps(projects, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "patterns.json").write_text(json.dumps(patterns, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "sentiment.json").write_text(json.dumps(sentiment, ensure_ascii=False, indent=2), encoding="utf-8")
    bundle = {"meta": meta, "projects": projects, "patterns": patterns, "sentiment": sentiment}
    # cif.json — single self-describing bundle for LLMs / apps needing tracking·signal·prediction data
    (OUT / "cif.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "data.js").write_text(
        "// AUTO-GENERATED by tools/build_json.py — do not edit by hand.\n"
        "window.CIF = " + json.dumps(bundle, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8")
    print(f"[build_json] {meta['projects']} projects ({meta['deep']} deep, {meta['summary']} summary), "
          f"{meta['sentiment']} sentiment, {meta['patterns']} patterns "
          f"-> poc/cif.json, data.js, projects.json, patterns.json, sentiment.json")
    if discovered:
        print(f"[build_json] auto-discovered {len(discovered)} dossier(s) not in index: {', '.join(discovered)}")

if __name__ == "__main__":
    main()

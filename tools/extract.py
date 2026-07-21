#!/usr/bin/env python3
"""
extract.py — Deep-research source (.docx / .pdf) -> clean reflowed markdown.

Step 1 of the Ingest-Deep runbook. Deterministic, no LLM/API. Quality-preserving:
it only reflows the source text; the dossier synthesis stays human/LLM reasoning.

Design notes (why it works this way):
  - .docx is a ZIP of XML; text lives in <w:t> runs, paragraphs are <w:p>. We walk
    the body in document order and, crucially, reconstruct any Word TABLE
    (<w:tbl>/<w:tr>/<w:tc>) row-by-row so column<->row association is never lost
    (a flat <w:t> sweep scrambles tables — that is the failure this avoids).
  - .pdf uses pypdf.extract_text(). Some PDFs need the `cffi` backend for pypdf's
    crypto provider import; install it if extraction fails.
  - Citation chips ([span_12], start_span, [1] …) from grounded exports are stripped.
  - Numbered section titles ("N Title") are normalised to "## N Title" so the 23
    CIF sections are trivially detectable downstream.

Usage:
    python tools/extract.py INPUT.docx [-o OUTPUT.md]
    python tools/extract.py INPUT.pdf  [-o OUTPUT.md]
If -o is omitted the markdown is written to stdout.
"""
import argparse
import html
import re
import sys
import zipfile

# Canonical CIF section titles (substring match on numbered heading lines).
# Covers both the 23 deep-dossier sections and the 8 sentiment sections so the
# same normaliser detects headings for either document type.
SECTION_TITLES = [
    # deep (23)
    "Executive Summary", "Industry Background", "Project Origin", "Innovation Analysis",
    "Technology Evolution", "Funding Intelligence", "Community Intelligence",
    "Narrative Intelligence", "Competitive Landscape", "Product Evolution",
    "Tokenomics Intelligence", "Airdrop", "Token Lifecycle", "Business Intelligence",
    "Success", "Historical Timeline", "Current Status", "Lessons Learned",
    "Knowledge Extraction", "Transferable Intelligence", "Open Questions",
    "Evidence Level", "Karya yang dikutip",
    # sentiment (8)
    "Overview & Coverage", "Overview and Coverage", "Sentiment Timeline", "Community Voice",
    "Project Voice", "Divergence", "Engagement Authenticity", "Sentiment Patterns", "Provenance",
]

CHIP_RE = re.compile(r"\[span_\d+\]\((?:start|end)_span\)|\[span_\d+\]|start_span|end_span|\[\d+\]")


def _cell_text(tc_xml: str) -> str:
    runs = re.findall(r"<w:t\b[^>]*>(.*?)</w:t>", tc_xml, re.S)
    return html.unescape("".join(runs)).strip()


def _table_to_bullets(tbl_xml: str) -> list:
    """Render a Word table as row-preserving 'Header: Value' bullets (lossless)."""
    rows = []
    for tr in re.findall(r"<w:tr\b.*?>(.*?)</w:tr>", tbl_xml, re.S):
        cells = [_cell_text(tc) for tc in re.findall(r"<w:tc>(.*?)</w:tc>", tr, re.S)]
        if any(cells):
            rows.append(cells)
    if not rows:
        return []
    header = rows[0]
    out = []
    for row in rows[1:]:
        # pair each cell with its column header; falls back to positional label
        parts = []
        for i, val in enumerate(row):
            label = header[i] if i < len(header) and header[i] else f"Col{i+1}"
            parts.append(f"  - {label}: {val}")
        out.append(f"- {row[0]}")
        out.extend(parts[1:])
    return out


def extract_docx(path: str) -> str:
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    # Split body into ordered blocks: tables and paragraphs, preserving position.
    blocks = re.split(r"(<w:tbl>.*?</w:tbl>)", xml, flags=re.S)
    out = []
    for block in blocks:
        if block.startswith("<w:tbl>"):
            out.extend(_table_to_bullets(block))
        else:
            for para in re.split(r"</w:p>", block):
                txt = html.unescape("".join(re.findall(r"<w:t\b[^>]*>(.*?)</w:t>", para, re.S))).strip()
                if txt:
                    out.append(txt)
    return "\n\n".join(out)


def extract_pdf(path: str) -> str:
    try:
        import pypdf
    except ModuleNotFoundError:
        sys.exit("pypdf not installed. Run: pip install pypdf cffi")
    reader = pypdf.PdfReader(path)
    text = "\n".join((p.extract_text() or "") for p in reader.pages)
    text = re.sub(r"[ \t]*\n[ \t]*", " ", text)  # rejoin wrapped lines
    return text


def normalise(text: str) -> str:
    text = text.replace("\r", "")
    text = CHIP_RE.sub("", text)
    text = re.sub(r"\(\s*\)", "", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    paras = [p.strip() for p in re.split(r"\n{2,}", text) if p.strip()]
    out = []
    for p in paras:
        m = re.match(r"^#{0,3}\s*(\d{1,2})\s+(.+)$", p)
        if m and len(p) < 70 and any(t.lower() in p.lower() for t in SECTION_TITLES):
            out.append(f"\n## {m.group(1)} {m.group(2).strip()}")
        else:
            out.append(p)
    return re.sub(r"\n{3,}", "\n\n", "\n\n".join(out)).strip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract deep-research .docx/.pdf to clean markdown.")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", help="output .md path (default: stdout)")
    args = ap.parse_args()

    low = args.input.lower()
    if low.endswith(".docx"):
        raw = extract_docx(args.input)
    elif low.endswith(".pdf"):
        raw = extract_pdf(args.input)
    else:
        sys.exit("Unsupported input; expected .docx or .pdf")

    md = normalise(raw)
    sections = re.findall(r"^## .*", md, re.M)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(md)
        print(f"wrote {args.output} ({len(md)} chars, {len(sections)} sections detected)", file=sys.stderr)
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()

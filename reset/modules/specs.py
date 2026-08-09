"""
specs.py — what "correct output" means per phase, and how to ask for it again when it isn't.

This is the knowledge base behind the self-repair loop. Each check pairs a TEST (run the
real downstream parser, not an approximation) with a REPAIR HINT (the precise corrective
instruction to send back). Nothing here calls the API; repair.py drives the loop.

Design rule: a check must run the SAME code the database sync will run. Every format bug
this project has hit passed a looser proxy check and still extracted zero rows -- citation
density was green on all four of the phases that broke on 2026-08-05. So the tests below
import tools/extract_*.py directly rather than pattern-matching for "looks about right".

Adding a new check: append a Check to the relevant list in PHASE_CHECKS. Keep the hint
concrete (exact literal labels + a worked example); vague hints like "use the right format"
have to be paid for with a full regeneration and do not work.
"""
import re
from dataclasses import dataclass
from pathlib import Path

from . import config

import ingest as _ingest  # tools/ingest.py -- validate_phase_content, the assembled-dossier gate
import extract_entities as _extract_entities
import extract_events as _extract_events
import extract_decision_events as _extract_decision_events
import extract_knowledge as _extract_knowledge
import extract_behavior as _extract_behavior
import extract_qa as _extract_qa

# The `## <Title>` heading tools/ingest.py writes above each phase in the assembled dossier.
# The extractors slice on these, so a single phase checked in isolation has to be wrapped in
# the same shape or every parser returns nothing for reasons that have nothing to do with the
# phase's own content.
PHASE_TITLES = {
    "foundation": "Foundation Intelligence",
    "entity": "Entity Intelligence",
    "history": "Historical Intelligence",
    "technology": "Technology Intelligence",
    "financial": "Financial Intelligence",
    "token": "Token Intelligence",
    "ecosystem": "Ecosystem Intelligence",
    "market": "Market Intelligence",
    "behavioral": "Behavioral Intelligence",
    "knowledge": "Knowledge Extraction",
    "conflict": "Validation & Quality Assurance (CIF Score)",
}
# What each phase's slice is terminated BY in a real dossier -- the next phase's title.
_NEXT_TITLE = {
    "entity": "Historical Intelligence",
    "history": "Technology Intelligence",
    "behavioral": "Knowledge Extraction",
    "knowledge": "Validation & Quality Assurance (CIF Score)",
}


def wrap_for_extractor(text: str, key: str) -> str:
    """One phase's raw text, wrapped as the extractors expect to find it in a dossier."""
    body = re.sub(r"(?im)^PROJECT:.*\n", "", text, count=1)
    title = PHASE_TITLES.get(key, key.title())
    tail = _NEXT_TITLE.get(key, "Validation & Quality Assurance (CIF Score)")
    return f"## {title}\n_ref: x_\n\n{body}\n\n## {tail}\n"


def wrap_phase_file(proj_dir: Path, num: int, key: str) -> str:
    path = proj_dir / f"{num:02d}-{key}.docx"
    if not path.exists():
        return ""
    return wrap_for_extractor(path.read_text(encoding="utf-8"), key)


@dataclass
class Check:
    name: str          # short stable id, appears in repairs.log
    describe: str      # human summary for the console
    test: object       # (text, project_name) -> (ok: bool, detail: str)
    hint: str          # exact corrective instruction sent back to the model


# ---------------------------------------------------------------------------
# Universal checks -- applied to every phase 1-10.
# ---------------------------------------------------------------------------

# Whole phases have come back as leaked tool-call syntax or the model narrating the task
# instead of doing it: raw <tool_call>/<invoke> JSON (Cosmos phases 2-3, EigenLayer all of
# 1-8), "I'll search for..." repeated with zero findings (Berachain, every phase), and
# "The user wants me to produce Phase 6..." (Compound phase 6) / a decorative "MEMULAI
# PENELITIAN" banner with no content (Friend.tech phase 1). These sail past every
# format/citation check because there is no malformed data -- there is no data at all.
_JUNK_PATTERNS = [
    (r"<tool_call>|<invoke\s+name=|</?function_calls>|\.invoke\s*\(",
     "raw tool-call syntax leaked into the answer"),
    (r"(?im)^\s*(?:I'll|I will|Let me)\s+(?:search|research|gather|look|start|begin)\b",
     "search narration instead of research findings"),
    (r"(?im)^\s*The user (?:wants|asked|is asking)\b",
     "meta-commentary about the task instead of the answer"),
    (r"(?im)^\s*(?:█|▓|═){5,}",
     "decorative banner with no dataset content"),
]


def _check_no_junk(text: str, project_name: str) -> tuple:
    head = text[:4000]
    hits = [why for pat, why in _JUNK_PATTERNS if re.search(pat, head)]
    # Count narration lines across the whole body too: one stray "Let me check" mid-answer is
    # noise, twenty of them in a row IS the answer and means nothing was researched.
    narration = len(re.findall(
        r"(?im)^\s*(?:I'll|I will|Let me)\s+(?:search|research|gather)\b", text))
    if narration >= 3:
        hits.append(f"{narration} lines of search narration and no findings")
    if hits:
        return False, "; ".join(sorted(set(hits)))
    return True, ""


def _check_min_length(text: str, project_name: str) -> tuple:
    n = len(text.strip())
    if n < config.MIN_PHASE_CHARS:
        return False, f"only {n} chars (minimum {config.MIN_PHASE_CHARS})"
    return True, ""


def _check_ingest_contract(text: str, project_name: str) -> tuple:
    """Delegates to tools/ingest.py's own validate_phase_content -- the gate that will reject
    this phase at assembly time. Running it here means a fixable rejection costs one repair
    round now instead of a whole project failing at the end of an unattended run."""
    reasons = _ingest.validate_phase_content("check.docx", project_name, text)
    if reasons:
        return False, "; ".join(reasons)
    return True, ""


_UNIVERSAL = [
    Check("no_junk", "real research content (not tool-call syntax or narration)", _check_no_junk,
          "Jawaban sebelumnya TIDAK berisi hasil riset — hanya berisi narasi pencarian, "
          "sintaks tool-call, atau komentar tentang tugas. JANGAN tulis kalimat seperti "
          "\"I'll search for...\", \"Let me research...\", \"The user wants me to...\", "
          "JANGAN tampilkan <tool_call> / <invoke ...>, dan JANGAN buat banner dekoratif. "
          "Tulis LANGSUNG isi dataset final sesuai template: fakta konkret dengan angka, "
          "tanggal, nama entity, dan sitasi per fakta. Jika suatu fakta benar-benar tidak "
          "dapat diverifikasi, tulis \"Tidak diketahui\" pada field itu — bukan narasi."),
    Check("min_length", "substantial content", _check_min_length,
          "Jawaban sebelumnya terlalu pendek untuk sebuah laporan phase. Lengkapi SELURUH "
          "field/section yang diminta template, jangan berhenti di tengah."),
    Check("ingest_contract", "PROJECT header + citation density", _check_ingest_contract,
          "Jawaban sebelumnya gagal verifikasi kontrak dataset. Wajib: (a) baris pertama "
          "\"PROJECT: <Nama Project>\"; (b) setiap fakta punya sitasi — pakai tag "
          "(HIGH)/(MEDIUM)/(LOW), atau minimal 3 baris \"Sources:\" berisi URL lengkap "
          "https://..., atau minimal 3 sitasi internal 【Phase N — Section】; (c) jangan pakai "
          "placeholder \"[sumber tidak dapat diverifikasi ulang]\" untuk mayoritas fakta."),
]


# ---------------------------------------------------------------------------
# Per-phase machine-format checks -- these run the real extractors.
# ---------------------------------------------------------------------------

def _check_entities(text: str, project_name: str) -> tuple:
    wrapped = wrap_for_extractor(text, "entity")
    rows = (_extract_entities.parse_entities(wrapped, project_name)
            or _extract_entities.parse_entities_block(wrapped, project_name))
    if not rows:
        return False, "extract_entities parsed 0 entities"
    return True, f"{len(rows)} entities"


def _check_events(text: str, project_name: str) -> tuple:
    wrapped = wrap_for_extractor(text, "history")
    rows = _extract_events.parse_events(wrapped, project_name.lower())
    if not rows:
        return False, "extract_events parsed 0 events"
    return True, f"{len(rows)} events"


def _check_decisions(text: str, project_name: str) -> tuple:
    rows = _extract_decision_events.parse_keputusan_events(text, project_name)
    if not rows:
        return False, "extract_decision_events parsed 0 Keputusan blocks"
    return True, f"{len(rows)} decision events"


def _check_behavior_sections(text: str, project_name: str) -> tuple:
    wrapped = wrap_for_extractor(text, "behavioral")
    prof = _extract_behavior.parse_behavior(wrapped, project_name)
    empty = [k for k in ("strategicObjectives", "decisionPatterns", "riskResponse", "tradeOffs")
             if not prof.get(k)]
    if empty:
        return False, f"empty after parsing: {', '.join(empty)}"
    return True, ", ".join(f"{k}={len(prof[k])}" for k in prof if isinstance(prof[k], list))


def _check_knowledge(text: str, project_name: str) -> tuple:
    wrapped = wrap_for_extractor(text, "knowledge")
    rows = _extract_knowledge.parse_knowledge(wrapped, project_name)
    if not rows:
        return False, "extract_knowledge parsed 0 items"
    return True, f"{len(rows)} knowledge items"


def _check_qa_parse(text: str, project_name: str) -> tuple:
    """extract_qa.parse_qa returns None for two very different reasons, so say which.

    The first version reported both as "no CIF Score Calculation block", which sent the
    diagnosis in the wrong direction on Aave: the block was missing because the report was cut
    off, not because the model formatted it wrong. The detail line now reports what IS in the
    text -- how many 'Kontribusi:' lines, which dimension labels appear, whether the text ends
    mid-sentence -- so the next failure is readable without opening the file.
    """
    wrapped = wrap_for_extractor(text, "conflict")
    res = _extract_qa.parse_qa(wrapped, project_name)
    if res is not None and res.get("dimensions"):
        return True, (f"total={res['total']} {len(res['dimensions'])} dimensions "
                      f"{len(res.get('phases') or [])} phases")

    kontribusi = len(re.findall(r"(?im)^\s*Kontribusi:", text))
    labels = [d for d in _extract_qa.DIMENSION_KEYS if re.search(rf"(?m)^\s*{re.escape(d)}\s*\(",
                                                                 text)]
    tail = text.rstrip()[-60:].replace("\n", " ")
    looks_cut = not text.rstrip().endswith((".", "!", "?", "|", "-", ")", "]"))
    return False, (
        f"extract_qa parsed 0 dimensions -- 'Kontribusi:' lines={kontribusi}, "
        f"dimension headings found={labels or 'none'}, "
        f"{'text ends mid-sentence (likely truncated): ' if looks_cut else 'ends at: '}"
        f"...{tail!r}")


def _check_no_md_headers(text: str, project_name: str) -> tuple:
    """`## ` anywhere in Phase 11's body silently truncates it.

    tools/ingest.py assembles each phase under its own `## <title>` heading, and
    extract_qa.py bounds the section with `(?=\\n## |\\Z)`. A `## ` the model adds inside the
    report therefore ends the section early: everything after it -- Conflict Register,
    Evidence Audit, sometimes the score itself -- is dropped with no error anywhere. Same
    failure that cost Phase 9 its Decision Timeline. Arbitrum's real Phase 11 has zero.
    """
    bad = re.findall(r"(?m)^(#{2,6}\s+\S.*)$", text)
    if bad:
        return False, f"{len(bad)} markdown header line(s), first: {bad[0][:60]!r}"
    return True, "no markdown headers"


_QA_HINT = (
    "Laporan Phase 11 tidak terbaca oleh parser CIF Score. Perbaiki DUA hal:\n"
    "1. WAJIB ada bagian berjudul persis `CIF SCORE CALCULATION` (huruf besar semua), dan di "
    "dalamnya setiap dimensi ditulis sebagai `<Nama Dimensi> (<bobot>%)` pada barisnya sendiri, "
    "diakhiri baris `Kontribusi: <skor> × <bobot> = <hasil>`. Contoh persis:\n"
    "Research Quality (25%)\n"
    "- <detail penilaian>\n"
    "Kontribusi: 8.5 × 0.25 = 2.13\n"
    "2. JANGAN pernah memakai heading markdown (`##`, `###`) di mana pun dalam laporan. "
    "Gunakan baris teks huruf besar biasa sebagai judul bagian, seperti `COVERAGE REPORT` dan "
    "`CONFLICT REGISTER`. Satu baris `## ` saja akan memotong laporan ini di tengah dan "
    "membuang semua isi setelahnya."
)


_ENTITY_HINT = (
    "Format blok ENTITY salah sehingga tidak terparsing. Tulis SETIAP entity sebagai blok "
    "flat text, label BAHASA INGGRIS persis ini, satu field per baris, dipisah \"---\" "
    "antar-entity. JANGAN pakai heading markdown, bold, bullet, atau label Indonesia:\n\n"
    "Entity: <Nama>\nType: <Person|Organization|Foundation|Investor|Protocol|DAO|Exchange|...>\n"
    "Relationship: <peran/hubungan ke project, boleh panjang>\nPeriod: <2021–sekarang>\n"
    "Exposure Type: <technical-integration|investment|governance|...>\n"
    "Evidence: (HIGH) [Nama Sumber, https://...]; [Nama Sumber, https://...]\n---"
)
_HISTORY_HINT = (
    "Format blok EVENT salah sehingga tidak terparsing. Tulis SETIAP event dengan LABEL "
    "SENDIRIAN di satu baris, lalu BARIS KOSONG, lalu isinya di baris berikutnya. Dipisah "
    "\"---\" antar-event. BUKAN \"Label: isi\" satu baris, BUKAN heading markdown, BUKAN bold:\n\n"
    "Event ID\n\nEV-001\n\nDate\n\n2021-08-31\n\nEvent Name\n\n<nama singkat>\n\nEvent Type\n\n"
    "Founding\n\nDescription\n\n<maks 3 kalimat fakta>\n\nParticipants\n\n<Entity A; Entity B>\n\n"
    "Location\n\n<lokasi atau Tidak diketahui>\n\nStatus\n\nCompleted\n\nImmediate Result\n\n"
    "<hasil langsung>\n\nSources\n\nhttps://...\n\n---"
)
_DECISION_HINT = (
    "Section \"Decision Timeline\" tidak terparsing. Setiap keputusan WAJIB diawali literal "
    "\"Keputusan:\" (bukan \"Decision:\"), judul singkat, lalu tanggal dalam kurung di akhir "
    "baris; field di bawahnya diawali bullet titik-tengah \"· \" dengan label PERSIS dan "
    "berurutan:\n\n"
    "Keputusan: <judul singkat> (2023-11)\n"
    "· Trigger: <pemicu>\n· Evidence: <bukti/sitasi>\n· Decision: <apa yang diputuskan>\n"
    "· Immediate Result: <hasil langsung>\n· Long-term Impact: <dampak jangka panjang>\n"
    "· Supporting Dataset: <Phase 3 EV-001, dll>"
)
_BEHAVIOR_HINT = (
    "Section-section Behavioral tidak terparsing. Penyebab paling sering (dan yang kemungkinan "
    "besar terjadi di jawaban sebelumnya): item \"Pola 1: ...\" sudah ditulis dengan benar, "
    "TAPI BARIS NAMA SECTION di atasnya HILANG — diganti garis pemisah \"---\" atau tidak "
    "ditulis sama sekali. Penomoran \"Pola\" dimulai ulang dari 1 di tiap section, jadi tanpa "
    "baris nama section, enam blok \"Pola 1..N\" yang berurutan tidak bisa dibedakan dan "
    "SEMUANYA hilang dari database walau isinya sempurna.\n\n"
    "Tulis nama section SEBAGAI TEKS BIASA di barisnya sendiri (TANPA \"## \", TANPA bold, "
    "TANPA titik dua), tepat sebelum item-itemnya. Garis \"---\" BUKAN pengganti nama section:\n"
    "- \"Strategic Objectives\"        -> item bernomor: \"1. <judul>\", \"2. <judul>\"\n"
    "- \"Technical Decision Pattern\"  -> \"Pola 1: <judul>\"\n"
    "- \"Financial Decision Pattern\"  -> \"Pola 1: <judul>\"\n"
    "- \"Ecosystem Decision Pattern\"  -> \"Pola 1: <judul>\"\n"
    "- \"Governance Decision Pattern\" -> \"Pola 1: <judul>\"\n"
    "- \"Risk Response Pattern\"       -> \"Pola 1: <judul>\"\n"
    "- \"Recurring Behavioral Pattern\"-> \"Pola 1: <judul>\"\n"
    "- \"Strategic Trade-offs\"        -> \"Trade-off 1: <judul>\"\n"
    "Literal \"Pola \" (bukan \"Pattern \") dan \"Trade-off \". Field pendukung di bawah tiap "
    "item diawali \"· \". WAJIB isi SEMUA section di atas — jangan berhenti sebelum "
    "Strategic Trade-offs selesai."
)
_KNOWLEDGE_HINT = (
    "Section Knowledge tidak terparsing. Nama section ditulis SEBAGAI TEKS BIASA di barisnya "
    "sendiri (TANPA \"## \"/\"### \", TANPA bold), dan setiap item WAJIB bernomor dengan kata "
    "kunci yang tepat:\n"
    "\"Core Insights\" -> \"Insight 1: <judul>\"\n"
    "\"Strategic Principles\" -> \"Principle 1: <judul>\"\n"
    "\"Success Factors\" -> \"Factor 1: <judul>\"\n"
    "\"Failure Factors\" -> \"Factor 1: <judul>\"\n"
    "\"Decision Framework\" -> \"Step 1: <judul>\"\n"
    "\"Reusable Playbook\" -> \"Playbook 1: <judul>\"\n"
    "\"Anti-patterns\" -> \"Anti-pattern 1: <judul>\"\n"
    "Di bawah tiap item, field pendukung pakai label: Explanation:, Evidence:, "
    "Supporting Dataset:, Confidence:."
)

PHASE_CHECKS = {
    "entity": [Check("entities_parse", "entity blocks parse", _check_entities, _ENTITY_HINT)],
    "history": [Check("events_parse", "event blocks parse", _check_events, _HISTORY_HINT)],
    "behavioral": [
        Check("decisions_parse", "Decision Timeline parses", _check_decisions, _DECISION_HINT),
        Check("behavior_sections", "all 4 behaviour groupings parse", _check_behavior_sections,
              _BEHAVIOR_HINT),
    ],
    "knowledge": [Check("knowledge_parse", "knowledge items parse", _check_knowledge,
                        _KNOWLEDGE_HINT)],
    "conflict": [
        Check("qa_parse", "CIF Score Calculation parses", _check_qa_parse, _QA_HINT),
        Check("no_md_headers", "no markdown headers to truncate the report",
              _check_no_md_headers, _QA_HINT),
    ],
}


def checks_for(num: int, key: str) -> list:
    """Universal checks + this phase's format checks.

    Phase 11 used to be excluded, on the grounds that it was assembled from four stages and
    had no extractor to test against. Both halves stopped being true on 2026-08-09: it now
    goes out as one prompt like every other phase, and extract_qa.py is exactly the extractor
    that reads it. Leaving it unchecked meant an unparseable audit was written to disk, the
    project reported success, and poc/qa.json silently gained nothing.

    All three universal checks were verified against the one known-good Phase 11
    (data_project/Arbitrum/11-conflict.docx) before being switched on here, so they cannot
    trigger a repair loop on correct output.
    """
    return _UNIVERSAL + PHASE_CHECKS.get(key, [])


def run_checks(num: int, key: str, project_name: str, text: str) -> list:
    """Returns the list of FAILED (Check, detail) pairs -- empty means the phase is good."""
    failed = []
    for check in checks_for(num, key):
        try:
            ok, detail = check.test(text, project_name)
        except Exception as e:  # noqa: BLE001 -- a broken check must not kill the run
            ok, detail = False, f"check raised {type(e).__name__}: {e}"
        if not ok:
            failed.append((check, detail))
    return failed


def build_repair_prompt(num: int, key: str, project_name: str, failed: list) -> str:
    """The corrective message sent back after a failed phase.

    Deliberately asks for a COMPLETE rewrite of the phase rather than a patch: the phase file
    is saved verbatim and then parsed as a whole, so a partial answer ("here are the three
    fixed blocks") would have to be merged by hand, which is exactly the manual work this
    loop exists to remove. Every failure's hint is included so two problems get fixed in one
    round instead of two.
    """
    problems = "\n\n".join(
        f"{i}. MASALAH [{c.name}]: {detail}\n   PERBAIKAN WAJIB: {c.hint}"
        for i, (c, detail) in enumerate(failed, 1)
    )
    return (
        f"STOP. Output Phase {num:02d}-{key} untuk project {project_name} DITOLAK oleh "
        f"validator otomatis dan tidak bisa dipakai.\n\n"
        f"{problems}\n\n"
        f"Tulis ULANG SELURUH output Phase {num:02d}-{key} dari awal, lengkap, dengan format "
        f"yang sudah diperbaiki di atas. Pertahankan SEMUA fakta dan sitasi yang sudah benar "
        f"dari jawaban sebelumnya — ini perbaikan FORMAT, jangan kurangi isi atau ganti fakta, "
        f"dan jangan mengarang fakta baru. Jangan tulis penjelasan/permintaan maaf/komentar "
        f"apa pun di luar isi dataset — balas HANYA dengan isi Phase {num:02d}-{key} final."
    )

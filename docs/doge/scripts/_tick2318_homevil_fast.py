# -*- coding: utf-8 -*-
"""Tick 2318 leftover dual — Homevil Vilvoorde VAPH YE2025 (fast race)."""
from __future__ import annotations

import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
RAW = DATA / "raw" / "tick2318"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

UTC = "2026-08-27T22:45:00Z"
TICK = "2318"
RQ = "rq_2318"
NEXT_RQ = "rq_2319"
ENTITY = "vzw_homevil_vilvoorde"
KBO = "0420.610.608"
KBO_DIGITS = "0420610608"
GAP = "gap_homevil_nbb_pdf_assets_debt_empty_omzet_bruto_4_12m_pnl_jump_160pct_vaph_matrix_l5"
LB = "lb_homevil_bruto_4_12m_empty_omzet_pnl_jump_160pct_fte_41_jr2025"
COMM = "comm_homevil_jr2025_statutory_vaph_empty_omzet_bruto_pnl_jump"
SRC_EN = "src_homevil_jr2025_cw_en"

BRUTO, BRUTO24 = 4124105, 3528134
PNL, PNL24 = 870902, 334982
EQUITY, EQUITY24 = 6296387, 5477317
FTE, FTE24 = 41.1, 39.6
FILED = "08.06.2026"
EMAIL = "info@homevil.be"
ADDR = "Kursaalstraat 10, 1800 Vilvoorde"
PHONE = "022548910"
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
ABS, COST, DIFF, PI = 5.6, 3.5, 2.5, 5.4


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(path: Path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def append_rows(path: Path, id_key: str, new_rows):
    fields, rows = read_csv(path)
    have = {r.get(id_key) for r in rows}
    added = 0
    for nr in new_rows:
        if nr.get(id_key) in have:
            continue
        rows.append(nr)
        have.add(nr.get(id_key))
        added += 1
    write_csv(path, fields, rows)
    return added


# claim
rq_fields, rqrows = read_csv(DATA / "research_queue.csv")
rq = next((r for r in rqrows if r.get("task_id") == RQ), None)
if not rq:
    raise SystemExit("rq_2318 missing")
st, eid = rq.get("status"), (rq.get("entity_id") or "").strip()
if st == "done":
    raise SystemExit("rq_2318 already done")
if eid and eid != ENTITY:
    raise SystemExit(f"blocked by {eid}")
if st not in ("open", "in_progress"):
    raise SystemExit(f"bad status {st}")

_, ents = read_csv(DATA / "entities.csv")
if any(r.get("entity_id") == ENTITY for r in ents):
    raise SystemExit("Homevil already mined")

ls_fields, lsrows = read_csv(DATA / "loop_state.csv")
main = next(r for r in lsrows if r.get("state_id") == "main")
ticks = int(main.get("ticks_completed") or 0)
NEW_TICKS = str(ticks + 1)

for r in rqrows:
    if r.get("task_id") == RQ:
        r["status"] = "in_progress"
        r["entity_id"] = ENTITY
        r["updated_utc"] = UTC
        r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM Homevil"
write_csv(DATA / "research_queue.csv", rq_fields, rqrows)
print("CLAIMED")

RAW.mkdir(parents=True, exist_ok=True)
(RAW / "cw_en_excerpt.txt").write_text(
    f"Homevil YE2025 empty omzet bruto {BRUTO} pnl JUMP {PNL} (+{PNL_PCT}%) equity {EQUITY} FTE {FTE} filed {FILED}\n",
    encoding="utf-8",
)

append_rows(DATA / "sources.csv", "source_id", [
    {"source_id": SRC_EN, "title": "Homevil YE2025 CW EN (bruto 4.12m empty omzet / pnl JUMP +160%)", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/homevil", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "companyweb", "notes": f"tick{TICK}; Medium CW EN; empty omzet; bruto JUMP {BRUTO}; pnl JUMP {PNL} (+{PNL_PCT}%); equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}"},
    {"source_id": "src_homevil_jr2025_cw_nl", "title": "Homevil YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/homevil", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "companyweb", "notes": f"tick{TICK}; Medium CW NL; neerlegging {FILED}"},
    {"source_id": "src_homevil_jr2025_cw_fr", "title": "Homevil YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/homevil", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "companyweb", "notes": f"tick{TICK}; Medium CW FR; marge {BRUTO}; resultat {PNL}"},
    {"source_id": f"src_homevil_kbo_{KBO_DIGITS}", "title": f"KBO Homevil {KBO} Actief VZW NACE 87.202", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}", "publisher": "KBO / BCE", "accessed_date": "2026-08-27", "source_class": "kbo", "notes": f"tick{TICK}; Strong KBO Actief 1 VE Aanbestedende RSZ 87.202; {ADDR}; {EMAIL}"},
    {"source_id": "src_homevil_vaph_foi_2318", "title": "VAPH Homevil FOI info@homevil.be", "url": "https://www.vaph.be/organisaties/adressen", "publisher": "VAPH", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; {EMAIL}; T {PHONE}"},
])
append_rows(DATA / "budgets.csv", "budget_id", [
    {"budget_id": "bud_homevil_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": str(BRUTO), "amount_max_eur": str(BRUTO), "basis": "CW bruto YE2025 primary (empty omzet)", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; bruto JUMP {BRUTO} +{BRUTO_PCT}% vs {BRUTO24}"},
    {"budget_id": "bud_homevil_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": str(PNL), "amount_max_eur": str(PNL), "basis": "CW pnl YE2025 JUMP +160%", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; pnl JUMP {PNL} vs {PNL24}"},
    {"budget_id": "bud_homevil_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": str(EQUITY), "amount_max_eur": str(EQUITY), "basis": "CW equity YE2025", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; equity JUMP {EQUITY}"},
    {"budget_id": "bud_homevil_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": str(FTE), "amount_max_eur": str(FTE), "basis": "CW FTE YE2025", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; FTE JUMP {FTE} vs {FTE24}"},
    {"budget_id": "bud_homevil_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL24), "amount_min_eur": str(PNL24), "amount_max_eur": str(PNL24), "basis": "CW pnl YE2024 cmp", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL24}"},
])
cash = f'{{"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
append_rows(DATA / "commitments.csv", "commitment_id", [{
    "commitment_id": COMM, "title": "Homevil YE2025 leftover dual (bruto 4.12m empty omzet / pnl JUMP +160% / FTE 41.1 / Medium)",
    "entity_id": ENTITY, "beneficiary": "VAPH clienten Vilvoorde", "legal_basis": f"VZW Homevil (KBO {KBO}; Actief; RSZ 87.202)",
    "decision_date": "2026-06-08", "start_year": "2025", "end_year": "2025", "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash, "remaining_eur": "0", "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/homevil",
    "stated_goal": "Flemish VAPH woon/dag/begeleiding Vilvoorde",
    "cut_option": "Publish NBB PDF; reconcile empty omzet vs bruto 4.12m + pnl JUMP +160%",
    "source_id": SRC_EN, "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Vilvoorde>Homevil>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; after Schoonderhage@2317; Domino EVERY-10@2310",
}])
append_rows(DATA / "leaderboard.csv", "item_id", [{
    "item_id": LB, "name": "Homevil bruto 4.12m / empty omzet / pnl JUMP +160% / FTE 41.1 (YE2025)",
    "level": "L5", "type": "vaph_vzw_statutory", "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Vilvoorde>Homevil>JR2025",
    "annual_cost_eur": str(BRUTO), "total_cost_eur": str(BRUTO),
    "tco_notes": f"CW empty omzet / bruto JUMP {BRUTO} / pnl JUMP {PNL} (+{PNL_PCT}%) / equity JUMP {EQUITY} / FTE JUMP {FTE}",
    "confidence": "medium", "source_id": SRC_EN, "beneficiaries": "VAPH adults mental disability Vilvoorde",
    "stated_goal": "Flemish VAPH care", "measured_outcome": f"empty omzet; bruto {BRUTO}; pnl JUMP {PNL_PCT}%; FTE {FTE}",
    "absurdity_score": str(ABS), "cost_score": str(COST), "difficulty": str(DIFF), "priority_index": str(PI),
    "cut_proposal": "FOI NBB PDF assets/debt + omzet opacity", "status": "open", "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}",
}])
append_rows(DATA / "entities.csv", "entity_id", [{
    "entity_id": ENTITY,
    "name_nl": "Homevil VZW (Vilvoorde / VAPH mentale handicap)",
    "name_fr": "Homevil ASBL (Vilvorde / VAPH handicap mental)",
    "name_en": "Homevil VZW (Vilvoorde / VAPH mental disability care)",
    "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl",
    "website": "https://homevil.be/", "foi_email": EMAIL, "foi_postal": ADDR,
    "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE RSZ 87.202 Aanbestedende; empty omzet; bruto JUMP {BRUTO}; pnl JUMP {PNL} (+{PNL_PCT}%); equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}; FOI {GAP}; not TE-additive",
}])
append_rows(DATA / "foi_queue.csv", "gap_id", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Vilvoorde>Homevil>NBB_PDF_empty_omzet_pnl_jump_vaph",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025; assets/debt/cash; why omzet unpublished while bruto EUR{BRUTO}; why pnl JUMP EUR{PNL} (+{PNL_PCT}%); FTE {FTE}; VAPH subsidy split",
    "why_it_matters": "Medium CW Vilvoorde VAPH (bruto 4.12m empty omzet / pnl JUMP +160%); assets/debt unpublished",
    "priority": "8", "recipient_body": "Homevil VZW", "recipient_email": EMAIL,
    "recipient_postal": f"{ADDR} (T {PHONE})", "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready", "date_ready": "2026-08-27", "date_sent": "", "date_due": "", "date_answered": "",
    "response_summary": "", "linked_commitment_id": COMM, "linked_leaderboard_id": LB,
    "created_utc": UTC, "updated_utc": UTC, "notes": f"tick{TICK}; ready NOT sent",
}])
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Homevil (empty omzet / bruto 4.12m / pnl JUMP +160%)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**recipient:** {EMAIL}

## Brief
```text
Aan: Homevil VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Homevil (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting waarom omzet unpublished terwijl bruto EUR{BRUTO}.
3. Toelichting pnl JUMP EUR{PNL} (+{PNL_PCT}% vs YE2024 EUR{PNL24}).
4. Split bruto (VAPH / dagprijs / overige); FTE {FTE} vs {FTE24}.

Ref: {GAP}
```
- [x] ready NOT sent
""",
    encoding="utf-8",
)

rq_fields, rqrows = read_csv(DATA / "research_queue.csv")
for r in rqrows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = "leftover dual — Homevil YE2025 Medium (bruto JUMP 4.12m / empty omzet / pnl JUMP +160% / FTE 41.1)"
        r["notes"] = f"tick{TICK}: Homevil YE2025 Medium (empty omzet; bruto JUMP {BRUTO}; pnl JUMP {PNL} +{PNL_PCT}%; equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE Vilvoorde VAPH); FOI {GAP} ready not sent; after Schoonderhage@2317; next EVERY-10 2320"
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append({
        "task_id": NEXT_RQ,
        "title": "leftover dual after Homevil — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill", "priority": "8", "status": "open", "hierarchy_target": "L5", "entity_id": "",
        "instructions": "After Homevil YE2025 Medium (bruto 4.12m empty omzet / pnl JUMP +160%). Prefer AGB/FARO if YE2025 else FREE (De Max/Gandae/Aralea/Manupal/De Ploeg/Vlotter if YE2025). Do NOT redo Homevil/Schoonderhage/Havenzate/Iris/OTB/Olo-Rotonde/Hejmen/Domino stack.",
        "blocked_gap_id": "", "created_utc": UTC, "updated_utc": UTC,
        "notes": f"spawned after tick{TICK} Homevil; next EVERY-10 2320",
    })
write_csv(DATA / "research_queue.csv", rq_fields, rqrows)

for r in lsrows:
    if r.get("state_id") == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = UTC
        r["last_unit_id"] = RQ
        r["ticks_completed"] = NEW_TICKS
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} leftover dual Homevil {KBO} Medium (empty omzet; bruto JUMP {BRUTO}; "
            f"pnl JUMP {PNL} +{PNL_PCT}%; equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE Vilvoorde VAPH); "
            f"after Schoonderhage@2317; Domino EVERY-10@2310; AGB/FARO YE2024; next {NEXT_RQ}; next EVERY-10 2320"
        )
write_csv(DATA / "loop_state.csv", ls_fields, lsrows)

with LOG.open("a", encoding="utf-8") as f:
    f.write(f"""
### {UTC} - tick {TICK} - rq_{TICK} Homevil Vilvoorde VAPH (bruto JUMP 4.12m / empty omzet / pnl JUMP +160% / FTE 41.1 / Medium)

- Unit: **{RQ}** leftover dual after **Schoonderhage@2317**. Prefer NON-stall: AGB/FARO/AIESH YE2024. Took FREE VAPH **Homevil VZW** YE2025 (KBO **{KBO}**; {ADDR}; 1 VE; RSZ **87.202**; Aanbestedende; {EMAIL}).
- Found: CW NL+EN+FR YE2025 live - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}%; pnl **EUR{PNL}** JUMP +{PNL_PCT}%; equity **EUR{EQUITY}** JUMP +14.95%; FTE **{FTE}**; filed **{FILED}**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources/budgets/commitments/leaderboard/entities/foi; {RQ}=done + {NEXT_RQ} open; ticks={NEW_TICKS}.
- FOI: **ready not sent**. NOT every-10 (last 2310; next 2320). Next: {NEXT_RQ}.
""")
print("DONE", TICK, "Homevil", NEW_TICKS)

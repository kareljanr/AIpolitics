# -*- coding: utf-8 -*-
"""Tick 2325: Mivalti Tielt VAPH YE2025 — APPEND-ONLY."""
from __future__ import annotations

import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
RAW = DATA / "raw" / "tick2325"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

UTC = "2026-08-28T00:30:00Z"
TICK = "2325"
RQ, NEXT_RQ = "rq_2325", "rq_2326"
ENTITY = "vzw_mivalti_tielt"
KBO = "0416.406.548"
KBO_DIGITS = "0416406548"
GAP = "gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_fte_jump_vaph_matrix_l5"
LB = "lb_mivalti_bruto_11_49m_omzet_1_68m_6_82x_pnl_jump_fte_135_jr2025"
COMM = "comm_mivalti_jr2025_statutory_vaph_bruto_11_49m_6_82x_pnl_jump"

OMZET, OMZET24 = 1683253, 1609944
BRUTO, BRUTO24 = 11487628, 10636440
PNL, PNL24 = 470626, 370928
EQUITY, EQUITY24 = 8134690, 7660758
FTE, FTE24 = 134.9, 133.1
FILED = "16.06.2026"
EMAIL = "info@mivalti.be"
ADDR = "Gruuthusestraat 36, 8700 Tielt"
RATIO = round(BRUTO / OMZET, 2)  # 6.82
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
ABS, COST, DIFF, PI = 7.0, 5.5, 3.0, 6.2


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames), list(r)


def write_csv(path: Path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
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


_, lsrows = read_csv(DATA / "loop_state.csv")
main = next(r for r in lsrows if r.get("state_id") == "main")
ticks = int(main.get("ticks_completed") or 0)
if ticks >= 2325:
    raise SystemExit(f"already at {ticks}")

_, rqrows = read_csv(DATA / "research_queue.csv")
rq = next((r for r in rqrows if r.get("task_id") == RQ), None)
if not rq or rq.get("status") not in ("open", "in_progress"):
    raise SystemExit(f"rq_2325 not claimable: {rq and rq.get('status')}")

_, ents = read_csv(DATA / "entities.csv")
if any(r.get("entity_id") == ENTITY for r in ents):
    raise SystemExit("Mivalti already in entities")

RAW.mkdir(parents=True, exist_ok=True)
FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(RAW / "cw_en_excerpt.txt").write_text(
    f"Mivalti YE2025 omzet {OMZET} bruto {BRUTO} ~{RATIO}x pnl JUMP {PNL} equity {EQUITY} FTE {FTE} filed {FILED}\n"
    f"https://www.companyweb.be/en/{KBO_DIGITS}/mivalti\n",
    encoding="utf-8",
)

print("sources +", append_rows(DATA / "sources.csv", "source_id", [
    {"source_id": "src_mivalti_jr2025_cw_en", "title": f"Mivalti YE2025 CW EN (bruto 11.49m / omzet 1.68m ~{RATIO}x)", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/mivalti", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "companyweb", "notes": f"tick{TICK}; Medium CW EN; omzet JUMP {OMZET} (+4.55%); bruto JUMP {BRUTO} (~{RATIO}x); pnl JUMP {PNL} ({PNL_PCT}%); equity JUMP {EQUITY}; FTE JUMP {FTE}; filed {FILED}"},
    {"source_id": "src_mivalti_jr2025_cw_nl", "title": "Mivalti YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/mivalti", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "companyweb", "notes": f"tick{TICK}; Medium CW NL; neerlegging {FILED}"},
    {"source_id": "src_mivalti_jr2025_cw_fr", "title": "Mivalti YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/mivalti", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "companyweb", "notes": f"tick{TICK}; Medium CW FR; CA {OMZET}; marge {BRUTO}; résultat {PNL}"},
    {"source_id": f"src_mivalti_kbo_{KBO_DIGITS}", "title": f"KBO Mivalti {KBO} Actief VZW NACE 87.202 Tielt", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}", "publisher": "KBO / BCE", "accessed_date": "2026-08-28", "source_class": "kbo", "notes": f"tick{TICK}; Strong KBO Actief; VZW 25.05.1976; Gruuthusestraat 36 8700 Tielt; RSZ 87.202"},
    {"source_id": "src_mivalti_site_contact_2325", "title": "Mivalti FOI info@mivalti.be", "url": "https://mivalti.be/", "publisher": "Mivalti VZW", "accessed_date": "2026-08-28", "source_class": "foi_contact", "notes": f"tick{TICK}; {EMAIL}; {ADDR}"},
]))

print("budgets +", append_rows(DATA / "budgets.csv", "budget_id", [
    {"budget_id": "bud_mivalti_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": str(BRUTO), "amount_max_eur": str(BRUTO), "basis": f"CW bruto YE2025 primary (~{RATIO}x omzet)", "source_id": "src_mivalti_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; bruto {BRUTO}"},
    {"budget_id": "bud_mivalti_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": str(OMZET), "amount_max_eur": str(OMZET), "basis": "CW omzet YE2025", "source_id": "src_mivalti_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; omzet {OMZET}"},
    {"budget_id": "bud_mivalti_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": str(PNL), "amount_max_eur": str(PNL), "basis": "CW pnl YE2025", "source_id": "src_mivalti_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; pnl {PNL}"},
    {"budget_id": "bud_mivalti_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": str(EQUITY), "amount_max_eur": str(EQUITY), "basis": "CW equity YE2025", "source_id": "src_mivalti_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; equity {EQUITY}"},
    {"budget_id": "bud_mivalti_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": str(FTE), "amount_max_eur": str(FTE), "basis": "CW FTE YE2025", "source_id": "src_mivalti_jr2025_cw_en", "confidence": "medium", "notes": f"tick{TICK}; FTE {FTE}"},
]))

print("commitments +", append_rows(DATA / "commitments.csv", "commitment_id", [{
    "commitment_id": COMM,
    "title": f"Mivalti YE2025 leftover dual (bruto 11.49m / omzet 1.68m ~{RATIO}x / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "VAPH cliënten Tielt woon/dag",
    "legal_basis": f"VZW Mivalti (KBO {KBO}; Actief; RSZ 87.202)",
    "decision_date": "2026-06-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/mivalti",
    "stated_goal": "Flemish VAPH residential Tielt",
    "cut_option": f"Publish NBB PDF; reconcile bruto÷omzet ~{RATIO}x",
    "source_id": "src_mivalti_jr2025_cw_en",
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Tielt>Mivalti>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; after Ritmica@2324; Het Eepos Ver.OCMW no CW YE2025",
}]))

print("leaderboard +", append_rows(DATA / "leaderboard.csv", "item_id", [{
    "item_id": LB,
    "name": f"Mivalti bruto 11.49m / omzet 1.68m ~{RATIO}x / pnl JUMP / FTE 134.9 (YE2025)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Tielt>Mivalti>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": f"CW omzet JUMP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl JUMP {PNL} / equity JUMP {EQUITY} / FTE JUMP {FTE} / filed {FILED}",
    "confidence": "medium",
    "source_id": "src_mivalti_jr2025_cw_en",
    "beneficiaries": "VAPH adults mental disability Tielt",
    "stated_goal": "Flemish VAPH residential + day support",
    "measured_outcome": f"bruto÷omzet ~{RATIO}x; pnl JUMP {PNL_PCT}%; FTE {FTE}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF FOI; reconcile bruto÷omzet ~{RATIO}x + assets/debt",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Ritmica@2324",
}]))

print("entities +", append_rows(DATA / "entities.csv", "entity_id", [{
    "entity_id": ENTITY,
    "name_nl": "Mivalti VZW (Tielt / VAPH woonondersteuning)",
    "name_fr": "Mivalti ASBL (Tielt / VAPH hébergement)",
    "name_en": "Mivalti VZW (Tielt VAPH residential care)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://mivalti.be/",
    "foi_email": EMAIL,
    "foi_postal": ADDR,
    "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW RSZ 87.202; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging {FILED}; FOI {GAP}; after Ritmica@2324; AGB Bornem JR2024; FARO/AIESH YE2024; not TE-additive",
}]))

print("foi_queue +", append_rows(DATA / "foi_queue.csv", "gap_id", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Tielt>Mivalti>NBB_PDF_assets_debt_bruto_gt_omzet_vaph",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025; why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x); assets/debt/cash; VAPH/PVB split",
    "why_it_matters": f"Medium CW VAPH Tielt residential VZW (bruto 11.49m / omzet 1.68m ~{RATIO}x / FTE {FTE}); assets/debt unpublished",
    "priority": "8",
    "recipient_body": "Mivalti VZW",
    "recipient_email": EMAIL,
    "recipient_postal": ADDR,
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-28",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO",
}]))

(FOI_DRAFTS / f"{GAP}.md").write_text(f"""# FOI draft — Mivalti (NBB PDF / bruto≫omzet ~{RATIO}x)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** Mivalti VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; RSZ **87.202**)  
**recipient:** {EMAIL}

## Brief
```text
Aan: Mivalti VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Mivalti (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVB-matrix.
3. Schulden LT/KT en liquide middelen YE2025.

Ref: {GAP}
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")

for r in rqrows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = f"leftover dual — Mivalti YE2025 Medium (bruto JUMP 11.49m / ~{RATIO}x omzet / pnl JUMP / FTE {FTE})"
        r["notes"] = f"tick{TICK}: Mivalti YE2025 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; Tielt VAPH); FOI {GAP} ready not sent; after Ritmica@2324; Het Eepos Ver.OCMW no CW YE2025; stalls YE2024; next EVERY-10 2330"
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append({
        "task_id": NEXT_RQ,
        "title": "leftover dual after Mivalti — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": f"After Mivalti YE2025 Medium (bruto ~{RATIO}x). Prefer AGB Bornem/APB → FARO/AIESH if YE2025 → FREE ETA-VAPH-WZC-maatwerk (Den Brand/Gandae/Manupal/Aralea if YE2025). Do NOT redo Mivalti/Ritmica/Dominiek Savio/Humival/Heder/Homevil/Het Eepos stack.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"spawned after tick{TICK} Mivalti; stalls YE2024; next EVERY-10 2330",
    })
write_csv(DATA / "research_queue.csv", read_csv(DATA / "research_queue.csv")[0], rqrows)

for r in lsrows:
    if r.get("state_id") == "main":
        r.update({
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": TICK,
            "paused": "no",
            "notes": f"tick{TICK} leftover dual Mivalti {KBO} Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; Tielt VAPH); after Ritmica@2324; AGB Bornem JR2024; FARO/AIESH YE2024; next {NEXT_RQ}; next EVERY-10 2330; continuous hole_fill",
        })
write_csv(DATA / "loop_state.csv", read_csv(DATA / "loop_state.csv")[0], lsrows)

with LOG.open("a", encoding="utf-8") as f:
    f.write(f"""
### {UTC} - tick {TICK} - rq_{TICK} Mivalti Tielt (bruto JUMP 11.49m / ~{RATIO}x omzet / pnl JUMP / FTE {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Ritmica@2324** (retargeted from Het Eepos Ver.OCMW — no CW YE2025 euros). Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH/Aralea/Vlotter/Manupal/Gandae still **YE2024**. Took FREE Flemish VAPH **Mivalti VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief**; RSZ **87.202**; {EMAIL}). Do not redo Ritmica/Dominiek Savio/Humival/Heder/Homevil stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +4.55%; bruto **EUR{BRUTO}** JUMP +8% (~**{RATIO}x**); pnl **EUR{PNL}** JUMP +26.88%; equity **EUR{EQUITY}** JUMP +6.19%; FTE **{FTE}**; neerlegging **{FILED}**. Strong KBO Actief. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2320**; next **2330**). Next: {NEXT_RQ}.
""")
print("DONE tick", TICK)

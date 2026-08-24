from pathlib import Path
import csv, json
csv.field_size_limit(10_000_000)
root = Path(".")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2313"
raw.mkdir(parents=True, exist_ok=True)

TICK = "2313"
UTC = "2026-08-27T21:30:00Z"
ENTITY = "vzw_hejmen_leuven"
KBO = "0426.383.987"
KBO_DIGITS = "0426383987"
BRUTO = 2696639
PNL = 166418
EQUITY = 2887744
FTE = 32.1
BRUTO_2024 = 2583385
PNL_2024 = 173356
EQUITY_2024 = 2733216
FTE_2024 = 32.8
GAP = "gap_hejmen_nbb_pdf_assets_debt_empty_omzet_bruto_2_70m_pnl_drop_vaph_matrix_l5"
LB = "lb_hejmen_bruto_2_70m_empty_omzet_pnl_drop_equity_jump_jr2025"
COMM = "comm_hejmen_jr2025_statutory_vaph_bruto_2_70m_empty_omzet"
RQ = "rq_2313"
RQ_NEXT = "rq_2314"
SRC_EN = "src_hejmen_jr2025_cw_en"
SRC_NL = "src_hejmen_jr2025_cw_nl"
SRC_FR = "src_hejmen_jr2025_cw_fr"
SRC_KBO = "src_hejmen_kbo_0426383987"
SRC_SITE = "src_hejmen_site_contact_2313"
SRC_NBB = "src_hejmen_nbb_consult_0426383987"
ABS, COST, DIFF = 4.8, 4.2, 3.0
PI = round((ABS + COST) / 2, 2)
ADDR = "s-Hertogenlaan 62, 3000 Leuven"

def append_csv(path, rows, id_key):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing = list(reader)
    have = {r.get(id_key) for r in existing}
    new = [r for r in rows if r.get(id_key) not in have]
    if not new:
        print(path.name, "already")
        return
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(path.name, "+", len(new))

path = data / "research_queue.csv"
with path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
found = False
for row in rows:
    if row["task_id"] == RQ:
        eid = (row.get("entity_id") or "").strip()
        print("before", row["status"], eid)
        if row["status"] == "done" and eid and eid != ENTITY:
            raise SystemExit("done by " + eid)
        if row["status"] == "in_progress" and eid and eid != ENTITY:
            raise SystemExit("locked " + eid)
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = f"leftover dual — Hejmen YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m / empty omzet / pnl DROP -4% / FTE {FTE})"
        row["notes"] = (
            f"tick{TICK}: Hejmen Leuven YE2025 Medium (empty omzet; bruto JUMP {BRUTO} +4.38%; "
            f"pnl DROP {PNL} -4%; equity JUMP {EQUITY}; FTE {FTE}; 3 VE VAPH); FOI {GAP}; "
            f"after M HKA@2312; next EVERY-10 2320"
        )
        found = True
if not found:
    raise SystemExit("missing")
if not any(row["task_id"] == RQ_NEXT for row in rows):
    rows.append({
        "task_id": RQ_NEXT,
        "title": "leftover dual after Hejmen — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": "After Hejmen. Prefer AGB/FARO YE2025 else unused. Do NOT redo Hejmen/Willekom/Zewopa/Huis in de Stad/Katrinahof/Alvinnenberg/TMK/Kompas stack.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"spawned after tick{TICK}; next EVERY-10 2320",
    })
    print("spawned")
tmp = path.with_suffix(".tmp.csv")
with tmp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)
tmp.replace(path)
print("rq ok")

append_csv(data / "sources.csv", [
    {"source_id": SRC_EN, "title": "Hejmen YE2025 Companyweb EN", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/hejmen", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; empty omzet; bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 30.06.2026"},
    {"source_id": SRC_NL, "title": "Hejmen YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/hejmen", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL YE2025; neerlegging 30.06.2026; Middelgroot {FTE} FTE; NACE 87.202"},
    {"source_id": SRC_FR, "title": "Hejmen YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/hejmen", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW FR YE2025"},
    {"source_id": SRC_KBO, "title": f"KBO Hejmen {KBO}", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW 3 VE; {ADDR}; RSZ 87.202"},
    {"source_id": SRC_SITE, "title": "Hejmen FOI channel info@hejmen.be", "url": "https://www.hejmen.be/contact", "publisher": "Hejmen vzw", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; info@hejmen.be; T 016 22 10 25"},
    {"source_id": SRC_NBB, "title": "NBB CBSO consult Hejmen", "url": f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}", "publisher": "NBB CBSO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; filing 30.06.2026; assets/debt FOI"},
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_hejmen_omzet_jr2025_statutory_empty", "entity_id": ENTITY, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; omzet unpublished"},
    {"budget_id": "bud_hejmen_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; bruto JUMP +4.38% vs {BRUTO_2024}"},
    {"budget_id": "bud_hejmen_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; pnl DROP -4% vs {PNL_2024}"},
    {"budget_id": "bud_hejmen_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; equity JUMP +5.65%"},
    {"budget_id": "bud_hejmen_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; FTE {FTE} vs {FTE_2024}"},
    {"budget_id": "bud_hejmen_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL_2024), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 cmp"},
], "budget_id")

cash = json.dumps({"2025_omzet": None, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE, "2024_bruto": BRUTO_2024, "2024_pnl": PNL_2024, "2024_equity": EQUITY_2024, "2024_fte": FTE_2024}, separators=(",", ":"))
append_csv(data / "commitments.csv", [{
    "commitment_id": COMM,
    "title": f"Hejmen YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / empty omzet / pnl DROP / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "Adults with mental disability / VAPH Leuven",
    "legal_basis": f"VZW Hejmen (KBO {KBO}; 3 VE; RSZ 87.202)",
    "decision_date": "2026-06-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/hejmen",
    "stated_goal": "VAPH residential + day care mental disability Leuven",
    "cut_option": "Publish NBB PDF; disclose omzet + VAPH matrix",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Leuven>Hejmen>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}",
}], "commitment_id")

append_csv(data / "leaderboard.csv", [{
    "item_id": LB,
    "name": f"Hejmen bruto {BRUTO/1e6:.2f}m / empty omzet / pnl DROP -4% / equity JUMP (YE2025 VAPH Leuven)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Leuven>Hejmen>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": f"empty omzet / bruto JUMP {BRUTO} +4.38% / pnl DROP {PNL} -4% / equity JUMP {EQUITY} / FTE {FTE}",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Adults with mental disability VAPH Leuven",
    "stated_goal": "VAPH residential care",
    "measured_outcome": f"empty omzet; bruto +4.38%; pnl -4%; FTE {FTE}; filed 30.06.2026",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": "NBB PDF FOI; disclose omzet + VAPH subsidy matrix",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW + Strong KBO; FOI {GAP}",
}], "item_id")

append_csv(data / "entities.csv", [{
    "entity_id": ENTITY,
    "name_nl": "Hejmen VZW (Leuven / VAPH huisvesting mentale handicap)",
    "name_fr": "Hejmen ASBL (Louvain / hebergement VAPH handicap mental)",
    "name_en": "Hejmen ASBL (Leuven VAPH residential mental-disability care)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.hejmen.be/",
    "foi_email": "info@hejmen.be",
    "foi_postal": ADDR,
    "notes": f"tick{TICK} YE2025 Medium CW + Strong KBO {KBO} Actief 3 VE RSZ 87.202; empty omzet; bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; FOI {GAP}",
}], "entity_id")

append_csv(data / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Leuven>Hejmen>NBB_PDF_empty_omzet_bruto_2_70m_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025 assets/debt/cash; empty omzet vs bruto {BRUTO}; pnl {PNL}; VAPH matrix",
    "why_it_matters": f"VAPH housing VZW bruto {BRUTO/1e6:.2f}m empty omzet; assets/debt unpublished",
    "priority": "8",
    "recipient_body": "Hejmen VZW",
    "recipient_email": "info@hejmen.be",
    "recipient_postal": ADDR,
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK}; ready NOT sent",
}], "gap_id")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} leftover dual Hejmen {KBO} Medium (empty omzet; bruto JUMP {BRUTO} +4.38%; pnl DROP {PNL} -4%; equity JUMP {EQUITY}; FTE {FTE}; 3 VE Leuven VAPH); after M HKA@2312; AGB Bornem JR2024; FARO/AIESH YE2024; next {RQ_NEXT}; next EVERY-10 2320; continuous hole_fill\n",
    encoding="utf-8",
)
(raw / "summary.json").write_text(json.dumps({"tick": TICK, "unit": RQ, "entity": ENTITY, "bruto": BRUTO, "pnl": PNL, "fte": FTE, "confidence": "medium", "pi": PI}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(f"Hejmen YE2025 empty omzet bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE} filed 30.06.2026\n", encoding="utf-8")
(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — Hejmen Leuven (NBB PDF / empty omzet / bruto 2.70m / pnl DROP -4%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Hejmen VZW — KBO **{KBO}** (Actief; {ADDR}; **3 VE**; FTE {FTE}; RSZ **87.202**; VAPH)  
**recipient:** info@hejmen.be · {ADDR} (T 016 22 10 25)  
**tick:** {TICK}  
**confidence:** Medium

## Context
CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +4.38%; pnl **EUR{PNL:,}** DROP -4%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **30.06.2026**.

## Brief
```text
Aan: Hejmen VZW via info@hejmen.be
Betreft: Openbaarmaking jaarrekening 2025 (KBO {KBO})
1. NBB PDF YE2025 assets/debt/cash
2. Toelichting empty omzet / bruto {BRUTO} / pnl DROP / FTE
3. VAPH-toelagen matrix
Ref: {GAP}
```
- [x] ready NOT sent
""", encoding="utf-8")

log = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} Hejmen Leuven (bruto JUMP {BRUTO/1e6:.2f}m / empty omzet / pnl DROP -4% / FTE {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Willekom@2311**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH still **YE2024**; Gandae still **YE2024**. Took unused FREE Flemish VAPH **Hejmen VZW** YE2025 (KBO **{KBO}**; {ADDR}; **3 VE**; RSZ **87.202**; info@hejmen.be). Do not redo Willekom/Zewopa/Huis in de Stad/Katrinahof/Alvinnenberg/TMK/Kompas stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +4.38%; pnl **EUR{PNL}** DROP -4%; equity **EUR{EQUITY}** JUMP +5.65%; FTE **{FTE}** (vs {FTE_2024}); neerlegging **30.06.2026**. Strong KBO Actief 3 VE. Assets/debt Unknown. Medium.
- Wrote: sources (+6); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2320**). Next: {RQ_NEXT}.
"""
text = log.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print("log ok")
print("DONE", TICK, BRUTO, PI)

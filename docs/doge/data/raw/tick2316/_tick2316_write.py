from pathlib import Path
import csv, json, time, shutil
csv.field_size_limit(10_000_000)
root = Path(".")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2316"
raw.mkdir(parents=True, exist_ok=True)

TICK = "2316"
UTC = "2026-08-27T22:15:00Z"
ENTITY = "vzw_ons_tehuis_brabant"
KBO = "0413.336.103"
KBO_DIGITS = "0413336103"
OMZET = 1820095
BRUTO = 10405932
PNL = 1089571
EQUITY = 13305684
FTE = 118.5
OMZET_2024 = 1542304
BRUTO_2024 = 9858784
PNL_2024 = 580167
EQUITY_2024 = 12337070
FTE_2024 = 118.0
RATIO = round(BRUTO / OMZET, 2)  # 5.72
GAP = "gap_otb_nbb_pdf_assets_debt_bruto_gt_omzet_5_72x_pnl_jump_88pct_vaph_matrix_l5"
LB = "lb_otb_bruto_10_41m_omzet_1_82m_5_72x_pnl_jump_jr2025"
COMM = "comm_otb_jr2025_statutory_vaph_bruto_10_41m_5_72x_pnl_jump"
RQ = "rq_2316"
RQ_NEXT = "rq_2317"
SRC_EN = "src_otb_jr2025_cw_en"
SRC_NL = "src_otb_jr2025_cw_nl"
SRC_FR = "src_otb_jr2025_cw_fr"
SRC_KBO = "src_otb_kbo_0413336103"
SRC_SITE = "src_otb_site_contact_2316"
SRC_NBB = "src_otb_nbb_consult_0413336103"
ABS, COST, DIFF = 6.2, 5.5, 3.0
PI = round((ABS + COST) / 2, 2)
ADDR = "Perksesteenweg 126, 1910 Kampenhout"

def append_csv(path, rows, id_key):
    with path.open(encoding="utf-8-sig", newline="") as f:
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

def write_queue(rows, fields):
    path = data / "research_queue.csv"
    tmp = data / "rq_2316_out.csv"
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    for i in range(10):
        try:
            if path.exists():
                path.unlink()
            shutil.move(str(tmp), str(path))
            print("queue write ok", i)
            return
        except Exception as e:
            print("queue retry", i, e)
            time.sleep(0.4)
    raise SystemExit("queue write failed")

path = data / "research_queue.csv"
with path.open(encoding="utf-8-sig", newline="") as f:
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
        row["title"] = f"leftover dual — Ons Tehuis-Brabant YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP +88% / FTE {FTE})"
        row["notes"] = (
            f"tick{TICK}: Ons Tehuis-Brabant YE2025 Medium (omzet JUMP {OMZET} +18.01%; bruto JUMP {BRUTO} ~{RATIO}x; "
            f"pnl JUMP {PNL} +87.8%; equity JUMP {EQUITY}; FTE {FTE}; 1 VE VAPH Kampenhout); FOI {GAP}; "
            f"after Havenzate@2315; next EVERY-10 2320"
        )
        found = True
if not found:
    raise SystemExit("missing")
if not any(row["task_id"] == RQ_NEXT for row in rows):
    rows.append({
        "task_id": RQ_NEXT,
        "title": "leftover dual after Ons Tehuis-Brabant — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": "After Ons Tehuis-Brabant. Prefer AGB/FARO YE2025 else unused. Do NOT redo Ons Tehuis-Brabant/Havenzate/Hejmen/Willekom/Iris/Huis in de Stad stack.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"spawned after tick{TICK}; next EVERY-10 2320",
    })
    print("spawned")
write_queue(rows, fields)

append_csv(data / "sources.csv", [
    {"source_id": SRC_EN, "title": "Ons Tehuis-Brabant YE2025 Companyweb EN", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/ons-tehuis-brabant", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 07.07.2026"},
    {"source_id": SRC_NL, "title": "Ons Tehuis-Brabant YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/ons-tehuis-brabant", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL YE2025; neerlegging 07.07.2026; Groot {FTE} FTE; NACE 87.202"},
    {"source_id": SRC_FR, "title": "Ons Tehuis-Brabant YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/ons-tehuis-brabant", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW FR YE2025"},
    {"source_id": SRC_KBO, "title": f"KBO Ons Tehuis-Brabant {KBO}", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW 1 VE; {ADDR}; RSZ 87.202; aanbestedende overheid"},
    {"source_id": SRC_SITE, "title": "Ons Tehuis-Brabant FOI channel info@otbvzw.be", "url": "https://www.onstehuisbrabant.be/contact", "publisher": "Ons Tehuis Brabant vzw", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; info@otbvzw.be; T 016 65 91 10"},
    {"source_id": SRC_NBB, "title": "NBB CBSO consult Ons Tehuis-Brabant", "url": f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}", "publisher": "NBB CBSO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; filing 07.07.2026; assets/debt FOI"},
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_otb_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; omzet JUMP +18.01% vs {OMZET_2024}"},
    {"budget_id": "bud_otb_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; bruto JUMP +5.55% ~{RATIO}x"},
    {"budget_id": "bud_otb_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; pnl JUMP +87.8% vs {PNL_2024}"},
    {"budget_id": "bud_otb_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; equity JUMP +7.85%"},
    {"budget_id": "bud_otb_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; FTE {FTE} vs {FTE_2024}"},
    {"budget_id": "bud_otb_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL_2024), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 cmp"},
], "budget_id")

cash = json.dumps({"2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE, "2024_omzet": OMZET_2024, "2024_bruto": BRUTO_2024, "2024_pnl": PNL_2024, "2024_equity": EQUITY_2024, "2024_fte": FTE_2024}, separators=(",", ":"))
append_csv(data / "commitments.csv", [{
    "commitment_id": COMM,
    "title": f"Ons Tehuis-Brabant YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / ~{RATIO}x / pnl JUMP / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "Adults with mental disability / VAPH Kampenhout",
    "legal_basis": f"VZW Ons Tehuis-Brabant (KBO {KBO}; 1 VE; RSZ 87.202; aanbestedende overheid)",
    "decision_date": "2026-07-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/ons-tehuis-brabant",
    "stated_goal": "VAPH residential + day support mental disability",
    "cut_option": f"Publish NBB PDF; disclose VAPH matrix behind bruto~{RATIO}x",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Kampenhout>Ons_Tehuis_Brabant>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; FOI {GAP}",
}], "commitment_id")

append_csv(data / "leaderboard.csv", [{
    "item_id": LB,
    "name": f"Ons Tehuis-Brabant bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / pnl JUMP +88% (YE2025 VAPH Kampenhout)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Kampenhout>Ons_Tehuis_Brabant>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": f"omzet JUMP {OMZET} +18.01% / bruto JUMP {BRUTO} ~{RATIO}x / pnl JUMP {PNL} +87.8% / equity JUMP {EQUITY} / FTE {FTE}",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Adults with mental disability VAPH Kampenhout",
    "stated_goal": "VAPH residential care",
    "measured_outcome": f"omzet +18.01%; bruto ~{RATIO}x; pnl +87.8%; FTE {FTE}; filed 07.07.2026",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"NBB PDF FOI; VAPH subsidy matrix behind bruto~{RATIO}x",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW + Strong KBO; FOI {GAP}",
}], "item_id")

append_csv(data / "entities.csv", [{
    "entity_id": ENTITY,
    "name_nl": "Ons Tehuis-Brabant VZW (Kampenhout / VAPH huisvesting mentale handicap)",
    "name_fr": "Ons Tehuis-Brabant ASBL (Kampenhout / hebergement VAPH handicap mental)",
    "name_en": "Ons Tehuis-Brabant ASBL (Kampenhout VAPH residential mental-disability care)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.onstehuisbrabant.be/",
    "foi_email": "info@otbvzw.be",
    "foi_postal": ADDR,
    "notes": f"tick{TICK} YE2025 Medium CW + Strong KBO {KBO} Actief 1 VE RSZ 87.202 aanbestedende overheid; omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE}; FOI {GAP}",
}], "entity_id")

append_csv(data / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Kampenhout>Ons_Tehuis_Brabant>NBB_PDF_bruto_5_72x_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025 assets/debt/cash; omzet {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl {PNL}; VAPH matrix",
    "why_it_matters": f"VAPH housing VZW bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet; assets/debt unpublished",
    "priority": "8",
    "recipient_body": "Ons Tehuis-Brabant VZW",
    "recipient_email": "info@otbvzw.be",
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
    + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} leftover dual Ons Tehuis-Brabant {KBO} Medium (omzet JUMP {OMZET} +18.01%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +87.8%; equity JUMP {EQUITY}; FTE {FTE}; 1 VE Kampenhout VAPH); after Havenzate@2315; AGB Bornem JR2024; FARO/AIESH YE2024; next {RQ_NEXT}; next EVERY-10 2320; continuous hole_fill\n",
    encoding="utf-8",
)
(raw / "summary.json").write_text(json.dumps({"tick": TICK, "unit": RQ, "entity": ENTITY, "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "ratio": RATIO, "confidence": "medium", "pi": PI}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(f"Ons Tehuis-Brabant YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} FTE {FTE} filed 07.07.2026\n", encoding="utf-8")
(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — Ons Tehuis-Brabant (NBB PDF / bruto~{RATIO}x / pnl JUMP +88%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ons Tehuis-Brabant VZW — KBO **{KBO}** (Actief; {ADDR}; **1 VE**; FTE {FTE}; RSZ **87.202**; VAPH; aanbestedende overheid)  
**recipient:** info@otbvzw.be · {ADDR} (T 016 65 91 10)  
**tick:** {TICK}  
**confidence:** Medium

## Context
CW YE2025: omzet **EUR{OMZET:,}** JUMP +18.01%; bruto **EUR{BRUTO:,}** (~{RATIO}x); pnl **EUR{PNL:,}** JUMP +87.8%; FTE **{FTE}**; filed **07.07.2026**.

## Brief
```text
Aan: Ons Tehuis-Brabant VZW via info@otbvzw.be
Betreft: Openbaarmaking jaarrekening 2025 (KBO {KBO})
1. NBB PDF YE2025 assets/debt/cash
2. Toelichting omzet/bruto~{RATIO}x/pnl JUMP/FTE
3. VAPH-toelagen matrix
Ref: {GAP}
```
- [x] ready NOT sent
""", encoding="utf-8")

log = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} Ons Tehuis-Brabant Kampenhout (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP +88% / FTE {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Havenzate@2315**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH still **YE2024**; Gandae still **YE2024**. Took unused FREE Flemish VAPH **Ons Tehuis-Brabant VZW** YE2025 (KBO **{KBO}**; {ADDR}; **1 VE**; RSZ **87.202**; aanbestedende overheid; info@otbvzw.be). Do not redo Havenzate/Hejmen/Willekom/Iris/Huis in de Stad/Katrinahof stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +18.01%; bruto **EUR{BRUTO}** JUMP +5.55% (~{RATIO}x); pnl **EUR{PNL}** JUMP +87.8%; equity **EUR{EQUITY}** JUMP +7.85%; FTE **{FTE}** (vs {FTE_2024}); neerlegging **07.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium.
- Wrote: sources (+6); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2320**). Next: {RQ_NEXT}.
"""
text = log.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print("log ok")
print("DONE", TICK, BRUTO, RATIO, PI)

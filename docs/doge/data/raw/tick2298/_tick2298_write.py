# tick2298: De Okkernoot / Wonen en Werken Autisme YE2025 leftover dual Medium
from pathlib import Path
import csv, json
csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2298"
raw.mkdir(parents=True, exist_ok=True)

TICK, UTC = "2298", "2026-08-27T17:30:00Z"
ENTITY, KBO, KBO_DIGITS = "vzw_de_okkernoot_pajottegem", "0443.397.688", "0443397688"
OMZET, BRUTO, PNL, EQUITY, FTE = 2488539, 13441120, 2326835, 14663706, 143.3
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 1881671, 10497948, 1088580, 12427489, 126.5
RATIO = round(BRUTO / OMZET, 2)  # 5.4
GAP = "gap_de_okkernoot_nbb_pdf_assets_debt_bruto_gt_omzet_5_40x_pnl_jump_vaph_matrix_l5"
LB = "lb_de_okkernoot_bruto_13_44m_omzet_2_49m_5_40x_pnl_jump_fte_jump_jr2025"
COMM = "comm_de_okkernoot_jr2025_statutory_vaph_bruto_13_44m_5_40x_pnl_jump"
RQ, RQ_NEXT = "rq_2298", "rq_2299"
SRC_EN, SRC_NL, SRC_FR = "src_de_okkernoot_jr2025_cw_en", "src_de_okkernoot_jr2025_cw_nl", "src_de_okkernoot_jr2025_cw_fr"
SRC_KBO, SRC_SITE = "src_de_okkernoot_kbo_0443397688", "src_de_okkernoot_site_contact_2298"
ABS, COST, DIFF, PI = 7.2, 6.2, 3.0, round((7.2 + 6.2) / 2, 2)

def append_csv(path, rows, id_key):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, existing = reader.fieldnames, list(reader)
    have = {r.get(id_key) for r in existing}
    new = [r for r in rows if r.get(id_key) not in have]
    if not new:
        print(path.name, "already"); return
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(path.name, "+", len(new))

def upsert_rq():
    path = data / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, rows = reader.fieldnames, list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            r.update({
                "status": "done", "entity_id": ENTITY, "updated_utc": UTC, "blocked_gap_id": GAP,
                "title": f"leftover dual — De Okkernoot YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE})",
                "notes": f"tick{TICK}: De Okkernoot/WonenWerkenAutisme YE2025 Medium (omzet JUMP {OMZET} +32.25%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +113.75%; equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE VAPH autism Pajottegem); FOI {GAP} ready not sent; after SOBO@2297; stalls AGB/FARO/AIESH YE2024",
            })
            found = True
            break
    if not found:
        raise SystemExit("missing " + RQ)
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": "leftover dual after De Okkernoot — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill", "priority": "8", "status": "open", "hierarchy_target": "L5", "entity_id": "",
            "instructions": f"leftover dual after De Okkernoot YE2025 Medium (omzet JUMP {OMZET/1e6:.2f}m / bruto~{RATIO}x / pnl JUMP). Prefer AGB/FARO if YE2025 else unused ETA-VAPH-WZC-maatwerk (Gandae YE2024). Do NOT redo De Okkernoot/SOBO/Ryhove/Rozemarijn/Mo-Clean/NLZ/Entiris/A-kwadraat/OptimaT stack.",
            "blocked_gap_id": "", "created_utc": UTC, "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} De Okkernoot; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next EVERY-10 2300",
        })
        print("rq_next spawned", RQ_NEXT)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames); w.writeheader(); w.writerows(rows)
    print("research_queue updated")

append_csv(data / "sources.csv", [
    {"source_id": SRC_EN, "title": "De Okkernoot YE2025 Companyweb EN", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 09.07.2026; assets/debt Unknown"},
    {"source_id": SRC_NL, "title": "De Okkernoot YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/wonen-en-werken-voor-personen-met-autisme", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 09.07.2026; Groot {FTE} FTE"},
    {"source_id": SRC_FR, "title": "De Okkernoot YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif; CA {OMZET}; marge brute {BRUTO}; benefice {PNL}"},
    {"source_id": SRC_KBO, "title": f"KBO Wonen en Werken Autisme / De Okkernoot {KBO}", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW sinds 22.09.1990; 1 VE; Repingestraat 12 1570 Pajottegem sinds 01.01.2025; RSZ 87.202 / BTW 87.201+87.202; aanbestedende overheid"},
    {"source_id": SRC_SITE, "title": "De Okkernoot FOI channel info@de-okkernoot.be", "url": "https://www.de-okkernoot.be/", "publisher": "De Okkernoot VZW", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; info@de-okkernoot.be; +32 54 56 74 53; Repingestraat 12 Vollezele/Pajottegem; VAPH autism care"},
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_de_okkernoot_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; omzet JUMP +32.25% vs YE2024 {OMZET24}"},
    {"budget_id": "bud_de_okkernoot_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; bruto JUMP +28.04% vs YE2024 {BRUTO24}; bruto/omzet ~{RATIO}x"},
    {"budget_id": "bud_de_okkernoot_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; pnl JUMP +113.75% vs YE2024 {PNL24}"},
    {"budget_id": "bud_de_okkernoot_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; equity JUMP +17.99% vs YE2024 {EQUITY24}"},
    {"budget_id": "bud_de_okkernoot_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE24}; assets/debt Unknown"},
    {"budget_id": "bud_de_okkernoot_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL24), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative"},
], "budget_id")

cash = json.dumps({"2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE, "2024_omzet": OMZET24, "2024_bruto": BRUTO24, "2024_pnl": PNL24, "2024_equity": EQUITY24, "2024_fte": FTE24}, separators=(",", ":"))
append_csv(data / "commitments.csv", [{"commitment_id": COMM, "title": f"De Okkernoot YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE} / Medium)", "entity_id": ENTITY, "beneficiary": "VAPH autism / mental-disability clients Pajottenland", "legal_basis": f"VZW Wonen en Werken voor personen met Autisme / De Okkernoot (KBO {KBO}; Actief; 1 VE; RSZ 87.202; aanbestedende overheid)", "decision_date": "2026-07-09", "start_year": "2025", "end_year": "2025", "total_envelope_eur": str(BRUTO), "cash_by_year": cash, "remaining_eur": "0", "status": "active", "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}", "stated_goal": "Flemish VAPH residential + day support autism / inclusive employment Pajottegem", "cut_option": f"Publish NBB PDF assets/debt; disclose VAPH matrix behind bruto~{RATIO}x omzet", "source_id": SRC_EN, "confidence": "medium", "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Pajottegem>DeOkkernoot>JR2025_statutory_L5", "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; omzet {OMZET} ~{RATIO}x; FOI {GAP}; not TE-additive"}], "commitment_id")

append_csv(data / "leaderboard.csv", [{"item_id": LB, "name": f"De Okkernoot bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / pnl JUMP +114% / FTE JUMP {FTE} (YE2025 VAPH autism)", "level": "L5", "type": "vaph_vzw_statutory", "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Pajottegem>DeOkkernoot>JR2025", "annual_cost_eur": str(BRUTO), "total_cost_eur": str(BRUTO), "tco_notes": f"CW omzet JUMP {OMZET} (+32.25%) / bruto JUMP {BRUTO} (+28.04%; ~{RATIO}x) / pnl JUMP {PNL} (+113.75%) / equity JUMP {EQUITY} (+17.99%) / FTE JUMP {FTE} (vs {FTE24}) / 1 VE VAPH autism", "confidence": "medium", "source_id": SRC_EN, "beneficiaries": "VAPH autism / mental-disability clients Vollezele-Halle-Herne belt", "stated_goal": "Inclusive residential + day support autism spectrum", "measured_outcome": f"omzet JUMP +32.25%; bruto JUMP +28.04% (~{RATIO}x); pnl JUMP +113.75%; equity JUMP +17.99%; FTE JUMP {FTE}; filed 09.07.2026", "absurdity_score": str(ABS), "cost_score": str(COST), "difficulty": str(DIFF), "priority_index": str(PI), "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose VAPH matrix behind bruto>~{RATIO}x omzet", "status": "open", "struck_reason": "", "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after SOBO@2297; AGB/FARO/AIESH YE2024"}], "item_id")

append_csv(data / "entities.csv", [{"entity_id": ENTITY, "name_nl": "De Okkernoot / Wonen en Werken voor personen met Autisme VZW (Pajottegem)", "name_fr": "De Okkernoot / Habiter et travailler pour personnes avec autisme ASBL (Pajottegem)", "name_en": "De Okkernoot autism care ASBL (Pajottegem VAPH)", "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl", "website": "https://www.de-okkernoot.be/", "foi_email": "info@de-okkernoot.be", "foi_postal": "Repingestraat 12, 1570 Pajottegem", "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE VZW RSZ 87.202; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 09.07.2026; FOI {GAP}; aanbestedende overheid; after SOBO@2297; not TE-additive"}], "entity_id")

append_csv(data / "foi_queue.csv", [{"gap_id": GAP, "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Pajottegem>DeOkkernoot>NBB_PDF_assets_debt_bruto_gt_omzet_5_40x_pnl_jump_vaph", "entity_id": ENTITY, "what_is_missing": f"NBB PDF YE2025 full (assets/debt/cash); omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); pnl JUMP EUR{PNL}; FTE JUMP {FTE}; VAPH subsidy matrix", "why_it_matters": f"Medium CW shows VAPH autism VZW (bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet / pnl JUMP +114% / FTE JUMP); assets/debt unpublished", "priority": "8", "recipient_body": "De Okkernoot / Wonen en Werken voor personen met Autisme VZW", "recipient_email": "info@de-okkernoot.be", "recipient_postal": "Repingestraat 12, 1570 Pajottegem", "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md", "status": "ready", "date_ready": "2026-08-27", "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "", "linked_commitment_id": COMM, "linked_leaderboard_id": LB, "created_utc": UTC, "updated_utc": UTC, "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after SOBO@2297"}], "gap_id")

upsert_rq()
(data / "loop_state.csv").write_text("state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n" + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} leftover dual De Okkernoot {KBO} Medium (omzet JUMP {OMZET} +32.25%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +113.75%; equity JUMP {EQUITY} +17.99%; FTE JUMP {FTE}; 1 VE VAPH autism Pajottegem); after SOBO@2297; AGB Bornem JR2024; FARO/AIESH YE2024; next {RQ_NEXT}; next EVERY-10 2300; continuous hole_fill\n", encoding="utf-8")
(raw / "summary.json").write_text(json.dumps({"tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO, "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE, "ratio_bruto_omzet": RATIO, "confidence": "medium", "gap": GAP}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(f"De Okkernoot YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE} filed 09.07.2026 info@de-okkernoot.be\n", encoding="utf-8")
log = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} De Okkernoot Pajottegem (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **SOBO@2297**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH/Citeco/Groupe Foes still **YE2024**; Gandae YE2024. Took FREE Flemish VAPH autism dual **De Okkernoot / Wonen en Werken voor personen met Autisme VZW** YE2025 (KBO **{KBO}**; Repingestraat 12 Pajottegem; **Actief** **1 VE**; RSZ **87.202**; info@de-okkernoot.be). Do not redo SOBO/Ryhove/Rozemarijn/Mo-Clean/Entiris/A-kwadraat/OptimaT stack.
- Found: Companyweb EN YE2025 - omzet **EUR{OMZET}** JUMP +32.25%; bruto **EUR{BRUTO}** JUMP +28.04% (~{RATIO}x); pnl **EUR{PNL}** JUMP +113.75%; equity **EUR{EQUITY}** JUMP +17.99%; FTE **{FTE}** JUMP; neerlegging **09.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@de-okkernoot.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2290**; next **2300**). Next: {RQ_NEXT}.
"""
text = log.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8"); print("loop_log ok")
(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — De Okkernoot (NBB PDF / bruto~{RATIO}x omzet / pnl JUMP / VAPH)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Wonen en Werken voor personen met Autisme VZW / De Okkernoot — KBO **{KBO}** (Actief; Repingestraat 12, 1570 Pajottegem; **1 VE**; FTE {FTE}; RSZ **87.202**; VAPH autism)  
**recipient:** info@de-okkernoot.be · Repingestraat 12, 1570 Pajottegem (+32 54 56 74 53)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [site](https://www.de-okkernoot.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds **22.09.1990**; **1 VE**; zetel Repingestraat 12, 1570 Pajottegem; RSZ **87.202**; aanbestedende overheid.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +32.25%; bruto **EUR{BRUTO:,}** JUMP +28.04% (~{RATIO}x); pnl **EUR{PNL:,}** JUMP +113.75%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **09.07.2026**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After SOBO@2297.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Okkernoot / Wonen en Werken voor personen met Autisme VZW
via info@de-okkernoot.be
Repingestraat 12, 1570 Pajottegem
Betreft: Openbaarmaking jaarrekening 2025 (KBO {KBO})

Geachte,

Op grond van openbaarheid van bestuur (Vlaams Bestuursdecreet), vraag ik:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting omzet JUMP EUR{OMZET} naast bruto EUR{BRUTO} (~{RATIO}x), pnl JUMP EUR{PNL}, FTE JUMP {FTE}.
3. Overzicht VAPH-vergoedingen achter bruto~{RATIO}x omzet YE2025.
4. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("DONE", TICK, "pi", PI, "bruto", BRUTO)

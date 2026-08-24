# tick2296: Ryhove YE2025 leftover dual Medium (after Rozemarijn@2295 race)
from pathlib import Path
import csv
import json

csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2296"
raw.mkdir(parents=True, exist_ok=True)

TICK = "2296"
UTC = "2026-08-27T16:45:00Z"
ENTITY = "vzw_ryhove_gent"
KBO = "0407.215.007"
KBO_DIGITS = "0407215007"

OMZET = 8047721
BRUTO = 17669323
PNL = 1330675
EQUITY = 11953407
FTE = 406.5
OMZET_2024 = 7344248
BRUTO_2024 = 16067213
PNL_2024 = 1019355
EQUITY_2024 = 10715133
FTE_2024 = 388.5
RATIO = round(BRUTO / OMZET, 2)

GAP = "gap_ryhove_nbb_pdf_assets_debt_bruto_gt_omzet_2_20x_pnl_jump_fte_jump_matrix_l5"
LB = "lb_ryhove_bruto_17_67m_omzet_8_05m_2_20x_pnl_jump_fte_jump_jr2025"
COMM = "comm_ryhove_jr2025_statutory_maatwerk_bruto_17_67m_2_20x_pnl_jump"
RQ = "rq_2296"
RQ_NEXT = "rq_2297"

SRC_EN = "src_ryhove_jr2025_cw_en"
SRC_NL = "src_ryhove_jr2025_cw_nl"
SRC_FR = "src_ryhove_jr2025_cw_fr"
SRC_KBO = "src_ryhove_kbo_0407215007"
SRC_SITE = "src_ryhove_site_contact_2296"

ABS, COST, DIFF = 5.5, 6.5, 3.0
PI = round((ABS + COST) / 2, 2)


def append_csv(path: Path, rows: list[dict], id_key: str):
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


def upsert_research_queue():
    path = data / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["updated_utc"] = UTC
            r["blocked_gap_id"] = GAP
            r["notes"] = (
                f"tick{TICK}: Ryhove YE2025 Medium (omzet JUMP {OMZET} +9.58%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +30.54%; equity JUMP {EQUITY}; "
                f"FTE JUMP {FTE}; 3 VE Gent maatwerk); FOI {GAP} ready not sent; "
                f"after Rozemarijn@2295; stalls AGB/FARO/AIESH YE2024"
            )
            r["title"] = (
                f"leftover dual — Ryhove YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m "
                f"/ ~{RATIO}x omzet / pnl JUMP +30.54% / FTE JUMP {FTE})"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"missing {RQ}")
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": (
                "leftover dual after Ryhove — prefer AGB/FARO-YE2025/AIESH/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Ryhove YE2025 Medium (omzet JUMP {OMZET/1e6:.2f}m / "
                f"bruto~{RATIO}x / pnl JUMP / FTE JUMP {FTE}). Prefer leftover dual: AGB Bornem/APB → "
                "FARO/AIESH/REW if YE2025 → unused DSO/water/nuclear/IGS/HVZ or FREE "
                "ETA-VAPH-WZC-maatwerk (SOBO/Gandae still YE2024). "
                "Do NOT redo Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ/Labor/Intro/Ateljee/"
                "Borgerstein/Waak/InterWest/BWB/Wroeter/Springplank/Ecoso/De Brug stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Ryhove; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; "
                "AGB Bornem JR2024; Gandae/SOBO YE2024; next EVERY-10 2300"
            ),
        })
        print("rq_next spawned", RQ_NEXT)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print("research_queue updated")


append_csv(data / "sources.csv", [
    {"source_id": SRC_EN, "title": "Ryhove YE2025 Companyweb EN", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 08.05.2026; assets/debt Unknown"},
    {"source_id": SRC_NL, "title": "Ryhove YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/ryhove", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 08.05.2026; Groot {FTE} FTE"},
    {"source_id": SRC_FR, "title": "Ryhove YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/ryhove", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Gent; CA {OMZET}; marge brute {BRUTO}; benefice {PNL}"},
    {"source_id": SRC_KBO, "title": f"KBO Ryhove {KBO}", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW Ryhove sinds 01.01.1961; 3 VE; Koningsdal 24 9000 Gent; RSZ/BTW NACE 88.993; info@ryhove.be"},
    {"source_id": SRC_SITE, "title": "Ryhove FOI channel info@ryhove.be", "url": "https://www.ryhove.be/", "publisher": "Ryhove VZW", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; info@ryhove.be; +32 9 226 29 37; Koningsdal 24 9000 Gent"},
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_ryhove_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; omzet JUMP +9.58% vs YE2024 {OMZET_2024}"},
    {"budget_id": "bud_ryhove_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; bruto JUMP +9.97% vs YE2024 {BRUTO_2024}; bruto/omzet ~{RATIO}x"},
    {"budget_id": "bud_ryhove_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; pnl JUMP +30.54% vs YE2024 {PNL_2024}"},
    {"budget_id": "bud_ryhove_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; equity JUMP +11.56% vs YE2024 {EQUITY_2024}"},
    {"budget_id": "bud_ryhove_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE_2024}; assets/debt Unknown"},
    {"budget_id": "bud_ryhove_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL_2024), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL_2024} comparative"},
], "budget_id")

cash = json.dumps({"2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE, "2024_omzet": OMZET_2024, "2024_bruto": BRUTO_2024, "2024_pnl": PNL_2024, "2024_equity": EQUITY_2024, "2024_fte": FTE_2024}, separators=(",", ":"))
append_csv(data / "commitments.csv", [{"commitment_id": COMM, "title": f"Ryhove YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE} / Medium)", "entity_id": ENTITY, "beneficiary": "Maatwerkers Gent / Ryhove Urban Factory path", "legal_basis": f"VZW Ryhove (KBO {KBO}; Actief; 3 VE; RSZ/BTW 88.993; Gent)", "decision_date": "2026-05-08", "start_year": "2025", "end_year": "2025", "total_envelope_eur": str(BRUTO), "cash_by_year": cash, "remaining_eur": "0", "status": "active", "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}", "stated_goal": "Flemish maatwerk / adapted work Gent inclusive employment", "cut_option": f"Publish NBB PDF assets/debt; disclose Vlaamse maatwerk matrix behind bruto~{RATIO}x omzet", "source_id": SRC_EN, "confidence": "medium", "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Ryhove>JR2025_statutory_L5", "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; omzet {OMZET} ~{RATIO}x; FOI {GAP}; not TE-additive"}], "commitment_id")

append_csv(data / "leaderboard.csv", [{"item_id": LB, "name": f"Ryhove bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / pnl JUMP +30.5% / FTE JUMP {FTE} (YE2025 Gent maatwerk)", "level": "L5", "type": "maatwerk_vzw_statutory", "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Ryhove>JR2025", "annual_cost_eur": str(BRUTO), "total_cost_eur": str(BRUTO), "tco_notes": f"CW omzet JUMP {OMZET} (+9.58%) / bruto JUMP {BRUTO} (+9.97%; ~{RATIO}x) / pnl JUMP {PNL} (+30.54%) / equity JUMP {EQUITY} (+11.56%) / FTE JUMP {FTE} (vs {FTE_2024}) / 3 VE", "confidence": "medium", "source_id": SRC_EN, "beneficiaries": "Maatwerkers Gent region / Ryhove Urban Factory", "stated_goal": "Flemish maatwerkbedrijf / inclusive employment Gent", "measured_outcome": f"omzet JUMP +9.58%; bruto JUMP +9.97% (~{RATIO}x); pnl JUMP +30.54%; equity JUMP +11.56%; FTE JUMP {FTE}; filed 08.05.2026", "absurdity_score": str(ABS), "cost_score": str(COST), "difficulty": str(DIFF), "priority_index": str(PI), "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose Vlaamse maatwerk matrix behind bruto>~{RATIO}x omzet", "status": "open", "struck_reason": "", "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after Rozemarijn@2295; AGB/FARO/AIESH YE2024"}], "item_id")

append_csv(data / "entities.csv", [{"entity_id": ENTITY, "name_nl": "Ryhove VZW (Gent / Vlaams maatwerk)", "name_fr": "Ryhove ASBL (Gand / entreprise de travail adapte flamande)", "name_en": "Ryhove adapted-work ASBL (Ghent Flemish maatwerk)", "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl", "website": "https://www.ryhove.be/", "foi_email": "info@ryhove.be", "foi_postal": "Koningsdal 24, 9000 Gent", "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 3 VE VZW RSZ/BTW 88.993; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 08.05.2026; FOI {GAP}; after Rozemarijn@2295; not TE-additive"}], "entity_id")

append_csv(data / "foi_queue.csv", [{"gap_id": GAP, "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Ryhove>NBB_PDF_assets_debt_bruto_gt_omzet_2_20x_pnl_jump_fte_jump", "entity_id": ENTITY, "what_is_missing": f"NBB PDF YE2025 full (assets/debt/cash); omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); pnl JUMP EUR{PNL}; FTE JUMP {FTE}; Vlaamse maatwerk subsidy matrix", "why_it_matters": f"Medium CW shows large Gent maatwerk VZW (bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet / pnl JUMP / FTE JUMP to {FTE}); assets/debt unpublished", "priority": "8", "recipient_body": "Ryhove VZW", "recipient_email": "info@ryhove.be", "recipient_postal": "Koningsdal 24, 9000 Gent", "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md", "status": "ready", "date_ready": "2026-08-27", "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "", "linked_commitment_id": COMM, "linked_leaderboard_id": LB, "created_utc": UTC, "updated_utc": UTC, "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Rozemarijn@2295"}], "gap_id")

upsert_research_queue()
(data / "loop_state.csv").write_text("state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n" + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} leftover dual Ryhove {KBO} Medium (omzet JUMP {OMZET} +9.58%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +30.54%; equity JUMP {EQUITY} +11.56%; FTE JUMP {FTE}; 3 VE Gent maatwerk); after Rozemarijn@2295 / Mo-Clean@2294; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {RQ_NEXT}; next EVERY-10 2300; continuous hole_fill\n", encoding="utf-8")
print("loop_state ok")
(raw / "summary.json").write_text(json.dumps({"tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO, "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE, "ratio_bruto_omzet": RATIO, "confidence": "medium", "gap": GAP}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(f"Ryhove YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE} filed 08.05.2026 info@ryhove.be\n", encoding="utf-8")

log_path = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} Ryhove Gent (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Rozemarijn@2295**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW/Citeco/Groupe Foes still **YE2024**; Gandae/SOBO/APN still **YE2024**. Took unused FREE Flemish maatwerk **Ryhove VZW** YE2025 (KBO **{KBO}**; Koningsdal 24 Gent; **Actief** **3 VE**; RSZ/BTW **88.993**; info@ryhove.be). Do not redo Rozemarijn/Mo-Clean/Den Azalee/NLZ/Waak/InterWest/BWB/Wroeter/Springplank/Ateljee/Borgerstein stack.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +9.58% vs YE2024 EUR{OMZET_2024}; bruto **EUR{BRUTO}** JUMP +9.97% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** JUMP +30.54%; equity **EUR{EQUITY}** JUMP +11.56%; FTE **{FTE}** JUMP (vs {FTE_2024}); neerlegging **08.05.2026**. Strong KBO Actief 3 VE VZW. Assets/debt Unknown. Medium. FOI via info@ryhove.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2290**; next **2300**). Next: {RQ_NEXT} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk SOBO-Gandae).
"""
text = log_path.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log_path.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print("loop_log ok")
else:
    print("loop_log already")

(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — Ryhove (NBB PDF / bruto~{RATIO}x omzet / pnl JUMP / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ryhove VZW — KBO **{KBO}** (Actief; Koningsdal 24, 9000 Gent; **3 VE**; FTE {FTE} CW; NACE **88.993**; Flemish maatwerk)  
**recipient:** info@ryhove.be · Koningsdal 24, 9000 Gent (+32 9 226 29 37)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}) · [CW NL](https://www.companyweb.be/nl/{KBO_DIGITS}/ryhove) · [CW FR](https://www.companyweb.be/fr/{KBO_DIGITS}/ryhove) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [site](https://www.ryhove.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Ryhove** sinds **01.01.1961**; **3 VE**; zetel Koningsdal 24, 9000 Gent; RSZ/BTW NACE **88.993**; info@ryhove.be.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +9.58%; bruto **EUR{BRUTO:,}** JUMP +9.97% (~{RATIO}x); pnl **EUR{PNL:,}** JUMP +30.54%; equity **EUR{EQUITY:,}** JUMP +11.56%; FTE **{FTE}**; filed **08.05.2026**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Citeco/Groupe Foes YE2024; Gandae/SOBO YE2024. After Rozemarijn@2295.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Ryhove VZW
via info@ryhove.be
Koningsdal 24, 9000 Gent
Betreft: Openbaarmaking jaarrekening 2025 Ryhove (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaams Bestuursdecreet e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet JUMP EUR{OMZET} (+9.58%) naast bruto EUR{BRUTO}
   (~{RATIO}x omzet), pnl JUMP EUR{PNL} (+30.54%) en FTE JUMP {FTE} (vs {FTE_2024}).
3. Overzicht van Vlaamse maatwerktoelagen achter personeelskosten (FTE {FTE}).
4. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("DONE tick", TICK, "pi", PI, "bruto", BRUTO)

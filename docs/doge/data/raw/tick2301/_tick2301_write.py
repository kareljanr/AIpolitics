# tick2301: Havinet YE2025 leftover dual Medium (after De Kiem EVERY-10@2300)
from pathlib import Path
import csv, json
csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2301"
raw.mkdir(parents=True, exist_ok=True)

TICK, UTC = "2301", "2026-08-27T18:15:00Z"
ENTITY, KBO, KBO_DIGITS = "vzw_havinet_grimbergen", "0642.602.234", "0642602234"
OMZET, BRUTO, PNL, EQUITY, FTE = 4242068, 29388752, 870523, 31190394, 365.9
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 4132111, 28148555, 791466, 29399852, 372.2
RATIO = round(BRUTO / OMZET, 2)
GAP = "gap_havinet_nbb_pdf_assets_debt_bruto_gt_omzet_6_93x_pnl_jump_vaph_matrix_l5"
LB = "lb_havinet_bruto_29_39m_omzet_4_24m_6_93x_pnl_jump_fte_drop_jr2025"
COMM = "comm_havinet_jr2025_statutory_vaph_bruto_29_39m_6_93x_pnl_jump"
RQ, RQ_NEXT = "rq_2301", "rq_2302"
SRC_EN, SRC_NL, SRC_FR = "src_havinet_jr2025_cw_en", "src_havinet_jr2025_cw_nl", "src_havinet_jr2025_cw_fr"
SRC_KBO, SRC_SITE = "src_havinet_kbo_0642602234", "src_havinet_site_contact_2301"
ABS, COST, DIFF, PI = 7.5, 6.8, 3.0, round((7.5 + 6.8) / 2, 2)

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
                "title": f"leftover dual — Havinet YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE DROP {FTE})",
                "notes": f"tick{TICK}: Havinet YE2025 Medium (omzet JUMP {OMZET} +2.66%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +9.99%; equity JUMP {EQUITY}; FTE DROP {FTE}; 11 VE VAPH Grimbergen EigenThuis+Zonnestraal+DeValier); FOI {GAP} ready not sent; after De Kiem EVERY-10@2300; stalls AGB/FARO/AIESH YE2024",
            })
            found = True
            break
    if not found:
        raise SystemExit("missing " + RQ)
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": "leftover dual after Havinet — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill", "priority": "8", "status": "open", "hierarchy_target": "L5", "entity_id": "",
            "instructions": f"leftover dual after Havinet YE2025 Medium (omzet JUMP {OMZET/1e6:.2f}m / bruto~{RATIO}x / pnl JUMP). Prefer AGB/FARO if YE2025 else unused ETA-VAPH-WZC-maatwerk (Gandae YE2024). Do NOT redo Havinet/De Kiem/JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove/Entiris/Mirto/Blankedale/Werkmmaat stack.",
            "blocked_gap_id": "", "created_utc": UTC, "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} Havinet; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next EVERY-10 2310",
        })
        print("rq_next spawned", RQ_NEXT)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames); w.writeheader(); w.writerows(rows)
    print("research_queue updated")

append_csv(data / "sources.csv", [
    {"source_id": SRC_EN, "title": "Havinet YE2025 Companyweb EN", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/havinet", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 17.07.2026; assets/debt Unknown"},
    {"source_id": SRC_NL, "title": "Havinet YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/havinet", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 17.07.2026; Groot {FTE} FTE"},
    {"source_id": SRC_FR, "title": "Havinet YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/havinet", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Grimbergen; CA {OMZET}; marge brute {BRUTO}; benefice {PNL}"},
    {"source_id": SRC_KBO, "title": f"KBO Havinet {KBO}", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW sinds 22.09.2015; 11 VE; Schildpadstraat 30 1850 Grimbergen; RSZ 87.202; aanbestedende overheid; absorbed Eigen Thuis 0414.950.162 + Zonnestraal 0415.848.601 + De Valier 0429.699.409 since 28.06.2023"},
    {"source_id": SRC_SITE, "title": "Havinet FOI channel info@havinet.be", "url": "https://havinet.be/", "publisher": "Havinet VZW", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; info@havinet.be; +32 2 269 60 06; Schildpadstraat 30 Grimbergen; VAPH Eigen Thuis / Zonnestraal"},
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_havinet_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; omzet JUMP +2.66% vs YE2024 {OMZET24}"},
    {"budget_id": "bud_havinet_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; bruto JUMP +4.41% vs YE2024 {BRUTO24}; bruto/omzet ~{RATIO}x"},
    {"budget_id": "bud_havinet_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; pnl JUMP +9.99% vs YE2024 {PNL24}"},
    {"budget_id": "bud_havinet_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; equity JUMP +6.09% vs YE2024 {EQUITY24}"},
    {"budget_id": "bud_havinet_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; FTE DROP {FTE} vs YE2024 {FTE24}; assets/debt Unknown"},
    {"budget_id": "bud_havinet_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL24), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative"},
], "budget_id")

cash = json.dumps({"2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE, "2024_omzet": OMZET24, "2024_bruto": BRUTO24, "2024_pnl": PNL24, "2024_equity": EQUITY24, "2024_fte": FTE24}, separators=(",", ":"))
append_csv(data / "commitments.csv", [{"commitment_id": COMM, "title": f"Havinet YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE DROP {FTE} / Medium)", "entity_id": ENTITY, "beneficiary": "VAPH disability clients Grimbergen Eigen Thuis / Zonnestraal / De Valier path", "legal_basis": f"VZW Havinet (KBO {KBO}; Actief; 11 VE; RSZ 87.202; aanbestedende overheid; absorbed Eigen Thuis+Zonnestraal+De Valier 28.06.2023)", "decision_date": "2026-07-17", "start_year": "2025", "end_year": "2025", "total_envelope_eur": str(BRUTO), "cash_by_year": cash, "remaining_eur": "0", "status": "active", "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/havinet", "stated_goal": "Flemish VAPH residential care disability Grimbergen campus", "cut_option": f"Publish NBB PDF assets/debt; disclose VAPH matrix behind bruto~{RATIO}x omzet", "source_id": SRC_EN, "confidence": "medium", "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Grimbergen>Havinet>JR2025_statutory_L5", "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; omzet {OMZET} ~{RATIO}x; FOI {GAP}; not TE-additive"}], "commitment_id")

append_csv(data / "leaderboard.csv", [{"item_id": LB, "name": f"Havinet bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / pnl JUMP / FTE DROP {FTE} (YE2025 VAPH Grimbergen)", "level": "L5", "type": "vaph_vzw_statutory", "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Grimbergen>Havinet>JR2025", "annual_cost_eur": str(BRUTO), "total_cost_eur": str(BRUTO), "tco_notes": f"CW omzet JUMP {OMZET} (+2.66%) / bruto JUMP {BRUTO} (+4.41%; ~{RATIO}x) / pnl JUMP {PNL} (+9.99%) / equity JUMP {EQUITY} (+6.09%) / FTE DROP {FTE} (vs {FTE24}) / 11 VE VAPH EigenThuis+Zonnestraal+DeValier", "confidence": "medium", "source_id": SRC_EN, "beneficiaries": "VAPH disability clients Grimbergen / Vlaams-Brabant belt", "stated_goal": "Inclusive residential + day support disability", "measured_outcome": f"omzet JUMP +2.66%; bruto JUMP +4.41% (~{RATIO}x); pnl JUMP +9.99%; equity JUMP +6.09%; FTE DROP {FTE}; filed 17.07.2026", "absurdity_score": str(ABS), "cost_score": str(COST), "difficulty": str(DIFF), "priority_index": str(PI), "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose VAPH matrix behind bruto>~{RATIO}x omzet", "status": "open", "struck_reason": "", "notes": f"tick{TICK}; Medium CW; FOI {GAP}; after De Kiem EVERY-10@2300; AGB/FARO/AIESH YE2024"}], "item_id")

append_csv(data / "entities.csv", [{"entity_id": ENTITY, "name_nl": "Havinet VZW (Grimbergen / VAPH Eigen Thuis + Zonnestraal + De Valier)", "name_fr": "Havinet ASBL (Grimbergen / VAPH Eigen Thuis + Zonnestraal + De Valier)", "name_en": "Havinet ASBL (Grimbergen VAPH disability care group)", "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl", "website": "https://havinet.be/", "foi_email": "info@havinet.be", "foi_postal": "Schildpadstraat 30, 1850 Grimbergen", "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 11 VE VZW RSZ 87.202; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 17.07.2026; FOI {GAP}; absorbed Eigen Thuis+Zonnestraal+De Valier 28.06.2023; after De Kiem@2300; not TE-additive"}], "entity_id")

append_csv(data / "foi_queue.csv", [{"gap_id": GAP, "hierarchy_path": "Vlaanderen>Vlaams_Brabant>Grimbergen>Havinet>NBB_PDF_assets_debt_bruto_gt_omzet_6_93x_pnl_jump_vaph", "entity_id": ENTITY, "what_is_missing": f"NBB PDF YE2025 full (assets/debt/cash); omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); pnl JUMP EUR{PNL}; FTE DROP {FTE}; VAPH subsidy matrix; post-merger Eigen Thuis/Zonnestraal/De Valier split", "why_it_matters": f"Medium CW shows large VAPH Grimbergen group (bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet / pnl JUMP / FTE 366 / 11 VE); assets/debt unpublished", "priority": "8", "recipient_body": "Havinet VZW", "recipient_email": "info@havinet.be", "recipient_postal": "Schildpadstraat 30, 1850 Grimbergen", "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md", "status": "ready", "date_ready": "2026-08-27", "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "", "linked_commitment_id": COMM, "linked_leaderboard_id": LB, "created_utc": UTC, "updated_utc": UTC, "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after De Kiem EVERY-10@2300"}], "gap_id")

upsert_rq()
(data / "loop_state.csv").write_text("state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n" + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} leftover dual Havinet {KBO} Medium (omzet JUMP {OMZET} +2.66%; bruto JUMP {BRUTO} ~{RATIO}x; pnl JUMP {PNL} +9.99%; equity JUMP {EQUITY} +6.09%; FTE DROP {FTE}; 11 VE VAPH Grimbergen); after De Kiem EVERY-10@2300; AGB Bornem JR2024; FARO/AIESH YE2024; next {RQ_NEXT}; next EVERY-10 2310; continuous hole_fill\n", encoding="utf-8")
(raw / "summary.json").write_text(json.dumps({"tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO, "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE, "ratio_bruto_omzet": RATIO, "confidence": "medium", "gap": GAP}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(f"Havinet YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE} filed 17.07.2026 info@havinet.be\n", encoding="utf-8")

log = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} Havinet Grimbergen (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE DROP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **De Kiem EVERY-10@2300** (took over stale in_progress claim). Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH/Citeco/Groupe Foes/Gandae still **YE2024**. Took FREE Flemish VAPH dual **Havinet VZW** YE2025 (KBO **{KBO}**; Schildpadstraat 30 Grimbergen; **Actief** **11 VE**; RSZ **87.202**; absorbed Eigen Thuis+Zonnestraal+De Valier; info@havinet.be). Do not redo De Kiem/JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove/Entiris/Mirto/Blankedale/Werkmmaat stack.
- Found: Companyweb EN YE2025 - omzet **EUR{OMZET}** JUMP +2.66%; bruto **EUR{BRUTO}** JUMP +4.41% (~{RATIO}x); pnl **EUR{PNL}** JUMP +9.99%; equity **EUR{EQUITY}** JUMP +6.09%; FTE **{FTE}** DROP (vs {FTE24}); neerlegging **17.07.2026**. Strong KBO Actief 11 VE. Assets/debt Unknown. Medium. FOI via info@havinet.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2300**; next **2310**). Next: {RQ_NEXT}.
"""
text = log.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8"); print("loop_log ok")

(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — Havinet (NBB PDF / bruto~{RATIO}x omzet / pnl JUMP / VAPH)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Havinet VZW — KBO **{KBO}** (Actief; Schildpadstraat 30, 1850 Grimbergen; **11 VE**; FTE {FTE}; RSZ **87.202**; VAPH; absorbed Eigen Thuis+Zonnestraal+De Valier)  
**recipient:** info@havinet.be · Schildpadstraat 30, 1850 Grimbergen (+32 2 269 60 06)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}/havinet) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [site](https://havinet.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds **22.09.2015**; **11 VE**; zetel Schildpadstraat 30 Grimbergen; RSZ **87.202**; aanbestedende overheid; absorbed Eigen Thuis / Zonnestraal / De Valier since **28.06.2023**.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +2.66%; bruto **EUR{BRUTO:,}** JUMP +4.41% (~{RATIO}x); pnl **EUR{PNL:,}** JUMP +9.99%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **17.07.2026**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After De Kiem EVERY-10@2300.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Havinet VZW
via info@havinet.be
Schildpadstraat 30, 1850 Grimbergen
Betreft: Openbaarmaking jaarrekening 2025 Havinet (KBO {KBO})

Geachte,

Op grond van openbaarheid van bestuur (Vlaams Bestuursdecreet), vraag ik:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting omzet JUMP EUR{OMZET} naast bruto EUR{BRUTO} (~{RATIO}x), pnl JUMP EUR{PNL}, FTE {FTE}.
3. Overzicht VAPH-vergoedingen achter bruto~{RATIO}x omzet; uitsplitsing Eigen Thuis / Zonnestraal / De Valier.
4. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("DONE", TICK, "pi", PI, "bruto", BRUTO)

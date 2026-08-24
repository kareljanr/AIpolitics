# tick2297: Stroom Maatwerk Antwerpen YE2025 leftover dual Medium (after Ryhove@2296)
from pathlib import Path
import csv
import json

csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2297"
raw.mkdir(parents=True, exist_ok=True)

TICK = "2297"
UTC = "2026-08-27T17:00:00Z"
ENTITY = "vzw_stroom_maatwerk_antwerpen"
KBO = "0407.839.369"
KBO_DIGITS = "0407839369"

OMZET = 9196890
BRUTO = 19463745
PNL = 437325
EQUITY = 27798223
FTE = 494.9
OMZET_2024 = 8717106
BRUTO_2024 = 18625364
PNL_2024 = 440032
EQUITY_2024 = 27427204
FTE_2024 = 489.0
RATIO = round(BRUTO / OMZET, 2)  # 2.12

GAP = "gap_stroom_nbb_pdf_assets_debt_bruto_gt_omzet_2_12x_fte_jump_matrix_l5"
LB = "lb_stroom_bruto_19_46m_omzet_9_20m_2_12x_fte_jump_jr2025"
COMM = "comm_stroom_jr2025_statutory_maatwerk_bruto_19_46m_2_12x_fte_jump"
RQ = "rq_2297"
RQ_NEXT = "rq_2298"

SRC_EN = "src_stroom_jr2025_cw_en"
SRC_NL = "src_stroom_jr2025_cw_nl"
SRC_KBO = "src_stroom_kbo_0407839369"
SRC_SITE = "src_stroom_site_contact_2297"
SRC_NBB = "src_stroom_nbb_consult_0407839369"

ABS, COST, DIFF = 5.6, 6.8, 3.0
PI = round((ABS + COST) / 2, 2)  # 6.2


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
            st = r.get("status")
            eid = (r.get("entity_id") or "").strip()
            if st == "done" and eid and eid != ENTITY:
                raise SystemExit(f"{RQ} already done by other entity={eid}")
            if st == "done" and eid == ENTITY:
                print(f"{RQ} already done self")
                found = True
                break
            if st == "in_progress" and eid and eid != ENTITY:
                raise SystemExit(f"{RQ} race-locked by entity={eid}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["updated_utc"] = UTC
            r["blocked_gap_id"] = GAP
            r["title"] = (
                f"leftover dual — Stroom Maatwerk YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m "
                f"/ ~{RATIO}x omzet / pnl DROP -0.62% / FTE JUMP {FTE})"
            )
            r["notes"] = (
                f"tick{TICK}: Stroom Maatwerk YE2025 Medium (omzet JUMP {OMZET} +5.5%; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -0.62%; equity JUMP {EQUITY}; "
                f"FTE JUMP {FTE}; 2 VE Antwerpen/Merksem maatwerk); FOI {GAP} ready not sent; "
                f"after Ryhove@2296; stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; "
                f"REW already YE2025@2289; next EVERY-10 2300"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"missing {RQ}")
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": (
                "leftover dual after Stroom — prefer AGB/FARO-YE2025/AIESH/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Stroom Maatwerk YE2025 Medium (omzet JUMP {OMZET/1e6:.2f}m / "
                f"bruto~{RATIO}x / pnl DROP / FTE JUMP {FTE}). Prefer leftover dual: AGB Bornem/APB → "
                "FARO/AIESH if YE2025 → Citeco/Groupe Foes if YE2025 → unused DSO/water/nuclear/IGS/HVZ "
                "or FREE ETA-VAPH-WZC-maatwerk (SOBO/Gandae/De Winning/De Kromme Boom still YE2024). "
                "Do NOT redo Stroom/Ryhove/Rozemarijn/De Stobbe/Mo-Clean/Den Azalee/NLZ/Labor/"
                "Intro/Buseloc/Ateljee/Borgerstein/Waak/InterWest/BWB/Wroeter/Springplank/Ecoso/De Brug stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Stroom; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "AGB Bornem JR2024; REW taken@2289 YE2025; Gandae/SOBO YE2024; next EVERY-10 2300"
            ),
        })
        print("rq_next spawned", RQ_NEXT)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print("research_queue updated")


append_csv(data / "sources.csv", [
    {
        "source_id": SRC_EN,
        "title": "Stroom Maatwerk YE2025 Companyweb EN",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/stroom-maatwerk",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 08.07.2026; assets/debt Unknown; Antwerp maatwerk",
    },
    {
        "source_id": SRC_NL,
        "title": "Stroom Maatwerk YE2025 Companyweb NL",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/stroom-maatwerk",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 08.07.2026; Groot {FTE} FTE; NACE beschutte/sociale werkplaatsen",
    },
    {
        "source_id": SRC_KBO,
        "title": f"KBO Stroom Maatwerk {KBO}",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief VZW STROOM maatwerk sinds 01.01.1960; 2 VE; Winterling 3-7 2170 Antwerpen; RSZ NACE 88.993; BTW NACE 88.999; jaarvergadering mei",
    },
    {
        "source_id": SRC_SITE,
        "title": "Stroom Maatwerk FOI channel info@stroommaatwerk.be",
        "url": "https://www.stroommaatwerk.be/",
        "publisher": "Stroom maatwerk vzw",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@stroommaatwerk.be; T 03 646 94 64; Winterling 3-7 2170 Merksem/Antwerpen; BE {KBO}",
    },
    {
        "source_id": SRC_NBB,
        "title": "NBB CBSO consult Stroom 0407839369",
        "url": f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}",
        "publisher": "NBB CBSO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; NBB consult portal for statutory PDF; CW cites filing 08.07.2026; full PDF assets/debt still FOI",
    },
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_stroom_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; omzet JUMP +5.5% vs YE2024 {OMZET_2024}"},
    {"budget_id": "bud_stroom_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; bruto JUMP +4.5% vs YE2024 {BRUTO_2024}; bruto/omzet ~{RATIO}x"},
    {"budget_id": "bud_stroom_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; pnl DROP -0.62% vs YE2024 {PNL_2024}"},
    {"budget_id": "bud_stroom_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; equity JUMP +1.35% vs YE2024 {EQUITY_2024}"},
    {"budget_id": "bud_stroom_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE_2024}; assets/debt Unknown"},
    {"budget_id": "bud_stroom_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL_2024), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL_2024} comparative"},
], "budget_id")

cash = json.dumps({
    "2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE,
    "2024_omzet": OMZET_2024, "2024_bruto": BRUTO_2024, "2024_pnl": PNL_2024, "2024_equity": EQUITY_2024, "2024_fte": FTE_2024,
}, separators=(",", ":"))

append_csv(data / "commitments.csv", [{
    "commitment_id": COMM,
    "title": f"Stroom Maatwerk YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / FTE JUMP {FTE} / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "Maatwerkers Antwerpen-Merksem / Stroom adapted-work path",
    "legal_basis": f"VZW STROOM maatwerk (KBO {KBO}; Actief; 2 VE; RSZ 88.993; BTW 88.999; Antwerpen)",
    "decision_date": "2026-07-08",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/stroom-maatwerk",
    "stated_goal": "Flemish maatwerk / adapted work Antwerp inclusive employment",
    "cut_option": f"Publish NBB PDF assets/debt; disclose Vlaamse maatwerk matrix behind bruto~{RATIO}x omzet and FTE {FTE}",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>Stroom_Maatwerk>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; omzet {OMZET} ~{RATIO}x; FOI {GAP}; not TE-additive; DISTINCT Woonstroom/Ziekenhuis aan de Stroom",
}], "commitment_id")

append_csv(data / "leaderboard.csv", [{
    "item_id": LB,
    "name": f"Stroom bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / FTE JUMP {FTE} (YE2025 Antwerp maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>Stroom_Maatwerk>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": f"CW omzet JUMP {OMZET} (+5.5%) / bruto JUMP {BRUTO} (+4.5%; ~{RATIO}x) / pnl DROP {PNL} (-0.62%) / equity JUMP {EQUITY} (+1.35%) / FTE JUMP {FTE} (vs {FTE_2024}) / 2 VE",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Maatwerkers Antwerpen-Merksem (~400 distance-to-labour-market per site narrative)",
    "stated_goal": "Flemish maatwerkbedrijf / inclusive employment Antwerp",
    "measured_outcome": f"omzet JUMP +5.5%; bruto JUMP +4.5% (~{RATIO}x); pnl DROP -0.62%; equity JUMP +1.35%; FTE JUMP {FTE}; filed 08.07.2026",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose Vlaamse maatwerk matrix behind bruto>~{RATIO}x omzet + FTE {FTE}",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW NL+EN + Strong KBO; FOI {GAP}; after Ryhove@2296; AGB/FARO/AIESH YE2024; DISTINCT Woonstroom",
}], "item_id")

append_csv(data / "entities.csv", [{
    "entity_id": ENTITY,
    "name_nl": "Stroom Maatwerk VZW (Antwerpen-Merksem / Vlaams maatwerk)",
    "name_fr": "Stroom Maatwerk ASBL (Anvers-Merksem / entreprise de travail adapte flamande)",
    "name_en": "Stroom Maatwerk adapted-work ASBL (Antwerp-Merksem Flemish maatwerk)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.stroommaatwerk.be/",
    "foi_email": "info@stroommaatwerk.be",
    "foi_postal": "Winterling 3-7, 2170 Antwerpen (Merksem)",
    "notes": f"tick{TICK} YE2025 Medium CW NL+EN + Strong KBO {KBO} Actief 2 VE VZW RSZ 88.993 BTW 88.999; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 08.07.2026; FOI {GAP}; after Ryhove@2296; DISTINCT Woonstroom wm_wstr / Ziekenhuis aan de Stroom; not TE-additive",
}], "entity_id")

append_csv(data / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>Stroom_Maatwerk>NBB_PDF_assets_debt_bruto_gt_omzet_2_12x_fte_jump",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025 full (assets/debt/cash); omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL}; FTE JUMP {FTE}; Vlaamse maatwerk subsidy matrix",
    "why_it_matters": f"Medium CW shows large Antwerp maatwerk VZW (bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet / FTE JUMP to {FTE}); assets/debt unpublished; public maatwerk subsidy opacity",
    "priority": "8",
    "recipient_body": "Stroom Maatwerk VZW",
    "recipient_email": "info@stroommaatwerk.be",
    "recipient_postal": "Winterling 3-7, 2170 Antwerpen (Merksem)",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW NL+EN + Strong KBO; after Ryhove@2296",
}], "gap_id")

upsert_research_queue()

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} leftover dual Stroom Maatwerk {KBO} Medium (omzet JUMP {OMZET} +5.5%; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -0.62%; equity JUMP {EQUITY} +1.35%; FTE JUMP {FTE}; 2 VE Antwerpen-Merksem maatwerk); after Ryhove@2296; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; REW@2289; next {RQ_NEXT}; next EVERY-10 2300; continuous hole_fill\n",
    encoding="utf-8",
)
print("loop_state ok")

(raw / "summary.json").write_text(json.dumps({
    "tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO,
    "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE,
    "ratio_bruto_omzet": RATIO, "confidence": "medium", "gap": GAP, "pi": PI,
}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(
    f"Stroom Maatwerk YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE} filed 08.07.2026 info@stroommaatwerk.be\n",
    encoding="utf-8",
)

log_path = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} Stroom Maatwerk Antwerpen (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl DROP / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Ryhove@2296**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/Citeco/Groupe Foes still **YE2024**; REW already taken YE2025@2289; Gandae/SOBO/De Winning/De Kromme Boom still **YE2024**. Took unused FREE Flemish maatwerk **Stroom Maatwerk VZW** YE2025 (KBO **{KBO}**; Winterling 3-7 Antwerpen/Merksem; **Actief** **2 VE**; RSZ **88.993**; info@stroommaatwerk.be). Do not redo Ryhove/Rozemarijn/De Stobbe/Mo-Clean/Labor/Intro/Buseloc/Waak/InterWest/BWB stack.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +5.5% vs YE2024 EUR{OMZET_2024}; bruto **EUR{BRUTO}** JUMP +4.5% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** DROP -0.62%; equity **EUR{EQUITY}** JUMP +1.35%; FTE **{FTE}** JUMP (vs {FTE_2024}); neerlegging **08.07.2026**. Strong KBO Actief 2 VE VZW. Assets/debt Unknown. Medium. FOI via info@stroommaatwerk.be.
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

(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — Stroom Maatwerk (NBB PDF / bruto~{RATIO}x omzet / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Stroom Maatwerk VZW — KBO **{KBO}** (Actief; Winterling 3-7, 2170 Antwerpen/Merksem; **2 VE**; FTE {FTE} CW; NACE **88.993**; Flemish maatwerk)  
**recipient:** info@stroommaatwerk.be · Winterling 3-7, 2170 Merksem (T 03 646 94 64)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}/stroom-maatwerk) · [CW NL](https://www.companyweb.be/nl/{KBO_DIGITS}/stroom-maatwerk) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}) · [site](https://www.stroommaatwerk.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **STROOM maatwerk** sinds **01.01.1960**; **2 VE**; zetel Winterling 3-7, 2170 Antwerpen; RSZ NACE **88.993**; BTW NACE **88.999**; info@stroommaatwerk.be.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +5.5%; bruto **EUR{BRUTO:,}** JUMP +4.5% (~{RATIO}x); pnl **EUR{PNL:,}** DROP -0.62%; equity **EUR{EQUITY:,}** JUMP +1.35%; FTE **{FTE}**; filed **08.07.2026**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; REW already@2289. After Ryhove@2296. DISTINCT Woonstroom / Ziekenhuis aan de Stroom.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Stroom Maatwerk VZW
via info@stroommaatwerk.be
Winterling 3-7, 2170 Merksem (Antwerpen)
Betreft: Openbaarmaking jaarrekening 2025 Stroom Maatwerk (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaams Bestuursdecreet e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet JUMP EUR{OMZET} (+5.5%) naast bruto EUR{BRUTO}
   (~{RATIO}x omzet), pnl DROP EUR{PNL} (-0.62%) en FTE JUMP {FTE} (vs {FTE_2024}).
3. Overzicht van Vlaamse maatwerktoelagen achter personeelskosten (FTE {FTE}).
4. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("DONE tick", TICK, "pi", PI, "bruto", BRUTO)

# tick2298: JOMI Jobs & Milieu Sint-Niklaas YE2025 leftover dual Medium (after SOBO@2297)
from pathlib import Path
import csv
import json

csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2298"
raw.mkdir(parents=True, exist_ok=True)

TICK = "2298"
UTC = "2026-08-27T17:15:00Z"
ENTITY = "vzw_jomi_jobs_milieu_sint_niklaas"
KBO = "0465.817.952"
KBO_DIGITS = "0465817952"

OMZET = None  # unpublished
BRUTO = 1975037
PNL = 60113
EQUITY = 1463137
FTE = 46.2
BRUTO_2024 = 1657656
PNL_2024 = 89667
EQUITY_2024 = 1407273
FTE_2024 = 41.1

GAP = "gap_jomi_nbb_pdf_assets_debt_empty_omzet_bruto_1_98m_pnl_drop_33pct_fte_jump_matrix_l5"
LB = "lb_jomi_bruto_1_98m_empty_omzet_pnl_drop_fte_jump_jr2025"
COMM = "comm_jomi_jr2025_statutory_maatwerk_bruto_1_98m_empty_omzet_pnl_drop"
RQ = "rq_2298"
RQ_NEXT = "rq_2299"

SRC_EN = "src_jomi_jr2025_cw_en"
SRC_NL = "src_jomi_jr2025_cw_nl"
SRC_FR = "src_jomi_jr2025_cw_fr"
SRC_KBO = "src_jomi_kbo_0465817952"
SRC_SITE = "src_jomi_site_contact_2298"
SRC_NBB = "src_jomi_nbb_consult_0465817952"

ABS, COST, DIFF = 5.0, 4.6, 3.0
PI = round((ABS + COST) / 2, 2)  # 4.8


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
                f"leftover dual — JOMI YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m / empty omzet / "
                f"pnl DROP -33% / FTE JUMP {FTE})"
            )
            r["notes"] = (
                f"tick{TICK}: JOMI Jobs&Milieu YE2025 Medium (empty omzet; bruto JUMP {BRUTO} +19.15%; "
                f"pnl DROP {PNL} -32.96%; equity JUMP {EQUITY}; FTE JUMP {FTE}; 2 VE Sint-Niklaas groen-maatwerk); "
                f"FOI {GAP} ready not sent; after SOBO@2297; stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; "
                f"Gandae YE2024; next EVERY-10 2300"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"missing {RQ}")
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": (
                "leftover dual after JOMI — prefer AGB/FARO-YE2025/AIESH/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after JOMI YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m / empty omzet / "
                f"pnl DROP -33% / FTE JUMP {FTE}). Prefer leftover dual: AGB Bornem/APB → "
                "FARO/AIESH if YE2025 → Citeco/Groupe Foes if YE2025 → unused DSO/water/nuclear/IGS/HVZ "
                "or FREE ETA-VAPH-WZC-maatwerk (Gandae if YE2025). "
                "Do NOT redo JOMI/SOBO/Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ/Labor/"
                "Intro/Buseloc/Ateljee/Borgerstein/Waak/InterWest/BWB/Wroeter/Springplank/Stroom stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} JOMI; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "AGB Bornem JR2024; Gandae YE2024; next EVERY-10 2300"
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
        "title": "JOMI Jobs & Milieu YE2025 Companyweb EN",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/jobs-milieu",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; empty omzet; bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 09.06.2026; assets/debt Unknown; Sint-Niklaas groen maatwerk",
    },
    {
        "source_id": SRC_NL,
        "title": "JOMI Jobs & Milieu YE2025 Companyweb NL",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/jobs-milieu",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 09.06.2026; Middelgroot {FTE} FTE; NACE beschutte/sociale werkplaatsen; omzet unpublished",
    },
    {
        "source_id": SRC_FR,
        "title": "JOMI Jobs & Milieu YE2025 Companyweb FR",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/jobs-milieu",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; CA non publié; marge brute {BRUTO}; FTE {FTE}",
    },
    {
        "source_id": SRC_KBO,
        "title": f"KBO JOMI Jobs & Milieu {KBO}",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief VZW Jobs & Milieu / afk JOMI sinds 27.01.1999; 2 VE; Driegaaienstraat 184 9100 Sint-Niklaas; RSZ NACE 88.993; BTW NACE 81.300 landschapsverzorging; jaarvergadering mei",
    },
    {
        "source_id": SRC_SITE,
        "title": "JOMI FOI channel info@jomi-vzw.be",
        "url": "https://www.doeners.be/aanbod/jobs-en-milieu-vzw",
        "publisher": "Doeners / JOMI listing",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@jomi-vzw.be; T 03 776 10 59; Driegaaienstraat 184 9100 Sint-Niklaas; BE {KBO}",
    },
    {
        "source_id": SRC_NBB,
        "title": "NBB CBSO consult JOMI 0465817952",
        "url": f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}",
        "publisher": "NBB CBSO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; NBB consult portal for statutory PDF; CW cites filing 09.06.2026; full PDF assets/debt still FOI",
    },
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_jomi_omzet_jr2025_statutory_empty", "entity_id": ENTITY, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; omzet unpublished / empty on CW YE2025"},
    {"budget_id": "bud_jomi_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; bruto JUMP +19.15% vs YE2024 {BRUTO_2024}; empty omzet"},
    {"budget_id": "bud_jomi_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; pnl DROP -32.96% vs YE2024 {PNL_2024}"},
    {"budget_id": "bud_jomi_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; equity JUMP +3.97% vs YE2024 {EQUITY_2024}"},
    {"budget_id": "bud_jomi_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE_2024}; assets/debt Unknown"},
    {"budget_id": "bud_jomi_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL_2024), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL_2024} comparative"},
], "budget_id")

cash = json.dumps({
    "2025_omzet": None, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE,
    "2024_bruto": BRUTO_2024, "2024_pnl": PNL_2024, "2024_equity": EQUITY_2024, "2024_fte": FTE_2024,
}, separators=(",", ":"))

append_csv(data / "commitments.csv", [{
    "commitment_id": COMM,
    "title": f"JOMI YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / empty omzet / pnl DROP / FTE JUMP {FTE} / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "Maatwerkers Sint-Niklaas / JOMI green adapted-work path",
    "legal_basis": f"VZW Jobs & Milieu / JOMI (KBO {KBO}; Actief; 2 VE; RSZ 88.993; BTW 81.300; Sint-Niklaas)",
    "decision_date": "2026-06-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/jobs-milieu",
    "stated_goal": "Flemish maatwerk / green landscaping inclusive employment Sint-Niklaas",
    "cut_option": "Publish NBB PDF assets/debt; disclose omzet + Vlaamse maatwerk matrix behind empty-omzet bruto 1.98m and FTE 46.2",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>JOMI>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; empty omzet; FOI {GAP}; not TE-additive; DISTINCT Mo-Clean/Den Azalee (board link only)",
}], "commitment_id")

append_csv(data / "leaderboard.csv", [{
    "item_id": LB,
    "name": f"JOMI bruto {BRUTO/1e6:.2f}m / empty omzet / pnl DROP -33% / FTE JUMP {FTE} (YE2025 Sint-Niklaas maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>JOMI>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": f"CW empty omzet / bruto JUMP {BRUTO} (+19.15%) / pnl DROP {PNL} (-32.96%) / equity JUMP {EQUITY} (+3.97%) / FTE JUMP {FTE} (vs {FTE_2024}) / 2 VE",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Maatwerkers Sint-Niklaas green/landscaping adapted work",
    "stated_goal": "Flemish maatwerkbedrijf / inclusive green employment Sint-Niklaas",
    "measured_outcome": f"empty omzet; bruto JUMP +19.15%; pnl DROP -32.96%; equity JUMP +3.97%; FTE JUMP {FTE}; filed 09.06.2026",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose omzet + Vlaamse maatwerk matrix behind empty-omzet bruto {BRUTO/1e6:.2f}m + FTE {FTE}",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW NL+EN+FR + Strong KBO; FOI {GAP}; after SOBO@2297; AGB/FARO/AIESH YE2024; DISTINCT Mo-Clean/Den Azalee",
}], "item_id")

append_csv(data / "entities.csv", [{
    "entity_id": ENTITY,
    "name_nl": "JOMI / Jobs & Milieu VZW (Sint-Niklaas / Vlaams groen-maatwerk)",
    "name_fr": "JOMI / Jobs & Milieu ASBL (Saint-Nicolas / entreprise de travail adapte verte flamande)",
    "name_en": "JOMI / Jobs & Milieu adapted-work ASBL (Sint-Niklaas Flemish green maatwerk)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.doeners.be/aanbod/jobs-en-milieu-vzw",
    "foi_email": "info@jomi-vzw.be",
    "foi_postal": "Driegaaienstraat 184, 9100 Sint-Niklaas",
    "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE VZW RSZ 88.993 BTW 81.300; empty omzet; bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 09.06.2026; FOI {GAP}; after SOBO@2297; DISTINCT Mo-Clean/Den Azalee; not TE-additive",
}], "entity_id")

append_csv(data / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Sint-Niklaas>JOMI>NBB_PDF_assets_debt_empty_omzet_bruto_1_98m_pnl_drop_fte_jump",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025 full (assets/debt/cash); empty omzet vs bruto EUR{BRUTO}; pnl DROP EUR{PNL}; FTE JUMP {FTE}; Vlaamse maatwerk subsidy matrix",
    "why_it_matters": f"Medium CW shows Sint-Niklaas green maatwerk VZW (bruto {BRUTO/1e6:.2f}m / empty omzet / pnl DROP -33% / FTE JUMP to {FTE}); assets/debt unpublished; public maatwerk subsidy opacity",
    "priority": "8",
    "recipient_body": "Jobs & Milieu VZW (JOMI)",
    "recipient_email": "info@jomi-vzw.be",
    "recipient_postal": "Driegaaienstraat 184, 9100 Sint-Niklaas",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW NL+EN+FR + Strong KBO; after SOBO@2297",
}], "gap_id")

upsert_research_queue()

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} leftover dual JOMI {KBO} Medium (empty omzet; bruto JUMP {BRUTO} +19.15%; pnl DROP {PNL} -32.96%; equity JUMP {EQUITY}; FTE JUMP {FTE}; 2 VE Sint-Niklaas groen-maatwerk); after SOBO@2297; AGB Bornem JR2024; FARO/AIESH YE2024; Gandae YE2024; next {RQ_NEXT}; next EVERY-10 2300; continuous hole_fill\n",
    encoding="utf-8",
)
print("loop_state ok")

(raw / "summary.json").write_text(json.dumps({
    "tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO,
    "omzet": None, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE,
    "confidence": "medium", "gap": GAP, "pi": PI,
}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(
    f"JOMI YE2025 empty omzet bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE} filed 09.06.2026 info@jomi-vzw.be\n",
    encoding="utf-8",
)
(raw / "_tick2298_write.py").write_text(Path(__file__).read_text(encoding="utf-8") if False else "", encoding="utf-8")

log_path = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} JOMI Jobs & Milieu Sint-Niklaas (bruto JUMP {BRUTO/1e6:.2f}m / empty omzet / pnl DROP -33% / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **SOBO@2297**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Gandae still **YE2024**. Took unused FREE Flemish groen-maatwerk **JOMI / Jobs & Milieu VZW** YE2025 (KBO **{KBO}**; Driegaaienstraat 184 Sint-Niklaas; **Actief** **2 VE**; RSZ **88.993**; BTW **81.300**; info@jomi-vzw.be). Do not redo SOBO/Ryhove/Rozemarijn/Mo-Clean/Den Azalee/NLZ/Labor/Intro/Buseloc/Ateljee/Borgerstein/Waak/InterWest/BWB/Wroeter/Springplank/Stroom stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +19.15% vs YE2024 EUR{BRUTO_2024}; pnl **EUR{PNL}** DROP -32.96% vs YE2024 EUR{PNL_2024}; equity **EUR{EQUITY}** JUMP +3.97%; FTE **{FTE}** JUMP (vs {FTE_2024}); neerlegging **09.06.2026**. Strong KBO Actief 2 VE VZW. Assets/debt Unknown. Medium. FOI via info@jomi-vzw.be.
- Wrote: sources (+6); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2290**; next **2300**). Next: {RQ_NEXT} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk Gandae-if-YE2025).
"""
text = log_path.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log_path.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print("loop_log ok")
else:
    print("loop_log already")

(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — JOMI Jobs & Milieu (NBB PDF / empty omzet / bruto 1.98m / pnl DROP -33%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Jobs & Milieu VZW (JOMI) — KBO **{KBO}** (Actief; Driegaaienstraat 184, 9100 Sint-Niklaas; **2 VE**; FTE {FTE} CW; RSZ **88.993**; BTW **81.300**)  
**recipient:** info@jomi-vzw.be · Driegaaienstraat 184, 9100 Sint-Niklaas (T 03 776 10 59)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}/jobs-milieu) · [CW NL](https://www.companyweb.be/nl/{KBO_DIGITS}/jobs-milieu) · [CW FR](https://www.companyweb.be/fr/{KBO_DIGITS}/jobs-milieu) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}) · [contact listing](https://www.doeners.be/aanbod/jobs-en-milieu-vzw)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN+FR YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Jobs & Milieu** / afk **JOMI** sinds **27.01.1999**; **2 VE**; zetel Driegaaienstraat 184, 9100 Sint-Niklaas; RSZ NACE **88.993**; BTW NACE **81.300** landschapsverzorging.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +19.15%; pnl **EUR{PNL:,}** DROP −32.96%; equity **EUR{EQUITY:,}** JUMP +3.97%; FTE **{FTE}**; filed **09.06.2026**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024. After SOBO@2297. DISTINCT Mo-Clean/Den Azalee (board link only).

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Jobs & Milieu VZW (JOMI)
via info@jomi-vzw.be
Driegaaienstraat 184, 9100 Sint-Niklaas
Betreft: Openbaarmaking jaarrekening 2025 JOMI (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaams Bestuursdecreet e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij unpublished omzet naast bruto JUMP EUR{BRUTO} (+19.15%),
   pnl DROP EUR{PNL} (−32.96%) en FTE JUMP {FTE} (vs {FTE_2024}).
3. Overzicht van Vlaamse maatwerktoelagen achter personeelskosten (FTE {FTE}).
4. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("DONE tick", TICK, "pi", PI, "bruto", BRUTO)

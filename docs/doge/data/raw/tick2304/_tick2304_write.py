# tick2304: Levensvreugde Verblijven YE2025 leftover dual Medium
from pathlib import Path
import csv
import json

csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2304"
raw.mkdir(parents=True, exist_ok=True)

TICK, UTC = "2304", "2026-08-27T19:15:00Z"
ENTITY, KBO, KBO_DIGITS = "vzw_levensvreugde_verblijven_aalst", "0441.398.401", "0441398401"
OMZET, BRUTO, PNL, EQUITY, FTE = 2133748, 12474923, 232887, 8353853, 161.8
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 2016766, 11518261, 177332, 8163688, 155.6
RATIO = round(BRUTO / OMZET, 2)
GAP = "gap_levensvreugde_nbb_pdf_assets_debt_bruto_gt_omzet_5_85x_pnl_jump_vaph_matrix_l5"
LB = "lb_levensvreugde_bruto_12_47m_omzet_2_13m_5_85x_pnl_jump_fte_jump_jr2025"
COMM = "comm_levensvreugde_jr2025_statutory_vaph_bruto_12_47m_5_85x_pnl_jump"
RQ, RQ_NEXT = "rq_2304", "rq_2305"
SRC_EN = "src_levensvreugde_jr2025_cw_en"
SRC_NL = "src_levensvreugde_jr2025_cw_nl"
SRC_FR = "src_levensvreugde_jr2025_cw_fr"
SRC_KBO = "src_levensvreugde_kbo_0441398401"
SRC_SITE = "src_levensvreugde_site_contact_2304"
ABS, COST, DIFF, PI = 7.3, 6.2, 3.0, round((7.3 + 6.2) / 2, 2)


def append_csv(path, rows, id_key):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, existing = reader.fieldnames, list(reader)
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


def upsert_rq():
    path = data / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, rows = reader.fieldnames, list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            r.update({
                "status": "done",
                "entity_id": ENTITY,
                "updated_utc": UTC,
                "blocked_gap_id": GAP,
                "title": (
                    f"leftover dual — Levensvreugde Verblijven YE2025 Medium "
                    f"(bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE})"
                ),
                "notes": (
                    f"tick{TICK}: Levensvreugde Verblijven YE2025 Medium "
                    f"(omzet JUMP {OMZET} +5.8%; bruto JUMP {BRUTO} ~{RATIO}x; "
                    f"pnl JUMP {PNL} +31.33%; equity JUMP {EQUITY}; FTE JUMP {FTE}; "
                    f"5 VE VAPH Aalst); FOI {GAP} ready not sent; after Voluit@2303; "
                    f"stalls AGB/FARO/AIESH YE2024"
                ),
            })
            found = True
            break
    if not found:
        raise SystemExit("missing " + RQ)
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": (
                "leftover dual after Levensvreugde — prefer AGB/FARO-YE2025/"
                "AIESH/or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Levensvreugde YE2025 Medium "
                f"(omzet JUMP {OMZET/1e6:.2f}m / bruto~{RATIO}x / pnl JUMP). "
                "Prefer AGB/FARO if YE2025 else unused ETA-VAPH-WZC-maatwerk "
                "(Alvinnenberg FREE if YE2025; Gandae YE2024). Do NOT redo "
                "Levensvreugde/Voluit/Havinet/De Kiem/Kompas/MLP/JOMI/"
                "De Okkernoot/SOBO/Ryhove/Travie/Labor/Stroom stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Levensvreugde; FARO/AIESH YE2024; "
                "AGB Bornem JR2024; next EVERY-10 2310"
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
        "title": "Levensvreugde Verblijven YE2025 Companyweb EN",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": (
            f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} "
            f"pnl {PNL} equity {EQUITY} FTE {FTE}; filed 02.07.2026; assets/debt Unknown"
        ),
    },
    {
        "source_id": SRC_NL,
        "title": "Levensvreugde Verblijven YE2025 Companyweb NL",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/levensvreugde-verblijven",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": (
            f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; "
            f"neerlegging 02.07.2026; Groot {FTE} FTE"
        ),
    },
    {
        "source_id": SRC_FR,
        "title": "Levensvreugde Verblijven YE2025 Companyweb FR",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": (
            f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Aalst; "
            f"CA {OMZET}; marge brute {BRUTO}; benefice {PNL}"
        ),
    },
    {
        "source_id": SRC_KBO,
        "title": f"KBO Levensvreugde Verblijven {KBO}",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Strong KBO Actief VZW sinds 13.11.1989; 5 VE; "
            "Botermelkstraat 201 9300 Aalst; RSZ 87.202; "
            "levensvreugde@levensvreugde.be"
        ),
    },
    {
        "source_id": SRC_SITE,
        "title": "Levensvreugde FOI channel levensvreugde@levensvreugde.be",
        "url": "https://levensvreugde-verblijven.be/contact/",
        "publisher": "Levensvreugde Verblijven VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": (
            f"tick{TICK}; levensvreugde@levensvreugde.be; +32 53 76 79 79; "
            "Botermelkstraat 201 Aalst; VAPH vergunde zorgaanbieder"
        ),
    },
], "source_id")

append_csv(data / "budgets.csv", [
    {
        "budget_id": "bud_levensvreugde_omzet_jr2025_statutory",
        "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET),
        "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts",
        "source_id": SRC_EN, "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet JUMP +5.8% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_levensvreugde_bruto_jr2025_statutory",
        "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO),
        "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts",
        "source_id": SRC_EN, "confidence": "medium",
        "notes": (
            f"tick{TICK}; Medium CW; bruto JUMP +8.31% vs YE2024 {BRUTO24}; "
            f"bruto/omzet ~{RATIO}x"
        ),
    },
    {
        "budget_id": "bud_levensvreugde_pnl_jr2025_statutory",
        "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL),
        "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts",
        "source_id": SRC_EN, "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl JUMP +31.33% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_levensvreugde_equity_jr2025_statutory",
        "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY),
        "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts",
        "source_id": SRC_EN, "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity JUMP +2.33% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_levensvreugde_fte_jr2025_statutory",
        "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE),
        "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts",
        "source_id": SRC_EN, "confidence": "medium",
        "notes": (
            f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE24}; "
            "assets/debt Unknown"
        ),
    },
    {
        "budget_id": "bud_levensvreugde_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL24),
        "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts",
        "source_id": SRC_EN, "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative",
    },
], "budget_id")

cash = json.dumps({
    "2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL,
    "2025_equity": EQUITY, "2025_fte": FTE,
    "2024_omzet": OMZET24, "2024_bruto": BRUTO24, "2024_pnl": PNL24,
    "2024_equity": EQUITY24, "2024_fte": FTE24,
}, separators=(",", ":"))

append_csv(data / "commitments.csv", [{
    "commitment_id": COMM,
    "title": (
        f"Levensvreugde Verblijven YE2025 leftover dual "
        f"(bruto {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE} / Medium)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "VAPH disability clients Aalst / Dendermonde belt",
    "legal_basis": (
        f"VZW Levensvreugde Verblijven (KBO {KBO}; Actief; 5 VE; RSZ 87.202; VAPH vergund)"
    ),
    "decision_date": "2026-07-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
    "stated_goal": "Flemish VAPH residential + day support disability Aalst",
    "cut_option": (
        f"Publish NBB PDF assets/debt; disclose VAPH matrix behind bruto~{RATIO}x omzet"
    ),
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Aalst>Levensvreugde>JR2025_statutory_L5",
    "notes": (
        f"tick{TICK}; Medium CW; bruto primary {BRUTO}; omzet {OMZET} ~{RATIO}x; "
        f"FOI {GAP}; not TE-additive"
    ),
}], "commitment_id")

append_csv(data / "leaderboard.csv", [{
    "item_id": LB,
    "name": (
        f"Levensvreugde bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / "
        f"pnl JUMP +31% / FTE JUMP {FTE} (YE2025 VAPH Aalst)"
    ),
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Aalst>Levensvreugde>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet JUMP {OMZET} (+5.8%) / bruto JUMP {BRUTO} (+8.31%; ~{RATIO}x) / "
        f"pnl JUMP {PNL} (+31.33%) / equity JUMP {EQUITY} (+2.33%) / "
        f"FTE JUMP {FTE} (vs {FTE24}) / 5 VE VAPH Aalst"
    ),
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "VAPH disability clients Aalst / Dendermonde belt",
    "stated_goal": "Inclusive residential + day support disability",
    "measured_outcome": (
        f"omzet JUMP +5.8%; bruto JUMP +8.31% (~{RATIO}x); pnl JUMP +31.33%; "
        f"equity JUMP +2.33%; FTE JUMP {FTE}; filed 02.07.2026"
    ),
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": (
        f"Publish NBB PDF assets/debt/cash FOI; disclose VAPH matrix behind "
        f"bruto>~{RATIO}x omzet"
    ),
    "status": "open",
    "struck_reason": "",
    "notes": (
        f"tick{TICK}; Medium CW; FOI {GAP}; after Voluit@2303; AGB/FARO/AIESH YE2024"
    ),
}], "item_id")

append_csv(data / "entities.csv", [{
    "entity_id": ENTITY,
    "name_nl": "Levensvreugde Verblijven VZW (Aalst / VAPH)",
    "name_fr": "Levensvreugde Verblijven ASBL (Alost / VAPH)",
    "name_en": "Levensvreugde Verblijven ASBL (Aalst VAPH disability care)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://levensvreugde-verblijven.be/",
    "foi_email": "levensvreugde@levensvreugde.be",
    "foi_postal": "Botermelkstraat 201, 9300 Aalst",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 5 VE VZW "
        f"RSZ 87.202; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} "
        f"equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 02.07.2026; FOI {GAP}; "
        f"after Voluit@2303; not TE-additive"
    ),
}], "entity_id")

append_csv(data / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": (
        "Vlaanderen>Oost_Vlaanderen>Aalst>Levensvreugde>"
        "NBB_PDF_assets_debt_bruto_gt_omzet_5_85x_pnl_jump_vaph"
    ),
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); omzet EUR{OMZET}; "
        f"bruto EUR{BRUTO} (~{RATIO}x); pnl JUMP EUR{PNL}; FTE JUMP {FTE}; "
        "VAPH subsidy matrix"
    ),
    "why_it_matters": (
        f"Medium CW shows VAPH Aalst VZW (bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet / "
        f"pnl JUMP +31% / FTE 162 / 5 VE); assets/debt unpublished"
    ),
    "priority": "8",
    "recipient_body": "Levensvreugde Verblijven VZW",
    "recipient_email": "levensvreugde@levensvreugde.be",
    "recipient_postal": "Botermelkstraat 201, 9300 Aalst",
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
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; after Voluit@2303",
}], "gap_id")

upsert_rq()

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,"
    f"tick{TICK} leftover dual Levensvreugde {KBO} Medium "
    f"(omzet JUMP {OMZET} +5.8%; bruto JUMP {BRUTO} ~{RATIO}x; "
    f"pnl JUMP {PNL} +31.33%; equity JUMP {EQUITY} +2.33%; FTE JUMP {FTE}; "
    f"5 VE VAPH Aalst); after Voluit@2303; AGB Bornem JR2024; FARO/AIESH YE2024; "
    f"next {RQ_NEXT}; next EVERY-10 2310; continuous hole_fill\n",
    encoding="utf-8",
)

(raw / "summary.json").write_text(json.dumps({
    "tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO,
    "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE,
    "ratio_bruto_omzet": RATIO, "confidence": "medium", "gap": GAP,
}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(
    f"Levensvreugde YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) "
    f"pnl {PNL} equity {EQUITY} FTE {FTE} filed 02.07.2026 "
    f"levensvreugde@levensvreugde.be\n",
    encoding="utf-8",
)

log = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} Levensvreugde Verblijven Aalst (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl JUMP / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Voluit@2303**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH still **YE2024**. Took FREE Flemish VAPH dual **Levensvreugde Verblijven VZW** YE2025 (KBO **{KBO}**; Botermelkstraat 201 Aalst; **Actief** **5 VE**; RSZ **87.202**; levensvreugde@levensvreugde.be). Do not redo Voluit/Havinet/De Kiem/Kompas/MLP/JOMI/De Okkernoot/SOBO/Ryhove/Travie/Labor/Stroom stack.
- Found: Companyweb EN YE2025 - omzet **EUR{OMZET}** JUMP +5.8%; bruto **EUR{BRUTO}** JUMP +8.31% (~{RATIO}x); pnl **EUR{PNL}** JUMP +31.33%; equity **EUR{EQUITY}** JUMP +2.33%; FTE **{FTE}** JUMP; neerlegging **02.07.2026**. Strong KBO Actief 5 VE. Assets/debt Unknown. Medium. FOI via levensvreugde@levensvreugde.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2300**; next **2310**). Next: {RQ_NEXT}.
"""
text = log.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print("loop_log ok")

(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — Levensvreugde Verblijven (NBB PDF / bruto~{RATIO}x omzet / pnl JUMP / VAPH)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Levensvreugde Verblijven VZW — KBO **{KBO}** (Actief; Botermelkstraat 201, 9300 Aalst; **5 VE**; FTE {FTE}; RSZ **87.202**; VAPH)  
**recipient:** levensvreugde@levensvreugde.be · Botermelkstraat 201, 9300 Aalst (+32 53 76 79 79)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [site](https://levensvreugde-verblijven.be/contact/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds **13.11.1989**; **5 VE**; zetel Botermelkstraat 201 Aalst; RSZ **87.202**; levensvreugde@levensvreugde.be.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +5.8%; bruto **EUR{BRUTO:,}** JUMP +8.31% (~{RATIO}x); pnl **EUR{PNL:,}** JUMP +31.33%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **02.07.2026**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After Voluit@2303.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Levensvreugde Verblijven VZW
via levensvreugde@levensvreugde.be
Botermelkstraat 201, 9300 Aalst
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

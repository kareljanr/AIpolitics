# -*- coding: utf-8 -*-
"""Tick 2219 leftover dual — Opnieuw & Co Antwerpen YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T18:35:00Z"

ENTITY = "vzw_opnieuw_co_antwerpen"
OMZET = 6453147
BRUTO = 9202255
PNL = 569440
EQUITY = 4718001
FTE = 205.3
OMZET_PY = 6289529
BRUTO_PY = 8869111
PNL_PY = 706388
EQUITY_PY = 4016916
RATIO = round(BRUTO / OMZET, 2)  # ~1.43
OMZET_PCT = round((OMZET - OMZET_PY) / OMZET_PY * 100, 2)  # +2.60
BRUTO_PCT = round((BRUTO - BRUTO_PY) / BRUTO_PY * 100, 2)  # +3.76
PNL_PCT = round((PNL - PNL_PY) / PNL_PY * 100, 2)  # -19.39
EQUITY_PCT = round((EQUITY - EQUITY_PY) / EQUITY_PY * 100, 2)  # +17.45

SRC_EN = "src_opnieuw_co_jr2025_cw_en"
COMM = "comm_opnieuw_co_jr2025_statutory_maatwerk_omzet_jump_pnl_drop_bruto_gt_omzet"
LB = "lb_opnieuw_co_omzet_6_45m_pnl_drop_19pct_bruto_gt_omzet_1_43x_jr2025"
GAP = "gap_opnieuw_co_nbb_pdf_assets_debt_pnl_drop_bruto_gt_omzet_9ve_matrix_l5"

PI = "6.90"
ABS = "7.3"
COST = "5.0"
DIFF = "3.0"


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    idkey = cols[0]
    have = {row[idkey] for row in existing}
    added = 0
    for row in rows:
        if row.get(idkey) in have:
            print("SKIP", path.name, row.get(idkey))
            continue
        existing.append({c: row.get(c, "") for c in cols})
        added += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("append", path.name, "+", added, "total", len(existing))


def update_csv_rows(path, key, updates):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        rows = list(r)
    n = 0
    for row in rows:
        if row.get(key) in updates:
            row.update(updates[row[key]])
            n += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("update", path.name, n)


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_opnieuw_co_jr2025_cw_nl",
            title="Companyweb NL Opnieuw & Co YE2025 statutory",
            url="https://www.companyweb.be/nl/0466209120/opnieuw-co",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                f"tick2219; YE2025 omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} "
                f"(~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) "
                f"FTE {FTE}; neerlegging 09.07.2026; raw docs/doge/data/raw/tick2219/"
            ),
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Opnieuw & Co YE2025 statutory",
            url="https://www.companyweb.be/en/0466209120/opnieuw-co",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                f"tick2219; EN mirror YE2025 Medium; filed 09-07-2026; Turnover {OMZET}; "
                f"Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; Employees {FTE}; "
                f"raw tick2219/"
            ),
        ),
        dict(
            source_id="src_opnieuw_co_jr2025_cw_fr",
            title="Companyweb FR Opnieuw & Co YE2025 statutory",
            url="https://www.companyweb.be/fr/0466209120/opnieuw-co",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                f"tick2219; FR mirror YE2025 Medium; deposés 09-07-2026; CA {OMZET}; "
                f"Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2219/"
            ),
        ),
        dict(
            source_id="src_opnieuw_co_kbo_2219",
            title="KBO Opnieuw & Co 0466.209.120 Actief VZW Antwerpen 9 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0466209120",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2219; Actief VZW sinds 03.09.1998; zetel Ullensstraat 26 2610 Antwerpen "
                "sinds 10.01.2023; 9 VE; RSZ NACE 88.993; BTW NACE 47.792/47.793 reuse retail"
            ),
        ),
        dict(
            source_id="src_opnieuw_co_site_contact_2219",
            title="Opnieuw & Co FOI channel info@opnieuwenco.be",
            url="https://www.opnieuwenco.be/",
            publisher="Opnieuw & Co VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes=(
                "tick2219; info@opnieuwenco.be; Ullensstraat 26 2610 Antwerpen; "
                "kringloop/maatwerk reuse"
            ),
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_opnieuw_co_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        f"tick2219; Medium CW; omzet JUMP +{OMZET_PCT}% vs YE2024 {OMZET_PY}; primary envelope",
    ),
    (
        "bud_opnieuw_co_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        f"tick2219; Medium CW; bruto JUMP +{BRUTO_PCT}% vs YE2024 {BRUTO_PY}; bruto/omzet ~{RATIO}x",
    ),
    (
        "bud_opnieuw_co_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2219; Medium CW; pnl DROP {PNL_PCT}% vs YE2024 {PNL_PY}",
    ),
    (
        "bud_opnieuw_co_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2219; Medium CW; equity JUMP +{EQUITY_PCT}% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_opnieuw_co_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        "tick2219; Medium CW; FTE 205.3; prior-year FTE not on CW card; assets/debt Unknown",
    ),
    (
        "bud_opnieuw_co_omzet_jr2024_statutory_cmp",
        "2024",
        OMZET_PY,
        "CW statutory omzet YE2024 comparative",
        f"tick2219; YE2024 omzet {OMZET_PY} comparative",
    ),
]:
    budgets.append(
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year=year,
            amount_eur=str(amount),
            amount_min_eur=str(amount),
            amount_max_eur=str(amount),
            basis=basis,
            source_id=SRC_EN,
            confidence="medium",
            notes=notes,
        )
    )
append_csv(ROOT / "budgets.csv", budgets)

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id=COMM,
            title=(
                f"Opnieuw & Co Antwerpen YE2025 leftover dual (omzet JUMP 6.45m / "
                f"pnl DROP {PNL_PCT:.0f}% / bruto≫omzet ~{RATIO}x / Medium)"
            ),
            entity_id=ENTITY,
            beneficiary="maatwerkers / kringloop reuse clients Antwerpen 2610 / 9 VE",
            legal_basis="VZW maatwerk (KBO 0466.209.120; Actief; 9 VE; RSZ NACE 88.993)",
            decision_date="2026-07-09",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": OMZET,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_omzet": OMZET_PY,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0466209120/opnieuw-co",
            stated_goal="Sheltered employment / kringloop reuse maatwerk Antwerpen",
            cut_option=(
                f"Publish NBB PDF assets/debt FOI; disclose pnl DROP {PNL_PCT:.0f}% with "
                f"equity JUMP + bruto~{RATIO}x loonkost matrix + 9 VE allocation"
            ),
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Wilrijk>OpnieuwCo>JR2025_statutory_L5",
            notes=(
                f"tick2219; Medium CW; omzet primary; pnl DROP {PNL_PCT}% with equity JUMP "
                f"+{EQUITY_PCT}% + bruto~{RATIO}x; 9 VE; assets/debt Unknown; preferred AGB "
                "Bornem JR2024; FARO/AIESH/REW YE2024; NBSW YE2025 deferred; after Veerkracht 4 "
                "race@2218; not TE-additive of 348bn; do not redo Veerkracht4/Werkmmaat/"
                "Constructief/Deltagroep/Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen Min/ACG"
            ),
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name=(
                f"Opnieuw & Co omzet JUMP 6.45m / pnl DROP {PNL_PCT:.0f}% / "
                f"bruto≫omzet ~{RATIO}x (YE2025)"
            ),
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Wilrijk>OpnieuwCo>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=(
                f"CW omzet JUMP envelope 6.45m / bruto 9.20m (~{RATIO}x) / pnl DROP 569k "
                f"{PNL_PCT}% from YE2024 706k / equity JUMP 4.72m +{EQUITY_PCT}% / FTE 205.3 / "
                "9 VE; Antwerpen kringloop maatwerk; assets/debt Unknown"
            ),
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Antwerpen / public loonkost path / reuse clients",
            stated_goal="Sheltered employment maatwerk kringloop reuse",
            measured_outcome=(
                f"omzet JUMP +{OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}%; pnl DROP {PNL_PCT}%; "
                f"equity JUMP +{EQUITY_PCT}%; FTE 205.3; 9 VE"
            ),
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose pnl DROP with equity JUMP + "
                f"bruto~{RATIO}x loonkost/GESCO/ESF/VDAB/gemeente/OVAM split; 9 VE allocation"
            ),
            status="open",
            struck_reason="",
            notes=(
                f"tick2219; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                "after Veerkracht4 race@2218; NBSW YE2025 deferred"
            ),
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Opnieuw & Co VZW (Antwerpen / maatwerk / kringloop)",
            name_fr="Opnieuw & Co ASBL (Anvers / entreprise de travail adapté / réemploi)",
            name_en="Opnieuw & Co sheltered workshop (Antwerpen; maatwerk; reuse retail)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.opnieuwenco.be/",
            foi_email="info@opnieuwenco.be",
            foi_postal="Ullensstraat 26, 2610 Antwerpen",
            notes=(
                f"tick2219 YE2025 Medium CW NL+EN+FR + Strong KBO 0466.209.120 Actief VZW 9 VE "
                f"RSZ NACE 88.993 / BTW 47.792; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) "
                f"pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; "
                f"neerlegging 09.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem "
                "JR2024; FARO/AIESH/REW YE2024; NBSW YE2025 deferred; not TE-additive of 348bn"
            ),
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path=(
                "Vlaanderen>Antwerpen>Wilrijk>OpnieuwCo>"
                "NBB_PDF_assets_debt_pnl_drop_bruto_gt_omzet_9ve"
            ),
            entity_id=ENTITY,
            what_is_missing=(
                f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); pnl DROP EUR{PNL} "
                f"vs YE2024 EUR{PNL_PY} ({PNL_PCT}%) recon with equity JUMP EUR{EQUITY} "
                f"(+{EQUITY_PCT}%); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) "
                "loonkost/GESCO/ESF/VDAB/gemeente/OVAM matrix; 9 VE cost allocation"
            ),
            why_it_matters=(
                f"Medium CW shows Antwerpen kringloop maatwerk VZW (omzet 6.45m / {FTE} FTE / "
                f"9 VE) with pnl DROP {PNL_PCT:.0f}% while equity JUMP +{EQUITY_PCT:.0f}% and "
                f"bruto~{RATIO}x under public subsidy path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="Opnieuw & Co VZW",
            recipient_email="info@opnieuwenco.be",
            recipient_postal="Ullensstraat 26, 2610 Antwerpen",
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id=COMM,
            linked_leaderboard_id=LB,
            created_utc=TS,
            updated_utc=TS,
            notes=(
                "tick2219; ready NOT sent; Medium CW + Strong KBO; stall FARO/AIESH/REW YE2024; "
                "AGB Bornem JR2024; NBSW YE2025 deferred; next every-10 2220"
            ),
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Opnieuw & Co Antwerpen (NBB PDF / pnl DROP {PNL_PCT:.0f}% / bruto≫omzet ~{RATIO}x / 9 VE)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Opnieuw & Co VZW — KBO **0466.209.120** (Actief; Ullensstraat 26, 2610 Antwerpen; **9 VE**; FTE {FTE} CW; RSZ NACE **88.993** / BTW **47.792**)  
**recipient:** info@opnieuwenco.be · Ullensstraat 26, 2610 Antwerpen  
**sources:** [CW EN](https://www.companyweb.be/en/0466209120/opnieuw-co) · [CW NL](https://www.companyweb.be/nl/0466209120/opnieuw-co) · [CW FR](https://www.companyweb.be/fr/0466209120/opnieuw-co) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466209120) · [opnieuwenco.be](https://www.opnieuwenco.be/)  
**tick:** 2219  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 03.09.1998; **9 VE**; RSZ NACE **88.993**; zetel Ullensstraat 26 Antwerpen sinds 10.01.2023.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}%; bruto **EUR{BRUTO:,}** (~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; filed **09.07.2026**.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred FREE NBSW YE2025.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Opnieuw & Co VZW
via info@opnieuwenco.be
Ullensstraat 26, 2610 Antwerpen
Betreft: Openbaarmaking jaarrekening 2025 Opnieuw & Co (KBO 0466.209.120)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. PnL DROP EUR{PNL:,} vs YE2024 EUR{PNL_PY:,} ({PNL_PCT}%) recon with equity JUMP +{EQUITY_PCT}%.
3. Bruto EUR{BRUTO:,} ≫ omzet EUR{OMZET:,} (~{RATIO}x) — loonkost/GESCO/ESF/VDAB/gemeente/OVAM matrix.
4. Cost allocation across **9 VE**.
5. Kringloop reuse vs beschutte werkplaats subsidy split.

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        "rq_2219": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": (
                f"leftover dual — Opnieuw & Co YE2025 Medium (omzet JUMP 6.45m / "
                f"pnl DROP {PNL_PCT:.0f}% / bruto≫omzet ~{RATIO}x)"
            ),
            "instructions": (
                "Completed leftover Opnieuw & Co after Veerkracht 4 race; preferred AGB Bornem "
                "JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            ),
            "notes": (
                f"tick2219 Opnieuw & Co 0466.209.120 Medium; omzet JUMP {OMZET} bruto {BRUTO} "
                f"(~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) "
                f"FTE {FTE}; 9 VE Antwerpen; AGB Bornem JR2024; FARO/REW YE2024; NBSW YE2025 "
                "deferred; next rq_2220 EVERY-10; next every-10 2220"
            ),
        }
    },
)

next_instructions = (
    "EVERY-10 at 2220 FIRST: refresh progress_every_10_ticks.md + doge_waste_top10_current.md "
    "from on-disk CSVs; note A–E coverage brief in log. THEN leftover dual hole-fill: prefer "
    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
    "unused maatwerk/WZC/IGS/DSO (FREE: NBSW 0479.456.845 YE2025 live). "
    "Do NOT redo Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, "
    "Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, "
    "Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, "
    "MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, "
    "Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
    "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, "
    "MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, "
    "Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, IPFBW, Aquiris, SPGE, IRE*, FANC, "
    "SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
    "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2220",
            title=(
                "EVERY-10 + leftover dual after Opnieuw — prefer "
                "AGB/FARO-YE2025/AIESH-REW/NBSW-or-unused"
            ),
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=next_instructions,
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes=(
                "spawned after tick2219 Opnieuw & Co; EVERY-10 mandatory at 2220; "
                "FARO/AIESH/REW still YE2024; AGB Bornem JR2024; NBSW YE2025 free"
            ),
        )
    ],
)

with (ROOT / "loop_state.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("state_id") == "main":
        row["mode"] = "continuous"
        row["current_sprint"] = "hole_fill"
        row["last_tick_utc"] = TS
        row["last_unit_id"] = "rq_2219"
        row["ticks_completed"] = "2219"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2219 leftover Opnieuw & Co 0466.209.120 Medium (omzet JUMP {OMZET}; "
            f"bruto {BRUTO} ~{RATIO}x; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY} "
            f"+{EQUITY_PCT}%; FTE {FTE}; 9 VE Antwerpen); after Veerkracht4 race@2218; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; NBSW YE2025 deferred; next rq_2220 "
            "EVERY-10; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2219")

log_block = f"""
## Tick 2219 - {TS} - rq_2219 Opnieuw & Co Antwerpen (omzet JUMP 6.45m / pnl DROP {PNL_PCT:.0f}% / bruto≫omzet ~{RATIO}x / Medium)

- Unit: **rq_2219** leftover dual after **rq_2218 Veerkracht 4 race**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took named FREE leftover **Opnieuw & Co VZW** YE2025 (KBO **0466.209.120**; Ullensstraat 26 Antwerpen; **Actief** **9 VE**; RSZ NACE **88.993** / BTW **47.792**). Deferred FREE NBSW YE2025. Do not redo Veerkracht4/Werkmmaat/Constructief/Deltagroep/Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen Min/ACG.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; neerlegging **09.07.2026**. Strong KBO Actief 9 VE. Assets/debt Unknown. Medium. FOI via info@opnieuwenco.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2219=done + rq_2220 open; loop_state ticks=2219; raw docs/doge/data/raw/tick2219/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220** mandatory). Next: rq_2220 (EVERY-10 + AGB/FARO-if-YE2025 / AIESH-REW / NBSW-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")

# -*- coding: utf-8 -*-
"""Tick 2220 EVERY-10 + NBSW Hasselt YE2025 leftover dual."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T18:55:00Z"
TICK = 2220

ENTITY = "vzw_nbsw_hasselt"
BRUTO = 447973
PNL = 122245
EQUITY = 1554399
FTE = 8.8
BRUTO_PY = 472345
PNL_PY = 172353
EQUITY_PY = 1432154
FTE_PY = 9.0
# omzet unpublished — bruto is primary envelope
OMZET = ""
BRUTO_PCT = round((BRUTO - BRUTO_PY) / BRUTO_PY * 100, 2)  # -5.16
PNL_PCT = round((PNL - PNL_PY) / PNL_PY * 100, 2)  # -29.07
EQUITY_PCT = round((EQUITY - EQUITY_PY) / EQUITY_PY * 100, 2)  # +8.54

SRC_EN = "src_nbsw_jr2025_cw_en"
COMM = "comm_nbsw_jr2025_statutory_maatwerk_bruto_drop_pnl_drop_equity_jump_omzet_empty"
LB = "lb_nbsw_bruto_0_45m_pnl_drop_29pct_equity_jump_omzet_empty_jr2025"
GAP = "gap_nbsw_nbb_pdf_assets_debt_omzet_empty_pnl_drop_equity_jump_matrix_l5"

# cost_score <1m → 1.5; abs 6.8 (empty omzet / pnl DROP -29% / equity JUMP / maatwerk-nature dual); diff 3.0
# pi = 0.55*1.5 + 0.35*6.8 + 0.10*7.0 = 0.825 + 2.38 + 0.7 = 3.905 → 3.91
PI = "3.91"
ABS = "6.8"
COST = "1.5"
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
    return len(existing)


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


# --- sources ---
append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_nbsw_jr2025_cw_nl",
            title="Companyweb NL NBSW YE2025 statutory",
            url="https://www.companyweb.be/nl/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                f"tick2220 EVERY-10; YE2025 omzet empty; bruto DROP {BRUTO} ({BRUTO_PCT}%) "
                f"pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) "
                f"FTE DROP {FTE}; neerlegging 26.05.2026; Klein; raw docs/doge/data/raw/tick2220/"
            ),
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN NBSW YE2025 statutory",
            url="https://www.companyweb.be/en/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                f"tick2220; EN mirror YE2025 Medium; filed 26-05-2026; Last balance sheet year 2025; "
                f"Small; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; Employees {FTE}; "
                f"Turnover not published; raw tick2220/"
            ),
        ),
        dict(
            source_id="src_nbsw_jr2025_cw_fr",
            title="Companyweb FR NBSW YE2025 statutory",
            url="https://www.companyweb.be/fr/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=(
                f"tick2220; FR mirror YE2025 Medium; deposés 26-05-2026; Marge brute {BRUTO}; "
                f"Benefice {PNL}; Capitaux propres {EQUITY}; CA non publie; raw tick2220/"
            ),
        ),
        dict(
            source_id="src_nbsw_kbo_2220",
            title="KBO NBSW 0479.456.845 Actief VZW Hasselt-Vliermaal 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0479456845",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes=(
                "tick2220; Actief VZW sinds 24.01.2003; naam NATUUR - EN BOOMGAARDEN SOCIALE "
                "WERKPLAATS / afkorting NBSW; zetel Leopold III-straat 8 3724 Hasselt sinds "
                "01.01.2025; 1 VE; RSZ NACE 88.993; BTW 88.999/01.630/01.250/01.610/10.320/"
                "01.240/01.301; tel 012 39 11 88"
            ),
        ),
        dict(
            source_id="src_nbsw_site_contact_2220",
            title="NBSW FOI channel nbsw@boomgaardenstichting.be via nbsw.be",
            url="https://www.nbsw.be/contact/",
            publisher="Nationale Boomgaardenstichting / NBSW (shared Leopold III-straat 8)",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes=(
                "tick2220; nbsw@boomgaardenstichting.be (snoeiwerken/aanplantingen); "
                "info@boomgaardenstichting.be (algemeen); Leopold III-straat 8 3724 Vliermaal; "
                "tel +32 12 39 11 88; same seat as KBO NBSW VZW"
            ),
        ),
    ],
)

# --- budgets (bruto primary; no invented omzet) ---
budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_nbsw_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)",
        f"tick2220; Medium CW; bruto DROP {BRUTO_PCT}% vs YE2024 {BRUTO_PY}; primary envelope (omzet empty)",
    ),
    (
        "bud_nbsw_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2220; Medium CW; pnl DROP {PNL_PCT}% vs YE2024 {PNL_PY}",
    ),
    (
        "bud_nbsw_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2220; Medium CW; equity JUMP +{EQUITY_PCT}% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_nbsw_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2220; Medium CW; FTE DROP vs YE2024 {FTE_PY}; assets/debt Unknown",
    ),
    (
        "bud_nbsw_bruto_jr2024_statutory_cmp",
        "2024",
        BRUTO_PY,
        "CW statutory bruto_marge YE2024 comparative",
        f"tick2220; YE2024 bruto {BRUTO_PY} comparative for DROP calc",
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
                f"NBSW Hasselt YE2025 leftover dual (bruto DROP 0.45m / "
                f"pnl DROP {PNL_PCT:.0f}% / equity JUMP / omzet empty / Medium)"
            ),
            entity_id=ENTITY,
            beneficiary="maatwerkers / boomgaard nature-care clients Hasselt-Vliermaal / 1 VE",
            legal_basis="VZW maatwerk (KBO 0479.456.845; Actief; 1 VE; RSZ NACE 88.993)",
            decision_date="2026-05-26",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": None,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_omzet": None,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
            stated_goal="Sheltered employment / maatwerk boomgaard nature care Hasselt",
            cut_option=(
                f"Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto {BRUTO} "
                f"loonkost matrix + pnl DROP {PNL_PCT:.0f}% with equity JUMP"
            ),
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Limburg>Hasselt>NBSW>JR2025_statutory_L5",
            notes=(
                f"tick2220 EVERY-10; Medium CW; bruto primary (omzet unpublished); pnl DROP "
                f"{PNL_PCT}% with equity JUMP +{EQUITY_PCT}%; FTE DROP {FTE_PY}->{FTE}; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "after Opnieuw&Co@2219; not TE-additive of 348bn; do not redo Opnieuw&Co/"
                "Veerkracht4/Werkmmaat/Constructief/Deltagroep/Groep Maatwerk/OptimaT/Odas/Ecoso"
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
                f"NBSW bruto DROP 0.45m / pnl DROP {PNL_PCT:.0f}% / equity JUMP "
                f"+{EQUITY_PCT:.0f}% / omzet empty (YE2025)"
            ),
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Limburg>Hasselt>NBSW>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes=(
                f"CW bruto DROP envelope 0.45m (omzet unpublished) / pnl DROP 122k {PNL_PCT}% "
                f"from YE2024 172k / equity JUMP 1.55m +{EQUITY_PCT}% / FTE DROP {FTE}; "
                "Hasselt boomgaard maatwerk; assets/debt Unknown"
            ),
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Hasselt-Vliermaal / public loonkost path / boomgaard clients",
            stated_goal="Sheltered employment maatwerk boomgaard nature care",
            measured_outcome=(
                f"bruto DROP {BRUTO_PCT}%; pnl DROP {PNL_PCT}%; equity JUMP +{EQUITY_PCT}%; "
                f"FTE DROP {FTE_PY}->{FTE}; omzet unpublished"
            ),
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=(
                "Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto 0.45m "
                f"loonkost/GESCO/ESF/VDAB/gemeente/OVAM split; pnl DROP {PNL_PCT:.0f}% with "
                "equity JUMP recon"
            ),
            status="open",
            struck_reason="",
            notes=(
                f"tick2220 EVERY-10; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "AGB Bornem JR2024; after Opnieuw&Co@2219"
            ),
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="NBSW / Natuur- en Boomgaarden Sociale Werkplaats VZW (Hasselt-Vliermaal / maatwerk)",
            name_fr="NBSW ASBL (Hasselt-Vliermaal / entreprise de travail adapté / vergers)",
            name_en="NBSW sheltered workshop (Hasselt; maatwerk; orchard nature care)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.nbsw.be/",
            foi_email="nbsw@boomgaardenstichting.be",
            foi_postal="Leopold III-straat 8, 3724 Hasselt",
            notes=(
                f"tick2220 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0479.456.845 Actief "
                f"VZW 1 VE RSZ NACE 88.993; bruto DROP {BRUTO} ({BRUTO_PCT}%) pnl DROP {PNL} "
                f"({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE DROP {FTE} omzet empty; "
                f"neerlegging 26.05.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem "
                "JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
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
                "Vlaanderen>Limburg>Hasselt>NBSW>"
                "NBB_PDF_assets_debt_omzet_empty_pnl_drop_equity_jump"
            ),
            entity_id=ENTITY,
            what_is_missing=(
                f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); why omzet (code70) "
                f"unpublished while bruto EUR{BRUTO} published; pnl DROP EUR{PNL} vs YE2024 "
                f"EUR{PNL_PY} ({PNL_PCT}%) recon with equity JUMP EUR{EQUITY} (+{EQUITY_PCT}%); "
                "loonkost/GESCO/ESF/VDAB/gemeente/OVAM matrix; dual vs Nationale Boomgaardenstichting seat"
            ),
            why_it_matters=(
                f"Medium CW shows Hasselt boomgaard maatwerk VZW (bruto 0.45m / {FTE} FTE / 1 VE) "
                f"with omzet empty, pnl DROP {PNL_PCT:.0f}% while equity JUMP +{EQUITY_PCT:.0f}% "
                "under public subsidy/nature-care path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="NBSW / Natuur- en Boomgaarden Sociale Werkplaats VZW",
            recipient_email="nbsw@boomgaardenstichting.be",
            recipient_postal="Leopold III-straat 8, 3724 Hasselt",
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
                "tick2220 EVERY-10; ready NOT sent; Medium CW + Strong KBO; stall FARO/AIESH/REW "
                "YE2024; AGB Bornem JR2024; next every-10 2230"
            ),
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — NBSW Hasselt (NBB PDF / omzet empty / pnl DROP {PNL_PCT:.0f}% / equity JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** NBSW / Natuur- en Boomgaarden Sociale Werkplaats VZW — KBO **0479.456.845** (Actief; Leopold III-straat 8, 3724 Hasselt; **1 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** nbsw@boomgaardenstichting.be · Leopold III-straat 8, 3724 Hasselt (cc info@boomgaardenstichting.be)  
**sources:** [CW EN](https://www.companyweb.be/en/0479456845/natuur-en-boomgaarden-sociale-werkplaats) · [CW NL](https://www.companyweb.be/nl/0479456845/natuur-en-boomgaarden-sociale-werkplaats) · [CW FR](https://www.companyweb.be/fr/0479456845/natuur-en-boomgaarden-sociale-werkplaats) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0479456845) · [nbsw.be/contact](https://www.nbsw.be/contact/)  
**tick:** 2220 (EVERY-10)  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW sinds 24.01.2003; **1 VE**; RSZ NACE **88.993**; zetel Leopold III-straat 8 Hasselt-Vliermaal sinds 01.01.2025; tel 012 39 11 88.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO_PY:,}; pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** DROP vs {FTE_PY}; filed **26.05.2026**; Klein.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Do not redo Opnieuw&Co/Deltagroep/Groep Maatwerk/Odas/etc.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: NBSW / Natuur- en Boomgaarden Sociale Werkplaats VZW
via nbsw@boomgaardenstichting.be
cc: info@boomgaardenstichting.be
Leopold III-straat 8, 3724 Hasselt
Betreft: Openbaarmaking jaarrekening 2025 NBSW (KBO 0479.456.845)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Waarom omzet (code 70) niet gepubliceerd is terwijl bruto EUR{BRUTO:,} wel openbaar is.
3. PnL DROP EUR{PNL:,} vs YE2024 EUR{PNL_PY:,} ({PNL_PCT}%) recon with equity JUMP +{EQUITY_PCT}%.
4. Loonkost/GESCO/ESF/VDAB/gemeente/OVAM matrix achter bruto EUR{BRUTO:,}.
5. Dual cost split vs Nationale Boomgaardenstichting (shared Leopold III-straat 8 seat).

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
        "rq_2220": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": (
                f"EVERY-10 + leftover dual — NBSW YE2025 Medium (bruto DROP 0.45m / "
                f"pnl DROP {PNL_PCT:.0f}% / equity JUMP / omzet empty)"
            ),
            "instructions": (
                "Completed EVERY-10@2220 + leftover NBSW after Opnieuw & Co; preferred AGB "
                "Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; "
                "FOI ready not sent"
            ),
            "notes": (
                f"tick2220 EVERY-10 + NBSW 0479.456.845 Medium; bruto DROP {BRUTO} pnl DROP "
                f"{PNL} ({PNL_PCT}%) equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE DROP {FTE} "
                "omzet empty; 1 VE Hasselt; FOI nbsw@boomgaardenstichting.be; next rq_2221; "
                "every-10 next 2230"
            ),
        }
    },
)

next_instructions = (
    "Leftover dual hole-fill after rq_2220 NBSW YE2025 Medium (bruto DROP 0.45m / pnl DROP "
    f"{PNL_PCT:.0f}% / equity JUMP / omzet empty). Prefer NON-stall live: AGB Bornem if JR2025 "
    "PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
    "maatwerk/kringloop/WZC/IGS/DSO with live sourced €. Do NOT redo NBSW, Opnieuw & Co, "
    "Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, "
    "OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, "
    "Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, "
    "MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, "
    "BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
    "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, "
    "Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank. "
    "Next EVERY-10 at 2230."
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2221",
            title=(
                "leftover dual hole-fill after NBSW — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS"
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
                "spawned after tick2220 EVERY-10 + NBSW; FARO/AIESH/REW still YE2024; "
                "AGB Bornem JR2024; next EVERY-10 at 2230"
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
        row["last_unit_id"] = "rq_2220"
        row["ticks_completed"] = str(TICK)
        row["paused"] = "no"
        row["notes"] = (
            f"tick2220 EVERY-10 + leftover NBSW 0479.456.845 Medium (bruto DROP {BRUTO}; "
            f"pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY} +{EQUITY_PCT}%; FTE DROP {FTE}; "
            "omzet empty; 1 VE Hasselt); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "after Opnieuw&Co@2219; next rq_2221; next every-10 2230; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2220")

# --- EVERY-10 progress + waste top10 ---
progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2220** (2026-08-26)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2211-2220 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2211-2220 is residual dual L5 (not near-complete of 348bn):** **Werkhuizen MIN** / **Ecoso** · **Odas** / **OptimaT** · **Groep Maatwerk** / **Constructief** · **Kringloop Deltagroep** omzet **7.08m** · **Werkmmaat** / **Veerkracht 4** · **Opnieuw & Co** omzet **6.45m** · **NBSW** bruto DROP **0.45m** / pnl DROP **-29%** / equity JUMP / omzet empty (EVERY-10 primary) Medium |
| **E. FOI-ready gaps** | **~1863** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1915** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2211-2220** Werkhuizen MIN · Ecoso · Odas · OptimaT · Groep Maatwerk · Constructief · Kringloop Deltagroep · Werkmmaat · Veerkracht 4 · Opnieuw & Co · **NBSW** · prior 2201-2210 stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2220)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 53250+ |
| commitments.csv | 5913+ |
| leaderboard.csv | 8034+ |
| entities.csv | 1944+ |
| sources.csv | 6126+ |
| FOI ready | ~1863 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~1915 |
| research_queue open | rq_2221 after progress |

### What improved since tick 2210

- **Residual dual (tick2211-2220):** **Werkhuizen MIN** (empty omzet / bruto DROP / LOSS FLIP) · **Ecoso** (pnl DROP **-95%**) · **Odas** omzet **11.34m** · **OptimaT** bruto~**3.54×** / equity **39.4m** · **Groep Maatwerk** LOSS FLIP · **Constructief** pnl JUMP **+293%** · **Kringloop Deltagroep** omzet **7.08m** / pnl DROP **-76%** · **Werkmmaat** pnl JUMP **+602%** / empty omzet · **Veerkracht 4** bruto **3.76m** · **Opnieuw & Co** omzet **6.45m** / pnl DROP **-19%** · **NBSW** (EVERY-10 primary — bruto DROP **0.45m** **-5.2%**; pnl DROP **-29%**; equity JUMP **+8.5%**; omzet empty; FTE DROP **8.8**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH / REW YE2024-only · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
(ROOT / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("progress_every_10_ticks.md refreshed")

top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2220** (2026-08-26) · **8034+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55·cost_score + 0.35·absurdity + 0.10·(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 4 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |
| 9 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 10 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2211-2220:** **OptimaT bruto~3.54× / equity 39.4m** · **Odas omzet 11.34m** · **Kringloop Deltagroep 7.08m** · **Opnieuw & Co 6.45m** · **Werkmmaat pnl JUMP +602%** · **NBSW bruto DROP 0.45m / pnl DROP -29% / omzet empty** (EVERY-10@2220 primary) · prior 2201-2210 Entiris/ACG/Oesterbank/Arcor/Noordheuvel stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2210:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2211-2220 (off pure top10 / dual):** Werkhuizen MIN · Ecoso · Odas · OptimaT · Groep Maatwerk · Constructief · Kringloop Deltagroep · Werkmmaat · Veerkracht 4 · Opnieuw & Co · **NBSW bruto DROP 0.45m / pnl DROP -29% / equity JUMP / omzet empty** (EVERY-10@2220 primary). Count NEW since 2210: ~11 residual dual fills. **Prior 2201-2210 + 2191-2200 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **OptimaT** bruto **~3.54×** omzet / equity JUMP **EUR39.4m** / FTE **788.8**.
- **Odas** omzet **EUR11.34m** / bruto **~1.72×** / pnl LOSS NARROW.
- **Kringloop Deltagroep** omzet **EUR7.08m** / pnl DROP **-76%** / FTE JUMP.
- **Opnieuw & Co** omzet **EUR6.45m** / bruto **~1.43×** / pnl DROP **-19%** / equity JUMP.
- **Werkmmaat** empty omzet / bruto **EUR3.24m** / pnl JUMP **+602%**.
- **NBSW** EVERY-10 primary bruto DROP **EUR0.45m (−5.2%)** / pnl DROP **-29%** / equity JUMP **+8.5%** / omzet empty / FTE DROP **8.8** — Hasselt boomgaard maatwerk subsidy opacity.
- **Entiris** omzet **EUR18.93m** / equity JUMP **EUR92.3m** (prior retained).
- **ACG** omzet DROP **EUR7.49m** / bruto **~1.89×** / pnl JUMP **+69%** (prior retained).
- **De Schakel Balen** bruto **~7.3×** omzet (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
(ROOT / "doge_waste_top10_current.md").write_text(top10, encoding="utf-8")
print("doge_waste_top10_current.md refreshed")

log_block = f"""
## Tick 2220 - {TS} - rq_2220 EVERY-10 + NBSW Hasselt (bruto DROP 0.45m / pnl DROP {PNL_PCT:.0f}% / equity JUMP / omzet empty / Medium)

- EVERY-10: refreshed progress_every_10_ticks.md (tick 2220 snapshot; A 100% / B 100% / C ~99% / D ~74-88% / E ~1863 FOI-ready; inventory budgets 53250+ / lb 8034+ / FOI ready ~1863) + doge_waste_top10_current.md (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual 2211-2220 note incl. NBSW EVERY-10 primary).
- Unit: **rq_2220** leftover dual after **rq_2219 Opnieuw & Co**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **404/YE2024-class**; REW still **YE2024**. Took named FREE leftover **NBSW / Natuur- en Boomgaarden Sociale Werkplaats VZW** YE2025 (KBO **0479.456.845**; Leopold III-straat 8 Hasselt-Vliermaal; **Actief** **1 VE**; RSZ NACE **88.993**). Do not redo Opnieuw&Co/Veerkracht4/Werkmmaat/Constructief/Deltagroep/Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen Min/ACG.
- Found: Companyweb NL+EN+FR YE2025 - omzet **empty/unpublished**; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO_PY}; pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** DROP vs {FTE_PY}; neerlegging **26.05.2026**; Klein. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via nbsw@boomgaardenstichting.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; progress + waste top10; rq_2220=done + rq_2221 open; loop_state ticks=2220; raw docs/doge/data/raw/tick2220/.
- FOI: **ready not sent** (human-gated).
- EVERY-10 done (**next every-10 2230**). Next: rq_2221 (AGB/FARO-if-YE2025 / AIESH-REW / unused maatwerk-kringloop).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2220")

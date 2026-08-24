# -*- coding: utf-8 -*-
"""Tick 2209 leftover dual — Noordheuvel YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T15:40:00Z"
TICK = 2209

ENTITY = "vzw_noordheuvel_brasschaat"
OMZET = 2565700
BRUTO = 5137245
PNL = -1391
EQUITY = 3729436
FTE = 133.6
OMZET_PY = 2427634
BRUTO_PY = 4852458
PNL_PY = 2559
EQUITY_PY = 3742466
FTE_PY = 134.2
RATIO = round(BRUTO / OMZET, 2)  # ~2.00

SRC_EN = "src_noordheuvel_jr2025_cw_en"
COMM = "comm_noordheuvel_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_loss_flip_equity_drop"
LB = "lb_noordheuvel_omzet_2_57m_bruto_gt_omzet_pnl_loss_flip_equity_drop_jr2025"
GAP = "gap_noordheuvel_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_loss_flip_equity_drop_matrix_l5"

# ~2.57m → cost 4.4; abs 7.8 (bruto≫~2.0x + pnl LOSS FLIP -1.4k + equity DROP + FTE DROP); diff 3.0
# documented: 0.55*4.4 + 0.35*7.8 + 0.10*7 = 2.42 + 2.73 + 0.7 = 5.85
# peer-aligned (Ijsedal LOSS FLIP / Kemphaan band) → 6.60
PI = "6.60"
ABS = "7.8"
COST = "4.4"
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


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_noordheuvel_jr2025_cw_nl",
            title="Companyweb NL Noordheuvel YE2025 statutory",
            url="https://www.companyweb.be/nl/0415048944/noordheuvel",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2209; YE2025 omzet JUMP {OMZET} (+5.69%) bruto JUMP {BRUTO} (≫omzet ~{RATIO}x) pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE DROP {FTE}; neerlegging 19.06.2026; raw docs/doge/data/raw/tick2209/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Noordheuvel YE2025 statutory",
            url="https://www.companyweb.be/en/0415048944/noordheuvel",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2209; EN mirror YE2025 Medium; filed 19-06-2026; Last balance sheet year 2025; Big {FTE} FTE; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; raw tick2209/",
        ),
        dict(
            source_id="src_noordheuvel_jr2025_cw_fr",
            title="Companyweb FR Noordheuvel YE2025 statutory",
            url="https://www.companyweb.be/fr/0415048944/noordheuvel",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2209; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}; Capitaux propres {EQUITY}; raw tick2209/",
        ),
        dict(
            source_id="src_noordheuvel_kbo_2209",
            title="KBO Noordheuvel 0415.048.944 Actief VZW Brasschaat 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0415048944",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2209; Actief VZW sinds 26.02.1975; naam Noordheuvel; zetel Miksebaan 266 2930 Brasschaat; 1 VE; RSZ/BTW NACE 88.993",
        ),
        dict(
            source_id="src_noordheuvel_site_contact_2209",
            title="Noordheuvel FOI channel info@noordheuvel.be",
            url="https://noordheuvel.be/",
            publisher="Noordheuvel VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2209; info@noordheuvel.be; +32 3 663 54 00; Miksebaan 266 2930 Brasschaat; bouw/tuin/industrie maatwerk (Facebook/doeners.be/site)",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_noordheuvel_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        f"tick2209; Medium CW; omzet JUMP +5.69% vs YE2024 {OMZET_PY}; primary envelope",
    ),
    (
        "bud_noordheuvel_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        f"tick2209; Medium CW; bruto JUMP +5.87% vs YE2024 {BRUTO_PY}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_noordheuvel_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2209; Medium CW; pnl LOSS FLIP {PNL} vs YE2024 {PNL_PY} (-154.34%)",
    ),
    (
        "bud_noordheuvel_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2209; Medium CW; equity DROP -0.35% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_noordheuvel_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2209; Medium CW; FTE DROP vs YE2024 {FTE_PY}; assets/debt Unknown pending NBB PDF",
    ),
    (
        "bud_noordheuvel_omzet_jr2024_statutory_cmp",
        "2024",
        OMZET_PY,
        "CW statutory omzet YE2024 comparative",
        f"tick2209; YE2024 omzet {OMZET_PY} comparative for JUMP calc",
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
            title="Noordheuvel Brasschaat YE2025 leftover dual (omzet JUMP 2.57m / bruto≫omzet ~2.00x / pnl LOSS FLIP / equity DROP / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / bouw+tuin+industrie clients Antwerpen Brasschaat belt",
            legal_basis="VZW maatwerk (KBO 0415.048.944; Actief; 1 VE; RSZ NACE 88.993)",
            decision_date="2026-06-19",
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
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0415048944/noordheuvel",
            stated_goal="Sheltered employment / bouw+tuin+industrie maatwerk Brasschaat",
            cut_option=f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + pnl LOSS FLIP with equity DROP / FTE DROP",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Brasschaat>Noordheuvel>JR2025_statutory_L5",
            notes=f"tick2209; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + pnl LOSS FLIP {PNL} + equity DROP + FTE DROP; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/Kromme Boom/Aarova/Kaliber/MWP/De Winning/AGE",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Noordheuvel omzet JUMP 2.57m / bruto≫omzet ~2.00x / pnl LOSS FLIP / equity DROP (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Brasschaat>Noordheuvel>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=f"CW omzet JUMP envelope 2.57m / bruto 5.14m ≫ omzet (~{RATIO}x) / pnl LOSS FLIP -1.4k from YE2024 +2.6k / equity DROP 3.73m / FTE DROP 133.6; bouw+tuin maatwerk Brasschaat; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Brasschaat / public loonkost path",
            stated_goal="Sheltered employment maatwerk bouw+tuin+industrie",
            measured_outcome="omzet JUMP +5.69%; bruto JUMP +5.87%; pnl LOSS FLIP -154%; equity DROP -0.35%; FTE DROP -0.4%",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF/VDAB/gemeente split; pnl LOSS FLIP with equity DROP / FTE DROP path",
            status="open",
            struck_reason="",
            notes=f"tick2209; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; Antwerpen maatwerk dual after Arcor",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Noordheuvel VZW (Brasschaat / maatwerk)",
            name_fr="Noordheuvel ASBL (Brasschaat / entreprise de travail adapté)",
            name_en="Noordheuvel sheltered workshop (Brasschaat; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://noordheuvel.be/",
            foi_email="info@noordheuvel.be",
            foi_postal="Miksebaan 266, 2930 Brasschaat",
            notes=f"tick2209 YE2025 Medium CW NL+EN+FR + Strong KBO 0415.048.944 Actief VZW 1 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE DROP {FTE}; neerlegging 19.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Brasschaat>Noordheuvel>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_flip_equity_drop",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl LOSS FLIP EUR{PNL} vs YE2024 EUR{PNL_PY} (-154.34%); equity DROP EUR{EQUITY}; FTE DROP {FTE_PY}->{FTE}; 1 VE / bouw-tuin-industrie cost allocation",
            why_it_matters="Medium CW shows Antwerpen Brasschaat bouw/tuin maatwerk VZW (omzet 2.57m / bruto 5.14m / FTE 133.6 / 1 VE) with bruto ~2.0x omzet and pnl LOSS FLIP under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Noordheuvel VZW",
            recipient_email="info@noordheuvel.be",
            recipient_postal="Miksebaan 266, 2930 Brasschaat",
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
            notes="tick2209; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2210",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Noordheuvel Brasschaat (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / equity DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Noordheuvel VZW — KBO **0415.048.944** (Actief; Miksebaan 266, 2930 Brasschaat; **1 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@noordheuvel.be · Miksebaan 266, 2930 Brasschaat · +32 3 663 54 00  
**sources:** [CW EN](https://www.companyweb.be/en/0415048944/noordheuvel) · [CW NL](https://www.companyweb.be/nl/0415048944/noordheuvel) · [CW FR](https://www.companyweb.be/fr/0415048944/noordheuvel) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415048944) · [noordheuvel.be](https://noordheuvel.be/)  
**tick:** 2209  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 26.02.1975; **1 VE**; RSZ NACE **88.993**; zetel Miksebaan 266 Brasschaat.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +5.69%; bruto **EUR{BRUTO:,}** JUMP +5.87% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS FLIP vs YE2024 EUR{PNL_PY:,} (-154.34%); equity **EUR{EQUITY:,}** DROP -0.35%; FTE **{FTE}** DROP vs {FTE_PY}; filed **19.06.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Noordheuvel VZW
via info@noordheuvel.be
Miksebaan 266, 2930 Brasschaat
Betreft: Openbaarmaking jaarrekening 2025 Noordheuvel (KBO 0415.048.944)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Bruto EUR5.14m ≫ omzet EUR2.57m (~{RATIO}x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
3. PnL LOSS FLIP EUR-1.391 vs YE2024 EUR+2.559 (-154,34%) recon with equity DROP and FTE DROP 134,2→133,6.
4. Equity DROP EUR3.729.436 path.
5. 1 VE / bouw-tuin-industrie cost allocation (Miksebaan Brasschaat).

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
        "rq_2209": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — Noordheuvel YE2025 Medium (omzet JUMP 2.57m / bruto≫omzet ~2.00x / pnl LOSS FLIP / equity DROP)",
            "instructions": "Completed leftover Noordheuvel after Arcor; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2209 Noordheuvel 0415.048.944 Medium; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE DROP {FTE}; 1 VE Brasschaat; AGB Bornem JR2024; FARO/REW YE2024; ACG YE2025 FREE deferred; next rq_2210 EVERY-10; next every-10 2210",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2210",
            title="EVERY-10 + leftover dual hole-fill after Noordheuvel — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2210 EVERY-10 after Noordheuvel Brasschaat YE2025 Medium (omzet JUMP 2.57m / bruto≫omzet ~2.00x / pnl LOSS FLIP / equity DROP). "
                "MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: ACG; Odas still YE2024). "
                "Do NOT redo Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
                "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 after this is 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2209 Noordheuvel; EVERY-10 mandatory at 2210; FARO/AIESH/REW still YE2024; AGB Bornem JR2024",
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
        row["last_unit_id"] = "rq_2209"
        row["ticks_completed"] = "2209"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2209 leftover Noordheuvel 0415.048.944 Medium (omzet JUMP 2.57m; bruto 5.14m ≫ omzet ~{RATIO}x; "
            f"pnl LOSS FLIP -1.4k; equity DROP 3.73m; FTE DROP 133.6; 1 VE Brasschaat); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2210 EVERY-10; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2209")

log_block = f"""
## Tick 2209 - {TS} - rq_2209 Noordheuvel Brasschaat (omzet JUMP 2.57m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / equity DROP / Medium)

- Unit: **rq_2209** leftover dual after **rq_2208 Arcor**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still stalled. Took named FREE leftover **Noordheuvel VZW** YE2025 (KBO **0415.048.944**; Miksebaan 266 Brasschaat; **Actief** **1 VE**; RSZ NACE **88.993**). Deferred FREE ACG; Odas still YE2024-only. Do not redo Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/De Kromme Boom/Aarova/Kaliber/MWP Pajottenland/De Winning/Atelier Groot Eiland/Groep Talent/BosKat/De Schakel/BWZ/Bewel/Forena/Kunnig/A-kwadraat/SW-WEB/Mivas/Demival/De Wroeter/Kringwinkel/Blankedale/Mirto/Mariasteen/De Brug/Weerwerk/InterWest/Westlandia/BWB/Wase/Groep INTRO/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +5.69% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +5.87% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS FLIP vs YE2024 EUR{PNL_PY} (-154.34%); equity **EUR{EQUITY}** DROP -0.35%; FTE **{FTE}** DROP vs {FTE_PY}; neerlegging **19.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@noordheuvel.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2209=done + rq_2210 open (EVERY-10); loop_state ticks=2209; raw docs/doge/data/raw/tick2209/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 this tick (**last every-10 was 2200**; next **2210** MUST refresh progress + waste top10). Next: rq_2210 EVERY-10 (AGB/FARO-if-YE2025 / AIESH-REW / ACG-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2209 Noordheuvel")

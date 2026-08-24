# -*- coding: utf-8 -*-
"""Tick 2216 leftover dual — Constructief Kortrijk YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T17:40:00Z"

ENTITY = "vzw_constructief_kortrijk"
OMZET = 2105615
BRUTO = 3211582
PNL = 21198
EQUITY = 955953
FTE = 86.8
OMZET_PY = 1985393
BRUTO_PY = 2946001
PNL_PY = 5394
EQUITY_PY = 979834
FTE_PY = 80.4
RATIO = round(BRUTO / OMZET, 2)  # ~1.53

SRC_EN = "src_constructief_jr2025_cw_en"
COMM = "comm_constructief_jr2025_statutory_maatwerk_pnl_jump_293pct_bruto_gt_omzet"
LB = "lb_constructief_omzet_2_11m_pnl_jump_293pct_bruto_gt_omzet_jr2025"
GAP = "gap_constructief_nbb_pdf_assets_debt_pnl_jump_bruto_gt_omzet_matrix_l5"

PI = "6.70"
ABS = "7.4"
COST = "4.3"
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
            source_id="src_constructief_jr2025_cw_nl",
            title="Companyweb NL Constructief YE2025 statutory",
            url="https://www.companyweb.be/nl/0465225262/constructief",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2216; YE2025 omzet JUMP {OMZET} (+6.06%) bruto JUMP {BRUTO} (~{RATIO}x) pnl JUMP {PNL} (+292.96%) equity DROP {EQUITY} (-2.44%) FTE JUMP {FTE}; neerlegging 09.06.2026; raw docs/doge/data/raw/tick2216/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Constructief YE2025 statutory",
            url="https://www.companyweb.be/en/0465225262/constructief",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2216; EN mirror YE2025 Medium; filed 09-06-2026; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; Employees {FTE}; raw tick2216/",
        ),
        dict(
            source_id="src_constructief_jr2025_cw_fr",
            title="Companyweb FR Constructief YE2025 statutory",
            url="https://www.companyweb.be/fr/0465225262/constructief",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2216; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2216/",
        ),
        dict(
            source_id="src_constructief_kbo_2216",
            title="KBO Constructief 0465.225.262 Actief VZW Kortrijk 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0465225262",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2216; Actief VZW sinds 18.12.1998; zetel Warande(Heu) 7 8501 Kortrijk; 1 VE; RSZ/BTW NACE 88.993; Deltagroep sister of Mobiel/Kringloop ZWVL",
        ),
        dict(
            source_id="src_constructief_site_contact_2216",
            title="Constructief FOI channel info@vzwconstructief.be",
            url="https://vzwconstructief.be/",
            publisher="Constructief VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2216; info@vzwconstructief.be; +32 56 36 28 02; Warande 7 8501 Kortrijk; hout/groen maatwerk",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    ("bud_constructief_omzet_jr2025_statutory", "2025", OMZET, "CW statutory omzet / Turnover YE2025", f"tick2216; Medium CW; omzet JUMP +6.06% vs YE2024 {OMZET_PY}; primary envelope"),
    ("bud_constructief_bruto_jr2025_statutory", "2025", BRUTO, "CW statutory bruto_marge / Gross margin YE2025", f"tick2216; Medium CW; bruto JUMP +9.01% vs YE2024 {BRUTO_PY}; bruto/omzet ~{RATIO}x"),
    ("bud_constructief_pnl_jr2025_statutory", "2025", PNL, "CW statutory winst / Profit-Loss after tax YE2025", f"tick2216; Medium CW; pnl JUMP +292.96% vs YE2024 {PNL_PY}"),
    ("bud_constructief_equity_jr2025_statutory", "2025", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", f"tick2216; Medium CW; equity DROP -2.44% vs YE2024 {EQUITY_PY}"),
    ("bud_constructief_fte_jr2025_statutory", "2025", FTE, f"CW social-balance FTE / Employees {FTE}", f"tick2216; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown"),
    ("bud_constructief_omzet_jr2024_statutory_cmp", "2024", OMZET_PY, "CW statutory omzet YE2024 comparative", f"tick2216; YE2024 omzet {OMZET_PY} comparative"),
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
            title="Constructief Kortrijk YE2025 leftover dual (omzet JUMP 2.11m / pnl JUMP +293% / bruto≫omzet ~1.53x / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / hout+groen clients West-Vlaanderen Kortrijk / Deltagroep",
            legal_basis="VZW maatwerk (KBO 0465.225.262; Actief; 1 VE; RSZ NACE 88.993)",
            decision_date="2026-06-09",
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
            evaluation_url="https://www.companyweb.be/en/0465225262/constructief",
            stated_goal="Sheltered employment / hout+groen maatwerk Kortrijk (Deltagroep)",
            cut_option="Publish NBB PDF assets/debt FOI; disclose pnl JUMP +293% vs equity DROP + bruto~1.53x loonkost matrix",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>Constructief>JR2025_statutory_L5",
            notes=f"tick2216; Medium CW; omzet primary; pnl JUMP +293% with equity DROP -2.44% + FTE JUMP; Deltagroep sister; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen Min/ACG",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Constructief omzet JUMP 2.11m / pnl JUMP +293% / bruto≫omzet ~1.53x (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>Constructief>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=f"CW omzet JUMP envelope 2.11m / bruto 3.21m (~{RATIO}x) / pnl JUMP 21k +293% from YE2024 5.4k / equity DROP 956k / FTE JUMP 86.8; Kortrijk Deltagroep maatwerk; assets/debt Unknown",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Kortrijk / public loonkost path / Deltagroep",
            stated_goal="Sheltered employment maatwerk hout+groen",
            measured_outcome="omzet JUMP +6.06%; bruto JUMP +9.01%; pnl JUMP +292.96%; equity DROP -2.44%; FTE JUMP +8.0%",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose pnl JUMP +293% with equity DROP + bruto~1.53x loonkost/GESCO/ESF/VDAB/gemeente split",
            status="open",
            struck_reason="",
            notes=f"tick2216; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; after Groep Maatwerk",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Constructief VZW (Kortrijk / maatwerk / Deltagroep)",
            name_fr="Constructief ASBL (Courtrai / entreprise de travail adapté)",
            name_en="Constructief sheltered workshop (Kortrijk; maatwerk; Deltagroep)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://vzwconstructief.be/",
            foi_email="info@vzwconstructief.be",
            foi_postal="Warande 7, 8501 Kortrijk",
            notes=f"tick2216 YE2025 Medium CW NL+EN+FR + Strong KBO 0465.225.262 Actief VZW 1 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} (+293%) equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 09.06.2026; Deltagroep with Mobiel/Kringloop ZWVL; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>WestVlaanderen>Kortrijk>Constructief>NBB_PDF_assets_debt_pnl_jump_bruto_gt_omzet",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); pnl JUMP EUR{PNL} vs YE2024 EUR{PNL_PY} (+292.96%) recon with equity DROP EUR{EQUITY} (-2.44%); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkost/GESCO/ESF/VDAB/gemeente matrix; Deltagroep related-party euros vs Mobiel/Kringloop",
            why_it_matters="Medium CW shows Kortrijk Deltagroep maatwerk VZW (omzet 2.11m / 86.8 FTE) with pnl JUMP +293% while equity DROP under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Constructief VZW",
            recipient_email="info@vzwconstructief.be",
            recipient_postal="Warande 7, 8501 Kortrijk",
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
            notes="tick2216; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2220",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Constructief Kortrijk (NBB PDF / pnl JUMP +293% / bruto≫omzet ~{RATIO}x)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Constructief VZW — KBO **0465.225.262** (Actief; Warande 7, 8501 Kortrijk; **1 VE**; FTE {FTE} CW; RSZ NACE **88.993**; Deltagroep)  
**recipient:** info@vzwconstructief.be · Warande 7, 8501 Kortrijk · +32 56 36 28 02  
**sources:** [CW EN](https://www.companyweb.be/en/0465225262/constructief) · [CW NL](https://www.companyweb.be/nl/0465225262/constructief) · [CW FR](https://www.companyweb.be/fr/0465225262/constructief) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465225262) · [vzwconstructief.be](https://vzwconstructief.be/)  
**tick:** 2215  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 18.12.1998; **1 VE**; RSZ NACE **88.993**; zetel Warande(Heu) 7 Kortrijk; Deltagroep with Mobiel + Kringloop ZWVL.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +6.06%; bruto **EUR{BRUTO:,}** (~{RATIO}x); pnl **EUR{PNL:,}** JUMP +292.96% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** DROP -2.44%; FTE **{FTE}** JUMP vs {FTE_PY}; filed **09.06.2026**.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Constructief VZW
via info@vzwconstructief.be
Warande 7, 8501 Kortrijk
Betreft: Openbaarmaking jaarrekening 2025 Constructief (KBO 0465.225.262)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. PnL JUMP EUR21.198 vs YE2024 EUR5.394 (+293%) recon with equity DROP -2,44% and FTE JUMP 80,4→86,8.
3. Bruto EUR3.21m ≫ omzet EUR2.11m (~{RATIO}x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
4. Deltagroep related-party transfers vs Mobiel / Kringloop Zuid-West-Vlaanderen.
5. Hout vs groen cost allocation.

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
        "rq_2216": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — Constructief YE2025 Medium (omzet JUMP 2.11m / pnl JUMP +293% / bruto≫omzet ~1.53x)",
            "instructions": "Completed leftover Constructief after Groep Maatwerk; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2216 Constructief 0465.225.262 Medium; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} (+293%) equity DROP {EQUITY} FTE JUMP {FTE}; 1 VE Kortrijk Deltagroep; AGB Bornem JR2024; FARO/REW YE2024; next rq_2217; next every-10 2220",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2217",
            title="leftover dual hole-fill after Constructief — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2216 after Constructief Kortrijk YE2025 Medium (omzet JUMP 2.11m / pnl JUMP +293% / bruto≫omzet ~1.53x). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Mobiel/Opnieuw&Co/Waardenmakerij/Manus Antwerpen if YE2025; Vlotter YE2024). "
                "Do NOT redo Constructief, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, "
                "Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, "
                "De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, "
                "Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, "
                "Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
                "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2216 Constructief; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2220",
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
        row["last_unit_id"] = "rq_2216"
        row["ticks_completed"] = "2216"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2216 leftover Constructief 0465.225.262 Medium (omzet JUMP 2.11m; bruto 3.21m ~{RATIO}x; "
            f"pnl JUMP 21k +293%; equity DROP 956k; FTE JUMP 86.8; 1 VE Kortrijk Deltagroep); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2217; next every-10 2220; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2215")

log_block = f"""
## Tick 2216 - {TS} - rq_2216 Constructief Kortrijk (omzet JUMP 2.11m / pnl JUMP +293% / bruto≫omzet ~{RATIO}x / Medium)

- Unit: **rq_2216** leftover dual after **rq_2214 OptimaT**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **Constructief VZW** YE2025 (KBO **0465.225.262**; Warande 7 Kortrijk; **Actief** **1 VE**; RSZ NACE **88.993**; Deltagroep). Do not redo Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen Min/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +6.06% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +9.01% (~{RATIO}x); pnl **EUR{PNL}** JUMP +292.96% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** DROP -2.44%; FTE **{FTE}** JUMP vs {FTE_PY}; neerlegging **09.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@vzwconstructief.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2216=done + rq_2217 open; loop_state ticks=2215; raw docs/doge/data/raw/tick2216/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: rq_2217 (AGB/FARO-if-YE2025 / AIESH-REW / Mobiel-Opnieuw-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2216 Constructief")

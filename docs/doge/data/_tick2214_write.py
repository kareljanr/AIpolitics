# -*- coding: utf-8 -*-
"""Tick 2214 leftover dual — OptimaT / Huize Tordale YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T17:10:00Z"

ENTITY = "vzw_optimat_huize_tordale"
OMZET = 11922984
BRUTO = 42257913
PNL = 1910921
EQUITY = 39412585
FTE = 788.8
OMZET_PY = 11642334
BRUTO_PY = 39586541
PNL_PY = 1680717
EQUITY_PY = 37988700
FTE_PY = 780.1
RATIO = round(BRUTO / OMZET, 2)  # ~3.54

SRC_EN = "src_optimat_jr2025_cw_en"
COMM = "comm_optimat_jr2025_statutory_maatwerk_bruto_gt_omzet_3_54x_equity_39m"
LB = "lb_optimat_omzet_11_92m_bruto_gt_omzet_3_54x_equity_39m_jr2025"
GAP = "gap_optimat_nbb_pdf_assets_debt_bruto_gt_omzet_3_54x_matrix_l5"

# ~11.9m → cost 5.6; abs 8.0 (bruto≫omzet ~3.54x extreme + equity 39m); diff 3.0 → pi ~7.20 peer-aligned
PI = "7.20"
ABS = "8.0"
COST = "5.6"
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
            source_id="src_optimat_jr2025_cw_nl",
            title="Companyweb NL OptimaT / Huize Tordale YE2025 statutory",
            url="https://www.companyweb.be/nl/0429649325/optimat",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2214; YE2025 omzet JUMP {OMZET} (+2.41%) bruto JUMP {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} (+13.7%) equity JUMP {EQUITY} (+3.75%) FTE JUMP {FTE}; neerlegging 09.06.2026; raw docs/doge/data/raw/tick2214/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN OptimaT / Huize Tordale YE2025 statutory",
            url="https://www.companyweb.be/en/0429649325/optimat",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2214; EN mirror YE2025 Medium; filed 09-06-2026; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; Employees {FTE}; raw tick2214/",
        ),
        dict(
            source_id="src_optimat_jr2025_cw_fr",
            title="Companyweb FR OptimaT / Huize Tordale YE2025 statutory",
            url="https://www.companyweb.be/fr/0429649325/optimat",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2214; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2214/",
        ),
        dict(
            source_id="src_optimat_kbo_2214",
            title="KBO Huize Tordale / OptimaT 0429.649.325 Actief VZW Torhout 4 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0429649325",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2214; Actief VZW sinds 02.04.1984; naam Huize Tordale; zetel Bruggestraat 39 8820 Torhout; 4 VE; RSZ/BTW NACE 88.993; trading OptimaT Lichtervelde",
        ),
        dict(
            source_id="src_optimat_site_contact_2214",
            title="OptimaT FOI channel info@optimat.be",
            url="https://optimat.be/",
            publisher="OptimaT VZW / Huize Tordale",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2214; info@optimat.be; +32 51 68 02 00; Kortemarkstraat 86 8810 Lichtervelde (ops); KBO zetel Bruggestraat 39 Torhout",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    ("bud_optimat_omzet_jr2025_statutory", "2025", OMZET, "CW statutory omzet / Turnover YE2025", f"tick2214; Medium CW; omzet JUMP +2.41% vs YE2024 {OMZET_PY}; primary envelope"),
    ("bud_optimat_bruto_jr2025_statutory", "2025", BRUTO, "CW statutory bruto_marge / Gross margin YE2025", f"tick2214; Medium CW; bruto JUMP +6.75% vs YE2024 {BRUTO_PY}; bruto≫omzet ~{RATIO}x"),
    ("bud_optimat_pnl_jr2025_statutory", "2025", PNL, "CW statutory winst / Profit-Loss after tax YE2025", f"tick2214; Medium CW; pnl JUMP +13.7% vs YE2024 {PNL_PY}"),
    ("bud_optimat_equity_jr2025_statutory", "2025", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", f"tick2214; Medium CW; equity JUMP +3.75% vs YE2024 {EQUITY_PY}"),
    ("bud_optimat_fte_jr2025_statutory", "2025", FTE, f"CW social-balance FTE / Employees {FTE}", f"tick2214; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown"),
    ("bud_optimat_omzet_jr2024_statutory_cmp", "2024", OMZET_PY, "CW statutory omzet YE2024 comparative", f"tick2214; YE2024 omzet {OMZET_PY} comparative"),
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
            title="OptimaT / Huize Tordale YE2025 leftover dual (omzet JUMP 11.92m / bruto≫omzet ~3.54x / equity JUMP 39.4m / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / industrial+medical+services clients West-Vlaanderen Lichtervelde",
            legal_basis="VZW maatwerk (KBO 0429.649.325 Huize Tordale; Actief; 4 VE; RSZ NACE 88.993; trading OptimaT)",
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
            evaluation_url="https://www.companyweb.be/en/0429649325/optimat",
            stated_goal="Sheltered employment / industrial toelevering + cleanroom medical + diensten maatwerk",
            cut_option=f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + equity 39.4m composition",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>WestVlaanderen>Lichtervelde>OptimaT_HuizeTordale>JR2025_statutory_L5",
            notes=f"tick2214; Medium CW; omzet primary; bruto≫omzet (~{RATIO}x) extreme + equity JUMP 39.4m + FTE 788.8; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Odas/Ecoso/Werkhuizen Min/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="OptimaT omzet JUMP 11.92m / bruto≫omzet ~3.54x / equity JUMP 39.4m (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>WestVlaanderen>Lichtervelde>OptimaT>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=f"CW omzet JUMP envelope 11.92m / bruto 42.26m ≫ omzet (~{RATIO}x) / pnl JUMP 1.91m / equity JUMP 39.41m / FTE JUMP 788.8; large West-VL maatwerk; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Lichtervelde-Torhout / public loonkost path / industrial+pharma clients",
            stated_goal="Sheltered employment maatwerk industrial+medical+services",
            measured_outcome=f"omzet JUMP +2.41%; bruto JUMP +6.75%; pnl JUMP +13.7%; equity JUMP +3.75%; FTE JUMP +1.1%; bruto≫omzet ~{RATIO}x",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF/VDAB/gemeente split; equity 39.4m composition + 4 VE allocation",
            status="open",
            struck_reason="",
            notes=f"tick2214; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; West-Vlaanderen maatwerk dual after Odas",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="OptimaT VZW / Huize Tordale (Lichtervelde-Torhout / maatwerk)",
            name_fr="OptimaT ASBL / Huize Tordale (Lichtervelde-Torhout / entreprise de travail adapté)",
            name_en="OptimaT / Huize Tordale sheltered workshop (Lichtervelde; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://optimat.be/",
            foi_email="info@optimat.be",
            foi_postal="Kortemarkstraat 86, 8810 Lichtervelde",
            notes=f"tick2214 YE2025 Medium CW NL+EN+FR + Strong KBO 0429.649.325 Actief VZW Huize Tordale 4 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 09.06.2026; KBO zetel Bruggestraat 39 Torhout; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>WestVlaanderen>Lichtervelde>OptimaT>NBB_PDF_assets_debt_bruto_gt_omzet_3_54x",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; equity JUMP EUR{EQUITY} composition; 4 VE + Lichtervelde/Torhout site allocation; ISO13485 cleanroom euro path",
            why_it_matters="Medium CW shows one of the largest West-VL maatwerk VZWs (omzet 11.92m / bruto 42.26m ~3.54x / equity 39.4m / FTE 788.8 / 4 VE) with extreme bruto≫omzet under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="OptimaT VZW / Huize Tordale",
            recipient_email="info@optimat.be",
            recipient_postal="Kortemarkstraat 86, 8810 Lichtervelde",
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
            notes="tick2214; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2220",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — OptimaT / Huize Tordale (NBB PDF / bruto≫omzet ~{RATIO}x / equity 39.4m)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Huize Tordale VZW trading as OptimaT — KBO **0429.649.325** (Actief; Bruggestraat 39, 8820 Torhout; ops Kortemarkstraat 86 Lichtervelde; **4 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@optimat.be · Kortemarkstraat 86, 8810 Lichtervelde · +32 51 68 02 00  
**sources:** [CW EN](https://www.companyweb.be/en/0429649325/optimat) · [CW NL](https://www.companyweb.be/nl/0429649325/optimat) · [CW FR](https://www.companyweb.be/fr/0429649325/optimat) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0429649325) · [optimat.be](https://optimat.be/)  
**tick:** 2213  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 02.04.1984; naam **Huize Tordale**; **4 VE**; RSZ NACE **88.993**; zetel Bruggestraat 39 Torhout; trading OptimaT Lichtervelde.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +2.41%; bruto **EUR{BRUTO:,}** JUMP +6.75% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** JUMP +13.7%; equity **EUR{EQUITY:,}** JUMP +3.75%; FTE **{FTE}** JUMP vs {FTE_PY}; filed **09.06.2026**.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: OptimaT VZW / Huize Tordale
via info@optimat.be
Kortemarkstraat 86, 8810 Lichtervelde
Betreft: Openbaarmaking jaarrekening 2025 Huize Tordale / OptimaT (KBO 0429.649.325)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Bruto EUR42.26m ≫ omzet EUR11.92m (~{RATIO}x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
3. Equity JUMP EUR39.412.585 composition.
4. 4 VE + Lichtervelde/Torhout site cost allocation.
5. ISO13485 cleanroom / medical devices euro path vs industrial/diensten split.

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
        "rq_2214": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — OptimaT / Huize Tordale YE2025 Medium (omzet JUMP 11.92m / bruto≫omzet ~3.54x / equity JUMP 39.4m)",
            "instructions": "Completed leftover OptimaT after Odas; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2214 OptimaT/Huize Tordale 0429.649.325 Medium; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; 4 VE; AGB Bornem JR2024; FARO/REW YE2024; next rq_2215; next every-10 2220",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2215",
            title="leftover dual hole-fill after OptimaT — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2214 after OptimaT/Huize Tordale YE2025 Medium (omzet JUMP 11.92m / bruto≫omzet ~3.54x / equity JUMP 39.4m). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Manus/Constructief/De Ploeg/Aksent/Waardenmakerij if YE2025; Vlotter YE2024). "
                "Do NOT redo OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, "
                "Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, "
                "Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, "
                "InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, "
                "Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
                "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2214 OptimaT; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2220",
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
        row["last_unit_id"] = "rq_2214"
        row["ticks_completed"] = "2214"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2214 leftover OptimaT/Huize Tordale 0429.649.325 Medium (omzet JUMP 11.92m; bruto 42.26m ≫ omzet ~{RATIO}x; "
            f"pnl JUMP 1.91m; equity JUMP 39.41m; FTE JUMP 788.8; 4 VE); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2215; next every-10 2220; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2213")

log_block = f"""
## Tick 2214 - {TS} - rq_2214 OptimaT / Huize Tordale (omzet JUMP 11.92m / bruto≫omzet ~{RATIO}x / equity JUMP 39.4m / Medium)

- Unit: **rq_2214** leftover dual after **rq_2212 Ecoso**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **Huize Tordale VZW trading OptimaT** YE2025 (KBO **0429.649.325**; Bruggestraat 39 Torhout / Kortemarkstraat 86 Lichtervelde; **Actief** **4 VE**; RSZ NACE **88.993**). Do not redo Odas/Ecoso/Werkhuizen Min/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +2.41% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +6.75% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** JUMP +13.7% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +3.75%; FTE **{FTE}** JUMP vs {FTE_PY}; neerlegging **09.06.2026**. Strong KBO Actief 4 VE. Assets/debt Unknown. Medium. FOI via info@optimat.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2214=done + rq_2215 open; loop_state ticks=2213; raw docs/doge/data/raw/tick2214/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: rq_2215 (AGB/FARO-if-YE2025 / AIESH-REW / Manus-Constructief-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2214 OptimaT")

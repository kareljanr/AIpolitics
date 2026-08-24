# -*- coding: utf-8 -*-
"""Tick 2212 leftover dual — Ecoso Mechelen YE2025 Medium."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T16:40:00Z"

ENTITY = "vzw_ecoso_mechelen"
OMZET = 5616998
BRUTO = 7662595
PNL = 13789
EQUITY = 7150781
FTE = 175.7
OMZET_PY = 5163556
BRUTO_PY = 7498374
PNL_PY = 274534
EQUITY_PY = 7136992
FTE_PY = 170.9
RATIO = round(BRUTO / OMZET, 2)  # ~1.36

SRC_EN = "src_ecoso_jr2025_cw_en"
COMM = "comm_ecoso_jr2025_statutory_maatwerk_omzet_jump_pnl_drop_95pct_17ve"
LB = "lb_ecoso_omzet_5_62m_pnl_drop_95pct_17ve_jr2025"
GAP = "gap_ecoso_nbb_pdf_assets_debt_pnl_drop_95pct_17ve_matrix_l5"

PI = "6.90"
ABS = "7.6"
COST = "5.1"
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
            source_id="src_ecoso_jr2025_cw_nl",
            title="Companyweb NL Ecoso YE2025 statutory",
            url="https://www.companyweb.be/nl/0629934529/ecoso",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2212; YE2025 omzet JUMP {OMZET} (+8.78%) bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} (-94.98%) equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 02.07.2026; raw docs/doge/data/raw/tick2212/",
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN Ecoso YE2025 statutory",
            url="https://www.companyweb.be/en/0629934529/ecoso",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2212; EN mirror YE2025 Medium; filed 02-07-2026; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; Employees {FTE}; raw tick2212/",
        ),
        dict(
            source_id="src_ecoso_jr2025_cw_fr",
            title="Companyweb FR Ecoso YE2025 statutory",
            url="https://www.companyweb.be/fr/0629934529/ecoso",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes=f"tick2212; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}; Marge brute {BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2212/",
        ),
        dict(
            source_id="src_ecoso_kbo_2212",
            title="KBO Ecoso 0629.934.529 Actief VZW Mechelen 17 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0629934529",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2212; Actief VZW sinds 20.04.2015; zetel Oude Baan 1F 2800 Mechelen; 17 VE; RSZ/BTW NACE 88.993",
        ),
        dict(
            source_id="src_ecoso_site_contact_2212",
            title="Ecoso FOI channel info@ecoso.be",
            url="https://www.ecoso.be/",
            publisher="Ecoso VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2212; info@ecoso.be; Oude Baan 1F 2800 Mechelen; maatwerk",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    ("bud_ecoso_omzet_jr2025_statutory", "2025", OMZET, "CW statutory omzet / Turnover YE2025", f"tick2212; Medium CW; omzet JUMP +8.78% vs YE2024 {OMZET_PY}; primary envelope"),
    ("bud_ecoso_bruto_jr2025_statutory", "2025", BRUTO, "CW statutory bruto_marge / Gross margin YE2025", f"tick2212; Medium CW; bruto JUMP +2.19% vs YE2024 {BRUTO_PY}; bruto/omzet ~{RATIO}x"),
    ("bud_ecoso_pnl_jr2025_statutory", "2025", PNL, "CW statutory winst / Profit-Loss after tax YE2025", f"tick2212; Medium CW; pnl DROP -94.98% vs YE2024 {PNL_PY}"),
    ("bud_ecoso_equity_jr2025_statutory", "2025", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", f"tick2212; Medium CW; equity JUMP +0.19% vs YE2024 {EQUITY_PY}"),
    ("bud_ecoso_fte_jr2025_statutory", "2025", FTE, f"CW social-balance FTE / Employees {FTE}", f"tick2212; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown"),
    ("bud_ecoso_omzet_jr2024_statutory_cmp", "2024", OMZET_PY, "CW statutory omzet YE2024 comparative", f"tick2212; YE2024 omzet {OMZET_PY} comparative"),
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
            title="Ecoso Mechelen YE2025 leftover dual (omzet JUMP 5.62m / pnl DROP -95% / 17 VE / Medium)",
            entity_id=ENTITY,
            beneficiary="maatwerkers / clients Antwerpen Mechelen belt",
            legal_basis="VZW maatwerk (KBO 0629.934.529; Actief; 17 VE; RSZ NACE 88.993)",
            decision_date="2026-07-02",
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
            evaluation_url="https://www.companyweb.be/en/0629934529/ecoso",
            stated_goal="Sheltered employment maatwerk Mechelen",
            cut_option="Publish NBB PDF assets/debt FOI; disclose pnl DROP -95% vs omzet JUMP + 17 VE cost allocation",
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Mechelen>Ecoso>JR2025_statutory_L5",
            notes=f"tick2212; Medium CW; omzet primary; pnl crater -95% despite omzet JUMP + FTE JUMP; 17 VE sprawl; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn; do not redo Werkhuizen Min/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name="Ecoso omzet JUMP 5.62m / pnl DROP -95% / 17 VE (YE2025)",
            level="L5",
            type="maatwerk_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Mechelen>Ecoso>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes=f"CW omzet JUMP envelope 5.62m / bruto 7.66m (~{RATIO}x) / pnl DROP 14k -95% from YE2024 275k / equity 7.15m / FTE JUMP 175.7 / 17 VE; Mechelen maatwerk; assets/debt Unknown",
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="maatwerkers Mechelen / public loonkost path",
            stated_goal="Sheltered employment maatwerk",
            measured_outcome="omzet JUMP +8.78%; bruto JUMP +2.19%; pnl DROP -94.98%; equity JUMP +0.19%; FTE JUMP +2.8%; 17 VE",
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose pnl crater -95% vs omzet JUMP + 17 VE site cost matrix + loonkost/GESCO/ESF split",
            status="open",
            struck_reason="",
            notes=f"tick2212; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; after Werkhuizen Min",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Ecoso VZW (Mechelen / maatwerk)",
            name_fr="Ecoso ASBL (Malines / entreprise de travail adapté)",
            name_en="Ecoso sheltered workshop (Mechelen; maatwerk)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.ecoso.be/",
            foi_email="info@ecoso.be",
            foi_postal="Oude Baan 1F, 2800 Mechelen",
            notes=f"tick2212 YE2025 Medium CW NL+EN+FR + Strong KBO 0629.934.529 Actief VZW 17 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl DROP {PNL} (-95%) equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 02.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Mechelen>Ecoso>NBB_PDF_assets_debt_pnl_drop_95pct_17ve",
            entity_id=ENTITY,
            what_is_missing=f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); pnl DROP EUR{PNL} vs YE2024 EUR{PNL_PY} (-94.98%) recon with omzet JUMP EUR{OMZET} (+8.78%) and FTE JUMP {FTE_PY}->{FTE}; 17 VE cost allocation; loonkost/GESCO/ESF/VDAB/gemeente matrix behind bruto EUR{BRUTO}",
            why_it_matters="Medium CW shows Mechelen maatwerk VZW (omzet 5.62m / 175.7 FTE / 17 VE) with pnl crater -95% despite omzet+FTE JUMP under public subsidy path; assets/debt unpublished",
            priority="8",
            recipient_body="Ecoso VZW",
            recipient_email="info@ecoso.be",
            recipient_postal="Oude Baan 1F, 2800 Mechelen",
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
            notes="tick2212; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; AGB Bornem JR2024; next every-10 2220",
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Ecoso Mechelen (NBB PDF / pnl DROP -95% / 17 VE)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ecoso VZW — KBO **0629.934.529** (Actief; Oude Baan 1F, 2800 Mechelen; **17 VE**; FTE {FTE} CW; RSZ NACE **88.993**)  
**recipient:** info@ecoso.be · Oude Baan 1F, 2800 Mechelen  
**sources:** [CW EN](https://www.companyweb.be/en/0629934529/ecoso) · [CW NL](https://www.companyweb.be/nl/0629934529/ecoso) · [CW FR](https://www.companyweb.be/fr/0629934529/ecoso) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0629934529) · [ecoso.be](https://www.ecoso.be/)  
**tick:** 2212  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 20.04.2015; **17 VE**; RSZ NACE **88.993**; zetel Oude Baan 1F Mechelen.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +8.78%; bruto **EUR{BRUTO:,}** (~{RATIO}x); pnl **EUR{PNL:,}** DROP -94.98% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}**; FTE **{FTE}** JUMP vs {FTE_PY}; filed **02.07.2026**.
- Assets/debt Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Ecoso VZW
via info@ecoso.be
Oude Baan 1F, 2800 Mechelen
Betreft: Openbaarmaking jaarrekening 2025 Ecoso (KBO 0629.934.529)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. PnL DROP EUR13.789 vs YE2024 EUR274.534 (-94,98%) recon with omzet JUMP +8,78% and FTE JUMP 170,9→175,7.
3. Loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix achter bruto EUR7.66m.
4. Cost allocation across **17 VE**.
5. Equity path EUR7.150.781.

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
        "rq_2212": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": "leftover dual — Ecoso YE2025 Medium (omzet JUMP 5.62m / pnl DROP -95% / 17 VE)",
            "instructions": "Completed leftover Ecoso after Werkhuizen Min; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent",
            "notes": f"tick2212 Ecoso 0629.934.529 Medium; omzet JUMP {OMZET} bruto {BRUTO} pnl DROP {PNL} (-95%) equity JUMP {EQUITY} FTE JUMP {FTE}; 17 VE Mechelen; AGB Bornem JR2024; FARO/REW YE2024; Vlotter YE2024 deferred; next rq_2213; next every-10 2220",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2213",
            title="leftover dual hole-fill after Ecoso — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2213 after Ecoso Mechelen YE2025 Medium (omzet JUMP 5.62m / pnl DROP -95% / 17 VE). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: Vlotter Facilities still YE2024; De Ploeg/OptimaT/Manus/Constructief if YE2025). "
                "Do NOT redo Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, "
                "MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, "
                "De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "NLZ/Natuur-en-Landschapszorg, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2212 Ecoso; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; next EVERY-10 at 2220",
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
        row["last_unit_id"] = "rq_2212"
        row["ticks_completed"] = "2212"
        row["paused"] = "no"
        row["notes"] = (
            f"tick2212 leftover Ecoso 0629.934.529 Medium (omzet JUMP 5.62m; bruto 7.66m ~{RATIO}x; "
            f"pnl DROP 14k -95%; equity JUMP 7.15m; FTE JUMP 175.7; 17 VE Mechelen); "
            "AGB Bornem JR2024; FARO/REW YE2024; next rq_2213; next every-10 2220; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2212")

log_block = f"""
## Tick 2212 - {TS} - rq_2212 Ecoso Mechelen (omzet JUMP 5.62m / pnl DROP -95% / 17 VE / Medium)

- Unit: **rq_2212** leftover dual after **rq_2211 Werkhuizen Min**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **Ecoso VZW** YE2025 (KBO **0629.934.529**; Oude Baan 1F Mechelen; **Actief** **17 VE**; RSZ NACE **88.993**). Deferred Vlotter Facilities (YE2024-only). Do not redo Werkhuizen Min/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/NLZ.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +8.78% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +2.19% (~{RATIO}x); pnl **EUR{PNL}** DROP -94.98% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +0.19%; FTE **{FTE}** JUMP vs {FTE_PY}; neerlegging **02.07.2026**. Strong KBO Actief 17 VE. Assets/debt Unknown. Medium. FOI via info@ecoso.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2212=done + rq_2213 open; loop_state ticks=2212; raw docs/doge/data/raw/tick2212/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: rq_2213 (AGB/FARO-if-YE2025 / AIESH-REW / unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2212 Ecoso")

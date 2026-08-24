# tick2215 — Groep Maatwerk YE2025 Medium (omzet DROP 1.18m / bruto≫omzet ~1.39x / pnl LOSS FLIP)
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10_000_000)

ENTITY_ID = "vzw_groep_maatwerk_tienen"
TICK = "2215"
UTC = "2026-08-26T17:25:00Z"
ACCESSED = "2026-08-26"

OMZET_25 = 1179969
OMZET_24 = 1269476
BRUTO_25 = 1641848
BRUTO_24 = 1683780
PNL_25 = -16910
PNL_24 = 27829
EQUITY_25 = 1139690
EQUITY_24 = 1156600
FTE_25 = 17.9
RATIO = round(BRUTO_25 / OMZET_25, 2)  # ~1.39

GAP_ID = "gap_groep_maatwerk_nbb_pdf_assets_debt_pnl_loss_flip_bruto_gt_omzet_matrix_l5"
SRC_EN = "src_groep_maatwerk_jr2025_cw_en"
SRC_NL = "src_groep_maatwerk_jr2025_cw_nl"
SRC_FR = "src_groep_maatwerk_jr2025_cw_fr"
SRC_KBO = "src_groep_maatwerk_kbo_2215"
SRC_SITE = "src_groep_maatwerk_site_contact_2215"
COMM_ID = "comm_groep_maatwerk_jr2025_statutory_federatie_pnl_loss_flip_bruto_gt_omzet"
LB_ID = "lb_groep_maatwerk_omzet_drop_1_18m_pnl_loss_flip_bruto_gt_omzet_jr2025"

PI = "6.50"
ABS = "7.0"
COST = "4.2"
DIFF = "3.0"


def read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        rows = list(r)
        return list(r.fieldnames or []), rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def append_rows(path: Path, new_rows: list[dict]) -> None:
    fields, rows = read_csv(path)
    existing_ids = {row.get(fields[0]) for row in rows}
    id_key = fields[0]
    added = 0
    for nr in new_rows:
        if nr.get(id_key) in existing_ids:
            for i, row in enumerate(rows):
                if row.get(id_key) == nr.get(id_key):
                    rows[i] = {**row, **nr}
                    break
        else:
            rows.append({k: nr.get(k, "") for k in fields})
            added += 1
    write_csv(path, fields, rows)
    print(path.name, "rows", len(rows), "added", added)


def update_research_queue() -> None:
    fields, rows = read_csv(DATA / "research_queue.csv")
    by_id = {r["task_id"]: r for r in rows}
    r = by_id["rq_2215"]
    r["status"] = "done"
    r["entity_id"] = ENTITY_ID
    r["title"] = (
        "leftover dual — Groep Maatwerk YE2025 Medium "
        "(omzet DROP 1.18m / bruto≫omzet ~1.39x / pnl LOSS FLIP)"
    )
    r["updated_utc"] = UTC
    r["notes"] = (
        "tick2215 Groep Maatwerk 0421.292.675 YE2025 Medium CW NL+EN+FR; omzet 1179969 DROP -7.05%; "
        f"bruto 1641848 DROP -2.49% (bruto≫omzet ~{RATIO}x); pnl -16910 LOSS FLIP vs +27829; "
        "equity 1139690 DROP -1.46%; FTE 17.9; neerlegging 15.05.2026; Strong KBO Actief VZW 1 VE "
        "Tienen RSZ 94.110 / BTW 88.993; FOI ready not sent; AGB Bornem JR2024; FARO/REW YE2024; "
        "OptimaT already tick2214"
    )
    r["instructions"] = (
        "DONE tick2215 Groep Maatwerk YE2025. Do not redo. Next: AGB/FARO-if-YE2025 / AIESH-REW / "
        "unused maatwerk-WZC-IGS."
    )
    if "rq_2216" not in by_id:
        rows.append(
            {
                "task_id": "rq_2216",
                "title": (
                    "leftover dual hole-fill after Groep Maatwerk — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2216 after rq_2215 Groep Maatwerk YE2025 Medium (omzet DROP 1.18m / "
                    "bruto≫omzet ~1.39x / pnl LOSS FLIP). Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "maatwerk/WZC/IGS with live sourced €. Do not redo Groep Maatwerk/OptimaT/Odas/"
                    "Ecoso/Werkhuizen MIN/ACG/Noordheuvel/Arcor/Kemphaan/Entiris."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2215 Groep Maatwerk; FARO/AIESH/REW still YE2024; "
                    "AGB Bornem JR2024; next EVERY-10 2220"
                ),
            }
        )
    else:
        by_id["rq_2216"]["status"] = "open"
        by_id["rq_2216"]["updated_utc"] = UTC
    write_csv(DATA / "research_queue.csv", fields, rows)
    print("research_queue updated; open head rq_2216")


def update_loop_state() -> None:
    fields, rows = read_csv(DATA / "loop_state.csv")
    row = rows[0]
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = UTC
    row["last_unit_id"] = "rq_2215"
    row["ticks_completed"] = "2215"
    row["paused"] = "no"
    row["notes"] = (
        "tick2215 Groep Maatwerk 0421.292.675 Medium (omzet DROP 1.18m; bruto≫omzet ~1.39x 1.64m; "
        "pnl LOSS FLIP -17k; equity DROP 1.14m; FTE 17.9; 1 VE Tienen federatie); AGB Bornem JR2024; "
        "FARO/REW YE2024; OptimaT tick2214; next rq_2216; next every-10 2220; continuous hole_fill"
    )
    write_csv(DATA / "loop_state.csv", fields, rows)
    print("loop_state -> 2215")


def write_foi_draft() -> None:
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    path = FOI_DRAFTS / f"{GAP_ID}.md"
    path.write_text(
        f"""# FOI draft — Groep Maatwerk (NBB PDF / pnl LOSS FLIP / bruto≫omzet ~{RATIO}x)

**gap_id:** `{GAP_ID}`  
**status:** ready (NOT sent)  
**entity:** GROEP MAATWERK VZW — KBO **0421.292.675** (Actief; Goossensvest 34, 3300 Tienen; **1 VE**; FTE 17.9 CW; RSZ NACE **94.110**; BTW NACE **88.993**)  
**recipient:** info@groepmaatwerk.be · Goossensvest 34, 3300 Tienen  
**sources:** [CW EN](https://www.companyweb.be/en/0421292675/groep-maatwerk) · [CW NL](https://www.companyweb.be/nl/0421292675/groep-maatwerk) · [CW FR](https://www.companyweb.be/fr/0421292675/groep-maatwerk) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421292675) · [groepmaatwerk.be](https://groepmaatwerk.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 26.04.1980; **1 VE**; zetel Goossensvest 34 Tienen; RSZ NACE **94.110** (werkgeversorganisatie); BTW NACE **88.993**; Vlaamse Federatie van Beschutte Werkplaatsen / maatwerkfederatie.
- CW YE2025: omzet **EUR1,179,969** DROP -7.05% vs YE2024 EUR1,269,476; bruto **EUR1,641,848** DROP -2.49% (bruto≫omzet ~{RATIO}x); pnl **EUR-16,910** LOSS FLIP vs YE2024 profit EUR27,829; equity **EUR1,139,690** DROP -1.46%; FTE **17.9**; filed **15.05.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024. OptimaT already tick2214.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: GROEP MAATWERK VZW
via info@groepmaatwerk.be
Goossensvest 34, 3300 Tienen
Betreft: Openbaarmaking jaarrekening 2025 Groep Maatwerk (KBO 0421.292.675)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Bruto EUR1.641.848 vs omzet EUR1.179.969 (~{RATIO}x) — lidgelden/vorming/fondsen/projectsubsidies matrix.
3. Pnl LOSS FLIP EUR-16.910 (vs YE2024 winst EUR27.829) reconciliatie met equity DROP EUR1.139.690 (-1,46%) en omzet DROP -7,05%.
4. Publieke vs private opbrengsten (VDAB/departement WSE/ESF/leden) en FTE 17,9 koststructuur.
5. Eventuele herstructurering / fuseepad toelichting 2025-2026.

Periode YE2025 (+ YE2024 comparative). Ref: {GAP_ID}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )
    print("FOI draft", path)


def append_log() -> None:
    entry = f"""
## Tick {TICK} - {UTC} - rq_2215 Groep Maatwerk (omzet DROP 1.18m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / Medium)

- Unit: **rq_2215** leftover dual after **rq_2214 OptimaT**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; REW still **YE2024**. Took named FREE leftover **GROEP MAATWERK VZW** YE2025 (KBO **0421.292.675**; Goossensvest 34 Tienen; **Actief** **1 VE**; RSZ NACE **94.110** / BTW **88.993**) — previously deferred. Do not redo OptimaT/Odas/Ecoso/Werkhuizen MIN/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/Aarova/MWP/AGE stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR1179969** DROP -7.05% vs YE2024 EUR1269476; bruto **EUR1641848** DROP -2.49% (bruto≫omzet ~{RATIO}x); pnl **EUR-16910** LOSS FLIP vs YE2024 EUR27829; equity **EUR1139690** DROP -1.46%; FTE **17.9**; neerlegging **15.05.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@groepmaatwerk.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY_ID}); foi + draft {GAP_ID}; rq_2215=done + rq_2216 open; loop_state ticks=2215; raw docs/doge/data/raw/tick2215/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: rq_2216 (AGB/FARO-if-YE2025 / AIESH-REW / unused maatwerk-WZC-IGS).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log appended")


def main() -> None:
    append_rows(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY_ID,
                "name_nl": "GROEP MAATWERK VZW (Tienen / federatie beschutte werkplaatsen)",
                "name_fr": "GROEP MAATWERK ASBL (Tirlemont / fédération entreprises de travail adapté)",
                "name_en": "GROEP MAATWERK VZW (Tienen / Flemish sheltered-workshop federation)",
                "level": "parastatal",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://groepmaatwerk.be/",
                "foi_email": "info@groepmaatwerk.be",
                "foi_postal": "Goossensvest 34, 3300 Tienen",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0421.292.675 Actief VZW 1 VE "
                    "RSZ 94.110 / BTW 88.993; omzet DROP 1179969 bruto DROP 1641848 "
                    f"(bruto≫omzet ~{RATIO}x) pnl LOSS FLIP -16910 equity DROP 1139690 FTE 17.9; "
                    f"neerlegging 15.05.2026; assets/debt Unknown; FOI {GAP_ID}; preferred AGB Bornem "
                    "JR2024; FARO/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN GROEP MAATWERK YE2025 statutory",
                "url": "https://www.companyweb.be/en/0421292675/groep-maatwerk",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN YE2025 Medium; Last balance sheet year 2025; Turnover 1179969; "
                    "Gross margin 1641848; Profit/Loss -16910; Equity 1139690; Employees 17.9; "
                    "filed 15-05-2026; raw tick2215/"
                ),
            },
            {
                "source_id": SRC_NL,
                "title": "Companyweb NL GROEP MAATWERK YE2025 statutory",
                "url": "https://www.companyweb.be/nl/0421292675/groep-maatwerk",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; NL mirror YE2025 Medium; Laatste balansjaar 2025; Omzet 1179969; "
                    "Brutomarge 1641848; Winst/Verlies -16910; Eigen vermogen 1139690; Personeel 17,9; "
                    "raw tick2215/"
                ),
            },
            {
                "source_id": SRC_FR,
                "title": "Companyweb FR GROEP MAATWERK YE2025 statutory",
                "url": "https://www.companyweb.be/fr/0421292675/groep-maatwerk",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA 1179969; "
                    "Marge brute 1641848; Perte -16910; Capitaux propres 1139690; raw tick2215/"
                ),
            },
            {
                "source_id": SRC_KBO,
                "title": "KBO GROEP MAATWERK 0421.292.675 Actief VZW Tienen 1 VE",
                "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0421292675",
                "publisher": "KBO FOD Economie",
                "accessed_date": ACCESSED,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW sinds 26.04.1980; naam GROEP MAATWERK; zetel Goossensvest 34 "
                    "3300 Tienen sinds 15.09.2004; 1 VE; RSZ NACE 94.110; BTW NACE 88.993; "
                    "Vlaamse federatie beschutte werkplaatsen"
                ),
            },
            {
                "source_id": SRC_SITE,
                "title": "Groep Maatwerk FOI channel info@groepmaatwerk.be",
                "url": "https://groepmaatwerk.be/",
                "publisher": "GROEP MAATWERK VZW",
                "accessed_date": ACCESSED,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@groepmaatwerk.be; Goossensvest 34 3300 Tienen; sector federation site"
                ),
            },
        ],
    )

    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_groep_maatwerk_omzet_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(OMZET_25),
                "amount_min_eur": str(OMZET_25),
                "amount_max_eur": str(OMZET_25),
                "basis": "CW statutory omzet / Turnover YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet DROP -7.05% vs YE2024 {OMZET_24}; primary envelope",
            },
            {
                "budget_id": "bud_groep_maatwerk_bruto_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(BRUTO_25),
                "amount_min_eur": str(BRUTO_25),
                "amount_max_eur": str(BRUTO_25),
                "basis": "CW statutory bruto / Gross margin YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto DROP -2.49% vs YE2024 {BRUTO_24}; bruto≫omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_groep_maatwerk_pnl_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(PNL_25),
                "amount_min_eur": str(PNL_25),
                "amount_max_eur": str(PNL_25),
                "basis": "CW statutory winst/verlies / Profit-Loss YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP vs YE2024 profit {PNL_24}",
            },
            {
                "budget_id": "bud_groep_maatwerk_equity_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(EQUITY_25),
                "amount_min_eur": str(EQUITY_25),
                "amount_max_eur": str(EQUITY_25),
                "basis": "CW statutory eigen_vermogen / Equity YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity DROP -1.46% vs YE2024 {EQUITY_24}",
            },
            {
                "budget_id": "bud_groep_maatwerk_fte_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(FTE_25),
                "amount_min_eur": str(FTE_25),
                "amount_max_eur": str(FTE_25),
                "basis": "CW social-balance FTE / Employees 17.9",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE 17.9; assets/debt Unknown pending NBB PDF",
            },
            {
                "budget_id": "bud_groep_maatwerk_omzet_jr2024_statutory_cmp",
                "entity_id": ENTITY_ID,
                "year": "2024",
                "amount_eur": str(OMZET_24),
                "amount_min_eur": str(OMZET_24),
                "amount_max_eur": str(OMZET_24),
                "basis": "CW statutory omzet YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 omzet {OMZET_24} comparative for DROP calc",
            },
        ],
    )

    cash = {
        "2025_omzet": OMZET_25,
        "2025_bruto": BRUTO_25,
        "2025_pnl": PNL_25,
        "2025_equity": EQUITY_25,
        "2025_fte": FTE_25,
        "2024_omzet": OMZET_24,
        "2024_bruto": BRUTO_24,
        "2024_pnl": PNL_24,
        "2024_equity": EQUITY_24,
    }
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM_ID,
                "title": (
                    "Groep Maatwerk YE2025 leftover dual (omzet DROP 1.18m / "
                    f"bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / Medium)"
                ),
                "entity_id": ENTITY_ID,
                "beneficiary": "63 maatwerkbedrijven / ~20k maatwerkers Vlaanderen (federation members)",
                "legal_basis": "VZW federatie (KBO 0421.292.675; Actief; 1 VE; RSZ 94.110; BTW 88.993)",
                "decision_date": "2026-05-15",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET_25),
                "cash_by_year": json.dumps(cash, separators=(",", ":")),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": "https://www.companyweb.be/en/0421292675/groep-maatwerk",
                "stated_goal": "Sector federation / vorming / belangenbehartiging beschutte werkplaatsen",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; disclose lidgelden/vorming/fondsen/subsidie split "
                    "behind bruto≫omzet and LOSS FLIP"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Tienen>GroepMaatwerk>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary; bruto≫omzet (~{RATIO}x) + pnl LOSS FLIP; "
                    "assets/debt Unknown; preferred stall FARO/REW YE2024; AGB Bornem JR2024"
                ),
            }
        ],
    )

    append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB_ID,
                "name": (
                    f"Groep Maatwerk omzet DROP 1.18m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP (YE2025)"
                ),
                "level": "L5",
                "type": "maatwerk_federatie_vzw_statutory",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Tienen>GroepMaatwerk>JR2025",
                "annual_cost_eur": str(OMZET_25),
                "total_cost_eur": str(OMZET_25),
                "tco_notes": (
                    f"CW omzet DROP envelope 1.18m / bruto 1.64m ≫ omzet (~{RATIO}x) / pnl LOSS FLIP "
                    "-17k / equity DROP 1.14m / FTE 17.9; federation not TE-additive of 348bn"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "member maatwerkbedrijven / coaches / vorming participants",
                "stated_goal": "Flemish sheltered-workshop federation advocacy + training",
                "measured_outcome": (
                    "omzet DROP -7.05%; bruto DROP -2.49%; pnl LOSS FLIP; equity DROP -1.46%; "
                    f"bruto≫omzet ~{RATIO}x"
                ),
                "absurdity_score": ABS,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose lidgelden/vorming/fondsen/"
                    "projectsubsidie matrix behind bruto≫omzet + LOSS FLIP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP_ID}; stall FARO/REW YE2024; AGB Bornem JR2024; "
                    "OptimaT already tick2214"
                ),
            }
        ],
    )

    append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP_ID,
                "hierarchy_path": (
                    "Vlaanderen>VlaamsBrabant>Tienen>GroepMaatwerk>NBB_PDF_assets_debt_pnl_loss_flip"
                ),
                "entity_id": ENTITY_ID,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BRUTO_25} ≫ "
                    f"omzet EUR{OMZET_25} (~{RATIO}x) lidgelden/vorming/fondsen/projectsubsidies matrix; "
                    f"pnl LOSS FLIP EUR{PNL_25} vs YE2024 profit EUR{PNL_24}; equity DROP composition; "
                    "publieke vs private opbrengsten"
                ),
                "why_it_matters": (
                    "Medium CW shows Vlaamse maatwerkfederatie (omzet 1.18m DROP / bruto 1.64m ≫ omzet / "
                    "pnl LOSS FLIP / FTE 17.9 / 1 VE) with unpublished assets/debt under public-adjacent "
                    "sector funding path"
                ),
                "priority": "8",
                "recipient_body": "GROEP MAATWERK VZW",
                "recipient_email": "info@groepmaatwerk.be",
                "recipient_postal": "Goossensvest 34, 3300 Tienen",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP_ID}.md",
                "status": "ready",
                "date_ready": ACCESSED,
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM_ID,
                "linked_leaderboard_id": LB_ID,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; "
                    "AGB Bornem JR2024; next every-10 2220"
                ),
            }
        ],
    )

    write_foi_draft()
    update_research_queue()
    update_loop_state()
    append_log()
    print("DONE tick2215 Groep Maatwerk")


if __name__ == "__main__":
    main()

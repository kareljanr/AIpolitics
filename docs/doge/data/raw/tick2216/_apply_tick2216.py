# tick2216 — De Kringloopwinkel Deltagroep YE2025 Medium
# (omzet JUMP 7.08m / bruto≫omzet ~1.44x / pnl DROP -76% / FTE JUMP)
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10_000_000)

ENTITY_ID = "vzw_kringloopwinkel_deltagroep"
TICK = "2216"
UTC = "2026-08-26T17:45:00Z"
ACCESSED = "2026-08-26"

OMZET_25 = 7084153
OMZET_24 = 6764072
BRUTO_25 = 10211363
BRUTO_24 = 9562335
PNL_25 = 61321
PNL_24 = 250522
EQUITY_25 = 7022047
EQUITY_24 = 7078135
FTE_25 = 234.3
FTE_24 = 215.9
RATIO = round(BRUTO_25 / OMZET_25, 2)  # ~1.44

GAP_ID = "gap_kringloop_deltagroep_nbb_pdf_assets_debt_pnl_drop_bruto_gt_omzet_fte_jump_matrix_l5"
SRC_EN = "src_kringloop_deltagroep_jr2025_cw_en"
SRC_NL = "src_kringloop_deltagroep_jr2025_cw_nl"
SRC_FR = "src_kringloop_deltagroep_jr2025_cw_fr"
SRC_KBO = "src_kringloop_deltagroep_kbo_2216"
SRC_SITE = "src_kringloop_deltagroep_site_contact_2216"
COMM_ID = "comm_kringloop_deltagroep_jr2025_statutory_maatwerk_pnl_drop_bruto_gt_omzet"
LB_ID = "lb_kringloop_deltagroep_omzet_7_08m_pnl_drop_76pct_bruto_gt_omzet_jr2025"

PI = "6.90"
ABS = "7.2"
COST = "5.0"
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
    r = by_id["rq_2216"]
    r["status"] = "done"
    r["entity_id"] = ENTITY_ID
    r["title"] = (
        "leftover dual — Kringloopwinkel Deltagroep YE2025 Medium "
        "(omzet JUMP 7.08m / pnl DROP -76% / bruto≫omzet ~1.44x / FTE JUMP)"
    )
    r["updated_utc"] = UTC
    r["blocked_gap_id"] = GAP_ID
    r["notes"] = (
        "tick2216 Kringloopwinkel Deltagroep 0455.224.265 YE2025 Medium CW NL+EN+FR; "
        f"omzet {OMZET_25} JUMP +4.73%; bruto {BRUTO_25} JUMP +6.79% (bruto≫omzet ~{RATIO}x); "
        f"pnl {PNL_25} DROP -75.52% vs {PNL_24}; equity {EQUITY_25} DROP -0.79%; "
        f"FTE {FTE_25} JUMP vs {FTE_24}; neerlegging 10.06.2026; Strong KBO Actief VZW 12 VE "
        "Kortrijk RSZ 88.993 / BTW 47.792; Constructief sister Deltagroep; FOI ready not sent; "
        "AGB Bornem JR2024; FARO/REW YE2024; race note: rq_2215 kept Groep Maatwerk+Constructief"
    )
    r["instructions"] = (
        "DONE tick2216 Kringloopwinkel Deltagroep YE2025. Do not redo. Next: AGB/FARO-if-YE2025 / "
        "AIESH-REW / Mobiel-or-unused maatwerk-WZC-IGS."
    )
    if "rq_2217" not in by_id:
        rows.append(
            {
                "task_id": "rq_2217",
                "title": (
                    "leftover dual hole-fill after Kringloop Deltagroep — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Mobiel-or-unused maatwerk-WZC-IGS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2217 after rq_2216 Kringloopwinkel Deltagroep YE2025 Medium "
                    f"(omzet JUMP 7.08m / pnl DROP -76% / bruto≫omzet ~{RATIO}x / FTE JUMP). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Mobiel (Deltagroep sister) or unused "
                    "maatwerk/WZC/IGS with live sourced €. Do not redo Kringloop Deltagroep/"
                    "Constructief/Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen MIN/ACG/"
                    "Noordheuvel/Arcor/Kemphaan/Entiris."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2216 Kringloop Deltagroep; FARO/AIESH/REW still YE2024; "
                    "AGB Bornem JR2024; next EVERY-10 2220"
                ),
            }
        )
    else:
        by_id["rq_2217"]["status"] = "open"
        by_id["rq_2217"]["updated_utc"] = UTC
    write_csv(DATA / "research_queue.csv", fields, rows)
    print("research_queue updated; open head rq_2217")


def update_loop_state() -> None:
    fields, rows = read_csv(DATA / "loop_state.csv")
    row = rows[0]
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = UTC
    row["last_unit_id"] = "rq_2216"
    row["ticks_completed"] = "2216"
    row["paused"] = "no"
    row["notes"] = (
        f"tick2216 Kringloopwinkel Deltagroep 0455.224.265 Medium (omzet JUMP 7.08m; "
        f"bruto≫omzet ~{RATIO}x 10.21m; pnl DROP 61k -76%; equity DROP 7.02m; FTE JUMP 234.3; "
        "12 VE Kortrijk Deltagroep); AGB Bornem JR2024; FARO/REW YE2024; Constructief sister; "
        "next rq_2217; next every-10 2220; continuous hole_fill"
    )
    write_csv(DATA / "loop_state.csv", fields, rows)
    print("loop_state -> 2216")


def write_foi_draft() -> None:
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    path = FOI_DRAFTS / f"{GAP_ID}.md"
    path.write_text(
        f"""# FOI draft — Kringloopwinkel Deltagroep (NBB PDF / pnl DROP -76% / bruto≫omzet ~{RATIO}x / FTE JUMP)

**gap_id:** `{GAP_ID}`  
**status:** ready (NOT sent)  
**entity:** De Kringloopwinkel Deltagroep VZW — KBO **0455.224.265** (Actief; Warande(Heu) 9, 8501 Kortrijk; **12 VE**; FTE 234.3 CW; RSZ NACE **88.993**; BTW NACE **47.792**; Deltagroep)  
**recipient:** info@deltagroep.be · Warande(Heu) 9, 8501 Kortrijk · 056 23 45 20  
**sources:** [CW EN](https://www.companyweb.be/en/0455224265/de-kringloopwinkel-deltagroep) · [CW NL](https://www.companyweb.be/nl/0455224265/de-kringloopwinkel-deltagroep) · [CW FR](https://www.companyweb.be/fr/0455224265/de-kringloopwinkel-deltagroep) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455224265) · [deltagroep.be](https://www.deltagroep.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 07.04.1995; **12 VE**; zetel Warande(Heu) 9 Kortrijk; RSZ NACE **88.993**; BTW NACE **47.792**; Deltagroep sister of Constructief (Warande 7).
- CW YE2025: omzet **EUR7,084,153** JUMP +4.73% vs YE2024 EUR6,764,072; bruto **EUR10,211,363** JUMP +6.79% (bruto≫omzet ~{RATIO}x); pnl **EUR61,321** DROP -75.52% vs YE2024 EUR250,522; equity **EUR7,022,047** DROP -0.79%; FTE **234.3** JUMP vs 215.9; filed **10.06.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/REW YE2024. Constructief already race-filled tick2215.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Kringloopwinkel Deltagroep VZW
via info@deltagroep.be
Warande(Heu) 9, 8501 Kortrijk
Betreft: Openbaarmaking jaarrekening 2025 Kringloopwinkel Deltagroep (KBO 0455.224.265)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. PnL DROP EUR61.321 vs YE2024 EUR250.522 (-75,52%) reconciliatie met FTE JUMP 215,9→234,3 en omzet JUMP +4,73%.
3. Bruto EUR10.211.363 ≫ omzet EUR7.084.153 (~{RATIO}x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente/OVAM matrix.
4. Deltagroep related-party transfers vs Constructief VZW 0465.225.262 / Mobiel.
5. Per-VE / winkel vs atelier cost allocation (12 VE).

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
## Tick {TICK} - {UTC} - rq_2216 Kringloopwinkel Deltagroep (omzet JUMP 7.08m / bruto≫omzet ~{RATIO}x / pnl DROP -76% / FTE JUMP / Medium)

- Unit: **rq_2216** leftover dual after **rq_2215 Groep Maatwerk (+race Constructief)**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH probe thin/404-class; REW still **YE2024**. Took named FREE leftover **De Kringloopwinkel Deltagroep VZW** YE2025 (KBO **0455.224.265**; Warande(Heu) 9 Kortrijk; **Actief** **12 VE**; RSZ NACE **88.993** / BTW **47.792**) — Constructief sister. Do not redo Constructief/Groep Maatwerk/OptimaT/Odas/Ecoso/Werkhuizen MIN/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/Aarova/MWP/AGE stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET_25}** JUMP +4.73% vs YE2024 EUR{OMZET_24}; bruto **EUR{BRUTO_25}** JUMP +6.79% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL_25}** DROP -75.52% vs YE2024 EUR{PNL_24}; equity **EUR{EQUITY_25}** DROP -0.79%; FTE **{FTE_25}** JUMP vs {FTE_24}; neerlegging **10.06.2026**. Strong KBO Actief 12 VE. Assets/debt Unknown. Medium. FOI via info@deltagroep.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY_ID}); foi + draft {GAP_ID}; rq_2216=done + rq_2217 open; loop_state ticks=2216; raw docs/doge/data/raw/tick2216/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: rq_2217 (AGB/FARO-if-YE2025 / AIESH-REW / Mobiel-or-unused).
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
                "name_nl": "De Kringloopwinkel Deltagroep VZW (Kortrijk / maatwerk / hergebruik)",
                "name_fr": "De Kringloopwinkel Deltagroep ASBL (Courtrai / entreprise de travail adapté / réemploi)",
                "name_en": "De Kringloopwinkel Deltagroep VZW (Kortrijk / sheltered employment / reuse)",
                "level": "parastatal",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.deltagroep.be/",
                "foi_email": "info@deltagroep.be",
                "foi_postal": "Warande(Heu) 9, 8501 Kortrijk",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0455.224.265 Actief VZW 12 VE "
                    f"RSZ 88.993 / BTW 47.792; omzet JUMP {OMZET_25} bruto JUMP {BRUTO_25} "
                    f"(bruto≫omzet ~{RATIO}x) pnl DROP {PNL_25} equity DROP {EQUITY_25} FTE JUMP {FTE_25}; "
                    f"neerlegging 10.06.2026; assets/debt Unknown; FOI {GAP_ID}; Constructief sister "
                    "Deltagroep Warande 7; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN De Kringloopwinkel Deltagroep YE2025 statutory",
                "url": "https://www.companyweb.be/en/0455224265/de-kringloopwinkel-deltagroep",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN YE2025 Medium; Last balance sheet year 2025; Turnover {OMZET_25}; "
                    f"Gross margin {BRUTO_25}; Profit/Loss {PNL_25}; Equity {EQUITY_25}; Employees {FTE_25}; "
                    "filed 10-06-2026; raw tick2216/"
                ),
            },
            {
                "source_id": SRC_NL,
                "title": "Companyweb NL De Kringloopwinkel Deltagroep YE2025 statutory",
                "url": "https://www.companyweb.be/nl/0455224265/de-kringloopwinkel-deltagroep",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; NL mirror YE2025 Medium; Laatste balansjaar 2025; Omzet {OMZET_25}; "
                    f"Brutomarge {BRUTO_25}; Winst/Verlies {PNL_25}; Eigen vermogen {EQUITY_25}; "
                    f"Personeel {str(FTE_25).replace('.', ',')}; raw tick2216/"
                ),
            },
            {
                "source_id": SRC_FR,
                "title": "Companyweb FR De Kringloopwinkel Deltagroep YE2025 statutory",
                "url": "https://www.companyweb.be/fr/0455224265/de-kringloopwinkel-deltagroep",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET_25}; "
                    f"Marge brute {BRUTO_25}; Bénéfice {PNL_25}; Capitaux propres {EQUITY_25}; raw tick2216/"
                ),
            },
            {
                "source_id": SRC_KBO,
                "title": "KBO De Kringloopwinkel Deltagroep 0455.224.265 Actief VZW Kortrijk 12 VE",
                "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0455224265",
                "publisher": "KBO FOD Economie",
                "accessed_date": ACCESSED,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW sinds 07.04.1995; naam DE KRINGLOOPWINKEL DELTAGROEP; "
                    "zetel Warande(Heu) 9 8501 Kortrijk sinds 12.06.2017; 12 VE; RSZ NACE 88.993; "
                    "BTW NACE 47.792; boekjaar 31 december; jaarvergadering mei"
                ),
            },
            {
                "source_id": SRC_SITE,
                "title": "Deltagroep FOI channel info@deltagroep.be",
                "url": "https://www.deltagroep.be/",
                "publisher": "De Kringloopwinkel Deltagroep VZW",
                "accessed_date": ACCESSED,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@deltagroep.be; Warande(Heu) 9 8501 Kortrijk; tel 056 23 45 20; "
                    "Constructief sister site"
                ),
            },
        ],
    )

    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_kringloop_deltagroep_omzet_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(OMZET_25),
                "amount_min_eur": str(OMZET_25),
                "amount_max_eur": str(OMZET_25),
                "basis": "CW statutory omzet / Turnover YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet JUMP +4.73% vs YE2024 {OMZET_24}; primary envelope",
            },
            {
                "budget_id": "bud_kringloop_deltagroep_bruto_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(BRUTO_25),
                "amount_min_eur": str(BRUTO_25),
                "amount_max_eur": str(BRUTO_25),
                "basis": "CW statutory bruto / Gross margin YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +6.79% vs YE2024 {BRUTO_24}; bruto≫omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_kringloop_deltagroep_pnl_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(PNL_25),
                "amount_min_eur": str(PNL_25),
                "amount_max_eur": str(PNL_25),
                "basis": "CW statutory winst/verlies / Profit-Loss YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl DROP -75.52% vs YE2024 {PNL_24}",
            },
            {
                "budget_id": "bud_kringloop_deltagroep_equity_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(EQUITY_25),
                "amount_min_eur": str(EQUITY_25),
                "amount_max_eur": str(EQUITY_25),
                "basis": "CW statutory eigen_vermogen / Equity YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity DROP -0.79% vs YE2024 {EQUITY_24}",
            },
            {
                "budget_id": "bud_kringloop_deltagroep_fte_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(FTE_25),
                "amount_min_eur": str(FTE_25),
                "amount_max_eur": str(FTE_25),
                "basis": "CW social-balance FTE / Employees 234.3",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE_24}->{FTE_25}; assets/debt Unknown pending NBB PDF",
            },
            {
                "budget_id": "bud_kringloop_deltagroep_omzet_jr2024_statutory_cmp",
                "entity_id": ENTITY_ID,
                "year": "2024",
                "amount_eur": str(OMZET_24),
                "amount_min_eur": str(OMZET_24),
                "amount_max_eur": str(OMZET_24),
                "basis": "CW statutory omzet YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 omzet {OMZET_24} comparative for JUMP calc",
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
        "2024_fte": FTE_24,
        "ve": 12,
        "ratio_bruto_omzet": RATIO,
    }
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM_ID,
                "title": (
                    "Kringloopwinkel Deltagroep YE2025 leftover dual "
                    f"(omzet JUMP 7.08m / pnl DROP -76% / bruto≫omzet ~{RATIO}x / FTE JUMP)"
                ),
                "entity_id": ENTITY_ID,
                "beneficiary": "maatwerkers / reuse clients Zuid-West-Vlaanderen Kortrijk (Deltagroep 12 VE)",
                "legal_basis": "VZW maatwerk / hergebruik (KBO 0455.224.265; Actief; 12 VE; RSZ NACE 88.993)",
                "decision_date": "2026-06-10",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET_25),
                "cash_by_year": json.dumps(cash, separators=(",", ":")),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": "https://www.companyweb.be/en/0455224265/de-kringloopwinkel-deltagroep",
                "stated_goal": "Sheltered employment / reuse retail maatwerk Kortrijk (Deltagroep)",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; disclose pnl DROP -76% with FTE JUMP + bruto~1.44x "
                    "loonkost matrix + Constructief related-party"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>KringloopDeltagroep>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + pnl DROP "
                    "-75.52% with FTE JUMP primary absurdity; assets/debt Unknown; preferred AGB Bornem "
                    "JR2024; FARO/REW YE2024; Constructief sister; not TE-additive of 348bn"
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
                    f"Kringloopwinkel Deltagroep omzet JUMP 7.08m / pnl DROP -76% / "
                    f"bruto≫omzet ~{RATIO}x / FTE JUMP (YE2025)"
                ),
                "level": "L5",
                "type": "maatwerk_vzw_statutory",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>KringloopDeltagroep>JR2025",
                "annual_cost_eur": str(OMZET_25),
                "total_cost_eur": str(OMZET_25),
                "tco_notes": (
                    f"CW omzet JUMP envelope 7.08m / bruto 10.21m (~{RATIO}x) / pnl DROP 61k -76% from "
                    "YE2024 251k / equity DROP 7.02m / FTE JUMP 234.3; Kortrijk Deltagroep reuse maatwerk; "
                    "assets/debt Unknown"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "maatwerkers Kortrijk / public loonkost path / Deltagroep reuse clients",
                "stated_goal": "Sheltered employment maatwerk + tweedehands hergebruik",
                "measured_outcome": (
                    "omzet JUMP +4.73%; bruto JUMP +6.79%; pnl DROP -75.52%; equity DROP -0.79%; "
                    f"FTE JUMP {FTE_24}->{FTE_25}"
                ),
                "absurdity_score": ABS,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose pnl DROP -76% with FTE JUMP + "
                    f"bruto~{RATIO}x loonkost/GESCO/ESF/VDAB/OVAM split + Constructief related-party"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP_ID}; stall FARO/REW YE2024; AGB Bornem JR2024; "
                    "Constructief sister after Groep Maatwerk/Constructief race"
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
                    "Vlaanderen>WestVlaanderen>Kortrijk>KringloopDeltagroep>"
                    "NBB_PDF_assets_debt_pnl_drop_bruto_gt_omzet_fte_jump"
                ),
                "entity_id": ENTITY_ID,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); pnl DROP EUR{PNL_25} vs "
                    f"YE2024 EUR{PNL_24} (-75.52%) recon with FTE JUMP {FTE_24}->{FTE_25}; bruto EUR{BRUTO_25} "
                    f"≫ omzet EUR{OMZET_25} (~{RATIO}x) loonkost/GESCO/ESF/VDAB/gemeente/OVAM matrix; "
                    "Deltagroep related-party vs Constructief 0465.225.262 / Mobiel; 12 VE allocation"
                ),
                "why_it_matters": (
                    "Medium CW shows Kortrijk Deltagroep reuse maatwerk VZW (omzet 7.08m / 234.3 FTE) with "
                    "pnl DROP -76% while hiring FTE under public subsidy path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "De Kringloopwinkel Deltagroep VZW",
                "recipient_email": "info@deltagroep.be",
                "recipient_postal": "Warande(Heu) 9, 8501 Kortrijk",
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
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2220; "
                    "Constructief sister Deltagroep"
                ),
            }
        ],
    )

    write_foi_draft()
    update_research_queue()
    update_loop_state()
    append_log()
    print("tick2216 complete")


if __name__ == "__main__":
    main()

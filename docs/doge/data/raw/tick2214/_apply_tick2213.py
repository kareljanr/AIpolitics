# tick2213 — Odas Brugge YE2025 Medium (omzet JUMP 11.34m / bruto≫omzet ~1.72x / pnl LOSS NARROW)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10_000_000)

ENTITY_ID = "vzw_odas_brugge"
TICK = "2213"
UTC = "2026-08-26T16:55:00Z"
ACCESSED = "2026-08-26"

# YE2025 sourced (CW NL+EN+FR)
OMZET_25 = 11339072
OMZET_24 = 10091970
BRUTO_25 = 19484424
BRUTO_24 = 17713823
PNL_25 = -285014
PNL_24 = -594866
EQUITY_25 = 11259247
EQUITY_24 = 11626013
FTE_25 = 518.1
FTE_24 = 521.6

GAP_ID = "gap_odas_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_loss_narrow_equity_drop_matrix_l5"
SRC_EN = "src_odas_jr2025_cw_en"
SRC_NL = "src_odas_jr2025_cw_nl"
SRC_FR = "src_odas_jr2025_cw_fr"
SRC_KBO = "src_odas_kbo_2213"
SRC_SITE = "src_odas_site_contact_2213"
COMM_ID = "comm_odas_jr2025_statutory_maatwerk_omzet_jump_bruto_gt_omzet_pnl_loss_narrow"
LB_ID = "lb_odas_omzet_11_34m_bruto_gt_omzet_pnl_loss_narrow_jr2025"


def read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        rows = list(r)
        return list(r.fieldnames or []), rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def append_rows(path: Path, new_rows: list[dict]) -> None:
    fields, rows = read_csv(path)
    existing_ids = set()
    id_key = fields[0]
    for row in rows:
        existing_ids.add(row.get(id_key))
    added = 0
    for nr in new_rows:
        if nr.get(id_key) in existing_ids:
            # update in place
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
    # close rq_2213 (rq_2212 Ecoso already done on main)
    r = by_id["rq_2213"]
    r["status"] = "done"
    r["entity_id"] = ENTITY_ID
    r["title"] = (
        "leftover dual — Odas Brugge YE2025 Medium "
        "(omzet JUMP 11.34m / bruto≫omzet ~1.72x / pnl LOSS NARROW -285k)"
    )
    r["updated_utc"] = UTC
    r["notes"] = (
        "tick2213 Odas 0407.201.149 YE2025 Medium CW NL+EN+FR; omzet 11339072 JUMP +12.36%; "
        "bruto 19484424 JUMP +10.0% (bruto≫omzet ~1.72x); pnl -285014 LOSS NARROW +52.09% vs "
        "-594866; equity 11259247 DROP -3.15%; FTE 518.1 DROP vs 521.6; neerlegging 05.06.2026; "
        "Strong KBO Actief VZW 8 VE RSZ 88.993; FOI ready not sent; AGB Bornem JR2024; "
        "FARO/AIESH/REW YE2024; Groep Maatwerk YE2025 deferred; Ecoso already tick2212"
    )
    r["instructions"] = (
        "DONE tick2213 Odas YE2025. Do not redo. Next: AGB/FARO-if-YE2025 / AIESH-REW / "
        "Groep Maatwerk or unused maatwerk-WZC-IGS."
    )
    # spawn rq_2214 if missing
    if "rq_2214" not in by_id:
        rows.append(
            {
                "task_id": "rq_2214",
                "title": (
                    "leftover dual hole-fill after Odas — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/GroepMaatwerk-unused maatwerk-WZC-IGS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2214 after rq_2213 Odas YE2025 Medium (omzet JUMP 11.34m / "
                    "bruto≫omzet ~1.72x / pnl LOSS NARROW). Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Groep Maatwerk "
                    "0421.292.675 YE2025 or unused maatwerk/WZC/IGS with live sourced €. "
                    "Do not redo Odas/Ecoso/Werkhuizen MIN/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2213 Odas; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; "
                    "Groep Maatwerk YE2025 deferred; next EVERY-10 2220"
                ),
            }
        )
    else:
        by_id["rq_2214"]["status"] = "open"
        by_id["rq_2214"]["updated_utc"] = UTC
    write_csv(DATA / "research_queue.csv", fields, rows)
    print("research_queue updated; open head rq_2214")


def update_loop_state() -> None:
    fields, rows = read_csv(DATA / "loop_state.csv")
    row = rows[0]
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = UTC
    row["last_unit_id"] = "rq_2213"
    row["ticks_completed"] = "2213"
    row["paused"] = "no"
    row["notes"] = (
        "tick2213 Odas Brugge 0407.201.149 Medium (omzet JUMP 11.34m; bruto≫omzet ~1.72x 19.48m; "
        "pnl LOSS NARROW -285k; equity DROP 11.26m -3.15%; FTE DROP 518.1; 8 VE Brugge); "
        "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Groep Maatwerk YE2025 deferred; Ecoso tick2212; "
        "next rq_2214; next every-10 2220; continuous hole_fill"
    )
    write_csv(DATA / "loop_state.csv", fields, rows)
    print("loop_state -> 2213")


def write_foi_draft() -> None:
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    path = FOI_DRAFTS / f"{GAP_ID}.md"
    path.write_text(
        f"""# FOI draft — Odas Brugge (NBB PDF / bruto≫omzet ~1.72x / pnl LOSS NARROW / equity DROP)

**gap_id:** `{GAP_ID}`  
**status:** ready (NOT sent)  
**entity:** Odas VZW — KBO **0407.201.149** (Actief; Pathoekeweg 11G, 8000 Brugge; **8 VE**; FTE 518.1 CW; RSZ NACE **88.993**)  
**recipient:** info@odas.be · Pathoekeweg 11G, 8000 Brugge · +32 50 34 33 99  
**sources:** [CW EN](https://www.companyweb.be/en/0407201149/odas) · [CW NL](https://www.companyweb.be/nl/0407201149/odas) · [CW FR](https://www.companyweb.be/fr/0407201149/odas) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407201149) · [odas.be](https://www.odas.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 12.05.1966; **8 VE**; RSZ NACE **88.993**; BTW NACE 88.999/55.100/56.111; zetel Pathoekeweg 11G Brugge sinds 16.01.2025.
- CW YE2025: omzet **EUR11,339,072** JUMP +12.36% vs YE2024 EUR10,091,970; bruto **EUR19,484,424** JUMP +10.0% (bruto≫omzet ~1.72x); pnl **EUR-285,014** LOSS NARROW +52.09% vs YE2024 loss EUR-594,866; equity **EUR11,259,247** DROP -3.15% vs YE2024 EUR11,626,013; FTE **518.1** DROP vs 521.6; filed **05.06.2026**.
- Assets/debt/cash Unknown. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred FREE Groep Maatwerk YE2025; Ecoso already tick2212.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Odas VZW
via info@odas.be
Pathoekeweg 11G, 8000 Brugge
Betreft: Openbaarmaking jaarrekening 2025 Odas (KBO 0407.201.149)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Bruto EUR19.484.424 vs omzet EUR11.339.072 (~1,72x) — loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix.
3. Pnl LOSS NARROW EUR-285.014 (+52,09% vs YE2024 verlies EUR-594.866) reconciliatie met equity DROP EUR11.259.247 (-3,15%) en FTE DROP 521,6→518,1.
4. Split over 8 VE (industry / catering / groen / andere) en publieke vs private omzet.
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
## Tick {TICK} - {UTC} - rq_2213 Odas Brugge (omzet JUMP 11.34m / bruto≫omzet ~1.72x / pnl LOSS NARROW -285k / Medium)

- Unit: **rq_2213** leftover dual after **rq_2212 Ecoso**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **404/YE2024-class**; REW still **YE2024**. Took named FREE leftover **Odas VZW** YE2025 (KBO **0407.201.149**; Pathoekeweg 11G Brugge; **Actief** **8 VE**; RSZ NACE **88.993**) — previously deferred as YE2024-only, now live. Deferred FREE Groep Maatwerk **0421.292.675** YE2025. Do not redo Ecoso/Werkhuizen MIN/ACG/Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Trianval/Ijsedal/Aarova/MWP/AGE stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR11339072** JUMP +12.36% vs YE2024 EUR10091970; bruto **EUR19484424** JUMP +10.0% (bruto≫omzet ~1.72x); pnl **EUR-285014** LOSS NARROW +52.09% vs YE2024 EUR-594866; equity **EUR11259247** DROP -3.15%; FTE **518.1** DROP vs 521.6; neerlegging **05.06.2026**. Strong KBO Actief 8 VE. Assets/debt Unknown. Medium. FOI via info@odas.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.90); entities (+1 {ENTITY_ID}); foi + draft {GAP_ID}; rq_2213=done + rq_2214 open; loop_state ticks=2213; raw docs/doge/data/raw/tick2213/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2210**; next **2220**). Next: rq_2214 (AGB/FARO-if-YE2025 / AIESH-REW / GroepMaatwerk-or-unused).
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
                "name_nl": "Odas VZW (Brugge / maatwerk)",
                "name_fr": "Odas ASBL (Bruges / entreprise de travail adapté)",
                "name_en": "Odas VZW (Bruges sheltered workshop / maatwerk)",
                "level": "parastatal",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.odas.be/",
                "foi_email": "info@odas.be",
                "foi_postal": "Pathoekeweg 11G, 8000 Brugge",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.201.149 Actief VZW 8 VE "
                    "RSZ NACE 88.993; omzet JUMP 11339072 bruto JUMP 19484424 (bruto≫omzet ~1.72x) "
                    "pnl LOSS NARROW -285014 equity DROP 11259247 FTE DROP 518.1; neerlegging 05.06.2026; "
                    f"assets/debt Unknown; FOI {GAP_ID}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Odas YE2025 statutory",
                "url": "https://www.companyweb.be/en/0407201149/odas",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN YE2025 Medium; Last balance sheet year 2025; Turnover 11339072; "
                    "Gross margin 19484424; Profit/Loss -285014; Equity 11259247; Employees 518.1; "
                    "filed 05-06-2026; raw tick2213/"
                ),
            },
            {
                "source_id": SRC_NL,
                "title": "Companyweb NL Odas YE2025 statutory",
                "url": "https://www.companyweb.be/nl/0407201149/odas",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; NL mirror YE2025 Medium; Laatste balansjaar 2025; Omzet 11339072; "
                    "Brutomarge 19484424; Winst/Verlies -285014; Eigen vermogen 11259247; Personeel 518,1; "
                    "raw tick2213/"
                ),
            },
            {
                "source_id": SRC_FR,
                "title": "Companyweb FR Odas YE2025 statutory",
                "url": "https://www.companyweb.be/fr/0407201149/odas",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": ACCESSED,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA 11339072; "
                    "Marge brute 19484424; Perte -285014; Capitaux propres 11259247; raw tick2213/"
                ),
            },
            {
                "source_id": SRC_KBO,
                "title": "KBO Odas 0407.201.149 Actief VZW Brugge 8 VE",
                "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407201149",
                "publisher": "KBO FOD Economie",
                "accessed_date": ACCESSED,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW sinds 12.05.1966; naam ODAS; zetel Pathoekeweg 11G 8000 Brugge "
                    "sinds 16.01.2025; 8 VE; RSZ NACE 88.993; BTW NACE 88.999/55.100/56.111; aannemer erkenning"
                ),
            },
            {
                "source_id": SRC_SITE,
                "title": "Odas FOI channel info@odas.be",
                "url": "https://www.odas.be/",
                "publisher": "Odas VZW",
                "accessed_date": ACCESSED,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@odas.be; +32 50 34 33 99; Pathoekeweg 11G 8000 Brugge; "
                    "also industrie@odas.be / jobs@odas.be"
                ),
            },
        ],
    )

    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_odas_omzet_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(OMZET_25),
                "amount_min_eur": str(OMZET_25),
                "amount_max_eur": str(OMZET_25),
                "basis": "CW statutory omzet / Turnover YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet JUMP +12.36% vs YE2024 {OMZET_24}; primary envelope",
            },
            {
                "budget_id": "bud_odas_bruto_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(BRUTO_25),
                "amount_min_eur": str(BRUTO_25),
                "amount_max_eur": str(BRUTO_25),
                "basis": "CW statutory bruto / Gross margin YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +10.0% vs YE2024 {BRUTO_24}; bruto≫omzet ~1.72x",
            },
            {
                "budget_id": "bud_odas_pnl_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(PNL_25),
                "amount_min_eur": str(PNL_25),
                "amount_max_eur": str(PNL_25),
                "basis": "CW statutory winst/verlies / Profit-Loss YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS NARROW +52.09% vs YE2024 {PNL_24}",
            },
            {
                "budget_id": "bud_odas_equity_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(EQUITY_25),
                "amount_min_eur": str(EQUITY_25),
                "amount_max_eur": str(EQUITY_25),
                "basis": "CW statutory eigen_vermogen / Equity YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity DROP -3.15% vs YE2024 {EQUITY_24}",
            },
            {
                "budget_id": "bud_odas_fte_jr2025_statutory",
                "entity_id": ENTITY_ID,
                "year": "2025",
                "amount_eur": str(FTE_25),
                "amount_min_eur": str(FTE_25),
                "amount_max_eur": str(FTE_25),
                "basis": "CW social-balance FTE / Employees 518.1",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE DROP vs YE2024 {FTE_24}; assets/debt Unknown pending NBB PDF",
            },
            {
                "budget_id": "bud_odas_omzet_jr2024_statutory_cmp",
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

    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM_ID,
                "title": (
                    "Odas Brugge YE2025 leftover dual (omzet JUMP 11.34m / bruto≫omzet ~1.72x / "
                    "pnl LOSS NARROW -285k / Medium)"
                ),
                "entity_id": ENTITY_ID,
                "beneficiary": "maatwerkers / industry+catering+groen clients Brugge belt",
                "legal_basis": "VZW maatwerk (KBO 0407.201.149; Actief; 8 VE; RSZ NACE 88.993)",
                "decision_date": "2026-06-05",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET_25),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET_25},"2025_bruto":{BRUTO_25},"2025_pnl":{PNL_25},'
                    f'"2025_equity":{EQUITY_25},"2025_fte":{FTE_25},'
                    f'"2024_omzet":{OMZET_24},"2024_bruto":{BRUTO_24},"2024_pnl":{PNL_24},'
                    f'"2024_equity":{EQUITY_24},"2024_fte":{FTE_24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": "https://www.companyweb.be/en/0407201149/odas",
                "stated_goal": "Sheltered employment / industry+catering+groen maatwerk Brugge",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~1.72x loonkost matrix + "
                    "pnl LOSS NARROW -285k / equity DROP -3.15% recon"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>West-Vlaanderen>Brugge>Odas>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; bruto≫omzet subsidy-path flag; "
                    f"FOI {GAP_ID}; not TE-additive"
                ),
            }
        ],
    )

    append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB_ID,
                "name": "Odas omzet JUMP 11.34m / bruto≫omzet ~1.72x / pnl LOSS NARROW (YE2025)",
                "level": "L5",
                "type": "maatwerk_vzw_statutory",
                "hierarchy_path": "Vlaanderen>West-Vlaanderen>Brugge>Odas>JR2025",
                "annual_cost_eur": str(OMZET_25),
                "total_cost_eur": str(OMZET_25),
                "tco_notes": (
                    "CW omzet JUMP envelope 11.34m / bruto 19.48m (~1.72x) / pnl LOSS NARROW -285k "
                    "from YE2024 loss -595k (+52%) / equity DROP 11.26m (-3.15%) / FTE DROP 518.1; "
                    "Brugge 8-VE maatwerk; assets/debt Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "maatwerkers Brugge / public loonkost path / industry+catering+groen clients",
                "stated_goal": "Sheltered employment maatwerk industry + catering + groen",
                "measured_outcome": (
                    "omzet JUMP +12.36%; bruto≫omzet ~1.72x; pnl LOSS NARROW +52.09%; "
                    "equity DROP -3.15%; FTE DROP -3.5"
                ),
                "absurdity_score": "7.7",
                "cost_score": "5.9",
                "difficulty": "3.0",
                "priority_index": "6.90",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet loonkost/GESCO/ESF/"
                    "VDAB/gemeente split; recon LOSS NARROW -285k with equity DROP -3.15% and FTE DROP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP_ID}; not TE-additive of 348bn; "
                    "residual dual off pure annual top10"
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
                    "Vlaanderen>West-Vlaanderen>Brugge>Odas>NBB_PDF_assets_debt_bruto_gt_omzet_"
                    "pnl_loss_narrow_equity_drop"
                ),
                "entity_id": ENTITY_ID,
                "what_is_missing": (
                    "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                    "bruto EUR19484424 vs omzet EUR11339072 (~1.72x) loonkostsubsidie/GESCO/ESF/VDAB/"
                    "gemeente matrix; pnl LOSS NARROW EUR-285014 vs YE2024 loss EUR-594866 (+52.09%) "
                    "recon with equity DROP EUR11259247 (-3.15%) and FTE DROP 521.6->518.1; "
                    "8 VE industry/catering/groen split"
                ),
                "why_it_matters": (
                    "Medium CW shows Brugge maatwerk VZW (omzet 11.34m / bruto 19.48m / FTE 518.1) "
                    "with bruto≫omzet ~1.72x, continued loss under public subsidy path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Odas VZW",
                "recipient_email": "info@odas.be",
                "recipient_postal": "Pathoekeweg 11G, 8000 Brugge",
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
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall AGB/FARO/AIESH/REW"
                ),
            }
        ],
    )

    write_foi_draft()
    update_research_queue()
    update_loop_state()
    append_log()
    print("DONE tick2212 Odas")


if __name__ == "__main__":
    main()

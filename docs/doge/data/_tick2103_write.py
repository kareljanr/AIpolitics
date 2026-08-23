# tick 2103 — Comnexio YE2025 Medium CW leftover dual (ORES contact-centre daughter)
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T06:25:00Z"
DATE = "2026-08-25"
ENTITY = "sc_comnexio"
GAP = "gap_comnexio_nbb_pdf_assets_debt_pnl_equity_flat_matrix_l5"
COMM = "comm_comnexio_jr2025_statutory_ores_contact_centre"
LB = "lb_comnexio_omzet_drop_9_93m_equity_flat_25k_jr2025"

OMZET = 9932761
EQUITY = 25000
BRUTO = 7151535
FTE = 147.9


def append_csv(path: Path, rows: list[dict], id_key: str):
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    have = {row.get(id_key) for row in existing}
    new_rows = [row for row in rows if row.get(id_key) not in have]
    if not new_rows:
        print(f"skip {path.name}: already present")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(existing)
        for row in new_rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"append {path.name}: +{len(new_rows)}")


sources = [
    {
        "source_id": "src_comnexio_jr2025_cw_nl",
        "title": "Comnexio Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0727639263/comnexio",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2103; YE2025 omzet/equity/bruto/FTE; pnl omitted on CW; neerlegging 18.06.2026; Medium",
    },
    {
        "source_id": "src_comnexio_jr2025_cw_en",
        "title": "Comnexio Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0727639263/comnexio",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2103; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_comnexio_jr2025_cw_fr",
        "title": "Comnexio Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0727639263/comnexio",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2103; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_comnexio_kbo_2103",
        "title": "KBO Comnexio 0727.639.263",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=727639263",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2103; Actief SC; 2 VE; NACE 82.200; pouvoir adjudicateur; info@comnexio.be; Strong identity",
    },
    {
        "source_id": "src_comnexio_nbb_consult_2103",
        "title": "NBB CBSO consult Comnexio 0727639263",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0727639263",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2103; deposit portal; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_comnexio_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_comnexio_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2103; omzet DROP 9932761 (-6.71%) vs YE2024 10647751; double-count vs ORES group possible",
    },
    {
        "budget_id": "bud_comnexio_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_comnexio_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2103; equity FLAT 25000 (0%) vs YE2024 25000; thin capital shell",
    },
    {
        "budget_id": "bud_comnexio_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_comnexio_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2103; bruto DROP 7151535 (-1.88%) vs YE2024 7288487",
    },
    {
        "budget_id": "bud_comnexio_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_comnexio_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2103; FTE JUMP 147.9 vs YE2024 147.6",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Comnexio SC (ORES contact center)",
            "name_fr": "Comnexio SC (centre d'appels ORES)",
            "name_en": "Comnexio SC (ORES Assets contact-centre daughter)",
            "level": "other",
            "parent_id": "ores",
            "community_language": "fr",
            "website": "https://www.comnexio.be",
            "foi_email": "info@comnexio.be",
            "foi_postal": "Avenue Georges Lemaitre 38, 6041 Charleroi",
            "notes": (
                "tick2103 YE2025 Medium CW NL+EN+FR + Strong KBO 0727.639.263 Actief SC "
                "2 VE pouvoir adjudicateur; omzet DROP 9.93m bruto DROP 7.15m equity FLAT 25k "
                "FTE JUMP 147.9; pnl Unknown (CW omits); NACE 82.200; ORES Assets contact-centre "
                f"daughter; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "do not redo ORES SC/ORES Assets/RESA/AIEG/AREWAL/Enodia/Fluxys"
            ),
        }
    ],
    "entity_id",
)

append_csv(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "Comnexio YE2025 leftover dual (omzet DROP 9.93m / equity FLAT 25k)",
            "entity_id": ENTITY,
            "beneficiary": "ORES Assets / Walloon DSO customers via contact-centre OSP",
            "legal_basis": "SC / aanbestedende overheid / ORES group contact centre (KBO 0727.639.263)",
            "decision_date": "2026-06-18",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE},"2025_pnl":"Unknown"}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0727639263/comnexio",
            "stated_goal": "Provide contact-centre services for ORES Assets at cost",
            "cut_option": (
                "Publish NBB PDF assets/debt/pnl FOI; map ORES Assets related-party share; "
                "explain omzet DROP -6.71pct with equity flat 25k"
            ),
            "source_id": "src_comnexio_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Wallonie>GRD>ORES>Comnexio>JR2025_statutory_L5",
            "notes": (
                "tick2103; Medium CW; pnl/assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive of 348bn; double-count vs ORES group possible"
            ),
        }
    ],
    "commitment_id",
)

append_csv(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Comnexio omzet DROP 9.93m / equity FLAT 25k ORES call-centre shell (YE2025)",
            "level": "L5",
            "type": "dso_shared_services_statutory",
            "hierarchy_path": "Wallonie>GRD>ORES>Comnexio>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary contact-centre envelope; equity flat 25k; pnl Unknown; "
                "double-count vs ORES Assets possible; assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_comnexio_jr2025_cw_en",
            "beneficiaries": "ORES Assets / Walloon DSO end-users (call centre)",
            "stated_goal": "Contact-centre OSP for ORES Assets at cost",
            "measured_outcome": (
                "omzet DROP -6.71%; bruto DROP -1.88%; equity FLAT 25000; "
                "FTE JUMP 147.9; pnl Unknown on CW"
            ),
            "absurdity_score": "5.0",
            "cost_score": "3.5",
            "difficulty": "3.5",
            "priority_index": "4.5",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/pnl FOI; disclose ORES Assets customer share; "
                "explain omzet DROP with flat 25k equity"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2103; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "DISTINCT ORES SC/Assets; do not redo RESA/AIEG/AREWAL/Enodia/Fluxys"
            ),
        }
    ],
    "item_id",
)

append_csv(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Wallonie>GRD>ORES>Comnexio>NBB_PDF_assets_debt_pnl",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); P&L (CW omits); "
                "ORES Assets vs other customer split; related-party with ORES SC; "
                "explanation of omzet DROP -6.71% with equity FLAT 25000"
            ),
            "why_it_matters": (
                "Medium CW shows 9.93m omzet ORES contact-centre SC with equity flat 25k "
                "and no published P&L; material L5 residual after ORES SC ops shell; "
                "cost-plus double-count risk vs ORES Assets"
            ),
            "priority": "8",
            "recipient_body": "Comnexio SC",
            "recipient_email": "info@comnexio.be",
            "recipient_postal": "Avenue Georges Lemaitre 38, 6041 Charleroi",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": DATE,
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "tick2103; human-send only; Medium CW; next every-10 2110",
        }
    ],
    "gap_id",
)

rq_path = DATA / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row["task_id"] == "rq_2103":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — Comnexio YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover Comnexio YE2025 Medium CW; KBO 0727.639.263; "
            f"omzet DROP {OMZET} bruto DROP {BRUTO} equity FLAT {EQUITY} FTE JUMP {FTE}; "
            f"pnl Unknown; FOI {GAP}; 2 VE; ORES Assets contact-centre daughter; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
        )
        row["notes"] = (
            "tick2103 Comnexio Medium omzet DROP 9.93m bruto DROP 7.15m equity FLAT 25k "
            "FTE JUMP 147.9 pnl Unknown; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2104; next every-10 2110"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2104" for r in rows):
    rows.append(
        {
            "task_id": "rq_2104",
            "title": "leftover dual hole-fill after Comnexio — prefer AGB/FARO-YE2025/AIESH-REW/Korian/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2104 after Comnexio YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Korian Belgium "
                "0869.769.702 if YE2025 unused, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                "Do NOT redo Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, "
                "AREWAL, Familiezorg Gent, emeis, Armonea, Colisee, AIEG, RESA, Enodia, Fluxys*, ETB, "
                "Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, "
                "CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, "
                "IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2103 Comnexio; next every-10 2110; Korian Belgium deferred if live",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2103 not found"

with (DATA / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            UTC,
            "rq_2103",
            "2103",
            "no",
            (
                "tick2103 leftover Comnexio 0727.639.263 Medium CW (omzet DROP 9.93m bruto DROP "
                "7.15m equity FLAT 25k FTE JUMP 147.9; pnl/assets/debt Unknown; 2 VE); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2104; next every-10 2110; "
                "continuous hole_fill"
            ),
        ]
    )

if "## Tick 2103 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2103 already present")
else:
    log_block = f"""

## Tick 2103 - {UTC} - rq_2103 Comnexio (omzet DROP 9.93m / equity FLAT 25k / Medium)

- Unit: **rq_2103** leftover dual after **rq_2102 ORES SC**. Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. Took deferred unused ORES contact-centre daughter **Comnexio** YE2025 (KBO **0727.639.263**; Avenue Georges Lemaitre 38 Charleroi; SC / **2 VE** / pouvoir adjudicateur; NACE **82.200**). DISTINCT from ORES SC / ORES Assets.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** DROP −6.71%; bruto **EUR{BRUTO}** DROP −1.88%; equity **EUR{EQUITY}** FLAT; FTE **{FTE}** JUMP vs YE2024 147.6; **pnl Unknown** (CW omits P&L; cost-plus historically ~0); neerlegging **18.06.2026**. Assets/debt Unknown. Medium. Strong KBO (info@comnexio.be). Omzet primary; double-count vs ORES group possible.
- Wrote: sources (+5); budgets (+4, no invented pnl); commitments (+1); leaderboard (+1 pi 4.5); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2103=done + rq_2104 open; loop_state ticks=2103; raw docs/doge/data/raw/tick2103/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 2110**). Next: rq_2104 (AGB/FARO-if-YE2025 / AIESH-REW / Korian-if-unused / unused).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2103 write OK; found=", found)

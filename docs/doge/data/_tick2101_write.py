# tick 2101 — ORES SC YE2025 Medium CW leftover dual (unused DSO ops)
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T06:10:00Z"
DATE = "2026-08-25"
ENTITY = "sc_ores"
GAP = "gap_ores_sc_nbb_pdf_assets_debt_pnl_equity_thin_matrix_l5"
COMM = "comm_ores_sc_jr2025_statutory_dso_ops"
LB = "lb_ores_sc_omzet_jump_920_91m_equity_thin_0_46m_jr2025"

OMZET = 920909050
EQUITY = 461806
BRUTO = 325847115
FTE = 3000


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
        "source_id": "src_ores_sc_jr2025_cw_nl",
        "title": "ORES SC Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0897436971/operateur-de-reseaux-d-energies",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2101; YE2025 omzet/equity/bruto/FTE; pnl omitted on CW; neerlegging 16.06.2026; Medium",
    },
    {
        "source_id": "src_ores_sc_jr2025_cw_en",
        "title": "ORES SC Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0897436971/operateur-de-reseaux-d-energies",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2101; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_ores_sc_jr2025_cw_fr",
        "title": "ORES SC Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0897436971/operateur-de-reseaux-d-energies",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2101; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_ores_sc_kbo_2101",
        "title": "KBO ORES SC 0897.436.971",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=897436971",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2101; Actief SC; 33 VE; NACE 35.140/35.220; pouvoir adjudicateur; Strong identity",
    },
    {
        "source_id": "src_ores_sc_nbb_consult_2101",
        "title": "NBB CBSO consult ORES SC 0897436971",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0897436971",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2101; deposit portal; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_ores_sc_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_ores_sc_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2101; omzet JUMP 920909050 (+16.99%) vs YE2024 787137854; double-count vs ores Assets possible",
    },
    {
        "budget_id": "bud_ores_sc_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_ores_sc_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2101; equity DROP 461806 (-0.80%) vs YE2024 465516; thin vs omzet",
    },
    {
        "budget_id": "bud_ores_sc_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_ores_sc_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2101; bruto JUMP 325847115 (+15.70%) vs YE2024 281641147",
    },
    {
        "budget_id": "bud_ores_sc_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_ores_sc_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2101; FTE JUMP 3000 vs YE2024 2819.5",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "ORES SC (Opérateur de Réseaux d'Énergies)",
            "name_fr": "ORES SC (Operateur de Reseaux d'Energies)",
            "name_en": "ORES SC (Walloon DSO network operator at cost)",
            "level": "other",
            "parent_id": "ores",
            "community_language": "fr",
            "website": "https://www.ores.be",
            "foi_email": "contact@ores.be",
            "foi_postal": "Avenue Jean Mermoz 14, 6041 Charleroi",
            "notes": (
                "tick2101 YE2025 Medium CW NL+EN+FR + Strong KBO 0897.436.971 Actief SC "
                "33 VE pouvoir adjudicateur; omzet JUMP 920.91m bruto JUMP 325.85m equity THIN "
                "0.46m FTE JUMP 3000; pnl Unknown (CW omits); NACE 35.140/35.220; "
                "cost-plus ops daughter of ORES Assets; FOI "
                f"{GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "do not redo RESA/AIEG/AREWAL/Enodia/Fluxys/ETB/Elia/BNO"
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
            "title": "ORES SC YE2025 leftover dual (omzet JUMP 920.91m / equity THIN 0.46m)",
            "entity_id": ENTITY,
            "beneficiary": "Walloon communes on ORES Assets network (elec/gas DSO ops at cost)",
            "legal_basis": "SC / aanbestedende overheid / GRD exploitant (KBO 0897.436.971)",
            "decision_date": "2026-06-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE},"2025_pnl":"Unknown"}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0897436971/operateur-de-reseaux-d-energies",
            "stated_goal": "Operate Walloon DSO networks for ORES Assets at cost",
            "cut_option": (
                "Publish NBB PDF assets/debt/pnl FOI; reconcile cost-plus vs ORES Assets; "
                "explain equity thin 0.46m vs omzet 921m"
            ),
            "source_id": "src_ores_sc_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Wallonie>GRD>ORES_SC>JR2025_statutory_L5",
            "notes": (
                "tick2101; Medium CW; pnl/assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive of 348bn; double-count vs ores Assets possible"
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
            "name": "ORES SC omzet JUMP 920.91m / equity THIN 0.46m cost-plus shell (YE2025)",
            "level": "L5",
            "type": "dso_ops_statutory",
            "hierarchy_path": "Wallonie>GRD>ORES_SC>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary DSO-ops envelope; equity thin; pnl Unknown; "
                "double-count vs ORES Assets possible; assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_ores_sc_jr2025_cw_en",
            "beneficiaries": "ORES Assets communes / Walloon elec+gas end-users",
            "stated_goal": "Operate DSO networks at cost for ORES Assets",
            "measured_outcome": (
                "omzet JUMP +16.99%; bruto JUMP +15.70%; equity DROP -0.80% thin; "
                "FTE JUMP 3000; pnl Unknown on CW"
            ),
            "absurdity_score": "6.0",
            "cost_score": "7.5",
            "difficulty": "4.0",
            "priority_index": "6.8",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/pnl FOI; map cost-plus vs ORES Assets CA; "
                "disclose elec/gas/lighting split"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2101; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "DISTINCT ores Assets; do not redo RESA/AIEG/AREWAL/Enodia/Fluxys"
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
            "hierarchy_path": "Wallonie>GRD>ORES_SC>NBB_PDF_assets_debt_pnl_equity",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); P&L (CW omits); "
                "elec/gas/lighting omzet split; related-party ORES Assets/Comnexio; "
                "explanation of equity thin 461806 vs omzet 920.91m"
            ),
            "why_it_matters": (
                "Medium CW shows 920.91m omzet Walloon DSO ops SC with equity thin 0.46m "
                "and no published P&L; material L5 residual distinct from ORES Assets; "
                "cost-plus double-count risk"
            ),
            "priority": "9",
            "recipient_body": "ORES SC",
            "recipient_email": "contact@ores.be",
            "recipient_postal": "Avenue Jean Mermoz 14, 6041 Charleroi",
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
            "notes": "tick2101; human-send only; Medium CW; next every-10 2110",
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
    if row["task_id"] == "rq_2101":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — ORES SC YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover ORES SC YE2025 Medium CW; KBO 0897.436.971; "
            f"omzet JUMP {OMZET} bruto JUMP {BRUTO} equity THIN {EQUITY} FTE JUMP {FTE}; "
            f"pnl Unknown; FOI {GAP}; 33 VE; DISTINCT ORES Assets; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
        )
        row["notes"] = (
            "tick2101 ORES SC Medium omzet JUMP 920.91m bruto JUMP 325.85m equity THIN 0.46m "
            "FTE JUMP 3000 pnl Unknown; FOI ready; superseded stale SLG-Vlaanderen claim "
            "(already mined); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2102; next every-10 2110"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2102" for r in rows):
    rows.append(
        {
            "task_id": "rq_2102",
            "title": "leftover dual hole-fill after ORES SC — prefer AGB/FARO-YE2025/AIESH-REW/Comnexio/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2102 after ORES SC YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Comnexio 0727.639.263 "
                "YE2025 live unused deferred, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                "Do NOT redo ORES SC, Always Home, SLG Operaties, SLG Vlaanderen VZW, AREWAL, "
                "Familiezorg Gent, emeis, Begralim, Armonea, Colisee, AIEG, RESA, Enodia, Fluxys*, "
                "ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, "
                "Hydria, CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, "
                "EURIDICE, IRE*, BRUGEL, ORES Assets."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2101 ORES SC; next every-10 2110; Comnexio YE2025 deferred",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2101 not found"

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
            "rq_2101",
            "2101",
            "no",
            (
                "tick2101 leftover ORES SC 0897.436.971 Medium CW (omzet JUMP 920.91m bruto JUMP "
                "325.85m equity THIN 0.46m FTE JUMP 3000; pnl/assets/debt Unknown; 33 VE); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2102; next every-10 2110; "
                "continuous hole_fill"
            ),
        ]
    )

if "## Tick 2101 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2101 already present")
else:
    log_block = f"""

## Tick 2101 - {UTC} - rq_2101 ORES SC (omzet JUMP 920.91m / equity THIN 0.46m / Medium)

- Unit: **rq_2101** leftover dual after **rq_2100 Always Home** (in_progress claim for SLG Vlaanderen superseded — that entity already mined). Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. Took unused Walloon DSO ops **ORES SC** YE2025 newly live (KBO **0897.436.971**; Avenue Jean Mermoz 14 Charleroi; SC / **33 VE** / pouvoir adjudicateur; NACE **35.140/35.220**). DISTINCT from ORES Assets (`ores`). Do not redo RESA/AIEG/AREWAL/Enodia/Fluxys/ETB/Elia/BNO/Always Home/SLG.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +16.99%; bruto **EUR{BRUTO}** JUMP +15.70%; equity **EUR{EQUITY}** DROP −0.80% thin; FTE **{FTE}** JUMP vs YE2024 2819.5; **pnl Unknown** (CW omits P&L; cost-plus historically ~0); neerlegging **16.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via contact@ores.be. Omzet primary; double-count vs ORES Assets possible.
- Wrote: sources (+5); budgets (+4, no invented pnl); commitments (+1); leaderboard (+1 pi 6.8); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2101=done + rq_2102 open; loop_state ticks=2101; raw docs/doge/data/raw/tick2101/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 2110**). Next: rq_2102 (AGB/FARO-if-YE2025 / AIESH-REW / Comnexio deferred / unused).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2101 write OK; found=", found)

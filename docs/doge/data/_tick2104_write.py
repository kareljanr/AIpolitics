# tick 2104 — INTRADEL YE2025 Medium CW leftover dual (unused Walloon waste IGS)
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T06:40:00Z"
DATE = "2026-08-25"
ENTITY = "igs_intradel"
GAP = "gap_intradel_nbb_pdf_assets_debt_pnl_loss_narrow_matrix_l5"
COMM = "comm_intradel_jr2025_statutory_waste_igs"
LB = "lb_intradel_omzet_drop_125_06m_pnl_loss_narrow_12_68m_jr2025"

OMZET = 125062424
PNL = -12682319
EQUITY = 35537642
BRUTO = 25332295
FTE = 321


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
        "source_id": "src_intradel_jr2025_cw_nl",
        "title": "INTRADEL Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0219511295/association-intercommunale-de-traitement-des-dechets-liegeois",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2104; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 04.07.2026; Medium",
    },
    {
        "source_id": "src_intradel_jr2025_cw_en",
        "title": "INTRADEL Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0219511295/association-intercommunale-de-traitement-des-dechets-liegeois",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2104; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_intradel_jr2025_cw_fr",
        "title": "INTRADEL Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0219511295/association-intercommunale-de-traitement-des-dechets-liegeois",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2104; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_intradel_kbo_2104",
        "title": "KBO INTRADEL 0219.511.295",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=219511295",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2104; Actief SC; 55 VE; NACE 38.110/35.110; pouvoir adjudicateur; Strong identity",
    },
    {
        "source_id": "src_intradel_nbb_consult_2104",
        "title": "NBB CBSO consult INTRADEL 0219511295",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0219511295",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2104; deposit portal; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_intradel_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_intradel_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2104; omzet DROP 125062424 (-3.55%) vs YE2024 129659229",
    },
    {
        "budget_id": "bud_intradel_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_intradel_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2104; pnl LOSS NARROW -12682319 (+16.51% vs YE2024 LOSS -15191078)",
    },
    {
        "budget_id": "bud_intradel_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_intradel_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2104; equity DROP 35537642 (-0.44%) vs YE2024 35693639",
    },
    {
        "budget_id": "bud_intradel_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_intradel_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2104; bruto DROP 25332295 (-3.15%) vs YE2024 26157103",
    },
    {
        "budget_id": "bud_intradel_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_intradel_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2104; FTE JUMP 321 vs YE2024 319.4",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "INTRADEL (afvalintercommunale Luik)",
            "name_fr": "INTRADEL (Association intercommunale de traitement des dechets liegeois)",
            "name_en": "INTRADEL (Liege-area waste intercommunale)",
            "level": "other",
            "parent_id": "wallonie_gov",
            "community_language": "fr",
            "website": "https://www.intradel.be",
            "foi_email": "officiel.ic-intradel@intradel.be",
            "foi_postal": "Pré Wigy 20, 4040 Herstal",
            "notes": (
                "tick2104 YE2025 Medium CW NL+EN+FR + Strong KBO 0219.511.295 Actief SC "
                "55 VE pouvoir adjudicateur; omzet DROP 125.06m bruto DROP 25.33m pnl LOSS NARROW "
                "-12.68m equity DROP 35.54m FTE JUMP 321; NACE 38.110/35.110; "
                f"FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "Korian Belgium already mined; do not redo HYGEA/BEP Environnement/IPALLE"
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
            "title": "INTRADEL YE2025 leftover dual (omzet DROP 125.06m / pnl LOSS NARROW -12.68m)",
            "entity_id": ENTITY,
            "beneficiary": "Liege-area communes (waste collection/treatment + energy from waste)",
            "legal_basis": "SC intercommunale / aanbestedende overheid (KBO 0219.511.295)",
            "decision_date": "2026-07-04",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0219511295/association-intercommunale-de-traitement-des-dechets-liegeois",
            "stated_goal": "Collect and treat non-hazardous waste for Liege-area communes",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map commune contribution matrix; "
                "explain multi-year LOSS NARROW path with equity erosion"
            ),
            "source_id": "src_intradel_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Wallonie>Liege>INTRADEL>JR2025_statutory_L5",
            "notes": (
                "tick2104; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive of 348bn; omzet primary"
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
            "name": "INTRADEL omzet DROP 125.06m / pnl LOSS NARROW -12.68m (YE2025)",
            "level": "L5",
            "type": "waste_igs_statutory",
            "hierarchy_path": "Wallonie>Liege>INTRADEL>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary waste-IGS envelope; multi-year LOSS path; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_intradel_jr2025_cw_en",
            "beneficiaries": "Liege-area commune households / waste service users (55 VE)",
            "stated_goal": "Waste collection and treatment intercommunale",
            "measured_outcome": (
                "omzet DROP -3.55%; bruto DROP -3.15%; pnl LOSS NARROW +16.51%; "
                "equity DROP -0.44%; FTE JUMP 321"
            ),
            "absurdity_score": "6.5",
            "cost_score": "7.5",
            "difficulty": "4.0",
            "priority_index": "7.0",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; commune contribution matrix; "
                "explain persistent LOSS with only narrow improvement"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2104; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "do not redo HYGEA/BEP Env/IPALLE/Korian"
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
            "hierarchy_path": "Wallonie>Liege>INTRADEL>NBB_PDF_assets_debt_pnl_loss",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); waste vs energy "
                "omzet split; commune contribution matrix; explanation of LOSS NARROW "
                "-12.68m with equity DROP"
            ),
            "why_it_matters": (
                "Medium CW shows 125.06m omzet Liege waste intercommunale with multi-year "
                "LOSS path without balanstotaal/assets/debt; material L5 residual IGS"
            ),
            "priority": "9",
            "recipient_body": "INTRADEL SC",
            "recipient_email": "officiel.ic-intradel@intradel.be",
            "recipient_postal": "Pré Wigy 20, 4040 Herstal",
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
            "notes": "tick2104; human-send only; Medium CW; next every-10 2110",
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
    if row["task_id"] == "rq_2104":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — INTRADEL YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover INTRADEL YE2025 Medium CW; KBO 0219.511.295; "
            f"omzet DROP {OMZET} bruto DROP {BRUTO} pnl LOSS NARROW {PNL} equity DROP {EQUITY} "
            f"FTE JUMP {FTE}; FOI {GAP}; 55 VE; Korian Belgium already mined; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
        )
        row["notes"] = (
            "tick2104 INTRADEL Medium omzet DROP 125.06m bruto DROP 25.33m pnl LOSS NARROW "
            "-12.68m equity DROP 35.54m FTE JUMP 321; FOI ready; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2105; next every-10 2110"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2105" for r in rows):
    rows.append(
        {
            "task_id": "rq_2105",
            "title": "leftover dual hole-fill after INTRADEL — prefer AGB/FARO-YE2025/AIESH-REW/IDELUX-Eau/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2105 after INTRADEL YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else IDELUX Eau 0204.359.994 "
                "YE2025 live unused deferred, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                "Do NOT redo INTRADEL, Comnexio, ORES SC, ORES Assets, Korian Belgium, SLG Vlaanderen, "
                "Always Home, SLG Operaties, AREWAL, HYGEA, BEP Environnement, AIEG, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, "
                "Vivaqua, Hydria, CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, "
                "SCK CEN, EURIDICE, IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2104 INTRADEL; next every-10 2110; IDELUX Eau YE2025 deferred",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2104 not found"

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
            "rq_2104",
            "2104",
            "no",
            (
                "tick2104 leftover INTRADEL 0219.511.295 Medium CW (omzet DROP 125.06m bruto DROP "
                "25.33m pnl LOSS NARROW -12.68m equity DROP 35.54m FTE JUMP 321; assets/debt Unknown; "
                "55 VE); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2105; next every-10 2110; "
                "continuous hole_fill"
            ),
        ]
    )

if "## Tick 2104 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2104 already present")
else:
    log_block = f"""

## Tick 2104 - {UTC} - rq_2104 INTRADEL (omzet DROP 125.06m / pnl LOSS NARROW -12.68m / Medium)

- Unit: **rq_2104** leftover dual after **rq_2103 Comnexio**. Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. Korian Belgium **already mined** (race tick2103 CSV). Took unused Walloon waste IGS **INTRADEL** YE2025 (KBO **0219.511.295**; Pré Wigy 20 Herstal; SC / **55 VE** / pouvoir adjudicateur; NACE **38.110/35.110**). DISTINCT from HYGEA / BEP Environnement.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** DROP −3.55%; bruto **EUR{BRUTO}** DROP −3.15%; pnl **LOSS EUR{PNL}** LOSS NARROW +16.51% vs YE2024 LOSS −15191078; equity **EUR{EQUITY}** DROP −0.44%; FTE **{FTE}** JUMP vs YE2024 319.4; neerlegging **04.07.2026**. Assets/debt Unknown. Medium. Strong KBO (officiel.ic-intradel@intradel.be). Omzet primary.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 7.0); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2104=done + rq_2105 open; loop_state ticks=2104; raw docs/doge/data/raw/tick2104/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 2110**). Next: rq_2105 (AGB/FARO-if-YE2025 / AIESH-REW / IDELUX Eau deferred / unused).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2104 write OK; found=", found)

# tick 2107 — IDELUX Développement YE2025 Medium CW leftover dual
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T07:10:00Z"
DATE = "2026-08-25"
ENTITY = "igs_idelux_developpement"
GAP = "gap_idelux_developpement_nbb_pdf_assets_debt_pnl_flip_loss_matrix_l5"
COMM = "comm_idelux_developpement_jr2025_statutory_igs"
LB = "lb_idelux_dev_omzet_drop_19_15m_pnl_flip_loss_fte_drop_jr2025"

OMZET = 19151123
PNL = -898763
EQUITY = 102328170
BRUTO = 10797628
FTE = 91.1


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
        "source_id": "src_idelux_dev_jr2025_cw_nl",
        "title": "IDELUX Développement Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0205797475/association-intercommunale-pour-le-developpement-economique-durable-de-la-province-de-luxembourg",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2107; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 19.06.2026; Medium",
    },
    {
        "source_id": "src_idelux_dev_jr2025_cw_en",
        "title": "IDELUX Développement Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0205797475/association-intercommunale-pour-le-developpement-economique-durable-de-la-province-de-luxembourg",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2107; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_idelux_dev_jr2025_cw_fr",
        "title": "IDELUX Développement Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0205797475/association-intercommunale-pour-le-developpement-economique-durable-de-la-province-de-luxembourg",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2107; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_idelux_dev_kbo_2107",
        "title": "KBO IDELUX Développement 0205.797.475",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=205797475",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2107; Actief SC; 1 VE; NACE 84.130+; pouvoir adjudicateur; Strong identity",
    },
    {
        "source_id": "src_idelux_dev_nbb_consult_2107",
        "title": "NBB CBSO consult IDELUX Développement 0205797475",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0205797475",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2107; deposit portal; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_idelux_dev_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_idelux_dev_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2107; omzet DROP 19151123 (-29.80%) vs YE2024 27281519",
    },
    {
        "budget_id": "bud_idelux_dev_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_idelux_dev_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2107; pnl FLIP LOSS -898763 vs YE2024 PROFIT 3205547",
    },
    {
        "budget_id": "bud_idelux_dev_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_idelux_dev_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2107; equity JUMP 102328170 (+1.15%) vs YE2024 101166215",
    },
    {
        "budget_id": "bud_idelux_dev_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_idelux_dev_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2107; bruto DROP 10797628 (-20.50%) vs YE2024 13582098",
    },
    {
        "budget_id": "bud_idelux_dev_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_idelux_dev_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2107; FTE DROP 91.1 vs YE2024 118.1",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "IDELUX Développement",
            "name_fr": "IDELUX Développement (Association intercommunale)",
            "name_en": "IDELUX Développement (Luxembourg province economic development IGS)",
            "level": "other",
            "parent_id": "wallonie_gov",
            "community_language": "fr",
            "website": "https://www.idelux.be",
            "foi_email": "officiel.ic-ideluxdeveloppement@idelux.be",
            "foi_postal": "Schoppach, drève de l'Arc-en-Ciel 98, 6700 Arlon",
            "notes": (
                "tick2107 YE2025 Medium CW NL+EN+FR + Strong KBO 0205.797.475 Actief SC "
                "1 VE pouvoir adjudicateur; omzet DROP 19.15m bruto DROP 10.80m pnl FLIP LOSS "
                "-0.90m equity JUMP 102.33m FTE DROP 91.1; NACE 84.130+; "
                f"FOI {GAP}; DISTINCT Projets Publics/Eau/Finances/Environnement; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
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
            "title": "IDELUX Développement YE2025 leftover dual (omzet DROP 19.15m / pnl FLIP LOSS)",
            "entity_id": ENTITY,
            "beneficiary": "Luxembourg province communes (economic development / zoning / engineering)",
            "legal_basis": "SC intercommunale / aanbestedende overheid (KBO 0205.797.475)",
            "decision_date": "2026-06-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0205797475/association-intercommunale-pour-le-developpement-economique-durable-de-la-province-de-luxembourg",
            "stated_goal": "Sustainable economic development of Luxembourg province",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map related-party IDELUX group; "
                "explain pnl FLIP LOSS and omzet DROP -29.80pct with FTE DROP"
            ),
            "source_id": "src_idelux_dev_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Developpement>JR2025_statutory_L5",
            "notes": (
                "tick2107; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
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
            "name": "IDELUX Développement omzet DROP 19.15m / pnl FLIP LOSS / FTE DROP (YE2025)",
            "level": "L5",
            "type": "igs_economic_development_statutory",
            "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Developpement>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary economic-development IGS envelope; pnl FLIP LOSS; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_idelux_dev_jr2025_cw_en",
            "beneficiaries": "Luxembourg province communes / firms (IDELUX Développement)",
            "stated_goal": "Economic development and zoning support",
            "measured_outcome": (
                "omzet DROP -29.80%; bruto DROP -20.50%; pnl FLIP LOSS; "
                "equity JUMP +1.15%; FTE DROP 91.1 from 118.1"
            ),
            "absurdity_score": "6.0",
            "cost_score": "5.5",
            "difficulty": "3.5",
            "priority_index": "5.8",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; disclose IDELUX group related-party; "
                "explain revenue/FTE collapse with pnl flip to loss"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2107; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "do not redo Projets Publics/Eau/Finances/Environnement/INTRADEL"
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
            "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Developpement>NBB_PDF_assets_debt_pnl_flip",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); activity split "
                "development/engineering/real-estate; related-party IDELUX sisters; "
                "explanation of pnl FLIP LOSS and omzet/FTE DROP"
            ),
            "why_it_matters": (
                "Medium CW shows 19.15m omzet Luxembourg economic-development IGS flipping "
                "to LOSS with -29.8pct omzet and -23pct FTE without balanstotaal/assets/debt; "
                "material L5 residual after Projets Publics"
            ),
            "priority": "8",
            "recipient_body": "IDELUX Développement SC",
            "recipient_email": "officiel.ic-ideluxdeveloppement@idelux.be",
            "recipient_postal": "Schoppach, drève de l'Arc-en-Ciel 98, 6700 Arlon",
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
            "notes": "tick2107; human-send only; Medium CW; next every-10 2110",
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
    if row["task_id"] == "rq_2107":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — IDELUX Développement YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover IDELUX Développement YE2025 Medium CW; KBO 0205.797.475; "
            f"omzet DROP {OMZET} bruto DROP {BRUTO} pnl FLIP LOSS {PNL} equity JUMP {EQUITY} "
            f"FTE DROP {FTE}; FOI {GAP}; 1 VE; DISTINCT Projets Publics/Eau/Finances; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
        )
        row["notes"] = (
            "tick2107 IDELUX Développement Medium omzet DROP 19.15m bruto DROP 10.80m pnl FLIP "
            "LOSS -0.90m equity JUMP 102.33m FTE DROP 91.1; FOI ready; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2108; next every-10 2110"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2108" for r in rows):
    rows.append(
        {
            "task_id": "rq_2108",
            "title": "leftover dual hole-fill after IDELUX Développement — prefer AGB/FARO-YE2025/AIESH-REW/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2108 after IDELUX Développement YE2025 Medium. Prefer leftover AGB/APB if "
                "JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
                "unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. Do NOT redo IDELUX "
                "Développement, IDELUX Projets Publics, IDELUX Eau, IDELUX Finances, IDELUX "
                "Environnement, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, HYGEA, "
                "BEP Environnement, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, "
                "Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Belgoprocess, "
                "Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2107 IDELUX Développement; next every-10 2110",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2107 not found"

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
            "rq_2107",
            "2107",
            "no",
            (
                "tick2107 leftover IDELUX Développement 0205.797.475 Medium CW "
                "(omzet DROP 19.15m bruto DROP 10.80m pnl FLIP LOSS -0.90m equity JUMP 102.33m "
                "FTE DROP 91.1; assets/debt Unknown; 1 VE); AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_2108; next every-10 2110; continuous hole_fill"
            ),
        ]
    )

if "## Tick 2107 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2107 already present")
else:
    log_block = f"""

## Tick 2107 - {UTC} - rq_2107 IDELUX Développement (omzet DROP 19.15m / pnl FLIP LOSS / Medium)

- Unit: **rq_2107** leftover dual after **rq_2106 IDELUX Projets Publics**. Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. Took preferred unused IGS sister **IDELUX Développement** YE2025 (KBO **0205.797.475**; Schoppach Arc-en-Ciel 98 Arlon; SC / **1 VE** / pouvoir adjudicateur; NACE **84.130**+). DISTINCT from Projets Publics / Eau / Finances / Environnement.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** DROP −29.80%; bruto **EUR{BRUTO}** DROP −20.50%; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT 3205547; equity **EUR{EQUITY}** JUMP +1.15%; FTE **{FTE}** DROP vs YE2024 118.1; neerlegging **19.06.2026**. Assets/debt Unknown. Medium. Strong KBO (officiel.ic-ideluxdeveloppement@idelux.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.8); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2107=done + rq_2108 open; loop_state ticks=2107; raw docs/doge/data/raw/tick2107/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 2110**). Next: rq_2108 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2107 write OK; found=", found)

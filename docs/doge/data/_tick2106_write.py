# tick 2106 — IDELUX Projets Publics YE2025 Medium CW leftover dual
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T06:55:00Z"
DATE = "2026-08-25"
ENTITY = "igs_idelux_projets_publics"
GAP = "gap_idelux_projets_publics_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
COMM = "comm_idelux_projets_publics_jr2025_statutory_igs"
LB = "lb_idelux_pp_omzet_jump_6_49m_pnl_jump_0_54m_bruto_jump_jr2025"

OMZET = 6490215
PNL = 543627
EQUITY = 44152960
BRUTO = 1104487
FTE = 12.5


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
        "source_id": "src_idelux_pp_jr2025_cw_nl",
        "title": "IDELUX Projets Publics Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0832382635/association-intercommunale-idelux-projets-publics",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2106; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 19.06.2026; Medium",
    },
    {
        "source_id": "src_idelux_pp_jr2025_cw_en",
        "title": "IDELUX Projets Publics Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0832382635/association-intercommunale-idelux-projets-publics",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2106; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_idelux_pp_jr2025_cw_fr",
        "title": "IDELUX Projets Publics Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0832382635/association-intercommunale-idelux-projets-publics",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2106; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_idelux_pp_kbo_2106",
        "title": "KBO IDELUX Projets Publics 0832.382.635",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=832382635",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2106; Actief SC; 2 VE; NACE 68.122/82.990; pouvoir adjudicateur; Strong identity",
    },
    {
        "source_id": "src_idelux_pp_nbb_consult_2106",
        "title": "NBB CBSO consult IDELUX Projets Publics 0832382635",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0832382635",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2106; deposit portal; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_idelux_pp_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_idelux_pp_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2106; omzet JUMP 6490215 (+4.34%) vs YE2024 6220488",
    },
    {
        "budget_id": "bud_idelux_pp_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_idelux_pp_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2106; pnl JUMP 543627 (+647.75%) vs YE2024 72701",
    },
    {
        "budget_id": "bud_idelux_pp_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_idelux_pp_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2106; equity JUMP 44152960 (+0.17%) vs YE2024 44078773",
    },
    {
        "budget_id": "bud_idelux_pp_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_idelux_pp_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2106; bruto JUMP 1104487 (+61.25%) vs YE2024 684954",
    },
    {
        "budget_id": "bud_idelux_pp_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_idelux_pp_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2106; FTE DROP 12.5 vs YE2024 12.6",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "IDELUX Projets Publics",
            "name_fr": "IDELUX Projets publics (Association intercommunale)",
            "name_en": "IDELUX Public Projects intercommunale (Luxembourg province)",
            "level": "other",
            "parent_id": "wallonie_gov",
            "community_language": "fr",
            "website": "https://www.idelux.be",
            "foi_email": "officiel.ic-ideluxprojetspublics@idelux.be",
            "foi_postal": "Schoppach, drève de l'Arc-en-Ciel 98, 6700 Arlon",
            "notes": (
                "tick2106 YE2025 Medium CW NL+EN+FR + Strong KBO 0832.382.635 Actief SC "
                "2 VE pouvoir adjudicateur; omzet JUMP 6.49m bruto JUMP 1.10m pnl JUMP 0.54m "
                "equity JUMP 44.15m FTE DROP 12.5; NACE 68.122/82.990; "
                f"FOI {GAP}; DISTINCT IDELUX Eau (tick588)/Finances/Environnement; "
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
            "title": "IDELUX Projets Publics YE2025 leftover dual (omzet JUMP 6.49m / pnl JUMP 0.54m)",
            "entity_id": ENTITY,
            "beneficiary": "Luxembourg province communes (non-residential public project development)",
            "legal_basis": "SC intercommunale / aanbestedende overheid (KBO 0832.382.635)",
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
            "evaluation_url": "https://www.companyweb.be/en/0832382635/association-intercommunale-idelux-projets-publics",
            "stated_goal": "Develop non-residential public projects for Luxembourg province communes",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map related-party IDELUX group; "
                "explain pnl JUMP +647.75pct and bruto JUMP +61.25pct"
            ),
            "source_id": "src_idelux_pp_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Projets_Publics>JR2025_statutory_L5",
            "notes": (
                "tick2106; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; IDELUX Eau already mined; not TE-additive of 348bn"
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
            "name": "IDELUX Projets Publics omzet JUMP 6.49m / pnl JUMP +647pct (YE2025)",
            "level": "L5",
            "type": "igs_project_development_statutory",
            "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Projets_Publics>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary public-projects IGS envelope; pnl JUMP outlier; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_idelux_pp_jr2025_cw_en",
            "beneficiaries": "Luxembourg province communes (IDELUX group)",
            "stated_goal": "Non-residential public project development",
            "measured_outcome": (
                "omzet JUMP +4.34%; bruto JUMP +61.25%; pnl JUMP +647.75%; "
                "equity JUMP +0.17%; FTE DROP 12.5"
            ),
            "absurdity_score": "5.5",
            "cost_score": "3.5",
            "difficulty": "3.5",
            "priority_index": "4.7",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; disclose IDELUX group related-party; "
                "explain pnl/bruto JUMP vs modest omzet growth"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2106; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "do not redo IDELUX Eau/Finances/Environnement/INTRADEL"
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
            "hierarchy_path": "Wallonie>Luxembourg>IDELUX>Projets_Publics>NBB_PDF_assets_debt_pnl",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); project vs services "
                "omzet split; related-party IDELUX Eau/Finances/Environnement/Développement; "
                "explanation of pnl JUMP +647.75% and bruto JUMP +61.25%"
            ),
            "why_it_matters": (
                "Medium CW shows 6.49m omzet Luxembourg public-projects IGS with outlier pnl "
                "JUMP without balanstotaal/assets/debt; material L5 residual after INTRADEL"
            ),
            "priority": "8",
            "recipient_body": "IDELUX Projets Publics SC",
            "recipient_email": "officiel.ic-ideluxprojetspublics@idelux.be",
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
            "notes": "tick2106; human-send only; Medium CW; next every-10 2110",
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
    if row["task_id"] == "rq_2106":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — IDELUX Projets Publics YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover IDELUX Projets Publics YE2025 Medium CW; KBO 0832.382.635; "
            f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} "
            f"FTE DROP {FTE}; FOI {GAP}; 2 VE; IDELUX Eau already mined tick588; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
        )
        row["notes"] = (
            "tick2106 IDELUX Projets Publics Medium omzet JUMP 6.49m bruto JUMP 1.10m pnl JUMP "
            "0.54m equity JUMP 44.15m FTE DROP 12.5; FOI ready; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2107; next every-10 2110"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2107" for r in rows):
    rows.append(
        {
            "task_id": "rq_2107",
            "title": "leftover dual hole-fill after IDELUX Projets Publics — prefer AGB/FARO-YE2025/AIESH-REW/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2107 after IDELUX Projets Publics YE2025 Medium. Prefer leftover AGB/APB if "
                "JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
                "IDELUX Développement if YE2025 unused, else unused water/DSO/IGS/HVZ/energy/"
                "hospital/WZC/psych. Do NOT redo IDELUX Projets Publics, IDELUX Eau, IDELUX Finances, "
                "IDELUX Environnement, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, "
                "HYGEA, BEP Environnement, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, "
                "Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, "
                "Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2106 IDELUX Projets Publics; next every-10 2110",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2106 not found"

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
            "rq_2106",
            "2106",
            "no",
            (
                "tick2106 leftover IDELUX Projets Publics 0832.382.635 Medium CW "
                "(omzet JUMP 6.49m bruto JUMP 1.10m pnl JUMP 0.54m equity JUMP 44.15m "
                "FTE DROP 12.5; assets/debt Unknown; 2 VE); AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_2107; next every-10 2110; continuous hole_fill"
            ),
        ]
    )

if "## Tick 2106 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2106 already present")
else:
    log_block = f"""

## Tick 2106 - {UTC} - rq_2106 IDELUX Projets Publics (omzet JUMP 6.49m / pnl JUMP 0.54m / Medium)

- Unit: **rq_2106** leftover dual after **rq_2105 INTRADEL**. Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. IDELUX Eau already mined (tick588). Took unused IGS sister **IDELUX Projets Publics** YE2025 (KBO **0832.382.635**; Schoppach Arc-en-Ciel 98 Arlon; SC / **2 VE** / pouvoir adjudicateur; NACE **68.122/82.990**). DISTINCT from IDELUX Eau/Finances/Environnement.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +4.34%; bruto **EUR{BRUTO}** JUMP +61.25%; pnl **EUR{PNL}** JUMP +647.75%; equity **EUR{EQUITY}** JUMP +0.17%; FTE **{FTE}** DROP vs YE2024 12.6; neerlegging **19.06.2026**. Assets/debt Unknown. Medium. Strong KBO (officiel.ic-ideluxprojetspublics@idelux.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 4.7); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2106=done + rq_2107 open; loop_state ticks=2106; raw docs/doge/data/raw/tick2106/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 2110**). Next: rq_2107 (AGB/FARO-if-YE2025 / AIESH-REW / IDELUX Développement / unused).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2106 write OK; found=", found)

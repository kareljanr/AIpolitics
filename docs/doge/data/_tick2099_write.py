# tick 2099 — SLG Operaties Vlaanderen YE2025 Medium CW leftover dual
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T05:40:00Z"
DATE = "2026-08-25"
ENTITY = "nv_slg_operaties_vlaanderen"
GAP = "gap_slg_operaties_vl_nbb_pdf_assets_debt_merger_jump_matrix_l5"
COMM = "comm_slg_operaties_vl_jr2025_statutory_merger_jump"
LB = "lb_slg_operaties_vl_omzet_jump_58_28m_fte_1095_merger_jr2025"

OMZET = 58284887
PNL = 347702
EQUITY = 19875741
BRUTO = 36784094
FTE = 1095.3


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
        "source_id": "src_slg_op_vl_jr2025_cw_nl",
        "title": "SLG Operaties Vlaanderen Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0845064196/slg-operaties-vlaanderen",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2099; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 28.07.2026; Medium",
    },
    {
        "source_id": "src_slg_op_vl_jr2025_cw_en",
        "title": "SLG Operaties Vlaanderen Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0845064196/slg-operaties-vlaanderen",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2099; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_slg_op_vl_jr2025_cw_fr",
        "title": "SLG Operaties Vlaanderen Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0845064196/slg-operaties-vlaanderen",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2099; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_slg_op_vl_kbo_2099",
        "title": "KBO SLG Operaties Vlaanderen 0845.064.196",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=845064196",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": (
            "tick2099; Actief NV; 9 VE; NACE 87.301/87.101; kapitaal 2673565.99; "
            "7 absorptions Jul 2025; Strong identity"
        ),
    },
    {
        "source_id": "src_slg_op_vl_nbb_consult_2099",
        "title": "NBB CBSO consult SLG Operaties Vlaanderen 0845064196",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0845064196",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2099; deposit portal; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_slg_op_vl_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_slg_op_vl_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2099; omzet JUMP 58284887 (+424.09%) vs YE2024 11121236; merger-driven",
    },
    {
        "budget_id": "bud_slg_op_vl_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_slg_op_vl_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2099; pnl JUMP 347702 (+32.61%) vs YE2024 262190",
    },
    {
        "budget_id": "bud_slg_op_vl_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_slg_op_vl_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2099; equity JUMP 19875741 (+200.99%) vs YE2024 6603371",
    },
    {
        "budget_id": "bud_slg_op_vl_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_slg_op_vl_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2099; bruto JUMP 36784094 (+440.36%) vs YE2024 6807365",
    },
    {
        "budget_id": "bud_slg_op_vl_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_slg_op_vl_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2099; FTE JUMP 1095.3 vs YE2024 101.7; merger-driven",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "SLG Operaties Vlaanderen NV",
            "name_fr": "SLG Operaties Vlaanderen SA",
            "name_en": "SLG Operaties Vlaanderen NV (Armonea/Colisee Flanders ops)",
            "level": "other",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.armonea.be",
            "foi_email": "info@armonea.be",
            "foi_postal": "Satenrozen 1B, 2550 Kontich",
            "notes": (
                "tick2099 YE2025 Medium CW NL+EN+FR + Strong KBO 0845.064.196 Actief NV "
                "9 VE; NACE 87.301/87.101; kapitaal 2.67m; omzet JUMP 58.28m bruto JUMP 36.78m "
                "pnl JUMP 0.35m equity JUMP 19.88m FTE JUMP 1095.3; 7 WZC absorptions Jul 2025 "
                "(Heydeveld/Prinsenpark/Edelweis/Sporenpark/Maretak/Elckerlyc/Boneput); "
                "DISTINCT Armonea/Colisee/emeis/Always Home; FOI "
                "gap_slg_operaties_vl_nbb_pdf_assets_debt_merger_jump_matrix_l5; "
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
            "title": "SLG Operaties VL YE2025 leftover dual (omzet JUMP 58.28m / FTE JUMP 1095 merger)",
            "entity_id": ENTITY,
            "beneficiary": "Flanders ROB/RVT residents via Armonea-Colisee SLG ops (9 VE after Jul 2025 mergers)",
            "legal_basis": "NV ROB/RVT / publiek gesubsidieerde ouderenzorg (KBO 0845.064.196)",
            "decision_date": "2026-07-28",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0845064196/slg-operaties-vlaanderen",
            "stated_goal": "Operate Flanders nursing homes after 2025 absorption wave",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map Zorgkas vs omzet; disclose per-absorbed "
                "entity contribution to +424pct omzet / +1095 FTE JUMP"
            ),
            "source_id": "src_slg_op_vl_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Zorg>SLG_Operaties_Vlaanderen>JR2025_statutory_L5",
            "notes": (
                "tick2099; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
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
            "name": "SLG Operaties VL omzet JUMP 58.28m / FTE 1095 merger shell (YE2025)",
            "level": "L5",
            "type": "wzc_ops_statutory_merger",
            "hierarchy_path": "Vlaanderen>Zorg>SLG_Operaties_Vlaanderen>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary after Jul 2025 multi-WZC absorption; bruto 36.78m; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_slg_op_vl_jr2025_cw_en",
            "beneficiaries": "SLG/Armonea Flanders ROB-RVT residents (9 VE)",
            "stated_goal": "Consolidate Flanders nursing-home operations",
            "measured_outcome": (
                "omzet JUMP +424.09%; bruto JUMP +440.36%; pnl JUMP +32.61%; "
                "equity JUMP +200.99%; FTE JUMP 1095.3 from 101.7"
            ),
            "absurdity_score": "6.5",
            "cost_score": "7.0",
            "difficulty": "4.0",
            "priority_index": "7.0",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; map Zorgkas/public subsidy vs omzet; "
                "disclose merger contribution matrix for 7 absorbed WZCs"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2099; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "DISTINCT Armonea/Colisee/emeis; do not redo Familiezorg Gent/AREWAL"
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
            "hierarchy_path": "Vlaanderen>Zorg>SLG_Operaties_Vlaanderen>NBB_PDF_assets_debt_merger",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); Zorgkas/public "
                "subsidy vs omzet split; per-absorbed WZC contribution to omzet/FTE/equity "
                "JUMP; list of 9 VE campuses"
            ),
            "why_it_matters": (
                "Medium CW shows 58.28m omzet / 1095 FTE Armonea-Colisee Flanders ops NV "
                "after Jul 2025 absorption wave without balanstotaal/assets/debt; material "
                "L5 residual distinct from Armonea holding LOSS path"
            ),
            "priority": "8",
            "recipient_body": "SLG Operaties Vlaanderen NV (via Armonea)",
            "recipient_email": "info@armonea.be",
            "recipient_postal": "Satenrozen 1B, 2550 Kontich",
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
            "notes": "tick2099; human-send only; Medium CW; next every-10 2100",
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
    if row["task_id"] == "rq_2099":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — SLG Operaties Vlaanderen YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover SLG Operaties Vlaanderen YE2025 Medium CW; KBO 0845.064.196; "
            f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} "
            f"FTE JUMP {FTE}; FOI {GAP}; 7 WZC absorptions Jul 2025; 9 VE; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Armonea/Colisee/emeis"
        )
        row["notes"] = (
            "tick2099 SLG Operaties VL Medium omzet JUMP 58.28m bruto JUMP 36.78m pnl JUMP "
            "0.35m equity JUMP 19.88m FTE JUMP 1095.3; FOI ready; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2100 EVERY-10; next every-10 2100"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2100" for r in rows):
    rows.append(
        {
            "task_id": "rq_2100",
            "title": "EVERY-10 + leftover dual hole-fill after SLG Operaties — prefer AGB/FARO-YE2025/AIESH-REW/unused",
            "sprint": "hole_fill",
            "priority": "9",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2100 after SLG Operaties Vlaanderen YE2025 Medium. MUST refresh "
                "progress_every_10_ticks.md + doge_waste_top10_current.md then hole-fill one "
                "unit. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                "Do NOT redo SLG Operaties Vlaanderen, AREWAL, Familiezorg Gent, emeis Belgium, "
                "Begralim, Sint-Lucia, Lidwina, SED, Zilvervogel, Familiezorg WV, De Lovie, Ocura, "
                "Armonea, Colisee Belgium, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, "
                "Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, "
                "Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2099 SLG Operaties; EVERY-10 mandatory at 2100",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2099 not found"

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
            "rq_2099",
            "2099",
            "no",
            (
                "tick2099 leftover SLG Operaties Vlaanderen 0845.064.196 Medium CW "
                "(omzet JUMP 58.28m bruto JUMP 36.78m pnl JUMP 0.35m equity JUMP 19.88m "
                "FTE JUMP 1095.3; 7 absorptions Jul 2025; 9 VE; assets/debt Unknown); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2100 EVERY-10; continuous hole_fill"
            ),
        ]
    )

if "## Tick 2099 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2099 already present")
else:
    log_block = f"""

## Tick 2099 - {UTC} - rq_2099 SLG Operaties Vlaanderen (omzet JUMP 58.28m / FTE JUMP 1095 / Medium)

- Unit: **rq_2099** leftover dual after **rq_2098 AREWAL**. Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. Took deferred unused WZC ops **SLG Operaties Vlaanderen** YE2025 (KBO **0845.064.196**; Satenrozen 1B Kontich; NV ROB/RVT; **9 VE**; NACE **87.301/87.101**). KBO documents **7 absorptions** Jul 2025 (Heydeveld/Prinsenpark/Edelweis/Sporenpark/Maretak/Elckerlyc/Boneput) explaining scale JUMP. DISTINCT from Armonea NV / Colisée / emeis / Always Home.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +424.09%; bruto **EUR{BRUTO}** JUMP +440.36%; pnl **EUR{PNL}** JUMP +32.61%; equity **EUR{EQUITY}** JUMP +200.99%; FTE **{FTE}** JUMP vs YE2024 101.7; neerlegging **28.07.2026**. Assets/debt Unknown. Medium. Strong KBO Actief NV kapitaal 2.67m. FOI via info@armonea.be. Omzet primary envelope.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 7.0); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2099=done + rq_2100 open; loop_state ticks=2099; raw docs/doge/data/raw/tick2099/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 2100** — MUST refresh progress + waste top10 then hole-fill). Next: rq_2100.
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2099 write OK; found=", found)

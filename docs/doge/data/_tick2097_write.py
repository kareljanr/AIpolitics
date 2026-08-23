# tick 2097 — AREWAL YE2025 Medium CW leftover dual (unused DSO shared-services)
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T05:20:00Z"
DATE = "2026-08-25"
ENTITY = "sc_arewal"
GAP = "gap_arewal_nbb_pdf_assets_debt_bruto_jump_equity_thin_matrix_l5"
COMM = "comm_arewal_jr2025_statutory_dso_shared_services"
LB = "lb_arewal_omzet_5_63m_bruto_jump_equity_thin_jr2025"

OMZET = 5631689
PNL = 1000
EQUITY = 31800
BRUTO = 920377
FTE = 7.7


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
        "source_id": "src_arewal_jr2025_cw_nl",
        "title": "AREWAL Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0627818345/arewal",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2097; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 02.07.2026; Medium",
    },
    {
        "source_id": "src_arewal_jr2025_cw_en",
        "title": "AREWAL Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0627818345/arewal",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2097; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_arewal_jr2025_cw_fr",
        "title": "AREWAL Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0627818345/arewal",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2097; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_arewal_kbo_2097",
        "title": "KBO AREWAL 0627.818.345",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=627818345",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2097; Actief SCRL; 1 VE; NACE 70.200; pouvoir adjudicateur; Strong identity",
    },
    {
        "source_id": "src_arewal_nbb_consult_2097",
        "title": "NBB CBSO consult AREWAL 0627818345",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0627818345",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2097; deposit portal index; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_arewal_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_arewal_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2097; omzet DROP 5631689 (-6.00%) vs YE2024 5990896",
    },
    {
        "budget_id": "bud_arewal_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_arewal_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2097; pnl FLAT 1000 (0%) vs YE2024 1000; structural pass-through",
    },
    {
        "budget_id": "bud_arewal_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_arewal_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2097; equity JUMP 31800 (+3.25%) vs YE2024 30800; thin vs omzet",
    },
    {
        "budget_id": "bud_arewal_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_arewal_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2097; bruto JUMP 920377 (+39.86%) vs YE2024 658058; with omzet DROP",
    },
    {
        "budget_id": "bud_arewal_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_arewal_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2097; FTE JUMP 7.7 vs YE2024 5.2",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "AREWAL (gedeelde diensten AIEG/AIESH/REW)",
            "name_fr": "AREWAL (services partages AIEG/AIESH/REW)",
            "name_en": "AREWAL (shared services AIEG/AIESH/REW)",
            "level": "other",
            "parent_id": "wallonie_gov",
            "community_language": "fr",
            "website": "https://www.aieg.be/",
            "foi_email": "officiel.ic-aieg@aieg.be",
            "foi_postal": "Rue des Marais 11, 5300 Andenne",
            "notes": (
                "tick2097 YE2025 Medium CW NL+EN+FR + Strong KBO 0627.818.345 Actief SCRL "
                "1 VE pouvoir adjudicateur; omzet DROP 5.63m bruto JUMP 0.92m pnl FLAT 1k "
                "equity THIN 31.8k FTE JUMP 7.7; NACE 70.200; shared seat with AIEG; "
                "FOI gap_arewal_nbb_pdf_assets_debt_bruto_jump_equity_thin_matrix_l5; "
                "AIESH/REW still YE2024; do not redo AIEG/RESA/Enodia/Fluxys/ETB/Elia/BNO/"
                "Synergrid/Atrias/Synatom/IPFBW/IGRETEC"
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
            "title": "AREWAL YE2025 leftover dual (omzet DROP 5.63m / bruto JUMP / equity thin)",
            "entity_id": ENTITY,
            "beneficiary": "Walloon micro-DSOs AIEG/AIESH/REW shared services + public lighting support",
            "legal_basis": "SCRL / aanbestedende overheid / GRD shared vehicle (KBO 0627.818.345)",
            "decision_date": "2026-07-02",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0627818345/arewal",
            "stated_goal": "Mutualise GRD support and public-lighting OSP for AIEG/AIESH/REW",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map related-party split AIEG/AIESH/REW; "
                "explain bruto JUMP +39.86pct with omzet DROP and flat 1k pnl; equity thin"
            ),
            "source_id": "src_arewal_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Wallonie>GRD>AREWAL>JR2025_statutory_L5",
            "notes": (
                "tick2097; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive of 348bn; omzet primary envelope"
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
            "name": "AREWAL omzet 5.63m / bruto JUMP + equity thin 31.8k (YE2025)",
            "level": "L5",
            "type": "dso_shared_services_statutory",
            "hierarchy_path": "Wallonie>GRD>AREWAL>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary GRD shared-services envelope; bruto JUMP +39.86pct; "
                "equity thin 31.8k; assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_arewal_jr2025_cw_en",
            "beneficiaries": "AIEG / AIESH / REW + communes on those GRDs",
            "stated_goal": "Shared GRD support and public-lighting OSP",
            "measured_outcome": (
                "omzet DROP -6.00%; bruto JUMP +39.86%; pnl FLAT 1000; "
                "equity JUMP +3.25% but thin; FTE JUMP 7.7"
            ),
            "absurdity_score": "5.5",
            "cost_score": "4.5",
            "difficulty": "3.5",
            "priority_index": "5.5",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; disclose AIEG/AIESH/REW related-party "
                "matrix; explain bruto JUMP with flat 1k pnl and equity thin vs 5.63m omzet"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2097; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "do not redo AIEG/RESA/Enodia/Fluxys/ETB/Elia"
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
            "hierarchy_path": "Wallonie>GRD>AREWAL>NBB_PDF_assets_debt_bruto_equity",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); related-party "
                "omzet split AIEG/AIESH/REW; explanation of bruto JUMP +39.86% with omzet "
                "DROP -6% and flat pnl 1000; equity thin 31800 vs omzet; shareholder register"
            ),
            "why_it_matters": (
                "Medium CW shows 5.63m omzet aanbestedende GRD shared-services shell with "
                "structural flat 1k pnl and equity thin without balanstotaal/assets/debt; "
                "material L5 residual linking stalled AIESH/REW YE2024 parents"
            ),
            "priority": "8",
            "recipient_body": "AREWAL SCRL (via AIEG seat)",
            "recipient_email": "officiel.ic-aieg@aieg.be",
            "recipient_postal": "Rue des Marais 11, 5300 Andenne",
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
            "notes": "tick2097; human-send only; Medium CW; next every-10 2100",
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
    if row["task_id"] == "rq_2097":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — AREWAL YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["instructions"] = (
            "Completed leftover AREWAL YE2025 Medium CW; KBO 0627.818.345; "
            f"omzet DROP {OMZET} bruto JUMP {BRUTO} pnl FLAT {PNL} equity THIN {EQUITY} "
            f"FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "NACE 70.200 1 VE; shared seat AIEG; DISTINCT from AIEG parent"
        )
        row["notes"] = (
            "tick2097 AREWAL Medium omzet DROP 5.63m bruto JUMP 0.92m pnl FLAT 1k "
            "equity THIN 31.8k FTE JUMP 7.7; FOI ready; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2098; next every-10 2100"
        )
        row["blocked_gap_id"] = GAP
        row["hierarchy_target"] = "L5"

if not any(r.get("task_id") == "rq_2098" for r in rows):
    rows.append(
        {
            "task_id": "rq_2098",
            "title": "leftover dual hole-fill after AREWAL — prefer AGB/FARO-YE2025/AIESH-REW/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2098 after AREWAL YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF "
                "live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                "water/DSO/IGS/HVZ/energy/hospital/WZC/psych. SLG Operaties Vlaanderen "
                "0845.064.196 YE2025 live (distinct Armonea/Always Home path) unused deferred. "
                "Do NOT redo AREWAL, emeis Belgium, Begralim, Sint-Lucia, Lidwina, SED "
                "Zoutleeuw, Zilvervogel, Familiezorg WV, De Lovie, Ocura, Lindelo, Medemens, "
                "Augustinus Halle, Ben, Stuyvenberg, Wijshage, Mater Dei, Den Akker, AIEG, "
                "RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, "
                "IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Belgoprocess, Laborelec, "
                "NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2097 AREWAL; next every-10 2100; prefer FARO/AIESH/REW if YE2025",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2097 not found"

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
            "rq_2097",
            "2097",
            "no",
            (
                "tick2097 leftover AREWAL 0627.818.345 Medium CW (omzet DROP 5.63m bruto JUMP "
                "0.92m pnl FLAT 1k equity THIN 31.8k FTE JUMP 7.7; assets/debt Unknown; "
                "NACE 70.200 1 VE); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2098; "
                "next every-10 2100; continuous hole_fill"
            ),
        ]
    )

log_marker = "## Tick 2097 -"
if log_marker in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2097 already present")
else:
    log_block = f"""

## Tick 2097 - {UTC} - rq_2097 AREWAL (omzet DROP 5.63m / bruto JUMP 0.92m / equity THIN / Medium)

- Unit: **rq_2097** leftover dual after **rq_2096 emeis Belgium**. Prefer: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused DSO shared-services **AREWAL** YE2025 live (KBO **0627.818.345**; Rue des Marais 11 Andenne shared with AIEG; SCRL / **pouvoir adjudicateur**; NACE **70.200**; **1 VE**). Parent AIEG already mined rq_1944. Do not redo emeis/Begralim/Sint-Lucia/Lidwina/SED/Zilvervogel/Familiezorg/De Lovie/Ocura/Lindelo/Medemens/AIEG/RESA/Enodia/Fluxys/ETB/Elia/BNO/Synergrid/Atrias/Synatom/IPFBW/nuclear-water list.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** DROP −6.00%; bruto **EUR{BRUTO}** JUMP +39.86%; pnl **FLAT EUR{PNL}**; equity **EUR{EQUITY}** JUMP +3.25% but thin vs omzet; FTE **{FTE}** JUMP vs YE2024 5.2; neerlegging **02.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief SCRL 1 VE adjudicateur; FOI via officiel.ic-aieg@aieg.be. Omzet primary envelope (shared-services SC).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.5); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2097=done + rq_2098 open; loop_state ticks=2097; raw under docs/doge/data/raw/tick2097/.
- FOI: **ready not sent** (human-gated; officiel.ic-aieg@aieg.be).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2098 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC; SLG Operaties deferred).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2097 write OK; found=", found)

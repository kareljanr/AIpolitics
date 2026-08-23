# tick 2108 — WZC Sint-Camillus Wevelgem YE2025 Medium CW leftover dual
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T07:25:00Z"
DATE = "2026-08-25"
ENTITY = "vzw_wzc_sint_camillus_wevelgem"
GAP = "gap_wzc_sint_camillus_wevelgem_nbb_pdf_assets_debt_pnl_jump_fte_drop_matrix_l5"
COMM = "comm_wzc_sint_camillus_wevelgem_jr2025_statutory"
LB = "lb_camillus_wevelgem_omzet_jump_8_42m_pnl_jump_fte_drop_jr2025"

OMZET = 8423064
PNL = 157847
EQUITY = 4941991
BRUTO = 8383864
FTE = 115.8


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
        "source_id": "src_camillus_wevelgem_jr2025_cw_nl",
        "title": "WZC Sint-Camillus Wevelgem Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0417958152",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2108; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 01.07.2026; Medium",
    },
    {
        "source_id": "src_camillus_wevelgem_jr2025_cw_en",
        "title": "WZC Sint-Camillus Wevelgem Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0417958152",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2108; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_camillus_wevelgem_jr2025_cw_fr",
        "title": "WZC Sint-Camillus Wevelgem Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0417958152",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2108; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_camillus_wevelgem_kbo_2108",
        "title": "KBO WZC Sint-Camillus 0417.958.152",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=417958152",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2108; Actief VZW; 1 VE; NACE 87.101 RVT; Strong identity; no KBO email",
    },
    {
        "source_id": "src_camillus_wevelgem_site_2108",
        "title": "WZC Sint-Camillus Wevelgem website contact",
        "url": "https://wzcsintcamillus.be/",
        "publisher": "WZC Sint-Camillus",
        "accessed_date": DATE,
        "source_class": "entity_site",
        "notes": "tick2108; info@wzcsintcamillus.be; 056 41 15 70; Kloosterstraat 21 Wevelgem",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_camillus_wevelgem_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_camillus_wevelgem_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2108; omzet JUMP 8423064 (+4.07%) vs YE2024 8093879",
    },
    {
        "budget_id": "bud_camillus_wevelgem_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_camillus_wevelgem_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2108; pnl JUMP 157847 (+208.10%) vs YE2024 51233",
    },
    {
        "budget_id": "bud_camillus_wevelgem_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_camillus_wevelgem_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2108; equity JUMP 4941991 (+1.92%) vs YE2024 4849002",
    },
    {
        "budget_id": "bud_camillus_wevelgem_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_camillus_wevelgem_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2108; bruto JUMP 8383864 (+0.86%) vs YE2024 8312070; near omzet",
    },
    {
        "budget_id": "bud_camillus_wevelgem_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_camillus_wevelgem_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2108; FTE DROP 115.8 vs YE2024 123.8",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "WZC Sint-Camillus (Wevelgem)",
            "name_fr": "MR/MRS Sint-Camillus (Wevelgem)",
            "name_en": "WZC Sint-Camillus nursing home (Wevelgem)",
            "level": "other",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://wzcsintcamillus.be/",
            "foi_email": "info@wzcsintcamillus.be",
            "foi_postal": "Kloosterstraat 21, 8560 Wevelgem",
            "notes": (
                "tick2108 YE2025 Medium CW NL+EN+FR + Strong KBO 0417.958.152 Actief VZW "
                "1 VE; NACE 87.101 RVT; omzet JUMP 8.42m bruto JUMP 8.38m pnl JUMP 0.16m "
                "equity JUMP 4.94m FTE DROP 115.8; FOI "
                f"{GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "Zilverlinde Olen deferred"
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
            "title": "WZC Sint-Camillus Wevelgem YE2025 leftover dual (omzet JUMP 8.42m / pnl JUMP / FTE DROP)",
            "entity_id": ENTITY,
            "beneficiary": "Wevelgem elderly residents (RVT / assisted living)",
            "legal_basis": "VZW RVT / publiek gesubsidieerde ouderenzorg (KBO 0417.958.152)",
            "decision_date": "2026-07-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0417958152",
            "stated_goal": "Residential nursing-home care Wevelgem",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map Zorgkas vs omzet; "
                "explain pnl JUMP +208pct with FTE DROP"
            ),
            "source_id": "src_camillus_wevelgem_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>West-Vlaanderen>Wevelgem>WZC_Sint_Camillus>JR2025_statutory_L5",
            "notes": (
                "tick2108; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
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
            "name": "WZC Sint-Camillus Wevelgem omzet JUMP 8.42m / pnl JUMP / FTE DROP (YE2025)",
            "level": "L5",
            "type": "wzc_vzw_statutory",
            "hierarchy_path": "Vlaanderen>West-Vlaanderen>Wevelgem>WZC_Sint_Camillus>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary RVT envelope; bruto near omzet; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_camillus_wevelgem_jr2025_cw_en",
            "beneficiaries": "Wevelgem WZC Sint-Camillus residents (1 VE)",
            "stated_goal": "RVT nursing-home care",
            "measured_outcome": (
                "omzet JUMP +4.07%; bruto JUMP +0.86%; pnl JUMP +208.10%; "
                "equity JUMP +1.92%; FTE DROP 115.8 from 123.8"
            ),
            "absurdity_score": "4.5",
            "cost_score": "3.5",
            "difficulty": "3.0",
            "priority_index": "4.3",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; map Zorgkas vs omzet; "
                "explain pnl JUMP with staffing DROP"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2108; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Zilverlinde Olen still deferred"
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
            "hierarchy_path": "Vlaanderen>West-Vlaanderen>Wevelgem>WZC_Sint_Camillus>NBB_PDF_assets_debt",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); Zorgkas/public "
                "subsidy vs omzet split; explanation of pnl JUMP +208% with FTE DROP"
            ),
            "why_it_matters": (
                "Medium CW shows 8.42m omzet Wevelgem RVT VZW with pnl JUMP and staffing DROP "
                "without balanstotaal/assets/debt; material L5 residual WZC"
            ),
            "priority": "8",
            "recipient_body": "WZC Sint-Camillus VZW",
            "recipient_email": "info@wzcsintcamillus.be",
            "recipient_postal": "Kloosterstraat 21, 8560 Wevelgem",
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
            "notes": "tick2108; human-send only; Medium CW; next every-10 2110",
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
    if row["task_id"] == "rq_2108":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — WZC Sint-Camillus Wevelgem YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover WZC Sint-Camillus Wevelgem YE2025 Medium CW; KBO 0417.958.152; "
            f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} "
            f"FTE DROP {FTE}; FOI {GAP}; 1 VE NACE 87.101; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Zilverlinde Olen still deferred"
        )
        row["notes"] = (
            "tick2108 Sint-Camillus Wevelgem Medium omzet JUMP 8.42m bruto JUMP 8.38m pnl JUMP "
            "0.16m equity JUMP 4.94m FTE DROP 115.8; FOI ready; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2109; next every-10 2110"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2109" for r in rows):
    rows.append(
        {
            "task_id": "rq_2109",
            "title": "leftover dual hole-fill after Sint-Camillus — prefer AGB/FARO-YE2025/AIESH-REW/Zilverlinde/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2109 after WZC Sint-Camillus Wevelgem YE2025 Medium. Prefer leftover AGB/APB "
                "if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
                "WZC Zilverlinde Olen 0445.175.263 YE2025 live deferred, else unused water/DSO/IGS/"
                "HVZ/energy/hospital/WZC/psych. Do NOT redo Sint-Camillus Wevelgem, IDELUX "
                "Développement, IDELUX Projets Publics, IDELUX Eau, IDELUX Finances, IDELUX "
                "Environnement, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, HYGEA, "
                "BEP Environnement, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, "
                "Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Belgoprocess, "
                "Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2108 Sint-Camillus; next every-10 2110; Zilverlinde deferred",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2108 not found"

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
            "rq_2108",
            "2108",
            "no",
            (
                "tick2108 leftover WZC Sint-Camillus Wevelgem 0417.958.152 Medium CW "
                "(omzet JUMP 8.42m bruto JUMP 8.38m pnl JUMP 0.16m equity JUMP 4.94m "
                "FTE DROP 115.8; assets/debt Unknown; 1 VE); AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_2109; next every-10 2110; continuous hole_fill"
            ),
        ]
    )

if "## Tick 2108 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2108 already present")
else:
    log_block = f"""

## Tick 2108 - {UTC} - rq_2108 WZC Sint-Camillus Wevelgem (omzet JUMP 8.42m / pnl JUMP / FTE DROP / Medium)

- Unit: **rq_2108** leftover dual after **rq_2107 IDELUX Développement**. Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. Took deferred unused WZC **Sint-Camillus Wevelgem** YE2025 (KBO **0417.958.152**; Kloosterstraat 21 Wevelgem; VZW / **1 VE** / NACE **87.101** RVT). Zilverlinde Olen still deferred.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +4.07%; bruto **EUR{BRUTO}** JUMP +0.86%; pnl **EUR{PNL}** JUMP +208.10%; equity **EUR{EQUITY}** JUMP +1.92%; FTE **{FTE}** DROP vs YE2024 123.8; neerlegging **01.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@wzcsintcamillus.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 4.3); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2108=done + rq_2109 open; loop_state ticks=2108; raw docs/doge/data/raw/tick2108/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 2110**). Next: rq_2109 (AGB/FARO-if-YE2025 / AIESH-REW / Zilverlinde / unused).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2108 write OK; found=", found)

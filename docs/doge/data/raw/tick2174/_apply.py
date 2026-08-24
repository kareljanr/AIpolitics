# -*- coding: utf-8 -*-
"""Apply tick 2174 Orpimmo CSV + state + RQ + log updates."""
import csv
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

TS = "2026-08-26T04:00:00Z"
ENTITY = "nv_orpimmo"
GAP = "gap_orpimmo_nbb_pdf_assets_debt_equity_jump_pnl_loss_emeis_matrix_l5"
COMM = "comm_orpimmo_jr2025_statutory_holding_equity_jump_70m_pnl_loss_28_7m"
LB = "lb_orpimmo_equity_jump_70m_pnl_loss_28_7m_jr2025"
SRC_EN = "src_orpimmo_jr2025_cw_en"


def append_row(path, rowdict):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", quoting=csv.QUOTE_MINIMAL)
        w.writerow({k: rowdict.get(k, "") for k in fieldnames})


# --- sources ---
sources = [
    {
        "source_id": "src_orpimmo_jr2025_cw_nl",
        "title": "Companyweb NL ORPIMMO YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0870166709",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": "tick2174; YE2025 omzet DROP 811011 pnl LOSS -28702811 equity JUMP FLIP 69963602 bruto 217680 FTE 4.9; neerlegging 08.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2174/",
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN ORPIMMO YE2025 statutory",
        "url": "https://www.companyweb.be/en/0870166709",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": "tick2174; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025; Turnover 811011 Profit/Loss -28702811 Equity 69963602",
    },
    {
        "source_id": "src_orpimmo_jr2025_cw_fr",
        "title": "Companyweb FR ORPIMMO YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0870166709",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": "tick2174; FR mirror YE2025 Medium; Dernier bilan 2025",
    },
    {
        "source_id": "src_orpimmo_kbo_2174",
        "title": "KBO ORPIMMO 0870.166.709 Actief NV Ukkel emeis board",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0870166709",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick2174; Actief NV; Alsembergsesteenweg 1037 1180 Ukkel; 1 VE; NACE 64.210/82.990; kapitaal 77700000; bestuurder emeis Belgium 0887.690.451; KBO email empty",
    },
    {
        "source_id": "src_orpimmo_foi_contact_2174",
        "title": "ORPIMMO / emeis Het Dorp FOI channel hetdorp@emeis.com",
        "url": "https://emeis.be/nl/locaties/woonzorgcentrum/het-dorp",
        "publisher": "emeis / Het Dorp path",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": "tick2174; hetdorp@emeis.com; same zetel Alsembergsesteenweg 1037 as Het Dorp + Senes WZC; KBO email empty",
    },
]
for s in sources:
    append_row(ROOT / "sources.csv", s)

# --- budgets ---
budgets = [
    ("bud_orpimmo_omzet_jr2025_statutory", 811011, "CW statutory omzet / Turnover YE2025", "omzet DROP -25.74% vs YE2024 1092165"),
    ("bud_orpimmo_bruto_jr2025_statutory", 217680, "CW statutory bruto_marge / Gross margin YE2025", "bruto DROP vs YE2024 451595"),
    ("bud_orpimmo_pnl_jr2025_statutory", -28702811, "CW statutory winst / Profit-Loss after tax YE2025", "pnl LOSS IMPROVED vs YE2024 -56689064"),
    ("bud_orpimmo_equity_jr2025_statutory", 69963602, "CW statutory eigen_vermogen / Equity YE2025", "equity JUMP FLIP vs YE2024 -61333586"),
    ("bud_orpimmo_fte_jr2025_statutory", 4.9, "CW social-balance FTE / Employees 4.9", "FTE 4.9; assets/debt Unknown"),
]
for bid, amt, basis, note in budgets:
    append_row(
        ROOT / "budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick2174; Medium CW; {note}",
        },
    )

# --- commitments ---
append_row(
    ROOT / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "ORPIMMO YE2025 leftover dual (equity JUMP 70.0m FLIP / pnl LOSS -28.7m / emeis)",
        "entity_id": ENTITY,
        "beneficiary": "emeis Belgium / Senes WZC / Het Dorp Ukkel path",
        "legal_basis": "NV holding (KBO 0870.166.709; Actief; 1 VE; NACE 64.210; board emeis Belgium 0887.690.451; kapitaal 77.7m)",
        "decision_date": "2026-07-08",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": 69963602,
        "cash_by_year": '{"2025_omzet":811011,"2025_bruto":217680,"2025_pnl":-28702811,"2025_equity":69963602,"2025_fte":4.9,"2024_omzet":1092165,"2024_bruto":451595,"2024_pnl":-56689064,"2024_equity":-61333586}',
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0870166709",
        "stated_goal": "Holding activities elderly-care RE/ops path (Orpimmo / emeis Ukkel)",
        "cut_option": "Publish NBB PDF assets/debt FOI; disclose equity FLIP vs sustained LOSS; related-party vs emeis/Het Dorp/Senes",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Brussel>Ukkel>Orpimmo>JR2025_statutory_L5",
        "notes": "tick2174; Medium CW; equity primary envelope (JUMP FLIP); pnl LOSS -28.7m IMPROVED; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Het Dorp VZW + emeis Belgium; Senes WZC 0666.821.451 FREE deferred",
    },
)

# --- leaderboard ---
# absurdity 7.2 (equity flip + deep ongoing loss), cost 7.0 (70m equity / 28.7m loss), difficulty 3.5
# pi ≈ (7.2*0.4 + 7.0*0.4 + (10-3.5)*0.2) wait — prior pattern uses explicit scores
# use: absurdity 7.2, cost 7.0, difficulty 3.5 → priority ≈ 6.6
append_row(
    ROOT / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "ORPIMMO equity JUMP 70.0m FLIP / pnl LOSS -28.7m (YE2025)",
        "level": "L5",
        "type": "care_holding_nv_statutory",
        "hierarchy_path": "Brussel>Ukkel>Orpimmo>JR2025",
        "annual_cost_eur": 69963602,
        "total_cost_eur": 69963602,
        "tco_notes": "CW equity JUMP FLIP envelope 70.0m (from NEG -61.3m) / pnl LOSS -28.7m IMPROVED / omzet DROP 0.81m / FTE 4.9; emeis board; assets/debt Unknown pending NBB PDF",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "emeis Belgium / Senes WZC / Het Dorp Ukkel path",
        "stated_goal": "Holding elderly-care RE/ops Ukkel",
        "measured_outcome": "equity JUMP FLIP to 70.0m; pnl LOSS -28.7m IMPROVED; omzet DROP -25.7%; FTE 4.9",
        "absurdity_score": 7.2,
        "cost_score": 7.0,
        "difficulty": 3.5,
        "priority_index": 6.6,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose equity FLIP mechanism + related-party vs emeis 0887.690.451 / Het Dorp / Senes",
        "status": "open",
        "struck_reason": "",
        "notes": "tick2174; Medium CW; FOI gap_orpimmo_nbb_pdf_assets_debt_equity_jump_pnl_loss_emeis_matrix_l5; stall FARO/AIESH/REW YE2024; Senes FREE deferred",
    },
)

# --- entities ---
append_row(
    ROOT / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "ORPIMMO NV (Ukkel / emeis holding)",
        "name_fr": "ORPIMMO SA (Uccle / emeis holding)",
        "name_en": "ORPIMMO NV (emeis Ukkel care holding)",
        "level": "parastatal",
        "parent_id": "brussels_gov",
        "community_language": "bi",
        "website": "https://emeis.be/nl/locaties/woonzorgcentrum/het-dorp",
        "foi_email": "hetdorp@emeis.com",
        "foi_postal": "Alsembergsesteenweg 1037, 1180 Ukkel",
        "notes": "tick2174 YE2025 Medium CW NL+EN+FR + Strong KBO 0870.166.709 Actief NV 1 VE NACE 64.210; kapitaal 77.7m; bestuurder emeis Belgium 0887.690.451; omzet DROP 811k pnl LOSS -28.70m IMPROVED equity JUMP FLIP 69.96m FTE 4.9; owns Senes WZC 0666.821.451; same zetel Het Dorp 0835.884.236; assets/debt Unknown; FOI gap_orpimmo_nbb_pdf_assets_debt_equity_jump_pnl_loss_emeis_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; Senes FREE deferred",
    },
)

# --- foi_queue ---
append_row(
    ROOT / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Brussel>Ukkel>Orpimmo>NBB_PDF_assets_debt_equity_flip_emeis",
        "entity_id": ENTITY,
        "what_is_missing": "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); equity JUMP FLIP to EUR69.96m vs YE2024 NEG -61.33m recon; pnl LOSS EUR-28.70m IMPROVED path; related-party vs emeis Belgium 0887.690.451 + Het Dorp 0835.884.236 + Senes WZC 0666.821.451; omzet DROP EUR811k holding-fee/dividend/herwaardering flows",
        "why_it_matters": "Medium CW shows emeis Ukkel holding with EUR70m equity FLIP while still EUR28.7m LOSS and only EUR0.81m omzet — balanstotaal/assets/debt unpublished; dual opacity vs mined Het Dorp NEG equity shell",
        "priority": 8,
        "recipient_body": "ORPIMMO NV / emeis Belgium",
        "recipient_email": "hetdorp@emeis.com",
        "recipient_postal": "Alsembergsesteenweg 1037, 1180 Ukkel",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": TS,
        "updated_utc": TS,
        "notes": "tick2174; ready NOT sent; Medium CW + Strong KBO; Senes WZC FREE deferred; next every-10 2180",
    },
)

# --- research_queue: close 2174 + spawn 2175 ---
rq_path = ROOT / "research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys()) if rows else []

updated = False
for row in rows:
    if row.get("task_id") == "rq_2174":
        row["title"] = "leftover dual - ORPIMMO YE2025 Medium (equity JUMP 70.0m FLIP / pnl LOSS -28.7m)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = TS
        row["notes"] = (
            "tick2174 Orpimmo 0870.166.709 Medium; equity JUMP FLIP 69.96m pnl LOSS -28.70m omzet DROP 811k FTE 4.9; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Senes FREE deferred; next rq_2175; next every-10 2180"
        )
        row["instructions"] = (
            "Completed leftover ORPIMMO after Langerheide; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; "
            "Medium CW YE2025 + Strong KBO; FOI ready not sent"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2174 not found")

# check if rq_2175 exists
has_2175 = any(r.get("task_id") == "rq_2175" for r in rows)
if not has_2175:
    rows.append(
        {
            "task_id": "rq_2175",
            "title": "leftover dual hole-fill after Orpimmo - prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2175 after Orpimmo YE2025 Medium (equity JUMP 70.0m FLIP / pnl LOSS -28.7m / emeis). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS/HVZ live euros. Do NOT redo Orpimmo/Langerheide/Cur@-Z/Het Dorp/"
                "De Vlietoever/Abdij/Aaigem/Anima*/Zorg-Saam/Ben/Sint Lodewijk/Lork Hoeselt/emeis Belgium. "
                "Optional: Senes WZC 0666.821.451 if still FREE YE2025."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick2174 Orpimmo; FARO/AIESH/REW still YE2024; next every-10 2180",
        }
    )

with open(rq_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

# --- loop_state ---
with open(ROOT / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_2174",
            "ticks_completed": "2174",
            "paused": "no",
            "notes": (
                "tick2174 leftover ORPIMMO 0870.166.709 Medium (equity JUMP FLIP 69.96m from NEG -61.3m; "
                "pnl LOSS -28.70m IMPROVED; omzet DROP 811k; bruto 218k; FTE 4.9; emeis board; 1 VE NACE 64.210); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Senes FREE deferred; next rq_2175; next every-10 2180; continuous hole_fill"
            ),
        }
    )

# --- loop_log ---
log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick 2174 - {TS} - rq_2174 ORPIMMO (equity JUMP 70.0m FLIP / pnl LOSS -28.7m / Medium)

- Unit: **rq_2174** leftover dual after **rq_2173 Langerheide** (race: concurrent closed 2173 as Langerheide while this fire probed care/emeis). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Skipped Residentie Oudenburg NACE 68 RE hospitality; Pidpa already Strong-mined. Took unused leftover **ORPIMMO NV** YE2025 (KBO **0870.166.709**; Alsembergsesteenweg 1037 Ukkel; **NV** NACE **64.210** holdings / **1 VE**; kapitaal EUR77.7m; bestuurder **emeis Belgium 0887.690.451**; same zetel as mined Het Dorp). Deferred FREE **Senes WZC** 0666.821.451 (NACE 68 RE sibling). Do not redo Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Abdij/Aaigem/Anima*/Zorg-Saam/emeis Belgium.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR811011** DROP -25.74% vs YE2024 EUR1092165; bruto **EUR217680** DROP; pnl **EUR-28702811** LOSS IMPROVED vs YE2024 EUR-56689064; equity **EUR69963602** JUMP FLIP vs YE2024 EUR-61333586; FTE **4.9**; neerlegging **08.07.2026**. Assets/debt Unknown. Medium. Strong KBO Actief NV + emeis board.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.6); entities (+1 nv_orpimmo); foi + draft gap_orpimmo_nbb_pdf_assets_debt_equity_jump_pnl_loss_emeis_matrix_l5; rq_2174=done + rq_2175 open; loop_state ticks=2174; raw docs/doge/data/raw/tick2174/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2170**; next **2180**). Next: rq_2175 (AGB/FARO-if-YE2025 / AIESH-REW / Senes-or-unused IGS-DSO-WZC-MRS-HVZ).
"""
with open(log, "a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick2174 Orpimmo applied")

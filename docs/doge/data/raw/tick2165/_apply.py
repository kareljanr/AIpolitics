# -*- coding: utf-8 -*-
"""Apply tick2165 Anima Vlaanderen YE2025 Medium CW to DOGE CSVs."""
import csv
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
NOW = "2026-08-26T01:00:00Z"
TICK = "2165"
RQ = "rq_2165"
NEXT_RQ = "rq_2166"

ENTITY = "nv_anima_vlaanderen"
OMZET = 64669756
BRUTO = 43507548
PNL = -1421442
EQUITY = -888180
FTE = 599.5
OMZET_2024 = 59268776
PNL_2024 = -258694
EQUITY_2024 = 533262
BRUTO_2024 = 40205937

# % moves
omzet_pct = (OMZET - OMZET_2024) / OMZET_2024 * 100  # +9.11
equity_flip = True

GAP = "gap_anima_vl_nbb_pdf_assets_debt_pnl_deeper_loss_equity_neg_matrix_l5"
COMM = "comm_anima_vl_jr2025_statutory_wzc_pnl_deeper_loss_omzet_64_67m"
LB = "lb_anima_vl_omzet_64_67m_pnl_deeper_loss_equity_neg_jr2025"

csv.field_size_limit(10**7)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames


def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


# --- sources ---
sources, sh = read_csv(DATA / "sources.csv")
new_sources = [
    {
        "source_id": "src_anima_vl_jr2025_cw_nl",
        "title": "Companyweb NL Anima Vlaanderen YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0698940725/anima-vlaanderen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity FLIP NEG {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 04.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2165/",
    },
    {
        "source_id": "src_anima_vl_jr2025_cw_en",
        "title": "Companyweb EN Anima Vlaanderen YE2025 statutory",
        "url": "https://www.companyweb.be/en/0698940725",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 04-07-2026; FTE {FTE}; raw docs/doge/data/raw/tick2165/anima_vl_en.html",
    },
    {
        "source_id": "src_anima_vl_jr2025_cw_fr",
        "title": "Companyweb FR Anima Vlaanderen YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0698940725",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium",
    },
    {
        "source_id": "src_anima_vl_kbo_2165",
        "title": "KBO Anima Vlaanderen 0698.940.725 Actief NV Mechelen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0698940725",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick2165; Actief NV; Zandvoortstraat 27 2800 Mechelen; 11 VE; NACE 87.301/87.302 ROB/serviceflats; KBO email empty; start 29.06.2018",
    },
    {
        "source_id": "src_anima_vl_foi_contact_2165",
        "title": "Anima Group FOI contact info@animagroup.be (Anima Vlaanderen)",
        "url": "https://animagroup.be/",
        "publisher": "Anima NV / Anima Vlaanderen",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": "tick2165; info@animagroup.be; tel 015 28 77 40; zetel Zandvoortstraat 27 Mechelen; sibling Avondvrede 0446.506.836 FREE deferred",
    },
]
existing_src = {r["source_id"] for r in sources}
for s in new_sources:
    if s["source_id"] not in existing_src:
        sources.append(s)
write_csv(DATA / "sources.csv", sources, sh)
print("sources", len(new_sources))

# --- entities ---
entities, eh = read_csv(DATA / "entities.csv")
if not any(r["entity_id"] == ENTITY for r in entities):
    entities.append(
        {
            "entity_id": ENTITY,
            "name_nl": "Anima Vlaanderen NV",
            "name_fr": "Anima Vlaanderen SA",
            "name_en": "Anima Vlaanderen (Flemish elderly-care operator)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://animagroup.be/",
            "foi_email": "info@animagroup.be",
            "foi_postal": "Zandvoortstraat 27, 2800 Mechelen",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0698.940.725 Actief NV 11 VE NACE 87.301/87.302; "
                f"omzet JUMP {OMZET/1e6:.2f}m (+{omzet_pct:.2f}%) pnl DEEPER LOSS {PNL/1e6:.2f}m equity FLIP NEG {EQUITY}; "
                f"bruto JUMP {BRUTO/1e6:.2f}m FTE {FTE}; assets/debt Unknown; neerlegging 04.07.2026; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"do not redo Zorg-Saam/Sint-Bernardus De Panne/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork/"
                f"OLV Kempen/HERTOG JAN/Lindeboom; Avondvrede 0446.506.836 FREE deferred; Anima hold 0469.969.453 FREE deferred"
            ),
        }
    )
write_csv(DATA / "entities.csv", entities, eh)
print("entities ok")

# --- budgets ---
budgets, bh = read_csv(DATA / "budgets.csv")
new_buds = [
    ("bud_anima_vl_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025"),
    ("bud_anima_vl_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025"),
    ("bud_anima_vl_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025"),
    ("bud_anima_vl_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025"),
    ("bud_anima_vl_fte_jr2025_statutory", FTE, f"CW social-balance FTE / Employees {FTE}"),
]
existing_b = {r["budget_id"] for r in budgets}
for bid, amt, basis in new_buds:
    if bid in existing_b:
        continue
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(amt),
            "amount_min_eur": str(amt),
            "amount_max_eur": str(amt),
            "basis": basis,
            "source_id": "src_anima_vl_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF",
        }
    )
write_csv(DATA / "budgets.csv", budgets, bh)
print("budgets", len(new_buds))

# --- commitments ---
comms, ch = read_csv(DATA / "commitments.csv")
if not any(r["commitment_id"] == COMM for r in comms):
    cash = (
        f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
        f'"2025_fte":{FTE},"2024_omzet":{OMZET_2024},"2024_pnl":{PNL_2024},'
        f'"2024_equity":{EQUITY_2024},"2024_bruto":{BRUTO_2024}}}'
    )
    comms.append(
        {
            "commitment_id": COMM,
            "title": "Anima Vlaanderen YE2025 leftover dual (omzet JUMP 64.67m / pnl DEEPER LOSS -1.42m / equity NEG)",
            "entity_id": ENTITY,
            "beneficiary": "WZC/ROB residents via Anima Vlaanderen (11 VE; Anima Group Flemish belt incl. Avondvrede path)",
            "legal_basis": "NV ROB/serviceflats (KBO 0698.940.725; Actief; 11 VE; NACE 87.301/87.302)",
            "decision_date": "2026-07-04",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0698940725",
            "stated_goal": "Residential elderly care Flanders (Anima Vlaanderen operating NV)",
            "cut_option": "Publish NBB PDF assets/debt FOI; explain pnl DEEPER LOSS + equity NEG flip despite omzet JUMP +9.1%; per-site matrix",
            "source_id": "src_anima_vl_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Anima>AnimaVlaanderen>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Zorg-Saam/Sint-Bernardus/Ruggeveld/"
                f"Salvator/Boterlaarhof/WZND/Foyer De Lork; Avondvrede FREE deferred"
            ),
        }
    )
write_csv(DATA / "commitments.csv", comms, ch)
print("commitments ok")

# --- leaderboard ---
# pi ~ (abs*cost)/difficulty style used ~5.5-6.7; use abs 6.4 cost 7.2 diff 4.0 -> pi ~6.1
lbs, lh = read_csv(DATA / "leaderboard.csv")
if not any(r["item_id"] == LB for r in lbs):
    lbs.append(
        {
            "item_id": LB,
            "name": "Anima Vlaanderen omzet JUMP 64.67m / pnl DEEPER LOSS -1.42m / equity NEG (YE2025)",
            "level": "L5",
            "type": "wzc_nv_statutory",
            "hierarchy_path": "Vlaanderen>Anima>AnimaVlaanderen>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                f"CW omzet envelope 64.67m / {FTE} FTE / 11 VE; pnl DEEPER LOSS -1.42m (vs YE2024 -0.26m); "
                f"equity FLIP NEG -0.89m; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": "src_anima_vl_jr2025_cw_en",
            "beneficiaries": "WZC/ROB clients Anima Vlaanderen network",
            "stated_goal": "Residential elderly care Flanders (Anima Group)",
            "measured_outcome": (
                f"omzet JUMP +{omzet_pct:.2f}%; bruto JUMP +{(BRUTO-BRUTO_2024)/BRUTO_2024*100:.2f}%; "
                f"pnl DEEPER LOSS; equity FLIP NEG; FTE {FTE}"
            ),
            "absurdity_score": "6.4",
            "cost_score": "7.2",
            "difficulty": "4.0",
            "priority_index": "6.1",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose deeper-loss + negative-equity path despite rising omzet; per-site matrix",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Anima hold/Avondvrede FREE deferred",
        }
    )
write_csv(DATA / "leaderboard.csv", lbs, lh)
print("leaderboard ok")

# --- foi_queue ---
foi, fh = read_csv(DATA / "foi_queue.csv")
if not any(r["gap_id"] == GAP for r in foi):
    foi.append(
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Anima>AnimaVlaanderen>NBB_PDF_assets_debt_pnl_deeper_loss_equity_neg",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "RIZIV/Vlaams vs dagprijs split; explanation of pnl DEEPER LOSS EUR-1.42m "
                "(vs YE2024 EUR-0.26m) and equity FLIP NEG EUR-0.89m despite omzet JUMP +9.1%; per-site 11 VE matrix"
            ),
            "why_it_matters": (
                "Medium CW shows EUR64.67m Anima Vlaanderen NV WZC/ROB operator with deepening LOSS "
                "and negative equity while turnover rose — no balanstotaal/assets/debt published"
            ),
            "priority": "8",
            "recipient_body": "Anima Vlaanderen NV / Anima Group",
            "recipient_email": "info@animagroup.be",
            "recipient_postal": "Zandvoortstraat 27, 2800 Mechelen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-26",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2170",
        }
    )
write_csv(DATA / "foi_queue.csv", foi, fh)
print("foi ok")

# --- research_queue: close 2165, spawn 2166 ---
rq, rh = read_csv(DATA / "research_queue.csv")
for r in rq:
    if r["task_id"] == RQ:
        r["title"] = (
            "leftover dual — Anima Vlaanderen YE2025 Medium (omzet JUMP 64.67m / pnl DEEPER LOSS -1.42m / equity NEG)"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "Completed leftover Anima Vlaanderen after Zorg-Saam; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; "
            "skipped Residentie Oudenburg NACE 68 private RE; Lork Hoeselt BV empty-omzet RE fallback deferred; "
            "Avondvrede 0446.506.836 FREE YE2025 deferred; Medium CW YE2025 + Strong KBO; FOI ready not sent"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK} Anima Vlaanderen Medium omzet JUMP {OMZET/1e6:.2f}m (+{omzet_pct:.2f}%) bruto JUMP {BRUTO/1e6:.2f}m "
            f"pnl DEEPER LOSS {PNL/1e6:.2f}m equity FLIP NEG {EQUITY} FTE {FTE}; KBO Actief NV 11 VE Mechelen; "
            f"FOI info@animagroup.be; next every-10 2170"
        )
if not any(r["task_id"] == NEXT_RQ for r in rq):
    rq.append(
        {
            "task_id": NEXT_RQ,
            "title": "leftover dual hole-fill after Anima Vlaanderen — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2166 after Anima Vlaanderen YE2025 Medium (omzet 64.67m / pnl DEEPER LOSS -1.42m / equity NEG). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS (optional: Avondvrede 0446.506.836 YE2025 FREE / Anima hold 0469.969.453 / "
                "Lork Hoeselt BV 0755.822.317). Do NOT redo Anima Vlaanderen/Zorg-Saam/Sint-Bernardus De Panne/"
                "Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork/OLV Kempen/HERTOG JAN/Lindeboom/IPFBW/Aquiris/"
                "SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/"
                "Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick2165 Anima Vlaanderen; FARO/AIESH/REW still YE2024; next every-10 2170",
        }
    )
write_csv(DATA / "research_queue.csv", rq, rh)
print("research_queue ok")

# --- loop_state ---
state_path = DATA / "loop_state.csv"
state_rows, sth = read_csv(state_path)
for r in state_rows:
    if r["state_id"] == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = NOW
        r["last_unit_id"] = RQ
        r["ticks_completed"] = TICK
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} leftover Anima Vlaanderen 0698.940.725 Medium (omzet JUMP 64.67m; pnl DEEPER LOSS -1.42m; "
            f"equity FLIP NEG -0.89m; FTE 599.5; 11 VE); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            f"Avondvrede/Anima hold/Lork Hoeselt FREE deferred; next {NEXT_RQ}; next every-10 2170; continuous hole_fill"
        )
write_csv(state_path, state_rows, sth)
print("loop_state ok")
print("DONE tick", TICK)

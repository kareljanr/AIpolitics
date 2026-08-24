# -*- coding: utf-8 -*-
"""Apply tick2166 Rusthuis Avondvrede YE2025 Medium CW."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
NOW = "2026-08-26T01:20:00Z"
TICK = "2166"
RQ = "rq_2166"
NEXT_RQ = "rq_2167"

ENTITY = "nv_rusthuis_avondvrede"
OMZET = 2199837
BRUTO = 1834588
PNL = -26205
EQUITY = 211466
FTE = 22.4
OMZET_2024 = 2367080
PNL_2024 = 95524
EQUITY_2024 = 237671
BRUTO_2024 = 1849185

omzet_pct = (OMZET - OMZET_2024) / OMZET_2024 * 100  # -7.07
equity_pct = (EQUITY - EQUITY_2024) / EQUITY_2024 * 100  # -11.03

GAP = "gap_avondvrede_nbb_pdf_assets_debt_pnl_flip_loss_omzet_drop_matrix_l5"
COMM = "comm_avondvrede_jr2025_statutory_wzc_pnl_flip_loss_omzet_2_20m"
LB = "lb_avondvrede_omzet_2_20m_pnl_flip_loss_jr2025"

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


sources, sh = read_csv(DATA / "sources.csv")
new_sources = [
    {
        "source_id": "src_avondvrede_jr2025_cw_nl",
        "title": "Companyweb NL Rusthuis Avondvrede YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0446506836/rusthuis-avondvrede",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; YE2025 omzet DROP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 03.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2166/",
    },
    {
        "source_id": "src_avondvrede_jr2025_cw_en",
        "title": "Companyweb EN Rusthuis Avondvrede YE2025 statutory",
        "url": "https://www.companyweb.be/en/0446506836",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 03-07-2026; FTE {FTE}",
    },
    {
        "source_id": "src_avondvrede_jr2025_cw_fr",
        "title": "Companyweb FR Rusthuis Avondvrede YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0446506836",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium",
    },
    {
        "source_id": "src_avondvrede_kbo_2166",
        "title": "KBO Rusthuis Avondvrede 0446.506.836 Actief NV Mechelen/Boechout",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0446506836",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick2166; Actief NV; zetel Zandvoortstraat 27 2800 Mechelen (Anima); 1 VE; NACE 87.101/87.301; site Boechout; KBO email empty; start 10.02.1992",
    },
    {
        "source_id": "src_avondvrede_foi_contact_2166",
        "title": "Avondvrede FOI contact avondvrede.dir@animagroup.be",
        "url": "https://rusthuisavondvrede.be/",
        "publisher": "Rusthuis Avondvrede / Anima Group",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": "tick2166; avondvrede.dir@animagroup.be; also info@animagroup.be; tel 03 455 44 56; Anima acquisition Oct 2024; rebuild path",
    },
]
existing_src = {r["source_id"] for r in sources}
for s in new_sources:
    if s["source_id"] not in existing_src:
        sources.append(s)
write_csv(DATA / "sources.csv", sources, sh)

entities, eh = read_csv(DATA / "entities.csv")
if not any(r["entity_id"] == ENTITY for r in entities):
    entities.append(
        {
            "entity_id": ENTITY,
            "name_nl": "Rusthuis Avondvrede NV (Boechout / Anima)",
            "name_fr": "Maison de repos Avondvrede SA (Boechout / Anima)",
            "name_en": "Avondvrede nursing home (Boechout / Anima Group)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://rusthuisavondvrede.be/",
            "foi_email": "avondvrede.dir@animagroup.be",
            "foi_postal": "Zandvoortstraat 27, 2800 Mechelen (site: Alexander Franckstraat 34, 2530 Boechout)",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0446.506.836 Actief NV 1 VE NACE 87.101/87.301; "
                f"omzet DROP {OMZET/1e6:.2f}m ({omzet_pct:.2f}%) pnl FLIP LOSS {PNL} equity DROP {EQUITY} "
                f"bruto DROP {BRUTO/1e6:.2f}m FTE {FTE}; assets/debt Unknown; neerlegging 03.07.2026; "
                f"FOI {GAP}; Anima Group sibling of Anima Vlaanderen; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"do not redo Anima Vlaanderen/t Hofke/Zorg-Saam/Sint-Bernardus De Panne/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork"
            ),
        }
    )
write_csv(DATA / "entities.csv", entities, eh)

budgets, bh = read_csv(DATA / "budgets.csv")
new_buds = [
    ("bud_avondvrede_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025"),
    ("bud_avondvrede_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025"),
    ("bud_avondvrede_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025"),
    ("bud_avondvrede_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025"),
    ("bud_avondvrede_fte_jr2025_statutory", FTE, f"CW social-balance FTE / Employees {FTE}"),
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
            "source_id": "src_avondvrede_jr2025_cw_en",
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF",
        }
    )
write_csv(DATA / "budgets.csv", budgets, bh)

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
            "title": "Rusthuis Avondvrede YE2025 leftover dual (omzet DROP 2.20m / pnl FLIP LOSS / FTE 22.4)",
            "entity_id": ENTITY,
            "beneficiary": "WZC residents Boechout Avondvrede (Anima Group; rebuild to 64 beds + AW path)",
            "legal_basis": "NV RVT/ROB (KBO 0446.506.836; Actief; 1 VE; NACE 87.101/87.301)",
            "decision_date": "2026-07-03",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0446506836",
            "stated_goal": "Residential elderly care Boechout (Avondvrede / Anima)",
            "cut_option": "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS + omzet DROP amid Anima rebuild; RIZIV/dagprijs split",
            "source_id": "src_avondvrede_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Boechout>Avondvrede>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Anima Vlaanderen/t Hofke/Zorg-Saam; "
                f"Anima hold 0469.969.453 FREE deferred"
            ),
        }
    )
write_csv(DATA / "commitments.csv", comms, ch)

lbs, lh = read_csv(DATA / "leaderboard.csv")
if not any(r["item_id"] == LB for r in lbs):
    lbs.append(
        {
            "item_id": LB,
            "name": "Rusthuis Avondvrede omzet DROP 2.20m / pnl FLIP LOSS (YE2025)",
            "level": "L5",
            "type": "wzc_nv_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Boechout>Avondvrede>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                f"CW omzet envelope 2.20m / {FTE} FTE; pnl FLIP LOSS from YE2024 profit; equity DROP {equity_pct:.1f}%; "
                f"Anima acquisition/rebuild; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": "src_avondvrede_jr2025_cw_en",
            "beneficiaries": "WZC clients Boechout Avondvrede",
            "stated_goal": "Residential elderly care Boechout",
            "measured_outcome": (
                f"omzet DROP {omzet_pct:.2f}%; bruto DROP; pnl FLIP LOSS; equity DROP {equity_pct:.2f}%; FTE {FTE}"
            ),
            "absurdity_score": "5.6",
            "cost_score": "4.2",
            "difficulty": "3.5",
            "priority_index": "5.0",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose pnl flip + omzet drop path under Anima rebuild",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Anima hold FREE deferred",
        }
    )
write_csv(DATA / "leaderboard.csv", lbs, lh)

foi, fh = read_csv(DATA / "foi_queue.csv")
if not any(r["gap_id"] == GAP for r in foi):
    foi.append(
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Boechout>Avondvrede>NBB_PDF_assets_debt_pnl_flip_loss",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "RIZIV/Vlaams vs dagprijs split; explanation of pnl FLIP LOSS EUR-26.2k "
                "(vs YE2024 profit EUR95.5k) and omzet DROP -7.1% under Anima rebuild/nieuwbouw"
            ),
            "why_it_matters": (
                "Medium CW shows EUR2.20m Boechout WZC NV (Anima) flipping to LOSS with falling omzet — "
                "no balanstotaal/assets/debt; rebuild opacity material for FOI"
            ),
            "priority": "8",
            "recipient_body": "Rusthuis Avondvrede NV / Anima Group",
            "recipient_email": "avondvrede.dir@animagroup.be",
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

rq, rh = read_csv(DATA / "research_queue.csv")
for r in rq:
    if r["task_id"] == RQ:
        r["title"] = (
            "leftover dual — Rusthuis Avondvrede YE2025 Medium (omzet DROP 2.20m / pnl FLIP LOSS)"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "Completed leftover Avondvrede after Anima Vlaanderen/t Hofke race; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent; Anima hold deferred"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK} Avondvrede Medium omzet DROP {OMZET/1e6:.2f}m ({omzet_pct:.2f}%) bruto DROP "
            f"pnl FLIP LOSS {PNL} equity DROP {EQUITY} FTE {FTE}; KBO Actief NV 1 VE Anima; "
            f"FOI avondvrede.dir@animagroup.be; next every-10 2170"
        )
if not any(r["task_id"] == NEXT_RQ for r in rq):
    rq.append(
        {
            "task_id": NEXT_RQ,
            "title": "leftover dual hole-fill after Avondvrede — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2167 after Avondvrede YE2025 Medium (omzet DROP 2.20m / pnl FLIP LOSS). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS (optional: Anima hold 0469.969.453 YE2025 FREE / Lork Hoeselt BV). "
                "Do NOT redo Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam/Sint-Bernardus De Panne/Ruggeveld/"
                "Salvator/Boterlaarhof/WZND/Foyer De Lork/IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/"
                "Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/"
                "Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick2166 Avondvrede; FARO/AIESH/REW still YE2024; next every-10 2170",
        }
    )
write_csv(DATA / "research_queue.csv", rq, rh)

state_rows, sth = read_csv(DATA / "loop_state.csv")
for r in state_rows:
    if r["state_id"] == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = NOW
        r["last_unit_id"] = RQ
        r["ticks_completed"] = TICK
        r["paused"] = "no"
        r["notes"] = (
            f"tick{TICK} leftover Avondvrede 0446.506.836 Medium (omzet DROP 2.20m; pnl FLIP LOSS -26k; "
            f"equity DROP 0.21m; FTE 22.4; Anima); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            f"Anima hold/Lork Hoeselt FREE deferred; next {NEXT_RQ}; next every-10 2170; continuous hole_fill"
        )
write_csv(DATA / "loop_state.csv", state_rows, sth)
print("DONE tick", TICK)

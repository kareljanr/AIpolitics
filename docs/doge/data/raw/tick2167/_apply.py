# -*- coding: utf-8 -*-
"""Apply tick2167 Anima NV holding YE2025 Medium CW."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
NOW = "2026-08-26T01:40:00Z"
TICK = "2167"
RQ = "rq_2167"
NEXT_RQ = "rq_2168"

ENTITY = "nv_anima"
OMZET = 2446909
BRUTO = 1328972
PNL = 2057209
EQUITY = 69520927
FTE = 1.2
OMZET_2024 = 1861143
PNL_2024 = 1445954
EQUITY_2024 = 67463718
BRUTO_2024 = 908257

omzet_pct = (OMZET - OMZET_2024) / OMZET_2024 * 100
pnl_pct = (PNL - PNL_2024) / PNL_2024 * 100
equity_pct = (EQUITY - EQUITY_2024) / EQUITY_2024 * 100

GAP = "gap_anima_hold_nbb_pdf_assets_debt_related_party_dividend_matrix_l5"
COMM = "comm_anima_hold_jr2025_statutory_holding_pnl_jump_omzet_2_45m"
LB = "lb_anima_hold_omzet_2_45m_pnl_jump_equity_69_5m_jr2025"

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
for s in [
    {
        "source_id": "src_anima_hold_jr2025_cw_nl",
        "title": "Companyweb NL Anima NV YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0469969453/anima",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 10.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2167/",
    },
    {
        "source_id": "src_anima_hold_jr2025_cw_en",
        "title": "Companyweb EN Anima NV YE2025 statutory",
        "url": "https://www.companyweb.be/en/0469969453",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 10-06-2026; FTE {FTE}",
    },
    {
        "source_id": "src_anima_hold_jr2025_cw_fr",
        "title": "Companyweb FR Anima NV YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0469969453",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium",
    },
    {
        "source_id": "src_anima_hold_kbo_2167",
        "title": "KBO Anima NV 0469.969.453 Actief holding Mechelen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0469969453",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick2167; Actief NV; Zandvoortstraat 27 2800 Mechelen; 1 VE; NACE 64.210 holdings; KBO email info@animagroup.be; commercial ANIMA HEALTH & CARE; start 21.01.2000",
    },
    {
        "source_id": "src_anima_hold_foi_contact_2167",
        "title": "Anima Group FOI contact info@animagroup.be",
        "url": "https://animagroup.be/",
        "publisher": "Anima NV",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": "tick2167; info@animagroup.be; tel 015 28 77 40; parent of Anima Vlaanderen + Avondvrede path",
    },
]:
    if s["source_id"] not in {r["source_id"] for r in sources}:
        sources.append(s)
write_csv(DATA / "sources.csv", sources, sh)

entities, eh = read_csv(DATA / "entities.csv")
if not any(r["entity_id"] == ENTITY for r in entities):
    entities.append(
        {
            "entity_id": ENTITY,
            "name_nl": "Anima NV (holding / Anima Health & Care)",
            "name_fr": "Anima SA (holding / Anima Health & Care)",
            "name_en": "Anima NV (elderly-care holding)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://animagroup.be/",
            "foi_email": "info@animagroup.be",
            "foi_postal": "Zandvoortstraat 27, 2800 Mechelen",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0469.969.453 Actief NV 1 VE NACE 64.210 holding; "
                f"omzet JUMP {OMZET/1e6:.2f}m (+{omzet_pct:.2f}%) pnl JUMP {PNL/1e6:.2f}m (+{pnl_pct:.2f}%) "
                f"equity JUMP {EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; neerlegging 10.06.2026; "
                f"FOI {GAP}; parent opacity vs Anima Vlaanderen LOSS + Avondvrede FLIP LOSS; "
                f"preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam"
            ),
        }
    )
write_csv(DATA / "entities.csv", entities, eh)

budgets, bh = read_csv(DATA / "budgets.csv")
existing_b = {r["budget_id"] for r in budgets}
for bid, amt, basis in [
    ("bud_anima_hold_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025"),
    ("bud_anima_hold_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025"),
    ("bud_anima_hold_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025"),
    ("bud_anima_hold_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025"),
    ("bud_anima_hold_fte_jr2025_statutory", FTE, f"CW social-balance FTE / Employees {FTE}"),
]:
    if bid not in existing_b:
        budgets.append(
            {
                "budget_id": bid,
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(amt),
                "amount_min_eur": str(amt),
                "amount_max_eur": str(amt),
                "basis": basis,
                "source_id": "src_anima_hold_jr2025_cw_en",
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
            "title": "Anima NV holding YE2025 leftover dual (omzet JUMP 2.45m / pnl JUMP 2.06m / equity 69.5m)",
            "entity_id": ENTITY,
            "beneficiary": "Anima Group shareholders / related WZC operators (Vlaanderen + Avondvrede path)",
            "legal_basis": "NV holding (KBO 0469.969.453; Actief; 1 VE; NACE 64.210)",
            "decision_date": "2026-06-10",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0469969453",
            "stated_goal": "Holding activities elderly-care group (Anima Health & Care)",
            "cut_option": "Publish NBB PDF assets/debt FOI; related-party/dividend matrix vs Anima Vlaanderen LOSS + Avondvrede FLIP LOSS",
            "source_id": "src_anima_hold_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Anima>AnimaHold>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam; "
                f"Lork Hoeselt FREE deferred"
            ),
        }
    )
write_csv(DATA / "commitments.csv", comms, ch)

lbs, lh = read_csv(DATA / "leaderboard.csv")
if not any(r["item_id"] == LB for r in lbs):
    lbs.append(
        {
            "item_id": LB,
            "name": "Anima NV hold omzet JUMP 2.45m / pnl JUMP 2.06m / equity 69.5m (YE2025)",
            "level": "L5",
            "type": "holding_nv_statutory",
            "hierarchy_path": "Vlaanderen>Anima>AnimaHold>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(EQUITY),
            "tco_notes": (
                f"CW omzet envelope 2.45m / pnl 2.06m / equity 69.5m / {FTE} FTE; holding profit while "
                f"Anima Vlaanderen LOSS + Avondvrede FLIP LOSS; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": "src_anima_hold_jr2025_cw_en",
            "beneficiaries": "Anima Group holding / related WZC network",
            "stated_goal": "Holding activities elderly-care group",
            "measured_outcome": (
                f"omzet JUMP +{omzet_pct:.2f}%; pnl JUMP +{pnl_pct:.2f}%; equity JUMP +{equity_pct:.2f}%; FTE {FTE}"
            ),
            "absurdity_score": "6.0",
            "cost_score": "5.5",
            "difficulty": "3.5",
            "priority_index": "5.7",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose related-party flows vs LOSS subsidiaries",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Lork Hoeselt FREE deferred",
        }
    )
write_csv(DATA / "leaderboard.csv", lbs, lh)

foi, fh = read_csv(DATA / "foi_queue.csv")
if not any(r["gap_id"] == GAP for r in foi):
    foi.append(
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Anima>AnimaHold>NBB_PDF_assets_debt_related_party_dividend",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "related-party / dividend / management-fee matrix vs Anima Vlaanderen (pnl LOSS -1.42m, equity NEG) "
                "and Avondvrede (pnl FLIP LOSS); consolidation perimeter"
            ),
            "why_it_matters": (
                "Medium CW shows EUR2.45m Anima holding with EUR2.06m profit and EUR69.5m equity while "
                "operating WZC subsidiaries post LOSS — related-party opacity without balanstotaal"
            ),
            "priority": "8",
            "recipient_body": "Anima NV / Anima Group",
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

rq, rh = read_csv(DATA / "research_queue.csv")
for r in rq:
    if r["task_id"] == RQ:
        r["title"] = (
            "leftover dual — Anima NV holding YE2025 Medium (omzet JUMP 2.45m / pnl JUMP 2.06m / equity 69.5m)"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "Completed leftover Anima hold after Avondvrede; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; "
            "Medium CW YE2025 + Strong KBO; FOI ready not sent; Lork Hoeselt deferred"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK} Anima hold Medium omzet JUMP {OMZET/1e6:.2f}m (+{omzet_pct:.2f}%) pnl JUMP {PNL/1e6:.2f}m "
            f"equity JUMP {EQUITY/1e6:.2f}m FTE {FTE}; KBO Actief NV holding 64.210; FOI info@animagroup.be; next every-10 2170"
        )
if not any(r["task_id"] == NEXT_RQ for r in rq):
    rq.append(
        {
            "task_id": NEXT_RQ,
            "title": "leftover dual hole-fill after Anima hold — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2168 after Anima NV holding YE2025 Medium (omzet 2.45m / pnl 2.06m / equity 69.5m). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS (optional: Lork Hoeselt BV 0755.822.317). "
                "Do NOT redo Anima hold/Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam/Sint-Bernardus De Panne/"
                "Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork/IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/"
                "Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/"
                "Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick2167 Anima hold; FARO/AIESH/REW still YE2024; next every-10 2170",
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
            f"tick{TICK} leftover Anima NV hold 0469.969.453 Medium (omzet JUMP 2.45m; pnl JUMP 2.06m; "
            f"equity JUMP 69.5m; FTE 1.2; NACE 64.210); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            f"Lork Hoeselt FREE deferred; next {NEXT_RQ}; next every-10 2170; continuous hole_fill"
        )
write_csv(DATA / "loop_state.csv", state_rows, sth)
print("DONE tick", TICK)

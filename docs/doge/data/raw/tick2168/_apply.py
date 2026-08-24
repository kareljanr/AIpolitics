# -*- coding: utf-8 -*-
"""Apply tick2168 WZC Foyer De Lork Hoeselt BV YE2025 Medium CW."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
NOW = "2026-08-26T02:00:00Z"
TICK = "2168"
RQ = "rq_2168"
NEXT_RQ = "rq_2169"

ENTITY = "bv_wzc_foyer_de_lork_hoeselt"
BRUTO = 785637
PNL = -87190
EQUITY = -126400
FTE = 0
BRUTO_2024 = -4514
PNL_2024 = -12055
EQUITY_2024 = -39210
# primary envelope = bruto (omzet empty)
PRIMARY = BRUTO

GAP = "gap_lork_hoeselt_nbb_pdf_assets_debt_omzet_empty_bruto_jump_equity_neg_matrix_l5"
COMM = "comm_lork_hoeselt_jr2025_statutory_re_bruto_jump_equity_neg"
LB = "lb_lork_hoeselt_bruto_785k_omzet_empty_equity_neg_jr2025"

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
        "source_id": "src_lork_hoeselt_jr2025_cw_nl",
        "title": "Companyweb NL WZC Foyer De Lork Hoeselt YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0755822317",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; YE2025 omzet empty bruto JUMP {BRUTO} pnl DEEPER LOSS {PNL} equity NEG {EQUITY} FTE {FTE}; neerlegging 13.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2168/",
    },
    {
        "source_id": "src_lork_hoeselt_jr2025_cw_en",
        "title": "Companyweb EN WZC Foyer De Lork Hoeselt YE2025 statutory",
        "url": "https://www.companyweb.be/en/0755822317",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 13-06-2026; Turnover unpublished; FTE {FTE}",
    },
    {
        "source_id": "src_lork_hoeselt_jr2025_cw_fr",
        "title": "Companyweb FR WZC Foyer De Lork Hoeselt YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0755822317",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-26",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium",
    },
    {
        "source_id": "src_lork_hoeselt_kbo_2168",
        "title": "KBO WZC Foyer De Lork Hoeselt 0755.822.317 Actief BV Schoten",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0755822317",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick2168; Actief BV; Horstebaan 3 2900 Schoten; 1 VE; NACE 68.201 RE lease; bestuurder Care Property 0456.378.070; KBO email empty; start 07.10.2020",
    },
    {
        "source_id": "src_lork_hoeselt_foi_contact_2168",
        "title": "Foyer De Lork / Care Property FOI channel",
        "url": "https://carepropertyinvest.be/",
        "publisher": "Care Property Invest / Foyer De Lork",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": "tick2168; info@carepropertyinvest.be; also try info@foyerdelork.be (VZW Geel sibling path); DISTINCT mined Foyer De Lork VZW 0446.022.331",
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
            "name_nl": "WZC Foyer De Lork Hoeselt BV (Schoten / Care Property)",
            "name_fr": "WZC Foyer De Lork Hoeselt SRL (Schoten / Care Property)",
            "name_en": "WZC Foyer De Lork Hoeselt BV (Care Property RE SPV)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://carepropertyinvest.be/",
            "foi_email": "info@carepropertyinvest.be",
            "foi_postal": "Horstebaan 3, 2900 Schoten",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0755.822.317 Actief BV 1 VE NACE 68.201; "
                f"omzet empty bruto JUMP {BRUTO} pnl DEEPER LOSS {PNL} equity NEG {EQUITY} FTE 0; "
                f"assets/debt Unknown; neerlegging 13.06.2026; Care Property board 0456.378.070; "
                f"FOI {GAP}; DISTINCT Foyer De Lork VZW Geel; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"do not redo Anima hold/Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam/Sint-Bernardus/Ruggeveld"
            ),
        }
    )
write_csv(DATA / "entities.csv", entities, eh)

budgets, bh = read_csv(DATA / "budgets.csv")
existing_b = {r["budget_id"] for r in budgets}
for bid, amt, basis in [
    ("bud_lork_hoeselt_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025 (omzet empty)"),
    ("bud_lork_hoeselt_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025"),
    ("bud_lork_hoeselt_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025"),
    ("bud_lork_hoeselt_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees 0"),
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
                "source_id": "src_lork_hoeselt_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet unpublished; assets/debt Unknown pending NBB PDF",
            }
        )
write_csv(DATA / "budgets.csv", budgets, bh)

comms, ch = read_csv(DATA / "commitments.csv")
if not any(r["commitment_id"] == COMM for r in comms):
    cash = (
        f'{{"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
        f'"2025_omzet":null,"2024_bruto":{BRUTO_2024},"2024_pnl":{PNL_2024},"2024_equity":{EQUITY_2024}}}'
    )
    comms.append(
        {
            "commitment_id": COMM,
            "title": "WZC Foyer De Lork Hoeselt YE2025 leftover dual (bruto JUMP 785k / omzet empty / equity NEG)",
            "entity_id": ENTITY,
            "beneficiary": "Care Property / Foyer De Lork Hoeselt RE lease path (Schoten zetel; Hoeselt name)",
            "legal_basis": "BV RE lease (KBO 0755.822.317; Actief; 1 VE; NACE 68.201; board Care Property 0456.378.070)",
            "decision_date": "2026-06-13",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(PRIMARY),
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0755822317",
            "stated_goal": "Residential care RE lease / Care Property SPV (Hoeselt-named)",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose omzet behind bruto JUMP; related-party vs Care Property + Foyer De Lork VZW",
            "source_id": "src_lork_hoeselt_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Schoten>LorkHoeselt>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; bruto primary (omzet empty); assets/debt Unknown; preferred AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Anima stack/Foyer De Lork VZW Geel"
            ),
        }
    )
write_csv(DATA / "commitments.csv", comms, ch)

lbs, lh = read_csv(DATA / "leaderboard.csv")
if not any(r["item_id"] == LB for r in lbs):
    lbs.append(
        {
            "item_id": LB,
            "name": "WZC Foyer De Lork Hoeselt bruto JUMP 785k / omzet empty / equity NEG (YE2025)",
            "level": "L5",
            "type": "wzc_re_bv_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Schoten>LorkHoeselt>JR2025",
            "annual_cost_eur": str(PRIMARY),
            "total_cost_eur": str(PRIMARY),
            "tco_notes": (
                f"CW bruto envelope 785k (omzet empty) / FTE 0 / equity NEG -126k; pnl DEEPER LOSS; "
                f"Care Property board; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": "src_lork_hoeselt_jr2025_cw_en",
            "beneficiaries": "Care Property / Foyer De Lork Hoeselt RE path",
            "stated_goal": "Care RE lease SPV (Hoeselt-named / Schoten zetel)",
            "measured_outcome": "bruto JUMP from NEG; pnl DEEPER LOSS -87k; equity NEG -126k; omzet unpublished; FTE 0",
            "absurdity_score": "5.8",
            "cost_score": "3.5",
            "difficulty": "3.5",
            "priority_index": "4.8",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose omzet + Care Property related-party lease matrix",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; DISTINCT Foyer De Lork VZW",
        }
    )
write_csv(DATA / "leaderboard.csv", lbs, lh)

foi, fh = read_csv(DATA / "foi_queue.csv")
if not any(r["gap_id"] == GAP for r in foi):
    foi.append(
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Schoten>LorkHoeselt>NBB_PDF_assets_debt_omzet_empty_bruto_jump",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); omzet/code70 behind bruto 785k; "
                "related-party lease vs Care Property 0456.378.070 + Foyer De Lork VZW; equity NEG recon"
            ),
            "why_it_matters": (
                "Medium CW shows Care Property BV WZC-RE SPV with empty omzet + bruto JUMP 785k + equity NEG — "
                "same opacity class as other empty-omzet care RE; no balanstotaal published"
            ),
            "priority": "8",
            "recipient_body": "WZC Foyer De Lork Hoeselt BV / Care Property Invest",
            "recipient_email": "info@carepropertyinvest.be",
            "recipient_postal": "Horstebaan 3, 2900 Schoten",
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
            "leftover dual — WZC Foyer De Lork Hoeselt YE2025 Medium (bruto JUMP 785k / omzet empty / equity NEG)"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "Completed leftover Lork Hoeselt BV after Anima hold; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; "
            "Medium CW YE2025 + Strong KBO; FOI ready not sent"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK} Lork Hoeselt Medium bruto JUMP {BRUTO} omzet empty pnl DEEPER LOSS {PNL} equity NEG {EQUITY} "
            f"FTE 0; KBO Actief BV NACE 68.201 Care Property board; FOI info@carepropertyinvest.be; next every-10 2170"
        )
if not any(r["task_id"] == NEXT_RQ for r in rq):
    rq.append(
        {
            "task_id": NEXT_RQ,
            "title": "leftover dual hole-fill after Lork Hoeselt — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2169 after Lork Hoeselt YE2025 Medium (bruto JUMP 785k / omzet empty / equity NEG). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo Lork Hoeselt/Anima hold/Avondvrede/Anima Vlaanderen/"
                "t Hofke/Zorg-Saam/Sint-Bernardus De Panne/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork VZW/"
                "IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/"
                "Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick2168 Lork Hoeselt; FARO/AIESH/REW still YE2024; next every-10 2170",
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
            f"tick{TICK} leftover Lork Hoeselt BV 0755.822.317 Medium (bruto JUMP 785k; omzet empty; "
            f"pnl DEEPER LOSS -87k; equity NEG -126k; FTE 0; Care Property board); AGB Bornem JR2024; "
            f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2170; continuous hole_fill"
        )
write_csv(DATA / "loop_state.csv", state_rows, sth)
print("DONE tick", TICK)

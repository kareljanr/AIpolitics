# -*- coding: utf-8 -*-
"""Apply tick 1711 CSV writes for Welzijnszorg vzw NBB YE2024 (deposit 2025-00186633)."""
import csv
from pathlib import Path

DOGE = Path(__file__).resolve().parents[2]
DATA = DOGE / "data"
csv.field_size_limit(10**7)

TS = "2026-08-23T19:45:00Z"
DAY = "2026-08-23"
EID = "vzw_welzijnszorg"
SRC = "src_welzijnszorg_nbb_2025_00186633"
CDN = "http://cdn.staatsbladmonitor.be/2025pdf/2025-00186633.pdf"
GAP = "gap_welzijnszorg_code73_2_57m_staff_1_51m_subsidy_split_l5"
LB = "lb_welzijnszorg_code73_2_57m_assets_3_94m_loss_0_23m"
COMM = "comm_welzijnszorg_jr2024_code73"
HP = "Belgie>Welzijn>Welzijnszorg>JR2024_L5"


def append_rows(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in existing:
            w.writerow(row)
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})
    return len(existing) + len(rows)


def update_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        rows = list(r)
    for row in rows:
        if row["task_id"] == "rq_1711":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["entity_id"] = EID
            row["blocked_gap_id"] = GAP
            row["instructions"] = (
                "Tick 1711 after 1710 PlayRight EVERY-10. Next every-10 is 1720. DONE "
                "Welzijnszorg vzw YE2024 NBB. Do NOT redo Welzijnszorg/PlayRight/SIMIM/"
                "Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/BlauweCluster/Flux50...."
            )
            row["notes"] = (
                "DONE tick1711: Welzijnszorg YE2024 assets 3940326 code73 2570346 staff "
                f"1514311 vte 20.4 pnl -233961; FOI {GAP}; deposit 2025-00186633; "
                "KBO 0416.426.839"
            )
    spawn = {
        "task_id": "rq_1712",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Tick 1712 after 1711 Welzijnszorg YE2024. Next every-10 is 1720. SBM HTML "
            "IP-blacklisted — prefer direct CDN / NBB / official org PDFs / Northdata "
            "deposit→CDN. Do NOT redo Welzijnszorg/PlayRight/SIMIM/Reprobel/Auvibel/"
            "Sabam/NSZ/FBM/Biovia/Medvia/BlauweCluster/Flux50/Catalisti/FlandersFOOD/"
            "Avansa*...."
            " Prefer leftover AGB/APB if PDF live else Natuurpunt vzw if CDN / "
            "NSZ 2026-00394221 if CDN 200 / Bosgroep/Dijk92 if JR euros / FARO if JR2025 / "
            "APEFE if JR euros / SOFAM/GO!/POV/BVAS/IOED/HVZ/IGS/other."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": (
            "spawned after tick1711 Welzijnszorg; NEXT AGB/NatuurpuntVZW/NSZ-if-200/"
            "Bosgroep/Dijk92/FARO/APEFE/SOFAM/GO!/POV/BVAS/IOED/HVZ/IGS; "
            "Welzijnszorg+PlayRight+SIMIM+Reprobel DONE; next every-10 1720"
        ),
    }
    rows.append(spawn)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def update_loop_state():
    path = DATA / "loop_state.csv"
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        rows = list(r)
    notes = (
        "tick1711 leftover Welzijnszorg vzw armoedebestrijding residual; KBO "
        "0416.426.839; official NBB VKT-VZW deposit 2025-00186633 CDN 200 (AV "
        "22.03.2025 YE2024); sourced euros assets 3940326 equity 2583248 debt 1357079 "
        "code73 2570346 staff 1514311 diensten 1730346 bruto 1206379 expl -244632 pnl "
        "-233961 VTE 20.4 beleg 1912998 cash 1050293; FOI ready subsidy/gift split; "
        "NSZ still CDN 403; Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight FOI still "
        "ready; Natuurpunt opaque; Dijk92 CDN 403; FARO no JR2025; APEFE RA2023; SOFAM "
        "JR2025 docx+transparantie live unused; NOT every-10 (next 1720); next rq_1712 "
        "AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/FARO/APEFE/SOFAM/GO!/POV/BVAS/"
        "IOED/HVZ/IGS/other; continuous hole_fill"
    )
    for row in rows:
        if row.get("state_id") == "main":
            row["mode"] = "continuous"
            row["current_sprint"] = "hole_fill"
            row["last_tick_utc"] = TS
            row["last_unit_id"] = "rq_1711"
            row["ticks_completed"] = "1711"
            row["paused"] = "no"
            row["notes"] = notes
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow(row)


entity = {
    "entity_id": EID,
    "name_nl": (
        "Welzijnszorg vzw / armoedebestrijding en solidair welzijnswerk (leftover "
        "national poverty NGO; NOT Welzijnszorg Kempen)"
    ),
    "name_fr": "Welzijnszorg asbl / lutte contre la pauvrete (residuelle nationale)",
    "name_en": "Welzijnszorg leftover Belgian national anti-poverty NGO",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.welzijnszorg.be",
    "foi_email": "koen.trappeniers@welzijnszorg.be",
    "foi_postal": "Huidevettersstraat 165 1000 Brussel",
    "notes": (
        "tick1711 leftover Welzijnszorg after PlayRight/AGB/NSZ hunt; NBB VKT-VZW "
        "2025-00186633 live; KBO 0416.426.839; FOI code73 gift/subsidy split"
    ),
}
n_ent = append_rows(DATA / "entities.csv", [entity])

sources = [
    {
        "source_id": SRC,
        "title": "Welzijnszorg NBB VKT-VZW YE2024 deposit 2025-00186633 (tick1711)",
        "url": CDN,
        "publisher": "NBB CBSO / Welzijnszorg vzw",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1711; CDN 200; AV 22.03.2025; assets 3940326; code73 2570346; staff "
            "1514311 VTE 20.4; pnl -233961; filed ~26.06.2025"
        ),
    },
    {
        "source_id": "src_welzijnszorg_kbo_0416426839_1711",
        "title": "KBO Public Search Welzijnszorg VZW 0416.426.839 (tick1711)",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl"
            "&ondernemingsnummer=416426839"
        ),
        "publisher": "FPS Economy KBO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": "tick1711; Huidevettersstraat 165 1000 Brussel; VZW",
    },
    {
        "source_id": "src_welzijnszorg_nbb_consult_0416426839_1711",
        "title": "NBB consult enterprise Welzijnszorg 0416.426.839 (tick1711)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0416426839",
        "publisher": "NBB CBSO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": "tick1711; deposit 2025-00186633",
    },
    {
        "source_id": "src_welzijnszorg_foi_contact_1711",
        "title": "Welzijnszorg FOI channel (koen.trappeniers@welzijnszorg.be)",
        "url": "https://www.welzijnszorg.be",
        "publisher": "Welzijnszorg",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": (
            "tick1711; email from NBB filing; Huidevettersstraat 165 1000 Brussel"
        ),
    },
]
n_src = append_rows(DATA / "sources.csv", sources)


def bud(bid, amount, notes):
    return {
        "budget_id": bid,
        "entity_id": EID,
        "year": "2024",
        "amount_eur": str(amount),
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": SRC,
        "confidence": "strong",
        "notes": notes,
    }


budgets = [
    bud("bud_welzijnszorg_assets_2024", 3940326, "NBB 20/58 3940326; tick1711"),
    bud("bud_welzijnszorg_va_2024", 130397, "NBB VA 130397 (MVA 7775 + FVA 122622); tick1711"),
    bud("bud_welzijnszorg_vlottend_2024", 3809930, "NBB vlottend 3809930; tick1711"),
    bud("bud_welzijnszorg_beleg_2024", 1912998, "NBB geldbeleggingen 1912998; tick1711"),
    bud("bud_welzijnszorg_cash_2024", 1050293, "NBB liquide middelen 1050293; tick1711"),
    bud("bud_welzijnszorg_equity_2024", 2583248, "NBB eigen vermogen 2583248; tick1711"),
    bud("bud_welzijnszorg_debt_2024", 1357079, "NBB schulden 1357079; tick1711"),
    bud(
        "bud_welzijnszorg_code73_2024",
        2570346,
        "NBB lidgeld/schenkingen/legaten/subsidies 73 2570346 ENVELOPE; tick1711",
    ),
    bud("bud_welzijnszorg_omzet_2024", 64408, "NBB omzet 70 64408; tick1711"),
    bud("bud_welzijnszorg_bruto_2024", 1206379, "NBB brutomarge 9900 1206379; tick1711"),
    bud(
        "bud_welzijnszorg_diensten_2024",
        1730346,
        "NBB handelsgoederen/diensten 60/61 1730346; tick1711",
    ),
    bud(
        "bud_welzijnszorg_staff_2024",
        1514311,
        "NBB bezoldigingen 62 1514311 / VTE 20.4; tick1711",
    ),
    bud("bud_welzijnszorg_expl_2024", -244632, "NBB bedrijfsverlies -244632; tick1711"),
    bud("bud_welzijnszorg_pnl_2024", -233961, "NBB verlies boekjaar -233961; tick1711"),
    bud("bud_welzijnszorg_vte_2024", 20.4, "NBB 9087 gemiddeld VTE 20.4 DROP from 22.3; tick1711"),
]
n_bud = append_rows(DATA / "budgets.csv", budgets)

commitment = {
    "commitment_id": COMM,
    "title": (
        "Welzijnszorg YE2024 leftover anti-poverty NGO (code73 2.57m / staff 1.51m / "
        "loss 0.23m)"
    ),
    "entity_id": EID,
    "beneficiary": "Armoedeorganisaties / Welzijnszorg projecten & beweging",
    "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; VL SCW erkenning path",
    "decision_date": "2025-03-22",
    "start_year": "2024",
    "end_year": "2024",
    "total_envelope_eur": "2570346",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": CDN,
    "stated_goal": (
        "Local leftover Welzijnszorg map — official YE2024 code73 2.57m; FOI gift/"
        "subsidy split"
    ),
    "cut_option": (
        "Publish gift vs public-subsidy split of code73; scrutinise staff 1.51m vs "
        "project pass-through; do not treat donor gifts as waste"
    ),
    "source_id": SRC,
    "confidence": "strong",
    "hierarchy_path": HP,
    "notes": (
        "tick1711; YE2024; code73 2570346 staff 1514311 VTE 20.4 assets 3.94m loss "
        "0.23m; not TE-additive of 348bn; ~85% gift-dependent per org claims — FOI "
        "to pin public share"
    ),
}
n_comm = append_rows(DATA / "commitments.csv", [commitment])

leaderboard = {
    "item_id": LB,
    "name": (
        "Welzijnszorg YE2024 leftover anti-poverty NGO: code73 2.57m / assets 3.94m / "
        "loss 0.23m"
    ),
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": HP,
    "annual_cost_eur": "2570346",
    "total_cost_eur": "3940326",
    "tco_notes": (
        "Leftover Welzijnszorg VZW anti-poverty NGO YE2024: code73 gifts/subsidies "
        "2.57m (ops envelope) / staff 1.51m 20.4 VTE / diensten 1.73m / bruto 1.21m / "
        "bedrijfsverlies -0.24m / pnl -0.23m; assets 3.94m (beleg 1.91m + cash 1.05m); "
        "equity 2.58m; NOT pure waste — scrutinise public-subsidy share vs gifts; FOI "
        "code73 split"
    ),
    "confidence": "strong",
    "source_id": SRC,
    "beneficiaries": "Armoedeorganisaties / project partners / bewegingswerk",
    "stated_goal": "Local leftover Welzijnszorg map — official NBB YE2024 live",
    "measured_outcome": (
        "Official Welzijnszorg NBB 2026-08-23: code73 2570346 / staff 1514311 VTE 20.4 "
        "/ assets 3940326 / pnl -233961"
    ),
    "absurdity_score": "4.0",
    "cost_score": "4.0",
    "difficulty": "3.0",
    "priority_index": "3.9",
    "cut_proposal": (
        "Do not treat donor gifts as waste; publish public-subsidy share of code73; "
        "scrutinise staff 1.51m vs project outflows"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1711; leftover after AGB unpublished / NSZ CDN403 / PlayRight done; not "
        "TE-additive of 348bn; charity/NGO — understate waste claim"
    ),
}
n_lb = append_rows(DATA / "leaderboard.csv", [leaderboard])

foi = {
    "gap_id": GAP,
    "hierarchy_path": HP,
    "entity_id": EID,
    "what_is_missing": (
        "Official YE2024 NBB publishes code73 2570346 / staff 1514311 VTE 20.4 / assets "
        "3940326 / pnl -233961; split of code73 into public subsidies vs private gifts/"
        "legacies Unknown; project pass-through vs overhead Unknown"
    ),
    "why_it_matters": (
        "Leftover national anti-poverty NGO with live NBB euros (2.57m code73 / 1.51m "
        "staff) — need gift vs public-subsidy split before any waste claim"
    ),
    "priority": "6",
    "recipient_body": "Welzijnszorg vzw / Bestuursorgaan",
    "recipient_email": "koen.trappeniers@welzijnszorg.be",
    "recipient_postal": "Huidevettersstraat 165 1000 Brussel",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": DAY,
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": TS,
    "updated_utc": TS,
    "notes": (
        "tick1711; human-send only; NSZ/Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight "
        "FOI still ready"
    ),
}
n_foi = append_rows(DATA / "foi_queue.csv", [foi])

update_queue()
update_loop_state()

print(
    f"tick1711 applied entities={n_ent} sources={n_src} budgets={n_bud} "
    f"commitments={n_comm} leaderboard={n_lb} foi={n_foi}"
)

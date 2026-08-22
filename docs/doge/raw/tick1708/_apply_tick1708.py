# -*- coding: utf-8 -*-
"""Apply tick 1708 CSV writes for Reprobel CV Jaarverslag 2025 (official org PDF)."""
import csv
from pathlib import Path

DOGE = Path(__file__).resolve().parents[2]
DATA = DOGE / "data"
csv.field_size_limit(10**7)

TS = "2026-08-23T18:45:00Z"
DAY = "2026-08-23"
EID = "cv_reprobel"
SRC = "src_reprobel_jv2025_official"
AR_URL = "https://www.reprobel.be/wp-content/uploads/2026/05/jaarverslag-2025-NL.pdf"
GAP = "gap_reprobel_commissions_1_97m_staff_1_23m_rechten_debt_20m_l5"
LB = "lb_reprobel_commissions_1_97m_inningen_29m_rechten_debt_20m"
COMM = "comm_reprobel_jv2025_commissions"
HP = "Belgie>Cultuur>Reprobel>JV2025_L5"


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
        if row["task_id"] == "rq_1708":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["entity_id"] = EID
            row["blocked_gap_id"] = GAP
            row["instructions"] = (
                "Tick 1708 after 1707 Auvibel. Next every-10 is 1710. DONE Reprobel CV "
                "JV2025 official. Do NOT redo Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/"
                "BlauweCluster/Flux50/Catalisti/FlandersFOOD/Avansa*...."
            )
            row["notes"] = (
                "DONE tick1708: Reprobel JV2025 equity 21000 VA 29694 commissions "
                "1965217 staff 1230803 vte 12.6 inningen 29453863 rechten debt "
                f"19878174; FOI {GAP}; KBO 0453.088.681"
            )
    spawn = {
        "task_id": "rq_1709",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Tick 1709 after 1708 Reprobel JV2025. Next every-10 is 1710. SBM HTML "
            "IP-blacklisted — prefer direct CDN / NBB / official org PDFs / Northdata "
            "deposit→CDN. Do NOT redo Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/Medvia/"
            "BlauweCluster/Flux50/Catalisti/FlandersFOOD/Avansa*...."
            " Prefer leftover AGB/APB if PDF live else Natuurpunt vzw if CDN / "
            "NSZ 2026-00394221 if CDN 200 / Bosgroep/Dijk92 if JR euros / FARO if JR2025 / "
            "APEFE if JR euros / PlayRight/SIMIM/Welzijnszorg/GO!/POV/BVAS/IOED/"
            "HVZ/IGS/other."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": (
            "spawned after tick1708 Reprobel JV2025; NEXT AGB/NatuurpuntVZW/NSZ-if-200/"
            "Bosgroep/Dijk92/FARO/APEFE/PlayRight/SIMIM/Welzijnszorg/GO!/POV/BVAS/"
            "IOED/HVZ/IGS; Reprobel+Auvibel+Sabam+FBM+Flux50 DONE; next every-10 1710"
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
        "tick1708 leftover Reprobel CV reprografie/authors collecting society residual; "
        "KBO 0453.088.681; official Reprobel Jaarverslag 2025 PDF live reprobel.be "
        "(AV/definitieve terbeschikkingstelling mei 2026); sourced euros equity 21000 "
        "VA 29694 beleg 15803646 cash 2204525 own ST recv 1139013 rechten recv 777399 "
        "own ST debt 381658 rechten debt 19878174 commissions 1965217 staff 1230803 "
        "diensten 1051445 costs/opbr 2590195 facturatie base 29571278 inningen "
        "29453863 werkingskostenratio 6.65% VTE 12.6; FOI ready NBB CDN deposit; "
        "NSZ still CDN 403; Blauwe/Sabam/Auvibel FOI still ready; Natuurpunt opaque; "
        "Dijk92 CDN 403; FARO no JR2025; APEFE RA2023; NOT every-10 (next 1710); next "
        "rq_1709 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/FARO/APEFE/PlayRight/"
        "SIMIM/Welzijnszorg/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill"
    )
    for row in rows:
        if row.get("state_id") == "main":
            row["mode"] = "continuous"
            row["current_sprint"] = "hole_fill"
            row["last_tick_utc"] = TS
            row["last_unit_id"] = "rq_1708"
            row["ticks_completed"] = "1708"
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
        "Reprobel cv / Collectieve beheersvennootschap reprografie en auteursrechten "
        "(leftover texts/images collecting CV; NOT Sabam / Auvibel / PlayRight)"
    ),
    "name_fr": (
        "Reprobel sc / Societe de gestion collective reprographie et droits d'auteur "
        "(residuelle)"
    ),
    "name_en": (
        "Reprobel leftover Belgian reprography and text/image rights collecting "
        "cooperative"
    ),
    "level": "other",
    "parent_id": "sec_federal",
    "community_language": "nl",
    "website": "https://www.reprobel.be",
    "foi_email": "licensing@reprobel.be",
    "foi_postal": "Havenlaan 86c-201a 1000 Brussel",
    "notes": (
        "tick1708 leftover Reprobel after Auvibel/Sabam/NSZ/AGB hunt; official JV2025 "
        "live; KBO 0453.088.681; fiduciary rights-heavy; FOI NBB CDN deposit; shared "
        "Tour & Taxis address with Auvibel"
    ),
}
n_ent = append_rows(DATA / "entities.csv", [entity])

sources = [
    {
        "source_id": SRC,
        "title": "Reprobel Official Jaarverslag 2025 NL (tick1708)",
        "url": AR_URL,
        "publisher": "Reprobel cv",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1708; official org PDF ~67p; AV/definitieve terbeschikkingstelling "
            "mei 2026; equity 21000; commissions 1965217; staff 1230803 VTE 12.6; "
            "inningen 29453863; rechten debt 19878174; werkingskostenratio 6.65%"
        ),
    },
    {
        "source_id": "src_reprobel_kbo_0453088681_1708",
        "title": "KBO Public Search Reprobel CV 0453.088.681 (tick1708)",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl"
            "&ondernemingsnummer=453088681"
        ),
        "publisher": "FPS Economy KBO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": "tick1708; Havenlaan 86c-201a 1000 Brussel; CV; BTW BE 0453.088.681",
    },
    {
        "source_id": "src_reprobel_nbb_consult_0453088681_1708",
        "title": "NBB consult enterprise Reprobel 0453.088.681 (tick1708)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0453088681",
        "publisher": "NBB CBSO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": "tick1708; CDN deposit id for 2025 filing still opaque; FOI residual",
    },
    {
        "source_id": "src_reprobel_foi_contact_1708",
        "title": "Reprobel FOI channel (licensing@reprobel.be)",
        "url": "https://www.reprobel.be/alles-over-reprobel/",
        "publisher": "Reprobel",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": (
            "tick1708; Havenlaan 86c-201a 1000 Brussel; licensing@reprobel.be; VTE "
            "12.6 stated on site"
        ),
    },
]
n_src = append_rows(DATA / "sources.csv", sources)


def bud(bid, amount, notes):
    return {
        "budget_id": bid,
        "entity_id": EID,
        "year": "2025",
        "amount_eur": str(amount),
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": SRC,
        "confidence": "strong",
        "notes": notes,
    }


budgets = [
    bud("bud_reprobel_equity_2025", 21000, "JV2025 eigen vermogen 21000 flat; tick1708"),
    bud(
        "bud_reprobel_va_2025",
        29694,
        "JV2025 vaste activa 29694 DROP (IVA 14750 + MVA 14941); tick1708",
    ),
    bud(
        "bud_reprobel_own_st_recv_2025",
        1139013,
        "JV2025 eigen-activiteit KT vorderingen 1139013 DROP (incl handels + BTW); "
        "tick1708",
    ),
    bud(
        "bud_reprobel_handelsrecv_2025",
        226858,
        "JV2025 handelsvorderingen eigen 226858 JUMP (incl op te stellen facturen "
        "154493 onderwijs commissies); tick1708",
    ),
    bud(
        "bud_reprobel_btw_recv_2025",
        912155,
        "JV2025 BTW te ontvangen 912155 (na 4.4m terugvordering 2025); tick1708",
    ),
    bud(
        "bud_reprobel_beleg_2025",
        15803646,
        "JV2025 geldbeleggingen 15803646 JUMP from 12277192; tick1708",
    ),
    bud(
        "bud_reprobel_cash_2025",
        2204525,
        "JV2025 liquide middelen/banktegoeden 2204525 DROP from 2441912; tick1708",
    ),
    bud(
        "bud_reprobel_rechten_recv_2025",
        777399,
        "JV2025 vorderingen rechten IX.Bis 777399; tick1708",
    ),
    bud(
        "bud_reprobel_own_st_debt_2025",
        381658,
        "JV2025 schulden <=1j eigen 381658 (leveranciers 193204 + belasting/sociale "
        "188454); tick1708",
    ),
    bud(
        "bud_reprobel_rechten_debt_2025",
        19878174,
        "JV2025 schulden rechten 19878174 (afwachting inning 768845 + te verdelen "
        "niet-voorbeh 14279605 + voorbeh 772980 + afwachting betaling 1056744 + "
        "other fiduciary components); tick1708",
    ),
    bud(
        "bud_reprobel_rechten_te_verdelen_2025",
        15052585,
        "JV2025 te verdelen geïnde rechten 14279605+772980=15052585; tick1708",
    ),
    bud(
        "bud_reprobel_commissions_2025",
        1965217,
        "JV2025 omzet/commissies 1965217 DROP ENVELOPE; tick1708",
    ),
    bud(
        "bud_reprobel_staff_2025",
        1230803,
        "JV2025 bezoldigingen 62 1230803 / VTE 12.6; tick1708",
    ),
    bud(
        "bud_reprobel_diensten_2025",
        1051445,
        "JV2025 diensten en diverse goederen 61 1051445; tick1708",
    ),
    bud(
        "bud_reprobel_costs_opbr_2025",
        2590195,
        "JV2025 kosten=opbrengsten 2590195 (pnl 0 collecting society); tick1708",
    ),
    bud("bud_reprobel_pnl_2025", 0, "JV2025 te bestemmen resultaat 0; tick1708"),
    bud(
        "bud_reprobel_vte_2025",
        12.6,
        "JV2025/site team 12.6 VTE einde boekjaar; tick1708",
    ),
    bud(
        "bud_reprobel_facturatie_base_2025",
        29571278,
        "JV2025 facturatie/ratio base 29571278 (werkingskostenratio 6.65%); tick1708",
    ),
    bud(
        "bud_reprobel_inningen_2025",
        29453863,
        "JV2025 totale inningen 29453863; tick1708",
    ),
    bud(
        "bud_reprobel_werkingskostenratio_pct_2025",
        6.65,
        "JV2025 netto werkingskostenratio 6.65% (commissions/facturatie); tick1708",
    ),
]
n_bud = append_rows(DATA / "budgets.csv", budgets)

commitment = {
    "commitment_id": COMM,
    "title": (
        "Reprobel JV2025 leftover reprografie collecting society (commissions 1.97m / "
        "inningen 29.5m / rechten debt 20m)"
    ),
    "entity_id": EID,
    "beneficiary": "Reprobel member CMOs / authors-publishers (texts/images)",
    "legal_basis": "WVV CV; WER XI reprografie/onderwijs; Bestuursdecreet openbaarheid",
    "decision_date": "2026-05-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1965217",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": AR_URL,
    "stated_goal": (
        "Local leftover Reprobel map — official JV2025 commissions 1.97m; FOI NBB CDN"
    ),
    "cut_option": (
        "Publish NBB CDN deposit + commission path vs 29.5m inningen; do not treat "
        "rechten debt as waste"
    ),
    "source_id": SRC,
    "confidence": "strong",
    "hierarchy_path": HP,
    "notes": (
        "tick1708; JV YE2025; commissions 1965217 staff 1230803 VTE 12.6 inningen "
        "29.5m rechten fiduciary ~19.9m debt; not TE-additive of 348bn"
    ),
}
n_comm = append_rows(DATA / "commitments.csv", [commitment])

leaderboard = {
    "item_id": LB,
    "name": (
        "Reprobel JV2025 leftover reprografie collecting society: commissions 1.97m / "
        "inningen 29m / rechten debt 20m"
    ),
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": HP,
    "annual_cost_eur": "1965217",
    "total_cost_eur": "19878174",
    "tco_notes": (
        "Leftover Reprobel CV reprografie/text-image CMO JV2025: commissions/omzet "
        "1.97m (ops envelope) / staff 1.23m 12.6 VTE / diensten 1.05m / costs=opbr "
        "2.59m / pnl 0; equity only 21k; balance dominated by authors-rights "
        "fiduciary debt 19.9m + beleggingen 15.8m (NOT Reprobel free cash); inningen "
        "29.5m / facturatie base 29.6m / werkingskostenratio 6.65%; peer of "
        "Sabam/Auvibel; NBB CDN deposit residual FOI; full balanstotaal not stated "
        "as single figure in narrative"
    ),
    "confidence": "strong",
    "source_id": SRC,
    "beneficiaries": "Auteurs/uitgevers via 15 national member CMOs",
    "stated_goal": "Local leftover Reprobel map — official JV2025 live",
    "measured_outcome": (
        "Official Reprobel JV2025 2026-08-23: commissions 1965217 / staff 1230803 VTE "
        "12.6 / inningen 29453863 / rechten debt 19878174 / equity 21000"
    ),
    "absurdity_score": "5.0",
    "cost_score": "4.0",
    "difficulty": "2.5",
    "priority_index": "4.4",
    "cut_proposal": (
        "Do not treat rechten debt 20m as waste; scrutinise commissions 1.97m vs "
        "diensten 1.05m / OPERA ERP; publish NBB CDN deposit id"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1708; leftover after AGB unpublished / NSZ CDN403 / Auvibel+Sabam done; "
        "not TE-additive of 348bn; fiduciary rights off pure-waste filter"
    ),
}
n_lb = append_rows(DATA / "leaderboard.csv", [leaderboard])

foi = {
    "gap_id": GAP,
    "hierarchy_path": HP,
    "entity_id": EID,
    "what_is_missing": (
        "Official JV2025 publishes commissions 1965217 / staff 1230803 VTE 12.6 / "
        "inningen 29453863 / rechten debt 19878174 / equity 21000; NBB CDN deposit "
        "reference for 2025 neerlegging Unknown; full statutory balanstotaal as single "
        "filed figure Unknown"
    ),
    "why_it_matters": (
        "Leftover Belgian reprografie collecting society with live official JV euros "
        "(1.97m commissions / 29.5m inningen / 20m rights fiduciary) — need CDN "
        "deposit pointer to reconcile management JV vs NBB statutory"
    ),
    "priority": "7",
    "recipient_body": "Reprobel cv / Bestuursorgaan",
    "recipient_email": "licensing@reprobel.be",
    "recipient_postal": "Havenlaan 86c-201a 1000 Brussel",
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
    "notes": "tick1708; human-send only; NSZ/Blauwe/Sabam/Auvibel FOI still ready",
}
n_foi = append_rows(DATA / "foi_queue.csv", [foi])

update_queue()
update_loop_state()

print(
    f"tick1708 applied entities={n_ent} sources={n_src} budgets={n_bud} "
    f"commitments={n_comm} leaderboard={n_lb} foi={n_foi}"
)

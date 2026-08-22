# -*- coding: utf-8 -*-
"""Apply tick 1712 CSV writes for SOFAM CV Jaarverslag/Transparantie 2025."""
import csv
from pathlib import Path

DOGE = Path(__file__).resolve().parents[2]
DATA = DOGE / "data"
csv.field_size_limit(10**7)

TS = "2026-08-23T20:05:00Z"
DAY = "2026-08-23"
EID = "cv_sofam"
SRC = "src_sofam_jv2025_official"
JV_URL = "https://www.sofam.be/dbfiles/mfile/2200/2204/JAARRAPPORT_SOFAM_2025_NL.docx"
TR_URL = "https://www.sofam.be/dbfiles/mfile/2200/2203/Transparantieverslag_2025.pdf"
GAP = "gap_sofam_commissions_0_83m_staff_0_54m_rechten_debt_5_7m_vte_l5"
LB = "lb_sofam_commissions_0_83m_inningen_4_2m_rechten_debt_5_7m"
COMM = "comm_sofam_jv2025_commissions"
HP = "Belgie>Cultuur>SOFAM>JV2025_L5"


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
        if row["task_id"] == "rq_1712":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["entity_id"] = EID
            row["blocked_gap_id"] = GAP
            row["instructions"] = (
                "Tick 1712 after 1711 Welzijnszorg. Next every-10 is 1720. DONE SOFAM "
                "CV JV2025+transparantie. Do NOT redo SOFAM/Welzijnszorg/PlayRight/"
                "SIMIM/Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/BlauweCluster/Flux50...."
            )
            row["notes"] = (
                "DONE tick1712: SOFAM YE2025 assets 6943084 commissions 830398 staff "
                f"538095 inningen 4204681 rechten debt 5736098; FOI {GAP}; "
                "KBO 0419.415.330"
            )
    spawn = {
        "task_id": "rq_1713",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Tick 1713 after 1712 SOFAM JV2025. Next every-10 is 1720. SBM HTML "
            "IP-blacklisted — prefer direct CDN / NBB / official org PDFs / Northdata "
            "deposit→CDN. Do NOT redo SOFAM/Welzijnszorg/PlayRight/SIMIM/Reprobel/"
            "Auvibel/Sabam/NSZ/FBM/Biovia/Medvia/BlauweCluster/Flux50/Catalisti/"
            "FlandersFOOD/Avansa*...."
            " Prefer leftover AGB/APB if PDF live else Natuurpunt vzw if CDN / "
            "NSZ 2026-00394221 if CDN 200 / Bosgroep/Dijk92 if JR euros / FARO if JR2025 / "
            "APEFE if JR euros / GO!/POV/BVAS/IOED/HVZ/IGS/other."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": (
            "spawned after tick1712 SOFAM; NEXT AGB/NatuurpuntVZW/NSZ-if-200/"
            "Bosgroep/Dijk92/FARO/APEFE/GO!/POV/BVAS/IOED/HVZ/IGS; "
            "SOFAM+Welzijnszorg+PlayRight+SIMIM+Reprobel DONE; next every-10 1720"
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
        "tick1712 leftover SOFAM CV visual-arts authors collecting society residual; "
        "KBO 0419.415.330; official Jaarrapport 2025 DOCX + Transparantieverslag 2025 "
        "PDF live sofam.be (AV 18.05.2026); sourced euros assets 6943084 equity 468830 "
        "debt 6474254 rechten debt 5736098 commissions 830398 staff 538095 diensten "
        "464044 inningen 4204681 beheers_A 1183446 nettokosten 816121 pnl 6287 VTE "
        "Unknown; FOI ready VTE/NBB CDN; NSZ still CDN 403; Blauwe/Sabam/Auvibel/"
        "Reprobel/SIMIM/PlayRight/Welzijnszorg FOI still ready; Natuurpunt opaque; "
        "Dijk92 CDN 403; FARO no JR2025; APEFE RA2023; NOT every-10 (next 1720); next "
        "rq_1713 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/FARO/APEFE/GO!/POV/"
        "BVAS/IOED/HVZ/IGS/other; continuous hole_fill"
    )
    for row in rows:
        if row.get("state_id") == "main":
            row["mode"] = "continuous"
            row["current_sprint"] = "hole_fill"
            row["last_tick_utc"] = TS
            row["last_unit_id"] = "rq_1712"
            row["ticks_completed"] = "1712"
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
        "SOFAM cv / Multimedia Maatschappij van de Auteurs de Visuele Kunsten "
        "(leftover visual-arts authors collecting CV; NOT Sabam / PlayRight / "
        "Reprobel / Auvibel / SIMIM)"
    ),
    "name_fr": (
        "SOFAM sc / Societe multimedia des auteurs des arts visuels (residuelle)"
    ),
    "name_en": (
        "SOFAM leftover Belgian visual-arts authors collecting cooperative"
    ),
    "level": "other",
    "parent_id": "sec_federal",
    "community_language": "nl",
    "website": "https://www.sofam.be",
    "foi_email": "info@sofam.be",
    "foi_postal": "Koninklijke Prinsstraat 87 1050 Brussel",
    "notes": (
        "tick1712 leftover SOFAM after Welzijnszorg/PlayRight/AGB/NSZ hunt; official "
        "JV2025+transparantie live; KBO 0419.415.330; fiduciary rights-heavy; FOI VTE"
    ),
}
n_ent = append_rows(DATA / "entities.csv", [entity])

sources = [
    {
        "source_id": SRC,
        "title": "SOFAM Official Jaarrapport 2025 NL DOCX (tick1712)",
        "url": JV_URL,
        "publisher": "SOFAM cv",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1712; AV 18.05.2026; YE2025 balans assets 6943084; omzet 830398; "
            "staff 538095; rechten debt 5736098; pnl 6287"
        ),
    },
    {
        "source_id": "src_sofam_transparantie_2025_1712",
        "title": "SOFAM Transparantieverslag 2025 Art.23 (tick1712)",
        "url": TR_URL,
        "publisher": "SOFAM cv",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1712; inningen 4204681; beheers_A 1183446; nettokosten 816121; "
            "ratio 19.41%"
        ),
    },
    {
        "source_id": "src_sofam_kbo_0419415330_1712",
        "title": "KBO Public Search SOFAM CV 0419.415.330 (tick1712)",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl"
            "&ondernemingsnummer=419415330"
        ),
        "publisher": "FPS Economy KBO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": "tick1712; Koninklijke Prinsstraat 87 1050 Brussel; CV; BTW BE 0419.415.330",
    },
    {
        "source_id": "src_sofam_foi_contact_1712",
        "title": "SOFAM FOI channel (info@sofam.be)",
        "url": "https://www.sofam.be/nl/159/0/",
        "publisher": "SOFAM",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick1712; info@sofam.be; +32 2 726 98 00",
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
    bud(
        "bud_sofam_assets_2025",
        6943084,
        "JV2025 VA 322252 + vlottend 6620832 = 6943084; tick1712",
    ),
    bud("bud_sofam_va_2025", 322252, "JV2025 vaste activa 322252; tick1712"),
    bud("bud_sofam_vlottend_2025", 6620832, "JV2025 vlottende activa 6620832; tick1712"),
    bud("bud_sofam_beleg_2025", 1814151, "JV2025 geldbeleggingen 1814151 DROP; tick1712"),
    bud("bud_sofam_cash_2025", 4716212, "JV2025 liquide middelen 4716212 JUMP; tick1712"),
    bud("bud_sofam_equity_2025", 468830, "JV2025 eigen vermogen 468830; tick1712"),
    bud("bud_sofam_debt_2025", 6474254, "JV2025 schulden 6474254; tick1712"),
    bud(
        "bud_sofam_rechten_debt_2025",
        5736098,
        "JV2025 schulden rechten 5736098 (LT te verdelen gereserveerd 1091525 + ST); "
        "tick1712",
    ),
    bud(
        "bud_sofam_commissions_2025",
        830398,
        "JV2025 omzet/commissies 70 830398 ENVELOPE; tick1712",
    ),
    bud(
        "bud_sofam_opbr_2025",
        838326,
        "JV2025 bedrijfsopbrengsten 70/74 838326; tick1712",
    ),
    bud("bud_sofam_staff_2025", 538095, "JV2025 bezoldigingen 62 538095; tick1712"),
    bud(
        "bud_sofam_diensten_2025",
        464044,
        "JV2025 diensten en diverse goederen 61 464044; tick1712",
    ),
    bud("bud_sofam_expl_2025", -23515, "JV2025 bedrijfswinst/verlies -23515; tick1712"),
    bud("bud_sofam_pnl_2025", 6287, "JV2025 winst boekjaar 6287; tick1712"),
    bud(
        "bud_sofam_inningen_2025",
        4204681,
        "Transparantie/JV2025 totale inningen 4204681; tick1712",
    ),
    bud(
        "bud_sofam_beheers_a_2025",
        1183446,
        "Transparantie DEEL2 A totaal kosten 1183446; tick1712",
    ),
    bud(
        "bud_sofam_nettokosten_2025",
        816121,
        "Transparantie DEEL2 B nettokosten 816121 (ratio 19.41%); tick1712",
    ),
]
n_bud = append_rows(DATA / "budgets.csv", budgets)

commitment = {
    "commitment_id": COMM,
    "title": (
        "SOFAM JV2025 leftover visual-arts collecting society (commissions 0.83m / "
        "inningen 4.2m / rechten debt 5.7m)"
    ),
    "entity_id": EID,
    "beneficiary": "SOFAM member visual artists / authors",
    "legal_basis": "WVV CV; WER XI auteursrechten/volgrecht; Bestuursdecreet openbaarheid",
    "decision_date": "2026-05-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "830398",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": JV_URL,
    "stated_goal": (
        "Local leftover SOFAM map — official JV2025 commissions 0.83m; FOI VTE"
    ),
    "cut_option": (
        "Publish VTE + NBB CDN deposit; do not treat rechten debt 5.7m as waste; "
        "scrutinise nettokosten ratio 19.4%"
    ),
    "source_id": SRC,
    "confidence": "strong",
    "hierarchy_path": HP,
    "notes": (
        "tick1712; YE2025; commissions 830398 staff 538095 assets 6.94m of which "
        "rechten fiduciary ~5.7m debt; inningen 4.2m; not TE-additive of 348bn"
    ),
}
n_comm = append_rows(DATA / "commitments.csv", [commitment])

leaderboard = {
    "item_id": LB,
    "name": (
        "SOFAM JV2025 leftover visual-arts collecting society: commissions 0.83m / "
        "inningen 4.2m / rechten debt 5.7m"
    ),
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": HP,
    "annual_cost_eur": "830398",
    "total_cost_eur": "6943084",
    "tco_notes": (
        "Leftover SOFAM CV visual-arts authors CMO YE2025: commissions/omzet 0.83m "
        "(ops envelope) / staff 0.54m / diensten 0.46m / expl -0.02m / pnl 6.3k; "
        "balance 6.94m dominated by rights fiduciary debt 5.74m + cash 4.72m / beleg "
        "1.81m; inningen 4.20m; beheers_A 1.18m / nettokosten 0.82m ratio 19.4%; peer "
        "of Sabam/PlayRight/Reprobel/Auvibel/SIMIM; VTE residual FOI"
    ),
    "confidence": "strong",
    "source_id": SRC,
    "beneficiaries": "Visuele kunstenaars / authors via SOFAM",
    "stated_goal": "Local leftover SOFAM map — official JV2025+transparantie live",
    "measured_outcome": (
        "Official SOFAM YE2025 2026-08-23: commissions 830398 / staff 538095 / "
        "inningen 4204681 / assets 6943084 / rechten debt 5736098"
    ),
    "absurdity_score": "5.0",
    "cost_score": "3.5",
    "difficulty": "2.5",
    "priority_index": "4.2",
    "cut_proposal": (
        "Do not treat rechten debt 5.7m as waste; scrutinise nettokosten ratio 19.4% "
        "vs peers; publish VTE"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1712; leftover after AGB unpublished / NSZ CDN403 / Welzijnszorg+"
        "PlayRight done; not TE-additive of 348bn"
    ),
}
n_lb = append_rows(DATA / "leaderboard.csv", [leaderboard])

foi = {
    "gap_id": GAP,
    "hierarchy_path": HP,
    "entity_id": EID,
    "what_is_missing": (
        "Official JV2025+transparantie publishes commissions 830398 / staff 538095 / "
        "inningen 4204681 / assets 6943084 / rechten debt 5736098; exact VTE Unknown; "
        "NBB CDN deposit id for YE2025 filing Unknown"
    ),
    "why_it_matters": (
        "Leftover Belgian visual-arts collecting society with live official YE2025 "
        "euros (0.83m commissions / 4.2m inningen / 5.7m rights fiduciary) — need VTE "
        "+ NBB statutory deposit pointer"
    ),
    "priority": "7",
    "recipient_body": "SOFAM cv / Bestuursorgaan",
    "recipient_email": "info@sofam.be",
    "recipient_postal": "Koninklijke Prinsstraat 87 1050 Brussel",
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
        "tick1712; human-send only; NSZ/Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/"
        "Welzijnszorg FOI still ready"
    ),
}
n_foi = append_rows(DATA / "foi_queue.csv", [foi])

update_queue()
update_loop_state()

print(
    f"tick1712 applied entities={n_ent} sources={n_src} budgets={n_bud} "
    f"commitments={n_comm} leaderboard={n_lb} foi={n_foi}"
)

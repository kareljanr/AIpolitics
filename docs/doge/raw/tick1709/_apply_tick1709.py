# -*- coding: utf-8 -*-
"""Apply tick 1709 CSV writes for SIMIM CV Jaarverslag/Art.23 2025 (official org PDF)."""
import csv
from pathlib import Path

DOGE = Path(__file__).resolve().parents[2]
DATA = DOGE / "data"
csv.field_size_limit(10**7)

TS = "2026-08-23T19:05:00Z"
DAY = "2026-08-23"
EID = "cv_simim"
SRC = "src_simim_jv2025_art23_official"
AR_URL = "https://www.simim.be/bedrijf/Jaarverslag_SIMIM_2025.pdf"
GAP = "gap_simim_beheers_3_64m_geinde_32m_nbb_balans_l5"
LB = "lb_simim_beheers_3_64m_geinde_32m_art23_2025"
COMM = "comm_simim_jv2025_beheerskosten"
HP = "Belgie>Cultuur>SIMIM>JV2025_L5"

# Art.23 DEEL2 A (totaal beheerskosten) + DEEL1 A geinde — sourced from official PDF
CATS = [
    ("reproductie", 5407508, 443667, 436321, 8.07),
    ("publieke_mededeling", 275251, 47191, 46410, 16.86),
    ("kabel", 4245335, 222045, 218368, 5.14),
    ("jaarlijkse_aanvullende", 16457204, 2650328, 2610193, 15.94),
    ("leenrecht", 41433, 2212, 2175, 5.25),
    ("thuiskopie", 2540117, 135602, 133356, 5.25),
    ("onderwijs_wetenschap", 36138, 1929, 1897, 5.25),
    ("internationale", 3406541, 136262, 133997, 3.93),
    ("andere", 7247, 1645, 1618, 22.32),
]
GEINDE = sum(c[1] for c in CATS)
BEHEERS_A = sum(c[2] for c in CATS)
BEHEERS_B = sum(c[3] for c in CATS)


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
        if row["task_id"] == "rq_1709":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["entity_id"] = EID
            row["blocked_gap_id"] = GAP
            row["instructions"] = (
                "Tick 1709 after 1708 Reprobel. Next every-10 is 1710. DONE SIMIM CV "
                "JV2025 Art.23 official. Do NOT redo SIMIM/Reprobel/Auvibel/Sabam/NSZ/"
                "FBM/Biovia/BlauweCluster/Flux50/Catalisti/FlandersFOOD/Avansa*...."
            )
            row["notes"] = (
                f"DONE tick1709: SIMIM Art.23 YE2025 geinde {GEINDE} beheers_a "
                f"{BEHEERS_A} beheers_b {BEHEERS_B}; FOI {GAP}; KBO 0455.701.446"
            )
    spawn = {
        "task_id": "rq_1710",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Tick 1710 after 1709 SIMIM Art.23 YE2025. THIS IS EVERY-10 — refresh "
            "progress_every_10_ticks.md + doge_waste_top10_current.md. SBM HTML "
            "IP-blacklisted — prefer direct CDN / NBB / official org PDFs / Northdata "
            "deposit→CDN. Do NOT redo SIMIM/Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/"
            "Medvia/BlauweCluster/Flux50/Catalisti/FlandersFOOD/Avansa*...."
            " Prefer leftover AGB/APB if PDF live else Natuurpunt vzw if CDN / "
            "NSZ 2026-00394221 if CDN 200 / Bosgroep/Dijk92 if JR euros / FARO if JR2025 / "
            "APEFE if JR euros / PlayRight/Welzijnszorg/GO!/POV/BVAS/IOED/HVZ/IGS/other."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": (
            "spawned after tick1709 SIMIM; EVERY-10 tick; NEXT AGB/NatuurpuntVZW/"
            "NSZ-if-200/Bosgroep/Dijk92/FARO/APEFE/PlayRight/Welzijnszorg/GO!/POV/"
            "BVAS/IOED/HVZ/IGS; SIMIM+Reprobel+Auvibel+Sabam DONE"
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
        "tick1709 leftover SIMIM CV muziekindustrie neighbouring-rights collecting "
        f"society residual; KBO 0455.701.446; official Jaarverslag_SIMIM_2025.pdf "
        f"(Art.23 WER transparency) live simim.be; sourced euros geinde {GEINDE} "
        f"beheerskosten_A {BEHEERS_A} beheerskosten_B_incl_fin {BEHEERS_B}; categories "
        "reproductie/publieke/kabel/jaarlijkse/leenrecht/thuiskopie/onderwijs/"
        "internationale/andere; full NBB balanstotaal/statutory JR residual FOI; NSZ "
        "still CDN 403; Blauwe/Sabam/Auvibel/Reprobel FOI still ready; Natuurpunt "
        "opaque; Dijk92 CDN 403; FARO no JR2025; APEFE RA2023; PlayRight only "
        "commissarisverslag YE2024 (no full JV2025 yet); NOT every-10 (next 1710); "
        "next rq_1710 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/FARO/APEFE/"
        "PlayRight/Welzijnszorg/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill"
    )
    for row in rows:
        if row.get("state_id") == "main":
            row["mode"] = "continuous"
            row["current_sprint"] = "hole_fill"
            row["last_tick_utc"] = TS
            row["last_unit_id"] = "rq_1709"
            row["ticks_completed"] = "1709"
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
        "SIMIM cv / Societe de l'Industrie Musicale - Muziekindustrie Maatschappij "
        "(leftover neighbouring-rights collecting CV for phonogram producers; NOT "
        "Sabam / PlayRight / Auvibel / Reprobel)"
    ),
    "name_fr": (
        "SIMIM sc / Societe de l'Industrie Musicale (gestion collective residuelle "
        "droits voisins producteurs)"
    ),
    "name_en": (
        "SIMIM leftover Belgian music-industry neighbouring-rights collecting "
        "cooperative (phonogram producers)"
    ),
    "level": "other",
    "parent_id": "sec_federal",
    "community_language": "nl",
    "website": "https://www.simim.be",
    "foi_email": "info@simim.be",
    "foi_postal": "Lenneke Marelaan 8 bus 5 1932 Zaventem",
    "notes": (
        "tick1709 leftover SIMIM after Reprobel/Auvibel/Sabam/NSZ/AGB hunt; official "
        "Art.23 YE2025 PDF live; KBO 0455.701.446; fiduciary rights-heavy; FOI NBB "
        "statutory balanstotaal"
    ),
}
n_ent = append_rows(DATA / "entities.csv", [entity])

sources = [
    {
        "source_id": SRC,
        "title": "SIMIM Official Jaarverslag / Art.23 transparency 2025 (tick1709)",
        "url": AR_URL,
        "publisher": "SIMIM cv",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            f"tick1709; official org PDF 15p Art.23 WER tables YE2025; geinde "
            f"{GEINDE}; beheers_A {BEHEERS_A}; beheers_B {BEHEERS_B}; no full "
            "balanstotaal in this PDF — FOI NBB"
        ),
    },
    {
        "source_id": "src_simim_rapport_gestion_2024_pointer_1709",
        "title": "SIMIM Rapport de Gestion YE2024 (entity pointer / prior year)",
        "url": "https://www.simim.be/bedrijf/Rapport_De_Gestion_SIMIM_2024.pdf",
        "publisher": "SIMIM cv",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1709 secondary pointer; YE2024 balanstotaal 44176104.88 / frais "
            "gestion 2988683 / dettes droits 42529340.50 / AV 26.06.2025 — NOT used "
            "as YE2025 euros"
        ),
    },
    {
        "source_id": "src_simim_kbo_0455701446_1709",
        "title": "KBO Public Search SIMIM CV 0455.701.446 (tick1709)",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl"
            "&ondernemingsnummer=455701446"
        ),
        "publisher": "FPS Economy KBO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": "tick1709; Lenneke Marelaan 8 bus 5 1932 Zaventem; CV; BTW BE 0455.701.446",
    },
    {
        "source_id": "src_simim_foi_contact_1709",
        "title": "SIMIM FOI channel (info@simim.be)",
        "url": "https://www.simim.be/indexEN.html",
        "publisher": "SIMIM",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick1709; info@simim.be; +32 2 775 82 10",
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
        "bud_simim_geinde_total_2025",
        GEINDE,
        f"Art.23 sum A geinde across 9 categories {GEINDE}; tick1709",
    ),
    bud(
        "bud_simim_beheers_a_total_2025",
        BEHEERS_A,
        f"Art.23 sum DEEL2 A beheerskosten {BEHEERS_A} ENVELOPE; tick1709",
    ),
    bud(
        "bud_simim_beheers_b_total_2025",
        BEHEERS_B,
        f"Art.23 sum DEEL2 B beheerskosten incl fin {BEHEERS_B}; tick1709",
    ),
]
for slug, geinde, ba, bb, ratio in CATS:
    budgets.append(
        bud(
            f"bud_simim_geinde_{slug}_2025",
            geinde,
            f"Art.23 {slug} A geinde {geinde}; tick1709",
        )
    )
    budgets.append(
        bud(
            f"bud_simim_beheers_{slug}_2025",
            ba,
            f"Art.23 {slug} DEEL2 A beheers {ba} (B {bb} ratio {ratio}%); tick1709",
        )
    )

n_bud = append_rows(DATA / "budgets.csv", budgets)

commitment = {
    "commitment_id": COMM,
    "title": (
        "SIMIM Art.23 YE2025 leftover phonogram collecting society (beheers 3.64m / "
        "geinde 32.4m)"
    ),
    "entity_id": EID,
    "beneficiary": "SIMIM member phonogram producers / music industry",
    "legal_basis": "WVV CV; WER XI naburige rechten Art.23; Bestuursdecreet openbaarheid",
    "decision_date": "2026-01-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BEHEERS_A),
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": AR_URL,
    "stated_goal": (
        "Local leftover SIMIM map — official Art.23 YE2025 beheers 3.64m; FOI NBB"
    ),
    "cut_option": (
        "Publish NBB statutory balanstotaal + full JR; do not treat rights geinde as "
        "SIMIM opex waste"
    ),
    "source_id": SRC,
    "confidence": "strong",
    "hierarchy_path": HP,
    "notes": (
        f"tick1709; Art.23 YE2025; beheers_A {BEHEERS_A} geinde {GEINDE}; not "
        "TE-additive of 348bn; PDF is transparency tables not full balance sheet"
    ),
}
n_comm = append_rows(DATA / "commitments.csv", [commitment])

leaderboard = {
    "item_id": LB,
    "name": (
        "SIMIM Art.23 YE2025 leftover phonogram collecting society: beheers 3.64m / "
        "geinde 32m"
    ),
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": HP,
    "annual_cost_eur": str(BEHEERS_A),
    "total_cost_eur": str(GEINDE),
    "tco_notes": (
        f"Leftover SIMIM CV neighbouring-rights CMO Art.23 YE2025: beheerskosten "
        f"{BEHEERS_A} (ops envelope; B incl fin {BEHEERS_B}) / geinde rechten "
        f"{GEINDE} across reproductie/publieke/kabel/jaarlijkse/leenrecht/thuiskopie/"
        "onderwijs/internationale/andere; largest stream jaarlijkse aanvullende "
        "16.5m geinde / 2.65m beheers; peer of Sabam/PlayRight/Auvibel/Reprobel; "
        "full NBB balanstotaal residual FOI (YE2024 rapport had balans ~44.2m)"
    ),
    "confidence": "strong",
    "source_id": SRC,
    "beneficiaries": "Phonogram producers / music industry via SIMIM members",
    "stated_goal": "Local leftover SIMIM map — official Art.23 YE2025 live",
    "measured_outcome": (
        f"Official SIMIM Art.23 2026-08-23: beheers_A {BEHEERS_A} / geinde {GEINDE}"
    ),
    "absurdity_score": "5.0",
    "cost_score": "4.2",
    "difficulty": "2.5",
    "priority_index": "4.5",
    "cut_proposal": (
        "Do not treat geinde 32m as waste; scrutinise beheers 3.64m vs streams "
        "(jaarlijkse 15.9% ratio elevated); publish NBB statutory"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1709; leftover after AGB unpublished / NSZ CDN403 / Reprobel+Auvibel+"
        "Sabam done; not TE-additive of 348bn"
    ),
}
n_lb = append_rows(DATA / "leaderboard.csv", [leaderboard])

foi = {
    "gap_id": GAP,
    "hierarchy_path": HP,
    "entity_id": EID,
    "what_is_missing": (
        f"Official Art.23 YE2025 publishes geinde {GEINDE} / beheerskosten_A "
        f"{BEHEERS_A}; full NBB statutory jaarrekening PDF/deposit Unknown; "
        "balanstotaal / equity / VTE / staff costs Unknown for YE2025 (YE2024 "
        "rapport de gestion had balans 44176105 / frais 2988683)"
    ),
    "why_it_matters": (
        "Leftover Belgian phonogram neighbouring-rights collecting society with live "
        "Art.23 euros (3.64m beheers / 32.4m geinde) — need NBB statutory to reconcile "
        "transparency tables vs filed accounts and pin staff/VTE"
    ),
    "priority": "7",
    "recipient_body": "SIMIM cv / Bestuursorgaan",
    "recipient_email": "info@simim.be",
    "recipient_postal": "Lenneke Marelaan 8 bus 5 1932 Zaventem",
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
    "notes": "tick1709; human-send only; NSZ/Blauwe/Sabam/Auvibel/Reprobel FOI still ready",
}
n_foi = append_rows(DATA / "foi_queue.csv", [foi])

update_queue()
update_loop_state()

print(
    f"tick1709 applied entities={n_ent} sources={n_src} budgets={n_bud} "
    f"commitments={n_comm} leaderboard={n_lb} foi={n_foi} "
    f"GEINDE={GEINDE} BEHEERS_A={BEHEERS_A}"
)

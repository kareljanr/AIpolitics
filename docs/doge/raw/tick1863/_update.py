import csv
from pathlib import Path

csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")
now = "2026-08-26T03:25:00Z"
tick = 1863
eid = "vzw_bosgroep_houtland"
gap = "gap_bosgroep_houtland_nbb_ye2025_unpublished_l5"


def read_csv(name):
    with (DATA / name).open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), list(r.fieldnames)


def write_csv(name, rows, fieldnames):
    with (DATA / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


sources, scols = read_csv("sources.csv")
sources += [
    {
        "source_id": "src_bgh_site",
        "title": "Bosgroep Houtland official site",
        "url": "https://www.bosgroephoutland.be/",
        "publisher": "Bosgroep Houtland VZW",
        "accessed_date": "2026-08-26",
        "source_class": "official_web",
        "notes": "tick1863; leftover Bosgroep after Digipolis; no JR2025 euros on site; FOI NBB YE2025",
    },
    {
        "source_id": "src_kbo_bgh_0866482291",
        "title": "KBO Bosgroep Houtland VZW 0866.482.291",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0866482291",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick1863; Actief VZW Brugge belt; Northdata no YE2025 deposit this tick",
    },
    {
        "source_id": "src_bgh_foi_contact",
        "title": "Bosgroep Houtland FOI channel (bosgroephoutland@west-vlaanderen.be)",
        "url": "https://bosgroepen.be/houtland/",
        "publisher": "Bosgroep Houtland VZW",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": "tick1863; human-send only; email from official site",
    },
]
write_csv("sources.csv", sources, scols)

ents, ecols = read_csv("entities.csv")
if not any(e.get("entity_id") == eid for e in ents):
    ents.append(
        {
            "entity_id": eid,
            "name_nl": "Bosgroep Houtland VZW (leftover Bosgroep Brugge belt; NOT RL Houtland & Polders)",
            "name_fr": "Groupement forestier Houtland ASBL",
            "name_en": "Houtland Forest Group VZW (Bruges belt leftover Bosgroep)",
            "level": "other",
            "parent_id": "prov_west_vlaanderen",
            "community_language": "nl",
            "website": "https://www.bosgroephoutland.be/",
            "foi_email": "bosgroephoutland@west-vlaanderen.be",
            "foi_postal": "West-Vlaanderen / Brugge belt (bosgroepen.be/houtland)",
            "notes": (
                "tick1863 leftover Bosgroep after Digipolis/LimburgFOI/AGB/Dijk92/FARO/HVZ hunt; "
                "KBO 0866.482.291; NBB YE2025 unpublished; euros Unknown; FOI ready"
            ),
        }
    )
write_csv("entities.csv", ents, ecols)

comms, ccols = read_csv("commitments.csv")
comms.append(
    {
        "commitment_id": "comm_bgh_jr2025_pending_nbb",
        "title": "Bosgroep Houtland VZW YE2025 statutory JR pending NBB (euros Unknown)",
        "entity_id": eid,
        "beneficiary": "Private + public forest owners Houtland / Brugge belt",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; bosgroepen framework",
        "decision_date": "",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "pending_foi",
        "evaluation_url": "https://www.bosgroephoutland.be/",
        "stated_goal": "Sustainable forest management Houtland",
        "cut_option": "FOI NBB YE2025 + subsidy split + RLHP relation",
        "source_id": "src_bgh_site",
        "confidence": "unknown",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>BosgroepHoutland>JR2025_L5",
        "notes": (
            "tick1863; NO invented euros; Dijk92 CDN403; FARO YE2024; AGB Bornem JR2024; "
            "HVZ Fluvia/Waasland/Westhoek no public JR2025 PDF this tick"
        ),
    }
)
write_csv("commitments.csv", comms, ccols)

lbs, lcols = read_csv("leaderboard.csv")
lbs.append(
    {
        "item_id": "lb_bgh_jr2025_nbb_foi_l5",
        "name": "Bosgroep Houtland VZW YE2025 NBB unpublished FOI (euros Unknown)",
        "level": "L5",
        "type": "foi_gap",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>BosgroepHoutland>JR2025_L5",
        "annual_cost_eur": "",
        "total_cost_eur": "",
        "tco_notes": "No YE2025 deposit; statutory euros Unknown; FOI ready",
        "confidence": "unknown",
        "source_id": "src_bgh_site",
        "beneficiaries": "Houtland forest owners / 21 gemeenten class",
        "stated_goal": "Duurzaam bosbeheer Houtland",
        "measured_outcome": "Site live; no statutory euros this tick",
        "absurdity_score": "4.0",
        "cost_score": "1.5",
        "difficulty": "3.0",
        "priority_index": "2.8",
        "cut_proposal": "Publish NBB YE2025; map VL/prov subsidies",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1863; anti-stuck FOI; not TE-additive; do not invent euros",
    }
)
write_csv("leaderboard.csv", lbs, lcols)

fois, fcols = read_csv("foi_queue.csv")
fois.append(
    {
        "gap_id": gap,
        "hierarchy_path": "Vlaanderen>WestVlaanderen>BosgroepHoutland>JR2025_L5",
        "entity_id": eid,
        "what_is_missing": (
            "NBB YE2025 statutory deposit PDF (balans/PnL/sociale balans/toelichting) + AV vaststelling; "
            "werkingssubsidies VL/provincie 2025; relation to RL Houtland & Polders / Bosgroep IJzer; pers/VTE"
        ),
        "why_it_matters": (
            "Preferred leftover Bosgroep of mined Brugge-Houtland belt — no YE2025 deposit after "
            "AGB/Dijk92/FARO/HVZ stall; euros still Unknown"
        ),
        "priority": "8",
        "recipient_body": "Bosgroep Houtland VZW / bestuursorgaan",
        "recipient_email": "bosgroephoutland@west-vlaanderen.be",
        "recipient_postal": "West-Vlaanderen (via bosgroepen.be/houtland)",
        "draft_letter_path": f"docs/doge/foi/drafts/{gap}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_bgh_jr2025_pending_nbb",
        "linked_leaderboard_id": "lb_bgh_jr2025_nbb_foi_l5",
        "created_utc": now,
        "updated_utc": now,
        "notes": "tick1863; human-send only; euros Unknown; NOT Bosgroep Limburg 1861",
    }
)
write_csv("foi_queue.csv", fois, fcols)

rq, rcols = read_csv("research_queue.csv")
for row in rq:
    if row.get("task_id") == "rq_1863":
        row["status"] = "blocked_foi"
        row["entity_id"] = eid
        row["blocked_gap_id"] = gap
        row["updated_utc"] = now
        row["notes"] = (
            "tick1863 BLOCKED_FOI Bosgroep Houtland VZW KBO 0866.482.291; NBB YE2025 unpublished "
            "after Digipolis PDF / BosgroepLimburgFOI / AGB Bornem JR2024 / Dijk92 403 / FARO YE2024 / "
            "HVZ Fluvia-Waasland-Westhoek no JR PDF; euros Unknown"
        )
rq.append(
    {
        "task_id": "rq_1864",
        "title": "Leftover dual residual hole-fill after Bosgroep Houtland FOI (AGB/Dijk92/FARO/IJzer-if-CDN / other HVZ-IGS)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1864 after 1863 Bosgroep Houtland FOI. Prefer leftover AGB/APB if PDF live, else "
            "Dijk92/Enebra if CDN 200, else FARO if TRUE NBB YE2025, else Bosgroep IJzer en Leie if "
            "CDN 200, else other HVZ/IGS live JR2025 euros. BosgroepHoutlandFOI+Digipolis+"
            "BosgroepLimburgFOI+DiependaeleIOED taken. Skip done. Prefer NON-Eneco. Next every-10 1870."
        ),
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": now,
        "notes": "spawned after tick1863; next every-10 1870",
    }
)
write_csv("research_queue.csv", rq, rcols)

ls, lsc = read_csv("loop_state.csv")
for row in ls:
    if row.get("state_id") == "main":
        row["last_tick_utc"] = now
        row["last_unit_id"] = "rq_1863"
        row["ticks_completed"] = "1863"
        row["paused"] = "no"
        row["notes"] = (
            "tick1863 leftover Bosgroep Houtland VZW 0866.482.291 FOI (NBB YE2025 unpublished; "
            "euros Unknown); AGB Bornem JR2024; Dijk92 403; FARO YE2024; next rq_1864; "
            "next every-10 1870; continuous hole_fill"
        )
write_csv("loop_state.csv", ls, lsc)

print("OK", tick, "foi", len(fois), "rq", len(rq))

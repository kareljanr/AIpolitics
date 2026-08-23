import csv
from pathlib import Path

csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")
now = "2026-08-26T02:40:00Z"
tick = 1861
eid = "vzw_bosgroep_limburg"
gap = "gap_bosgroep_limburg_nbb_ye2025_unpublished_l5"


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
        "source_id": "src_bgl_jaaroverzicht_2025",
        "title": "Bosgroep Limburg jaaroverzicht 2025 (activity metrics; no euros)",
        "url": "https://bosgroeplimburg.jaaroverzichtlimburg.be/",
        "publisher": "Bosgroep Limburg VZW",
        "accessed_date": "2026-08-26",
        "source_class": "official_web",
        "notes": "tick1861; 5339 leden; ~22000 ha; 42220 plantingen; NO euros; NBB YE2025 FOI",
    },
    {
        "source_id": "src_bgl_beleidsplan_2026_2031",
        "title": "Bosgroep Limburg beleidsplan 2026-2031 PDF",
        "url": "https://bosgroep.limburg.be/sites/default/files/media/files/2026-02/bosgroep_limburg_beleidsplan_2026-2031.pdf",
        "publisher": "Bosgroep Limburg VZW",
        "accessed_date": "2026-08-26",
        "source_class": "official_web",
        "notes": "tick1861; cites activiteitenverslag 2025; 3409 bosbeheerders + 1930 sympathisanten; no statutory euros",
    },
    {
        "source_id": "src_kbo_bgl_0668619317",
        "title": "KBO Bosgroep Limburg VZW 0668.619.317",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0668619317",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick1861; parent of CoLimBo CV 0890.220.171; zetel Universiteitslaan 1 Hasselt",
    },
    {
        "source_id": "src_bgl_foi_contact",
        "title": "Bosgroep Limburg FOI channel (bosgroep@limburg.be)",
        "url": "https://bosgroep.limburg.be/",
        "publisher": "Bosgroep Limburg VZW",
        "accessed_date": "2026-08-26",
        "source_class": "foi_contact",
        "notes": "tick1861; human-send only; Universiteitslaan 1 3500 Hasselt",
    },
]
write_csv("sources.csv", sources, scols)

ents, ecols = read_csv("entities.csv")
if not any(e.get("entity_id") == eid for e in ents):
    ents.append(
        {
            "entity_id": eid,
            "name_nl": "Bosgroep Limburg VZW (leftover Bosgroep parent; NOT CoLimBo CV)",
            "name_fr": "Groupement forestier Limbourg ASBL",
            "name_en": "Limburg Forest Group VZW (parent; CoLimBo daughter separate)",
            "level": "other",
            "parent_id": "prov_limburg",
            "community_language": "nl",
            "website": "https://bosgroep.limburg.be/",
            "foi_email": "bosgroep@limburg.be",
            "foi_postal": "Universiteitslaan 1 3500 Hasselt",
            "notes": (
                "tick1861 leftover Bosgroep after AGB/Dijk92/FARO/HVZ hunt; KBO 0668.619.317; "
                "jaaroverzicht 2025 activity-only; NBB YE2025 unpublished; euros Unknown; FOI ready"
            ),
        }
    )
write_csv("entities.csv", ents, ecols)

# placeholder commitment: Unknown euros — use empty envelope note via status blocked pattern
comms, ccols = read_csv("commitments.csv")
comms.append(
    {
        "commitment_id": "comm_bgl_jr2025_pending_nbb",
        "title": "Bosgroep Limburg VZW YE2025 statutory JR pending NBB (euros Unknown)",
        "entity_id": eid,
        "beneficiary": "Private + public forest owners Limburg / provincie dual",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; bosgroepen framework",
        "decision_date": "",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "pending_foi",
        "evaluation_url": "https://bosgroeplimburg.jaaroverzichtlimburg.be/",
        "stated_goal": "Sustainable private/public forest management Limburg",
        "cut_option": "FOI NBB YE2025 + subsidy split + CoLimBo relation",
        "source_id": "src_bgl_jaaroverzicht_2025",
        "confidence": "unknown",
        "hierarchy_path": "Vlaanderen>Limburg>BosgroepLimburg>JR2025_L5",
        "notes": (
            "tick1861; NO invented euros; activity metrics only (5339 leden / ~22000 ha); "
            "Dijk92 CDN403; FARO YE2024; AGB Bornem JR2024; daughter CoLimBo taken 1452"
        ),
    }
)
write_csv("commitments.csv", comms, ccols)

lbs, lcols = read_csv("leaderboard.csv")
lbs.append(
    {
        "item_id": "lb_bgl_jr2025_nbb_foi_l5",
        "name": "Bosgroep Limburg VZW YE2025 NBB unpublished FOI (euros Unknown)",
        "level": "L5",
        "type": "foi_gap",
        "hierarchy_path": "Vlaanderen>Limburg>BosgroepLimburg>JR2025_L5",
        "annual_cost_eur": "",
        "total_cost_eur": "",
        "tco_notes": "Activity-only jaaroverzicht 2025; statutory euros Unknown; FOI ready",
        "confidence": "unknown",
        "source_id": "src_bgl_jaaroverzicht_2025",
        "beneficiaries": "5339 leden / ~22000 ha forest Limburg",
        "stated_goal": "Duurzaam bosbeheer Limburg",
        "measured_outcome": "Public activity metrics; no statutory euros this tick",
        "absurdity_score": "4.0",
        "cost_score": "1.5",
        "difficulty": "3.0",
        "priority_index": "2.8",
        "cut_proposal": "Publish NBB YE2025; map VL/prov subsidies; CoLimBo dual",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1861; anti-stuck FOI; not TE-additive; do not invent euros",
    }
)
write_csv("leaderboard.csv", lbs, lcols)

fois, fcols = read_csv("foi_queue.csv")
fois.append(
    {
        "gap_id": gap,
        "hierarchy_path": "Vlaanderen>Limburg>BosgroepLimburg>JR2025_L5",
        "entity_id": eid,
        "what_is_missing": (
            "NBB YE2025 statutory deposit PDF (balans/PnL/sociale balans/toelichting) + AV vaststelling; "
            "werkingssubsidies VL/provincie 2025; CoLimBo CV relation/steun; pers/VTE"
        ),
        "why_it_matters": (
            "Preferred leftover Bosgroep parent of mined Limburg cities — public jaaroverzicht has "
            "activity metrics only; statutory euros still Unknown after AGB/Dijk92/FARO/HVZ stall"
        ),
        "priority": "8",
        "recipient_body": "Bosgroep Limburg VZW / bestuursorgaan",
        "recipient_email": "bosgroep@limburg.be",
        "recipient_postal": "Universiteitslaan 1 3500 Hasselt",
        "draft_letter_path": f"docs/doge/foi/drafts/{gap}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_bgl_jr2025_pending_nbb",
        "linked_leaderboard_id": "lb_bgl_jr2025_nbb_foi_l5",
        "created_utc": now,
        "updated_utc": now,
        "notes": "tick1861; human-send only; euros Unknown; Dijk92 403; FARO YE2024; AGB Bornem JR2024",
    }
)
write_csv("foi_queue.csv", fois, fcols)

rq, rcols = read_csv("research_queue.csv")
for row in rq:
    if row.get("task_id") == "rq_1861":
        row["status"] = "blocked_foi"
        row["entity_id"] = eid
        row["blocked_gap_id"] = gap
        row["updated_utc"] = now
        row["notes"] = (
            "tick1861 BLOCKED_FOI Bosgroep Limburg VZW KBO 0668.619.317; jaaroverzicht 2025 "
            "activity-only no euros; NBB YE2025 unpublished after AGB Bornem JR2024 / Dijk92 403 / "
            "FARO YE2024 / HVZ Rivierenland+Midwest+BZA+Centrum already mined/FOI; euros Unknown"
        )
rq.append(
    {
        "task_id": "rq_1862",
        "title": "Leftover dual residual hole-fill after Bosgroep Limburg FOI (AGB/Dijk92/FARO/other HVZ-if-live / other IGS)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1862 after 1861 Bosgroep Limburg FOI. Prefer leftover AGB/APB if PDF live, else "
            "Dijk92/Enebra if CDN 200, else FARO if TRUE NBB YE2025, else other Bosgroep VZW "
            "(Houtland/IJzer en Leie) if CDN 200, else other HVZ/IGS with live official JR2025 euros. "
            "BosgroepLimburgFOI+DiependaeleIOED+Audio+TerNetheFOI taken. Skip done. Prefer NON-Eneco. "
            "Next every-10 1870."
        ),
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": now,
        "notes": "spawned after tick1861; next every-10 1870",
    }
)
write_csv("research_queue.csv", rq, rcols)

ls, lsc = read_csv("loop_state.csv")
for row in ls:
    if row.get("state_id") == "main":
        row["last_tick_utc"] = now
        row["last_unit_id"] = "rq_1861"
        row["ticks_completed"] = "1861"
        row["paused"] = "no"
        row["notes"] = (
            "tick1861 leftover Bosgroep Limburg VZW 0668.619.317 FOI (jaaroverzicht activity-only; "
            "NBB YE2025 unpublished; euros Unknown); AGB Bornem JR2024; Dijk92 403; FARO YE2024; "
            "next rq_1862; next every-10 1870; continuous hole_fill"
        )
write_csv("loop_state.csv", ls, lsc)

print("OK", tick, "foi", len(fois), "rq", len(rq))

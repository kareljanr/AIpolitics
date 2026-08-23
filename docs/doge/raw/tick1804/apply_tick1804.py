import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T04:15:00Z"
TICK = 1804
EID = "nv_storm_zandvliet"
GID = "gap_stormz_nbb_ye2025_deposit_l5_bruto_pnl_debt"
CID = "comm_stormz_zefier_dual_sza_stake_0_41m"
LID = "lb_stormz_zefier_dual_stake_0_41m_sector_div_0_15m_l5"
SRC = "src_stormz_zefier_balans_2025"


def read(fn):
    with (DATA / fn).open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write(fn, fields, rows):
    with (DATA / fn).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": SRC,
        "title": "Zefier detail balans YE2025 — aandelen Storm Zandvliet",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/67b43e8425285b6d3a0f2ace_7eb835a4d4c00a4dd68015464ffffb94_detail%20van%20de%20balans%20per%2031%20december%202023.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1804; SZA aandelen 411572.19; leftover Zefier dual after StormW FOI stall",
    },
    {
        "source_id": "src_stormz_zefier_sector_2025",
        "title": "Zefier rekeningsector Storm Zandvliet per vennoot boekjaar 2025",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee9881166c6038252ecc7_Storm%20Zandvliet%20nv.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1804; sector ontvangen dividend totaal 145044.91; Antwerpen dominant",
    },
    {
        "source_id": "src_stormz_kbo",
        "title": "KBO Storm Zandvliet NV 0501.625.305",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0501625305",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1804; NV; Borsbeeksebrug 22 2600 Berchem; Zefier dual SZA",
    },
]
ids = {r["source_id"] for r in rows}
for s in new_sources:
    if s["source_id"] not in ids:
        rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("entities.csv")
note = (
    "tick1804 leftover Zefier dual after StormW FOI; KBO 0501.625.305 Actief; NV; "
    "honest AGB Bornem still JR2024; AGB Wielsbeke already mined; NSZ/Dijk92/APEFE still CDN 403; FARO NBB YE2025 unpublished; "
    "Storm Zandvliet NBB YE2025 deposit NOT found on CDN after scan (SBM HTML IP blacklist); "
    "primary Zefier YE2025: aandelen SZA 411572; sector ontvangen dividend 145045 (Antwerpen 133200); "
    "aggregator leads NOT booked as strong primary; FOI for full NBB deposit L5; Terranova Solar CDN/sector deferred; NOT every-10 (next 1810)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "Storm Zandvliet NV (leftover Zefier dual / SZA; NOT StormW / StormG / SPS FIN / TNS)",
            "name_fr": "Storm Zandvliet SA (dual Zefier residuel / SZA)",
            "name_en": "Storm Zandvliet NV leftover Zefier dual wind project company",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/overlay-pages/storm-zandvliet-nv",
            "foi_email": "info@zefier.be",
            "foi_postal": "Borsbeeksebrug 22 2600 Berchem (Antwerpen)",
            "notes": note,
        }
    )
else:
    for r in rows:
        if r.get("entity_id") == EID:
            r["notes"] = note
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_stormz_zefier_shares_2025", 411572, "Zefier aandelen Storm Zandvliet 411572.19 YE2025; tick1804 primary"),
    ("bud_stormz_zefier_sector_div_recv_2025", 145045, "Zefier sector SZA ontvangen dividend totaal 145044.91; tick1804 primary"),
    ("bud_stormz_zefier_sector_div_antwerpen_2025", 133200, "Antwerpen slice sector dividend 133199.94; tick1804 primary"),
]
existing = {r["budget_id"] for r in rows}
for bid, amt, notes in budgets:
    if bid in existing:
        continue
    src = SRC if "shares" in bid else "src_stormz_zefier_sector_2025"
    rows.append(
        {
            "budget_id": bid,
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(amt),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "realized",
            "source_id": src,
            "confidence": "strong",
            "notes": notes,
        }
    )
write("budgets.csv", fields, rows)
print("budgets", len(rows))

fields, rows = read("commitments.csv")
if not any(r.get("commitment_id") == CID for r in rows):
    rows.append(
        {
            "commitment_id": CID,
            "title": "Storm Zandvliet Zefier dual SZA (stake 0.41m / sector div 0.15m; NBB YE2025 FOI)",
            "entity_id": EID,
            "beneficiary": "Zefier Antwerpen-belt municipalities / Storm Management / PMV-TINC stack",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal renewable dual via Zefier SZA sector",
            "decision_date": "2025-12-31",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "411572",
            "cash_by_year": "2025:411572",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee9881166c6038252ecc7_Storm%20Zandvliet%20nv.pdf",
            "stated_goal": "Local leftover Zefier Storm Zandvliet wind map — NBB YE2025 deposit FOI",
            "cut_option": "Publish NBB YE2025 deposit ID + L5 bruto/PnL/debt; reconcile sector dividend 145k",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormZandvliet>JR2025_L5",
            "notes": "tick1804; Zefier-primary stake+sector div only; NBB YE2025 CDN miss; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; not TE-additive",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "Storm Zandvliet Zefier dual: stake 0.41m / sector div 0.15m (NBB YE2025 FOI pending)",
            "level": "L5",
            "type": "igs_energy_project_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormZandvliet",
            "annual_cost_eur": "145045",
            "total_cost_eur": "411572",
            "tco_notes": "Envelope=Zefier SZA stake 411572; sector dividend recv 145045 (Antwerpen 133200); projectco NBB YE2025 not on CDN — FOI; not pure waste",
            "confidence": "medium",
            "source_id": SRC,
            "beneficiaries": "Antwerpen + Beveren-Kruibeke-Zwijndrecht + Brasschaat + Duffel + Kapellen + Mortsel",
            "stated_goal": "Local wind via Zefier SZA sector",
            "measured_outcome": "Zefier holds 0.41m equity; sector books 0.15m dividend map; projectco NBB opaque on CDN",
            "absurdity_score": "5",
            "cost_score": "3.5",
            "difficulty": "5",
            "priority_index": "4.3",
            "cut_proposal": "FOI NBB YE2025 deposit + bruto/PnL/debt L5 + reconcile sector dividend 145k",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1804 leftover Zefier dual stall FOI; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormZandvliet>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "NBB YE2025 deposit ID + full VKT/VOL PDF for Storm Zandvliet NV (KBO 0501.625.305) — CDN miss / SBM HTML IP blacklist; L5 omzet behind bruto; PnL/winstverwerking; schulden tegenpartijen; reconciliatie Zefier sector dividend 145045; AV 2026 notulen",
            "why_it_matters": "Leftover Zefier dual SZA after StormW FOI: Zefier holds 0.41m shares and books 0.15m sector dividend (Antwerpen-heavy) while projectco NBB YE2025 not retrievable on CDN",
            "priority": "8",
            "recipient_body": "Storm Zandvliet NV / Zefier cv / Storm Management NV",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Borsbeeksebrug 22 2600 Berchem (Antwerpen)",
            "draft_letter_path": f"docs/doge/foi/drafts/{GID}.md",
            "status": "ready",
            "date_ready": "2026-08-25",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": CID,
            "linked_leaderboard_id": LID,
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick1804 stall FOI; human-send only; no invented projectco euros; Terranova Solar deferred; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1804":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1804 Storm Zandvliet Zefier dual stall; KBO 0501.625.305; NBB YE2025 CDN miss; Zefier stake 411572 sector div 145045; FOI ready; every-10 1810"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1805" for r in rows):
    rows.append(
        {
            "task_id": "rq_1805",
            "title": "Leftover dual residual hole-fill after StormZ FOI (AGB/NSZ/Bosgroep/FARO/TNS/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1805 after 1804 Storm Zandvliet FOI stall. Prefer leftover AGB/APB of mined cities if PDF live unused, else Bosgroep / IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / Terranova Solar if CDN 200 or Zefier-primary FOI / OP-TIL/VI.BE if unused live / other HVZ if JR2025 euros newly live / other IGS. Skip already-done. Next every-10 1810.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1804; NEXT residual dual; Terranova Solar deferred; every-10 1810",
        }
    )
write("research_queue.csv", fields, rows)
print("research_queue updated")

fields, rows = read("loop_state.csv")
for r in rows:
    if r.get("state_id") == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = NOW
        r["last_unit_id"] = "rq_1804"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1804 leftover Storm Zandvliet NV Zefier dual SZA stall FOI; KBO 0501.625.305; NBB YE2025 CDN miss; "
            "Zefier-primary stake 411572 + sector div 145045 (Antwerpen 133200); Terranova Solar deferred; "
            "AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; NOT every-10 (next 1810); next rq_1805 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")

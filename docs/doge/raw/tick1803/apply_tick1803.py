import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T03:55:00Z"
TICK = 1803
EID = "nv_storm_wielsbeke"
GID = "gap_stormw_nbb_ye2025_deposit_l5_bruto_loss_debt"
CID = "comm_stormw_zefier_dual_swi_stake_0_21m"
LID = "lb_stormw_zefier_dual_stake_0_21m_loan_0_23m_l5"
SRC = "src_stormw_zefier_balans_2025"


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
        "title": "Zefier detail balans YE2025 — aandelen + achtergestelde lening Storm Wielsbeke",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/67b43e8425285b6d3a0f2ace_7eb835a4d4c00a4dd68015464ffffb94_detail%20van%20de%20balans%20per%2031%20december%202023.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1803; SWI aandelen 210531.21 + achtergestelde lening 233080.63; leftover Zefier dual after SPS FIN",
    },
    {
        "source_id": "src_stormw_zefier_sector_2025",
        "title": "Zefier rekeningsector Storm Wielsbeke per vennoot boekjaar 2025",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee9894ff822e68a89f748_Storm%20Wielsbeke%20nv.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1803; sector dividend ontvangst totaal 50000 across municipalities; Wielsbeke largest slice",
    },
    {
        "source_id": "src_stormw_kbo",
        "title": "KBO Storm Wielsbeke NV 0844.303.341",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0844303341",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1803; NV Actief; Borsbeeksebrug 22 2600 Antwerpen; AV May; capital 404442.20",
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
    "tick1803 leftover Zefier dual after SPS FIN; KBO 0844.303.341 Actief; NV; "
    "honest AGB Bornem still JR2024 on portal; AGB Wielsbeke JR2025 already mined tick943; NSZ/Dijk92/APEFE still CDN 403; FARO NBB YE2025 still unpublished; "
    "Storm Wielsbeke NBB YE2025 deposit NOT found on CDN after wide scan (SBM HTML IP blacklist); "
    "primary Zefier YE2025 balans: aandelen SWI 210531 + achtergestelde lening 233081; sector PDF ontvangen dividend totaal 50000; "
    "aggregator leads (NOT strong primary): bruto ~508595 / winst ~-228109 / EV ~1218806 / assets ~3130053 — FOI for full NBB deposit L5; NOT every-10 (next 1810)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "Storm Wielsbeke NV (leftover Zefier dual / SWI; NOT StormG / SPS FIN / EGPF / W4F)",
            "name_fr": "Storm Wielsbeke SA (dual Zefier residuel / SWI)",
            "name_en": "Storm Wielsbeke NV leftover Zefier dual wind project company",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/",
            "foi_email": "info@zefier.be",
            "foi_postal": "Borsbeeksebrug 22 2600 Antwerpen",
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
    ("bud_stormw_zefier_shares_2025", 210531, "Zefier aandelen Storm Wielsbeke 210531.21 YE2025; tick1803 primary"),
    ("bud_stormw_zefier_subord_loan_2025", 233081, "Zefier achtergestelde lening Storm Wielsbeke 233080.63 YE2025; tick1803 primary"),
    ("bud_stormw_zefier_sector_div_recv_2025", 50000, "Zefier sector SWI ontvangen dividend totaal 50000 boekjaar 2025; tick1803 primary"),
]
existing = {r["budget_id"] for r in rows}
for bid, amt, notes in budgets:
    if bid in existing:
        continue
    rows.append(
        {
            "budget_id": bid,
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(amt),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "realized",
            "source_id": SRC if "shares" in bid or "loan" in bid else "src_stormw_zefier_sector_2025",
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
            "title": "Storm Wielsbeke Zefier dual SWI (stake 0.21m + subord loan 0.23m; NBB YE2025 FOI)",
            "entity_id": EID,
            "beneficiary": "Zefier municipalities (West-Vlaanderen dual) / Storm Management / PMV-TINC stack",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal renewable dual via Zefier SWI sector",
            "decision_date": "2025-12-31",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "443612",
            "cash_by_year": "2025:443612",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/67b43e8425285b6d3a0f2ace_7eb835a4d4c00a4dd68015464ffffb94_detail%20van%20de%20balans%20per%2031%20december%202023.pdf",
            "stated_goal": "Local leftover Zefier Storm Wielsbeke wind map — NBB YE2025 deposit FOI",
            "cut_option": "Publish NBB YE2025 deposit ID + full L5 bruto/PnL/debt; explain sector dividend 50k vs projectco loss lead",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormWielsbeke>JR2025_L5",
            "notes": "tick1803; Zefier-primary stake+loan only; NBB YE2025 CDN miss after scan; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; not TE-additive",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "Storm Wielsbeke Zefier dual: stake 0.21m + subord loan 0.23m (NBB YE2025 FOI pending)",
            "level": "L5",
            "type": "igs_energy_project_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormWielsbeke",
            "annual_cost_eur": "50000",
            "total_cost_eur": "443612",
            "tco_notes": "Envelope=Zefier SWI stake 210531 + subord loan 233081; sector dividend recv 50000; projectco own NBB YE2025 not on CDN — FOI; not pure waste",
            "confidence": "medium",
            "source_id": SRC,
            "beneficiaries": "Zefier West-Vlaanderen municipalities + Storm/PMV stack",
            "stated_goal": "Local wind via Zefier SWI sector",
            "measured_outcome": "Zefier holds 0.21m equity + 0.23m loan; sector pays 50k dividend map; projectco NBB opaque on CDN",
            "absurdity_score": "5",
            "cost_score": "3",
            "difficulty": "5",
            "priority_index": "4.2",
            "cut_proposal": "FOI NBB YE2025 deposit + bruto/PnL/debt L5 + reconcile sector dividend vs projectco result",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1803 leftover Zefier dual stall FOI; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormWielsbeke>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "NBB YE2025 deposit ID + full VKT/VOL PDF for Storm Wielsbeke NV (KBO 0844.303.341) — CDN miss after wide scan / SBM HTML IP blacklist; L5 omzet behind bruto; PnL path; schulden/leningen tegenpartijen; reconciliatie Zefier sector dividend 50000 vs projectco resultaat; AV 2026 notulen",
            "why_it_matters": "Leftover Zefier dual SWI after SPS FIN/StormG: Zefier still holds 0.21m shares + 0.23m subord loan and books 50k sector dividend while projectco NBB YE2025 not retrievable on CDN",
            "priority": "8",
            "recipient_body": "Storm Wielsbeke NV / Zefier cv / Storm Management NV",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Borsbeeksebrug 22 2600 Antwerpen",
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
            "notes": "tick1803 stall FOI; human-send only; no invented projectco euros; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1803":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1803 Storm Wielsbeke Zefier dual stall; KBO 0844.303.341; NBB YE2025 CDN miss; Zefier stake 210531 loan 233081; FOI ready; every-10 1810"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1804" for r in rows):
    rows.append(
        {
            "task_id": "rq_1804",
            "title": "Leftover dual residual hole-fill after StormW FOI (AGB/NSZ/Bosgroep/FARO/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1804 after 1803 Storm Wielsbeke FOI stall. Prefer leftover AGB/APB of mined cities if PDF live unused, else Bosgroep / IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / Storm Zandvliet/Terranova if CDN 200 / OP-TIL/VI.BE if unused live / other HVZ if JR2025 euros newly live / other IGS. Skip already-done (AGB Wielsbeke mined). Next every-10 1810.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1803; NEXT residual dual; StormW NBB FOI pending; every-10 1810",
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
        r["last_unit_id"] = "rq_1803"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1803 leftover Storm Wielsbeke NV Zefier dual SWI stall FOI; KBO 0844.303.341; NBB YE2025 CDN miss after scan; "
            "Zefier-primary stake 210531 + subord loan 233081 + sector div 50000; AGB Bornem JR2024; AGB Wielsbeke already mined; "
            "NSZ/Dijk92/APEFE still 403; NOT every-10 (next 1810); next rq_1804 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")

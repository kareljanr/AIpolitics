# tick1813 — Storm Olen NV NBB YE2025 (IKA-Storm dual; bruto 0.29m / debt 12.10m)
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
NOW = "2026-08-25T07:25:00Z"

def read(name):
    with open(ROOT / name, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames

def write(name, rows, fields):
    with open(ROOT / name, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})

ents, ef = read("entities.csv")
if not any(e.get("entity_id") == "nv_storm_olen" for e in ents):
    ents.append({
        "entity_id": "nv_storm_olen",
        "name_nl": "Storm Olen NV (leftover IKA-Storm dual wind projectco; NOT LumIKA / StormG / StormW / StormZ)",
        "name_fr": "Storm Olen SA (dual IKA-Storm residuel / projet eolien)",
        "name_en": "Storm Olen NV leftover IKA-Storm dual wind project company",
        "level": "other",
        "parent_id": "igs_ika",
        "community_language": "nl",
        "website": "https://ika.vlaanderen/",
        "foi_email": "info@ika.vlaanderen",
        "foi_postal": "Borsbeeksebrug 22 2600 Berchem (Antwerpen)",
        "notes": (
            "tick1813 leftover IKA dual deferred from LumIKA 1812; KBO 0754.810.052 Actief; NV; "
            "official NBB VKT-kap YE2025 deposit 2026-00117861 CDN 200 26p; AV 30.04.2026; "
            "IKA + Storm Management bestuurders; sourced euros assets 14945362 MVA 12498634 IVA 1023585 "
            "bruto 294145 omzet empty expl 292268 pnl 87008 debt 12103483 LT 11302471 cash DROP 1305871 "
            "VTE 0 gewaarborgd 8347864; IKA FVA book 672851 (87174 sh 20pct class); FOI ready; "
            "AGB Bornem JR2024; Dijk92/NSZ/APEFE 403; NOT every-10 (next 1820)"
        ),
    })
write("entities.csv", ents, ef)

srcs, sf = read("sources.csv")
new_srcs = [
    {
        "source_id": "src_stormolen_jr2025_nbb",
        "title": "Storm Olen official NBB VKT-kap YE2025 deposit 2026-00117861",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117861.pdf",
        "publisher": "NBB / Storm Olen",
        "accessed_date": "2026-08-25",
        "source_class": "primary_pdf",
        "notes": "tick1813; 26p 214472; AV 30.04.2026; header 22.05.2026; model VKT-kap 26.0.11 m01-f; assets 14945362 bruto 294145 pnl 87008 omzet empty",
    },
    {
        "source_id": "src_stormolen_kbo_0754810052",
        "title": "KBO Public Search Storm Olen 0754.810.052",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0754810052",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick1813; NV; zetel Borsbeeksebrug 22 2600 Berchem; IKA bestuurder",
    },
    {
        "source_id": "src_stormolen_ika_cross",
        "title": "IKA YE2025 FVA lists Storm Olen book 672851.13 (from 2026-00259426)",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00259426.pdf",
        "publisher": "NBB / IKA",
        "accessed_date": "2026-08-25",
        "source_class": "primary_pdf",
        "notes": "tick1813; IKA FVA Storm Olen 87174 sh book 672851.13; dual residual path",
    },
]
have = {s["source_id"] for s in srcs}
for s in new_srcs:
    if s["source_id"] not in have:
        srcs.append(s)
write("sources.csv", srcs, sf)

buds, bf = read("budgets.csv")
budget_rows = [
    ("bud_stormolen_assets_14_95m_2025", "14945362", "assets YE2025"),
    ("bud_stormolen_mva_12_50m_2025", "12498634", "MVA YE2025"),
    ("bud_stormolen_bruto_0_29m_2025", "294145", "brutomarge 9900; omzet 70 empty"),
    ("bud_stormolen_pnl_0_09m_2025", "87008", "PnL 9904"),
    ("bud_stormolen_debt_12_10m_2025", "12103483", "schulden 17/49"),
    ("bud_stormolen_lt_debt_11_30m_2025", "11302471", "LT schulden 17"),
    ("bud_stormolen_cash_1_31m_2025", "1305871", "cash DROP from 2218291"),
    ("bud_stormolen_equity_2_84m_2025", "2841879", "equity 10/15"),
    ("bud_stormolen_expl_0_29m_2025", "292268", "bedrijfswinst 9901"),
    ("bud_stormolen_fin_cost_0_21m_2025", "205260", "financiële kosten 65"),
]
have_b = {b.get("budget_id") for b in buds}
for bid, amt, note in budget_rows:
    if bid not in have_b:
        buds.append({
            "budget_id": bid,
            "entity_id": "nv_storm_olen",
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "NBB VKT-kap YE2025",
            "source_id": "src_stormolen_jr2025_nbb",
            "confidence": "strong",
            "notes": f"tick1813; {note}; not TE-additive of 348bn",
        })
write("budgets.csv", buds, bf)

comms, cf = read("commitments.csv")
new_comms = [
    ("comm_stormolen_jr2025_bruto_0_29m", "Storm Olen JR2025 leftover IKA dual (bruto 0.29m / omzet empty / PnL 87k)", "294145", "Publish PPA/GSC behind empty omzet 70"),
    ("comm_stormolen_jr2025_debt_12_10m", "Storm Olen JR2025 leftover IKA dual (debt 12.10m / guaranteed 8.35m)", "12103483", "Publish LT lenders + guarantee counterparties"),
    ("comm_stormolen_jr2025_cash_drop_0_91m", "Storm Olen JR2025 leftover IKA dual (cash DROP 0.91m)", "912420", "Explain cash DROP + activated interest 417k"),
]
have_c = {c.get("commitment_id") for c in comms}
for cid, title, env, cut in new_comms:
    if cid not in have_c:
        comms.append({
            "commitment_id": cid,
            "title": title,
            "entity_id": "nv_storm_olen",
            "beneficiary": "IKA municipalities / Storm wind dual Olen",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal dual via IKA",
            "decision_date": "2026-04-30",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117861.pdf",
            "stated_goal": "Local leftover IKA-Storm wind dual map Olen",
            "cut_option": cut,
            "source_id": "src_stormolen_jr2025_nbb",
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>Antwerpen>IGS>IKA>StormOlen>JR2025_L5",
            "notes": "tick1813; NBB primary; FOI ready; not TE-additive of 348bn",
        })
write("commitments.csv", comms, cf)

lbs, lf = read("leaderboard.csv")
if not any(x.get("item_id") == "lb_stormolen_bruto_0_29m_debt_12_10m_omzet_empty_l5" for x in lbs):
    lbs.append({
        "item_id": "lb_stormolen_bruto_0_29m_debt_12_10m_omzet_empty_l5",
        "name": "Storm Olen JR2025: bruto 0.29m / debt 12.10m / omzet empty / VTE 0",
        "level": "L5",
        "type": "renewable_dual",
        "hierarchy_path": "Vlaanderen>Antwerpen>IGS>IKA>StormOlen",
        "annual_cost_eur": "294145",
        "total_cost_eur": "12103483",
        "tco_notes": (
            "Envelope=bruto 294145 (omzet 70 empty); assets 14945362 MVA 12498634 IVA 1023585; "
            "debt 12103483 LT 11302471 guaranteed 8347864; pnl 87008 expl 292268 fin cost 205260; "
            "cash DROP 1305871; equity 2841879; VTE 0; IKA book ~0.67m; dividend 0"
        ),
        "confidence": "strong",
        "source_id": "src_stormolen_jr2025_nbb",
        "beneficiaries": "IKA municipalities / Storm offtake Olen",
        "stated_goal": "Wind production dual IKA-Storm",
        "measured_outcome": "Thin bruto vs 12.1m debt; empty omzet; 0 staff",
        "absurdity_score": "5",
        "cost_score": "3.5",
        "difficulty": "4",
        "priority_index": "4.1",
        "cut_proposal": "FOI empty omzet 70 + ownership % + LT debt/guarantee matrix; scrutinise IKA dual",
        "status": "open",
        "struck_reason": "",
        "notes": "tick1813 leftover IKA dual; strong NBB; not TE-additive; not pure-waste top10",
    })
write("leaderboard.csv", lbs, lf)

fois, ff = read("foi_queue.csv")
if not any(x.get("gap_id") == "gap_stormolen_bruto_0_29m_omzet_empty_debt_12_10m_l5" for x in fois):
    fois.append({
        "gap_id": "gap_stormolen_bruto_0_29m_omzet_empty_debt_12_10m_l5",
        "hierarchy_path": "Vlaanderen>Antwerpen>IGS>IKA>StormOlen>JR2025_L5",
        "entity_id": "nv_storm_olen",
        "what_is_missing": (
            "Omzet code 70 empty behind bruto 294145; IKA vs Storm ownership %; LT debt 11.30m + "
            "gewaarborgd 8.35m counterparties; cash DROP path; activated interest 416653; AV PV 30.04.2026"
        ),
        "why_it_matters": (
            "IKA-Storm wind dual carries 12.1m debt on 0.29m bruto with empty omzet — residual opacity after LumIKA"
        ),
        "priority": "8",
        "recipient_body": "Storm Olen NV / Storm Management / IKA DV",
        "recipient_email": "info@ika.vlaanderen",
        "recipient_postal": "Borsbeeksebrug 22 2600 Berchem (Antwerpen)",
        "draft_letter_path": "docs/doge/foi/drafts/gap_stormolen_bruto_0_29m_omzet_empty_debt_12_10m_l5.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_stormolen_jr2025_bruto_0_29m",
        "linked_leaderboard_id": "lb_stormolen_bruto_0_29m_debt_12_10m_omzet_empty_l5",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "tick1813; human-send only; AGB Bornem JR2024; Dijk92/NSZ/APEFE 403; FARO YE2024 only",
    })
write("foi_queue.csv", fois, ff)

rqs, rf = read("research_queue.csv")
for row in rqs:
    if row.get("task_id") == "rq_1813":
        row["status"] = "done"
        row["entity_id"] = "nv_storm_olen"
        row["updated_utc"] = NOW
        row["notes"] = (
            "tick1813 done; Storm Olen NBB 2026-00117861 bruto 294145 debt 12103483 omzet empty VTE 0"
        )
if not any(r.get("task_id") == "rq_1814" for r in rqs):
    rqs.append({
        "task_id": "rq_1814",
        "title": "Leftover dual residual hole-fill after Storm Olen (AGB/NSZ/Dijk92/FARO/APEFE/HVZ/Pampero/other Storm/IGS)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1814 after 1813 Storm Olen. Prefer leftover AGB/APB if PDF live unused, else Pampero Wind / "
            "other IKA Storm* if CDN 200, else Dijk92 if CDN 200 / FARO NBB YE2025 / APEFE/NSZ if CDN 200 / "
            "HVZ Waasland if euros / other IGS. Skip done. Next every-10 1820."
        ),
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned after tick1813; Pampero 2025-00521828 YE Mar2025 live deferred; every-10 1820",
    })
write("research_queue.csv", rqs, rf)

ls, lsf = read("loop_state.csv")
for row in ls:
    if row.get("state_id") == "main":
        row["last_tick_utc"] = NOW
        row["last_unit_id"] = "rq_1813"
        row["ticks_completed"] = "1813"
        row["paused"] = "no"
        row["notes"] = (
            "tick1813 leftover Storm Olen NBB YE2025 bruto 294145 / debt 12103483 / omzet empty / VTE 0; "
            "KBO 0754.810.052; IKA-Storm dual; FOI empty omzet+debt; Pampero YE Mar2025 deferred; "
            "AGB Bornem JR2024; Dijk92/NSZ/APEFE 403; NOT every-10 (next 1820); next rq_1814; continuous hole_fill"
        )
write("loop_state.csv", ls, lsf)

entry = f"""
## Tick 1813 - {NOW} - rq_1813 Storm Olen NV (bruto 0.29m / debt 12.10m)

- Unit: **rq_1813** leftover dual residual after LumIKA; took deferred live **Storm Olen NV** (IKA–Storm dual; KBO **0754.810.052**). Preferred AGB Bornem still JR2024; Dijk92/NSZ/APEFE CDN **403**; FARO NBB YE2025 unpublished.
- Primary (strong, NBB VKT-kap [2026-00117861](http://cdn.staatsbladmonitor.be/2026pdf/2026-00117861.pdf) CDN 200 / 26p; AV **30.04.2026**): assets **EUR14,945,362**; MVA **EUR12,498,634**; IVA **EUR1,023,585**; bruto **EUR294,145** (omzet **70 empty**); expl **EUR292,268**; fin kosten **EUR205,260**; PnL **EUR87,008**; debt **EUR12,103,483** (LT **11,302,471**; gewaarborgd **8,347,864**); cash DROP **EUR1,305,871** (was **2,218,291**); equity **EUR2,841,879**; VTE **0**; dividend **0**; commissaris **EUR3,773**. IKA FVA book stake **EUR672,851**. IKA + Storm Management bestuurders.
- Wrote: entities nv_storm_olen; sources (+3); budgets (+10); commitments (+3); leaderboard; foi_queue ready; research_queue rq_1813=done + rq_1814 spawned; loop_state ticks=1813; FOI draft gap_stormolen_bruto_0_29m_omzet_empty_debt_12_10m_l5.md
- FOI opened: gap_stormolen_bruto_0_29m_omzet_empty_debt_12_10m_l5 (**ready**, human-send only)
- NOT every-10 (next **1820**). Next: rq_1814 (Pampero-if-200 / AGB / Dijk92 / FARO / other Storm / IGS).
"""
with open(Path("docs/doge/loop_log.md"), "a", encoding="utf-8") as f:
    f.write(entry)

print("tick1813 write OK")

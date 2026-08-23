# tick1814 — Pampero Wind NV NBB YE Mar2025 (IKA-Eneco dual; omzet DROP 6.87→2.93m)
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
NOW = "2026-08-25T07:45:00Z"

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
if not any(e.get("entity_id") == "nv_pampero_wind" for e in ents):
    ents.append({
        "entity_id": "nv_pampero_wind",
        "name_nl": "Pampero Wind NV (leftover IKA-Eneco-Campina dual wind; NOT LumIKA / StormOlen)",
        "name_fr": "Pampero Wind SA (dual IKA-Eneco-Campina residuel / projet eolien)",
        "name_en": "Pampero Wind NV leftover IKA-Eneco-Campina dual wind company",
        "level": "other",
        "parent_id": "igs_ika",
        "community_language": "nl",
        "website": "https://ika.vlaanderen/",
        "foi_email": "info@ika.vlaanderen",
        "foi_postal": "Battelsteenweg 455 bus I 2800 Mechelen",
        "notes": (
            "tick1814 leftover IKA dual deferred from Storm Olen 1813; KBO 0670.543.776 Actief; NV; "
            "official NBB VOL-kap YE Mar2025 (01.04.2024-31.03.2025) deposit 2025-00521828 CDN 200 48p; "
            "AV 08.09.2025; ownership Eneco 60pct / Campina Energie 20pct / IKA 20pct; sourced euros "
            "assets 22593925 MVA 19628321 IVA 479751 omzet 2934776 (was 6871652) expl 560779 "
            "pnl -129513 debt 16244775 LT 14613551 cash empty VTE unpublished dividend 200000; "
            "IKA FVA book 1469454.80; FOI ready; AGB Bornem JR2024; Dijk92/NSZ/APEFE 403; NOT every-10 (next 1820)"
        ),
    })
write("entities.csv", ents, ef)

srcs, sf = read("sources.csv")
new_srcs = [
    {
        "source_id": "src_pampero_jr2025_nbb",
        "title": "Pampero Wind official NBB VOL-kap YE Mar2025 deposit 2025-00521828",
        "url": "http://cdn.staatsbladmonitor.be/2025pdf/2025-00521828.pdf",
        "publisher": "NBB / Pampero Wind",
        "accessed_date": "2026-08-25",
        "source_class": "primary_pdf",
        "notes": "tick1814; 48p; AV 08.09.2025; header 01.10.2025; model VOL-kap 23.0.6 m02-f; assets 22593925 omzet 2934776 pnl -129513",
    },
    {
        "source_id": "src_pampero_kbo_0670543776",
        "title": "KBO Public Search Pampero Wind 0670.543.776",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0670543776",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick1814; NV; zetel Battelsteenweg 455/I Mechelen; IKA+Eneco+Campina",
    },
    {
        "source_id": "src_pampero_ika_cross",
        "title": "IKA YE2025 FVA lists Pampero Wind book 1469454.80 (from 2026-00259426)",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00259426.pdf",
        "publisher": "NBB / IKA",
        "accessed_date": "2026-08-25",
        "source_class": "primary_pdf",
        "notes": "tick1814; IKA FVA Pampero 3000 EUR capital notation book 1469454.80; 20pct class C",
    },
]
have = {s["source_id"] for s in srcs}
for s in new_srcs:
    if s["source_id"] not in have:
        srcs.append(s)
write("sources.csv", srcs, sf)

buds, bf = read("budgets.csv")
budget_rows = [
    ("bud_pampero_assets_22_59m_2025", "22593925", "assets YE Mar2025"),
    ("bud_pampero_mva_19_63m_2025", "19628321", "MVA YE Mar2025"),
    ("bud_pampero_omzet_2_93m_2025", "2934776", "omzet 70; was 6871652"),
    ("bud_pampero_pnl_loss_0_13m_2025", "129513", "PnL loss 9904 abs"),
    ("bud_pampero_debt_16_24m_2025", "16244775", "schulden 17/49"),
    ("bud_pampero_lt_debt_14_61m_2025", "14613551", "LT overige leningen 174"),
    ("bud_pampero_equity_6_02m_2025", "6023310", "equity 10/15"),
    ("bud_pampero_expl_0_56m_2025", "560779", "bedrijfswinst 9901"),
    ("bud_pampero_fin_cost_0_67m_2025", "667923", "financiële kosten 65"),
    ("bud_pampero_dividend_0_20m_2025", "200000", "uit te keren winst 694; was 2600000"),
]
have_b = {b.get("budget_id") for b in buds}
for bid, amt, note in budget_rows:
    if bid not in have_b:
        buds.append({
            "budget_id": bid,
            "entity_id": "nv_pampero_wind",
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "NBB VOL-kap YE Mar2025",
            "source_id": "src_pampero_jr2025_nbb",
            "confidence": "strong",
            "notes": f"tick1814; {note}; not TE-additive of 348bn",
        })
write("budgets.csv", buds, bf)

comms, cf = read("commitments.csv")
new_comms = [
    ("comm_pampero_jr2025_omzet_2_93m", "Pampero Wind YE Mar2025 leftover IKA dual (omzet DROP 2.93m / was 6.87m)", "2934776", "Publish PPA/GSC path behind omzet DROP"),
    ("comm_pampero_jr2025_debt_16_24m", "Pampero Wind YE Mar2025 leftover IKA dual (debt 16.24m / LT 14.61m)", "16244775", "Publish LT overige-leningen counterparties"),
    ("comm_pampero_jr2025_loss_0_13m", "Pampero Wind YE Mar2025 leftover IKA dual (PnL loss 0.13m / dividend 0.20m)", "129513", "Explain loss vs dividend + empty cash"),
]
have_c = {c.get("commitment_id") for c in comms}
for cid, title, env, cut in new_comms:
    if cid not in have_c:
        comms.append({
            "commitment_id": cid,
            "title": title,
            "entity_id": "nv_pampero_wind",
            "beneficiary": "IKA municipalities / Eneco / Campina Energie dual",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal dual via IKA 20pct",
            "decision_date": "2025-09-08",
            "start_year": "2024",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2025pdf/2025-00521828.pdf",
            "stated_goal": "Local leftover IKA-Eneco-Campina wind dual map",
            "cut_option": cut,
            "source_id": "src_pampero_jr2025_nbb",
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>Antwerpen>IGS>IKA>PamperoWind>JR2025_L5",
            "notes": "tick1814; NBB primary; FOI ready; not TE-additive of 348bn",
        })
write("commitments.csv", comms, cf)

lbs, lf = read("leaderboard.csv")
if not any(x.get("item_id") == "lb_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5" for x in lbs):
    lbs.append({
        "item_id": "lb_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5",
        "name": "Pampero Wind YE Mar2025: omzet DROP 6.87→2.93m / loss 0.13m / debt 16.24m",
        "level": "L5",
        "type": "renewable_dual",
        "hierarchy_path": "Vlaanderen>Antwerpen>IGS>IKA>PamperoWind",
        "annual_cost_eur": "2934776",
        "total_cost_eur": "16244775",
        "tco_notes": (
            "Envelope=omzet 2934776 (was 6871652; DROP 3936876); assets 22593925 MVA 19628321; "
            "debt 16244775 LT 14613551 overige leningen; pnl -129513 expl 560779 fin cost 667923; "
            "cash empty; equity 6023310; dividend 200000 (was 2.6m); VTE unpublished; "
            "ownership Eneco 60 / Campina 20 / IKA 20; IKA book ~1.47m"
        ),
        "confidence": "strong",
        "source_id": "src_pampero_jr2025_nbb",
        "beneficiaries": "IKA municipalities / Eneco / Campina Energie",
        "stated_goal": "Wind production dual IKA-Eneco-Campina",
        "measured_outcome": "Omzet halves YoY into loss; 16.2m debt; empty cash; 0 published VTE",
        "absurdity_score": "5.5",
        "cost_score": "4.5",
        "difficulty": "4",
        "priority_index": "4.8",
        "cut_proposal": "FOI omzet DROP + LT lenders + empty cash; scrutinise IKA 20pct dual",
        "status": "open",
        "struck_reason": "",
        "notes": "tick1814 leftover IKA dual; strong NBB; not TE-additive; not pure-waste top10",
    })
write("leaderboard.csv", lbs, lf)

fois, ff = read("foi_queue.csv")
if not any(x.get("gap_id") == "gap_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5" for x in fois):
    fois.append({
        "gap_id": "gap_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5",
        "hierarchy_path": "Vlaanderen>Antwerpen>IGS>IKA>PamperoWind>JR2025_L5",
        "entity_id": "nv_pampero_wind",
        "what_is_missing": (
            "Omzet DROP 6.87m→2.93m path; LT overige leningen 14.61m counterparties; empty cash 54/58; "
            "VTE; AV PV 08.09.2025 + dividend 0.20m rationale"
        ),
        "why_it_matters": (
            "IKA 20pct wind dual flips to loss while omzet halves and cash empties — residual opacity after Storm Olen"
        ),
        "priority": "8",
        "recipient_body": "Pampero Wind NV / IKA DV / Eneco Wind Belgium",
        "recipient_email": "info@ika.vlaanderen",
        "recipient_postal": "Battelsteenweg 455 bus I 2800 Mechelen",
        "draft_letter_path": "docs/doge/foi/drafts/gap_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_pampero_jr2025_omzet_2_93m",
        "linked_leaderboard_id": "lb_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "tick1814; human-send only; AGB Bornem JR2024; Dijk92/NSZ/APEFE 403; FARO YE2024 only",
    })
write("foi_queue.csv", fois, ff)

rqs, rf = read("research_queue.csv")
for row in rqs:
    if row.get("task_id") == "rq_1814":
        row["status"] = "done"
        row["entity_id"] = "nv_pampero_wind"
        row["updated_utc"] = NOW
        row["notes"] = (
            "tick1814 done; Pampero Wind NBB 2025-00521828 omzet 2934776 (DROP) debt 16244775 pnl -129513"
        )
if not any(r.get("task_id") == "rq_1815" for r in rqs):
    rqs.append({
        "task_id": "rq_1815",
        "title": "Leftover dual residual hole-fill after Pampero (AGB/NSZ/Dijk92/FARO/APEFE/HVZ/other Storm/IGS)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1815 after 1814 Pampero. Prefer leftover AGB/APB if PDF live unused, else other IKA Storm* "
            "(Geel/Westerlo/Meer/Minderhout/Retie/Zoersel) if CDN 200, else Dijk92 if CDN 200 / FARO NBB YE2025 / "
            "APEFE/NSZ if CDN 200 / HVZ if euros / other IGS. Skip done. Next every-10 1820."
        ),
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned after tick1814; every-10 1820",
    })
write("research_queue.csv", rqs, rf)

ls, lsf = read("loop_state.csv")
for row in ls:
    if row.get("state_id") == "main":
        row["last_tick_utc"] = NOW
        row["last_unit_id"] = "rq_1814"
        row["ticks_completed"] = "1814"
        row["paused"] = "no"
        row["notes"] = (
            "tick1814 leftover Pampero Wind NBB YE Mar2025 omzet 2934776 (DROP from 6871652) / debt 16244775 / "
            "loss 129513; KBO 0670.543.776; Eneco 60 / Campina 20 / IKA 20; FOI omzet DROP+LT debt+cash; "
            "AGB Bornem JR2024; Dijk92/NSZ/APEFE 403; NOT every-10 (next 1820); next rq_1815; continuous hole_fill"
        )
write("loop_state.csv", ls, lsf)

entry = f"""
## Tick 1814 - {NOW} - rq_1814 Pampero Wind NV (omzet DROP 2.93m / debt 16.24m)

- Unit: **rq_1814** leftover dual residual after Storm Olen; took deferred live **Pampero Wind NV** (IKA–Eneco–Campina; KBO **0670.543.776**). Preferred AGB Bornem still JR2024; Dijk92/NSZ/APEFE CDN often **403**; FARO NBB YE2025 unpublished.
- Primary (strong, NBB VOL-kap [2025-00521828](http://cdn.staatsbladmonitor.be/2025pdf/2025-00521828.pdf) CDN 200 / 48p; AV **08.09.2025**; YE **01.04.2024–31.03.2025**): assets **EUR22,593,925**; MVA **EUR19,628,321**; IVA **EUR479,751**; omzet **EUR2,934,776** (was **6,871,652**; DROP **3,936,876**); expl **EUR560,779**; fin kosten **EUR667,923**; PnL **EUR-129,513**; debt **EUR16,244,775** (LT **14,613,551** overige leningen); cash **empty**; equity **EUR6,023,310**; dividend **EUR200,000** (was **2,600,000**); VTE **unpublished**. Ownership: Eneco **60%** / Campina Energie **20%** / IKA **20%**. IKA FVA book **EUR1,469,455**.
- Wrote: entities nv_pampero_wind; sources (+3); budgets (+10); commitments (+3); leaderboard; foi_queue ready; research_queue rq_1814=done + rq_1815 spawned; loop_state ticks=1814; FOI draft gap_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5.md
- FOI opened: gap_pampero_omzet_drop_3_94m_loss_0_13m_debt_16_24m_l5 (**ready**, human-send only)
- NOT every-10 (next **1820**). Next: rq_1815 (other Storm*-if-200 / AGB / Dijk92 / FARO / IGS).
"""
with open(Path("docs/doge/loop_log.md"), "a", encoding="utf-8") as f:
    f.write(entry)

print("tick1814 write OK")

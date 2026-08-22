import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T01:05:00Z"
DATE = "2026-08-24"
EID = "nv_dommelhof_tw"


def read(fn):
    with open(base / fn, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write(fn, fields, rows):
    with open(base / fn, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


fields, rows = read("entities.csv")
assert not any(r["entity_id"] == EID for r in rows)
rows.append(
    {
        "entity_id": EID,
        "name_nl": "Dommelhof NV (leftover property shell dual Campus Dommelhof VZW Tielt-Winge; NOT Limburg culture Dommelhof EVA)",
        "name_fr": "Dommelhof SA (coquille immobiliere duale Campus Dommelhof asbl)",
        "name_en": "Dommelhof NV leftover property shell dual of Campus Dommelhof VZW care home",
        "level": "other",
        "parent_id": "vzw_dommelhof_tw",
        "community_language": "nl",
        "website": "https://www.campusdommelhof.be",
        "foi_email": "info@campusdommelhof.be",
        "foi_postal": "Haksbergstraat 7 3390 Sint-Joris-Winge",
        "notes": "tick1727 leftover Dommelhof NV dual after VZW tick1726; official NBB VKT-kap YE2025 deposit 2026-00238663 CDN 200; KBO 0433.155.577; same Van Roy bestuurders; FOI 70/huur VZW",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_dommelhof_nv_nbb_ye2025",
        "title": "Dommelhof NV NBB VKT-kap YE2025 deposit 2026-00238663",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00238663.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1727; AV 23.06.2026; neergelegd 01.07.2026; assets 12557297 buildings 11947335 debt 11605169 bruto 1234665 pnl 383717",
    },
    {
        "source_id": "src_dommelhof_nv_kbo",
        "title": "Dommelhof NV KBO 0433.155.577",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=433155577",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1727; NV; Haksbergstraat 7 3390 Sint-Joris-Winge",
    },
    {
        "source_id": "src_dommelhof_nv_portal",
        "title": "Campus Dommelhof portal (dual VZW/NV)",
        "url": "https://www.campusdommelhof.be",
        "publisher": "Dommelhof",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1727; WZC campus; NV holds buildings",
    },
    {
        "source_id": "src_dommelhof_nv_foi_contact_1727",
        "title": "Dommelhof NV FOI channel",
        "url": "https://www.campusdommelhof.be",
        "publisher": "Dommelhof NV",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1727; info@campusdommelhof.be; Haksbergstraat 7 3390 Sint-Joris-Winge",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_dommelhof_nv_assets_2025", "2025", "12557297", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB 20/58 assets 12557297; tick1727"),
    ("bud_dommelhof_nv_va_2025", "2025", "11960864", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB VA 21/28 11960864; tick1727"),
    ("bud_dommelhof_nv_buildings_2025", "2025", "11947335", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB terreinen/gebouwen 22 11947335; tick1727"),
    ("bud_dommelhof_nv_inventory_2025", "2025", "559912", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB voorraden 30/36 559912; tick1727"),
    ("bud_dommelhof_nv_cash_2025", "2025", "36304", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB liquide 54/58 36304 DROP vs 68119; tick1727"),
    ("bud_dommelhof_nv_equity_2025", "2025", "952128", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB EV 10/15 952128; tick1727"),
    ("bud_dommelhof_nv_debt_2025", "2025", "11605169", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB schulden 17/49 11605169; tick1727"),
    ("bud_dommelhof_nv_lt_fin_2025", "2025", "10492866", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB LT fin 170/4 10492866; tick1727"),
    ("bud_dommelhof_nv_st_current_lt_2025", "2025", "746729", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB LT within year 42 746729; tick1727"),
    ("bud_dommelhof_nv_hypotheek_book_2025", "2025", "11947335", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB hypotheek book value 91611 11947335; tick1727"),
    ("bud_dommelhof_nv_bruto_2025", "2025", "1234665", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB brutomarge 9900 1234665; 70/60/61 empty; tick1727"),
    ("bud_dommelhof_nv_afschr_2025", "2025", "452263", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB afschr 630 452263; tick1727"),
    ("bud_dommelhof_nv_expl_2025", "2025", "773325", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 773325; tick1727"),
    ("bud_dommelhof_nv_fincost_2025", "2025", "264538", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB fin kosten 65 264538; tick1727"),
    ("bud_dommelhof_nv_pnl_2025", "2025", "383717", "executed", "src_dommelhof_nv_nbb_ye2025", "strong", "NBB PnL 9904 383717; AV 23.06.2026; tick1727"),
]
for bid, year, amt, basis, sid, conf, notes in budgets:
    assert not any(r["budget_id"] == bid for r in rows)
    rows.append(
        {
            "budget_id": bid,
            "entity_id": EID,
            "year": year,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": sid,
            "confidence": conf,
            "notes": notes,
        }
    )
write("budgets.csv", fields, rows)
print("budgets", len(rows))

fields, rows = read("commitments.csv")
rows.append(
    {
        "commitment_id": "comm_dommelhof_nv_jr2025_assets",
        "title": "Dommelhof NV YE2025 leftover property dual WZC (assets 12.56m / debt 11.61m / bruto 1.23m)",
        "entity_id": EID,
        "beneficiary": "Campus Dommelhof VZW / WZC property",
        "legal_basis": "WVV NV; hypothecaire financiering; Bestuursdecreet openbaarheid",
        "decision_date": "2026-06-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1234665",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00238663.pdf",
        "stated_goal": "Local leftover Dommelhof NV dual map — official NBB YE2025; FOI huur VZW",
        "cut_option": "Publish empty 70 rent split vs VZW; scrutinise 11.6m debt on 11.9m buildings; hypotheek path",
        "source_id": "src_dommelhof_nv_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Dommelhof_TW>NV>JR2025_L5",
        "notes": "tick1727; YE2025 dual after VZW; assets 12.56m buildings 11.95m debt 11.61m bruto 1.23m pnl +384k staff empty; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_dommelhof_nv_assets_12_56m_debt_11_61m_bruto_1_23m",
        "name": "Dommelhof NV YE2025 leftover property dual: assets 12.56m / debt 11.61m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Dommelhof_TW>NV>JR2025_L5",
        "annual_cost_eur": "1234665",
        "total_cost_eur": "12557297",
        "tco_notes": "Leftover Dommelhof NV property shell YE2025: assets 12.56m / buildings 11.95m / debt 11.61m (LT fin 10.49m) / bruto 1.23m / pnl +384k / staff empty; hypotheek book 11.95m; dual VZW WZC ops 6.89m bruto; 70/60/61 unpublished",
        "confidence": "strong",
        "source_id": "src_dommelhof_nv_nbb_ye2025",
        "beneficiaries": "WZC Campus Dommelhof / property financiers",
        "stated_goal": "Local leftover Dommelhof NV dual map — official NBB YE2025 after VZW",
        "measured_outcome": "Official NBB YE2025 2026-08-24: assets 12557297 / debt 11605169 / bruto 1234665 / pnl 383717",
        "absurdity_score": "4.5",
        "cost_score": "4.5",
        "difficulty": "2.5",
        "priority_index": "4.0",
        "cut_proposal": "Publish VZW rent matrix for 1.23m bruto; map 11.6m debt vs care subsidy path; hypotheek disclosure",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1727; dual residual after Dommelhof VZW 1726; AGB/NSZ/Dijk92/APEFE still blocked; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_dommelhof_nv_assets_12_56m_debt_11_61m_bruto_1_23m_l5",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Dommelhof_TW>NV>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-kap publishes assets 12557297 / buildings 11947335 / debt 11605169 / bruto 1234665 / pnl 383717; omzet 70 empty / 60/61 empty / staff empty; intercompany huur/leningen with Dommelhof VZW 0443.049.478 unpublished; AV notulen 23.06.2026",
        "why_it_matters": "Leftover property NV dual of VL WZC with 12.56m assets and 11.61m debt — need rent flows vs VZW care ops + debt path",
        "priority": "8",
        "recipient_body": "Dommelhof NV / Bestuursorgaan",
        "recipient_email": "info@campusdommelhof.be",
        "recipient_postal": "Haksbergstraat 7 3390 Sint-Joris-Winge",
        "draft_letter_path": "docs/doge/foi/drafts/gap_dommelhof_nv_assets_12_56m_debt_11_61m_bruto_1_23m_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_dommelhof_nv_jr2025_assets",
        "linked_leaderboard_id": "lb_dommelhof_nv_assets_12_56m_debt_11_61m_bruto_1_23m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1727; human-send only; Dommelhof VZW FOI still ready; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1727":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_dommelhof_nv_assets_12_56m_debt_11_61m_bruto_1_23m_l5"
        r["notes"] = "DONE tick1727: Dommelhof NV KBO 0433.155.577 NBB YE2025 assets 12557297 debt 11605169 bruto 1234665 pnl 383717; FOI ready gap_dommelhof_nv_assets_12_56m_debt_11_61m_bruto_1_23m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1728",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1728 after 1727 Dommelhof NV YE2025 dual. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/KLJ/BoeK/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1727 DommelhofNV; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS; Dommelhof dual DONE; next every-10 1730",
    }
)
write("research_queue.csv", fields, rows)
print("rq", len(rows))

fields, rows = read("loop_state.csv")
assert len(rows) == 1
rows[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1727",
        "ticks_completed": "1727",
        "paused": "no",
        "notes": "tick1727 leftover Dommelhof NV dual residual; KBO 0433.155.577; official NBB VKT-kap YE2025 deposit 2026-00238663 CDN 200; sourced euros assets 12557297 buildings 11947335 debt 11605169 lt_fin 10492866 bruto 1234665 pnl 383717 cash 36304; 70/60/61 empty staff empty; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; NOT every-10 (next 1730); next rq_1728 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

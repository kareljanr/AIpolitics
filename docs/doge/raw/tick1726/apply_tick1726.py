import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T00:45:00Z"
DATE = "2026-08-24"
EID = "vzw_dommelhof_tw"


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
        "name_nl": "Dommelhof VZW / Campus Dommelhof (leftover VL woonzorgcentrum VZW Tielt-Winge; NOT Limburg culture Dommelhof EVA / Dommelhof NV 0433.155.577)",
        "name_fr": "Dommelhof asbl / Campus Dommelhof (maison de repos residuelle Tielt-Winge)",
        "name_en": "Dommelhof VZW Campus Dommelhof leftover Flemish residential care home Tielt-Winge",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.campusdommelhof.be",
        "foi_email": "info@campusdommelhof.be",
        "foi_postal": "Halensebaan 25 3390 Tielt-Winge",
        "notes": "tick1726 leftover VL WZC after AGB/NSZ/Dijk92/APEFE/ABS/Erfpunt-already-1536 hunt; official NBB VKT-VZW YE2025 deposit 2026-00325874 CDN 200; KBO 0443.049.478; FOI 70/73",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_dommelhof_tw_nbb_ye2025",
        "title": "Dommelhof VZW NBB VKT-VZW YE2025 deposit 2026-00325874",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00325874.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1726; AV 16.06.2026; neergelegd 23.07.2026; assets 3198037 bruto 6890095 staff 6613357 VTE 100.7 pnl 39070",
    },
    {
        "source_id": "src_dommelhof_tw_kbo",
        "title": "Dommelhof VZW KBO 0443.049.478",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=443049478",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1726; VZW; Halensebaan 25 3390 Tielt-Winge",
    },
    {
        "source_id": "src_dommelhof_tw_portal",
        "title": "Campus Dommelhof official portal",
        "url": "https://www.campusdommelhof.be",
        "publisher": "Dommelhof VZW",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1726; WZC / zorgcampus Tielt-Winge",
    },
    {
        "source_id": "src_dommelhof_tw_foi_contact_1726",
        "title": "Dommelhof VZW FOI channel",
        "url": "https://www.campusdommelhof.be",
        "publisher": "Dommelhof VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1726; info@campusdommelhof.be; directie@campusdommelhof.be; Halensebaan 25 3390 Tielt-Winge",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_dommelhof_tw_assets_2025", "2025", "3198037", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB 20/58 assets 3198037; tick1726"),
    ("bud_dommelhof_tw_va_2025", "2025", "870272", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB VA 21/28 870272; tick1726"),
    ("bud_dommelhof_tw_mva_2025", "2025", "868395", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB MVA 22/27 868395; tick1726"),
    ("bud_dommelhof_tw_vlottend_2025", "2025", "2327765", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB vlottend 29/58 2327765; tick1726"),
    ("bud_dommelhof_tw_cash_2025", "2025", "794830", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB liquide 54/58 794830 JUMP vs 376909; tick1726"),
    ("bud_dommelhof_tw_recv_2025", "2025", "1035557", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB ST recv 40/41 1035557; tick1726"),
    ("bud_dommelhof_tw_equity_2025", "2025", "630719", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB EV 10/15 630719 (=overgedragen); tick1726"),
    ("bud_dommelhof_tw_debt_2025", "2025", "2567318", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB schulden 17/49 2567318; tick1726"),
    ("bud_dommelhof_tw_lt_fin_2025", "2025", "606305", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB LT fin 170/4 606305; tick1726"),
    ("bud_dommelhof_tw_taxsoc_2025", "2025", "1109210", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB tax/soc 45 1109210 JUMP; tick1726"),
    ("bud_dommelhof_tw_bruto_2025", "2025", "6890095", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB brutomarge 9900 6890095; 70/73/60/61 empty VKT; tick1726"),
    ("bud_dommelhof_tw_staff_2025", "2025", "6613357", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB 62 6613357 / VTE 100.7; tick1726"),
    ("bud_dommelhof_tw_expl_2025", "2025", "65051", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 65051 FLIP vs -208398; tick1726"),
    ("bud_dommelhof_tw_pnl_2025", "2025", "39070", "executed", "src_dommelhof_tw_nbb_ye2025", "strong", "NBB PnL 9904 39070; AV 16.06.2026; tick1726"),
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
        "commitment_id": "comm_dommelhof_tw_jr2025_bruto",
        "title": "Dommelhof VZW YE2025 leftover VL WZC (bruto 6.89m / staff 6.61m VTE 100.7)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Tielt-Winge",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-06-16",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "6890095",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00325874.pdf",
        "stated_goal": "Local leftover Dommelhof WZC map — official NBB YE2025; FOI 70/73",
        "cut_option": "Publish empty 70/73/60/61 RIZIV/care split; scrutinise staff 6.61m of bruto 6.89m (~96%); Dommelhof NV dual",
        "source_id": "src_dommelhof_tw_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Dommelhof_TW>JR2025_L5",
        "notes": "tick1726; YE2025; bruto 6.89m staff 6.61m VTE 100.7 assets 3.20m pnl +39k; not Limburg culture Dommelhof; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_dommelhof_tw_bruto_6_89m_staff_6_61m_vte_100_7",
        "name": "Dommelhof VZW YE2025 leftover VL WZC: bruto 6.89m / staff 6.61m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Dommelhof_TW>JR2025_L5",
        "annual_cost_eur": "6890095",
        "total_cost_eur": "6890095",
        "tco_notes": "Leftover Dommelhof VZW WZC YE2025: bruto 6.89m / staff 6.61m / 100.7 VTE (~96% of bruto) / pnl +39k; 70/73/60/61 unpublished VKT; assets 3.20m cash 0.79m JUMP debt 2.57m; Dommelhof NV dual FOI",
        "confidence": "strong",
        "source_id": "src_dommelhof_tw_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff",
        "stated_goal": "Local leftover Dommelhof WZC map — official NBB YE2025 after AGB/IOED blocks",
        "measured_outcome": "Official NBB YE2025 2026-08-24: bruto 6890095 / staff 6613357 VTE 100.7 / pnl 39070 / assets 3198037",
        "absurdity_score": "4.0",
        "cost_score": "4.0",
        "difficulty": "2.5",
        "priority_index": "3.6",
        "cut_proposal": "Publish 70/73 RIZIV/dagprijs split; scrutinise staff share ~96% of bruto; map Dommelhof NV flows",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1726; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / ABS+BVAS no NBB / Erfpunt already 1536; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_dommelhof_bruto_6_89m_staff_6_61m_omzet_empty_l5",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Dommelhof_TW>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes bruto 6890095 / staff 6613357 VTE 100.7 / pnl 39070 / assets 3198037; omzet 70 empty / 73 empty / 60/61 empty; Dommelhof NV 0433.155.577 dual flows; AV notulen 16.06.2026",
        "why_it_matters": "Leftover VL WZC with live official YE2025 euros (6.89m bruto / 6.61m staff ~96%) — need RIZIV/care funding opacity + NV relation",
        "priority": "7",
        "recipient_body": "Dommelhof VZW / Bestuursorgaan",
        "recipient_email": "info@campusdommelhof.be",
        "recipient_postal": "Halensebaan 25 3390 Tielt-Winge",
        "draft_letter_path": "docs/doge/foi/drafts/gap_dommelhof_bruto_6_89m_staff_6_61m_omzet_empty_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_dommelhof_tw_jr2025_bruto",
        "linked_leaderboard_id": "lb_dommelhof_tw_bruto_6_89m_staff_6_61m_vte_100_7",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1726; human-send only; AGB/NSZ/Dijk92/APEFE still blocked; Erfpunt already mined 1536",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1726":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_dommelhof_bruto_6_89m_staff_6_61m_omzet_empty_l5"
        r["notes"] = "DONE tick1726: Dommelhof VZW KBO 0443.049.478 NBB YE2025 bruto 6890095 staff 6613357 VTE 100.7; FOI ready gap_dommelhof_bruto_6_89m_staff_6_61m_omzet_empty_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1727",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1727 after 1726 Dommelhof VZW YE2025. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/KLJ/BoeK/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Dommelhof NV dual optional, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1726 DommelhofTW; NEXT AGB/NSZ-if-200/DommelhofNV/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS; DommelhofTW+GO!+Natuurpunt+OVSG DONE; Erfpunt already 1536; next every-10 1730",
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
        "last_unit_id": "rq_1726",
        "ticks_completed": "1726",
        "paused": "no",
        "notes": "tick1726 leftover Dommelhof VZW WZC residual; KBO 0443.049.478; official NBB VKT-VZW YE2025 deposit 2026-00325874 CDN 200; sourced euros assets 3198037 bruto 6890095 staff 6613357 VTE 100.7 pnl 39070 cash 794830; 70/73 empty; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; Erfpunt already tick1536; NOT every-10 (next 1730); next rq_1727 AGB/NSZ-if-200/DommelhofNV/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

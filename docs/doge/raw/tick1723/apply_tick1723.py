import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T23:45:00Z"
DATE = "2026-08-23"
EID = "vzw_ovsg"


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
        "name_nl": "OVSG vzw / Onderwijsvereniging van Steden en Gemeenten (leftover VL municipal-education koepel; NOT KOV / GO! / POV)",
        "name_fr": "OVSG asbl / Association d enseignement des villes et communes (residuelle)",
        "name_en": "OVSG leftover Flemish municipal/urban education network VZW",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.ovsg.be",
        "foi_email": "an.vanwetter@ovsg.be",
        "foi_postal": "Bischoffsheimlaan 1-8 1000 Brussel",
        "notes": "tick1723 leftover OVSG after AGB/NatuurpuntVZW/NSZ/ABS/BVAS/GO!/POV hunt; official NBB VKT-VZW YE2025 deposit 2026-00165833 CDN 200; KBO 0443.649.492; FOI 70/73",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_ovsg_nbb_ye2025",
        "title": "OVSG NBB VKT-VZW YE2025 deposit 2026-00165833",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00165833.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1723; AV 10.06.2026; neergelegd 11.06.2026; assets 8546962 bruto 1734552 staff 1162662 VTE 22.3 kapsubs 455000 pnl 274103",
    },
    {
        "source_id": "src_ovsg_kbo",
        "title": "OVSG KBO 0443.649.492",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=443649492",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1723; VZW; Bischoffsheimlaan 1-8 1000 Brussel",
    },
    {
        "source_id": "src_ovsg_portal",
        "title": "OVSG official portal",
        "url": "https://www.ovsg.be",
        "publisher": "OVSG vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1723; VL municipal/urban education network",
    },
    {
        "source_id": "src_ovsg_foi_contact_1723",
        "title": "OVSG FOI channel",
        "url": "https://www.ovsg.be",
        "publisher": "OVSG vzw",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1723; an.vanwetter@ovsg.be; Bischoffsheimlaan 1-8 1000 Brussel",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_ovsg_assets_2025", "2025", "8546962", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB 20/58 assets 8546962; tick1723"),
    ("bud_ovsg_va_2025", "2025", "3681516", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB VA 21/28 3681516; tick1723"),
    ("bud_ovsg_buildings_2025", "2025", "3594826", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB terreinen/gebouwen 22 3594826; tick1723"),
    ("bud_ovsg_vlottend_2025", "2025", "4865446", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB vlottend 29/58 4865446; tick1723"),
    ("bud_ovsg_cash_2025", "2025", "3596329", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB liquide 54/58 3596329 JUMP vs 2880969; tick1723"),
    ("bud_ovsg_beleg_2025", "2025", "1000000", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB beleggingen 50/53 1000000; tick1723"),
    ("bud_ovsg_equity_2025", "2025", "6134114", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB EV 10/15 6134114; tick1723"),
    ("bud_ovsg_kapsubs_2025", "2025", "455000", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB kapitaalsubsidies 15 455000; tick1723"),
    ("bud_ovsg_debt_2025", "2025", "2412848", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB schulden 17/49 2412848; tick1723"),
    ("bud_ovsg_bruto_2025", "2025", "1734552", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB brutomarge 9900 1734552; 70/73 empty VKT; tick1723"),
    ("bud_ovsg_staff_2025", "2025", "1162662", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB 62 1162662 / VTE 22.3; tick1723"),
    ("bud_ovsg_expl_2025", "2025", "240976", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 240976; tick1723"),
    ("bud_ovsg_pnl_2025", "2025", "274103", "executed", "src_ovsg_nbb_ye2025", "strong", "NBB PnL 9904 274103; AV 10.06.2026; tick1723"),
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
        "commitment_id": "comm_ovsg_jr2025_bruto",
        "title": "OVSG YE2025 leftover VL municipal-education koepel (bruto 1.73m / staff 1.16m VTE 22.3)",
        "entity_id": EID,
        "beneficiary": "VL municipal/urban school boards via OVSG",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; officieel gesubsidieerd onderwijs",
        "decision_date": "2026-06-10",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1734552",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00165833.pdf",
        "stated_goal": "Local leftover OVSG map — official NBB YE2025; FOI 70/73",
        "cut_option": "Publish empty 70/73/60/61 split; scrutinise staff 1.16m of bruto 1.73m; kapsubs 455k path",
        "source_id": "src_ovsg_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>OVSG>JR2025_L5",
        "notes": "tick1723; YE2025; bruto 1.73m staff 1.16m VTE 22.3 assets 8.55m kapsubs 455k pnl +274k; dual residual after KOV; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_ovsg_bruto_1_73m_staff_1_16m_vte_22_3",
        "name": "OVSG YE2025 leftover VL municipal-education koepel: bruto 1.73m / staff 1.16m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Onderwijs>OVSG>JR2025_L5",
        "annual_cost_eur": "1734552",
        "total_cost_eur": "1734552",
        "tco_notes": "Leftover OVSG VZW YE2025: bruto 1.73m / staff 1.16m / 22.3 VTE / pnl +274k / kapsubs 455k; 70/73/60/61 unpublished VKT; assets 8.55m cash 3.60m debt 2.41m; dual residual after KOV",
        "confidence": "strong",
        "source_id": "src_ovsg_nbb_ye2025",
        "beneficiaries": "VL municipal/urban school boards / pupils",
        "stated_goal": "Local leftover OVSG map — official NBB YE2025 after KOV/education duals",
        "measured_outcome": "Official NBB YE2025 2026-08-23: bruto 1734552 / staff 1162662 VTE 22.3 / pnl 274103 / assets 8546962",
        "absurdity_score": "3.5",
        "cost_score": "3.0",
        "difficulty": "2.5",
        "priority_index": "3.2",
        "cut_proposal": "Publish 70/73 subsidy/lidgeld split; scrutinise staff share ~67% of bruto; kapsubs 455k reconciliation",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1723; leftover after AGB unpublished / NSZ CDN403 / NatuurpuntVZW CDN403 / ABS+BVAS no NBB / GO!+POV thin; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_ovsg_bruto_1_73m_staff_1_16m_omzet_empty_l5",
        "hierarchy_path": "Vlaanderen>Onderwijs>OVSG>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes bruto 1734552 / staff 1162662 VTE 22.3 / pnl 274103 / assets 8546962 / kapsubs 455000; omzet 70 empty / 73 empty / 60/61 empty; AV notulen 10.06.2026",
        "why_it_matters": "Leftover VL municipal-education koepel with live official YE2025 euros (1.73m bruto / 1.16m staff / 455k kapsubs) — need 70/73 opacity + public funding path",
        "priority": "7",
        "recipient_body": "OVSG vzw / Bestuursorgaan",
        "recipient_email": "an.vanwetter@ovsg.be",
        "recipient_postal": "Bischoffsheimlaan 1-8 1000 Brussel",
        "draft_letter_path": "docs/doge/foi/drafts/gap_ovsg_bruto_1_73m_staff_1_16m_omzet_empty_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_ovsg_jr2025_bruto",
        "linked_leaderboard_id": "lb_ovsg_bruto_1_73m_staff_1_16m_vte_22_3",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1723; human-send only; KOV FOI still ready if any; AGB/NSZ/NatuurpuntVZW still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1723":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_ovsg_bruto_1_73m_staff_1_16m_omzet_empty_l5"
        r["notes"] = "DONE tick1723: OVSG KBO 0443.649.492 NBB YE2025 bruto 1734552 staff 1162662 VTE 22.3 kapsubs 455000; FOI ready gap_ovsg_bruto_1_73m_staff_1_16m_omzet_empty_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1724",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1724 after 1723 OVSG YE2025. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo OVSG/KOV/KLJ/BoeK/LandelijkeGilden/Boerenbond/BIV/LaScam/deAuteurs/SACD/FARO/SOFAM/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, ABS/GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1723 OVSG; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS; OVSG+KOV DONE; next every-10 1730",
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
        "last_unit_id": "rq_1723",
        "ticks_completed": "1723",
        "paused": "no",
        "notes": "tick1723 leftover OVSG VZW residual; KBO 0443.649.492; official NBB VKT-VZW YE2025 deposit 2026-00165833 CDN 200; sourced euros assets 8546962 bruto 1734552 staff 1162662 VTE 22.3 kapsubs 455000 pnl 274103 cash 3596329; 70/73 empty; FOI ready; NSZ still CDN 403; NatuurpuntVZW YE2024 CDN 403; ABS/BVAS no NBB; AGB unpublished; NOT every-10 (next 1730); next rq_1724 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

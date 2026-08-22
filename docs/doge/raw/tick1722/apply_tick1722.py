import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T23:25:00Z"
DATE = "2026-08-23"
EID = "vzw_klj_groene_kring"


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
        "name_nl": "KLJ & Groene Kring vzw (leftover VL rural youth / young farmers; NOT Boerenbond / Landelijke Gilden / BoeK)",
        "name_fr": "KLJ & Groene Kring asbl (residuelle jeunesse rurale flamande)",
        "name_en": "KLJ & Groene Kring leftover Flemish rural youth VZW",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.groenekring.be",
        "foi_email": "info@groenekring.be",
        "foi_postal": "Diestsevest 32 bus 3B 3000 Leuven",
        "notes": "tick1722 leftover KLJ/Groene Kring after BoeK/Boerenbond/AGB hunt; official NBB VKT-VZW YE2025 deposit 2026-00072876 CDN 200; KBO 0408.659.020; FOI 70/73",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_klj_nbb_ye2025",
        "title": "KLJ & Groene Kring NBB VKT-VZW YE2025 deposit 2026-00072876",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00072876.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1722; AV 24.03.2026; neergelegd 30.03.2026; assets 2437835 bruto 2478479 staff 2199065 VTE 30.8 pnl 76606",
    },
    {
        "source_id": "src_klj_kbo",
        "title": "KLJ & Groene Kring KBO 0408.659.020",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=408659020",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1722; VZW; Diestsevest 32/3B 3000 Leuven",
    },
    {
        "source_id": "src_klj_portal",
        "title": "Groene Kring / KLJ official portal",
        "url": "https://www.groenekring.be",
        "publisher": "KLJ & Groene Kring vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1722; Boerenbond-adjacent rural youth",
    },
    {
        "source_id": "src_klj_foi_contact_1722",
        "title": "KLJ & Groene Kring FOI channel",
        "url": "https://www.groenekring.be",
        "publisher": "KLJ & Groene Kring vzw",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1722; info@groenekring.be; Diestsevest 32 bus 3B 3000 Leuven",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_klj_assets_2025", "2025", "2437835", "executed", "src_klj_nbb_ye2025", "strong", "NBB 20/58 assets 2437835; tick1722"),
    ("bud_klj_va_2025", "2025", "233419", "executed", "src_klj_nbb_ye2025", "strong", "NBB VA 21/28 233419; tick1722"),
    ("bud_klj_vlottend_2025", "2025", "2204416", "executed", "src_klj_nbb_ye2025", "strong", "NBB vlottend 29/58 2204416; tick1722"),
    ("bud_klj_cash_2025", "2025", "1132491", "executed", "src_klj_nbb_ye2025", "strong", "NBB liquide 54/58 1132491 JUMP vs 885707; tick1722"),
    ("bud_klj_beleg_2025", "2025", "300000", "executed", "src_klj_nbb_ye2025", "strong", "NBB beleggingen 50/53 300000; tick1722"),
    ("bud_klj_equity_2025", "2025", "823677", "executed", "src_klj_nbb_ye2025", "strong", "NBB EV 10/15 823677; tick1722"),
    ("bud_klj_debt_2025", "2025", "1614158", "executed", "src_klj_nbb_ye2025", "strong", "NBB schulden 17/49 1614158 (ST 673589 + overlopend 940569); tick1722"),
    ("bud_klj_bruto_2025", "2025", "2478479", "executed", "src_klj_nbb_ye2025", "strong", "NBB brutomarge 9900 2478479; 70/73 empty VKT; tick1722"),
    ("bud_klj_staff_2025", "2025", "2199065", "executed", "src_klj_nbb_ye2025", "strong", "NBB 62 2199065 / VTE 30.8; tick1722"),
    ("bud_klj_expl_2025", "2025", "72856", "executed", "src_klj_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 72856; tick1722"),
    ("bud_klj_pnl_2025", "2025", "76606", "executed", "src_klj_nbb_ye2025", "strong", "NBB PnL 9904 76606; AV 24.03.2026; tick1722"),
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
        "commitment_id": "comm_klj_jr2025_bruto",
        "title": "KLJ & Groene Kring YE2025 leftover VL rural youth (bruto 2.48m / staff 2.20m VTE 30.8)",
        "entity_id": EID,
        "beneficiary": "VL rural youth / young farmers via KLJ & Groene Kring",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; Boerenbond-adjacent youth",
        "decision_date": "2026-03-24",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "2478479",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00072876.pdf",
        "stated_goal": "Local leftover KLJ/Groene Kring map — official NBB YE2025; FOI 70/73",
        "cut_option": "Publish empty 70/73/60/61 split; scrutinise staff 2.20m of bruto 2.48m; Boerenbond funding relation",
        "source_id": "src_klj_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Jeugd>KLJ_GroeneKring>JR2025_L5",
        "notes": "tick1722; YE2025; bruto 2.48m staff 2.20m VTE 30.8 assets 2.44m pnl +77k; near Boerenbond Diestsevest; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_klj_bruto_2_48m_staff_2_20m_vte_30_8",
        "name": "KLJ & Groene Kring YE2025 leftover VL rural youth: bruto 2.48m / staff 2.20m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Jeugd>KLJ_GroeneKring>JR2025_L5",
        "annual_cost_eur": "2478479",
        "total_cost_eur": "2478479",
        "tco_notes": "Leftover KLJ/Groene Kring VZW YE2025: bruto 2.48m / staff 2.20m / 30.8 VTE / pnl +77k; 70/73/60/61 unpublished VKT; assets 2.44m cash 1.13m debt 1.61m; colocated Boerenbond area Leuven",
        "confidence": "strong",
        "source_id": "src_klj_nbb_ye2025",
        "beneficiaries": "VL rural youth / young farmers",
        "stated_goal": "Local leftover KLJ/Groene Kring map — official NBB YE2025 after BoeK/Boerenbond",
        "measured_outcome": "Official NBB YE2025 2026-08-23: bruto 2478479 / staff 2199065 VTE 30.8 / pnl 76606 / assets 2437835",
        "absurdity_score": "4.0",
        "cost_score": "3.5",
        "difficulty": "2.5",
        "priority_index": "3.7",
        "cut_proposal": "Publish 70/73 subsidy/lidgeld split; scrutinise staff share ~89% of bruto; clarify Boerenbond relation",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1722; leftover after AGB unpublished / NSZ CDN403 / BoeK+Boerenbond done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_klj_bruto_2_48m_staff_2_20m_omzet_empty_l5",
        "hierarchy_path": "Vlaanderen>Jeugd>KLJ_GroeneKring>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes bruto 2478479 / staff 2199065 VTE 30.8 / pnl 76606 / assets 2437835; omzet 70 empty / 73 empty / 60/61 empty; Boerenbond/Landelijke Gilden funding relation Unknown; AV notulen 24.03.2026",
        "why_it_matters": "Leftover VL rural youth VZW with live official YE2025 euros (2.48m bruto / 2.20m staff) — need 70/73 opacity + Boerenbond relation",
        "priority": "7",
        "recipient_body": "KLJ & Groene Kring vzw / Bestuursorgaan",
        "recipient_email": "info@groenekring.be",
        "recipient_postal": "Diestsevest 32 bus 3B 3000 Leuven",
        "draft_letter_path": "docs/doge/foi/drafts/gap_klj_bruto_2_48m_staff_2_20m_omzet_empty_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_klj_jr2025_bruto",
        "linked_leaderboard_id": "lb_klj_bruto_2_48m_staff_2_20m_vte_30_8",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1722; human-send only; BoeK/Boerenbond/LandelijkeGilden FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1722":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_klj_bruto_2_48m_staff_2_20m_omzet_empty_l5"
        r["notes"] = "DONE tick1722: KLJ/Groene Kring KBO 0408.659.020 NBB YE2025 bruto 2478479 staff 2199065 VTE 30.8; FOI ready gap_klj_bruto_2_48m_staff_2_20m_omzet_empty_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1723",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1723 after 1722 KLJ/Groene Kring YE2025. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo KLJ/BoeK/LandelijkeGilden/Boerenbond/BIV/LaScam/deAuteurs/SACD/FARO/SOFAM/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, ABS/GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1722 KLJ; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS; KLJ+BoeK+Boerenbond DONE; next every-10 1730",
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
        "last_unit_id": "rq_1722",
        "ticks_completed": "1722",
        "paused": "no",
        "notes": "tick1722 leftover KLJ & Groene Kring VZW residual; KBO 0408.659.020; official NBB VKT-VZW YE2025 deposit 2026-00072876 CDN 200; sourced euros assets 2437835 bruto 2478479 staff 2199065 VTE 30.8 pnl 76606 cash 1132491; 70/73 empty; FOI ready; NSZ still CDN 403; AGB unpublished; NOT every-10 (next 1730); next rq_1723 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

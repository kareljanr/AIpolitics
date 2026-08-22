import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T22:25:00Z"
DATE = "2026-08-23"
EID = "vzw_landelijke_gilden"


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
        "name_nl": "Landelijke Gilden vzw (leftover VL rural education/association under Boerenbond koepel; NOT Boerenbond / Ferm)",
        "name_fr": "Landelijke Gilden asbl (residuelle association rurale flamande)",
        "name_en": "Landelijke Gilden leftover Flemish rural guilds VZW",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.landelijkegilden.be",
        "foi_email": "info@landelijkegilden.be",
        "foi_postal": "Diestsevest 40 3000 Leuven",
        "notes": "tick1719 leftover Landelijke Gilden dual Boerenbond after AGB/NSZ hunt; official NBB VKT-VZW YE2025 deposit 2026-00263053 CDN 200; KBO 0410.028.601; FOI 70/73 split",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_lgilden_nbb_ye2025",
        "title": "Landelijke Gilden NBB VKT-VZW YE2025 deposit 2026-00263053",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00263053.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1719; AV 25.03.2026; neergelegd 08.07.2026; assets 1752932 bruto 3827855 staff 3641141 VTE 35.4; 70/73/60/61 empty VKT",
    },
    {
        "source_id": "src_lgilden_kbo",
        "title": "Landelijke Gilden KBO 0410.028.601",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=410028601",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1719; VZW; Diestsevest 40 3000 Leuven (same as Boerenbond)",
    },
    {
        "source_id": "src_lgilden_portal",
        "title": "Landelijke Gilden.be official portal",
        "url": "https://www.landelijkegilden.be",
        "publisher": "Landelijke Gilden vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1719; Boerenbond koepel partner",
    },
    {
        "source_id": "src_lgilden_foi_contact_1719",
        "title": "Landelijke Gilden FOI channel",
        "url": "https://www.landelijkegilden.be",
        "publisher": "Landelijke Gilden vzw",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1719; Diestsevest 40 3000 Leuven; via Boerenbond boekhouding if needed",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_lgilden_assets_2025", "2025", "1752932", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB 20/58 assets 1752932; tick1719"),
    ("bud_lgilden_va_2025", "2025", "230073", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB VA 21/28 230073 (IVA 214418 MVA 15630); tick1719"),
    ("bud_lgilden_vlottend_2025", "2025", "1522859", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB vlottend 29/58 1522859; tick1719"),
    ("bud_lgilden_cash_2025", "2025", "412400", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB liquide 54/58 412400 UP vs 364228; tick1719"),
    ("bud_lgilden_debt_2025", "2025", "1724265", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB schulden 17/49 1724265; EV codes empty (passiva=voorz+schulden); tick1719"),
    ("bud_lgilden_voorzieningen_2025", "2025", "28667", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB voorzieningen 16 28667; tick1719"),
    ("bud_lgilden_bruto_2025", "2025", "3827855", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB brutomarge 9900 3827855; 70/73 empty VKT; tick1719"),
    ("bud_lgilden_staff_2025", "2025", "3641141", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB 62 3641141 / VTE 35.4; tick1719"),
    ("bud_lgilden_afschr_2025", "2025", "185938", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB 630 afschrijvingen 185938; tick1719"),
    ("bud_lgilden_expl_2025", "2025", "-1185", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 -1185; tick1719"),
    ("bud_lgilden_pnl_before_tax_2025", "2025", "9", "executed", "src_lgilden_nbb_ye2025", "strong", "NBB 9903 9; tax 9; 9904 empty ~0; tick1719"),
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
        "commitment_id": "comm_lgilden_jr2025_bruto",
        "title": "Landelijke Gilden YE2025 leftover VL rural assoc dual Boerenbond (bruto 3.83m / staff 3.64m VTE 35.4)",
        "entity_id": EID,
        "beneficiary": "Landelijke Gilden members / VL rural communities",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; Boerenbond koepel partner",
        "decision_date": "2026-03-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "3827855",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00263053.pdf",
        "stated_goal": "Local leftover Landelijke Gilden dual Boerenbond — official NBB YE2025; FOI 70/73",
        "cut_option": "Publish empty 70/73/60/61 split; scrutinise staff 3.64m nearly absorbing bruto 3.83m; relation to Boerenbond subsidies",
        "source_id": "src_lgilden_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Lobby>LandelijkeGilden>JR2025_L5",
        "notes": "tick1719; YE2025; bruto 3.83m staff 3.64m VTE 35.4 assets 1.75m EV empty; same address as Boerenbond; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_lgilden_bruto_3_83m_staff_3_64m_vte_35_4",
        "name": "Landelijke Gilden YE2025 leftover VL rural assoc dual Boerenbond: bruto 3.83m / staff 3.64m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Lobby>LandelijkeGilden>JR2025_L5",
        "annual_cost_eur": "3827855",
        "total_cost_eur": "3827855",
        "tco_notes": "Leftover Landelijke Gilden VZW YE2025: bruto 3.83m almost entirely staff 3.64m / 35.4 VTE; 70/73/60/61 unpublished VKT; assets 1.75m debt 1.72m EV empty; colocated Boerenbond Diestsevest 40",
        "confidence": "strong",
        "source_id": "src_lgilden_nbb_ye2025",
        "beneficiaries": "VL rural guild members via Landelijke Gilden",
        "stated_goal": "Local leftover Landelijke Gilden dual Boerenbond — official NBB YE2025 CDN live",
        "measured_outcome": "Official NBB YE2025 2026-08-23: bruto 3827855 / staff 3641141 VTE 35.4 / assets 1752932",
        "absurdity_score": "5.0",
        "cost_score": "5.0",
        "difficulty": "2.5",
        "priority_index": "4.8",
        "cut_proposal": "Publish 70/73 subsidy/lidgeld split; scrutinise near 1:1 staff/bruto; clarify Boerenbond funding flows",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1719; leftover after AGB unpublished / NSZ CDN403 / Boerenbond done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_lgilden_bruto_3_83m_staff_3_64m_omzet_empty_l5",
        "hierarchy_path": "Vlaanderen>Lobby>LandelijkeGilden>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes bruto 3827855 / staff 3641141 VTE 35.4 / assets 1752932 / debt 1724265 / EV codes empty / expl -1185; omzet 70 empty / 73 empty / 60/61 empty; Boerenbond funding/doorstorting split Unknown; AV notulen 25.03.2026",
        "why_it_matters": "Leftover VL rural assoc dual Boerenbond with live official YE2025 euros (3.83m bruto ~all staff) — need 70/73 opacity + Boerenbond relation",
        "priority": "7",
        "recipient_body": "Landelijke Gilden vzw / Bestuursorgaan",
        "recipient_email": "info@landelijkegilden.be",
        "recipient_postal": "Diestsevest 40 3000 Leuven",
        "draft_letter_path": "docs/doge/foi/drafts/gap_lgilden_bruto_3_83m_staff_3_64m_omzet_empty_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_lgilden_jr2025_bruto",
        "linked_leaderboard_id": "lb_lgilden_bruto_3_83m_staff_3_64m_vte_35_4",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1719; human-send only; Boerenbond FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1719":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_lgilden_bruto_3_83m_staff_3_64m_omzet_empty_l5"
        r["notes"] = "DONE tick1719: Landelijke Gilden KBO 0410.028.601 NBB YE2025 bruto 3827855 staff 3641141 VTE 35.4 assets 1752932; FOI ready gap_lgilden_bruto_3_83m_staff_3_64m_omzet_empty_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1720",
        "title": "Mandatory progress@1720 coverage % layers A-E + waste top10",
        "sprint": "hole_fill",
        "priority": "10",
        "status": "open",
        "hierarchy_target": "L0",
        "entity_id": "gg_belgium",
        "instructions": "EVERY-10 tick 1720 MANDATORY: refresh progress_every_10_ticks.md + doge_waste_top10_current.md after VL residual 1711-1719 (Welzijnszorg SOFAM FARO SACD deAuteurs LaScam BIV Boerenbond LandelijkeGilden). Optionally one small primary fill if time. Then spawn rq_1721.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1719 Landelijke Gilden; EVERY-10 progress@1720 next",
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
        "last_unit_id": "rq_1719",
        "ticks_completed": "1719",
        "paused": "no",
        "notes": "tick1719 leftover Landelijke Gilden VZW dual Boerenbond; KBO 0410.028.601; official NBB VKT-VZW YE2025 deposit 2026-00263053 CDN 200; sourced euros assets 1752932 bruto 3827855 staff 3641141 VTE 35.4 debt 1724265 expl -1185; 70/73 empty; FOI ready; NSZ still CDN 403; AGB unpublished; NOT every-10 (NEXT 1720 MANDATORY progress+waste); next rq_1720 every-10 then AGB/Natuurpunt/NSZ/Bosgroep/Dijk92/APEFE/GO!/POV/BVAS/IOED/HVZ/IGS; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

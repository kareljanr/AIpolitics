import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T06:45:00Z"
DATE = "2026-08-24"
EID = "vzw_familiehof"
GAP = "gap_familiehof_bruto_3_98m_equity_neg_0_67m_comfort_l5"
COMM = "comm_familiehof_jr2025_bruto"
LB = "lb_familiehof_bruto_3_98m_equity_neg_0_67m_comfort"


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
        "name_nl": "Familiehof VZW (leftover VL WZC Schelle / Vivalto; dual Akapella deposit+1; NEG equity + comfort brief; NOT Akapella)",
        "name_fr": "Maison de repos Familiehof asbl (residuelle Schelle / Vivalto)",
        "name_en": "Familiehof residential care VZW leftover Flemish WZC Schelle Vivalto dual Akapella comfort letter",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vivaltohome.com/nl/maisons/familiehof/",
        "foi_email": "inge.vanbouwel@vivaltohome.com",
        "foi_postal": "Provinciale Steenweg 323 2627 Schelle",
        "notes": "tick1744 leftover Vivalto WZC after Akapella; official NBB VKT-VZW YE2025 deposit 2026-00139429 CDN 200; KBO 0474.243.193; equity NEG 666897 + Vivalto comfort letter to AV2027; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_familiehof_nbb_ye2025",
        "title": "Familiehof VZW NBB VKT-VZW YE2025 deposit 2026-00139429",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139429.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1744; AV 13.05.2026; assets 1976358 bruto 3982577 staff 3731195 VTE 64.9 pnl 130955 equity NEG 666897 debt 2643255; Vivalto comfort; Mazars zonder voorbehoud",
    },
    {
        "source_id": "src_familiehof_kbo",
        "title": "Familiehof VZW KBO 0474.243.193",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=474243193",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1744; VZW; Provinciale Steenweg 323 2627 Schelle",
    },
    {
        "source_id": "src_familiehof_portal",
        "title": "Familiehof Vivalto Home portal",
        "url": "https://www.vivaltohome.com/nl/maisons/familiehof/",
        "publisher": "Vivalto Home / Familiehof",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1744; WZC Schelle; inge.vanbouwel@vivaltohome.com; tel 03/887.00.19",
    },
    {
        "source_id": "src_familiehof_foi_contact_1744",
        "title": "Familiehof FOI channel",
        "url": "https://www.vivaltohome.com/nl/maisons/familiehof/",
        "publisher": "Familiehof VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1744; inge.vanbouwel@vivaltohome.com; Provinciale Steenweg 323 2627 Schelle",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_familiehof_assets_2025", "2025", "1976358", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB 20/58 assets 1976358 DROP vs 2248934; tick1744"),
    ("bud_familiehof_va_2025", "2025", "190899", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB VA 190899; tick1744"),
    ("bud_familiehof_vlottend_2025", "2025", "1785460", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB vlottend 1785460 DROP; tick1744"),
    ("bud_familiehof_cash_2025", "2025", "277765", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB liquide 277765 DROP vs 363678; tick1744"),
    ("bud_familiehof_andere_recv_2025", "2025", "760083", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB andere vorderingen 760083 DROP vs 1052568; FOI group; tick1744"),
    ("bud_familiehof_equity_2025", "2025", "-666897", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB EV NEG 666897 (improved vs NEG 797852); Vivalto comfort brief; tick1744"),
    ("bud_familiehof_debt_2025", "2025", "2643255", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB schulden 2643255; LT fin 1397990 of which other loans 1388689; tick1744"),
    ("bud_familiehof_bruto_2025", "2025", "3982577", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB brutomarge 9900 3982577; 70/73 empty VKT; tick1744"),
    ("bud_familiehof_staff_2025", "2025", "3731195", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB 62 3731195 / VTE 64.9 DROP vs 73.1; tick1744"),
    ("bud_familiehof_expl_2025", "2025", "178840", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 178840; tick1744"),
    ("bud_familiehof_pnl_2025", "2025", "130955", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB PnL 9904 130955 (vs -12357); AV 13.05.2026; Mazars zonder voorbehoud; tick1744"),
    ("bud_familiehof_lt_other_loans_2025", "2025", "1388689", "executed", "src_familiehof_nbb_ye2025", "strong", "NBB LT overige leningen 1388689; FOI creditor; tick1744"),
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
        "commitment_id": COMM,
        "title": "Familiehof YE2025 leftover VL WZC (bruto 3.98m / equity NEG 0.67m / Vivalto comfort)",
        "entity_id": EID,
        "beneficiary": "WZC residents Schelle / Vivalto group (comfort letter dependent)",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-13",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "3982577",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139429.pdf",
        "stated_goal": "Local leftover Familiehof WZC map — official NBB YE2025 Vivalto dual; FOI NEG equity + comfort brief",
        "cut_option": "Publish RIZIV bruto split; disclose LT other-loan creditor 1.39m; publish Vivalto comfort-letter terms and group cash/recv flows",
        "source_id": "src_familiehof_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Familiehof>JR2025_L5",
        "notes": "tick1744; YE2025 VKT; bruto 3.98m staff 3.73m VTE 64.9 pnl +131k assets 1.98m equity NEG 0.67m + comfort; dual Akapella deposit-1; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Familiehof YE2025: bruto 3.98m / equity NEG 0.67m / Vivalto comfort",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Familiehof>JR2025_L5",
        "annual_cost_eur": "3982577",
        "total_cost_eur": "3982577",
        "tco_notes": "Leftover Vivalto Familiehof WZC YE2025 VKT: bruto 3.98m (70/73 empty) / staff 3.73m VTE 64.9 DROP vs 73.1 / pnl +131k (vs -12k); assets DROP 2.25m→1.98m / equity NEG 0.67m (improved vs NEG 0.80m) with Vivalto Home Belgium comfort brief to AV2027 covering YE2026; debt 2.64m incl LT other loans 1.39m; Mazars zonder voorbehoud; dual Akapella deposit 2026-00139429 (=Akapella-1)",
        "confidence": "strong",
        "source_id": "src_familiehof_nbb_ye2025",
        "beneficiaries": "WZC residents Schelle / Vivalto group",
        "stated_goal": "Local leftover Familiehof WZC map — official NBB YE2025 after Akapella residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: bruto 3982577 / staff 3731195 VTE 64.9 / pnl 130955 / equity NEG 666897 / debt 2643255 / assets 1976358",
        "absurdity_score": "5.5",
        "cost_score": "3.3",
        "difficulty": "2.5",
        "priority_index": "4.4",
        "cut_proposal": "Publish comfort-letter terms + LT creditor 1.39m; disclose RIZIV bruto split; stop opaque Vivalto NEG-equity WZC continuum without public group map",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1744; leftover after AGB Bornem JR2024-only / Akapella done; Vivalto comfort pattern like Prinsenhof; CDN live also HofSchoten/Buitenhof/Zusterhof queued; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Familiehof>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes bruto 3982577 / staff 3731195 VTE 64.9 / pnl 130955 / assets 1976358 / equity NEG 666897 + Vivalto comfort brief; comfort-letter full text, LT other-loan creditor 1388689, RIZIV bruto split, and AV notulen 13.05.2026 unpublished",
        "why_it_matters": "Vivalto WZC with 4m bruto and NEG equity sustained only by group comfort letter — need creditor + comfort transparency for public-care euros",
        "priority": "9",
        "recipient_body": "Familiehof VZW / Vivalto Home Belgium NV / Bestuursorgaan",
        "recipient_email": "inge.vanbouwel@vivaltohome.com",
        "recipient_postal": "Provinciale Steenweg 323 2627 Schelle",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1744; human-send only; dual Akapella deposit-1; comfort like Prinsenhof; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1744":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1744: Familiehof KBO 0474.243.193 NBB YE2025 bruto 3982577 staff 3731195 VTE 64.9 equity NEG 666897 + Vivalto comfort; FOI ready gap_familiehof_bruto_3_98m_equity_neg_0_67m_comfort_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1745",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1745 after 1744 Familiehof YE2025. Next every-10 is 1750. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Familiehof/Akapella/DeVerlosser/VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC/Vivalto sister (Buitenhof deposit 2026-00136824 CDN200 / Hof van Schoten 2026-00143162 CDN200 / Zusterhof Geel 2026-00272840 CDN200 if unused).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1744 Familiehof; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/Buitenhof-HofSchoten-Zusterhof; next every-10 1750",
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
        "last_unit_id": "rq_1744",
        "ticks_completed": "1744",
        "paused": "no",
        "notes": "tick1744 leftover Familiehof WZC residual; KBO 0474.243.193; official NBB VKT-VZW YE2025 deposit 2026-00139429 CDN 200; sourced euros assets 1976358 bruto 3982577 staff 3731195 VTE 64.9 pnl 130955 equity NEG 666897 debt 2643255 LT other loans 1388689; Vivalto comfort to AV2027; Mazars oordeel zonder voorbehoud; dual Akapella deposit-1; FOI ready; AGB Bornem JR2024-only; NOT every-10 (next 1750); next rq_1745 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/Buitenhof-HofSchoten-Zusterhof; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T06:25:00Z"
DATE = "2026-08-24"
EID = "vzw_akapella"
GAP = "gap_akapella_bruto_5_00m_staff_4_37m_schenking_1_41m_l5"
COMM = "comm_akapella_jr2025_bruto"
LB = "lb_akapella_bruto_5_00m_staff_4_37m_schenking_1_41m"


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
        "name_nl": "Akapella Woonzorgcentrum VZW (leftover VL WZC Kapelle-op-den-Bos / Vivalto; dual Prinsenhof schenking 1.41m; NOT De Verlosser)",
        "name_fr": "Maison de repos Akapella asbl (residuelle Kapelle-op-den-Bos / Vivalto)",
        "name_en": "Akapella residential care VZW leftover Flemish WZC Kapelle-op-den-Bos Vivalto dual Prinsenhof donation",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vivaltohome.com/nl/akapella",
        "foi_email": "akapella.info@vivaltohome.com",
        "foi_postal": "Parallelweg 10 1880 Kapelle-op-den-Bos",
        "notes": "tick1743 leftover Vivalto WZC after De Verlosser; official NBB VKT-VZW YE2025 deposit 2026-00139430 CDN 200; KBO 0870.764.941; schenking 1405000 same as Prinsenhof; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_akapella_nbb_ye2025",
        "title": "Akapella WZC NBB VKT-VZW YE2025 deposit 2026-00139430",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139430.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1743; AV 08.05.2026; assets 1004739 bruto 4999525 staff 4373948 VTE 68 pnl 557243 equity 33392 schenking 1405000; Mazars zonder voorbehoud",
    },
    {
        "source_id": "src_akapella_kbo",
        "title": "Akapella WZC KBO 0870.764.941",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=870764941",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1743; VZW; Parallelweg 10 1880 Kapelle-op-den-Bos",
    },
    {
        "source_id": "src_akapella_portal",
        "title": "Akapella Vivalto Home portal",
        "url": "https://www.vivaltohome.com/nl/akapella",
        "publisher": "Vivalto Home / Akapella",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1743; WZC Kapelle-op-den-Bos; tel 015 71 50 20",
    },
    {
        "source_id": "src_akapella_foi_contact_1743",
        "title": "Akapella FOI channel",
        "url": "https://www.vivaltohome.com/nl/akapella",
        "publisher": "Akapella Woonzorgcentrum VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1743; akapella.info@vivaltohome.com; Parallelweg 10 1880 Kapelle-op-den-Bos",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_akapella_assets_2025", "2025", "1004739", "executed", "src_akapella_nbb_ye2025", "strong", "NBB 20/58 assets 1004739 DROP vs 2180271; tick1743"),
    ("bud_akapella_va_2025", "2025", "131022", "executed", "src_akapella_nbb_ye2025", "strong", "NBB VA 131022; tick1743"),
    ("bud_akapella_vlottend_2025", "2025", "873717", "executed", "src_akapella_nbb_ye2025", "strong", "NBB vlottend 873717 DROP; tick1743"),
    ("bud_akapella_cash_2025", "2025", "376390", "executed", "src_akapella_nbb_ye2025", "strong", "NBB liquide 376390 DROP vs 504895; tick1743"),
    ("bud_akapella_andere_recv_2025", "2025", "839", "executed", "src_akapella_nbb_ye2025", "strong", "NBB andere vorderingen 839 DROP vs 1070356; FOI group sweep; tick1743"),
    ("bud_akapella_equity_2025", "2025", "33392", "executed", "src_akapella_nbb_ye2025", "strong", "NBB EV 33392 DROP vs 881149 after schenking 1405000; tick1743"),
    ("bud_akapella_debt_2025", "2025", "971347", "executed", "src_akapella_nbb_ye2025", "strong", "NBB schulden 971347; tick1743"),
    ("bud_akapella_bruto_2025", "2025", "4999525", "executed", "src_akapella_nbb_ye2025", "strong", "NBB brutomarge 9900 4999525; 70/73 empty VKT; tick1743"),
    ("bud_akapella_staff_2025", "2025", "4373948", "executed", "src_akapella_nbb_ye2025", "strong", "NBB 62 4373948 / VTE 68; tick1743"),
    ("bud_akapella_expl_2025", "2025", "570221", "executed", "src_akapella_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 570221; tick1743"),
    ("bud_akapella_pnl_2025", "2025", "557243", "executed", "src_akapella_nbb_ye2025", "strong", "NBB PnL 9904 557243; AV 08.05.2026; Mazars zonder voorbehoud; tick1743"),
    ("bud_akapella_schenking_2025", "2025", "1405000", "executed", "src_akapella_nbb_ye2025", "strong", "NBB resultaatverwerking schenking 1405000 to similar VZW (same EUR as Prinsenhof); FOI; tick1743"),
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
        "title": "Akapella YE2025 leftover VL WZC (bruto 5.00m / staff 4.37m / schenking 1.41m)",
        "entity_id": EID,
        "beneficiary": "WZC residents Kapelle-op-den-Bos / Vivalto group / recipient VZW of 1.41m gift",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-08",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "4999525",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139430.pdf",
        "stated_goal": "Local leftover Akapella WZC map — official NBB YE2025 Vivalto dual; FOI 1.41m schenking twin Prinsenhof",
        "cut_option": "Publish RIZIV bruto split; identify 1.41m gift recipient and link to Prinsenhof onttrkking; map Vivalto cash sweep (andere recv DROP)",
        "source_id": "src_akapella_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Akapella>JR2025_L5",
        "notes": "tick1743; YE2025 VKT; bruto 5.00m staff 4.37m VTE 68 pnl +557k assets 1.00m DROP equity 33k after schenking 1.41m; Vivalto dual Prinsenhof; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Akapella YE2025: bruto 5.00m / staff 4.37m / schenking 1.41m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Akapella>JR2025_L5",
        "annual_cost_eur": "4999525",
        "total_cost_eur": "4999525",
        "tco_notes": "Leftover Vivalto Akapella WZC YE2025 VKT: bruto 5.00m (70/73 empty) / staff 4.37m VTE 68 / pnl +557k; assets DROP 2.18m→1.00m / equity DROP 0.88m→33k via explicit schenking 1.405m to similar VZW (same EUR as Prinsenhof); andere recv DROP 1.07m→0.8k; Mazars zonder voorbehoud; dual Vivalto Home BE",
        "confidence": "strong",
        "source_id": "src_akapella_nbb_ye2025",
        "beneficiaries": "WZC residents Kapelle-op-den-Bos / Vivalto group / gift recipient VZW",
        "stated_goal": "Local leftover Akapella WZC map — official NBB YE2025 after De Verlosser residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: bruto 4999525 / staff 4373948 VTE 68 / pnl 557243 / schenking 1405000 / assets 1004739",
        "absurdity_score": "5.2",
        "cost_score": "3.5",
        "difficulty": "2.5",
        "priority_index": "4.3",
        "cut_proposal": "Publish gift recipient + Prinsenhof twin 1.41m map; disclose RIZIV bruto split; stop opaque Vivalto inter-VZW surplus extraction",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1743; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / DeVerlosser+VivaltoHomeBE+Prinsenhof+Molenheide done; Vivalto schenking pattern; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Akapella>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes bruto 4999525 / staff 4373948 VTE 68 / pnl 557243 / assets 1004739 / equity 33392 after schenking 1405000; gift recipient identity, Prinsenhof twin link, and RIZIV bruto split unpublished; AV notulen 08.05.2026",
        "why_it_matters": "Vivalto WZC with 5m bruto extracting 1.41m gift (same EUR as Prinsenhof) while equity collapses — need group surplus-extraction transparency for public-care euros",
        "priority": "9",
        "recipient_body": "Akapella Woonzorgcentrum VZW / Vivalto Home Belgium NV / Bestuursorgaan",
        "recipient_email": "akapella.info@vivaltohome.com",
        "recipient_postal": "Parallelweg 10 1880 Kapelle-op-den-Bos",
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
        "notes": "tick1743; human-send only; dual Prinsenhof 1.41m twin; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1743":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1743: Akapella KBO 0870.764.941 NBB YE2025 bruto 4999525 staff 4373948 VTE 68 schenking 1405000 twin Prinsenhof; FOI ready gap_akapella_bruto_5_00m_staff_4_37m_schenking_1_41m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1744",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1744 after 1743 Akapella YE2025. Next every-10 is 1750. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Akapella/DeVerlosser/VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC/Vivalto sister (Familiehof/Buitenhof/Hof van Schoten if CDN live).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1743 Akapella; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/Vivalto-sister; next every-10 1750",
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
        "last_unit_id": "rq_1743",
        "ticks_completed": "1743",
        "paused": "no",
        "notes": "tick1743 leftover Akapella WZC residual; KBO 0870.764.941; official NBB VKT-VZW YE2025 deposit 2026-00139430 CDN 200; sourced euros assets 1004739 bruto 4999525 staff 4373948 VTE 68 pnl 557243 equity 33392 schenking 1405000 twin Prinsenhof; andere recv DROP 1070356 to 839; Mazars oordeel zonder voorbehoud; Vivalto; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; NOT every-10 (next 1750); next rq_1744 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/Vivalto-sister; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

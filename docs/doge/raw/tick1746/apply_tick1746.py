import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T07:25:00Z"
DATE = "2026-08-24"
EID = "bv_hofschoten"
GAP = "gap_hofschoten_bruto_2_88m_equity_neg_0_83m_comfort_l5"
COMM = "comm_hofschoten_jr2025_bruto"
LB = "lb_hofschoten_bruto_2_88m_equity_neg_0_83m_comfort"


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
        "name_nl": "Hof van Schoten BV (leftover VL WZC Schoten / Vivalto; NEG equity + comfort; staff>bruto; NOT Buitenhof)",
        "name_fr": "Maison de repos Hof van Schoten SRL (residuelle Schoten / Vivalto)",
        "name_en": "Hof van Schoten residential care BV leftover Flemish WZC Schoten Vivalto comfort letter",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vivaltohome.com/nl/maisons/hof-van-schoten/",
        "foi_email": "hofvanschoten@vivaltohome.com",
        "foi_postal": "Botermelkdijk 282 2900 Schoten",
        "notes": "tick1746 leftover Vivalto WZC BV after Buitenhof; official NBB VKT-inb YE2025 deposit 2026-00143162 CDN 200; KBO 0501.918.481; equity NEG 834711 + Vivalto comfort to AV2027; staff>bruto; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_hofschoten_nbb_ye2025",
        "title": "Hof van Schoten BV NBB VKT-inb YE2025 deposit 2026-00143162",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00143162.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1746; AV 08.05.2026; assets 1477675 bruto 2878805 staff 3047899 VTE 47.1 pnl -282679 equity NEG 834711 debt 2312387; Vivalto comfort; Aedifica OB 21137830; Mazars zonder voorbehoud + 5:153",
    },
    {
        "source_id": "src_hofschoten_kbo",
        "title": "Hof van Schoten BV KBO 0501.918.481",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=501918481",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1746; BV; Botermelkdijk 282 2900 Schoten",
    },
    {
        "source_id": "src_hofschoten_portal",
        "title": "Hof van Schoten Vivalto Home portal",
        "url": "https://www.vivaltohome.com/nl/maisons/hof-van-schoten/",
        "publisher": "Vivalto Home / Hof van Schoten",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1746; WZC Schoten; hofvanschoten@vivaltohome.com; tel 03/666.26.41",
    },
    {
        "source_id": "src_hofschoten_foi_contact_1746",
        "title": "Hof van Schoten FOI channel",
        "url": "https://www.vivaltohome.com/nl/maisons/hof-van-schoten/plaats-contact/",
        "publisher": "Hof van Schoten BV",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1746; hofvanschoten@vivaltohome.com; Botermelkdijk 282 2900 Schoten",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_hofschoten_assets_2025", "2025", "1477675", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB 20/58 assets 1477675 DROP vs 1756275; tick1746"),
    ("bud_hofschoten_va_2025", "2025", "271680", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB VA 271680; tick1746"),
    ("bud_hofschoten_vlottend_2025", "2025", "1205995", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB vlottend 1205995 DROP; tick1746"),
    ("bud_hofschoten_cash_2025", "2025", "266682", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB liquide 266682 JUMP vs 138490; tick1746"),
    ("bud_hofschoten_andere_recv_2025", "2025", "452643", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB andere vorderingen 452643 DROP vs 885481 (=related 9500); FOI group; tick1746"),
    ("bud_hofschoten_equity_2025", "2025", "-834711", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB EV NEG 834711 (worse vs NEG 552033); Vivalto comfort + art 5:153; tick1746"),
    ("bud_hofschoten_debt_2025", "2025", "2312387", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB schulden 2312387; LT overige leningen 1280225 (>5y); tick1746"),
    ("bud_hofschoten_bruto_2025", "2025", "2878805", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB brutomarge 9900 2878805; 70/60-61 empty VKT; tick1746"),
    ("bud_hofschoten_staff_2025", "2025", "3047899", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB 62 3047899 > bruto; VTE 47.1 DROP vs 52.4 (9087); tick1746"),
    ("bud_hofschoten_expl_2025", "2025", "-260036", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB bedrijfsverlies 9901 -260036; tick1746"),
    ("bud_hofschoten_pnl_2025", "2025", "-282679", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB PnL 9904 -282679; AV 08.05.2026; Mazars zonder voorbehoud + 5:153; tick1746"),
    ("bud_hofschoten_lt_other_loans_2025", "2025", "1280225", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB LT overige leningen 1280225 all >5y; FOI creditor; tick1746"),
    ("bud_hofschoten_aedifica_lease_ob_2025", "2025", "21137830", "executed", "src_hofschoten_nbb_ye2025", "strong", "NBB off-balance future Aedifica rents 21137830 to 14.12.2045; bankgarantie 493407; tick1746"),
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
        "title": "Hof van Schoten YE2025 leftover VL WZC (bruto 2.88m / equity NEG 0.83m / Vivalto comfort)",
        "entity_id": EID,
        "beneficiary": "WZC residents Schoten / Vivalto group (comfort letter dependent)",
        "legal_basis": "WVV BV; Woonzorgdecreet; Bestuursdecreet openbaarheid; art 5:153 WVV",
        "decision_date": "2026-05-08",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "2878805",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00143162.pdf",
        "stated_goal": "Local leftover Hof van Schoten WZC map — official NBB YE2025 Vivalto dual; FOI NEG equity + comfort + staff>bruto",
        "cut_option": "Publish comfort-letter terms; disclose LT other-loan creditor 1.28m; RIZIV bruto split; explain staff 3.05m > bruto 2.88m; map Aedifica TCO 21.1m",
        "source_id": "src_hofschoten_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>HofVanSchoten>JR2025_L5",
        "notes": "tick1746; YE2025 VKT-inb; bruto 2.88m staff 3.05m VTE 47.1 pnl -283k assets 1.48m equity NEG 0.83m + comfort; Aedifica OB 21.1m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Hof van Schoten YE2025: bruto 2.88m / equity NEG 0.83m / staff>bruto / comfort",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>HofVanSchoten>JR2025_L5",
        "annual_cost_eur": "2878805",
        "total_cost_eur": "2878805",
        "tco_notes": "Leftover Vivalto Hof van Schoten WZC BV YE2025 VKT-inb: bruto 2.88m (70 empty) / staff 3.05m > bruto / VTE 47.1 DROP vs 52.4 / pnl -283k; assets DROP 1.76m→1.48m / equity NEG 0.83m (worse vs NEG 0.55m) with Vivalto Home Belgium comfort brief to AV2027; debt 2.31m incl LT other loans 1.28m >5y; related recv 0.45m; Aedifica future rents OB 21.14m to 2045 + bankgarantie 0.49m; Mazars zonder voorbehoud + art 5:153 WVV NEG nettoactief; parent Vivalto Home Belgium / Vivalto Vie Holding Paris",
        "confidence": "strong",
        "source_id": "src_hofschoten_nbb_ye2025",
        "beneficiaries": "WZC residents Schoten / Vivalto group",
        "stated_goal": "Local leftover Hof van Schoten WZC map — official NBB YE2025 after Buitenhof residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: bruto 2878805 / staff 3047899 VTE 47.1 / pnl -282679 / equity NEG 834711 / debt 2312387 / assets 1477675 / Aedifica OB 21137830",
        "absurdity_score": "6.2",
        "cost_score": "3.0",
        "difficulty": "2.5",
        "priority_index": "4.6",
        "cut_proposal": "Publish comfort-letter terms + LT creditor 1.28m; disclose why staff exceeds bruto; RIZIV split; stop opaque Vivalto NEG-equity WZC continuum on public-care euros",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1746; leftover after AGB Bornem JR2024-only / Buitenhof done; CDN also live Zusterhof queued; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>HofVanSchoten>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-inb publishes bruto 2878805 / staff 3047899 > bruto VTE 47.1 / pnl -282679 / assets 1477675 / equity NEG 834711 + Vivalto comfort brief; comfort-letter full text, LT other-loan creditor 1280225, related recv 452643 terms, RIZIV bruto split, Aedifica lease TCO, and AV notulen 08.05.2026 unpublished",
        "why_it_matters": "Vivalto WZC BV with staff exceeding bruto and deepening NEG equity sustained only by group comfort letter — need creditor + comfort transparency for public-care euros",
        "priority": "9",
        "recipient_body": "Hof van Schoten BV / Vivalto Home Belgium NV / Bestuursorgaan",
        "recipient_email": "hofvanschoten@vivaltohome.com",
        "recipient_postal": "Botermelkdijk 282 2900 Schoten",
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
        "notes": "tick1746; human-send only; dual Buitenhof Vivalto sister; comfort like Familiehof; AGB/NSZ/Dijk92/APEFE still blocked preferred path",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1746":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = "Hof van Schoten BV JR2025 leftover dual residual"
        r["notes"] = "DONE tick1746: Hof van Schoten BV KBO 0501.918.481 NBB YE2025 bruto 2878805 staff 3047899 VTE 47.1 equity NEG 834711 + Vivalto comfort; FOI ready gap_hofschoten_bruto_2_88m_equity_neg_0_83m_comfort_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1747",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1747 after 1746 Hof van Schoten YE2025. Next every-10 is 1750. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo HofSchoten/Buitenhof/Familiehof/Akapella/DeVerlosser/VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC/Vivalto sister (Zusterhof Geel 2026-00272840 CDN200 if unused).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1746 HofSchoten; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/Zusterhof; next every-10 1750",
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
        "last_unit_id": "rq_1746",
        "ticks_completed": "1746",
        "paused": "no",
        "notes": "tick1746 leftover Hof van Schoten WZC BV residual; KBO 0501.918.481; official NBB VKT-inb YE2025 deposit 2026-00143162 CDN 200; sourced euros assets 1477675 bruto 2878805 staff 3047899 VTE 47.1 pnl -282679 equity NEG 834711 debt 2312387 LT other loans 1280225 Aedifica OB 21137830; Vivalto comfort to AV2027; Mazars oordeel zonder voorbehoud + 5:153; dual Buitenhof Vivalto sister; FOI ready; AGB Bornem JR2024-only; NOT every-10 (next 1750); next rq_1747 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/Zusterhof; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

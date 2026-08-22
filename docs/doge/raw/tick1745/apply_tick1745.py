import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T07:05:00Z"
DATE = "2026-08-24"
EID = "nv_buitenhof"
GAP = "gap_buitenhof_bruto_4_11m_fin_5_69m_related_loan_16_4m_l5"
COMM = "comm_buitenhof_jr2025_bruto"
LB = "lb_buitenhof_bruto_4_11m_fin_5_69m_related_loan_16_4m"


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
        "name_nl": "Buitenhof WZC NV (leftover VL WZC Brasschaat / Vivalto; non-rec fin 5.69m + related loan 16.4m; NOT Familiehof)",
        "name_fr": "Maison de repos Buitenhof SA (residuelle Brasschaat / Vivalto)",
        "name_en": "Buitenhof residential care NV leftover Flemish WZC Brasschaat Vivalto related-party loan",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vivaltohome.com/nl/maisons/buitenhof/",
        "foi_email": "info.buitenhof@vivaltohome.com",
        "foi_postal": "Papestraat 24 2930 Brasschaat",
        "notes": "tick1745 leftover Vivalto WZC NV after Familiehof; official NBB VKT-kap YE2025 deposit 2026-00136824 CDN 200; KBO 0453.581.304; non-rec fin income 5694303; related loan 16400000 indefinite; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_buitenhof_nbb_ye2025",
        "title": "Buitenhof WZC NV NBB VKT-kap YE2025 deposit 2026-00136824",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00136824.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1745; AV 08.05.2026; assets 28552979 bruto 4109579 staff 3029860 VTE 48.4 pnl 5404991 equity 14282598 debt 12192935; non-rec fin 5694303; related loan 16400000; Mazars zonder voorbehoud",
    },
    {
        "source_id": "src_buitenhof_kbo",
        "title": "Buitenhof WZC NV KBO 0453.581.304",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=453581304",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1745; NV; Papestraat 24 2930 Brasschaat",
    },
    {
        "source_id": "src_buitenhof_portal",
        "title": "Buitenhof Vivalto Home portal",
        "url": "https://www.vivaltohome.com/nl/maisons/buitenhof/",
        "publisher": "Vivalto Home / Buitenhof",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1745; WZC Brasschaat; info.buitenhof@vivaltohome.com; tel 03/651.46.16",
    },
    {
        "source_id": "src_buitenhof_foi_contact_1745",
        "title": "Buitenhof FOI channel",
        "url": "https://www.vivaltohome.com/nl/maisons/buitenhof/",
        "publisher": "Buitenhof WZC NV",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1745; info.buitenhof@vivaltohome.com; Papestraat 24 2930 Brasschaat",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_buitenhof_assets_2025", "2025", "28552979", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB 20/58 assets 28552979 vs 28231414; tick1745"),
    ("bud_buitenhof_va_2025", "2025", "27357053", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB VA 27357053; fin VA 16400000; tick1745"),
    ("bud_buitenhof_fin_va_2025", "2025", "16400000", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB fin VA 16400000 (acq 16.4m / dispose 15.388m); related loan indefinite; tick1745"),
    ("bud_buitenhof_vlottend_2025", "2025", "1195926", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB vlottend 1195926 JUMP; tick1745"),
    ("bud_buitenhof_cash_2025", "2025", "486530", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB liquide 486530 vs 481467; tick1745"),
    ("bud_buitenhof_trade_recv_2025", "2025", "674505", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB handelsvorderingen 674505 JUMP vs 392356; tick1745"),
    ("bud_buitenhof_equity_2025", "2025", "14282598", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB EV 14282598 JUMP vs 8877607 via PnL spike; tick1745"),
    ("bud_buitenhof_debt_2025", "2025", "12192935", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB schulden 12192935 DROP vs 17096176; LT fin lease 10203586; ST overige DROP 4585872→133834; tick1745"),
    ("bud_buitenhof_bruto_2025", "2025", "4109579", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB brutomarge 9900 4109579; 70/60-61 empty VKT; tick1745"),
    ("bud_buitenhof_staff_2025", "2025", "3029860", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB 62 3029860 / VTE 48.4 vs 48.2; tick1745"),
    ("bud_buitenhof_expl_2025", "2025", "67996", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 67996 (vs -178049); tick1745"),
    ("bud_buitenhof_nonrec_fin_2025", "2025", "5694303", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB 76B non-rec fin income 5694303; FOI nature; tick1745"),
    ("bud_buitenhof_pnl_2025", "2025", "5404991", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB PnL 9904 5404991 (vs -686601); AV 08.05.2026; Mazars zonder voorbehoud; tick1745"),
    ("bud_buitenhof_aedifica_lease_ob_2025", "2025", "9209906", "executed", "src_buitenhof_nbb_ye2025", "strong", "NBB off-balance future Aedifica rents 9209906 to 29.12.2037; tick1745"),
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
        "title": "Buitenhof YE2025 leftover VL WZC (bruto 4.11m / non-rec fin 5.69m / related loan 16.4m)",
        "entity_id": EID,
        "beneficiary": "WZC residents Brasschaat / Vivalto group (related-party loan dependent)",
        "legal_basis": "WVV NV; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-08",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "4109579",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00136824.pdf",
        "stated_goal": "Local leftover Buitenhof WZC map — official NBB YE2025 Vivalto dual; FOI non-rec fin + related loan",
        "cut_option": "Publish nature of 5.69m non-rec fin income; disclose related-party loan 16.4m terms/borrower; publish RIZIV bruto split; map Aedifica lease TCO",
        "source_id": "src_buitenhof_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Buitenhof>JR2025_L5",
        "notes": "tick1745; YE2025 VKT-kap; bruto 4.11m staff 3.03m VTE 48.4 pnl +5.40m driven by non-rec fin 5.69m; related loan 16.4m; Aedifica OB 9.21m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Buitenhof YE2025: bruto 4.11m / non-rec fin 5.69m / related loan 16.4m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Buitenhof>JR2025_L5",
        "annual_cost_eur": "4109579",
        "total_cost_eur": "4109579",
        "tco_notes": "Leftover Vivalto Buitenhof WZC NV YE2025 VKT-kap: bruto 4.11m (70 empty) / staff 3.03m VTE 48.4 / expl +68k; PnL +5.40m driven by opaque non-recurring financial income 5.69m; equity JUMP 8.88m→14.28m; debt DROP 17.1m→12.2m (ST other 4.59m→0.13m); financial VA swapped to related-party loan 16.4m indefinite on controlling persons; Aedifica future rents OB 9.21m to 2037; Mazars zonder voorbehoud + AV timing remark; parent Vivalto Home Belgium / Vivalto Vie Holding Paris",
        "confidence": "strong",
        "source_id": "src_buitenhof_nbb_ye2025",
        "beneficiaries": "WZC residents Brasschaat / Vivalto group",
        "stated_goal": "Local leftover Buitenhof WZC map — official NBB YE2025 after Familiehof residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: bruto 4109579 / staff 3029860 VTE 48.4 / pnl 5404991 / non-rec fin 5694303 / equity 14282598 / related loan 16400000 / assets 28552979",
        "absurdity_score": "6.0",
        "cost_score": "3.4",
        "difficulty": "2.5",
        "priority_index": "4.7",
        "cut_proposal": "Publish 5.69m non-rec fin nature + related loan 16.4m borrower/interest; disclose ST other-debt clearance 4.59m; RIZIV bruto split; stop opaque Vivalto group cash/loan reshuffles on public-care euros",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1745; leftover after AGB Bornem JR2024-only / Familiehof done; CDN also live HofSchoten/Zusterhof queued; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Buitenhof>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-kap publishes bruto 4109579 / staff 3029860 VTE 48.4 / pnl 5404991 driven by non-rec fin 5694303 / related loan 16400000 indefinite / ST other debt DROP 4585872→133834; nature of 5.69m fin income, loan borrower/terms, debt clearance, RIZIV bruto split, and AV notulen 08.05.2026 unpublished",
        "why_it_matters": "Vivalto WZC NV with 4.1m care bruto and 5.7m opaque non-rec fin income plus 16.4m related-party loan — need group cash transparency for public-care euros",
        "priority": "9",
        "recipient_body": "Buitenhof WZC NV / Vivalto Home Belgium NV / Bestuursorgaan",
        "recipient_email": "info.buitenhof@vivaltohome.com",
        "recipient_postal": "Papestraat 24 2930 Brasschaat",
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
        "notes": "tick1745; human-send only; dual Familiehof Vivalto sister; AGB/NSZ/Dijk92/APEFE still blocked preferred path",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1745":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = "Buitenhof WZC NV JR2025 leftover dual residual"
        r["notes"] = "DONE tick1745: Buitenhof NV KBO 0453.581.304 NBB YE2025 bruto 4109579 staff 3029860 VTE 48.4 pnl 5404991 non-rec fin 5694303 related loan 16400000; FOI ready gap_buitenhof_bruto_4_11m_fin_5_69m_related_loan_16_4m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1746",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1746 after 1745 Buitenhof YE2025. Next every-10 is 1750. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Buitenhof/Familiehof/Akapella/DeVerlosser/VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC/Vivalto sister (Hof van Schoten 2026-00143162 CDN200 / Zusterhof Geel 2026-00272840 CDN200 if unused).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1745 Buitenhof; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/HofSchoten-Zusterhof; next every-10 1750",
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
        "last_unit_id": "rq_1745",
        "ticks_completed": "1745",
        "paused": "no",
        "notes": "tick1745 leftover Buitenhof WZC NV residual; KBO 0453.581.304; official NBB VKT-kap YE2025 deposit 2026-00136824 CDN 200; sourced euros assets 28552979 bruto 4109579 staff 3029860 VTE 48.4 pnl 5404991 equity 14282598 debt 12192935 non-rec fin 5694303 related loan 16400000 Aedifica OB 9209906; Mazars oordeel zonder voorbehoud; dual Familiehof Vivalto sister; FOI ready; AGB Bornem JR2024-only; NOT every-10 (next 1750); next rq_1746 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HofSchoten-Zusterhof; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

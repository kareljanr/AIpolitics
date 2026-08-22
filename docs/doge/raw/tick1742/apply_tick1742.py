import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T06:05:00Z"
DATE = "2026-08-24"
EID = "vzw_de_verlosser"
GAP = "gap_deverlosser_omzet_3_02m_bruto_2_25m_staff_2_18m_l5"
COMM = "comm_deverlosser_jr2025_omzet"
LB = "lb_deverlosser_omzet_3_02m_bruto_2_25m_staff_2_18m"


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
        "name_nl": "Woonzorgcentrum De Verlosser VZW (leftover VL WZC Dilbeek; NOT Vivalto/Colisée/Armonea)",
        "name_fr": "Maison de repos De Verlosser asbl (residuelle Dilbeek)",
        "name_en": "De Verlosser residential care VZW leftover Flemish WZC Dilbeek",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://wzcdeverlosser.be",
        "foi_email": "info@wzcdeverlosser.be",
        "foi_postal": "Brusselstraat 647 1700 Dilbeek",
        "notes": "tick1742 leftover independent VL WZC after Vivalto holding; official NBB VKT-VZW YE2025 deposit 2026-00174957 CDN 200; KBO 0446.340.946; FOI omzet/73 empty",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_deverlosser_nbb_ye2025",
        "title": "WZC De Verlosser NBB VKT-VZW YE2025 deposit 2026-00174957",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00174957.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1742; AV 11.05.2026; assets 2391042 omzet 3015833 bruto 2248348 staff 2177394 VTE 31 pnl 94194; no commissaris VKT",
    },
    {
        "source_id": "src_deverlosser_kbo",
        "title": "WZC De Verlosser KBO 0446.340.946",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=446340946",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1742; VZW; Brusselstraat 647 1700 Dilbeek",
    },
    {
        "source_id": "src_deverlosser_portal",
        "title": "De Verlosser official portal",
        "url": "https://wzcdeverlosser.be",
        "publisher": "Woonzorgcentrum De Verlosser",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1742; WZC Sint-Ulriks-Kapelle Dilbeek; tel 02 453 94 41",
    },
    {
        "source_id": "src_deverlosser_foi_contact_1742",
        "title": "De Verlosser FOI channel",
        "url": "https://wzcdeverlosser.be",
        "publisher": "Woonzorgcentrum De Verlosser VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1742; info@wzcdeverlosser.be; Brusselstraat 647 1700 Dilbeek",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_deverlosser_assets_2025", "2025", "2391042", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB 20/58 assets 2391042; tick1742"),
    ("bud_deverlosser_va_2025", "2025", "767790", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB VA 767790; tick1742"),
    ("bud_deverlosser_buildings_2025", "2025", "415574", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB terreinen/gebouwen 415574; tick1742"),
    ("bud_deverlosser_vlottend_2025", "2025", "1623252", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB vlottend 1623252; tick1742"),
    ("bud_deverlosser_cash_2025", "2025", "89058", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB liquide 89058 DROP vs 140427; tick1742"),
    ("bud_deverlosser_beleg_2025", "2025", "1002257", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB geldbeleggingen 1002257; tick1742"),
    ("bud_deverlosser_equity_2025", "2025", "1690969", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB EV 1690969; tick1742"),
    ("bud_deverlosser_kapsubs_2025", "2025", "33600", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB kapitaalsubsidies 33600; tick1742"),
    ("bud_deverlosser_voorzieningen_2025", "2025", "143866", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB voorzieningen herstel 143866 DROP vs 320000; tick1742"),
    ("bud_deverlosser_debt_2025", "2025", "556207", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB schulden 556207; tick1742"),
    ("bud_deverlosser_bruto_2025", "2025", "2248348", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB brutomarge 9900 2248348; tick1742"),
    ("bud_deverlosser_omzet_2025", "2025", "3015833", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB omzet 70 3015833; code73 empty; FOI RIZIV; tick1742"),
    ("bud_deverlosser_goederen_diensten_2025", "2025", "1026867", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB 60/61 1026867 JUMP vs 827942; tick1742"),
    ("bud_deverlosser_staff_2025", "2025", "2177394", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB 62 2177394 / VTE 31; tick1742"),
    ("bud_deverlosser_expl_2025", "2025", "90558", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 90558; tick1742"),
    ("bud_deverlosser_pnl_2025", "2025", "94194", "executed", "src_deverlosser_nbb_ye2025", "strong", "NBB PnL 9904 94194; AV 11.05.2026; VKT no commissaris; tick1742"),
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
        "title": "De Verlosser YE2025 leftover VL WZC (omzet 3.02m / bruto 2.25m / staff 2.18m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Dilbeek",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-11",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "3015833",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00174957.pdf",
        "stated_goal": "Local leftover De Verlosser WZC map — official NBB YE2025 independent; FOI omzet/73",
        "cut_option": "Publish RIZIV/dagprijs split of omzet 3.02m despite empty 73; explain voorzieningen release 0.18m",
        "source_id": "src_deverlosser_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>DeVerlosser>JR2025_L5",
        "notes": "tick1742; YE2025 VKT; omzet 3.02m bruto 2.25m staff 2.18m VTE 31 pnl +94k assets 2.39m equity 1.69m debt 0.56m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "De Verlosser YE2025: omzet 3.02m / bruto 2.25m / staff 2.18m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>DeVerlosser>JR2025_L5",
        "annual_cost_eur": "3015833",
        "total_cost_eur": "3015833",
        "tco_notes": "Leftover independent Dilbeek WZC YE2025 VKT: omzet 3.02m (code73 empty) / bruto 2.25m / 60+61 1.03m JUMP / staff 2.18m VTE 31 / pnl +94k; assets 2.39m equity 1.69m debt 0.56m / voorzieningen release 0.18m; FOI RIZIV split",
        "confidence": "strong",
        "source_id": "src_deverlosser_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Dilbeek",
        "stated_goal": "Local leftover De Verlosser WZC map — official NBB YE2025 after Vivalto residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: omzet 3015833 / bruto 2248348 / staff 2177394 VTE 31 / pnl 94194 / assets 2391042",
        "absurdity_score": "2.8",
        "cost_score": "3.5",
        "difficulty": "2.0",
        "priority_index": "3.0",
        "cut_proposal": "Publish RIZIV/zorgkas/dagprijs split of omzet; explain herstel-voorziening release; keep as baseline independent WZC comparator vs commercial groups",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1742; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Vivalto+Colisee+Armonea+Prinsenhof+Molenheide done; independent; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>DeVerlosser>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes omzet 3015833 / bruto 2248348 / 60+61 1026867 / staff 2177394 VTE 31 / pnl 94194 / assets 2391042; code73 empty so RIZIV/dagprijs split and voorzieningen release basis unpublished; AV notulen 11.05.2026",
        "why_it_matters": "Independent VL WZC with 3.02m omzet but empty subsidy code — need public-care financing transparency as comparator vs commercial Vivalto/Colisée stacks",
        "priority": "7",
        "recipient_body": "Woonzorgcentrum De Verlosser VZW / Bestuursorgaan",
        "recipient_email": "info@wzcdeverlosser.be",
        "recipient_postal": "Brusselstraat 647 1700 Dilbeek",
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
        "notes": "tick1742; human-send only; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1742":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1742: De Verlosser KBO 0446.340.946 NBB YE2025 omzet 3015833 bruto 2248348 staff 2177394 VTE 31; FOI ready gap_deverlosser_omzet_3_02m_bruto_2_25m_staff_2_18m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1743",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1743 after 1742 De Verlosser YE2025. Next every-10 is 1750. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo DeVerlosser/VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1742 DeVerlosser; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1750",
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
        "last_unit_id": "rq_1742",
        "ticks_completed": "1742",
        "paused": "no",
        "notes": "tick1742 leftover De Verlosser WZC residual; KBO 0446.340.946; official NBB VKT-VZW YE2025 deposit 2026-00174957 CDN 200; sourced euros assets 2391042 omzet 3015833 bruto 2248348 goederen_diensten 1026867 staff 2177394 VTE 31 pnl 94194 equity 1690969 debt 556207 kapsubs 33600 voorzieningen 143866; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; NOT every-10 (next 1750); next rq_1743 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

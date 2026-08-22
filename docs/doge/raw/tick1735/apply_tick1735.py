import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T03:45:00Z"
DATE = "2026-08-24"
EID = "nv_molenheide_wzc"
GAP = "gap_molenheide_opbr_9_02m_debt_26_24m_fva_15_95m_l5"
COMM = "comm_molenheide_jr2025_opbr"
LB = "lb_molenheide_opbr_9_02m_debt_26_24m_fva_15_95m"


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
        "name_nl": "Molenheide Woonzorgcentrum NV (leftover VL WZC Wijnegem / Vivalto Home; NOT Sint-Jozef / Veilige Have)",
        "name_fr": "Maison de repos Molenheide SA (residuelle Wijnegem / Vivalto)",
        "name_en": "Molenheide residential care NV leftover Flemish WZC Wijnegem Vivalto",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vivaltohome.com/nl/maisons/molenheide/",
        "foi_email": "molenheide.admin@vivaltohome.com",
        "foi_postal": "Turnhoutsebaan 611 2110 Wijnegem",
        "notes": "tick1735 leftover VL WZC after Sint-Jozef Rumst; official NBB VOL-kap YE2025 deposit 2026-00139187 CDN 200; KBO 0810.616.132; Vivalto Home Belgium NV gedelegeerd; FOI debt 26.24m + FVA 15.95m + overlopende 10.72m",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_molenheide_nbb_ye2025",
        "title": "Molenheide WZC NBB VOL-kap YE2025 deposit 2026-00139187",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139187.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1735; AV 13.05.2026; assets 29875847 opbr 9017098 staff 5001893 VTE 89.2 pnl 405436 debt 26240354; Mazars oordeel zonder voorbehoud",
    },
    {
        "source_id": "src_molenheide_kbo",
        "title": "Molenheide WZC KBO 0810.616.132",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=810616132",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1735; NV; Turnhoutsebaan 611 2110 Wijnegem",
    },
    {
        "source_id": "src_molenheide_portal",
        "title": "Molenheide Vivalto Home portal",
        "url": "https://www.vivaltohome.com/nl/maisons/molenheide/",
        "publisher": "Vivalto Home / Molenheide WZC",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1735; WZC Wijnegem; tel 03/353.18.80",
    },
    {
        "source_id": "src_molenheide_foi_contact_1735",
        "title": "Molenheide WZC FOI channel",
        "url": "https://www.vivaltohome.com/nl/maisons/molenheide/",
        "publisher": "Molenheide Woonzorgcentrum NV",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1735; molenheide.admin@vivaltohome.com; Turnhoutsebaan 611 2110 Wijnegem",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_molenheide_assets_2025", "2025", "29875847", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB 20/58 assets 29875847; tick1735"),
    ("bud_molenheide_va_2025", "2025", "27963497", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB VA 21/28 27963497; tick1735"),
    ("bud_molenheide_mva_2025", "2025", "12014497", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB MVA 12014497 (leasing 11679862); tick1735"),
    ("bud_molenheide_fva_2025", "2025", "15949000", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB FVA verbonden 15949000; FOI group map; tick1735"),
    ("bud_molenheide_vlottend_2025", "2025", "1912350", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB vlottend 1912350; tick1735"),
    ("bud_molenheide_cash_2025", "2025", "435126", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB liquide 435126 JUMP vs 56998; tick1735"),
    ("bud_molenheide_equity_2025", "2025", "3635494", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB EV 3635494; tick1735"),
    ("bud_molenheide_debt_2025", "2025", "26240354", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB schulden 26240354; tick1735"),
    ("bud_molenheide_lt_leasing_2025", "2025", "13862846", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB LT leasingschulden 13862846; FOI counterpart; tick1735"),
    ("bud_molenheide_overlopende_2025", "2025", "10722381", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB overlopende passiva 10722381; FOI; tick1735"),
    ("bud_molenheide_opbr_2025", "2025", "9017098", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 9017098; tick1735"),
    ("bud_molenheide_omzet_2025", "2025", "8434992", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB omzet 70 8434992; FOI RIZIV split; tick1735"),
    ("bud_molenheide_andere_opbr_2025", "2025", "35314", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB andere 74 35314; tick1735"),
    ("bud_molenheide_nietrec_opbr_2025", "2025", "546792", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB niet-recurrente 76A 546792; FOI; tick1735"),
    ("bud_molenheide_staff_2025", "2025", "5001893", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB 62 5001893 / VTE 89.2 DROP vs 93.6; tick1735"),
    ("bud_molenheide_diensten_2025", "2025", "1501671", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB diensten 61 1501671 JUMP vs 1282547; tick1735"),
    ("bud_molenheide_expl_2025", "2025", "1094535", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 1094535; tick1735"),
    ("bud_molenheide_fincost_2025", "2025", "573126", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB financiële kosten 573126; tick1735"),
    ("bud_molenheide_pnl_2025", "2025", "405436", "executed", "src_molenheide_nbb_ye2025", "strong", "NBB PnL 9904 405436 retained (no dividend); AV 13.05.2026; Mazars zonder voorbehoud; tick1735"),
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
        "title": "Molenheide WZC YE2025 leftover VL WZC (opbr 9.02m / debt 26.24m / FVA 15.95m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Wijnegem / Vivalto group",
        "legal_basis": "WVV NV; Woonzorgdecreet; Bestuursdecreet openbaarheid where applicable",
        "decision_date": "2026-05-13",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "9017098",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139187.pdf",
        "stated_goal": "Local leftover Molenheide WZC map — official NBB YE2025; FOI debt+FVA+overlopende+RIZIV split",
        "cut_option": "Publish omzet RIZIV split + leasing/overlopende counterparties + FVA 15.95m Vivalto group map; explain diensten JUMP + VTE DROP",
        "source_id": "src_molenheide_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Molenheide>JR2025_L5",
        "notes": "tick1735; YE2025; opbr 9.02m omzet 8.43m staff 5.00m VTE 89.2 pnl +405k assets 29.88m debt 26.24m FVA 15.95m leasing 13.86m overlopende 10.72m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Molenheide WZC YE2025: opbr 9.02m / debt 26.24m / FVA 15.95m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Molenheide>JR2025_L5",
        "annual_cost_eur": "9017098",
        "total_cost_eur": "9017098",
        "tco_notes": "Leftover Molenheide Vivalto WZC YE2025: opbr 9.02m (omzet 8.43m / niet-rec 0.55m) / staff 5.00m VTE 89.2 DROP / diensten JUMP 1.50m / pnl +0.41m; assets 29.88m debt 26.24m (leasing 13.86m + overlopende 10.72m) / FVA verbonden 15.95m; Mazars zonder voorbehoud; FOI group+lease+RIZIV",
        "confidence": "strong",
        "source_id": "src_molenheide_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Wijnegem / Vivalto group",
        "stated_goal": "Local leftover Molenheide WZC map — official NBB YE2025 after Sint-Jozef Rumst residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 9017098 / staff 5001893 VTE 89.2 / pnl 405436 / debt 26240354 / FVA 15949000",
        "absurdity_score": "4.4",
        "cost_score": "4.0",
        "difficulty": "2.8",
        "priority_index": "4.0",
        "cut_proposal": "Publish RIZIV/zorgkas split of omzet; disclose leasing + 10.72m deferred counterparties; map 15.95m FVA Vivalto group flows",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1735; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / SintJozef+VeiligeHave+WitteMeren+TerEngelen done; private NV Vivalto; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Molenheide>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-kap publishes opbr 9017098 / omzet 8434992 / staff 5001893 VTE 89.2 / pnl 405436 / assets 29875847 / debt 26240354 / FVA 15949000 / leasing 13862846 / overlopende 10722381; RIZIV omzet split, leasing+deferred counterparties, and Vivalto group FVA map unpublished; AV notulen 13.05.2026",
        "why_it_matters": "Vivalto leftover VL WZC with 9.02m opbr but 26.24m debt + 15.95m related FVA + 10.72m deferred — need public-care financing and group transparency",
        "priority": "9",
        "recipient_body": "Molenheide Woonzorgcentrum NV / Vivalto Home Belgium NV",
        "recipient_email": "molenheide.admin@vivaltohome.com",
        "recipient_postal": "Turnhoutsebaan 611 2110 Wijnegem",
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
        "notes": "tick1735; human-send only; AGB/NSZ/Dijk92/APEFE still blocked; private NV FOI best-effort on public care euros",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1735":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1735: Molenheide KBO 0810.616.132 NBB YE2025 opbr 9017098 staff 5001893 VTE 89.2 debt 26240354 FVA 15949000; FOI ready gap_molenheide_opbr_9_02m_debt_26_24m_fva_15_95m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1736",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1736 after 1735 Molenheide YE2025. Next every-10 is 1740. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1735 Molenheide; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1740",
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
        "last_unit_id": "rq_1735",
        "ticks_completed": "1735",
        "paused": "no",
        "notes": "tick1735 leftover Molenheide WZC residual; KBO 0810.616.132; official NBB VOL-kap YE2025 deposit 2026-00139187 CDN 200; sourced euros assets 29875847 opbr 9017098 omzet 8434992 nietrec 546792 staff 5001893 VTE 89.2 diensten 1501671 pnl 405436 debt 26240354 leasing 13862846 overlopende 10722381 FVA 15949000; Mazars oordeel zonder voorbehoud; Vivalto Home; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; NOT every-10 (next 1740); next rq_1736 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

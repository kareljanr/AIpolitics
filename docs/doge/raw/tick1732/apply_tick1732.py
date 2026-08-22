import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T02:45:00Z"
DATE = "2026-08-24"
EID = "vzw_witte_meren"


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
        "name_nl": "Woonzorgcentrum Witte Meren VZW (leftover VL WZC Mol; NOT Ter Engelen)",
        "name_fr": "Maison de repos Witte Meren asbl (residuelle Mol)",
        "name_en": "Witte Meren residential care home leftover Flemish WZC Mol",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.wzcwittemeren.be",
        "foi_email": "info@wzcwittemeren.be",
        "foi_postal": "Collegestraat 69 2400 Mol",
        "notes": "tick1732 leftover VL WZC after Ter Engelen; official NBB VOL-VZW YE2025 deposit 2026-00123787 CDN 200; KBO 0418.234.997; FOI subsidy split + hypotheek",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_witte_meren_nbb_ye2025",
        "title": "WZC Witte Meren NBB VOL-VZW YE2025 deposit 2026-00123787",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00123787.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1732; AV 12.05.2026; assets 15422948 opbr 9532998 staff 7064455 VTE 107.4 pnl 195470",
    },
    {
        "source_id": "src_witte_meren_kbo",
        "title": "WZC Witte Meren KBO 0418.234.997",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=418234997",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1732; VZW; Collegestraat 69 2400 Mol",
    },
    {
        "source_id": "src_witte_meren_portal",
        "title": "Witte Meren official portal",
        "url": "https://www.wzcwittemeren.be",
        "publisher": "Woonzorgcentrum Witte Meren",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1732; WZC Mol",
    },
    {
        "source_id": "src_witte_meren_foi_contact_1732",
        "title": "Witte Meren FOI channel",
        "url": "https://www.wzcwittemeren.be",
        "publisher": "Woonzorgcentrum Witte Meren VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1732; info@wzcwittemeren.be; Collegestraat 69 2400 Mol",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_wittemeren_assets_2025", "2025", "15422948", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB 20/58 assets 15422948; tick1732"),
    ("bud_wittemeren_va_2025", "2025", "13995679", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB VA 21/28 13995679; tick1732"),
    ("bud_wittemeren_buildings_2025", "2025", "13560957", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB terreinen/gebouwen 13560957 hypothecated; tick1732"),
    ("bud_wittemeren_vlottend_2025", "2025", "1427269", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB vlottend 1427269; tick1732"),
    ("bud_wittemeren_cash_2025", "2025", "495219", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB liquide 495219 JUMP vs 198360; tick1732"),
    ("bud_wittemeren_equity_2025", "2025", "6885941", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB EV 6885941; tick1732"),
    ("bud_wittemeren_kapsubs_2025", "2025", "287131", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB kapitaalsubsidies 287131; tick1732"),
    ("bud_wittemeren_debt_2025", "2025", "8537008", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB schulden 8537008; tick1732"),
    ("bud_wittemeren_lt_fin_2025", "2025", "6549981", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB LT kredietinstellingen 6549981; tick1732"),
    ("bud_wittemeren_zekerheid_2025", "2025", "7074981", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB schulden zakelijke zekerheid 7074981; tick1732"),
    ("bud_wittemeren_opbr_2025", "2025", "9532998", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 9532998; tick1732"),
    ("bud_wittemeren_omzet_2025", "2025", "7975593", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB omzet 70 7975593 = dagprijs 3459174 + basistegemoetkoming zorg 4474822; tick1732"),
    ("bud_wittemeren_code73_2025", "2025", "1465035", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB code73 1465035 (subsidies 733 1464898); tick1732"),
    ("bud_wittemeren_subs_2025", "2025", "1464898", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB subsidies 733 1464898; donor split FOI; tick1732"),
    ("bud_wittemeren_staff_2025", "2025", "7064455", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB 62 7064455 / VTE 107.4; tick1732"),
    ("bud_wittemeren_diensten_2025", "2025", "1112397", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB diensten 61 1112397; tick1732"),
    ("bud_wittemeren_expl_2025", "2025", "328956", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 328956; tick1732"),
    ("bud_wittemeren_pnl_2025", "2025", "195470", "executed", "src_witte_meren_nbb_ye2025", "strong", "NBB PnL 9904 195470; AV 12.05.2026; tick1732"),
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
        "commitment_id": "comm_witte_meren_jr2025_opbr",
        "title": "WZC Witte Meren YE2025 leftover VL WZC (opbr 9.53m / staff 7.06m / subs 1.46m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Mol",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-12",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "9532998",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00123787.pdf",
        "stated_goal": "Local leftover Witte Meren WZC map — official NBB YE2025; FOI subsidy donor + hypotheek",
        "cut_option": "Publish subsidy 1.46m VL/gemeente/RIZIV split beyond basistegemoetkoming 4.47m; explain hypotheek 7.07m + kapsubs 0.29m",
        "source_id": "src_witte_meren_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>WitteMeren>JR2025_L5",
        "notes": "tick1732; YE2025; opbr 9.53m omzet 7.98m staff 7.06m VTE 107.4 pnl +195k assets 15.42m debt 8.54m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_wittemeren_opbr_9_53m_staff_7_06m_subs_1_46m",
        "name": "WZC Witte Meren YE2025: opbr 9.53m / staff 7.06m / subs 1.46m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>WitteMeren>JR2025_L5",
        "annual_cost_eur": "9532998",
        "total_cost_eur": "9532998",
        "tco_notes": "Leftover Witte Meren WZC YE2025: opbr 9.53m (omzet 7.98m = dagprijs 3.46m + basistegemoetkoming zorg 4.47m; code73 1.47m / subsidies 1.46m) / staff 7.06m VTE 107.4 / diensten 1.11m / pnl +0.20m; assets 15.42m debt 8.54m zakelijke zekerheid 7.07m; FOI donor split",
        "confidence": "strong",
        "source_id": "src_witte_meren_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Mol",
        "stated_goal": "Local leftover Witte Meren WZC map — official NBB YE2025 after Ter Engelen residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 9532998 / staff 7064455 VTE 107.4 / pnl 195470 / assets 15422948",
        "absurdity_score": "3.5",
        "cost_score": "3.5",
        "difficulty": "2.5",
        "priority_index": "3.2",
        "cut_proposal": "Publish RIZIV/VL/gemeente subsidy split of 1.46m beyond published basistegemoetkoming; scrutinise hypotheek 7.07m + kapsubs 0.29m",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1732; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Ter Engelen done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_wittemeren_opbr_9_53m_staff_7_06m_subs_1_46m_l5",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>WitteMeren>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes opbr 9532998 / omzet 7975593 (dagprijs 3459174 + basistegemoetkoming zorg 4474822) / subsidies 1464898 / staff 7064455 VTE 107.4 / pnl 195470 / assets 15422948; subsidy donor split and hypotheek detail unpublished; AV notulen 12.05.2026",
        "why_it_matters": "Leftover VL WZC with 9.53m opbr and published omzet split — need VL/gemeente/RIZIV subsidy transparency beyond basistegemoetkoming plus hypotheek/kapsubs",
        "priority": "8",
        "recipient_body": "Woonzorgcentrum Witte Meren VZW / Bestuursorgaan",
        "recipient_email": "info@wzcwittemeren.be",
        "recipient_postal": "Collegestraat 69 2400 Mol",
        "draft_letter_path": "docs/doge/foi/drafts/gap_wittemeren_opbr_9_53m_staff_7_06m_subs_1_46m_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_witte_meren_jr2025_opbr",
        "linked_leaderboard_id": "lb_wittemeren_opbr_9_53m_staff_7_06m_subs_1_46m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1732; human-send only; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1732":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_wittemeren_opbr_9_53m_staff_7_06m_subs_1_46m_l5"
        r["notes"] = "DONE tick1732: Witte Meren KBO 0418.234.997 NBB YE2025 opbr 9532998 staff 7064455 VTE 107.4 pnl 195470; FOI ready gap_wittemeren_opbr_9_53m_staff_7_06m_subs_1_46m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1733",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1733 after 1732 Witte Meren YE2025. Next every-10 is 1740. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1732 WitteMeren; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1740",
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
        "last_unit_id": "rq_1732",
        "ticks_completed": "1732",
        "paused": "no",
        "notes": "tick1732 leftover Witte Meren WZC residual; KBO 0418.234.997; official NBB VOL-VZW YE2025 deposit 2026-00123787 CDN 200; sourced euros assets 15422948 opbr 9532998 omzet 7975593 (dagprijs 3459174 + basistegemoetkoming 4474822) code73 1465035 subs 1464898 staff 7064455 VTE 107.4 diensten 1112397 pnl 195470 debt 8537008 zekerheid 7074981; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; NOT every-10 (next 1740); next rq_1733 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

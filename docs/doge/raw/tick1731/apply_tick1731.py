import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T02:25:00Z"
DATE = "2026-08-24"
EID = "vzw_ter_engelen"


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
        "name_nl": "Woonzorgcentrum Ter Engelen VZW (leftover VL WZC Lokeren; NOT Dommelhof TW / Covida group detail FOI)",
        "name_fr": "Maison de repos Ter Engelen asbl (residuelle Lokeren)",
        "name_en": "Ter Engelen residential care home leftover Flemish WZC Lokeren",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.terengelen.be",
        "foi_email": "info@covida.be",
        "foi_postal": "Polderstraat 4 9160 Lokeren",
        "notes": "tick1731 leftover VL WZC after AGB/NSZ/Dijk92/APEFE/LSC hunt; official NBB VOL-VZW YE2025 deposit 2026-00322588 CDN 200; KBO 0430.882.809; FOI code73 + LOSS",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_ter_engelen_nbb_ye2025",
        "title": "WZC Ter Engelen NBB VOL-VZW YE2025 deposit 2026-00322588",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00322588.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1731; AV 20.05.2026; assets 15006980 opbr 8064590 staff 5878986 VTE 87.5 pnl -482826",
    },
    {
        "source_id": "src_ter_engelen_kbo",
        "title": "WZC Ter Engelen KBO 0430.882.809",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=430882809",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1731; VZW; Polderstraat 4 9160 Lokeren",
    },
    {
        "source_id": "src_ter_engelen_portal",
        "title": "Ter Engelen official portal",
        "url": "https://www.terengelen.be",
        "publisher": "Woonzorgcentrum Ter Engelen / Covida",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1731; WZC Lokeren",
    },
    {
        "source_id": "src_ter_engelen_foi_contact_1731",
        "title": "Ter Engelen FOI channel",
        "url": "https://www.terengelen.be",
        "publisher": "Woonzorgcentrum Ter Engelen VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1731; info@covida.be; Polderstraat 4 9160 Lokeren",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_terengelen_assets_2025", "2025", "15006980", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB 20/58 assets 15006980; tick1731"),
    ("bud_terengelen_va_2025", "2025", "9895246", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB VA/MVA 9895246; tick1731"),
    ("bud_terengelen_buildings_2025", "2025", "9513052", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB terreinen/gebouwen 9513052; tick1731"),
    ("bud_terengelen_vlottend_2025", "2025", "5111734", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB vlottend 5111734; tick1731"),
    ("bud_terengelen_beleg_2025", "2025", "3778861", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB beleggingen 3778861; tick1731"),
    ("bud_terengelen_cash_2025", "2025", "134923", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB liquide 134923 DROP vs 623975; tick1731"),
    ("bud_terengelen_equity_2025", "2025", "8386880", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB EV 8386880; tick1731"),
    ("bud_terengelen_voorzieningen_2025", "2025", "450000", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB voorzieningen onderhoud 450000; tick1731"),
    ("bud_terengelen_debt_2025", "2025", "6170100", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB schulden 6170100; tick1731"),
    ("bud_terengelen_lt_fin_2025", "2025", "4468202", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB LT kredietinstellingen 4468202; tick1731"),
    ("bud_terengelen_opbr_2025", "2025", "8064590", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 8064590; tick1731"),
    ("bud_terengelen_omzet_2025", "2025", "6652388", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB omzet 70 6652388; tick1731"),
    ("bud_terengelen_code73_2025", "2025", "1360061", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB code73 1360061; tick1731"),
    ("bud_terengelen_staff_2025", "2025", "5878986", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB 62 5878986 / VTE 87.5; tick1731"),
    ("bud_terengelen_diensten_2025", "2025", "1584761", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB diensten 61 1584761 JUMP vs 802286; tick1731"),
    ("bud_terengelen_expl_2025", "2025", "-349347", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 -349347 LOSS FLIP; tick1731"),
    ("bud_terengelen_pnl_2025", "2025", "-482826", "executed", "src_ter_engelen_nbb_ye2025", "strong", "NBB PnL 9904 -482826 LOSS FLIP; AV 20.05.2026; tick1731"),
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
        "commitment_id": "comm_ter_engelen_jr2025_opbr",
        "title": "WZC Ter Engelen YE2025 leftover VL WZC (opbr 8.06m / staff 5.88m / LOSS 0.48m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Lokeren",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-20",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "8064590",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00322588.pdf",
        "stated_goal": "Local leftover Ter Engelen WZC map — official NBB YE2025; FOI code73+LOSS",
        "cut_option": "Publish code73 RIZIV/VL split of 1.36m; scrutinise diensten JUMP 1.58m + LOSS 0.48m; Covida group flows",
        "source_id": "src_ter_engelen_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>TerEngelen>JR2025_L5",
        "notes": "tick1731; YE2025; opbr 8.06m staff 5.88m VTE 87.5 pnl -483k assets 15.01m debt 6.17m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_terengelen_opbr_8_06m_staff_5_88m_loss_0_48m",
        "name": "WZC Ter Engelen YE2025: opbr 8.06m / staff 5.88m / LOSS 0.48m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>TerEngelen>JR2025_L5",
        "annual_cost_eur": "8064590",
        "total_cost_eur": "8064590",
        "tco_notes": "Leftover Ter Engelen WZC YE2025: opbr 8.06m (omzet 6.65m / code73 1.36m) / staff 5.88m VTE 87.5 / diensten JUMP 1.58m / afschr JUMP 0.48m / pnl -0.48m LOSS FLIP; assets 15.01m debt 6.17m cash DROP; Covida FOI",
        "confidence": "strong",
        "source_id": "src_ter_engelen_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Lokeren",
        "stated_goal": "Local leftover Ter Engelen WZC map — official NBB YE2025 after Dommelhof/LSC residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 8064590 / staff 5878986 VTE 87.5 / pnl -482826 / assets 15006980",
        "absurdity_score": "4.0",
        "cost_score": "3.5",
        "difficulty": "2.5",
        "priority_index": "3.5",
        "cut_proposal": "Publish RIZIV/VL subsidy split; explain diensten+afschr JUMP and LOSS flip; map Covida group",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1731; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403; Witte Meren CDN live unused deferred; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_terengelen_opbr_8_06m_staff_5_88m_loss_0_48m_l5",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>TerEngelen>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes opbr 8064590 / omzet 6652388 / code73 1360061 / staff 5878986 VTE 87.5 / pnl -482826 / assets 15006980; code73 donor split and Covida group flows unpublished; AV notulen 20.05.2026",
        "why_it_matters": "Leftover VL WZC with 8.06m opbr and 0.48m LOSS flip — need RIZIV/VL subsidy transparency + cost JUMP explanation",
        "priority": "8",
        "recipient_body": "Woonzorgcentrum Ter Engelen VZW / Bestuursorgaan",
        "recipient_email": "info@covida.be",
        "recipient_postal": "Polderstraat 4 9160 Lokeren",
        "draft_letter_path": "docs/doge/foi/drafts/gap_terengelen_opbr_8_06m_staff_5_88m_loss_0_48m_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_ter_engelen_jr2025_opbr",
        "linked_leaderboard_id": "lb_terengelen_opbr_8_06m_staff_5_88m_loss_0_48m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1731; human-send only; AGB/NSZ/Dijk92/APEFE still blocked; Witte Meren 2026-00123787 CDN 200 unused deferred",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1731":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_terengelen_opbr_8_06m_staff_5_88m_loss_0_48m_l5"
        r["notes"] = "DONE tick1731: Ter Engelen KBO 0430.882.809 NBB YE2025 opbr 8064590 staff 5878986 VTE 87.5 pnl -482826; FOI ready gap_terengelen_opbr_8_06m_staff_5_88m_loss_0_48m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1732",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1732 after 1731 Ter Engelen YE2025. Next every-10 is 1740. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else WZC Witte Meren if CDN 200, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1731 TerEngelen; NEXT AGB/WitteMeren-if-200/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1740",
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
        "last_unit_id": "rq_1731",
        "ticks_completed": "1731",
        "paused": "no",
        "notes": "tick1731 leftover Ter Engelen WZC residual; KBO 0430.882.809; official NBB VOL-VZW YE2025 deposit 2026-00322588 CDN 200; sourced euros assets 15006980 opbr 8064590 omzet 6652388 code73 1360061 staff 5878986 VTE 87.5 diensten 1584761 pnl -482826 debt 6170100; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; Witte Meren CDN 200 unused deferred; NOT every-10 (next 1740); next rq_1732 AGB/WitteMeren-if-200/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

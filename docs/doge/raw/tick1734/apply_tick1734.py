import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T03:25:00Z"
DATE = "2026-08-24"
EID = "vzw_sint_jozef_rumst"
GAP = "gap_sintjozef_opbr_6_28m_staff_4_24m_subs_1_27m_l5"
COMM = "comm_sintjozef_jr2025_opbr"
LB = "lb_sintjozef_opbr_6_28m_staff_4_24m_subs_1_27m"


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
        "name_nl": "Woon- en Zorgcentrum Sint-Jozef VZW (leftover VL WZC Rumst; NOT Veilige Have / Witte Meren / Ter Engelen)",
        "name_fr": "Maison de repos Sint-Jozef asbl (residuelle Rumst)",
        "name_en": "Sint-Jozef residential care home leftover Flemish WZC Rumst",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.sint-jozef-rumst.be",
        "foi_email": "info@sint-jozef-rumst.be",
        "foi_postal": "Schoolstraat 1 2840 Rumst",
        "notes": "tick1734 leftover VL WZC after Veilige Have; official NBB VOL-VZW YE2025 deposit 2026-00272845 CDN 200; KBO 0448.190.181; FOI code73 1.27m + kapsubs + VTE DROP; Vyvey oordeel zonder voorbehoud",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_sintjozef_nbb_ye2025",
        "title": "WZC Sint-Jozef Rumst NBB VOL-VZW YE2025 deposit 2026-00272845",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00272845.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1734; AV 25.06.2026; assets 16860795 opbr 6277820 staff 4236727 VTE 55.6 pnl 205527; Vyvey oordeel zonder voorbehoud",
    },
    {
        "source_id": "src_sintjozef_kbo",
        "title": "WZC Sint-Jozef Rumst KBO 0448.190.181",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=448190181",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1734; VZW; Schoolstraat 1 2840 Rumst; aanbestedende overheid",
    },
    {
        "source_id": "src_sintjozef_portal",
        "title": "Sint-Jozef Rumst official portal",
        "url": "https://www.sint-jozef-rumst.be",
        "publisher": "WZC Sint-Jozef Rumst",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1734; WZC Rumst; Zorggroep Antwerpen samenwerking",
    },
    {
        "source_id": "src_sintjozef_foi_contact_1734",
        "title": "Sint-Jozef Rumst FOI channel",
        "url": "https://www.sint-jozef-rumst.be/contact",
        "publisher": "Woon- en Zorgcentrum Sint-Jozef VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1734; info@sint-jozef-rumst.be; Schoolstraat 1 2840 Rumst; tel 03/451 35 30",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_sintjozef_assets_2025", "2025", "16860795", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB 20/58 assets 16860795; tick1734"),
    ("bud_sintjozef_va_2025", "2025", "14406196", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB VA 21/28 14406196; tick1734"),
    ("bud_sintjozef_buildings_2025", "2025", "14306868", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB terreinen/gebouwen 14306868; tick1734"),
    ("bud_sintjozef_vlottend_2025", "2025", "2454600", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB vlottend 2454600; tick1734"),
    ("bud_sintjozef_cash_2025", "2025", "484969", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB liquide 484969 DROP vs 544569; tick1734"),
    ("bud_sintjozef_beleg_2025", "2025", "1100000", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB geldbeleggingen 1100000; tick1734"),
    ("bud_sintjozef_equity_2025", "2025", "10874824", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB EV 10874824; tick1734"),
    ("bud_sintjozef_kapsubs_2025", "2025", "7413783", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB kapitaalsubsidies 7413783 DROP vs 7829590; FOI VIPA; tick1734"),
    ("bud_sintjozef_voorzieningen_2025", "2025", "197069", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB voorzieningen 197069 (herstel 150000); tick1734"),
    ("bud_sintjozef_debt_2025", "2025", "5788902", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB schulden 5788902; tick1734"),
    ("bud_sintjozef_lt_fin_2025", "2025", "4390037", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB LT fin 4390037 (krediet 3770037 + overige 620000); tick1734"),
    ("bud_sintjozef_opbr_2025", "2025", "6277820", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 6277820; tick1734"),
    ("bud_sintjozef_omzet_2025", "2025", "4791023", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB omzet 70 4791023 (dagprijs 2492727 + zorgkassen 1852486 + doorgerekend 445809); tick1734"),
    ("bud_sintjozef_code73_2025", "2025", "1271572", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB code73/subsidies 733 1271572; FOI donor split; tick1734"),
    ("bud_sintjozef_andere_opbr_2025", "2025", "210662", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB andere bedrijfsopbrengsten 74 210662; tick1734"),
    ("bud_sintjozef_staff_2025", "2025", "4236727", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB 62 4236727 / VTE 55.6 DROP vs 60.4; tick1734"),
    ("bud_sintjozef_diensten_2025", "2025", "508565", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB diensten 61 508565; tick1734"),
    ("bud_sintjozef_expl_2025", "2025", "306204", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 306204; tick1734"),
    ("bud_sintjozef_pnl_2025", "2025", "205527", "executed", "src_sintjozef_nbb_ye2025", "strong", "NBB PnL 9904 205527; AV 25.06.2026; Vyvey zonder voorbehoud; tick1734"),
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
        "title": "WZC Sint-Jozef Rumst YE2025 leftover VL WZC (opbr 6.28m / staff 4.24m / subs 1.27m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Rumst",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-06-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "6277820",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00272845.pdf",
        "stated_goal": "Local leftover Sint-Jozef Rumst WZC map — official NBB YE2025; FOI code73 + kapsubs + VTE DROP",
        "cut_option": "Publish code73 1.27m donor split + kapsubs 7.41m VIPA path; explain VTE DROP 60.4 to 55.6; map Zorggroep Antwerpen flows",
        "source_id": "src_sintjozef_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>SintJozefRumst>JR2025_L5",
        "notes": "tick1734; YE2025; opbr 6.28m omzet 4.79m code73 1.27m staff 4.24m VTE 55.6 pnl +206k assets 16.86m debt 5.79m kapsubs 7.41m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "WZC Sint-Jozef Rumst YE2025: opbr 6.28m / staff 4.24m / subs 1.27m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>SintJozefRumst>JR2025_L5",
        "annual_cost_eur": "6277820",
        "total_cost_eur": "6277820",
        "tco_notes": "Leftover Sint-Jozef Rumst WZC YE2025: opbr 6.28m (omzet 4.79m / code73 1.27m / andere 0.21m) / staff 4.24m VTE 55.6 DROP / pnl +0.21m; assets 16.86m debt 5.79m kapsubs 7.41m; Vyvey oordeel zonder voorbehoud; FOI subsidy donor + VIPA + Zorggroep Antwerpen",
        "confidence": "strong",
        "source_id": "src_sintjozef_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Rumst",
        "stated_goal": "Local leftover Sint-Jozef Rumst WZC map — official NBB YE2025 after Veilige Have residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 6277820 / staff 4236727 VTE 55.6 / pnl 205527 / assets 16860795",
        "absurdity_score": "3.8",
        "cost_score": "3.6",
        "difficulty": "2.5",
        "priority_index": "3.5",
        "cut_proposal": "Publish RIZIV/VL/gemeente/VIPA split of code73+kapsubs; explain VTE DROP; disclose Zorggroep Antwerpen money flows",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1734; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / VeiligeHave+WitteMeren+TerEngelen done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>SintJozefRumst>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes opbr 6277820 / omzet 4791023 / code73 1271572 / andere 210662 / staff 4236727 VTE 55.6 / pnl 205527 / assets 16860795; code73 donor split, kapsubs 7413783 VIPA path, VTE DROP vs 60.4, and Zorggroep Antwerpen flows unpublished; AV notulen 25.06.2026",
        "why_it_matters": "Leftover VL WZC with 6.28m opbr and 1.27m subsidies — need financing transparency and group/network map despite clean audit",
        "priority": "8",
        "recipient_body": "Woon- en Zorgcentrum Sint-Jozef VZW / Bestuursorgaan",
        "recipient_email": "info@sint-jozef-rumst.be",
        "recipient_postal": "Schoolstraat 1 2840 Rumst",
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
        "notes": "tick1734; human-send only; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1734":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1734: Sint-Jozef Rumst KBO 0448.190.181 NBB YE2025 opbr 6277820 staff 4236727 VTE 55.6 pnl 205527; FOI ready gap_sintjozef_opbr_6_28m_staff_4_24m_subs_1_27m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1735",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1735 after 1734 Sint-Jozef Rumst YE2025. Next every-10 is 1740. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC (e.g. Molenheide if CDN live).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1734 SintJozefRumst; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1740",
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
        "last_unit_id": "rq_1734",
        "ticks_completed": "1734",
        "paused": "no",
        "notes": "tick1734 leftover Sint-Jozef Rumst WZC residual; KBO 0448.190.181; official NBB VOL-VZW YE2025 deposit 2026-00272845 CDN 200; sourced euros assets 16860795 opbr 6277820 omzet 4791023 code73 1271572 andere 210662 staff 4236727 VTE 55.6 diensten 508565 pnl 205527 debt 5788902 kapsubs 7413783; Vyvey oordeel zonder voorbehoud; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; NOT every-10 (next 1740); next rq_1735 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

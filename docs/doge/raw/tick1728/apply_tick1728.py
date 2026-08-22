import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T01:25:00Z"
DATE = "2026-08-24"
EID = "vzw_lsc_oostbrabant"


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
        "name_nl": "LeerSteunCentrum Oost-Brabant VZW (leftover VL leersteuncentrum; NOT GO! / OVSG / KOV / LSC Noord-Brabant)",
        "name_fr": "Centre de soutien a l apprentissage Brabant oriental asbl (residuel)",
        "name_en": "Learning Support Centre East Brabant leftover Flemish leersteuncentrum VZW",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.leersteuncentrumoostbrabant.be",
        "foi_email": "jan.deceulaer@lscob.be",
        "foi_postal": "Platte Lostraat 541 3010 Kessel-Lo",
        "notes": "tick1728 leftover VL leersteuncentrum after AGB/NSZ/Dijk92/APEFE/ABS hunt; official NBB MIC-VZW YE2025 deposit 2026-00117935 CDN 200; KBO 0800.106.082; FOI code73 donor + staff empty",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_lsc_oostbrabant_nbb_ye2025",
        "title": "LeerSteunCentrum Oost-Brabant NBB MIC-VZW YE2025 deposit 2026-00117935",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117935.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1728; AV 21.05.2026; neergelegd 22.05.2026; assets 839257 code73 435527 bruto 141112 pnl 140967 cash 822488",
    },
    {
        "source_id": "src_lsc_oostbrabant_kbo",
        "title": "LeerSteunCentrum Oost-Brabant KBO 0800.106.082",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=800106082",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1728; VZW; Platte Lostraat 541 3010 Kessel-Lo",
    },
    {
        "source_id": "src_lsc_oostbrabant_portal",
        "title": "LeerSteunCentrum Oost-Brabant portal",
        "url": "https://www.leersteuncentrumoostbrabant.be",
        "publisher": "LeerSteunCentrum Oost-Brabant VZW",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1728; VL leersteun network Oost-Brabant",
    },
    {
        "source_id": "src_lsc_oostbrabant_foi_contact_1728",
        "title": "LeerSteunCentrum Oost-Brabant FOI channel",
        "url": "https://www.leersteuncentrumoostbrabant.be",
        "publisher": "LeerSteunCentrum Oost-Brabant VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1728; jan.deceulaer@lscob.be; Platte Lostraat 541 3010 Kessel-Lo",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_lsc_ob_assets_2025", "2025", "839257", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB 20/58 assets 839257; tick1728"),
    ("bud_lsc_ob_cash_2025", "2025", "822488", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB liquide 54/58 822488 JUMP vs 680588; tick1728"),
    ("bud_lsc_ob_equity_2025", "2025", "808234", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB EV 10/15 808234; tick1728"),
    ("bud_lsc_ob_destin_2025", "2025", "591000", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB bestemde fondsen 13 591000 (+100k); tick1728"),
    ("bud_lsc_ob_debt_2025", "2025", "31023", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB schulden 17/49 31023; tick1728"),
    ("bud_lsc_ob_code73_2025", "2025", "435527", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB code73 435527 DROP vs 890562; tick1728"),
    ("bud_lsc_ob_diensten_2025", "2025", "304183", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB 60/61 304183; tick1728"),
    ("bud_lsc_ob_bruto_2025", "2025", "141112", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB brutomarge 9900 141112 DROP vs 566490; tick1728"),
    ("bud_lsc_ob_expl_2025", "2025", "141090", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 141090; tick1728"),
    ("bud_lsc_ob_pnl_2025", "2025", "140967", "executed", "src_lsc_oostbrabant_nbb_ye2025", "strong", "NBB PnL 9904 140967; AV 21.05.2026; tick1728"),
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
        "commitment_id": "comm_lsc_oostbrabant_jr2025_code73",
        "title": "LeerSteunCentrum Oost-Brabant YE2025 leftover VL leersteun (code73 0.44m / bruto 0.14m)",
        "entity_id": EID,
        "beneficiary": "Oost-Brabant pupils needing leersteun / Catholic school boards",
        "legal_basis": "WVV VZW; Decreet leersteun; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-21",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "435527",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117935.pdf",
        "stated_goal": "Local leftover LSC Oost-Brabant map — official NBB YE2025; FOI donor+staff",
        "cut_option": "Publish code73 donor split (VL vs schoolbesturen); explain staff empty / detacheringen; destin +100k path",
        "source_id": "src_lsc_oostbrabant_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>Leersteun>LSC_OostBrabant>JR2025_L5",
        "notes": "tick1728; YE2025; code73 0.44m bruto 0.14m pnl +141k cash 0.82m staff empty; dual residual after GO!; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_lsc_oostbrabant_code73_0_44m_bruto_0_14m_staff_empty",
        "name": "LeerSteunCentrum Oost-Brabant YE2025: code73 0.44m / bruto 0.14m / staff empty",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Onderwijs>Leersteun>LSC_OostBrabant>JR2025_L5",
        "annual_cost_eur": "435527",
        "total_cost_eur": "435527",
        "tco_notes": "Leftover LSC Oost-Brabant YE2025: code73 0.44m DROP / diensten 0.30m / bruto 0.14m DROP / pnl +141k / cash 0.82m JUMP / destin 0.59m; staff 62 empty VTE unpublished; omzet 70 empty",
        "confidence": "strong",
        "source_id": "src_lsc_oostbrabant_nbb_ye2025",
        "beneficiaries": "Oost-Brabant pupils / Catholic school boards",
        "stated_goal": "Local leftover LSC map — official NBB YE2025 after GO!/OVSG education residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: code73 435527 / bruto 141112 / pnl 140967 / assets 839257",
        "absurdity_score": "3.0",
        "cost_score": "2.5",
        "difficulty": "2.0",
        "priority_index": "2.6",
        "cut_proposal": "Publish VL vs schoolbestuur donor matrix for 0.44m; disclose VTE/detacheringen; destin reserves path",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1728; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / ABS+BVAS no NBB; LSC Noord-Brabant CDN live unused deferred; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_lsc_oostbrabant_code73_0_44m_bruto_0_14m_staff_empty_l5",
        "hierarchy_path": "Vlaanderen>Onderwijs>Leersteun>LSC_OostBrabant>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB MIC-VZW publishes code73 435527 / diensten 304183 / bruto 141112 / pnl 140967 / assets 839257; omzet 70 empty; staff 62 empty / VTE unpublished; donor split of code73 and detacheringen opaque; AV notulen 21.05.2026",
        "why_it_matters": "Leftover VL leersteuncentrum with live YE2025 euros (0.44m code73) — need VL funding transparency + staffing model",
        "priority": "7",
        "recipient_body": "LeerSteunCentrum Oost-Brabant VZW / Bestuursorgaan",
        "recipient_email": "jan.deceulaer@lscob.be",
        "recipient_postal": "Platte Lostraat 541 3010 Kessel-Lo",
        "draft_letter_path": "docs/doge/foi/drafts/gap_lsc_oostbrabant_code73_0_44m_bruto_0_14m_staff_empty_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_lsc_oostbrabant_jr2025_code73",
        "linked_leaderboard_id": "lb_lsc_oostbrabant_code73_0_44m_bruto_0_14m_staff_empty",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1728; human-send only; AGB/NSZ/Dijk92/APEFE still blocked; LSC Noord-Brabant 2026-00109506 CDN 200 unused deferred",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1728":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_lsc_oostbrabant_code73_0_44m_bruto_0_14m_staff_empty_l5"
        r["notes"] = "DONE tick1728: LSC Oost-Brabant KBO 0800.106.082 NBB YE2025 code73 435527 bruto 141112 pnl 140967; FOI ready gap_lsc_oostbrabant_code73_0_44m_bruto_0_14m_staff_empty_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1729",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1729 after 1728 LSC Oost-Brabant YE2025. Next every-10 is 1730 (MUST progress). SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo LSC_OostBrabant/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/NSZ. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else LSC Noord-Brabant if CDN 200 text, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1728 LSC_OB; NEXT AGB/LSC_NoordBrabant-if-200/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC; LSC_OB DONE; next every-10 1730 MUST",
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
        "last_unit_id": "rq_1728",
        "ticks_completed": "1728",
        "paused": "no",
        "notes": "tick1728 leftover LeerSteunCentrum Oost-Brabant residual; KBO 0800.106.082; official NBB MIC-VZW YE2025 deposit 2026-00117935 CDN 200; sourced euros assets 839257 code73 435527 diensten 304183 bruto 141112 pnl 140967 cash 822488 destin 591000; staff empty; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; LSC Noord-Brabant CDN 200 unused deferred; NOT every-10 (next 1730 MUST); next rq_1729 AGB/LSC_NB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

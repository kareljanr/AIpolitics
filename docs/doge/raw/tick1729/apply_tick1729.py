import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T01:45:00Z"
DATE = "2026-08-24"
EID = "vzw_lsc_noordbrabant"


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
        "name_nl": "Leersteuncentrum Noord-Brabant VZW (leftover VL leersteuncentrum dual LSC Oost-Brabant; NOT GO! / OVSG / KOV)",
        "name_fr": "Centre de soutien a l apprentissage Brabant nord asbl (dual residuel)",
        "name_en": "Learning Support Centre North Brabant leftover Flemish leersteuncentrum dual LSC East Brabant",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.lscnb.be",
        "foi_email": "info@lscnb.be",
        "foi_postal": "Frederik de Merodestraat 18 2800 Mechelen",
        "notes": "tick1729 leftover VL leersteuncentrum dual after LSC OB 1728; official NBB S-vzw YE2025 deposit 2026-00109506 CDN 200; KBO 0799.959.988; FOI VTE + donor detail",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_lsc_noordbrabant_nbb_ye2025",
        "title": "Leersteuncentrum Noord-Brabant NBB S-vzw YE2025 deposit 2026-00109506",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00109506.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1729; AV ~04.05.2026; assets 1584939 opbr 475607 staff 15920 pnl 203213 cash 1506757",
    },
    {
        "source_id": "src_lsc_noordbrabant_kbo",
        "title": "Leersteuncentrum Noord-Brabant KBO 0799.959.988",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=799959988",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1729; VZW; Frederik de Merodestraat 18 2800 Mechelen",
    },
    {
        "source_id": "src_lsc_noordbrabant_portal",
        "title": "Leersteuncentrum Noord-Brabant portal",
        "url": "https://www.lscnb.be",
        "publisher": "Leersteuncentrum Noord-Brabant VZW",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1729; VL leersteun network Noord-Brabant",
    },
    {
        "source_id": "src_lsc_noordbrabant_foi_contact_1729",
        "title": "Leersteuncentrum Noord-Brabant FOI channel",
        "url": "https://www.lscnb.be",
        "publisher": "Leersteuncentrum Noord-Brabant VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1729; info@lscnb.be; Frederik de Merodestraat 18 2800 Mechelen",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_lsc_nb_assets_2025", "2025", "1584939", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB S-vzw assets 1584938.79; tick1729"),
    ("bud_lsc_nb_va_2025", "2025", "69510", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB VA/MVA 69510.45; tick1729"),
    ("bud_lsc_nb_cash_2025", "2025", "1506757", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB liquide 1506757.03 JUMP; tick1729"),
    ("bud_lsc_nb_equity_2025", "2025", "1274624", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB EV 1274623.57; tick1729"),
    ("bud_lsc_nb_fondsen_2025", "2025", "624659", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB fondsen 624658.51; tick1729"),
    ("bud_lsc_nb_overgedragen_2025", "2025", "649965", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB overgedragen resultaat 649965.06; tick1729"),
    ("bud_lsc_nb_debt_2025", "2025", "310315", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB schulden 310315.22; tick1729"),
    ("bud_lsc_nb_deferred_opbr_2025", "2025", "282078", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB overlopende/overgedragen opbrengsten 282077.68 to 2026; tick1729"),
    ("bud_lsc_nb_opbr_2025", "2025", "475607", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB werkingsopbrengsten 475606.66; tick1729"),
    ("bud_lsc_nb_werkingsuitkering_2025", "2025", "460354", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "JR toelichting werkingsuitkeringen 460353.71; tick1729"),
    ("bud_lsc_nb_diensten_2025", "2025", "227175", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB diensten 227175.09 (verplaatsingen 112296); tick1729"),
    ("bud_lsc_nb_staff_2025", "2025", "15920", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB bezoldigingen 15919.98; VTE Unknown; tick1729"),
    ("bud_lsc_nb_pnl_2025", "2025", "203213", "executed", "src_lsc_noordbrabant_nbb_ye2025", "strong", "NBB overschot boekjaar 203212.58; AV ~04.05.2026; tick1729"),
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
        "commitment_id": "comm_lsc_noordbrabant_jr2025_opbr",
        "title": "Leersteuncentrum Noord-Brabant YE2025 leftover VL leersteun dual (opbr 0.48m / staff 0.02m)",
        "entity_id": EID,
        "beneficiary": "Noord-Brabant pupils needing leersteun / Catholic school boards",
        "legal_basis": "WVV VZW; Decreet leersteun; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-04",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "475607",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00109506.pdf",
        "stated_goal": "Local leftover LSC Noord-Brabant dual map — official NBB YE2025; FOI VTE",
        "cut_option": "Publish IAC/OV4/GC envelope split of 0.46m werkingsuitkeringen; disclose VTE vs 16k staff; deferred opbr 0.28m path",
        "source_id": "src_lsc_noordbrabant_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>Leersteun>LSC_NoordBrabant>JR2025_L5",
        "notes": "tick1729; YE2025 dual after LSC OB; opbr 0.48m staff 0.02m pnl +203k cash 1.51m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_lsc_noordbrabant_opbr_0_48m_staff_0_02m_cash_1_51m",
        "name": "Leersteuncentrum Noord-Brabant YE2025: opbr 0.48m / staff 0.02m / cash 1.51m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Onderwijs>Leersteun>LSC_NoordBrabant>JR2025_L5",
        "annual_cost_eur": "475607",
        "total_cost_eur": "475607",
        "tco_notes": "Leftover LSC Noord-Brabant YE2025: opbr 0.48m (werkingsuitkeringen 0.46m) / diensten 0.23m (verplaatsingen 0.11m) / staff 0.02m VTE unpublished / pnl +203k / cash 1.51m JUMP / deferred opbr 0.28m; dual LSC OB",
        "confidence": "strong",
        "source_id": "src_lsc_noordbrabant_nbb_ye2025",
        "beneficiaries": "Noord-Brabant pupils / Catholic school boards",
        "stated_goal": "Local leftover LSC dual map — official NBB YE2025 after LSC Oost-Brabant",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 475607 / staff 15920 / pnl 203213 / assets 1584939",
        "absurdity_score": "3.0",
        "cost_score": "2.5",
        "difficulty": "2.0",
        "priority_index": "2.6",
        "cut_proposal": "Publish VL envelope matrix; disclose VTE/detacheringen; scrutinise cash buffer vs deferred opbr",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1729; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403; dual LSC OB 1728; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_lsc_noordbrabant_opbr_0_48m_staff_0_02m_vte_l5",
        "hierarchy_path": "Vlaanderen>Onderwijs>Leersteun>LSC_NoordBrabant>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB S-vzw publishes opbr 475607 / werkingsuitkeringen 460354 / staff 15920 / pnl 203213 / assets 1584939; VTE unpublished; IAC/OV4/GC envelope split and detacheringen opaque; AV notulen mei 2026",
        "why_it_matters": "Leftover VL leersteuncentrum dual with 0.48m opbr and tiny own payroll — need VL envelope transparency + staffing model",
        "priority": "7",
        "recipient_body": "Leersteuncentrum Noord-Brabant VZW / Bestuursorgaan",
        "recipient_email": "info@lscnb.be",
        "recipient_postal": "Frederik de Merodestraat 18 2800 Mechelen",
        "draft_letter_path": "docs/doge/foi/drafts/gap_lsc_noordbrabant_opbr_0_48m_staff_0_02m_vte_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_lsc_noordbrabant_jr2025_opbr",
        "linked_leaderboard_id": "lb_lsc_noordbrabant_opbr_0_48m_staff_0_02m_cash_1_51m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1729; human-send only; LSC OB FOI still ready; AGB/NSZ/Dijk92/APEFE still blocked; next tick 1730 MUST progress",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1729":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_lsc_noordbrabant_opbr_0_48m_staff_0_02m_vte_l5"
        r["notes"] = "DONE tick1729: LSC Noord-Brabant KBO 0799.959.988 NBB YE2025 opbr 475607 staff 15920 pnl 203213; FOI ready gap_lsc_noordbrabant_opbr_0_48m_staff_0_02m_vte_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1730",
        "title": "Mandatory progress@1730 coverage % layers A-E + waste top10",
        "sprint": "hole_fill",
        "priority": "10",
        "status": "open",
        "hierarchy_target": "L0",
        "entity_id": "gg_belgium",
        "instructions": "EVERY-10 MUST: refresh progress_every_10_ticks.md (coverage % layers A-E of TE) + doge_waste_top10_current.md (top 10 by priority_index). After LSC dual 1728-1729 / Dommelhof dual 1726-1727 / GO! 1725 / Natuurpunt 1724. Then spawn rq_1731 leftover hole-fill.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1729 LSC_NB; EVERY-10 MUST progress coverage % + waste top10",
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
        "last_unit_id": "rq_1729",
        "ticks_completed": "1729",
        "paused": "no",
        "notes": "tick1729 leftover Leersteuncentrum Noord-Brabant residual dual LSC OB; KBO 0799.959.988; official NBB S-vzw YE2025 deposit 2026-00109506 CDN 200; sourced euros assets 1584939 opbr 475607 werkingsuitkering 460354 staff 15920 diensten 227175 pnl 203213 cash 1506757 deferred 282078; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; NEXT rq_1730 EVERY-10 MUST progress coverage % + waste top10; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

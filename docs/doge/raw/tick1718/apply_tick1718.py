import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T22:05:00Z"
DATE = "2026-08-23"
EID = "vzw_boerenbond"


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
        "name_nl": "Boerenbond vzw (leftover VL farmers lobby / employers org; NOT MRBB holding / ABS)",
        "name_fr": "Boerenbond asbl (residuelle lobby agricole flamande)",
        "name_en": "Boerenbond leftover Flemish farmers association VZW",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.boerenbond.be",
        "foi_email": "boekhouding@boerenbond.be",
        "foi_postal": "Diestsevest 40 3000 Leuven",
        "notes": "tick1718 leftover Boerenbond after BIV/AGB/NSZ hunt; official NBB VOL-VZW YE2024 deposit 2025-00373835 CDN 200; KBO 0676.461.073; FOI subsidy split",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_boerenbond_nbb_ye2024",
        "title": "Boerenbond NBB VOL-VZW YE2024 deposit 2025-00373835",
        "url": "http://cdn.staatsbladmonitor.be/2025pdf/2025-00373835.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1718; AV 16.06.2025; neergelegd 13.08.2025; assets 11486087 opbr 26630731 code73 22741187 staff 15832262 VTE 146.3 pnl -922869",
    },
    {
        "source_id": "src_boerenbond_kbo",
        "title": "Boerenbond KBO 0676.461.073",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=676461073",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1718; VZW; Diestsevest 40 3000 Leuven",
    },
    {
        "source_id": "src_boerenbond_portal",
        "title": "Boerenbond.be official portal",
        "url": "https://www.boerenbond.be",
        "publisher": "Boerenbond vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1718; boekhouding@boerenbond.be",
    },
    {
        "source_id": "src_boerenbond_foi_contact_1718",
        "title": "Boerenbond FOI channel (boekhouding@boerenbond.be)",
        "url": "https://www.boerenbond.be",
        "publisher": "Boerenbond vzw",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1718; boekhouding@boerenbond.be; Diestsevest 40 3000 Leuven",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_boerenbond_assets_2024", "2024", "11486087", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB 20/58 assets 11486087; tick1718"),
    ("bud_boerenbond_va_2024", "2024", "1310092", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB VA 21/28 1310092; tick1718"),
    ("bud_boerenbond_vlottend_2024", "2024", "10175995", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB vlottend 29/58 10175995; tick1718"),
    ("bud_boerenbond_cash_2024", "2024", "3823452", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB liquide 54/58 3823452 DROP vs 4115282; tick1718"),
    ("bud_boerenbond_beleg_2024", "2024", "3311305", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB beleggingen 50/53 3311305; tick1718"),
    ("bud_boerenbond_equity_2024", "2024", "3585611", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB EV 10/15 3585611 (fondsen 6778105 + reserves 404116 + overgedragen -3596609); tick1718"),
    ("bud_boerenbond_debt_2024", "2024", "7773941", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB schulden 17/49 7773941; tick1718"),
    ("bud_boerenbond_opbrengsten_2024", "2024", "26630731", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB bedrijfsopbrengsten 70/76A 26630731; tick1718"),
    ("bud_boerenbond_omzet_2024", "2024", "1714883", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB omzet 70 1714883; tick1718"),
    ("bud_boerenbond_code73_2024", "2024", "22741187", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB code73 22741187 (lidgeld 1894010 + subsidies 20844540); tick1718"),
    ("bud_boerenbond_lidgeld_2024", "2024", "1894010", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB 730 lidgelden 1894010; tick1718"),
    ("bud_boerenbond_subsidies_2024", "2024", "20844540", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB 733 subsidies 20844540; public vs private split FOI; tick1718"),
    ("bud_boerenbond_andere_opbr_2024", "2024", "2174660", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB andere bedrijfsopbrengsten 74 2174660; tick1718"),
    ("bud_boerenbond_diensten_2024", "2024", "11138840", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB 61 diensten 11138840; tick1718"),
    ("bud_boerenbond_staff_2024", "2024", "15832262", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB 62 bezoldigingen 15832262 / VTE 146.3; tick1718"),
    ("bud_boerenbond_expl_2024", "2024", "-1074692", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB bedrijfswinst 9901 -1074692; tick1718"),
    ("bud_boerenbond_pnl_2024", "2024", "-922869", "executed", "src_boerenbond_nbb_ye2024", "strong", "NBB PnL 9904 -922869; AV 16.06.2025; tick1718"),
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
        "commitment_id": "comm_boerenbond_jr2024_opbr",
        "title": "Boerenbond YE2024 leftover VL farmers lobby (opbr 26.63m / subsidies 20.84m / staff 15.83m VTE 146.3)",
        "entity_id": EID,
        "beneficiary": "Boerenbond members / VL agriculture lobby",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; employers org",
        "decision_date": "2025-06-16",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "26630731",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2025pdf/2025-00373835.pdf",
        "stated_goal": "Local leftover Boerenbond map — official NBB YE2024; FOI subsidy split",
        "cut_option": "Publish public vs private subsidy split inside 20.84m code733; scrutinise staff 15.83m + diensten 11.14m on loss-making ops",
        "source_id": "src_boerenbond_nbb_ye2024",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Lobby>Boerenbond>JR2024_L5",
        "notes": "tick1718; YE2024; opbr 26.63m subsidies 20.84m lidgeld 1.89m staff 15.83m VTE 146.3 pnl -0.92m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_boerenbond_opbr_26_63m_subs_20_84m_staff_15_83m",
        "name": "Boerenbond YE2024 leftover VL farmers lobby: opbr 26.63m / subsidies 20.84m / staff 15.83m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Lobby>Boerenbond>JR2024_L5",
        "annual_cost_eur": "26630731",
        "total_cost_eur": "26630731",
        "tco_notes": "Leftover Boerenbond VZW YE2024: bedrijfsopbrengsten 26.63m of which subsidies 20.84m + lidgeld 1.89m; staff 15.83m / 146.3 VTE; diensten 11.14m; expl LOSS 1.07m / PnL LOSS 0.92m; assets 11.49m cash 3.82m",
        "confidence": "strong",
        "source_id": "src_boerenbond_nbb_ye2024",
        "beneficiaries": "VL farmers via Boerenbond lobby/services",
        "stated_goal": "Local leftover Boerenbond map — official NBB YE2024 CDN live",
        "measured_outcome": "Official NBB YE2024 2026-08-23: opbr 26630731 / subsidies 20844540 / staff 15832262 VTE 146.3 / pnl -922869",
        "absurdity_score": "5.5",
        "cost_score": "7.0",
        "difficulty": "3.0",
        "priority_index": "5.8",
        "cut_proposal": "Publish public-subsidy split of 20.84m; scrutinise LOSS ops with 15.83m staff; do not conflate with MRBB holding equity",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1718; leftover after AGB unpublished / NSZ CDN403 / BIV+LaScam done; distinct from MRBB holding; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_boerenbond_subs_20_84m_staff_15_83m_split_l5",
        "hierarchy_path": "Vlaanderen>Lobby>Boerenbond>JR2024_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes opbr 26630731 / code73 22741187 (lidgeld 1894010 + subsidies 20844540) / staff 15832262 VTE 146.3 / expl LOSS 1074692 / PnL LOSS 922869 / assets 11486087; public vs private subsidy split inside 20844540 Unknown; relation to MRBB/holding flows Unknown; AV notulen 16.06.2025; YE2025 status",
        "why_it_matters": "Leftover VL farmers lobby with live official YE2024 euros (26.6m opbr / 20.8m subsidies / 15.8m staff on LOSS) — need public-subsidy split",
        "priority": "8",
        "recipient_body": "Boerenbond vzw / Bestuursorgaan",
        "recipient_email": "boekhouding@boerenbond.be",
        "recipient_postal": "Diestsevest 40 3000 Leuven",
        "draft_letter_path": "docs/doge/foi/drafts/gap_boerenbond_subs_20_84m_staff_15_83m_split_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_boerenbond_jr2024_opbr",
        "linked_leaderboard_id": "lb_boerenbond_opbr_26_63m_subs_20_84m_staff_15_83m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1718; human-send only; NSZ/Blauwe/.../BIV FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1718":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_boerenbond_subs_20_84m_staff_15_83m_split_l5"
        r["notes"] = "DONE tick1718: Boerenbond KBO 0676.461.073 NBB YE2024 opbr 26630731 subsidies 20844540 staff 15832262 VTE 146.3 pnl -922869; FOI ready gap_boerenbond_subs_20_84m_staff_15_83m_split_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1719",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1719 after 1718 Boerenbond YE2024. Next every-10 is 1720 (MUST refresh progress+waste). SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Boerenbond/BIV/LaScam/deAuteurs/SACD/FARO/SOFAM/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1718 Boerenbond; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/GO!/POV/BVAS/IOED/HVZ/IGS; Boerenbond+BIV+LaScam DONE; next every-10 1720 MANDATORY",
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
        "last_unit_id": "rq_1718",
        "ticks_completed": "1718",
        "paused": "no",
        "notes": "tick1718 leftover Boerenbond VZW residual; KBO 0676.461.073; official NBB VOL-VZW YE2024 deposit 2025-00373835 CDN 200; sourced euros assets 11486087 opbr 26630731 code73 22741187 subsidies 20844540 lidgeld 1894010 staff 15832262 VTE 146.3 diensten 11138840 expl -1074692 pnl -922869; FOI ready subsidy split; NSZ still CDN 403; Blauwe/.../BIV FOI still ready; Natuurpunt opaque; Dijk92 CDN 403; APEFE no budget euros; AGB unpublished; NOT every-10 (next 1720 MANDATORY progress); next rq_1719 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

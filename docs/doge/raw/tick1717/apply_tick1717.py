import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T21:45:00Z"
DATE = "2026-08-23"
EID = "oi_biv"


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
        "name_nl": "BIV / Beroepsinstituut van Vastgoedmakelaars (leftover federal professional institute; NOT CIB / Federia)",
        "name_fr": "IPI / Institut Professionnel des Agents Immobiliers (residuel)",
        "name_en": "BIV leftover Belgian real-estate agents professional institute",
        "level": "other",
        "parent_id": "sec_federal",
        "community_language": "nl",
        "website": "https://www.biv.be",
        "foi_email": "info@biv.be",
        "foi_postal": "Luxemburgstraat 16B 1000 Brussel",
        "notes": "tick1717 leftover BIV after LaScam/AGB/NSZ hunt; official JV2025 finance live; KBO 0267.300.821; FOI NBB VTE",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_biv_jv2025_official",
        "title": "BIV Jaarverslag 2025 (official web; Financiële balans)",
        "url": "https://www.biv.be/jaarverslagen/2025/",
        "publisher": "BIV / IPI",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1717; Nationale Raad 25.03.2026; assets 3126436 opbr 11320352 lidgeld 10209751 bezoldigingen 3636101; 11004 makelaars",
    },
    {
        "source_id": "src_biv_kbo",
        "title": "BIV/IPI KBO 0267.300.821",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=267300821",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1717; Andere rechtsvorm; Luxemburgstraat 16 bus B 1000 Brussel; NACE 94.120",
    },
    {
        "source_id": "src_biv_portal",
        "title": "BIV jaarverslagen index",
        "url": "https://www.biv.be/nieuws/jaarverslagen",
        "publisher": "BIV / IPI",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1717; JV2025 + JV2024 web editions",
    },
    {
        "source_id": "src_biv_foi_contact_1717",
        "title": "BIV FOI channel (info@biv.be)",
        "url": "https://www.biv.be",
        "publisher": "BIV / IPI",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1717; info@biv.be; +32 2 505 38 50; Luxemburgstraat 16B 1000 Brussel",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
# round to whole euros for CSV consistency
budgets = [
    ("bud_biv_assets_2025", "2025", "3126436", "executed", "src_biv_jv2025_official", "strong", "JV2025 activa 3126436.04; Nationale Raad 25.03.2026; tick1717"),
    ("bud_biv_va_2025", "2025", "876399", "executed", "src_biv_jv2025_official", "strong", "JV2025 vaste activa 876399.39; tick1717"),
    ("bud_biv_vlottend_2025", "2025", "2250037", "executed", "src_biv_jv2025_official", "strong", "JV2025 vlottende activa 2250036.65; tick1717"),
    ("bud_biv_cash_2025", "2025", "1942664", "executed", "src_biv_jv2025_official", "strong", "JV2025 liquide middelen 1942663.80; tick1717"),
    ("bud_biv_equity_2025", "2025", "2269597", "executed", "src_biv_jv2025_official", "strong", "JV2025 eigen vermogen 2269597.33 (overgedragen 1732784 + sociaal passief 536813); tick1717"),
    ("bud_biv_debt_2025", "2025", "856839", "executed", "src_biv_jv2025_official", "strong", "JV2025 schulden 856838.71; tick1717"),
    ("bud_biv_opbrengsten_2025", "2025", "11320352", "executed", "src_biv_jv2025_official", "strong", "JV2025 totaal opbrengsten 11320351.90; tick1717"),
    ("bud_biv_lidgeld_2025", "2025", "10209751", "executed", "src_biv_jv2025_official", "strong", "JV2025 ledenbijdragen+dossierkosten 10209750.70; tick1717"),
    ("bud_biv_rappel_2025", "2025", "86987", "executed", "src_biv_jv2025_official", "strong", "JV2025 rappel+gerechtskosten 86987.20; tick1717"),
    ("bud_biv_fin_opbr_2025", "2025", "87333", "executed", "src_biv_jv2025_official", "strong", "JV2025 financiele opbrengsten 87332.79; tick1717"),
    ("bud_biv_diverse_opbr_2025", "2025", "691608", "executed", "src_biv_jv2025_official", "strong", "JV2025 diverse ontvangsten 691607.58; tick1717"),
    ("bud_biv_huur_opbr_2025", "2025", "129071", "executed", "src_biv_jv2025_official", "strong", "JV2025 opbrengsten huur 129070.51; tick1717"),
    ("bud_biv_diensten_2025", "2025", "6112900", "executed", "src_biv_jv2025_official", "strong", "JV2025 diverse goederen en diensten 6112900.29; tick1717"),
    ("bud_biv_zitpenningen_2025", "2025", "823771", "executed", "src_biv_jv2025_official", "strong", "JV2025 zitpenningen 823771.06; tick1717"),
    ("bud_biv_bezoldigingen_2025", "2025", "3636101", "executed", "src_biv_jv2025_official", "strong", "JV2025 bezoldigingen 3636101.07; VTE Unknown; tick1717"),
    ("bud_biv_verplaatsing_2025", "2025", "69096", "executed", "src_biv_jv2025_official", "strong", "JV2025 verplaatsingsonkosten 69096.06; tick1717"),
    ("bud_biv_belastingen_2025", "2025", "210586", "executed", "src_biv_jv2025_official", "strong", "JV2025 belastingen+RV 210585.70; tick1717"),
    ("bud_biv_afschrijvingen_2025", "2025", "156197", "executed", "src_biv_jv2025_official", "strong", "JV2025 afschrijvingen 156197.10; tick1717"),
    ("bud_biv_overgedragen_winst_2025", "2025", "291131", "executed", "src_biv_jv2025_official", "strong", "JV2025 over te dragen winst 291130.69; tick1717"),
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
        "commitment_id": "comm_biv_jv2025_lidgeld",
        "title": "BIV JV2025 leftover federal real-estate professional institute (lidgeld 10.21m / opbr 11.32m / bezoldigingen 3.64m)",
        "entity_id": EID,
        "beneficiary": "BIV-regulated vastgoedmakelaars / consumer protection via tucht+opsporing",
        "legal_basis": "Vastgoedmakelaarswet; federal professional institute under Middenstand minister; Bestuursdecreet openbaarheid",
        "decision_date": "2026-03-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "11320352",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.biv.be/jaarverslagen/2025/",
        "stated_goal": "Local leftover BIV map — official JV2025 finance live; FOI NBB VTE",
        "cut_option": "Do not treat full 11.3m as waste (member-funded); scrutinise diensten 6.11m + zitpenningen 0.82m + bezoldigingen 3.64m; publish NBB + VTE",
        "source_id": "src_biv_jv2025_official",
        "confidence": "strong",
        "hierarchy_path": "Belgie>Middenstand>BIV>JV2025_L5",
        "notes": "tick1717; YE2025; opbr 11.32m lidgeld 10.21m bezoldigingen 3.64m diensten 6.11m assets 3.13m; 11004 makelaars; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_biv_lidgeld_10_21m_opbr_11_32m_bezoldigingen_3_64m",
        "name": "BIV JV2025 leftover federal real-estate institute: lidgeld 10.21m / opbr 11.32m / bezoldigingen 3.64m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Belgie>Middenstand>BIV>JV2025_L5",
        "annual_cost_eur": "11320352",
        "total_cost_eur": "11320352",
        "tco_notes": "Leftover BIV YE2025: member-funded opbr 11.32m (lidgeld 10.21m) / diensten 6.11m / bezoldigingen 3.64m / zitpenningen 0.82m / assets 3.13m cash 1.94m; 11004 makelaars; VTE Unknown",
        "confidence": "strong",
        "source_id": "src_biv_jv2025_official",
        "beneficiaries": "Regulated vastgoedmakelaars + consumers via BIV tucht/opsporing",
        "stated_goal": "Local leftover BIV map — official JV2025 finance newly live after CMO residual",
        "measured_outcome": "Official BIV JV2025 2026-08-23: opbr 11320352 / lidgeld 10209751 / bezoldigingen 3636101 / assets 3126436",
        "absurdity_score": "4.0",
        "cost_score": "6.0",
        "difficulty": "2.5",
        "priority_index": "4.7",
        "cut_proposal": "Member-funded — do not treat as TE waste; scrutinise diensten 6.11m + zitpenningen 0.82m share; publish NBB + VTE",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1717; leftover after AGB unpublished / NSZ CDN403 / LaScam+deAuteurs done; federal professional institute; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_biv_lidgeld_10_21m_opbr_11_32m_nbb_vte_l5",
        "hierarchy_path": "Belgie>Middenstand>BIV>JV2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official JV2025 publishes assets 3126436 / opbr 11320352 / lidgeld 10209751 / diensten 6112900 / bezoldigingen 3636101 / zitpenningen 823771 / overgedragen winst 291131; NBB statutory PDF / deposit id Unknown; exact VTE Unknown; full revisorverslag; diverse ontvangsten 691608 composition; collectieve verzekeringspremie share inside lidgeld",
        "why_it_matters": "Leftover federal professional institute with live official YE2025 euros (11.3m member-funded / 3.64m wages) — need NBB reconcile + VTE",
        "priority": "7",
        "recipient_body": "BIV / Beroepsinstituut van Vastgoedmakelaars / Nationale Raad",
        "recipient_email": "info@biv.be",
        "recipient_postal": "Luxemburgstraat 16B 1000 Brussel",
        "draft_letter_path": "docs/doge/foi/drafts/gap_biv_lidgeld_10_21m_opbr_11_32m_nbb_vte_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_biv_jv2025_lidgeld",
        "linked_leaderboard_id": "lb_biv_lidgeld_10_21m_opbr_11_32m_bezoldigingen_3_64m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1717; human-send only; NSZ/Blauwe/Sabam/.../LaScam/deAuteurs FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1717":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_biv_lidgeld_10_21m_opbr_11_32m_nbb_vte_l5"
        r["notes"] = "DONE tick1717: BIV KBO 0267.300.821 JV2025 opbr 11320352 lidgeld 10209751 bezoldigingen 3636101 assets 3126436; FOI ready gap_biv_lidgeld_10_21m_opbr_11_32m_nbb_vte_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1718",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1718 after 1717 BIV JV2025. Next every-10 is 1720. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo BIV/LaScam/deAuteurs/SACD/FARO/SOFAM/Welzijnszorg/PlayRight/SIMIM/Reprobel/Auvibel/Sabam/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1717 BIV; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/GO!/POV/BVAS/IOED/HVZ/IGS; BIV+LaScam+deAuteurs+SACD DONE; next every-10 1720",
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
        "last_unit_id": "rq_1717",
        "ticks_completed": "1717",
        "paused": "no",
        "notes": "tick1717 leftover BIV residual; KBO 0267.300.821; official Jaarverslag 2025 finance live biv.be; sourced euros assets 3126436 opbr 11320352 lidgeld 10209751 diensten 6112900 bezoldigingen 3636101 zitpenningen 823771 overgedragen_winst 291131 cash 1942664; 11004 makelaars; FOI ready NBB/VTE; NSZ still CDN 403; Blauwe/Sabam/.../LaScam/deAuteurs FOI still ready; Natuurpunt opaque; Dijk92 CDN 403; APEFE no budget euros; AGB unpublished; NOT every-10 (next 1720); next rq_1718 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

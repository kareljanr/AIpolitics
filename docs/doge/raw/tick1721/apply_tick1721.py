import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T23:05:00Z"
DATE = "2026-08-23"
EID = "vzw_boek"


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
        "name_nl": "Boeren op een Kruispunt vzw (leftover VL farmer crisis-help NGO; NOT Boerenbond / Landelijke Gilden / ABS)",
        "name_fr": "Boeren op een Kruispunt asbl (residuelle aide agriculteurs flamands)",
        "name_en": "Boeren op een Kruispunt leftover Flemish farmer support NGO",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.boerenopeenkruispunt.be",
        "foi_email": "info@boerenopeenkruispunt.be",
        "foi_postal": "Liefkenshoek 22 9230 Wetteren",
        "notes": "tick1721 leftover BoeK after Boerenbond/LandelijkeGilden/AGB hunt; official NBB VKT-VZW YE2025 deposit 2026-00078929 CDN 200; KBO 0886.502.992; FOI 70/73 VL-subsidy split",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_boek_nbb_ye2025",
        "title": "Boeren op een Kruispunt NBB VKT-VZW YE2025 deposit 2026-00078929",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00078929.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1721; AV 27.03.2026; assets 1589020 bruto 1028070 staff 1039419 VTE 11.3 pnl -39913; 70/73 empty",
    },
    {
        "source_id": "src_boek_jv2025_official",
        "title": "Boeren op een Kruispunt Jaarverslag 2025 (official org PDF; pie charts)",
        "url": "https://www.boerenopeenkruispunt.be/sites/default/files/2026-04/Jaarverslag-2025-web.pdf",
        "publisher": "Boeren op een Kruispunt vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1721; published 02.04.2026; income pie VL Overheid 32pct / mentaal welbevinden 43pct / BB-Ferm 6pct; cost pie personeel 80pct; no absolute euros in text extract",
    },
    {
        "source_id": "src_boek_kbo",
        "title": "Boeren op een Kruispunt KBO 0886.502.992",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=886502992",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1721; VZW; Liefkenshoek 22 9230 Wetteren",
    },
    {
        "source_id": "src_boek_foi_contact_1721",
        "title": "Boeren op een Kruispunt FOI channel",
        "url": "https://www.boerenopeenkruispunt.be",
        "publisher": "Boeren op een Kruispunt vzw",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1721; info@boerenopeenkruispunt.be; 0800 99 138; Liefkenshoek 22 9230 Wetteren",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_boek_assets_2025", "2025", "1589020", "executed", "src_boek_nbb_ye2025", "strong", "NBB 20/58 assets 1589020 JUMP vs 1106694; tick1721"),
    ("bud_boek_va_2025", "2025", "585116", "executed", "src_boek_nbb_ye2025", "strong", "NBB VA 21/28 585116 JUMP (CIP/aanbouw 296377); tick1721"),
    ("bud_boek_vlottend_2025", "2025", "1003904", "executed", "src_boek_nbb_ye2025", "strong", "NBB vlottend 29/58 1003904; tick1721"),
    ("bud_boek_cash_2025", "2025", "791318", "executed", "src_boek_nbb_ye2025", "strong", "NBB liquide 54/58 791318 JUMP vs 386262; tick1721"),
    ("bud_boek_equity_2025", "2025", "675180", "executed", "src_boek_nbb_ye2025", "strong", "NBB EV 10/15 675180 (bestemde 423556 + overgedragen 251625); tick1721"),
    ("bud_boek_debt_2025", "2025", "913840", "executed", "src_boek_nbb_ye2025", "strong", "NBB schulden 17/49 913840 JUMP (LT fin 223407 + ST 165433 + overlopend 525000); tick1721"),
    ("bud_boek_bruto_2025", "2025", "1028070", "executed", "src_boek_nbb_ye2025", "strong", "NBB brutomarge 9900 1028070; 70/73 empty VKT; tick1721"),
    ("bud_boek_staff_2025", "2025", "1039419", "executed", "src_boek_nbb_ye2025", "strong", "NBB 62 1039419 / VTE 11.3; exceeds bruto; tick1721"),
    ("bud_boek_expl_2025", "2025", "-32628", "executed", "src_boek_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 -32628; tick1721"),
    ("bud_boek_pnl_2025", "2025", "-39913", "executed", "src_boek_nbb_ye2025", "strong", "NBB PnL 9904 -39913; AV 27.03.2026; tick1721"),
    ("bud_boek_lt_fin_debt_2025", "2025", "223407", "executed", "src_boek_nbb_ye2025", "strong", "NBB LT financiele schulden 223407; tick1721"),
    ("bud_boek_accrued_debt_2025", "2025", "525000", "executed", "src_boek_nbb_ye2025", "strong", "NBB overlopende rekeningen passief 525000 JUMP from 0; tick1721"),
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
        "commitment_id": "comm_boek_jr2025_bruto",
        "title": "Boeren op een Kruispunt YE2025 leftover VL farmer help NGO (bruto 1.03m / staff 1.04m VTE 11.3 / LOSS)",
        "entity_id": EID,
        "beneficiary": "VL farmers in crisis / psychosocial + business advice",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; VL farmer-welfare support",
        "decision_date": "2026-03-27",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1028070",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00078929.pdf",
        "stated_goal": "Local leftover BoeK map — official NBB YE2025; FOI VL-subsidy split",
        "cut_option": "Publish 70/73 VL/project subsidy split; scrutinise staff>bruto LOSS; accrued debt JUMP 0.53m",
        "source_id": "src_boek_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Landbouw>BoeK>JR2025_L5",
        "notes": "tick1721; YE2025; bruto 1.03m staff 1.04m VTE 11.3 pnl -40k assets 1.59m; JV pie VL 32pct / mentaal 43pct; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_boek_bruto_1_03m_staff_1_04m_loss_vte_11_3",
        "name": "Boeren op een Kruispunt YE2025 leftover VL farmer help NGO: bruto 1.03m / staff 1.04m LOSS",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Landbouw>BoeK>JR2025_L5",
        "annual_cost_eur": "1028070",
        "total_cost_eur": "1589020",
        "tco_notes": "Leftover BoeK VZW YE2025: bruto 1.03m / staff 1.04m exceeds bruto / VTE 11.3 / expl LOSS 33k / PnL LOSS 40k; assets JUMP 1.59m cash JUMP 0.79m / accrued debt JUMP 0.53m; 70/73 empty; JV pie VL Overheid 32pct + mentaal project 43pct",
        "confidence": "strong",
        "source_id": "src_boek_nbb_ye2025",
        "beneficiaries": "VL farmers/tuinders in financial/psychosocial crisis",
        "stated_goal": "Local leftover BoeK map — official NBB YE2025 + JV2025 pie live after Boerenbond dual",
        "measured_outcome": "Official NBB YE2025 2026-08-23: bruto 1028070 / staff 1039419 VTE 11.3 / pnl -39913 / assets 1589020",
        "absurdity_score": "4.0",
        "cost_score": "3.5",
        "difficulty": "2.5",
        "priority_index": "3.7",
        "cut_proposal": "Do not treat crisis-help as waste; publish VL/project subsidy split; scrutinise staff>bruto + accrued 0.53m",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1721; leftover after AGB unpublished / NSZ CDN403 / Boerenbond+LandelijkeGilden done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_boek_bruto_1_03m_staff_1_04m_subsidy_split_l5",
        "hierarchy_path": "Vlaanderen>Landbouw>BoeK>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VKT-VZW publishes bruto 1028070 / staff 1039419 VTE 11.3 / pnl -39913 / assets 1589020 / accrued debt JUMP 525000; omzet 70 empty / 73 empty / 60/61 empty; JV2025 pie claims VL Overheid 32pct + Project mentaal welbevinden 43pct + BB-Ferm 6pct without absolute euros; VL vs project vs gift split Unknown; AV notulen 27.03.2026",
        "why_it_matters": "Leftover VL farmer crisis-help NGO with live official YE2025 euros (1.03m bruto / staff>bruto LOSS) — need public-subsidy absolute split",
        "priority": "7",
        "recipient_body": "Boeren op een Kruispunt vzw / Bestuursorgaan",
        "recipient_email": "info@boerenopeenkruispunt.be",
        "recipient_postal": "Liefkenshoek 22 9230 Wetteren",
        "draft_letter_path": "docs/doge/foi/drafts/gap_boek_bruto_1_03m_staff_1_04m_subsidy_split_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_boek_jr2025_bruto",
        "linked_leaderboard_id": "lb_boek_bruto_1_03m_staff_1_04m_loss_vte_11_3",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1721; human-send only; Boerenbond/LandelijkeGilden FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1721":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_boek_bruto_1_03m_staff_1_04m_subsidy_split_l5"
        r["notes"] = "DONE tick1721: BoeK KBO 0886.502.992 NBB YE2025 bruto 1028070 staff 1039419 VTE 11.3 pnl -39913; FOI ready gap_boek_bruto_1_03m_staff_1_04m_subsidy_split_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1722",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1722 after 1721 BoeK YE2025. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo BoeK/LandelijkeGilden/Boerenbond/BIV/LaScam/deAuteurs/SACD/FARO/SOFAM/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, ABS/GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1721 BoeK; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS; BoeK+Boerenbond+LandelijkeGilden DONE; next every-10 1730",
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
        "last_unit_id": "rq_1721",
        "ticks_completed": "1721",
        "paused": "no",
        "notes": "tick1721 leftover Boeren op een Kruispunt VZW residual; KBO 0886.502.992; official NBB VKT-VZW YE2025 deposit 2026-00078929 CDN 200 + JV2025 pie; sourced euros assets 1589020 bruto 1028070 staff 1039419 VTE 11.3 pnl -39913 cash JUMP 791318 accrued debt JUMP 525000; 70/73 empty; FOI ready subsidy split; NSZ still CDN 403; AGB unpublished; NOT every-10 (next 1730); next rq_1722 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

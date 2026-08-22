import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T00:25:00Z"
DATE = "2026-08-24"
EID = "voi_go"


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
        "name_nl": "GO! onderwijs van de Vlaamse Gemeenschap / centrale diensten (leftover VL gemeenschapsonderwijs VOI; NOT OVSG / KOV / POV)",
        "name_fr": "GO! enseignement de la Communaute flamande / services centraux (residuel)",
        "name_en": "GO! Education of the Flemish Community central services leftover VOI",
        "level": "agency",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.g-o.be",
        "foi_email": "info@g-o.be",
        "foi_postal": "Willebroekkaai 36 1000 Brussel",
        "notes": "tick1725 leftover GO! after AGB/NSZ/Dijk92/APEFE/ABS hunt; official JR2024 centrale diensten text PDF (publicaties.vlaanderen.be/view-file/77989); Raad GO! 21.03.2025; FOI scholengroepen consolidatie + VTE",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_go_jr2024",
        "title": "GO! Jaarverslag 2024 official PDF (centrale diensten finance)",
        "url": "https://publicaties.vlaanderen.be/view-file/77989",
        "publisher": "GO! / publicaties.vlaanderen.be",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1725; Raad GO! 21.03.2025; tables in kEUR; assets 1162467k opbr 48780k staff 17574k pnl 6388k",
    },
    {
        "source_id": "src_go_portal",
        "title": "GO! official portal",
        "url": "https://www.g-o.be",
        "publisher": "GO! onderwijs van de Vlaamse Gemeenschap",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1725; Willebroekkaai 36 1000 Brussel; info@g-o.be",
    },
    {
        "source_id": "src_go_vlaanderen_pub",
        "title": "Vlaanderen.be publication page GO! jaarverslag",
        "url": "https://www.vlaanderen.be/publicaties/jaarverslag-go-onderwijs-van-de-vlaamse-gemeenschap",
        "publisher": "Vlaamse overheid",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1725; JR2024 published Sep 2025",
    },
    {
        "source_id": "src_go_foi_contact_1725",
        "title": "GO! FOI channel",
        "url": "https://www.g-o.be",
        "publisher": "GO!",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1725; info@g-o.be; Willebroekkaai 36 1000 Brussel",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

# amounts: JR tables in kEUR -> full EUR
fields, rows = read("budgets.csv")
budgets = [
    ("bud_go_assets_2024", "2024", "1162467000", "executed", "src_go_jr2024", "strong", "JR2024 centrale diensten assets 1162467 kEUR; tick1725"),
    ("bud_go_va_2024", "2024", "966544000", "executed", "src_go_jr2024", "strong", "JR2024 VA 966544 kEUR; tick1725"),
    ("bud_go_mva_2024", "2024", "962218000", "executed", "src_go_jr2024", "strong", "JR2024 MVA 962218 kEUR; tick1725"),
    ("bud_go_buildings_2024", "2024", "675677000", "executed", "src_go_jr2024", "strong", "JR2024 terreinen/gebouwen 675677 kEUR; tick1725"),
    ("bud_go_cip_2024", "2024", "285837000", "executed", "src_go_jr2024", "strong", "JR2024 activa in aanbouw 285837 kEUR; tick1725"),
    ("bud_go_vlottend_2024", "2024", "195923000", "executed", "src_go_jr2024", "strong", "JR2024 vlottend 195923 kEUR; tick1725"),
    ("bud_go_beleg_2024", "2024", "174000000", "executed", "src_go_jr2024", "strong", "JR2024 geldbeleggingen 174000 kEUR; tick1725"),
    ("bud_go_cash_2024", "2024", "52708000", "executed", "src_go_jr2024", "strong", "JR2024 liquide 52708 kEUR JUMP vs 5985k; tick1725"),
    ("bud_go_equity_2024", "2024", "1104267000", "executed", "src_go_jr2024", "strong", "JR2024 EV 1104267 kEUR; tick1725"),
    ("bud_go_kapsubs_2024", "2024", "700003000", "executed", "src_go_jr2024", "strong", "JR2024 kapitaalsubsidies 700003 kEUR; tick1725"),
    ("bud_go_debt_2024", "2024", "40687000", "executed", "src_go_jr2024", "strong", "JR2024 schulden 40687 kEUR; tick1725"),
    ("bud_go_st_fin_debt_2024", "2024", "20775000", "executed", "src_go_jr2024", "strong", "JR2024 ST fin schulden kredietinstellingen 20775 kEUR; tick1725"),
    ("bud_go_opbr_2024", "2024", "48780000", "executed", "src_go_jr2024", "strong", "JR2024 bedrijfsopbrengsten 48780 kEUR; omzet 70 empty; tick1725"),
    ("bud_go_code73_2024", "2024", "46621000", "executed", "src_go_jr2024", "strong", "JR2024 andere bedrijfsopbrengsten 73/74 46621 kEUR; tick1725"),
    ("bud_go_staff_2024", "2024", "17574000", "executed", "src_go_jr2024", "strong", "JR2024 bezoldigingen 62 17574 kEUR; VTE Unknown; tick1725"),
    ("bud_go_diensten_2024", "2024", "22785000", "executed", "src_go_jr2024", "strong", "JR2024 diensten 61 22785 kEUR; tick1725"),
    ("bud_go_expl_2024", "2024", "-33533000", "executed", "src_go_jr2024", "strong", "JR2024 bedrijfswinst 9901 -33533 kEUR LOSS; tick1725"),
    ("bud_go_pnl_2024", "2024", "6388000", "executed", "src_go_jr2024", "strong", "JR2024 PnL 9904 +6388 kEUR; Raad 21.03.2025; tick1725"),
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
        "commitment_id": "comm_go_jr2024_centrale_opbr",
        "title": "GO! JR2024 centrale diensten (opbr 48.78m / staff 17.57m / assets 1.16bn)",
        "entity_id": EID,
        "beneficiary": "GO! scholen/CLB/centrale diensten Vlaanderen+Brussel",
        "legal_basis": "Bijzonder decreet 17.07.1998 gemeenschapsonderwijs; Bestuursdecreet openbaarheid",
        "decision_date": "2025-03-21",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "48780000",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://publicaties.vlaanderen.be/view-file/77989",
        "stated_goal": "Local leftover GO! centrale map — official JR2024; FOI scholengroepen+VTE",
        "cut_option": "Publish VL toelage split of 46.62m code73/74; VTE for 17.57m staff; scholengroepen consolidation; kapsubs 700m path",
        "source_id": "src_go_jr2024",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>GO!>JR2024_centrale_L5",
        "notes": "tick1725; JR2024 centrale only (not full scholengroepen consol); opbr 48.78m staff 17.57m assets 1.16bn kapsubs 700m pnl +6.39m; dual residual after OVSG/KOV; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_go_centrale_opbr_48_78m_staff_17_57m_assets_1_16bn",
        "name": "GO! JR2024 centrale diensten: opbr 48.78m / staff 17.57m / assets 1.16bn",
        "level": "L5",
        "type": "agency_budget",
        "hierarchy_path": "Vlaanderen>Onderwijs>GO!>JR2024_centrale_L5",
        "annual_cost_eur": "48780000",
        "total_cost_eur": "48780000",
        "tco_notes": "Leftover GO! VOI centrale diensten JR2024: bedrijfsopbr 48.78m (73/74 46.62m; omzet 70 empty) / staff 17.57m / diensten 22.79m / expl -33.53m / pnl +6.39m; assets 1.16bn / kapsubs 700m / buildings 676m; scholengroepen consol FOI",
        "confidence": "strong",
        "source_id": "src_go_jr2024",
        "beneficiaries": "GO! pupils / staff / scholengroepen",
        "stated_goal": "Local leftover GO! map — official JR2024 after OVSG/KOV education duals",
        "measured_outcome": "Official JR2024 2026-08-24: opbr 48780000 / staff 17574000 / assets 1162467000 / pnl 6388000",
        "absurdity_score": "3.5",
        "cost_score": "5.0",
        "difficulty": "3.0",
        "priority_index": "4.0",
        "cut_proposal": "Publish VL funding matrix for 46.62m other opbr; VTE; full scholengroepen consol; scrutinise kapsubs 700m + expl loss 33.5m",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1725; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / ABS no NBB; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_go_centrale_assets_1_16bn_opbr_48_78m_staff_17_57m_l5",
        "hierarchy_path": "Vlaanderen>Onderwijs>GO!>JR2024_centrale_L5",
        "entity_id": EID,
        "what_is_missing": "Official JR2024 centrale diensten publishes assets 1162467000 / opbr 48780000 / staff 17574000 / pnl 6388000 / kapsubs 700003000; omzet 70 empty; VTE unpublished; scholengroepen consolidation unpublished in this JR extract",
        "why_it_matters": "Leftover VL gemeenschapsonderwijs VOI with 1.16bn assets and 48.78m centrale opbr — need VL funding split + full network consol",
        "priority": "8",
        "recipient_body": "GO! onderwijs van de Vlaamse Gemeenschap / Raad van het GO!",
        "recipient_email": "info@g-o.be",
        "recipient_postal": "Willebroekkaai 36 1000 Brussel",
        "draft_letter_path": "docs/doge/foi/drafts/gap_go_centrale_assets_1_16bn_opbr_48_78m_staff_17_57m_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_go_jr2024_centrale_opbr",
        "linked_leaderboard_id": "lb_go_centrale_opbr_48_78m_staff_17_57m_assets_1_16bn",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1725; human-send only; OVSG/KOV FOI still ready; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1725":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_go_centrale_assets_1_16bn_opbr_48_78m_staff_17_57m_l5"
        r["notes"] = "DONE tick1725: GO! JR2024 centrale opbr 48780000 staff 17574000 assets 1162467000 pnl 6388000; FOI ready gap_go_centrale_assets_1_16bn_opbr_48_78m_staff_17_57m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1726",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1726 after 1725 GO! JR2024 centrale. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo GO!/Natuurpunt/OVSG/KOV/KLJ/BoeK/LandelijkeGilden/Boerenbond/BIV/LaScam/deAuteurs/SACD/FARO/SOFAM/NSZ. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1725 GO!; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS; GO!+Natuurpunt+OVSG+KOV DONE; next every-10 1730",
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
        "last_unit_id": "rq_1725",
        "ticks_completed": "1725",
        "paused": "no",
        "notes": "tick1725 leftover GO! JR2024 centrale diensten residual; official JR2024 publicaties.vlaanderen.be/view-file/77989; sourced euros assets 1162467000 opbr 48780000 code73 46621000 staff 17574000 diensten 22785000 expl -33533000 pnl 6388000 kapsubs 700003000 cash 52708000; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/ASGB no NBB; NOT every-10 (next 1730); next rq_1726 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

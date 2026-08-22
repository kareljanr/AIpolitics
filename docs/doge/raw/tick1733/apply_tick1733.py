import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T03:05:00Z"
DATE = "2026-08-24"
EID = "vzw_veilige_have"


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
        "name_nl": "Woonzorgcentrum Veilige Have VZW (leftover VL WZC Aalter; NOT Witte Meren / Ter Engelen)",
        "name_fr": "Maison de repos Veilige Have asbl (residuelle Aalter)",
        "name_en": "Veilige Have residential care home leftover Flemish WZC Aalter",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.veiligehave.be",
        "foi_email": "info@veiligehave.be",
        "foi_postal": "Lostraat 28 9880 Aalter",
        "notes": "tick1733 leftover VL WZC after Witte Meren; official NBB VOL-VZW YE2025 deposit 2026-00279398 CDN 200; KBO 0449.507.205; FOI LOSS + qualified audit + borgstellingen",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_veilige_have_nbb_ye2025",
        "title": "WZC Veilige Have NBB VOL-VZW YE2025 deposit 2026-00279398",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00279398.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1733; AV 18.06.2026; assets 46554342 opbr 29978917 staff 20324429 VTE 291.9 pnl -448409; Figurad oordeel met voorbehoud",
    },
    {
        "source_id": "src_veilige_have_kbo",
        "title": "WZC Veilige Have KBO 0449.507.205",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=449507205",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1733; VZW; Lostraat 28 9880 Aalter",
    },
    {
        "source_id": "src_veilige_have_portal",
        "title": "Veilige Have official portal",
        "url": "https://www.veiligehave.be",
        "publisher": "Woonzorgcentrum Veilige Have",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1733; WZC Aalter",
    },
    {
        "source_id": "src_veilige_have_foi_contact_1733",
        "title": "Veilige Have FOI channel",
        "url": "https://www.veiligehave.be",
        "publisher": "Woonzorgcentrum Veilige Have VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1733; info@veiligehave.be; Lostraat 28 9880 Aalter",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_veiligehave_assets_2025", "2025", "46554342", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB 20/58 assets 46554342; tick1733"),
    ("bud_veiligehave_va_2025", "2025", "28277988", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB VA 21/28 28277988; tick1733"),
    ("bud_veiligehave_buildings_2025", "2025", "25161317", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB terreinen/gebouwen 25161317; tick1733"),
    ("bud_veiligehave_vlottend_2025", "2025", "18276354", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB vlottend 18276354; tick1733"),
    ("bud_veiligehave_cash_2025", "2025", "5404854", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB liquide 5404854; tick1733"),
    ("bud_veiligehave_equity_2025", "2025", "33395931", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB EV 33395931; tick1733"),
    ("bud_veiligehave_kapsubs_2025", "2025", "7547764", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB kapitaalsubsidies 7547764; tick1733"),
    ("bud_veiligehave_voorzieningen_2025", "2025", "111890", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB voorzieningen pensioen 111890 NEW; tick1733"),
    ("bud_veiligehave_debt_2025", "2025", "13046521", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB schulden 13046521; tick1733"),
    ("bud_veiligehave_lt_fin_2025", "2025", "7028294", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB LT kredietinstellingen 7028294; tick1733"),
    ("bud_veiligehave_opbr_2025", "2025", "29978917", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 29978917; tick1733"),
    ("bud_veiligehave_omzet_2025", "2025", "23144753", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB omzet 70 23144753; tick1733"),
    ("bud_veiligehave_code73_2025", "2025", "343029", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB code73/subsidies 733 343029 JUMP vs 0; tick1733"),
    ("bud_veiligehave_andere_opbr_2025", "2025", "6283647", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB andere bedrijfsopbrengsten 74 6283647; FOI split; tick1733"),
    ("bud_veiligehave_staff_2025", "2025", "20324429", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB 62 20324429 / VTE 291.9; tick1733"),
    ("bud_veiligehave_diensten_2025", "2025", "4528734", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB diensten 61 4528734 JUMP vs 3338853; tick1733"),
    ("bud_veiligehave_expl_2025", "2025", "-334928", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 -334928 LOSS; tick1733"),
    ("bud_veiligehave_pnl_2025", "2025", "-448409", "executed", "src_veilige_have_nbb_ye2025", "strong", "NBB PnL 9904 -448409 LOSS; AV 18.06.2026; Figurad voorbehoud; tick1733"),
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
        "commitment_id": "comm_veilige_have_jr2025_opbr",
        "title": "WZC Veilige Have YE2025 leftover VL WZC (opbr 29.98m / staff 20.32m / LOSS 0.45m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Aalter",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-06-18",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "29978917",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00279398.pdf",
        "stated_goal": "Local leftover Veilige Have WZC map — official NBB YE2025; FOI LOSS + qualified audit + borg",
        "cut_option": "Publish andere-opbr 6.28m + code73 0.34m split; explain diensten JUMP 4.53m + LOSS 0.45m; map solidaire borgstellingen + Figurad voorbehoud",
        "source_id": "src_veilige_have_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>VeiligeHave>JR2025_L5",
        "notes": "tick1733; YE2025; opbr 29.98m omzet 23.14m staff 20.32m VTE 291.9 pnl -448k assets 46.55m debt 13.05m kapsubs 7.55m; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_veiligehave_opbr_29_98m_staff_20_32m_loss_0_45m",
        "name": "WZC Veilige Have YE2025: opbr 29.98m / staff 20.32m / LOSS 0.45m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>VeiligeHave>JR2025_L5",
        "annual_cost_eur": "29978917",
        "total_cost_eur": "29978917",
        "tco_notes": "Leftover Veilige Have WZC YE2025: opbr 29.98m (omzet 23.14m / code73 0.34m / andere 6.28m) / staff 20.32m VTE 291.9 / diensten JUMP 4.53m / pnl -0.45m LOSS; assets 46.55m debt 13.05m kapsubs 7.55m; Figurad oordeel met voorbehoud + solidaire borgstellingen FOI",
        "confidence": "strong",
        "source_id": "src_veilige_have_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Aalter",
        "stated_goal": "Local leftover Veilige Have WZC map — official NBB YE2025 after Witte Meren residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 29978917 / staff 20324429 VTE 291.9 / pnl -448409 / assets 46554342",
        "absurdity_score": "4.5",
        "cost_score": "4.5",
        "difficulty": "2.5",
        "priority_index": "4.2",
        "cut_proposal": "Publish RIZIV/VL/gemeente split of andere-opbr+subs; explain LOSS + diensten JUMP; disclose solidaire borg scope and Figurad qualification basis",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1733; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / WitteMeren+TerEngelen done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_veiligehave_opbr_29_98m_staff_20_32m_loss_0_45m_l5",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>VeiligeHave>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes opbr 29978917 / omzet 23144753 / code73 343029 / andere 6283647 / staff 20324429 VTE 291.9 / pnl -448409 / assets 46554342; andere-opbr + subsidy donor split, solidaire borgstellingen detail, and Figurad qualification basis unpublished; AV notulen 18.06.2026",
        "why_it_matters": "Large leftover VL WZC with 29.98m opbr, 0.45m LOSS, and qualified audit + solidaire borg — need financing transparency and group-guarantee map",
        "priority": "9",
        "recipient_body": "Woonzorgcentrum Veilige Have VZW / Bestuursorgaan",
        "recipient_email": "info@veiligehave.be",
        "recipient_postal": "Lostraat 28 9880 Aalter",
        "draft_letter_path": "docs/doge/foi/drafts/gap_veiligehave_opbr_29_98m_staff_20_32m_loss_0_45m_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_veilige_have_jr2025_opbr",
        "linked_leaderboard_id": "lb_veiligehave_opbr_29_98m_staff_20_32m_loss_0_45m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1733; human-send only; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1733":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_veiligehave_opbr_29_98m_staff_20_32m_loss_0_45m_l5"
        r["notes"] = "DONE tick1733: Veilige Have KBO 0449.507.205 NBB YE2025 opbr 29978917 staff 20324429 VTE 291.9 pnl -448409; FOI ready gap_veiligehave_opbr_29_98m_staff_20_32m_loss_0_45m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1734",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1734 after 1733 Veilige Have YE2025. Next every-10 is 1740. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC (e.g. Sint-Jozef Rumst / Molenheide if CDN live).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1733 VeiligeHave; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1740",
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
        "last_unit_id": "rq_1733",
        "ticks_completed": "1733",
        "paused": "no",
        "notes": "tick1733 leftover Veilige Have WZC residual; KBO 0449.507.205; official NBB VOL-VZW YE2025 deposit 2026-00279398 CDN 200; sourced euros assets 46554342 opbr 29978917 omzet 23144753 code73 343029 andere 6283647 staff 20324429 VTE 291.9 diensten 4528734 pnl -448409 debt 13046521 kapsubs 7547764; Figurad oordeel met voorbehoud + solidaire borg; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; NOT every-10 (next 1740); next rq_1734 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

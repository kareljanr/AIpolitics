import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T04:05:00Z"
DATE = "2026-08-24"
EID = "vzw_gravenkasteel"
GAP = "gap_gravenkasteel_opbr_101_46m_staff_61_89m_fva_29m_l5"
COMM = "comm_gravenkasteel_jr2025_opbr"
LB = "lb_gravenkasteel_opbr_101_46m_staff_61_89m_fva_29m"


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
        "name_nl": "Gravenkasteel VZW / WZC Gravenkasteel (leftover VL WZC Puurs-Sint-Amands / Armonea-Colisée; NOT Molenheide / Sint-Jozef)",
        "name_fr": "Gravenkasteel asbl / maison de repos (residuelle Puurs-Sint-Amands / Colisée)",
        "name_en": "Gravenkasteel residential care VZW leftover Flemish WZC Puurs-Sint-Amands Armonea-Colisée",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://armonea.be/huizen/gravenkasteel/",
        "foi_email": "gravenkasteel.admin@armonea.be",
        "foi_postal": "Lippelodorp 4 2890 Sint-Amands",
        "notes": "tick1736 leftover VL WZC after Molenheide; official NBB VOL-VZW YE2025 deposit 2026-00369595 CDN 200; KBO 0874.863.091; Colisée Belgium NV bestuurder; FOI FVA 29m group + omzet 88.2m multi-site split",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_gravenkasteel_nbb_ye2025",
        "title": "Gravenkasteel VZW NBB VOL-VZW YE2025 deposit 2026-00369595",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00369595.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1736; AV 30.06.2026; assets 49003218 opbr 101464389 staff 61893515 VTE 1007 pnl 2600926 FVA 29000000; EY oordeel zonder voorbehoud",
    },
    {
        "source_id": "src_gravenkasteel_kbo",
        "title": "Gravenkasteel VZW KBO 0874.863.091",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=874863091",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1736; VZW; Lippelodorp 4 2890 Sint-Amands",
    },
    {
        "source_id": "src_gravenkasteel_portal",
        "title": "Gravenkasteel Armonea portal",
        "url": "https://armonea.be/huizen/gravenkasteel/",
        "publisher": "Armonea / Colisée",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1736; WZC Sint-Amands; tel 052 25 82 82",
    },
    {
        "source_id": "src_gravenkasteel_foi_contact_1736",
        "title": "Gravenkasteel FOI channel",
        "url": "https://armonea.be/huizen/gravenkasteel/",
        "publisher": "Gravenkasteel VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1736; gravenkasteel.admin@armonea.be; Lippelodorp 4 2890 Sint-Amands",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_gravenkasteel_assets_2025", "2025", "49003218", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB 20/58 assets 49003218; tick1736"),
    ("bud_gravenkasteel_va_2025", "2025", "39832655", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB VA 21/28 39832655; tick1736"),
    ("bud_gravenkasteel_mva_2025", "2025", "9718577", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB MVA 9718577; tick1736"),
    ("bud_gravenkasteel_fva_2025", "2025", "29000000", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB FVA verbonden vorderingen 29000000 JUMP vs 26000000; FOI Colisée; tick1736"),
    ("bud_gravenkasteel_vlottend_2025", "2025", "8634593", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB vlottend 8634593; tick1736"),
    ("bud_gravenkasteel_cash_2025", "2025", "130872", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB liquide 130872 JUMP vs 22576; tick1736"),
    ("bud_gravenkasteel_equity_2025", "2025", "21280030", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB EV 21280030; tick1736"),
    ("bud_gravenkasteel_kapsubs_2025", "2025", "149044", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB kapitaalsubsidies 149044; tick1736"),
    ("bud_gravenkasteel_debt_2025", "2025", "27723188", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB schulden 27723188; tick1736"),
    ("bud_gravenkasteel_st_leveranciers_2025", "2025", "9107628", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB ST leveranciers 9107628; tick1736"),
    ("bud_gravenkasteel_st_soc_2025", "2025", "12048820", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB ST bezoldigingen/sociale 12048820; tick1736"),
    ("bud_gravenkasteel_overlopende_2025", "2025", "3470508", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB overlopende 3470508; tick1736"),
    ("bud_gravenkasteel_opbr_2025", "2025", "101464389", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 101464389; tick1736"),
    ("bud_gravenkasteel_omzet_2025", "2025", "88200515", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB omzet 70 88200515; FOI multi-site/RIZIV; tick1736"),
    ("bud_gravenkasteel_code73_2025", "2025", "40122", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB code73 40122 DROP vs 123534; tick1736"),
    ("bud_gravenkasteel_andere_opbr_2025", "2025", "13189657", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB andere 74 13189657; FOI split; tick1736"),
    ("bud_gravenkasteel_staff_2025", "2025", "61893515", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB 62 61893515 / VTE 1007; tick1736"),
    ("bud_gravenkasteel_diensten_2025", "2025", "30904543", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB diensten 61 30904543 JUMP vs 29316933; tick1736"),
    ("bud_gravenkasteel_expl_2025", "2025", "1920243", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 1920243; tick1736"),
    ("bud_gravenkasteel_pnl_2025", "2025", "2600926", "executed", "src_gravenkasteel_nbb_ye2025", "strong", "NBB PnL 9904 2600926; AV 30.06.2026; EY zonder voorbehoud; tick1736"),
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
        "title": "Gravenkasteel YE2025 leftover VL WZC (opbr 101.46m / staff 61.89m / FVA 29m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Armonea-Colisée BE",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-06-30",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "101464389",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00369595.pdf",
        "stated_goal": "Local leftover Gravenkasteel/Armonea WZC map — official NBB YE2025; FOI group FVA 29m + omzet split",
        "cut_option": "Publish omzet/andere multi-site RIZIV split; map 29m related receivables to Colisée restructuring; explain diensten JUMP 30.9m",
        "source_id": "src_gravenkasteel_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Gravenkasteel>JR2025_L5",
        "notes": "tick1736; YE2025; opbr 101.46m omzet 88.20m andere 13.19m staff 61.89m VTE 1007 pnl +2.60m assets 49.00m debt 27.72m FVA 29.00m; Colisée group; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Gravenkasteel YE2025: opbr 101.46m / staff 61.89m / FVA 29m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Gravenkasteel>JR2025_L5",
        "annual_cost_eur": "101464389",
        "total_cost_eur": "101464389",
        "tco_notes": "Leftover Armonea-Colisée Gravenkasteel VZW YE2025: opbr 101.46m (omzet 88.20m / andere 13.19m / code73 40k) / staff 61.89m VTE 1007 / diensten JUMP 30.90m / pnl +2.60m; assets 49.00m debt 27.72m FVA related recv JUMP 29.00m; EY zonder voorbehoud; Colisée debt-equity restructuring FOI",
        "confidence": "strong",
        "source_id": "src_gravenkasteel_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Armonea-Colisée BE",
        "stated_goal": "Local leftover Gravenkasteel WZC map — official NBB YE2025 after Molenheide residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 101464389 / staff 61893515 VTE 1007 / pnl 2600926 / FVA 29000000",
        "absurdity_score": "5.2",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "5.0",
        "cut_proposal": "Publish multi-site RIZIV/omzet split; disclose 29m Colisée related receivables vs group restructuring; explain 30.9m diensten + ST payroll/RSZ 12.0m",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1736; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Molenheide+SintJozef+VeiligeHave done; Colisée/Armonea; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Gravenkasteel>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes opbr 101464389 / omzet 88200515 / andere 13189657 / staff 61893515 VTE 1007 / pnl 2600926 / assets 49003218 / debt 27723188 / FVA related 29000000; multi-site RIZIV/omzet split and Colisée group receivable map unpublished; AV notulen 30.06.2026",
        "why_it_matters": "Largest leftover VL WZC VZW mined this sprint: 101m opbr + 29m related group receivables amid Colisée restructuring — need public-care financing transparency",
        "priority": "9",
        "recipient_body": "Gravenkasteel VZW / Colisée Belgium NV / Bestuursorgaan",
        "recipient_email": "gravenkasteel.admin@armonea.be",
        "recipient_postal": "Lippelodorp 4 2890 Sint-Amands",
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
        "notes": "tick1736; human-send only; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1736":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1736: Gravenkasteel KBO 0874.863.091 NBB YE2025 opbr 101464389 staff 61893515 VTE 1007 FVA 29000000; FOI ready gap_gravenkasteel_opbr_101_46m_staff_61_89m_fva_29m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1737",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1737 after 1736 Gravenkasteel YE2025. Next every-10 is 1740. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC/Armonea-Colisée sister if live.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1736 Gravenkasteel; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1740",
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
        "last_unit_id": "rq_1736",
        "ticks_completed": "1736",
        "paused": "no",
        "notes": "tick1736 leftover Gravenkasteel WZC residual; KBO 0874.863.091; official NBB VOL-VZW YE2025 deposit 2026-00369595 CDN 200; sourced euros assets 49003218 opbr 101464389 omzet 88200515 code73 40122 andere 13189657 staff 61893515 VTE 1007 diensten 30904543 pnl 2600926 debt 27723188 FVA 29000000; EY oordeel zonder voorbehoud; Colisée/Armonea; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; ABS/BVAS no NBB; NOT every-10 (next 1740); next rq_1737 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

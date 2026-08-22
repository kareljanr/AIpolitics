import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T04:25:00Z"
DATE = "2026-08-24"
EID = "nv_armonea"
GAP = "gap_armonea_opbr_265_19m_loss_51_31m_equity_neg_l5"
COMM = "comm_armonea_jr2025_opbr"
LB = "lb_armonea_opbr_265_19m_loss_51_31m_equity_neg"


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
        "name_nl": "Armonea NV (leftover VL WZC operator / Colisée Belgium; dual Gravenkasteel VZW; NOT Molenheide Vivalto)",
        "name_fr": "Armonea SA (opérateur MRS residuel / Colisée Belgique; dual Gravenkasteel)",
        "name_en": "Armonea NV leftover Flemish nursing-home operator Colisée Belgium dual Gravenkasteel",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.armonea.be",
        "foi_email": "info@armonea.be",
        "foi_postal": "Stationsstraat 102 2800 Mechelen",
        "notes": "tick1737 leftover Armonea-Colisée dual after Gravenkasteel; official NBB VOL-kap YE2025 deposit 2026-00279656 CDN 200; KBO 0889.421.308; LOSS 51.31m equity NEG 12.26m Art 7:228/7:229; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_armonea_nbb_ye2025",
        "title": "Armonea NV NBB VOL-kap YE2025 deposit 2026-00279656",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00279656.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1737; AV 30.06.2026; assets 215482047 opbr 265194864 staff 153076606 VTE 2309.5 pnl -51306832 equity -12259638 debt 227700106; EY zonder voorbehoud + Art 7:228/7:229",
    },
    {
        "source_id": "src_armonea_kbo",
        "title": "Armonea NV KBO 0889.421.308",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=889421308",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1737; NV; Stationsstraat 102 2800 Mechelen",
    },
    {
        "source_id": "src_armonea_portal",
        "title": "Armonea official portal",
        "url": "https://www.armonea.be",
        "publisher": "Armonea / Colisée",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1737; multi-site VL/WAL/BXL WZC operator",
    },
    {
        "source_id": "src_armonea_foi_contact_1737",
        "title": "Armonea FOI channel",
        "url": "https://www.armonea.be",
        "publisher": "Armonea NV",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1737; info@armonea.be; Stationsstraat 102 2800 Mechelen",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_armonea_assets_2025", "2025", "215482047", "executed", "src_armonea_nbb_ye2025", "strong", "NBB 20/58 assets 215482047; tick1737"),
    ("bud_armonea_va_2025", "2025", "143990268", "executed", "src_armonea_nbb_ye2025", "strong", "NBB VA 143990268; tick1737"),
    ("bud_armonea_fva_2025", "2025", "119790078", "executed", "src_armonea_nbb_ye2025", "strong", "NBB FVA 119790078 (deelnemingen 110974759 DROP + vorderingen 8500000); FOI; tick1737"),
    ("bud_armonea_vlottend_2025", "2025", "69000939", "executed", "src_armonea_nbb_ye2025", "strong", "NBB vlottend 69000939 JUMP; tick1737"),
    ("bud_armonea_cash_2025", "2025", "29013140", "executed", "src_armonea_nbb_ye2025", "strong", "NBB liquide 29013140 JUMP vs 4414712; tick1737"),
    ("bud_armonea_equity_2025", "2025", "-12259638", "executed", "src_armonea_nbb_ye2025", "strong", "NBB EV -12259638 NEG vs +39047194; Art 7:228/7:229; tick1737"),
    ("bud_armonea_overgedragen_2025", "2025", "-131300577", "executed", "src_armonea_nbb_ye2025", "strong", "NBB overgedragen verlies -131300577; tick1737"),
    ("bud_armonea_debt_2025", "2025", "227700106", "executed", "src_armonea_nbb_ye2025", "strong", "NBB schulden 227700106; tick1737"),
    ("bud_armonea_lt_overige_2025", "2025", "124000000", "executed", "src_armonea_nbb_ye2025", "strong", "NBB LT overige leningen 124000000 JUMP vs 74000000; FOI Colisée; tick1737"),
    ("bud_armonea_st_leveranciers_2025", "2025", "34822015", "executed", "src_armonea_nbb_ye2025", "strong", "NBB ST leveranciers 34822015; tick1737"),
    ("bud_armonea_st_soc_2025", "2025", "29431465", "executed", "src_armonea_nbb_ye2025", "strong", "NBB ST bezoldigingen/sociale 29431465; tick1737"),
    ("bud_armonea_opbr_2025", "2025", "265194864", "executed", "src_armonea_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 265194864; tick1737"),
    ("bud_armonea_omzet_2025", "2025", "225856316", "executed", "src_armonea_nbb_ye2025", "strong", "NBB omzet 70 225856316; FOI RIZIV multi-site; tick1737"),
    ("bud_armonea_andere_opbr_2025", "2025", "38795231", "executed", "src_armonea_nbb_ye2025", "strong", "NBB andere 74 38795231; FOI; tick1737"),
    ("bud_armonea_staff_2025", "2025", "153076606", "executed", "src_armonea_nbb_ye2025", "strong", "NBB 62 153076606 / VTE 2309.5; tick1737"),
    ("bud_armonea_diensten_2025", "2025", "114912835", "executed", "src_armonea_nbb_ye2025", "strong", "NBB diensten 61 114912835 JUMP vs 109913208; tick1737"),
    ("bud_armonea_expl_2025", "2025", "-21148356", "executed", "src_armonea_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 -21148356 LOSS; tick1737"),
    ("bud_armonea_nietrec_fincost_2025", "2025", "24208032", "executed", "src_armonea_nbb_ye2025", "strong", "NBB niet-recurrente financiële kosten 66B 24208032; FOI impairments; tick1737"),
    ("bud_armonea_pnl_2025", "2025", "-51306832", "executed", "src_armonea_nbb_ye2025", "strong", "NBB PnL 9904 -51306832 LOSS; AV 30.06.2026; EY zonder voorbehoud + Art 7:228/7:229; tick1737"),
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
        "title": "Armonea YE2025 leftover VL WZC operator (opbr 265.19m / LOSS 51.31m / equity NEG)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Armonea-Colisée BE",
        "legal_basis": "WVV NV; Woonzorgdecreet; Bestuursdecreet openbaarheid where applicable; Art 7:228-7:229 WVV",
        "decision_date": "2026-06-30",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "265194864",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00279656.pdf",
        "stated_goal": "Local leftover Armonea operator map — official NBB YE2025 dual Gravenkasteel; FOI Art 7:228/7:229 + Colisée loans",
        "cut_option": "Publish RIZIV multi-site omzet split; disclose 124m LT related loans + 24.2m non-rec fincost; publish Art 7:228 remediation path",
        "source_id": "src_armonea_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Armonea>JR2025_L5",
        "notes": "tick1737; YE2025; opbr 265.19m omzet 225.86m staff 153.08m VTE 2309.5 pnl -51.31m assets 215.48m equity -12.26m debt 227.70m FVA 119.79m; Colisée dual Gravenkasteel; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Armonea YE2025: opbr 265.19m / LOSS 51.31m / equity NEG 12.26m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Armonea>JR2025_L5",
        "annual_cost_eur": "265194864",
        "total_cost_eur": "265194864",
        "tco_notes": "Leftover Armonea-Colisée operator YE2025: opbr 265.19m (omzet 225.86m / andere 38.80m) / staff 153.08m VTE 2309.5 / diensten 114.91m / expl -21.15m / pnl -51.31m LOSS; equity -12.26m NEG; debt 227.70m (LT related 124m JUMP); FVA 119.79m; Art 7:228/7:229 alarm; EY zonder voorbehoud; dual Gravenkasteel VZW",
        "confidence": "strong",
        "source_id": "src_armonea_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Armonea-Colisée BE",
        "stated_goal": "Local leftover Armonea operator map — official NBB YE2025 dual after Gravenkasteel residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 265194864 / staff 153076606 VTE 2309.5 / pnl -51306832 / equity -12259638 / debt 227700106",
        "absurdity_score": "6.5",
        "cost_score": "6.8",
        "difficulty": "3.2",
        "priority_index": "6.2",
        "cut_proposal": "Publish RIZIV multi-site split; disclose Colisée 124m loans + 24.2m impairments; force Art 7:228/7:229 remediation transparency for public-care continuity",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1737; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Gravenkasteel+Molenheide done; Colisée; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Armonea>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-kap publishes opbr 265194864 / omzet 225856316 / staff 153076606 VTE 2309.5 / pnl -51306832 / equity -12259638 / debt 227700106 / LT related loans 124000000 / non-rec fincost 24208032; multi-site RIZIV split, Colisée loan/stand-still map, and Art 7:228 remediation unpublished; AV notulen 30.06.2026",
        "why_it_matters": "Largest commercial VL WZC operator: 265m opbr, 51m LOSS, NEG equity under Art 7:228/7:229 — public-care continuity risk amid Colisée restructuring",
        "priority": "10",
        "recipient_body": "Armonea NV / Colisée Belgium NV / Bestuursorgaan",
        "recipient_email": "info@armonea.be",
        "recipient_postal": "Stationsstraat 102 2800 Mechelen",
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
        "notes": "tick1737; human-send only; dual Gravenkasteel; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1737":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1737: Armonea NV KBO 0889.421.308 NBB YE2025 opbr 265194864 staff 153076606 VTE 2309.5 pnl -51306832 equity -12259638 Art7228; FOI ready gap_armonea_opbr_265_19m_loss_51_31m_equity_neg_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1738",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1738 after 1737 Armonea YE2025. Next every-10 is 1740. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC/Colisée sister if live.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1737 Armonea; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC; next every-10 1740",
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
        "last_unit_id": "rq_1737",
        "ticks_completed": "1737",
        "paused": "no",
        "notes": "tick1737 leftover Armonea NV residual dual Gravenkasteel; KBO 0889.421.308; official NBB VOL-kap YE2025 deposit 2026-00279656 CDN 200; sourced euros assets 215482047 opbr 265194864 omzet 225856316 andere 38795231 staff 153076606 VTE 2309.5 diensten 114912835 expl -21148356 pnl -51306832 equity -12259638 debt 227700106 lt_loans 124000000 fva 119790078 cash 29013140; EY oordeel zonder voorbehoud + Art 7:228/7:229; Colisée; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; NOT every-10 (next 1740); next rq_1738 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC/LSC/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

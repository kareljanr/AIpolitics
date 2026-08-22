import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T04:45:00Z"
DATE = "2026-08-24"
EID = "nv_colisee_belgium"
GAP = "gap_colisee_be_loss_79_75m_equity_neg_75_40m_fva_198_69m_l5"
COMM = "comm_colisee_be_jr2025_loss"
LB = "lb_colisee_be_loss_79_75m_equity_neg_75_40m_fva_198_69m"


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
        "name_nl": "Colisée Belgium SA/NV (leftover BE care holding / dual Armonea NV + Gravenkasteel VZW; NOT Vivalto Molenheide)",
        "name_fr": "Colisée Belgium SA (holding soins residuel / dual Armonea + Gravenkasteel)",
        "name_en": "Colisée Belgium SA leftover Belgian care holding dual Armonea + Gravenkasteel",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "fr",
        "website": "https://www.colisee-group.com",
        "foi_email": "info@armonea.be",
        "foi_postal": "Place Marcel Broodthaers 8 1060 Saint-Gilles",
        "notes": "tick1738 leftover Colisée holding dual after Armonea; official NBB C-cap YE2025 deposit 2026-00287864 CDN 200; KBO 0723.858.144; LOSS 79.75m equity NEG 75.40m Art 7:228/7:229; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_colisee_be_nbb_ye2025",
        "title": "Colisée Belgium SA NBB C-cap YE2025 deposit 2026-00287864",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00287864.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1738; AV 30.06.2026; assets 210559837 pnl -79747564 equity -75398013 debt 285957850 FVA 198685617; EY opinion sans reserve + Art 7:228/7:229",
    },
    {
        "source_id": "src_colisee_be_kbo",
        "title": "Colisée Belgium SA KBO 0723.858.144",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=723858144",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1738; SA/NV; Place Marcel Broodthaers 8 1060 Saint-Gilles",
    },
    {
        "source_id": "src_colisee_be_portal",
        "title": "Colisée Group portal",
        "url": "https://www.colisee-group.com",
        "publisher": "Colisée Group",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1738; European elderly-care group; BE holding",
    },
    {
        "source_id": "src_colisee_be_foi_contact_1738",
        "title": "Colisée Belgium FOI channel (dual Armonea Remy)",
        "url": "https://www.armonea.be",
        "publisher": "Colisée Belgium SA",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1738; info@armonea.be dual; Place Marcel Broodthaers 8 1060 Saint-Gilles",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_colisee_be_assets_2025", "2025", "210559837", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB 20/58 assets 210559837; tick1738"),
    ("bud_colisee_be_fva_2025", "2025", "198685617", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB FVA linked 198685617; tick1738"),
    ("bud_colisee_be_participations_2025", "2025", "152685617", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB participations 152685617 after new impairments 67218368; FOI Armonea map; tick1738"),
    ("bud_colisee_be_creances_liees_2025", "2025", "46000000", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB créances liées 46000000 JUMP vs 4000000; tick1738"),
    ("bud_colisee_be_cash_2025", "2025", "29405", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB cash 29405 DROP vs 5020793; tick1738"),
    ("bud_colisee_be_equity_2025", "2025", "-75398013", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB equity -75398013 NEG; Art 7:228/7:229; tick1738"),
    ("bud_colisee_be_reporte_2025", "2025", "-354980597", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB perte reportée -354980597; tick1738"),
    ("bud_colisee_be_debt_2025", "2025", "285957850", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB dettes 285957850; tick1738"),
    ("bud_colisee_be_lt_loans_2025", "2025", "219000000", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB LT autres emprunts 219000000; FOI; tick1738"),
    ("bud_colisee_be_st_autres_2025", "2025", "51871564", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB ST autres dettes 51871564 JUMP vs 5086198; tick1738"),
    ("bud_colisee_be_impair_particip_2025", "2025", "67218368", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB new réductions de valeur participations 67218368; tick1738"),
    ("bud_colisee_be_services_2025", "2025", "2238050", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB services 61 2238050 JUMP vs 561716; tick1738"),
    ("bud_colisee_be_fincost_2025", "2025", "83513826", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB charges financières 83513826 (non-rec 71953267); tick1738"),
    ("bud_colisee_be_expl_2025", "2025", "-2239047", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB perte d'exploitation 9901 -2239047; tick1738"),
    ("bud_colisee_be_pnl_2025", "2025", "-79747564", "executed", "src_colisee_be_nbb_ye2025", "strong", "NBB PnL 9904 -79747564 LOSS; AV 30.06.2026; EY sans réserve + Art 7:228/7:229; tick1738"),
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
        "title": "Colisée Belgium YE2025 leftover BE care holding (LOSS 79.75m / equity NEG 75.40m / FVA 198.69m)",
        "entity_id": EID,
        "beneficiary": "Armonea / Gravenkasteel care residents via Colisée holding",
        "legal_basis": "CSA SA; Woonzorgdecreet cascade via Armonea; Art 7:228-7:229 CSA",
        "decision_date": "2026-06-30",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "79747564",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00287864.pdf",
        "stated_goal": "Local leftover Colisée BE holding map — official NBB YE2025 dual Armonea; FOI Art 7:228 + FVA impairments",
        "cut_option": "Publish Armonea/Gravenkasteel ownership map; disclose 67.2m participation impairments + 219m LT loans + Art 7:228 remediation",
        "source_id": "src_colisee_be_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>ColiseeBelgium>JR2025_L5",
        "notes": "tick1738; YE2025 holding; pnl -79.75m equity -75.40m assets 210.56m debt 285.96m FVA 198.69m participations 152.69m; dual Armonea+Gravenkasteel; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Colisée Belgium YE2025: LOSS 79.75m / equity NEG 75.40m / FVA 198.69m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>ColiseeBelgium>JR2025_L5",
        "annual_cost_eur": "79747564",
        "total_cost_eur": "285957850",
        "tco_notes": "Leftover Colisée BE holding YE2025: shell opbr ~0 / pnl -79.75m LOSS / equity -75.40m NEG / debt 285.96m (LT 219m) / FVA 198.69m (participations 152.69m after +67.22m impairments; related créances JUMP 46m) / cash DROP to 29k; Art 7:228/7:229; EY sans réserve; dual Armonea NV + Gravenkasteel VZW public-care cascade",
        "confidence": "strong",
        "source_id": "src_colisee_be_nbb_ye2025",
        "beneficiaries": "Armonea / Gravenkasteel care residents via Colisée holding",
        "stated_goal": "Local leftover Colisée BE holding map — official NBB YE2025 dual after Armonea residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: pnl -79747564 / equity -75398013 / debt 285957850 / FVA 198685617 / impairments 67218368",
        "absurdity_score": "6.8",
        "cost_score": "6.5",
        "difficulty": "3.5",
        "priority_index": "6.4",
        "cut_proposal": "Force Art 7:228/7:229 remediation transparency; map 152.7m Armonea-group participations + 67.2m impairments; disclose 219m LT + stand-still vs public-care continuity",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1738; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Armonea+Gravenkasteel+Molenheide done; holding shell; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>ColiseeBelgium>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB C-cap publishes pnl -79747564 / equity -75398013 / debt 285957850 / FVA 198685617 / participations 152685617 / new impairments 67218368 / related créances 46000000; Armonea/Gravenkasteel ownership map and Art 7:228 remediation unpublished; AV notulen 30.06.2026",
        "why_it_matters": "Colisée BE holding controls Armonea 265m care opbr via 198.7m FVA while posting 79.8m LOSS and NEG equity under Art 7:228/7:229 — public-care continuity risk",
        "priority": "10",
        "recipient_body": "Colisée Belgium SA / Colisée International SA / Bestuursorgaan",
        "recipient_email": "info@armonea.be",
        "recipient_postal": "Place Marcel Broodthaers 8 1060 Saint-Gilles",
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
        "notes": "tick1738; human-send only; dual Armonea+Gravenkasteel; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1738":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1738: Colisée Belgium KBO 0723.858.144 NBB YE2025 pnl -79747564 equity -75398013 FVA 198685617 Art7228; FOI ready gap_colisee_be_loss_79_75m_equity_neg_75_40m_fva_198_69m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1739",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1739 after 1738 Colisée Belgium YE2025. Next every-10 is 1740 MUST. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC (e.g. Prinsenhof CDN 2026-00176220 live).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1738 ColiseeBelgium; NEXT AGB/NSZ-if-200/Prinsenhof-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC; next every-10 1740 MUST",
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
        "last_unit_id": "rq_1738",
        "ticks_completed": "1738",
        "paused": "no",
        "notes": "tick1738 leftover Colisée Belgium SA residual dual Armonea; KBO 0723.858.144; official NBB C-cap YE2025 deposit 2026-00287864 CDN 200; sourced euros assets 210559837 pnl -79747564 equity -75398013 debt 285957850 lt_loans 219000000 fva 198685617 participations 152685617 impair 67218368 creances 46000000 cash 29405; EY opinion sans reserve + Art 7:228/7:229; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; Prinsenhof CDN 2026-00176220 live unused; NOT every-10 (next 1740 MUST); next rq_1739 AGB/NSZ-if-200/Prinsenhof/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

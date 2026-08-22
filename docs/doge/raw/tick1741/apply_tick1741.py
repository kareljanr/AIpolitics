import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T05:45:00Z"
DATE = "2026-08-24"
EID = "nv_vivalto_home_be"
GAP = "gap_vivalto_be_opbr_9_37m_fva_249_21m_debt_219_77m_l5"
COMM = "comm_vivalto_be_jr2025_opbr"
LB = "lb_vivalto_be_opbr_9_37m_fva_249_21m_debt_219_77m"


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
        "name_nl": "Vivalto Home Belgium SA/NV (leftover BE care holding / dual Molenheide + Prinsenhof; NOT Colisée/Armonea)",
        "name_fr": "Vivalto Home Belgium SA (holding soins residuel / dual Molenheide + Prinsenhof)",
        "name_en": "Vivalto Home Belgium SA leftover Belgian care holding dual Molenheide + Prinsenhof",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "fr",
        "website": "https://www.vivaltohome.com",
        "foi_email": "info@vivaltohome.com",
        "foi_postal": "Avenue du Domaine 13 1190 Forest",
        "notes": "tick1741 leftover Vivalto holding dual after Prinsenhof/Molenheide; official NBB C-cap YE2025 deposit 2026-00180299 CDN 200; KBO 0820.420.456; FVA 249.21m debt 219.77m; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_vivalto_be_nbb_ye2025",
        "title": "Vivalto Home Belgium SA NBB C-cap YE2025 deposit 2026-00180299",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00180299.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1741; AV 22.05.2026; assets 266811008 opbr 9371794 staff 736811 VTE 5 pnl 4231615 FVA 249209728 debt 219774069; Mazars sans réserve",
    },
    {
        "source_id": "src_vivalto_be_kbo",
        "title": "Vivalto Home Belgium SA KBO 0820.420.456",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=820420456",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1741; SA/NV; Avenue du Domaine 13 1190 Forest",
    },
    {
        "source_id": "src_vivalto_be_portal",
        "title": "Vivalto Home portal",
        "url": "https://www.vivaltohome.com",
        "publisher": "Vivalto Home",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1741; BE nursing-home network holding",
    },
    {
        "source_id": "src_vivalto_be_foi_contact_1741",
        "title": "Vivalto Home Belgium FOI channel",
        "url": "https://www.vivaltohome.com",
        "publisher": "Vivalto Home Belgium SA",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1741; info@vivaltohome.com; Avenue du Domaine 13 1190 Forest",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_vivalto_be_assets_2025", "2025", "266811008", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB 20/58 assets 266811008; tick1741"),
    ("bud_vivalto_be_fva_2025", "2025", "249209728", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB FVA linked 249209728; tick1741"),
    ("bud_vivalto_be_participations_2025", "2025", "241648314", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB participations 241648314 JUMP vs 177474875; FOI Molenheide/Prinsenhof map; tick1741"),
    ("bud_vivalto_be_creances_liees_2025", "2025", "7561414", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB créances liées 7561414; tick1741"),
    ("bud_vivalto_be_cash_2025", "2025", "310414", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB cash 310414 DROP vs 2915475; tick1741"),
    ("bud_vivalto_be_equity_2025", "2025", "47036939", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB equity 47036939; tick1741"),
    ("bud_vivalto_be_debt_2025", "2025", "219774069", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB dettes 219774069; tick1741"),
    ("bud_vivalto_be_lt_autres_2025", "2025", "145702851", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB LT autres emprunts 145702851 JUMP mainly filiales; FOI; tick1741"),
    ("bud_vivalto_be_obligations_2025", "2025", "23000000", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB emprunts obligataires 23000000; tick1741"),
    ("bud_vivalto_be_st_autres_2025", "2025", "46624517", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB ST autres dettes 46624517; tick1741"),
    ("bud_vivalto_be_opbr_2025", "2025", "9371794", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB ventes/prestations 9371794; tick1741"),
    ("bud_vivalto_be_autres_opbr_2025", "2025", "9214065", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB autres produits 74 9214065; FOI fee split; tick1741"),
    ("bud_vivalto_be_staff_2025", "2025", "736811", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB 62 736811 / VTE 5; tick1741"),
    ("bud_vivalto_be_services_2025", "2025", "2835599", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB services 61 2835599; tick1741"),
    ("bud_vivalto_be_expl_2025", "2025", "4839018", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB bénéfice d'exploitation 9901 4839018; tick1741"),
    ("bud_vivalto_be_fin_fva_opbr_2025", "2025", "4840000", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB produits immobilisations financières 750 4840000; tick1741"),
    ("bud_vivalto_be_pnl_2025", "2025", "4231615", "executed", "src_vivalto_be_nbb_ye2025", "strong", "NBB PnL 9904 4231615 FLIP; AV 22.05.2026; Mazars sans réserve; tick1741"),
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
        "title": "Vivalto Home Belgium YE2025 leftover BE care holding (opbr 9.37m / FVA 249.21m / debt 219.77m)",
        "entity_id": EID,
        "beneficiary": "Molenheide / Prinsenhof / other Vivalto WZC residents via holding",
        "legal_basis": "CSA SA; Woonzorgdecreet cascade via subsidiaries; Bestuursdecreet openbaarheid where applicable",
        "decision_date": "2026-05-22",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "9371794",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00180299.pdf",
        "stated_goal": "Local leftover Vivalto BE holding map — official NBB YE2025 dual Molenheide+Prinsenhof; FOI FVA/debt map",
        "cut_option": "Publish subsidiary book-value matrix (Molenheide/Prinsenhof+); disclose 145.7m LT filial loans + comfort-letter network; explain management-fee 9.21m",
        "source_id": "src_vivalto_be_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>VivaltoHomeBE>JR2025_L5",
        "notes": "tick1741; YE2025 holding; opbr 9.37m pnl +4.23m assets 266.81m equity 47.04m debt 219.77m FVA 249.21m participations 241.65m; dual Molenheide+Prinsenhof; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Vivalto Home Belgium YE2025: opbr 9.37m / FVA 249.21m / debt 219.77m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>VivaltoHomeBE>JR2025_L5",
        "annual_cost_eur": "9371794",
        "total_cost_eur": "249209728",
        "tco_notes": "Leftover Vivalto BE holding YE2025: opbr 9.37m (autres fees 9.21m / omzet empty) / staff 0.74m VTE 5 / pnl +4.23m FLIP; assets 266.81m equity 47.04m debt 219.77m (LT filial 145.70m JUMP + bonds 23m) / FVA 249.21m (participations JUMP 241.65m); Mazars sans réserve; dual Molenheide+Prinsenhof; INAMI/RIZIV filial risk noted",
        "confidence": "strong",
        "source_id": "src_vivalto_be_nbb_ye2025",
        "beneficiaries": "Molenheide / Prinsenhof / other Vivalto WZC residents via holding",
        "stated_goal": "Local leftover Vivalto BE holding map — official NBB YE2025 dual after Prinsenhof residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 9371794 / pnl 4231615 / FVA 249209728 / debt 219774069 / participations 241648314",
        "absurdity_score": "4.8",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "4.9",
        "cut_proposal": "Publish subsidiary FVA matrix + 145.7m LT filial debt map; disclose comfort letters to NEG-equity homes; explain 9.21m intercompany fees vs public RIZIV cascade",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1741; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Prinsenhof+Molenheide+Colisee+Armonea done; Vivalto holding; De Verlosser CDN live unused; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>VivaltoHomeBE>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB C-cap publishes opbr 9371794 / autres 9214065 / staff 736811 VTE 5 / pnl 4231615 / assets 266811008 / debt 219774069 / FVA 249209728 / participations 241648314 / LT filial loans 145702851; subsidiary book-value matrix and comfort-letter network unpublished; AV notulen 22.05.2026",
        "why_it_matters": "Vivalto BE holding controls Molenheide+Prinsenhof public-care cascade via 249m FVA and 146m filial debt while booking 9.2m intercompany fees — need group transparency",
        "priority": "9",
        "recipient_body": "Vivalto Home Belgium SA / Bestuursorgaan",
        "recipient_email": "info@vivaltohome.com",
        "recipient_postal": "Avenue du Domaine 13 1190 Forest",
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
        "notes": "tick1741; human-send only; dual Molenheide+Prinsenhof; AGB/NSZ/Dijk92/APEFE still blocked; De Verlosser CDN 2026-00174957 live unused",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1741":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1741: Vivalto Home Belgium KBO 0820.420.456 NBB YE2025 opbr 9371794 FVA 249209728 debt 219774069; FOI ready gap_vivalto_be_opbr_9_37m_fva_249_21m_debt_219_77m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1742",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1742 after 1741 Vivalto Home Belgium YE2025. Next every-10 is 1750. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC (e.g. De Verlosser CDN 2026-00174957 live).",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1741 VivaltoHomeBE; NEXT AGB/NSZ-if-200/DeVerlosser-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC; next every-10 1750",
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
        "last_unit_id": "rq_1741",
        "ticks_completed": "1741",
        "paused": "no",
        "notes": "tick1741 leftover Vivalto Home Belgium SA residual dual Molenheide+Prinsenhof; KBO 0820.420.456; official NBB C-cap YE2025 deposit 2026-00180299 CDN 200; sourced euros assets 266811008 opbr 9371794 autres 9214065 staff 736811 VTE 5 pnl 4231615 equity 47036939 debt 219774069 lt_filial 145702851 fva 249209728 participations 241648314; Mazars opinion sans reserve; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; De Verlosser CDN 2026-00174957 live unused; NOT every-10 (next 1750); next rq_1742 AGB/NSZ-if-200/DeVerlosser/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")

# tick1764 — Aux Hirondelles SA / Vivalto Embourg
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)
TS = "2026-08-24T15:45:00Z"
DATE = "2026-08-24"

ENTITY = "nv_hirondelles"
SRC_NBB = "src_hirondelles_jr2025_nbb"
SRC_SITE = "src_hirondelles_site"
SRC_KBO = "src_hirondelles_kbo"
COMM = "comm_hirondelles_jr2025_marge_2_88m"
LB = "lb_hirondelles_marge_2_88m_staff_2_36m_autres_creances_1_10m_l5"
GAP = "gap_hirondelles_marge_2_88m_staff_2_36m_autres_creances_lease_l5"
HIER = "Wallonie>Provinces>Liege>Communes>Chaudfontaine>Embourg>MRPA>AuxHirondelles>JR2025_L5"


def append_rows(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    id_key = fieldnames[0]
    ids = {row[id_key] for row in existing}
    added = 0
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in existing:
            w.writerow(row)
        for row in rows:
            if row[id_key] in ids:
                continue
            w.writerow({k: row.get(k, "") for k in fieldnames})
            added += 1
            ids.add(row[id_key])
    return added


sources = [
    {
        "source_id": SRC_NBB,
        "title": "Aux Hirondelles SA NBB A-cap YE2025 deposit 2026-00136826",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00136826.pdf",
        "publisher": "Nationale Bank van België / Aux Hirondelles SA",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1764; AV 08.05.2026; A-cap abbrev; Vivalto Home Belgium admin delegue; Forvis Mazars/Collie opinion sans reserve; Embourg Voie de l Ardenne 79",
    },
    {
        "source_id": SRC_SITE,
        "title": "Vivalto Home — Aux hirondelles maisons",
        "url": "https://www.vivaltohome.com/nl/maisons/aux-hirondelles/",
        "publisher": "Vivalto Home",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1764; Voie de l Ardenne 77-79 4053 Embourg; christel.hubert@vivaltohome.com; rusthuis 30 + WZC 35",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Aux Hirondelles SA 0473.658.423",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0473658423",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1764; SA/NV; Voie de l Ardenne 79 4053 Embourg; RPR Liege",
    },
]
print("sources", append_rows(DATA / "sources.csv", sources))

entities = [
    {
        "entity_id": ENTITY,
        "name_nl": "Aux Hirondelles SA (leftover Vivalto WZC dual / Embourg Chaudfontaine)",
        "name_fr": "Aux Hirondelles SA (WZC Vivalto résiduel / Embourg)",
        "name_en": "Aux Hirondelles SA leftover Vivalto nursing-home dual Embourg",
        "level": "other",
        "parent_id": "nv_vivalto_home_be",
        "community_language": "fr",
        "website": "https://www.vivaltohome.com/nl/maisons/aux-hirondelles/",
        "foi_email": "christel.hubert@vivaltohome.com",
        "foi_postal": "Voie de l'Ardenne 79 4053 Embourg",
        "notes": "tick1764 leftover Vivalto WZC dual Embourg after Pic-au-Vent; KBO 0473.658.423 Actief; SA; official NBB A-cap YE2025 deposit 2026-00136826 CDN 200; AV 08.05.2026; mère Vivalto Home Belgium admin délégué; commissaire Forvis Mazars/Collie opinion sans réserve; cautionnement ENPH pour Vivalto Home Belgium 205070; sourced euros assets 4094030 equity 1740546 debt 1979424 leasing LT 1058069 autres creances 1103015 FVA 500000 marge 2878361 staff 2364737 VTE 40.7 expl 296170 pnl 215131 admin 105888; FOI ready RIZIV/CA/autres creances/leasing/caution",
    },
]
print("entities", append_rows(DATA / "entities.csv", entities))

budgets = [
    {"budget_id": "bud_hirondelles_assets_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "4094030", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Assets YE2025 4094030 DROP vs 4530090; tick1764"},
    {"budget_id": "bud_hirondelles_equity_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "1740546", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Equity 1740546 UP vs 1636050; tick1764"},
    {"budget_id": "bud_hirondelles_debt_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "1979424", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Debt 1979424 DROP vs 2494015; tick1764"},
    {"budget_id": "bud_hirondelles_leasing_lt_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "1058069", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "LT credit/leasing 1058069; tick1764"},
    {"budget_id": "bud_hirondelles_autres_creances_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "1103015", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Autres creances ST 1103015; tick1764"},
    {"budget_id": "bud_hirondelles_fva_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "500000", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Immobilisations financieres 500000; tick1764"},
    {"budget_id": "bud_hirondelles_marge_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "2878361", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Marge brute 2878361 (A-cap; CA not disclosed); tick1764"},
    {"budget_id": "bud_hirondelles_staff_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "2364737", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Staff 2364737 / VTE 40.7; tick1764"},
    {"budget_id": "bud_hirondelles_expl_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "296170", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Benefice exploitation 296170 DROP vs 339261; tick1764"},
    {"budget_id": "bud_hirondelles_pnl_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "215131", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "PnL 215131 (a affecter 293026); tick1764"},
    {"budget_id": "bud_hirondelles_admin_remun_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "105888", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Benefice distribue administrateurs/gerants 105888; tick1764"},
    {"budget_id": "bud_hirondelles_caution_enph_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "205070", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Cautionnement ENPH en faveur de Vivalto Home Belgium SA 205070 off-balance; tick1764"},
]
print("budgets", append_rows(DATA / "budgets.csv", budgets))

commitments = [
    {
        "commitment_id": COMM,
        "title": "Aux Hirondelles SA JR2025 leftover Vivalto dual (marge 2.88m / staff 2.36m / autres creances 1.10m)",
        "entity_id": ENTITY,
        "beneficiary": "Aux Hirondelles SA / Vivalto Home Belgium / residents Embourg",
        "legal_basis": "CSA SA; decret wallon openbaarheid analog for dual care euros",
        "decision_date": "2026-05-08",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "2878361",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00136826.pdf",
        "stated_goal": "Local leftover Vivalto WZC map WAL Embourg — marge 2.88m / staff 2.36m / autres creances opacity",
        "cut_option": "Publish full CA/RIZIV split + autres creances 1.10m counterparties + leasing + ENPH caution terms; unit-cost per bed",
        "source_id": SRC_NBB,
        "confidence": "strong",
        "hierarchy_path": HIER,
        "notes": "tick1764; assets 4094030 equity 1740546 debt 1979424 leasing LT 1058069 autres creances 1103015 FVA 500000 marge 2878361 staff 2364737 VTE 40.7 expl 296170 pnl 215131 admin 105888 caution ENPH 205070; FOI ready not sent; not TE-additive; A-cap CA undisclosed; Brembloem still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403",
    },
]
print("commitments", append_rows(DATA / "commitments.csv", commitments))

leaderboard = [
    {
        "item_id": LB,
        "name": "Aux Hirondelles SA 2025: marge 2.88m / staff 2.36m (autres creances 1.10m + ENPH caution)",
        "level": "L5",
        "type": "nursing_home_private_dual",
        "hierarchy_path": "Wallonie>Provinces>Liege>Communes>Chaudfontaine>Embourg>MRPA>AuxHirondelles",
        "annual_cost_eur": "2878361",
        "total_cost_eur": "2878361",
        "tco_notes": "Envelope=marge bruto 2878361 (A-cap; CA undisclosed); staff 2.36m; autres creances 1.10m; leasing LT 1.06m; ENPH caution 0.21m for parent; admin remun 106k",
        "confidence": "strong",
        "source_id": SRC_NBB,
        "beneficiaries": "MRPA/WZC residents Embourg / Vivalto group",
        "stated_goal": "Nursing-home care (MRPA/MRS)",
        "measured_outcome": "PnL +215k; expl +296k DROP; CA hidden in A-cap; large related-ish autres creances; parent ENPH caution",
        "absurdity_score": "5.4",
        "cost_score": "5.2",
        "difficulty": "5",
        "priority_index": "5.7",
        "cut_proposal": "Publish full CA/RIZIV; disclose autres creances + leasing + ENPH caution; unit-cost",
        "status": "listed",
        "struck_reason": "",
        "notes": f"tick1764; FOI {GAP}",
    },
]
print("leaderboard", append_rows(DATA / "leaderboard.csv", leaderboard))

foi = [
    {
        "gap_id": GAP,
        "hierarchy_path": HIER,
        "entity_id": ENTITY,
        "what_is_missing": "NBB A-cap YE2025 live marge 2878361 but CA undisclosed; need full CA/RIZIV/residentie split; autres creances ST 1103015 counterparties; leasing LT 1058069 terms; FVA 500000 nature; cautionnement ENPH 205070 for Vivalto Home Belgium; admin remun 105888 breakdown",
        "why_it_matters": "Vivalto dual Embourg with abbreviated schema hiding CA + large autres creances and parent ENPH caution — opacity on public RIZIV share",
        "priority": "8",
        "recipient_body": "Aux Hirondelles SA / Vivalto Home Belgium SA",
        "recipient_email": "christel.hubert@vivaltohome.com",
        "recipient_postal": "Voie de l'Ardenne 79 4053 Embourg",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": TS,
        "updated_utc": TS,
        "notes": "tick1764; human-send only; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; VBWest verdaged; Joie et Sante CDN live for later",
    },
]
print("foi_queue", append_rows(DATA / "foi_queue.csv", foi))

rq_path = DATA / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found_1764 = False
found_1765 = False
for row in rows:
    if row["task_id"] == "rq_1764":
        found_1764 = True
        row["title"] = "Aux Hirondelles SA JR2025 leftover Vivalto dual residual"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = TS
        row["notes"] = (
            "DONE tick1764: Aux Hirondelles SA KBO 0473.658.423 NBB YE2025 marge 2878361 staff 2364737 "
            "VTE 40.7 autres creances 1103015 pnl 215131; "
            f"FOI ready {GAP}; NOT every-10 (next 1770)"
        )
    if row["task_id"] == "rq_1765":
        found_1765 = True

if not found_1765:
    rows.append(
        {
            "task_id": "rq_1765",
            "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Tick 1765 after 1764 Aux Hirondelles. Next every-10 is 1770. Prefer leftover AGB/APB if PDF live "
                "(Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, ABS/POV/BVAS, "
                "Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 (Joie et Sante 2026-00176215 live), "
                "other IOED/HVZ (VBWest if JR euros live) if official JR2025 euros live, other IGS/WZC. "
                "Do NOT redo AuxHirondelles/PicAuVent/Gerosin/Vesper continuum."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1764 Aux Hirondelles; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Dijk92/APEFE/HVZ-VBWest/JoieSante; next every-10 1770",
        }
    )

with rq_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, "") for k in fieldnames})
print("research_queue 1764 done", found_1764, "1765 spawned", not found_1765)

ls_path = DATA / "loop_state.csv"
with ls_path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
for row in ls_rows:
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = TS
    row["last_unit_id"] = "rq_1764"
    row["ticks_completed"] = "1764"
    row["paused"] = "no"
    row["notes"] = (
        "tick1764 leftover Aux Hirondelles Embourg; KBO 0473.658.423; NBB YE2025 marge 2878361 staff 2364737 "
        "VTE 40.7 autres creances 1103015 leasing LT 1058069 pnl 215131 admin 105888 caution ENPH 205070; "
        "FOI RIZIV/CA/autres creances/leasing; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; "
        "VBWest verdaged; JoieSante CDN live for later; NOT every-10 (next 1770); next rq_1765 "
        "AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/HVZ-VBWest/JoieSante; continuous hole_fill"
    )
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for row in ls_rows:
        w.writerow({k: row.get(k, "") for k in ls_fields})
print("loop_state -> 1764")
print("OK")

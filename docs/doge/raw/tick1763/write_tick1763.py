# tick1763 — La Residence Le Pic-au-Vent SA / Vivalto Tournai
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)
TS = "2026-08-24T15:15:00Z"
DATE = "2026-08-24"

ENTITY = "nv_picauvent"
SRC_NBB = "src_picauvent_jr2025_nbb"
SRC_SITE = "src_picauvent_site"
SRC_KBO = "src_picauvent_kbo"
COMM = "comm_picauvent_jr2025_marge_3_19m"
LB = "lb_picauvent_marge_3_19m_staff_2_38m_accruals_3_73m_l5"
GAP = "gap_picauvent_marge_3_19m_staff_2_38m_accruals_lease_l5"
HIER = "Wallonie>Provinces>Hainaut>Communes>Tournai>MRPA>PicAuVent>JR2025_L5"


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
        "title": "La Residence Le Pic-au-Vent SA NBB A-cap YE2025 deposit 2026-00139188",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139188.pdf",
        "publisher": "Nationale Bank van België / La Residence Le Pic-au-Vent SA",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1763; AV 13.05.2026; A-cap abbrev; Vivalto Home Belgium admin delegue; Forvis Mazars/Collie opinion sans reserve; Tournai Le Moulin 65",
    },
    {
        "source_id": SRC_SITE,
        "title": "Vivalto Home — Pic au Vent maisons",
        "url": "https://www.vivaltohome.com/nl/maisons/pic-au-vent/",
        "publisher": "Vivalto Home",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1763; Rue le Moulin 65 7500 Tournai; sophie.fockedey@vivaltohome.com; rusthuis 15 + WZC 45 + AW 21",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO La Residence Le Pic-au-Vent SA 0447.178.314",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0447178314",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1763; SA/NV; Le Moulin 65 7500 Tournai; RPR Hainaut div Tournai",
    },
]
print("sources", append_rows(DATA / "sources.csv", sources))

entities = [
    {
        "entity_id": ENTITY,
        "name_nl": "La Résidence Le Pic-au-Vent SA (leftover Vivalto WZC dual / Tournai)",
        "name_fr": "La Résidence Le Pic-au-Vent SA (WZC Vivalto résiduel / Tournai)",
        "name_en": "La Residence Le Pic-au-Vent SA leftover Vivalto nursing-home dual Tournai",
        "level": "other",
        "parent_id": "nv_vivalto_home_be",
        "community_language": "fr",
        "website": "https://www.vivaltohome.com/nl/maisons/pic-au-vent/",
        "foi_email": "sophie.fockedey@vivaltohome.com",
        "foi_postal": "Le Moulin 65 7500 Tournai",
        "notes": "tick1763 leftover Vivalto WZC dual Tournai after Gerosin; KBO 0447.178.314 Actief; SA; official NBB A-cap YE2025 deposit 2026-00139188 CDN 200; AV 13.05.2026; mère Vivalto Home Belgium admin délégué; commissaire Forvis Mazars/Collie opinion sans réserve; FVA 6138000 = 12.5pct VIVALTO LEASE; sourced euros assets 11817671 equity 1310749 debt 10506922 leasing/credit LT 5321223 accruals liab 3729795 marge brute 3192580 staff 2382825 VTE 39.6 expl 471102 pnl 235682 admin remun 84248; FOI ready RIZIV/CA/accruals/leasing",
    },
]
print("entities", append_rows(DATA / "entities.csv", entities))

budgets = [
    {"budget_id": "bud_picauvent_assets_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "11817671", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Assets YE2025 11817671; tick1763"},
    {"budget_id": "bud_picauvent_equity_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "1310749", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Equity 1310749 UP vs 1159316; tick1763"},
    {"budget_id": "bud_picauvent_debt_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "10506922", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Debt 10506922; tick1763"},
    {"budget_id": "bud_picauvent_leasing_lt_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "5321223", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "LT credit/leasing 5321223; tick1763"},
    {"budget_id": "bud_picauvent_fva_vivalto_lease_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "6138000", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "FVA 6138000 = 12.5pct VIVALTO LEASE KBO 0672.832.481; tick1763"},
    {"budget_id": "bud_picauvent_accruals_liab_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "3729795", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Comptes de regularisation passif 3729795; tick1763"},
    {"budget_id": "bud_picauvent_marge_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "3192580", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Marge brute 3192580 (A-cap; CA not disclosed); tick1763"},
    {"budget_id": "bud_picauvent_staff_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "2382825", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Staff 2382825 / VTE 39.6; tick1763"},
    {"budget_id": "bud_picauvent_expl_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "471102", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Benefice exploitation 471102; tick1763"},
    {"budget_id": "bud_picauvent_pnl_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "235682", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "PnL 235682; tick1763"},
    {"budget_id": "bud_picauvent_admin_remun_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "84248", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Benefice distribue administrateurs/gerants 84248 UP vs 66169; tick1763"},
    {"budget_id": "bud_picauvent_nrec_prod_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "190280", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Produits exploitation non recurrents 190280 (same as prior year); tick1763"},
]
print("budgets", append_rows(DATA / "budgets.csv", budgets))

commitments = [
    {
        "commitment_id": COMM,
        "title": "Pic-au-Vent SA JR2025 leftover Vivalto dual (marge 3.19m / staff 2.38m / accruals 3.73m / VIVALTO LEASE stake)",
        "entity_id": ENTITY,
        "beneficiary": "La Residence Le Pic-au-Vent SA / Vivalto Home Belgium / residents Tournai",
        "legal_basis": "CSA SA; decret wallon openbaarheid analog for dual care euros",
        "decision_date": "2026-05-13",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "3192580",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139188.pdf",
        "stated_goal": "Local leftover Vivalto WZC map WAL Tournai — marge 3.19m / staff 2.38m / accruals opacity",
        "cut_option": "Publish full CA/RIZIV split + accruals 3.73m composition + leasing terms + VIVALTO LEASE stake rationale; unit-cost per bed",
        "source_id": SRC_NBB,
        "confidence": "strong",
        "hierarchy_path": HIER,
        "notes": "tick1763; assets 11817671 equity 1310749 debt 10506922 leasing LT 5321223 FVA VIVALTO LEASE 6138000 accruals 3729795 marge 3192580 staff 2382825 VTE 39.6 expl 471102 pnl 235682 admin 84248; FOI ready not sent; not TE-additive; A-cap CA undisclosed; Brembloem still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403",
    },
]
print("commitments", append_rows(DATA / "commitments.csv", commitments))

leaderboard = [
    {
        "item_id": LB,
        "name": "Pic-au-Vent SA 2025: marge 3.19m / staff 2.38m (accruals 3.73m + VIVALTO LEASE 6.14m)",
        "level": "L5",
        "type": "nursing_home_private_dual",
        "hierarchy_path": "Wallonie>Provinces>Hainaut>Communes>Tournai>MRPA>PicAuVent",
        "annual_cost_eur": "3192580",
        "total_cost_eur": "3192580",
        "tco_notes": "Envelope=marge bruto 3192580 (A-cap; CA undisclosed); staff 2.38m; accruals liab 3.73m; FVA VIVALTO LEASE 6.14m; leasing LT 5.32m; admin remun 84k",
        "confidence": "strong",
        "source_id": SRC_NBB,
        "beneficiaries": "MRPA/WZC residents Tournai / Vivalto group",
        "stated_goal": "Nursing-home care (MRPA/MRS)",
        "measured_outcome": "PnL +236k; expl +471k; CA hidden in A-cap; large accruals + intra-group lease stake; admin remun UP",
        "absurdity_score": "5.5",
        "cost_score": "5.3",
        "difficulty": "5",
        "priority_index": "5.8",
        "cut_proposal": "Publish full CA/RIZIV; disclose accruals + leasing + VIVALTO LEASE stake; unit-cost",
        "status": "listed",
        "struck_reason": "",
        "notes": f"tick1763; FOI {GAP}",
    },
]
print("leaderboard", append_rows(DATA / "leaderboard.csv", leaderboard))

foi = [
    {
        "gap_id": GAP,
        "hierarchy_path": HIER,
        "entity_id": ENTITY,
        "what_is_missing": "NBB A-cap YE2025 live marge 3192580 but CA undisclosed; need full CA/RIZIV/residentie split; comptes regularisation passif 3729795 composition; leasing LT 5321223 terms; VIVALTO LEASE 12.5pct stake rationale; admin remun 84248 breakdown; nrec produits 190280 nature",
        "why_it_matters": "Vivalto dual Tournai with abbreviated schema hiding CA + large accruals and intra-group lease stake — opacity on public RIZIV share",
        "priority": "8",
        "recipient_body": "La Residence Le Pic-au-Vent SA / Vivalto Home Belgium SA",
        "recipient_email": "sophie.fockedey@vivaltohome.com",
        "recipient_postal": "Le Moulin 65 7500 Tournai",
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
        "notes": "tick1763; human-send only; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; VBWest verdaged; Aux Hirondelles / Joie et Sante also live CDN for later",
    },
]
print("foi_queue", append_rows(DATA / "foi_queue.csv", foi))

rq_path = DATA / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found_1763 = False
found_1764 = False
for row in rows:
    if row["task_id"] == "rq_1763":
        found_1763 = True
        row["title"] = "Pic-au-Vent SA JR2025 leftover Vivalto dual residual"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = TS
        row["notes"] = (
            "DONE tick1763: Pic-au-Vent SA KBO 0447.178.314 NBB YE2025 marge 3192580 staff 2382825 "
            "VTE 39.6 accruals 3729795 FVA VIVALTO LEASE 6138000 pnl 235682; "
            f"FOI ready {GAP}; NOT every-10 (next 1770)"
        )
    if row["task_id"] == "rq_1764":
        found_1764 = True

if not found_1764:
    rows.append(
        {
            "task_id": "rq_1764",
            "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Tick 1764 after 1763 Pic-au-Vent. Next every-10 is 1770. Prefer leftover AGB/APB if PDF live "
                "(Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, ABS/POV/BVAS, "
                "Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 (Aux Hirondelles 2026-00136826 / "
                "Joie et Sante 2026-00176215 live), other IOED/HVZ (VBWest if JR euros live) if official JR2025 "
                "euros live, other IGS/WZC. Do NOT redo PicAuVent/Gerosin/Vesper continuum."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1763 Pic-au-Vent; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Dijk92/APEFE/HVZ-VBWest/AuxHirondelles/JoieSante; next every-10 1770",
        }
    )

with rq_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, "") for k in fieldnames})
print("research_queue 1763 done", found_1763, "1764 spawned", not found_1764)

ls_path = DATA / "loop_state.csv"
with ls_path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
for row in ls_rows:
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = TS
    row["last_unit_id"] = "rq_1763"
    row["ticks_completed"] = "1763"
    row["paused"] = "no"
    row["notes"] = (
        "tick1763 leftover Pic-au-Vent Tournai; KBO 0447.178.314; NBB YE2025 marge 3192580 staff 2382825 "
        "VTE 39.6 accruals 3729795 FVA VIVALTO LEASE 6138000 pnl 235682 admin 84248; FOI RIZIV/CA/accruals/leasing; "
        "Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; VBWest verdaged; "
        "AuxHirondelles/JoieSante CDN live for later; NOT every-10 (next 1770); next rq_1764 "
        "AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/HVZ-VBWest/AuxHirondelles; continuous hole_fill"
    )
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for row in ls_rows:
        w.writerow({k: row.get(k, "") for k in ls_fields})
print("loop_state -> 1763")
print("OK")

# tick1762 — Gerosin NV / WZC E. Carpentier Kuurne (Vivalto leftover)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)
TS = "2026-08-24T14:45:00Z"
DATE = "2026-08-24"

ENTITY = "nv_gerosin"
SRC_NBB = "src_gerosin_jr2025_nbb"
SRC_SITE = "src_gerosin_site"
SRC_KBO = "src_gerosin_kbo"
COMM = "comm_gerosin_jr2025_opbr_4_49m"
LB = "lb_gerosin_opbr_4_49m_staff_3_02m_op_loss_nrec_l5"
GAP = "gap_gerosin_omzet_4_33m_staff_3_02m_related_recv_5m_nrec_l5"
HIER = "Vlaanderen>Provincies>West-Vlaanderen>Gemeenten>Kuurne>WZC>Gerosin>JR2025_L5"


def append_rows(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    ids = set()
    id_key = fieldnames[0]
    for row in existing:
        ids.add(row[id_key])
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


# --- sources ---
sources = [
    {
        "source_id": SRC_NBB,
        "title": "Gerosin NV NBB VOL-kap YE2025 deposit 2026-00139189",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139189.pdf",
        "publisher": "Nationale Bank van België / Gerosin NV",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1762; AV 13.05.2026; VOL-kap; Vivalto Home Belgium gedelegeerd bestuurder; Forvis Mazars/Collie oordeel zonder voorbehoud; Kuurne Doornenstraat 12",
    },
    {
        "source_id": SRC_SITE,
        "title": "Vivalto Home — E. Carpentier / Gerosin maisons",
        "url": "https://www.vivaltohome.com/nl/maisons/e-carpentier/",
        "publisher": "Vivalto Home",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1762; Doornenstraat 12 8520 Kuurne; gerosin.info@vivaltohome.com; WZC 35 + rusthuis 6 + KV 7 + AW 29",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Gerosin NV 0423.518.727",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0423518727",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1762; NV; Doornenstraat 12 8520 Kuurne; RPR Gent afd Kortrijk",
    },
]
print("sources", append_rows(DATA / "sources.csv", sources))

# --- entity ---
entities = [
    {
        "entity_id": ENTITY,
        "name_nl": "Gerosin NV (leftover Vivalto WZC dual / E. Carpentier Kuurne)",
        "name_fr": "Gerosin NV (WZC Vivalto residuel / E. Carpentier Courtrai-Kuurne)",
        "name_en": "Gerosin NV leftover Vivalto nursing-home dual E. Carpentier Kuurne",
        "level": "other",
        "parent_id": "nv_vivalto_home_be",
        "community_language": "nl",
        "website": "https://www.vivaltohome.com/nl/maisons/e-carpentier/",
        "foi_email": "gerosin.info@vivaltohome.com",
        "foi_postal": "Doornenstraat 12 8520 Kuurne",
        "notes": "tick1762 leftover Vivalto WZC dual Kuurne after Vesper; KBO 0423.518.727 Actief; NV; official NBB VOL-kap YE2025 deposit 2026-00139189 CDN 200; AV 13.05.2026; moeder Vivalto Home Belgium gedelegeerd bestuurder; commissaris Forvis Mazars/Collie oordeel zonder voorbehoud; sourced euros assets 11155241 equity 3443408 debt 6929117 leasing LT 4987859 related recv FVA 5000000 bedrijfsopbr 4492711 omzet 4333526 staff 3015082 VTE 47.3 bedrijfsverlies -932925 nrec afschr 1200000 nrec fin gain FVA 3272868 pnl 2007840; FOI ready RIZIV/related recv/leasing/nrec",
    },
]
print("entities", append_rows(DATA / "entities.csv", entities))

# --- budgets ---
budgets = [
    {"budget_id": "bud_gerosin_assets_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "11155241", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Assets YE2025 11155241 DROP vs 15802119; tick1762"},
    {"budget_id": "bud_gerosin_equity_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "3443408", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Equity 3443408 UP vs 1435568; tick1762"},
    {"budget_id": "bud_gerosin_debt_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "6929117", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Debt 6929117 DROP vs 13544851; tick1762"},
    {"budget_id": "bud_gerosin_leasing_lt_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "4987859", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "LT leasing 4987859; tick1762"},
    {"budget_id": "bud_gerosin_related_recv_fva_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "5000000", "amount_min_eur": "", "amount_max_eur": "", "basis": "stock", "source_id": SRC_NBB, "confidence": "strong", "notes": "Related FVA vorderingen 5000000 (deelnemingen prior 8844477 cleared); tick1762"},
    {"budget_id": "bud_gerosin_opbr_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "4492711", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Bedrijfsopbrengsten 4492711; tick1762"},
    {"budget_id": "bud_gerosin_omzet_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "4333526", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Omzet 4333526; tick1762"},
    {"budget_id": "bud_gerosin_staff_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "3015082", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Staff 3015082 / VTE 47.3; tick1762"},
    {"budget_id": "bud_gerosin_op_loss_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "-932925", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Bedrijfsverlies FLIP -932925 vs +88466; nrec afschr 1200000; tick1762"},
    {"budget_id": "bud_gerosin_nrec_afschr_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "1200000", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Niet-recurrente afschrijvingen/WV MVA 1200000; tick1762"},
    {"budget_id": "bud_gerosin_nrec_fin_gain_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "3272868", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Meerwaarden realisatie FVA 3272868; tick1762"},
    {"budget_id": "bud_gerosin_pnl_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "2007840", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "PnL 2007840 (te bestemmen 2124792); tick1762"},
    {"budget_id": "bud_gerosin_subsidies_2025", "entity_id": ENTITY, "year": "2025", "amount_eur": "12746", "amount_min_eur": "", "amount_max_eur": "", "basis": "realized", "source_id": SRC_NBB, "confidence": "strong", "notes": "Exploitatiesubsidies code 740 = 12746; tick1762"},
]
print("budgets", append_rows(DATA / "budgets.csv", budgets))

# --- commitment ---
commitments = [
    {
        "commitment_id": COMM,
        "title": "Gerosin NV JR2025 leftover Vivalto dual (opbr 4.49m / omzet 4.33m / staff 3.02m / op-loss + nrec FVA gain)",
        "entity_id": ENTITY,
        "beneficiary": "Gerosin NV / Vivalto Home Belgium / residents Kuurne E. Carpentier",
        "legal_basis": "WVV NV; CSA Art 3:6; Vlaams openbaarheidsdecreet analog for dual care euros",
        "decision_date": "2026-05-13",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "4492711",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00139189.pdf",
        "stated_goal": "Local leftover Vivalto WZC map VL Kuurne — opbr 4.49m / staff 3.02m / op-loss + nrec FVA gain",
        "cut_option": "Publish RIZIV/omzet split + related recv 5m counterparties + leasing LT terms + nrec 1.2m/3.27m toelichting; unit-cost per bed",
        "source_id": SRC_NBB,
        "confidence": "strong",
        "hierarchy_path": HIER,
        "notes": "tick1762; assets 11155241 equity 3443408 debt 6929117 leasing LT 4987859 related recv 5000000 opbr 4492711 omzet 4333526 staff 3015082 VTE 47.3 op_loss -932925 nrec_afschr 1200000 nrec_fin 3272868 pnl 2007840; FOI ready not sent; not TE-additive; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403",
    },
]
print("commitments", append_rows(DATA / "commitments.csv", commitments))

# --- leaderboard ---
leaderboard = [
    {
        "item_id": LB,
        "name": "Gerosin NV 2025: opbr 4.49m / staff 3.02m (op-loss -0.93m + nrec FVA gain 3.27m)",
        "level": "L5",
        "type": "nursing_home_private_dual",
        "hierarchy_path": "Vlaanderen>Provincies>West-Vlaanderen>Gemeenten>Kuurne>WZC>Gerosin",
        "annual_cost_eur": "4492711",
        "total_cost_eur": "4492711",
        "tco_notes": "Envelope=bedrijfsopbr 4492711; omzet 4333526; staff 3.02m; leasing LT 4.99m; related recv 5m; op-loss -933k after nrec afschr 1.2m; nrec FVA gain 3.27m papers over to pnl +2.01m",
        "confidence": "strong",
        "source_id": SRC_NBB,
        "beneficiaries": "WZC residents Kuurne E. Carpentier / Vivalto group",
        "stated_goal": "Nursing-home care (WZC/MRPA)",
        "measured_outcome": "Op-loss FLIP -933k vs +88k; one-off FVA meerwaarde 3.27m; related FVA recv still 5m; ST other debt DROP 7.1m->0.80m",
        "absurdity_score": "5.6",
        "cost_score": "5.4",
        "difficulty": "5",
        "priority_index": "5.9",
        "cut_proposal": "Publish RIZIV split; disclose related recv/leasing/nrec counterparties; unit-cost",
        "status": "listed",
        "struck_reason": "",
        "notes": f"tick1762; FOI {GAP}",
    },
]
print("leaderboard", append_rows(DATA / "leaderboard.csv", leaderboard))

# --- foi_queue ---
foi = [
    {
        "gap_id": GAP,
        "hierarchy_path": HIER,
        "entity_id": ENTITY,
        "what_is_missing": "NBB VOL-kap YE2025 live omzet 4333526; need RIZIV/residentie split; related FVA vorderingen 5000000 counterparties; leasing LT 4987859 terms; nrec afschr 1200000 + FVA meerwaarde 3272868 toelichting; exploitatiesubsidies 12746",
        "why_it_matters": "Vivalto dual Kuurne with op-loss papered by one-off FVA gain — opacity on public RIZIV share and related-party 5m recv",
        "priority": "8",
        "recipient_body": "Gerosin NV / Vivalto Home Belgium NV",
        "recipient_email": "gerosin.info@vivaltohome.com",
        "recipient_postal": "Doornenstraat 12 8520 Kuurne",
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
        "notes": "tick1762; human-send only; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; VBWest verdaged",
    },
]
print("foi_queue", append_rows(DATA / "foi_queue.csv", foi))

# --- research_queue: mark 1762 done + spawn 1763 ---
rq_path = DATA / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found_1762 = False
found_1763 = False
for row in rows:
    if row["task_id"] == "rq_1762":
        found_1762 = True
        row["title"] = "Gerosin NV JR2025 leftover Vivalto dual residual"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = TS
        row["notes"] = (
            "DONE tick1762: Gerosin NV KBO 0423.518.727 NBB YE2025 opbr 4492711 omzet 4333526 "
            "staff 3015082 VTE 47.3 op_loss -932925 nrec_afschr 1200000 nrec_fin 3272868 pnl 2007840; "
            f"FOI ready {GAP}; NOT every-10 (next 1770)"
        )
        row["instructions"] = (
            "Tick 1762 after 1761 Vesper. Next every-10 is 1770. Prefer leftover AGB/APB if PDF live "
            "(Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, ABS/POV/BVAS, "
            "Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200, other IOED/HVZ (VBWest if JR euros live) "
            "if official JR2025 euros live, other IGS/WZC. Do NOT redo Vesper continuum."
        )
    if row["task_id"] == "rq_1763":
        found_1763 = True

if not found_1763:
    rows.append(
        {
            "task_id": "rq_1763",
            "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Tick 1763 after 1762 Gerosin. Next every-10 is 1770. Prefer leftover AGB/APB if PDF live "
                "(Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, ABS/POV/BVAS, "
                "Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200, other IOED/HVZ (VBWest if JR euros live) "
                "if official JR2025 euros live, other IGS/WZC. Do NOT redo Gerosin/Vesper/Klavertje4/DeMolen/Felicite/Vivalys/BZA continuum."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1762 Gerosin; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Dijk92/APEFE/HVZ-VBWest/other-Vivalto; next every-10 1770",
        }
    )

with rq_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, "") for k in fieldnames})
print("research_queue 1762 done", found_1762, "1763 spawned", not found_1763)

# --- loop_state ---
ls_path = DATA / "loop_state.csv"
with ls_path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    ls_fields = r.fieldnames
    ls_rows = list(r)
for row in ls_rows:
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = TS
    row["last_unit_id"] = "rq_1762"
    row["ticks_completed"] = "1762"
    row["paused"] = "no"
    row["notes"] = (
        "tick1762 leftover Gerosin/E.Carpentier Kuurne; KBO 0423.518.727; NBB YE2025 opbr 4492711 omzet 4333526 "
        "staff 3015082 VTE 47.3 op_loss -932925 nrec_afschr 1200000 nrec_fin 3272868 pnl 2007840 related_recv 5m; "
        "FOI RIZIV/related/leasing/nrec; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE 403; "
        "VBWest verdaged; NOT every-10 (next 1770); next rq_1763 AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/HVZ-VBWest; "
        "continuous hole_fill"
    )
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for row in ls_rows:
        w.writerow({k: row.get(k, "") for k in ls_fields})
print("loop_state -> 1762")
print("OK")

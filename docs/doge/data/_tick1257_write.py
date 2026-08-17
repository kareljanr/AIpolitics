# -*- coding: utf-8 -*-
"""Tick 1257 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 IVA Historische Huizen Gent last JR2025 city organogram (no separate Entity II BBC)."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T07:45:00Z"
TICK = 1257
SRC = "src_iva_hhg_jr2025_city"
SRC2 = "src_iva_hhg_inkanteling_2025_gr00968"
ENT = "iva_historische_huizen_gent"
CITY = "city_gent"
SRC_URL = "https://stad.gent/sites/default/files/media/documents/Jaarrekening%202025%20Toelichting.pdf"
SRC2_URL = "https://ebesluitvorming.gent.be/zittingen/25.0410.8084.0653/agendapunten/25.1017.6729.4399"
GAP = "gap_iva_hhg_expl_7_05m_net_0_61m_extra_comptabel_inkanteling_l5"
HIER = "Vlaanderen>Gemeenten>Gent>IVA_Historische_Huizen"


def append_rows(path, new_rows):
    """Append dict rows using existing header; do not rewrite the file."""
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing_ids = set()
        id_key = fields[0]
        for row in reader:
            existing_ids.add(row.get(id_key))
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(id_key) in existing_ids:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added


def patch_entity_notes(path, entity_id, extra):
    tmp = path.with_suffix(".csv.tmp")
    found = False
    with path.open(encoding="utf-8", newline="") as fin, tmp.open("w", encoding="utf-8", newline="") as fout:
        r = csv.DictReader(fin)
        fields = r.fieldnames
        w = csv.DictWriter(fout, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in r:
            if row.get("entity_id") == entity_id:
                found = True
                notes = row.get("notes") or ""
                if extra not in notes:
                    row["notes"] = (notes + "; " + extra).strip("; ")
            w.writerow(row)
    tmp.replace(path)
    return found


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad Gent JR2025 Toelichting (294p) IVA Historische Huizen organogram last year",
            "url": SRC_URL,
            "publisher": "Stad Gent",
            "accessed_date": "2026-08-17",
            "source_class": "primary_pdf",
            "notes": (
                "tick1257; GR 2026_GR_00503 22.06.2026; Toelichting p.13 organogram IVA HH "
                "net +605959 expl +720315 / 6325610 / 7045925 invest -114357; "
                "no separate Entity II BBC (IVA inside city); inkanteling 1.1.2026 AGB K&E"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2025_GR_00968 externe verzelfstandiging IVA Historische Huizen in AGB Kunsten en Erfgoed",
            "url": SRC2_URL,
            "publisher": "Stad Gent gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1257; GR 24.11.2025; activa om niet; shop voorraad ten bezwarende titel + "
                "compenserende subsidie; extra-comptabel 26-70/90-12/21-85/17-81/PGE 30-27"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "IVA Historische Huizen Gent",
            "name_fr": "AIA Maisons historiques Gand",
            "name_en": "IVA Historic Houses Ghent (internal agency, no own KBO)",
            "level": "municipal_agency",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://historischehuizen.stad.gent",
            "foi_email": "infopunt@stad.gent",
            "foi_postal": "Botermarkt 1 9000 Gent",
            "notes": (
                "tick1257; last JR2025 as city organogram line (no Entity II BBC/KBO); "
                "Gravensteen/Belfort/SPA/SBA/stadspaleizen/Stadhuis; inkanteling 1.1.2026 "
                f"AGB Kunsten en Erfgoed Gent; FOI {GAP}"
            ),
        }
    ],
)
print("entities", n)

ok = patch_entity_notes(
    DATA / "entities.csv",
    CITY,
    "IVA Historische Huizen last JR2025 dual residual tick1257 (organogram +0.606m / expl rec 7.046m; inkanteling 1.1.2026)",
)
print("city_gent notes", ok)

bud_rows = [
    ("bud_iva_hhg_net_2025", 605959, "Organogram net IVA HH 2025 +0.606m (only surplus line in CSVT)"),
    ("bud_iva_hhg_expl_saldo_2025", 720315, "Exploitatiesaldo IVA HH 2025 +0.720m"),
    ("bud_iva_hhg_expl_exp_2025", 6325610, "Exploitatieuitgaven IVA HH 2025 6.326m"),
    ("bud_iva_hhg_expl_rec_2025", 7045925, "Exploitatieontvangsten IVA HH 2025 7.046m"),
    ("bud_iva_hhg_invest_saldo_2025", -114357, "Investeringssaldo IVA HH 2025 -0.114m"),
    ("bud_iva_hhg_invest_exp_2025", 114357, "Investeringsuitgaven IVA HH 2025 0.114m"),
    ("bud_iva_hhg_invest_rec_2025", 0, "Investeringsontvangsten IVA HH 2025 EUR0"),
    ("bud_iva_hhg_fin_saldo_2025", 0, "Financieringssaldo IVA HH 2025 EUR0"),
    ("bud_iva_hhg_od10062_t3_exp_2025", 585437, "OD10062 T3 invest uitgaven envelope 0.585m (pre-MJP 0.175 + in-MJP 0.410)"),
    ("bud_iva_hhg_od10062_t3_roer_2025", 203983, "OD10062 T3 roerende goederen 0.204m"),
    ("bud_iva_hhg_od10062_t3_erfgoed_2025", 381454, "OD10062 T3 erfgoed 0.381m"),
    ("bud_iva_hhg_od10062_t3_rec_2025", 42000, "OD10062 T3 investeringssubsidies 42.000"),
    ("bud_iva_hhg_meeting_spa_2025", 51128, "OD10062 2025 aangerekend meeting-infra Sint-Pietersabdij 51.128"),
    ("bud_iva_hhg_dept_csvt_2025", -101447860, "Departement Cultuur Sport Vrije Tijd organogram net -101.45m (context; not IVA-only)"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT if not bid.endswith("dept_csvt_2025") else CITY,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "bbc_jr_realized",
            "source_id": SRC,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}",
        }
        for bid, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    ("comm_iva_hhg_expl_rec_7_05m_2025", "IVA HH Gent expl ontvangsten 7.046m last year", "7045925", "Ticket/shop/other receipts last IVA year", "Ticket-split FOI"),
    ("comm_iva_hhg_expl_exp_6_33m_2025", "IVA HH Gent expl uitgaven 6.326m last year", "6325610", "Last-year IVA opex before inkanteling", "Personnel/goods split FOI"),
    ("comm_iva_hhg_expl_saldo_0_72m_2025", "IVA HH Gent expl saldo +0.720m", "720315", "Only surplus culture organogram line", "Keep as AGB K&E ringfence FOI"),
    ("comm_iva_hhg_net_0_61m_2025", "IVA HH Gent organogram net +0.606m", "605959", "Net after 0.114m invest", "YoY matrix FOI"),
    ("comm_iva_hhg_invest_0_11m_2025", "IVA HH Gent invest uitgaven 0.114m", "114357", "Last-year IVA capex", "Asset list om niet FOI"),
    ("comm_iva_hhg_od10062_0_59m", "OD10062 historische huizen T3 invest envelope 0.585m", "585437", "MJP invest envelope roerend+erfgoed", "Project-level FOI"),
    ("comm_iva_hhg_inkanteling_2026", "IVA HH inkanteling 1.1.2026 in AGB Kunsten en Erfgoed", "7045925", "Externe verzelfstandiging last-year scale", "Opening 1.1.2026 + extra-comptabel FOI"),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "IVA Historische Huizen / Stad Gent / AGB Kunsten en Erfgoed Gent",
            "legal_basis": "BBC JR2025 city organogram IVA + 2025_GR_00968 inkanteling",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2026",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary Stad Gent JR2025 Toelichting IVA HH",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_iva_hhg_expl_rec_7_05m_2025", "IVA HH Gent last-year expl receipts 7.05m (no ticket split)", "7045925", "7.0", "7.0", "3.0"),
    ("lb_iva_hhg_expl_exp_6_33m_2025", "IVA HH Gent last-year expl spend 6.33m (personnel hole)", "6325610", "6.5", "6.5", "3.0"),
    ("lb_iva_hhg_net_0_61m_2025", "IVA HH Gent organogram net +0.61m surplus folded into AGB", "605959", "7.5", "5.0", "3.0"),
    ("lb_iva_hhg_expl_saldo_0_72m_2025", "IVA HH Gent expl +0.72m only CSVT surplus line", "720315", "7.0", "5.0", "3.0"),
    ("lb_iva_hhg_invest_0_11m_2025", "IVA HH Gent invest 0.11m + assets om niet 2026", "114357", "6.5", "4.0", "3.0"),
    ("lb_iva_hhg_extra_comptabel_2025", "IVA HH extra-comptabel ticket accounts stay city till 2026", "7045925", "8.0", "6.5", "3.0"),
    ("lb_iva_hhg_inkanteling_2026", "IVA HH inkanteling 2026 into AGB K&E after surplus year", "7045925", "7.5", "6.5", "3.0"),
]
n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + "_L5",
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": "City IVA last JR2025 Historische Huizen Gent; inkanteling 1.1.2026 AGB K&E",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Gent residents / monument visitors",
            "stated_goal": "Local dual residual IVA map VL JR2025 last year before AGB fold",
            "measured_outcome": "expl rec 7.046m / exp 6.326m / net +0.606m; no separate BBC; extra-comptabel city-held; inkanteling 1.1.2026",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Ticket-split + extra-comptabel + 1.1.2026 opening FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary Stad Gent JR2025 Toelichting; not TE-additive without city GE",
        }
        for iid, name, cost, absurd, cscore, diff in lrows
    ],
)
print("leaderboard", n)

n = append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": HIER + ">jr2025_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "Ticket/shop/subsidy/personnel/VTE split of expl rec 7.045925m / exp 6.325610m; "
                "extra-comptabel YE2025 saldi 26-70/90-12/21-85/17-81/PGE 30-27 and 2026 city "
                "afpunting; shop inventory transfer value + compensating city subsidy; fixed "
                "assets om niet book value; AGB K&E 1.1.2026 opening after HH inkanteling; "
                "confirm no separate IVA BBC/KBO/NBB 2025"
            ),
            "why_it_matters": (
                "Last IVA year before fold into AGB K&E: surplus +0.606m on 7.05m receipts "
                "sits in city organogram; extra-comptabel ticket cash stays city; no Entity II BBC"
            ),
            "priority": "9",
            "recipient_body": "Stad Gent / AGB Kunsten en Erfgoed Gent",
            "recipient_email": "infopunt@stad.gent",
            "recipient_postal": "Botermarkt 1 9000 Gent",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_iva_hhg_expl_rec_7_05m_2025",
            "linked_leaderboard_id": "lb_iva_hhg_expl_rec_7_05m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_path = DATA / "research_queue.csv"
tmp = rq_path.with_suffix(".csv.tmp")
found_1257 = False
has_1258 = False
with rq_path.open(encoding="utf-8", newline="") as fin, tmp.open("w", encoding="utf-8", newline="") as fout:
    r = csv.DictReader(fin)
    fields = r.fieldnames
    w = csv.DictWriter(fout, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for row in r:
        if row.get("task_id") == "rq_1257":
            found_1257 = True
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["entity_id"] = ENT
            row["title"] = "IVA Historische Huizen Gent last JR2025 city organogram residual"
            row["instructions"] = (
                "Completed: IVA Historische Huizen Gent last JR2025 city Toelichting organogram "
                "(no separate Entity II BBC); inkanteling 1.1.2026 AGB K&E"
            )
            row["blocked_gap_id"] = GAP
            row["notes"] = (
                "tick1257; no own KBO; expl rec 7.046m exp 6.326m net +0.606m invest 0.114m; "
                "extra-comptabel city-held; FOI ready; spawn rq_1258"
            )
        if row.get("task_id") == "rq_1258":
            has_1258 = True
        w.writerow(row)
    if not has_1258:
        w.writerow(
            {
                "task_id": "rq_1258",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "hole_fill",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg not yet mined "
                    "(prefer AGB District09 Gent or sogent JR2025 if separate PDF exists, "
                    "else other unmined AGB/zorg with direct PDF; skip Mobil-O/AG EOS inactive; "
                    "skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat "
                    "unpublished; IVA Historische Huizen Gent done tick1257 — no separate Entity II BBC)"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned tick1257 after IVA Historische Huizen Gent last JR2025; next residual dual L5 VL",
            }
        )
tmp.replace(rq_path)
print("research_queue 1257", found_1257, "spawned_1258", not has_1258)

with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_1257",
            "ticks_completed": "1257",
            "paused": "no",
            "notes": (
                "tick1257 IVA Historische Huizen Gent last JR2025 city organogram residual; "
                "no Entity II BBC/KBO; expl rec 7.046m exp 6.326m net +0.606m invest 0.114m; "
                "inkanteling 1.1.2026 AGB K&E; extra-comptabel city-held; FOI ready; "
                "next rq_1258 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1257 - 2026-08-17 - rq_1257 IVA Historische Huizen Gent last JR2025
- Unit: IVA Historische Huizen Gent last JR2025 city organogram residual after city Gent stub tick101 + AGB Kunsten en Design tick1255 + AGB Erfgoed tick1256. **No separate Entity II BBC / KBO / NBB** (intern agentschap Stad Gent). Primary: Stad Gent JR2025 Toelichting 294p text (GR 2026_GR_00503 22.06.2026) + inkanteling 2025_GR_00968. Houses: Gravensteen / Belfort / SPA / SBA / stadspaleizen / Stadhuis. Inkanteling 1.1.2026 into AGB Kunsten en Erfgoed Gent (0537.520.055).
- EUR strong: expl ontvangsten **7.046m**; expl uitgaven **6.326m**; expl saldo **+0.720m**; invest **0.114m** (ontvangsten **0**); organogram net **+0.606m** (only surplus line in Departement CSVT **−101.45m**); OD10062 T3 envelope **0.585m**; 2025 meeting-infra SPA **51.128**. Extra-comptabel ticket accounts stay city until 2026 afpunting; activa om niet; shop-voorraad + compenserende subsidie (amounts FOI).
- CSVs: sources+2/entities(+city note)/budgets+14/commitments+7/leaderboard+7 + FOI ready `gap_iva_hhg_expl_7_05m_net_0_61m_extra_comptabel_inkanteling_l5` (not sent); rq_1257=done; spawn rq_1258.
- Next: rq_1258 residual dual L5 VL JR2025 hole_fill (prefer AGB District09 Gent or sogent JR2025 if separate PDF).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")

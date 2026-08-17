# -*- coding: utf-8 -*-
"""Tick 1262 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AG CIA Erfgoed Antwerpen JR2025 dual residual (city dual primary; BBC PDF opaque)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T08:05:00Z"
TICK = 1262
SRC = "src_cia_e_jr2025_cbs07873"
SRC2 = "src_cia_e_jr2025_gr00637"
SRC3 = "src_cia_e_jr2025_cbs06536"
SRC4 = "src_cia_e_jr2025_cbs06545"
ENT = "ag_cia_erfgoed_antwerpen"
CITY = "city_antwerpen"
SRC_URL = "https://ebesluit.antwerpen.be/zittingen/25.0115.8265.8765/agendapunten/25.1016.5566.9879"
SRC2_URL = "https://ebesluit.antwerpen.be/zittingen/25.0918.3949.0497/agendapunten/26.0526.3224.0683"
SRC3_URL = "https://ebesluit.antwerpen.be/zittingen/25.0113.4739.5953/agendapunten/25.0902.6161.5942"
SRC4_URL = "https://ebesluit.antwerpen.be/zittingen/25.0113.4739.5953/agendapunten/25.0819.0088.3119"
GAP = "gap_cia_e_bbc_jr2025_opaque_city_dual_11_34m_l5"
HIER = "Vlaanderen>Gemeenten>Antwerpen>AG_CIA_Erfgoed"


def append_rows(path, new_rows):
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


def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()


def patch_rq_target_and_append(path, target_id, new_target, spawn_row):
    text = path.read_text(encoding="utf-8")
    ends_nl = text.endswith("\n")
    lines = text.splitlines()
    header = lines[0]
    fields = next(csv.reader([header]))
    out = [header]
    found = False
    has_spawn = False
    spawn_id = spawn_row.get("task_id")
    for line in lines[1:]:
        if not line:
            continue
        rid = next(csv.reader([line]))[0]
        if rid == spawn_id:
            has_spawn = True
        if rid == target_id:
            found = True
            out.append(csv_line(fields, new_target))
        else:
            out.append(line)
    if not has_spawn:
        out.append(csv_line(fields, spawn_row))
    path.write_text("\n".join(out) + ("\n" if ends_nl else ""), encoding="utf-8")
    return found, not has_spawn


def patch_entity_notes_line(path, entity_id, extra, extra_fields=None):
    text = path.read_text(encoding="utf-8")
    ends_nl = text.endswith("\n")
    lines = text.splitlines()
    header = lines[0]
    fields = next(csv.reader([header]))
    out = [header]
    found = False
    for line in lines[1:]:
        if not line:
            continue
        row = next(csv.DictReader([header, line]))
        if row.get("entity_id") == entity_id:
            found = True
            if extra_fields:
                row.update(extra_fields)
            notes = row.get("notes") or ""
            if extra not in notes:
                row["notes"] = (notes + "; " + extra).strip("; ")
            out.append(csv_line(fields, row))
        else:
            out.append(line)
    path.write_text("\n".join(out) + ("\n" if ends_nl else ""), encoding="utf-8")
    return found


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "2025_CBS_07873 AG CIA Erfgoed+Kunsten dotatie 2025 vastlegging",
            "url": SRC_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1262; CBS 31.10.2025; Erfgoed KBO 0738.733.786 werk 5.38484066m "
                "(musea 3.33190596) + invest nom 5.95907188m (prior 3.72875752 + dit 2.23031436) "
                "= dual 11.34391254m; Kunsten werk besluit 0.187524m (motiv typo 0.705354 ignored)"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2026_GR_00637 AG CIA Erfgoed+Kunsten JR2025 advies/kwijting",
            "url": SRC2_URL,
            "publisher": "Stad Antwerpen gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1262; GR 29.06.2026; RVB 22.06.2026; Erfgoed BBC-only "
                "AG CIA E_JR25_final BBC.pdf; Kunsten BBC+NBB; oordeel zonder voorbehoud; "
                "N-VA/PVDA/Vooruit/GROEN/VB ja; cd&v onthouding; no euros in besluit; "
                "ebesluit TLS fail from box; NBB consult empty"
            ),
        },
        {
            "source_id": SRC3,
            "title": "2025_CBS_06536 AG CIA Erfgoed Digipolis IT nominatief 2025",
            "url": SRC3_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1262; werk 0.192m + invest 0.090m = 0.282m because Digipolis charged "
                "AGB for city-payroll staff and city-owned buildings; IKA 29.08.2025"
            ),
        },
        {
            "source_id": SRC4,
            "title": "2025_CBS_06545 AG CIA Erfgoed+Kunsten MJP 2020-2025 aanpassing 10",
            "url": SRC4_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1262; city planned 2025 expl 5.38484066m + invest 7.37495985m; "
                "invest gap vs CBS nom 1.41588797m"
            ),
        },
    ],
)
print("sources", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    ENT,
    (
        "tick1262 JR2025 dual residual; KBO 0738.733.786 BBC-only; city dual 11.344m "
        "(werk 5.385 + invest nom 5.959) + Digipolis IT 0.282m; MJP invest gap 1.416m; "
        "2026 lock 7.935m; BBC PDF opaque ebesluit TLS; FOI "
        + GAP
    ),
    extra_fields={
        "website": "https://www.antwerpen.be",
        "foi_email": "info@antwerpen.be",
        "foi_postal": "Grote Markt 1 2000 Antwerpen",
        "name_nl": "AG Culturele Instellingen Antwerpen/Erfgoed",
        "name_en": "AG CIA Erfgoed Antwerp museums/heritage AGB",
    },
)
print("entity cia_e", ok)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "CIA Erfgoed dual residual tick1262 (KBO 0738.733.786; city dual 11.344m / "
        "Digipolis IT 0.282m / 2026 lock 7.935m; BBC PDF opaque)"
    ),
)
print("city_antwerpen notes", ok)

bud_rows = [
    ("bud_cia_e_werk_2025", 5384841, "CBS 07873 werkingssubsidie 5.38484066m (10 doelstellingen)"),
    ("bud_cia_e_musea_werk_2025", 3331906, "CBS 07873 2BRS010104 musea collectie/werking/publiek 3.33190596m"),
    ("bud_cia_e_geletterde_werk_2025", 515000, "CBS 07873 2BRS010113 lees- en boekenstad 0.515m"),
    ("bud_cia_e_maritiem_werk_2025", 280000, "CBS 07873 2BRS010112 maritiem erfgoed 0.280m"),
    ("bud_cia_e_kunststad_werk_2025", 275000, "CBS 07873 2BRS010304 kunst in de stad 0.275m"),
    ("bud_cia_e_museale_werk_2025", 294000, "CBS 07873 2BRS010105 museale beleving 0.294m"),
    ("bud_cia_e_lokaal_erfgoed_werk_2025", 260000, "CBS 07873 2BRS010301 lokaal erfgoedbeleid 0.260m"),
    ("bud_cia_e_invest_nom_2025", 5959072, "CBS 07873 investering nominatief 5.95907188m"),
    ("bud_cia_e_invest_prior_2025", 3728758, "CBS 07873 invest reeds vastgelegd 3.72875752m"),
    ("bud_cia_e_invest_this_2025", 2230314, "CBS 07873 invest dit besluit 2.23031436m"),
    ("bud_cia_e_dual_core_2025", 11343913, "CBS 07873 city dual werk+invest 11.34391254m"),
    ("bud_cia_e_it_werk_2025", 192000, "CBS 06536 Digipolis IT werkingstoelage 0.192m"),
    ("bud_cia_e_it_invest_2025", 90000, "CBS 06536 Digipolis IT investeringstoelage 0.090m"),
    ("bud_cia_e_it_total_2025", 282000, "CBS 06536 Digipolis IT top-up 0.282m (city staff/buildings charged to AGB)"),
    ("bud_cia_e_dual_plus_it_2025", 11625913, "City dual 11.344m + Digipolis IT 0.282m = 11.62591254m"),
    ("bud_cia_e_mjp10_expl_2025", 5384841, "CBS 06545 MJP aanpassing 10 expl dotatie 5.38484066m (matches CBS 07873)"),
    ("bud_cia_e_mjp10_invest_planned_2025", 7374960, "CBS 06545 MJP aanpassing 10 invest dotatie 7.37495985m"),
    ("bud_cia_e_mjp10_invest_gap_2025", 1415888, "MJP invest 7.375m minus CBS nom 5.959m = 1.41588797m unrealized/uncommitted"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "cbs_vastlegging",
            "source_id": SRC,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}",
        }
        for bid, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_cia_e_city_dual_11_34m_2025",
        "CIA Erfgoed city dual werk 5.385m + invest nom 5.959m",
        "11343913",
        "City operating+invest dual to museums/heritage AGB",
        "Citeer Stad Antwerpen JR2025-tegenhanger vs 2026 lock 7.935m FOI",
    ),
    (
        "comm_cia_e_werk_5_38m_2025",
        "CIA Erfgoed werkingssubsidie 5.385m (musea 3.332m)",
        "5384841",
        "10 doelstellingen; cash on thesaurieplanning",
        "Cash vs vastlegging + VL counterpart FOI",
    ),
    (
        "comm_cia_e_invest_5_96m_2025",
        "CIA Erfgoed invest nominatief 5.959m (prior 3.729 + dit 2.230)",
        "5959072",
        "Uitbetaling op bewijsstukken",
        "MJP 7.375 vs CBS 5.959 gap 1.416m FOI",
    ),
    (
        "comm_cia_e_digipolis_it_0_28m_2025",
        "CIA Erfgoed Digipolis IT top-up 0.282m (city staff/buildings)",
        "282000",
        "Kostendelende vereniging charged AGB for city payroll + city buildings",
        "Verdeelsleutel + inside/outside dual 11.34m FOI",
    ),
    (
        "comm_cia_e_mjp_invest_gap_1_42m_2025",
        "CIA Erfgoed MJP invest 7.375m vs CBS nom 5.959m gap 1.416m",
        "1415888",
        "Aanpassing 10 planned invest not in CBS 07873 nominatief",
        "Restkredieten 2025-2026 FOI",
    ),
    (
        "comm_cia_e_bbc_jr2025_opaque",
        "CIA Erfgoed BBC JR2025 PDF named but not retrieved",
        "",
        "GR 2026_GR_00637 attachment AG CIA E_JR25_final BBC.pdf; BBC-only no NBB",
        "Publish working PDF + J2/J4/J5/T2-T4 FOI",
    ),
    (
        "comm_cia_e_vs_2026_lock_7_94m",
        "CIA Erfgoed 2025 dual 11.34m vs 2026 city lock 7.935m",
        "7934670",
        "Tick217 package musea 6.507 + geletterde 1.422 + cyber 6k",
        "Which 2025 lines drop in 2026 FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AG CIA Erfgoed / Stad Antwerpen musea en erfgoed",
            "legal_basis": "2025_CBS_07873 + 2026_GR_00637 + 2025_CBS_06536 + 2025_CBS_06545",
            "decision_date": "2026-06-29",
            "start_year": "2025",
            "end_year": "2026",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}" if env else "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong" if env else "medium",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary CBS HTML city dual; BBC PDF opaque",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_cia_e_city_dual_11_34m_2025", "CIA Erfgoed city dual 11.34m vs 2026 lock 7.94m", "11343913", "7.5", "7.5", "3.0"),
    ("lb_cia_e_digipolis_it_0_28m_2025", "CIA Erfgoed Digipolis IT 0.28m for city staff/buildings", "282000", "8.5", "5.0", "2.0"),
    ("lb_cia_e_bbc_opaque_jr2025", "CIA Erfgoed BBC JR2025 PDF named, euros unpublished", "11343913", "8.0", "7.0", "4.0"),
    ("lb_cia_e_mjp_invest_gap_1_42m_2025", "CIA Erfgoed MJP invest 7.38m vs CBS 5.96m gap 1.42m", "1415888", "7.0", "6.0", "3.0"),
    ("lb_cia_e_werk_5_38m_2025", "CIA Erfgoed werking 5.38m (musea 3.33m of 10 lines)", "5384841", "6.5", "6.5", "3.0"),
    ("lb_cia_e_invest_5_96m_2025", "CIA Erfgoed invest nom 5.96m (bewijsstukken)", "5959072", "6.5", "6.5", "3.0"),
    ("lb_cia_e_city_payroll_shell_2025", "CIA Erfgoed shell: city payroll + city buildings + AGB dual", "11343913", "8.0", "7.0", "3.0"),
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
            "tco_notes": "AG CIA Erfgoed JR2025 museums/heritage Entity II Antwerpen; BBC internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Antwerp residents / Groep Antwerpen musea",
            "stated_goal": "Local dual residual AGB map VL JR2025 heritage vehicle",
            "measured_outcome": "city dual 11.344m / Digipolis IT 0.282m / 2026 lock 7.935m / BBC PDF opaque",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish BBC PDF + Digipolis sleutel + 2025-vs-2026 lock FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary CBS HTML; not TE-additive without city GE; BBC assets/AFM/BBR unknown",
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
                "BBC JR2025 PDF (AG CIA E_JR25_final BBC.pdf on 2026_GR_00637) working URL + "
                "J2/J4/J5/T2-T4 totals (assets, AFM, gecorr AFM, BBR, fin debt, cash, personnel/VTE, P&L); "
                "city dual cash vs vastlegging 5.38484066+5.95907188=11.34391254; "
                "MJP invest 7.37495985 vs CBS nom 5.95907188 gap 1.41588797; "
                "Digipolis IT 0.192+0.090=0.282 inside/outside dual; "
                "2026 lock 7.93466994 vs 2025 dual; city-payroll/buildings shell"
            ),
            "why_it_matters": (
                "Remaining Antwerp Entity II after Zorgbedrijf / Vespa / AGSO: city dual 11.34m "
                "plus Digipolis IT bailout 0.28m for charges on city staff and city buildings; "
                "BBC JR2025 exists and was approved 29.06.2026 but PDF not retrievable (ebesluit TLS); "
                "no NBB filing; 2026 lock drops to 7.94m"
            ),
            "priority": "8",
            "recipient_body": "AG CIA Erfgoed / Stad Antwerpen",
            "recipient_email": "info@antwerpen.be",
            "recipient_postal": "Grote Markt 1 2000 Antwerpen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_cia_e_city_dual_11_34m_2025",
            "linked_leaderboard_id": "lb_cia_e_city_dual_11_34m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1262",
    "title": "AG CIA Erfgoed Antwerpen JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AG CIA Erfgoed city dual from 2025_CBS_07873 + GR 2026_GR_00637; "
        "KBO 0738.733.786 BBC-only; dual 11.344m / Digipolis IT 0.282m; BBC PDF opaque"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T07:45:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1262 AG CIA Erfgoed JR2025 dual residual; KBO 0738.733.786 BBC-only; "
        "city dual 11.344m werk 5.385 invest nom 5.959 Digipolis IT 0.282m "
        "MJP invest gap 1.416m 2026 lock 7.935m; BBC PDF opaque ebesluit TLS; "
        "FOI ready not sent; next rq_1263 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1263",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg not yet mined "
        "(Gent dual AGB cluster 1255-1259 + AG Vespa 1260 + AGSO 1261 + AG CIA Erfgoed 1262 done; "
        "prefer AG CIA Kunsten Antwerpen JR2025 PDF 2026_GR_00637 NBB+BBC or other unmined AGB/zorg "
        "with direct PDF; WAGSO Waregem already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat unpublished)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1262 after AG CIA Erfgoed JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1262", rq_new, rq_spawn)
print("research_queue 1262", found, "spawned_1263", spawned)

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
            "last_unit_id": "rq_1262",
            "ticks_completed": "1262",
            "paused": "no",
            "notes": (
                "tick1262 AG CIA Erfgoed JR2025 dual residual; KBO 0738.733.786 BBC-only; "
                "city dual 11.344m werk 5.385 invest nom 5.959 Digipolis IT 0.282m "
                "MJP invest gap 1.416m 2026 lock 7.935m; BBC PDF opaque; FOI ready; "
                "next rq_1263 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1262 - 2026-08-17 - rq_1262 AG CIA Erfgoed dual residual
- Unit: AG Culturele Instellingen Antwerpen/Erfgoed JR2025 Entity II after city package tick217 + Zorgbedrijf Antwerpen tick1246 + AG Vespa tick1260 + AGSO tick1261 (KBO 0738.733.786; BBC-only; RVB 22.06.2026 / GR 2026_GR_00637 29.06.2026). Distinct from Gent AGB cluster 1255–1259 and from sibling AG CIA Kunsten (0738.734.281, next). Seat Grote Markt 1. Staff on city payroll; buildings city-owned. WAGSO already mined tick1199.
- EUR strong (city dual primary HTML; BBC internals unknown): werk **5.385m** (musea **3.332m** + 9 other lines) + invest nom **5.959m** (prior **3.729m** + dit **2.230m**) = dual **11.344m**; Digipolis IT top-up **0.282m** (werk 0.192 + invest 0.090) because AGB billed for city staff/buildings → dual+IT **11.626m**; MJP10 invest planned **7.375m** vs CBS nom **5.959m** gap **1.416m**; 2026 lock **7.935m**. BBC PDF named (`AG CIA E_JR25_final BBC.pdf`) but ebesluit TLS fail + no org-site + NBB empty.
- CSVs: sources+4/entities(upgrade+city note)/budgets+18/commitments+7/leaderboard+7 + FOI ready `gap_cia_e_bbc_jr2025_opaque_city_dual_11_34m_l5` (not sent); rq_1262=done; spawn rq_1263; ticks=1262. No every-10 (1262 not a *0 tick).
- Next: rq_1263 residual dual L5 VL JR2025 hole_fill (prefer AG CIA Kunsten Antwerpen JR2025 PDF 2026_GR_00637 NBB+BBC).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")

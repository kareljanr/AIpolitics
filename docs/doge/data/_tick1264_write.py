# -*- coding: utf-8 -*-
"""Tick 1264 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AG Energiebesparingsfonds Antwerpen JR2025 dual residual (GR HTML BBC totals + city dual 2026/2023; PDFs opaque)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T08:15:00Z"
TICK = 1264
SRC = "src_ebf_jr2025_gr00656"
SRC2 = "src_ebf_jr2024_rvb00003"
SRC3 = "src_ebf_jr2024_cbs03357"
SRC4 = "src_ebf_rest_2024_cbs04706"
SRC5 = "src_ebf_werk_2023_cbs00753"
SRC6 = "src_ebf_werk_2024_cbs09422"
SRC7 = "src_ebesluit_energie_2026"
ENT = "ag_energiebesparingsfonds_antwerpen"
CITY = "city_antwerpen"
SRC_URL = "https://ebesluit.antwerpen.be/zittingen/25.0918.3949.0497/agendapunten/26.0605.2660.4666"
SRC2_URL = "https://ebesluit.antwerpen.be/zittingen/25.0410.7772.3354/agendapunten/25.0411.5439.2954"
SRC3_URL = "https://ebesluit.antwerpen.be/zittingen/25.0113.3147.8197/agendapunten/25.0505.5662.2882"
SRC4_URL = "https://ebesluit.antwerpen.be/zittingen/25.0113.0991.0577/agendapunten/25.0620.8950.7706"
SRC5_URL = "https://ebesluit.antwerpen.be/zittingen/22.0922.2678.7491/agendapunten/23.0130.4270.9460"
SRC6_URL = "https://ebesluit.antwerpen.be/zittingen/23.1017.6218.8757/agendapunten/24.1120.0490.6054"
SRC7_URL = "https://ebesluit.antwerpen.be/zittingen/25.0916.2153.6267/agendapunten/26.0120.6432.7464"
GAP = "gap_ebf_jr2025_pdf_opaque_city_dual_2025_unknown_bbr_1_02m_l5"
HIER = "Vlaanderen>Gemeenten>Antwerpen>AG_Energiebesparingsfonds"


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
            "title": "2026_GR_00656 AG Energiebesparingsfonds JR2025 advies/kwijting",
            "url": SRC_URL,
            "publisher": "Stad Antwerpen gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1264; GR 29.06.2026; KBO 0834.660.452; BBR year 0.046788m "
                "BBR cum 1.022437m AFM 0.082161m; restmiddelen 0 after Mijn Verbouwlening; "
                "RVB 29.05.2026 jr 4; BBC PDF opaque ebesluit TLS; NBB consult empty"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2025_RVBAGEBF_00003 AG Energiebesparingsfonds JR2024 vaststelling",
            "url": SRC2_URL,
            "publisher": "AG Energiebesparingsfonds raad van bestuur",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1264; RVB 29.04.2025; BBR year -0.150943m BBR cum 0.975650m "
                "AFM -0.130931m; compare vs JR2025 AFM swing +0.213092m"
            ),
        },
        {
            "source_id": SRC3,
            "title": "2025_CBS_03357 AG Energiebesparingsfonds JR2024 advies/kwijting",
            "url": SRC3_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1264; BBR year -0.150943m BBR cum 0.975850m (+0.000200 vs RVB) "
                "AFM -0.130931m; restmiddelen teruggave 0.004321m"
            ),
        },
        {
            "source_id": SRC4,
            "title": "2025_CBS_04706 AG Energiebesparingsfonds restmiddelen 2024",
            "url": SRC4_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1264; rest 0.00864188m; 50% city 0.00432094m; 50% klimaatplan; "
                "KBO 0834.660.452 Turnhoutsebaan 139"
            ),
        },
        {
            "source_id": SRC5,
            "title": "2023_CBS_00753 AG Energiebesparingsfonds toelage 2023 vastlegging",
            "url": SRC5_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1264; MJP werk 0.281253m; locked 0.264555m; index withheld 0.016698m"
            ),
        },
        {
            "source_id": SRC6,
            "title": "2024_CBS_09422 AG Energiebesparingsfonds toelage 2024 index add-on",
            "url": SRC6_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1264; extra lock 0.012398m; main 2024 lock 2024_CBS_00832 euros not retrieved"
            ),
        },
    ],
)
print("sources", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    ENT,
    (
        "tick1264 JR2025 dual residual; KBO 0834.660.452 BBC; BBR year 0.047m "
        "BBR cum 1.022m AFM 0.082m; city dual 2026 lock 0.592m vs 2023 0.265m "
        "(+0.327m); city dual 2025 unknown; PDFs opaque; FOI " + GAP
    ),
    extra_fields={
        "website": "https://www.antwerpenvoorklimaat.be",
        "foi_email": "info@antwerpen.be",
        "foi_postal": "Turnhoutsebaan 139 2140 Borgerhout",
    },
)
print("entity ebf", ok)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "EBF dual residual tick1264 (KBO 0834.660.452; BBR 1.022m / AFM 0.082m / "
        "city 2026 0.592m rise vs 2023 0.265m; 2025 lock unknown; PDF opaque)"
    ),
)
print("city_antwerpen notes", ok)

bud_rows = [
    ("bud_ebf_bbr_year_2025", "2025", 46788, SRC, "executed", "GR 00656 BBR boekjaar 0.046788m"),
    ("bud_ebf_bbr_cum_2025", "2025", 1022437, SRC, "executed", "GR 00656 gecumuleerd BBR 1.022437m"),
    ("bud_ebf_afm_2025", "2025", 82161, SRC, "executed", "GR 00656 AFM 0.082161m"),
    ("bud_ebf_rest_city_2025", "2025", 0, SRC, "executed", "GR 00656 geen restmiddelen teruggave na Mijn Verbouwlening"),
    ("bud_ebf_bbr_year_2024", "2024", -150943, SRC2, "executed", "RVB 00003 BBR boekjaar -0.150943m"),
    ("bud_ebf_bbr_cum_2024", "2024", 975650, SRC2, "executed", "RVB 00003 gecumuleerd BBR 0.975650m (CBS 03357 0.975850m +200)"),
    ("bud_ebf_afm_2024", "2024", -130931, SRC2, "executed", "RVB 00003 AFM -0.130931m"),
    ("bud_ebf_rest_2024", "2024", 8641.88, SRC4, "executed", "CBS 04706 restmiddelen 0.00864188m"),
    ("bud_ebf_rest_city_50_2024", "2024", 4320.94, SRC4, "executed", "CBS 04706 50% stad 0.00432094m"),
    ("bud_ebf_afm_swing_2024_25", "2025", 213092, SRC, "executed", "AFM -0.130931m (2024) to +0.082161m (2025) = +0.213092m"),
    ("bud_ebf_werk_2023", "2023", 264555, SRC5, "cbs_vastlegging", "CBS 00753 werk locked 0.264555m"),
    ("bud_ebf_werk_mjp_2023", "2023", 281253.13, SRC5, "budgeted", "CBS 00753 MJP werk 0.281253m"),
    ("bud_ebf_werk_index_2024", "2024", 12398.07, SRC6, "cbs_vastlegging", "CBS 09422 index add-on 0.012398m; main 2024 lock unknown"),
    ("bud_ebf_city_rise_2023_26", "2026", 326965.40, SRC7, "cbs_vastlegging", "City lock 0.264555m (2023) to 0.591520m (2026) = +0.326965m"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": year,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": src,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}",
        }
        for bid, year, amt, src, basis, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_ebf_bbr_1_02m_2025",
        "EBF BBR cum 1.022m / year +0.047m",
        "1022437",
        "Accumulated budget result after 2024 -0.151m year; restmiddelen 2025 = 0",
        "Publish BBC J2/J4/J5 + why no city clawback FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ebf_afm_0_08m_2025",
        "EBF AFM 0.082m after 2024 -0.131m",
        "82161",
        "AFM swing +0.213m; no expl/invest/fin split in HTML",
        "J4/J5 expl/invest/fin split FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ebf_afm_swing_0_21m_2024_25",
        "EBF AFM swing -0.131m (2024) to +0.082m (2025)",
        "213092",
        "RVB 00003 vs GR 00656; climate Energiehuis vehicle",
        "What reversed AFM FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ebf_city_rise_0_33m_2023_26",
        "EBF city werk 0.265m (2023) to 0.592m (2026) rise 0.327m",
        "326965.40",
        "Renovatiegolf / Energiehuis scale-up; 2025 lock unpublished",
        "Publish 2025 lock + which lines grew FOI",
        SRC7,
        SRC7_URL,
    ),
    (
        "comm_ebf_bbc_opaque_jr2025",
        "EBF BBC JR2025 PDFs not retrieved",
        "",
        "GR 00656 bijlagen + RVB 29.05.2026 jr 4; ebesluit TLS / NBB empty",
        "Publish working PDFs + J2/J4/J5/T2-T4 FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ebf_city_dual_2025_unknown",
        "EBF city dual 2025 lock euros unpublished in HTML",
        "",
        "2023 and 2026 locks public; 2025 CBS analog not found; 2024 main lock 00832 euros missing",
        "2025 nominatieve werkingstoelage vastlegging FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ebf_rest_0_2025",
        "EBF restmiddelen 2025 = 0 after Mijn Verbouwlening deferral",
        "0",
        "Vs 2024 rest 0.008642m / city 50% 0.004321m",
        "Exact deferred stock + clawback calc FOI",
        SRC,
        SRC_URL,
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AG Energiebesparingsfonds / Energiehuis / Stad Antwerpen climate",
            "legal_basis": "2026_GR_00656 + 2026_CBS_01114 + 2025_RVBAGEBF_00003 + 2025_CBS_04706 + 2023_CBS_00753",
            "decision_date": "2026-06-29",
            "start_year": "2025",
            "end_year": "2026",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}" if env else "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": evurl,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": src,
            "confidence": "strong" if env else "medium",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary GR+CBS HTML; BBC/NBB PDF opaque",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_ebf_bbr_1_02m_2025", "EBF BBR cum 1.02m / year +0.047m", "1022437", "6.5", "6.0", "3.0"),
    ("lb_ebf_afm_swing_0_21m_2024_25", "EBF AFM -0.13m (2024) to +0.08m (2025) swing 0.21m", "213092", "7.0", "5.0", "3.0"),
    ("lb_ebf_city_rise_0_33m_2023_26", "EBF city werk 0.26m (2023) to 0.59m (2026) rise 0.33m", "326965.40", "7.0", "5.5", "3.0"),
    ("lb_ebf_bbc_opaque_jr2025", "EBF BBC JR2025 PDFs not retrieved, schema unpublished", "1022437", "7.5", "6.0", "3.0"),
    ("lb_ebf_city_dual_2025_unknown", "EBF city dual 2025 lock euros unpublished", "591520.40", "7.0", "5.0", "3.0"),
    ("lb_ebf_rest_0_vs_bbr_1_02m_2025", "EBF restmiddelen 0 vs BBR 1.02m after Mijn Verbouwlening", "1022437", "6.5", "6.0", "3.0"),
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
            "tco_notes": "AG Energiebesparingsfonds JR2025 Energiehuis/renovatiegolf Entity II Antwerpen; BBC/NBB PDF internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Antwerp residents / Energiehuis / renovatiegolf",
            "stated_goal": "Local dual residual AGB map VL JR2025 climate/energy vehicle",
            "measured_outcome": "BBR 1.022m / AFM 0.082m / city 2026 0.592m rise vs 2023 0.265m / 2025 lock unknown / PDF opaque",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish BBC+NBB PDFs + 2025 city lock + explain 0.33m city rise vs 1.02m BBR FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary GR+CBS HTML; not TE-additive without city GE; cash/fin debt/VTE unknown",
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
                "BBC+NBB JR2025 PDFs (GR 2026_GR_00656 / RVB 29.05.2026 jr 4) working URL + "
                "J2/J4/J5/T2-T4 + NBB (assets, cash, fin debt, EV, omzet, personnel/VTE, "
                "expl/invest/fin, Mijn Verbouwlening deferred stock); city dual 2025 lock "
                "and cash vs 2023 lock 0.264555 / 2026 lock 0.591520; 2024 main lock "
                "2024_CBS_00832 euros; restmiddelen exact vs BBR 1.022437; AFM swing "
                "-0.130931 to +0.082161"
            ),
            "why_it_matters": (
                "Remaining Antwerp Entity II climate/Energiehuis after CIA Kunsten 1263: "
                "city dual jumped 0.265m (2023) to 0.592m (2026) while BBR sits at 1.02m "
                "and AFM flipped from -0.131m to +0.082m; 2025 city lock HTML not found; "
                "BBC JR2025 approved 29.06.2026 but PDFs not retrievable (ebesluit TLS / NBB empty)"
            ),
            "priority": "8",
            "recipient_body": "AG Energiebesparingsfonds / Stad Antwerpen",
            "recipient_email": "info@antwerpen.be",
            "recipient_postal": "Turnhoutsebaan 139 2140 Borgerhout",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_ebf_city_rise_0_33m_2023_26",
            "linked_leaderboard_id": "lb_ebf_city_rise_0_33m_2023_26",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1264",
    "title": "AG Energiebesparingsfonds Antwerpen JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AG Energiebesparingsfonds GR 00656 BBC totals + city dual 2026/2023; "
        "KBO 0834.660.452 BBC; BBR 1.022m AFM 0.082m city 2026 0.592m vs 2023 0.265m; "
        "2025 lock unknown; PDFs opaque"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T07:55:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1264 AG Energiebesparingsfonds JR2025 dual residual; KBO 0834.660.452 BBC; "
        "BBR year 0.047m BBR cum 1.022m AFM 0.082m; city dual 2026 lock 0.592m vs 2023 0.265m "
        "= +0.327m; 2025 lock unknown; restmiddelen 0; PDFs opaque ebesluit TLS; FOI ready "
        "not sent; next rq_1265 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1265",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg not yet mined "
        "(Gent dual AGB cluster 1255-1259 + AG Vespa 1260 + AGSO 1261 + AG CIA Erfgoed 1262 "
        "+ AG CIA Kunsten 1263 + AG Energiebesparingsfonds 1264 done; prefer AG Digipolis "
        "Antwerpen JR2025 GR 2026_GR_00616 assets 73.605m surplus 0.110m or other unmined "
        "AGB/zorg with direct PDF; WAGSO Waregem already mined tick1199; skip Mobil-O/AG EOS "
        "inactive; skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf "
        "Brasschaat unpublished; ebesluit TLS — prefer org sites / NBB / city HTML)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1264 after AG Energiebesparingsfonds JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1264", rq_new, rq_spawn)
print("research_queue 1264", found, "spawned_1265", spawned)

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
            "last_unit_id": "rq_1264",
            "ticks_completed": "1264",
            "paused": "no",
            "notes": (
                "tick1264 AG Energiebesparingsfonds JR2025 dual residual; KBO 0834.660.452 BBC; "
                "BBR year 0.047m BBR cum 1.022m AFM 0.082m; city dual 2026 0.592m vs 2023 0.265m; "
                "2025 lock unknown; PDFs opaque; FOI ready; next rq_1265 residual dual L5 VL "
                "(prefer Digipolis JR2025); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1264 - 2026-08-17 - rq_1264 AG Energiebesparingsfonds dual residual
- Unit: AG Energiebesparingsfonds Antwerpen JR2025 Entity II after CIA Kunsten tick1263 (KBO 0834.660.452; BBC; RVB 29.05.2026 jr 4 / GR 29.06.2026 `2026_GR_00656`). Distinct from CIA Kunsten/Erfgoed / Vespa / AGSO. Seat Turnhoutsebaan 139, 2140 Borgerhout. Energiehuis / renovatiegolf. Tick217 already had 2026 city lock 0.592m. WAGSO already mined tick1199.
- EUR strong (GR HTML BBC totals + city dual HTML; PDF internals unknown): BBR year **0.047m**; BBR cum **1.022m**; AFM **0.082m** (vs 2024 BBR **-0.151m** / AFM **-0.131m**, swing **+0.213m**); restmiddelen 2025 **0** after Mijn Verbouwlening (vs 2024 rest **0.0086m** / city 50% **0.0043m**); city 2026 lock **0.592m** of MJP **0.607m**; city 2023 lock **0.265m** of MJP **0.281m**; rise 2023→2026 **0.327m**. City dual 2025 lock HTML not found. BBC/NBB PDFs not retrieved (ebesluit TLS + NBB empty).
- CSVs: sources+6/entities(patch+city note)/budgets+14/commitments+7/leaderboard+6 + FOI ready `gap_ebf_jr2025_pdf_opaque_city_dual_2025_unknown_bbr_1_02m_l5` (not sent); rq_1264=done; spawn rq_1265; ticks=1264. No every-10 (1264 not a *0 tick).
- Next: rq_1265 residual dual L5 VL JR2025 hole_fill (prefer AG Digipolis Antwerpen JR2025 GR 2026_GR_00616 assets 73.605m surplus 0.110m or other unmined AGB/zorg with direct PDF).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")

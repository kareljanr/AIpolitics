# -*- coding: utf-8 -*-
"""Tick 1263 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AG CIA Kunsten Antwerpen JR2025 dual residual (RVB HTML BBC totals + city dual; PDFs opaque)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T07:55:00Z"
TICK = 1263
SRC = "src_cia_k_jr2025_rvb00010"
SRC2 = "src_cia_k_jr2025_cbs07873"
SRC3 = "src_cia_k_jr2025_gr00637"
SRC4 = "src_cia_k_jr2025_cbs06545"
SRC5 = "src_cia_k_jr2023_cbs03505"
ENT = "ag_cia_kunsten_antwerpen"
CITY = "city_antwerpen"
SRC_URL = "https://ebesluit.antwerpen.be/zittingen/25.1112.6377.0752/agendapunten/26.0526.9893.6547"
SRC2_URL = "https://ebesluit.antwerpen.be/zittingen/25.0115.8265.8765/agendapunten/25.1016.5566.9879"
SRC3_URL = "https://ebesluit.antwerpen.be/zittingen/25.0918.3949.0497/agendapunten/26.0526.3224.0683"
SRC4_URL = "https://ebesluit.antwerpen.be/zittingen/25.0113.4739.5953/agendapunten/25.0819.0088.3119"
SRC5_URL = "https://ebesluit.antwerpen.be/zittingen/22.1013.6262.2446/agendapunten/23.0420.3504.1353"
GAP = "gap_cia_k_jr2025_pdf_opaque_city_dual_0_19m_bbr_2_76m_l5"
HIER = "Vlaanderen>Gemeenten>Antwerpen>AG_CIA_Kunsten"


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
            "title": "2026_RVBKUNSTEN_00010 AG CIA Kunsten JR2025 vaststelling",
            "url": SRC_URL,
            "publisher": "AG CIA Kunsten raad van bestuur",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1263; RVB 22.06.2026; KBO 0738.734.281; assets 6.089636m "
                "BBR=avail 2.756636m AFM=gecorr 0.418177m PnL 0.256686m; "
                "BBC+NBB PDFs named; restmiddelen TBD Inspectie Financiën"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2025_CBS_07873 AG CIA Kunsten+Erfgoed dotatie 2025 vastlegging",
            "url": SRC2_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1263; CBS 31.10.2025; Kunsten KBO 0738.734.281 werk 0.187524m "
                "(podium 0.087524 + events 0.100000); invest 0; "
                "motiv typo 0.705354 ignored (table+art1=0.187524)"
            ),
        },
        {
            "source_id": SRC3,
            "title": "2026_GR_00637 AG CIA Erfgoed+Kunsten JR2025 advies/kwijting",
            "url": SRC3_URL,
            "publisher": "Stad Antwerpen gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1263; GR 29.06.2026; Kunsten BBC+NBB oordeel zonder voorbehoud; "
                "attachments AG CIA K_JR25_final BBC.pdf + venn B.pdf; no euros in GR; "
                "ebesluit PDF TLS fail from box; NBB consult 403"
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
                "tick1263; city planned 2025 expl Kunsten 0.187524m; "
                "geen investeringsdotatie Kunsten (matches CBS 07873)"
            ),
        },
        {
            "source_id": SRC5,
            "title": "2023_CBS_03505 AG CIA Kunsten dotatie 2023 vastlegging",
            "url": SRC5_URL,
            "publisher": "Stad Antwerpen college",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1263; 2023 werk 0.715984m (podium 0.615984 + events 0.100000); "
                "drop vs 2025 0.187524 = 0.528460m"
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
            "name_nl": "AG Culturele Instellingen Antwerpen/Kunsten",
            "name_fr": "AG Institutions culturelles Anvers/Arts",
            "name_en": "AG CIA Kunsten Antwerp performing-arts/Arenberg AGB",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.antwerpen.be/info/autonoom-gemeentebedrijf-culturele-instellingen-antwerpen-kunsten",
            "foi_email": "AG_Culturele_Instellingen@antwerpen.be",
            "foi_postal": "Grote Markt 1 2000 Antwerpen",
            "notes": (
                "tick1263 JR2025 dual residual; KBO 0738.734.281 BBC+NBB; "
                "assets 6.090m BBR=avail 2.757m AFM=gecorr 0.418m PnL 0.257m; "
                "city dual werk 0.188m invest 0 (drop vs 2023 0.716m = 0.528m); "
                "PDFs named ebesluit TLS; FOI " + GAP
            ),
        }
    ],
)
print("entity cia_k", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "CIA Kunsten dual residual tick1263 (KBO 0738.734.281; assets 6.090m / "
        "BBR 2.757m / AFM 0.418m / city werk 0.188m drop vs 2023 0.716m; PDF opaque)"
    ),
)
print("city_antwerpen notes", ok)

bud_rows = [
    ("bud_cia_k_werk_2025", 187524, "CBS 07873 werkingssubsidie 0.187524m (podium+events)"),
    ("bud_cia_k_podium_werk_2025", 87524, "CBS 07873 2BRS010109 podiumkunsten 0.087524m"),
    ("bud_cia_k_events_werk_2025", 100000, "CBS 07873 2BRS010303 cultuurevenementen 0.100m"),
    ("bud_cia_k_invest_2025", 0, "CBS 07873 + MJP10: geen investeringsdotatie Kunsten"),
    ("bud_cia_k_dual_2025", 187524, "CBS 07873 city dual werk only 0.187524m"),
    ("bud_cia_k_assets_2025", 6089636, "RVB 00010 balanstotaal 6.089636m 31.12.2025"),
    ("bud_cia_k_bbr_2025", 2756636, "RVB 00010 gecumuleerd BBR 2.756636m"),
    ("bud_cia_k_avail_bbr_2025", 2756636, "RVB 00010 beschikbaar BBR 2.756636m (= gecumuleerd)"),
    ("bud_cia_k_afm_2025", 418177, "RVB 00010 AFM 0.418177m"),
    ("bud_cia_k_gecorr_afm_2025", 418177, "RVB 00010 gecorr AFM 0.418177m (= AFM)"),
    ("bud_cia_k_pnl_2025", 256686, "RVB 00010 boekhoudkundig resultaat 0.256686m"),
    ("bud_cia_k_werk_2023", 715984, "CBS 03505 2023 werk 0.715984m (podium 0.616 + events 0.100)"),
    ("bud_cia_k_dual_drop_2023_25", 528460, "City werk drop 0.715984-0.187524=0.528460m (~74%)"),
    ("bud_cia_k_mjp10_expl_2025", 187524, "CBS 06545 MJP aanpassing 10 expl dotatie 0.187524m (matches CBS 07873)"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": "2025" if "2023" not in bid else "2023",
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "executed" if bid.startswith("bud_cia_k_assets") or "bbr" in bid or "afm" in bid or "pnl" in bid else "cbs_vastlegging",
            "source_id": SRC if bid.startswith(("bud_cia_k_assets", "bud_cia_k_bbr", "bud_cia_k_avail", "bud_cia_k_afm", "bud_cia_k_gecorr", "bud_cia_k_pnl")) else (SRC5 if "2023" in bid or "drop" in bid else SRC2),
            "confidence": "strong",
            "notes": note + f"; tick{TICK}",
        }
        for bid, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_cia_k_city_dual_0_19m_2025",
        "CIA Kunsten city dual werk 0.188m invest 0",
        "187524",
        "City operating dual to podium/Arenberg AGB; no invest",
        "Citeer cash vs vastlegging + 2026 lock FOI",
    ),
    (
        "comm_cia_k_dual_drop_0_53m_2023_25",
        "CIA Kunsten city werk drop 0.716m (2023) to 0.188m (2025)",
        "528460",
        "Podium line 0.616m to 0.088m; events line frozen 0.100m",
        "Which Arenberg/other lines dropped FOI",
    ),
    (
        "comm_cia_k_bbr_2_76m_2025",
        "CIA Kunsten BBR=avail 2.757m vs city dual 0.188m",
        "2756636",
        "Accumulated budget result equals available; restmiddelen TBD",
        "Restmiddelen + why city dual cut while BBR 2.76m FOI",
    ),
    (
        "comm_cia_k_afm_0_42m_2025",
        "CIA Kunsten AFM=gecorr AFM 0.418m",
        "418177",
        "RVB HTML; no AFM/MJP gap published",
        "J4/J5 expl/invest/fin split FOI",
    ),
    (
        "comm_cia_k_assets_6_09m_2025",
        "CIA Kunsten assets 6.090m / PnL 0.257m",
        "6089636",
        "RVB HTML balanstotaal + boekhoudkundig resultaat",
        "NBB omzet/EV/fin debt/cash/VTE FOI",
    ),
    (
        "comm_cia_k_bbc_nbb_jr2025_opaque",
        "CIA Kunsten BBC+NBB JR2025 PDFs named but not retrieved",
        "",
        "GR/RVB attachments AG CIA K_JR25_final BBC.pdf + venn B.pdf",
        "Publish working PDFs + J2/J4/J5/T2-T4 FOI",
    ),
    (
        "comm_cia_k_2026_lock_unknown",
        "CIA Kunsten 2026 MJP lock euros unpublished in HTML",
        "",
        "MJP 2026-2031 GR 15.12.2025 jr 932 + RVB aanpassing 1; no euro in HTML",
        "2026-2031 city expl/invest lock FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AG CIA Kunsten / Arenberg / Stad Antwerpen podium",
            "legal_basis": "2026_RVBKUNSTEN_00010 + 2025_CBS_07873 + 2026_GR_00637 + 2025_CBS_06545 + 2023_CBS_03505",
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
            "notes": f"tick{TICK}; primary RVB+CBS HTML; BBC/NBB PDF opaque",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_cia_k_dual_drop_0_53m_2023_25", "CIA Kunsten city werk 0.72m (2023) to 0.19m (2025) drop 0.53m", "528460", "8.0", "6.0", "3.0"),
    ("lb_cia_k_bbr_2_76m_vs_dual_0_19m_2025", "CIA Kunsten BBR 2.76m vs city dual 0.19m", "2756636", "8.0", "6.5", "3.0"),
    ("lb_cia_k_city_dual_0_19m_2025", "CIA Kunsten city dual werk 0.19m invest 0", "187524", "6.0", "4.0", "2.0"),
    ("lb_cia_k_afm_0_42m_2025", "CIA Kunsten AFM=gecorr 0.42m", "418177", "6.0", "5.0", "3.0"),
    ("lb_cia_k_assets_6_09m_pnl_0_26m_2025", "CIA Kunsten assets 6.09m / PnL 0.26m", "6089636", "6.5", "6.0", "3.0"),
    ("lb_cia_k_bbc_nbb_opaque_jr2025", "CIA Kunsten BBC+NBB JR2025 PDFs named, full schema unpublished", "6089636", "7.5", "6.5", "3.0"),
    ("lb_cia_k_2026_lock_unknown", "CIA Kunsten 2026 MJP lock euros unpublished", "187524", "7.0", "4.0", "3.0"),
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
            "tco_notes": "AG CIA Kunsten JR2025 podium/Arenberg Entity II Antwerpen; BBC/NBB PDF internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Antwerp residents / Arenberg / Groep Antwerpen podium",
            "stated_goal": "Local dual residual AGB map VL JR2025 performing-arts vehicle",
            "measured_outcome": "assets 6.090m / BBR 2.757m / AFM 0.418m / PnL 0.257m / city dual 0.188m drop vs 2023 0.716m / PDF opaque",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish BBC+NBB PDFs + explain 0.53m city dual drop vs 2.76m BBR FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary RVB+CBS HTML; not TE-additive without city GE; cash/fin debt/VTE unknown",
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
                "BBC+NBB JR2025 PDFs (AG CIA K_JR25_final BBC.pdf + venn B.pdf on "
                "2026_RVBKUNSTEN_00010 / 2026_GR_00637) working URL + J2/J4/J5/T2-T4 + NBB "
                "(cash, fin debt, EV, omzet, personnel/VTE, expl/invest/fin); "
                "city dual cash vs vastlegging 0.187524; motiv typo 0.705354 vs art1 0.187524; "
                "city werk drop 0.715984 (2023) to 0.187524 (2025) = 0.528460; "
                "restmiddelen exact vs BBR 2.756636; 2026-2031 city lock"
            ),
            "why_it_matters": (
                "Remaining Antwerp Entity II after Zorgbedrijf / Vespa / AGSO / CIA Erfgoed: "
                "tiny city dual 0.19m after 74% cut from 0.72m (2023) while BBR sits at 2.76m "
                "and assets 6.09m; BBC+NBB JR2025 exist and were approved 22/29.06.2026 but "
                "PDFs not retrievable (ebesluit TLS / NBB 403); 2026 lock unpublished"
            ),
            "priority": "8",
            "recipient_body": "AG CIA Kunsten / Stad Antwerpen",
            "recipient_email": "AG_Culturele_Instellingen@antwerpen.be",
            "recipient_postal": "Grote Markt 1 2000 Antwerpen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_cia_k_city_dual_0_19m_2025",
            "linked_leaderboard_id": "lb_cia_k_dual_drop_0_53m_2023_25",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1263",
    "title": "AG CIA Kunsten Antwerpen JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AG CIA Kunsten RVB 00010 BBC totals + city dual CBS 07873; "
        "KBO 0738.734.281 BBC+NBB; assets 6.090m BBR 2.757m AFM 0.418m city dual 0.188m; "
        "PDFs opaque"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T08:05:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1263 AG CIA Kunsten JR2025 dual residual; KBO 0738.734.281 BBC+NBB; "
        "assets 6.090m BBR=avail 2.757m AFM=gecorr 0.418m PnL 0.257m; "
        "city dual werk 0.188m invest 0 drop vs 2023 0.716m = 0.528m; "
        "PDFs opaque ebesluit TLS; FOI ready not sent; next rq_1264 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1264",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg not yet mined "
        "(Gent dual AGB cluster 1255-1259 + AG Vespa 1260 + AGSO 1261 + AG CIA Erfgoed 1262 "
        "+ AG CIA Kunsten 1263 done; prefer AG Energiebesparingsfonds Antwerpen JR2025 or "
        "other unmined AGB/zorg with direct PDF; WAGSO Waregem already mined tick1199; "
        "skip Mobil-O/AG EOS inactive; skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden "
        "/ Zorgbedrijf Brasschaat unpublished; ebesluit TLS — prefer org sites / NBB / city HTML)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1263 after AG CIA Kunsten JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1263", rq_new, rq_spawn)
print("research_queue 1263", found, "spawned_1264", spawned)

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
            "last_unit_id": "rq_1263",
            "ticks_completed": "1263",
            "paused": "no",
            "notes": (
                "tick1263 AG CIA Kunsten JR2025 dual residual; KBO 0738.734.281 BBC+NBB; "
                "assets 6.090m BBR=avail 2.757m AFM=gecorr 0.418m PnL 0.257m; "
                "city dual werk 0.188m invest 0 drop vs 2023 0.716m; PDFs opaque; FOI ready; "
                "next rq_1264 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1263 - 2026-08-17 - rq_1263 AG CIA Kunsten dual residual
- Unit: AG Culturele Instellingen Antwerpen/Kunsten JR2025 Entity II after city package + sibling AG CIA Erfgoed tick1262 (KBO 0738.734.281; BBC+NBB; RVB 22.06.2026 `2026_RVBKUNSTEN_00010` / GR 29.06.2026 `2026_GR_00637`). Distinct from Gent AGB cluster 1255–1259 and from sibling AG CIA Erfgoed (0738.733.786). Seat Grote Markt 1; venues Arenbergstraat 28 + Turnhoutsebaan 246. WAGSO already mined tick1199.
- EUR strong (RVB HTML BBC totals + city dual HTML; PDF internals unknown): assets **6.090m**; BBR = avail **2.757m**; AFM = gecorr **0.418m**; PnL **0.257m**; city werk **0.188m** (podium **0.088m** + events **0.100m**) + invest **0** = dual **0.188m**; city werk drop vs 2023 **0.716m** = **0.528m** (~74%). Motiv typo 0.705m ignored (table+art1=0.188m). Restmiddelen provisioned, exact TBD. BBC+NBB PDFs named (`AG CIA K_JR25_final BBC.pdf` + `venn B.pdf`) but ebesluit TLS + NBB 403.
- CSVs: sources+5/entities(new+city note)/budgets+14/commitments+7/leaderboard+7 + FOI ready `gap_cia_k_jr2025_pdf_opaque_city_dual_0_19m_bbr_2_76m_l5` (not sent); rq_1263=done; spawn rq_1264; ticks=1263. No every-10 (1263 not a *0 tick).
- Next: rq_1264 residual dual L5 VL JR2025 hole_fill (prefer AG Energiebesparingsfonds Antwerpen JR2025 or other unmined AGB/zorg with direct PDF).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")

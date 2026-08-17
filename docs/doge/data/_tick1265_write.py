# -*- coding: utf-8 -*-
"""Tick 1265 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AG Digipolis Antwerpen JR2025 dual residual (GR HTML BBC headlines + prior MJP/city dual; PDFs opaque)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T08:20:00Z"
TICK = 1265
SRC = "src_digipolis_jr2025_gr00616"
SRC2 = "src_digipolis_jr2024_gr00424"
SRC3 = "src_kbo_digipolis_0751541350"
ENT = "digipolis_antwerpen"
CITY = "city_antwerpen"
SRC_URL = "https://ebesluit.antwerpen.be/zittingen/25.0918.3949.0497/agendapunten/26.0504.9937.1986"
SRC2_URL = "https://ebesluit.antwerpen.be/zittingen/25.0113.9855.5071/agendapunten/25.0506.0538.7644"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0751541350"
GAP = "gap_digipolis_jr2025_pdf_opaque_assets_73_61m_surplus_0_11m_l5"
HIER = "Vlaanderen>Gemeenten>Antwerpen>AG_Digipolis"


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
            "title": "2026_GR_00616 AG Digipolis Antwerpen JR2025 advies/kwijting",
            "url": SRC_URL,
            "publisher": "Stad Antwerpen gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1265; GR 29.06.2026; RVB 29.04.2026; KBO 0751.541.350 BBC; "
                "assets 73.605124m surplus 0.109871m overgedragen; commissaris "
                "zonder voorbehoud financieel / niet-financieel in overeenstemming; "
                "BBC PDF opaque ebesluit TLS; NBB consult SPA/403"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2025_GR_00424 AG Digipolis Antwerpen JR2024 advies/kwijting",
            "url": SRC2_URL,
            "publisher": "Stad Antwerpen gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1265; GR JR2024; RVB 17.04.2025; assets 75.856194m deficit "
                "0.692714m; compare vs JR2025 asset drop 2.251070m surplus swing +0.802585m"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AG Digipolis Antwerpen 0751.541.350",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1265; AGB since 29.06.2020; seat Grote Markt 1 2000 since 29.10.2025; "
                "VE 2.309.779.836 Francis Wellesplein 1 2018 since 05.12.2025; "
                "info@digipolis.be + da_directiesecretariaat@digipolis.be; RSZ employer 2022; "
                "NACE 62.100/62.900; financials empty in KBO"
            ),
        },
    ],
)
print("sources", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    ENT,
    (
        "tick1265 JR2025 dual residual; KBO 0751.541.350 BBC; assets 73.605m "
        "surplus 0.110m vs 2024 assets 75.856m deficit 0.693m (drop 2.251m / "
        "swing +0.803m); member omzet 2025 221.900m / MJP 2026 245.610m; "
        "city 2025 75.201m+PZA 53.528m; PDFs opaque; FOI " + GAP
    ),
    extra_fields={
        "website": "https://www.digipolisantwerpen.be",
        "foi_email": "info@digipolis.be",
        "foi_postal": "Grote Markt 1 2000 Antwerpen / Francis Wellesplein 1 2018 Antwerpen",
    },
)
print("entity digipolis", ok)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "Digipolis dual residual tick1265 (KBO 0751.541.350; assets 73.605m / "
        "surplus 0.110m vs 2024 75.856m / -0.693m; member omzet 221.900m; PDF opaque)"
    ),
)
print("city_antwerpen notes", ok)

bud_rows = [
    ("bud_digipolis_assets_2025", "2025", 73605124, SRC, "executed", "GR 00616 balanstotaal 73.605124m"),
    ("bud_digipolis_surplus_2025", "2025", 109871, SRC, "executed", "GR 00616 overschot boekjaar 0.109871m overgedragen"),
    ("bud_digipolis_assets_2024", "2024", 75856194, SRC2, "executed", "GR 00424 balanstotaal 75.856194m"),
    ("bud_digipolis_deficit_2024", "2024", -692714, SRC2, "executed", "GR 00424 tekort boekjaar -0.692714m overgedragen"),
    ("bud_digipolis_assets_drop_2024_25", "2025", 2251070, SRC, "executed", "Assets 75.856194m (2024) to 73.605124m (2025) = drop 2.251070m"),
    ("bud_digipolis_surplus_swing_2024_25", "2025", 802585, SRC, "executed", "PnL -0.692714m (2024) to +0.109871m (2025) = swing +0.802585m"),
    ("bud_digipolis_bs_vs_member_omzet_2025", "2025", 148294484.67, SRC, "executed", "Member omzet 221.899609m minus BS 73.605124m = 148.294485m pass-through residual (not a cash gap)"),
    ("bud_digipolis_revisor_fee_2025", "2025", 12505, SRC, "budgeted", "Callens/Vandelanotte/Theunissen 12.505/year 2024-2026 (2024_GR_00536 path; already in HTML)"),
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
        "comm_digipolis_assets_73_61m_2025",
        "Digipolis JR2025 assets 73.605m",
        "73605124",
        "BBC headline GR 00616; drop 2.251m vs 2024 75.856m",
        "Publish J2/T2-T4 split FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_digipolis_surplus_0_11m_2025",
        "Digipolis JR2025 surplus 0.110m overgedragen",
        "109871",
        "Vs 2024 deficit 0.693m; swing +0.803m on ~222m member omzet",
        "J4/J5 expl/invest/fin + why thin surplus FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_digipolis_surplus_swing_0_80m_2024_25",
        "Digipolis PnL -0.693m (2024) to +0.110m (2025) swing 0.803m",
        "802585",
        "GR 00424 vs GR 00616; cost-sharing vehicle designed near-zero",
        "What reversed the 2024 deficit FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_digipolis_bs_vs_omzet_221_9m_2025",
        "Digipolis BS 73.61m vs member omzet 221.90m 2025",
        "221899608.67",
        "Pass-through AGB; city+PZA lock 128.73m is partial; MJP 2026 245.61m",
        "Reconcile omzet outturn vs markup annex + cash/fin debt FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_digipolis_bbc_opaque_jr2025",
        "Digipolis BBC+NBB JR2025 PDFs not retrieved",
        "",
        "GR 00616 bijlagen + RVB 29.04.2026; ebesluit TLS / NBB 403 / org site empty",
        "Publish working PDFs + J2/J4/J5/T2-T4 FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_digipolis_cbs_jr2025_unknown",
        "Digipolis CBS 2026 college analog JR2025 unpublished in HTML",
        "",
        "2024 analog 2025_CBS_03534 public; 2026 CBS kennisneming not found",
        "Publish CBS 2026 kennisneming + extra BBC totals FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_digipolis_city_lock_vs_recharge_2025_26",
        "Digipolis city lock 75.20m (2025) / 38.81m (2026) vs stad recharge 138.02m",
        "138020830.69",
        "Already mapped ticks 213/226; JR2025 cash vs lock still unpublished",
        "2025 cash gestort vs vastlegging + 2026 personnel residual FOI",
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
            "beneficiary": "AG Digipolis Antwerpen / Groep stad Antwerpen ICT members",
            "legal_basis": "2026_GR_00616 + 2025_GR_00424 + MJP 2026-2031 + kostendelende vereniging",
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
            "notes": f"tick{TICK}; primary GR+KBO HTML; BBC/NBB PDF opaque; distinct District09 Gent",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_digipolis_assets_73_61m_2025", "Digipolis JR2025 assets 73.61m (drop 2.25m vs 2024)", "73605124", "6.5", "8.0", "3.0"),
    ("lb_digipolis_surplus_0_11m_vs_omzet_221_9m_2025", "Digipolis surplus 0.11m on member omzet 221.90m", "109871", "7.5", "7.0", "3.0"),
    ("lb_digipolis_surplus_swing_0_80m_2024_25", "Digipolis PnL -0.69m (2024) to +0.11m (2025) swing 0.80m", "802585", "6.5", "5.5", "3.0"),
    ("lb_digipolis_bs_vs_member_omzet_221_9m_2025", "Digipolis BS 73.61m vs member omzet 221.90m pass-through", "221899608.67", "8.0", "9.0", "3.0"),
    ("lb_digipolis_bbc_opaque_jr2025", "Digipolis BBC JR2025 PDFs not retrieved, schema unpublished", "73605124", "7.5", "8.0", "3.0"),
    ("lb_digipolis_cbs_jr2025_unknown", "Digipolis CBS 2026 college analog JR2025 unpublished", "73605124", "6.5", "6.0", "3.0"),
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
            "tco_notes": "AG Digipolis Antwerpen JR2025 ICT cost-sharing Entity II; distinct District09 Gent; BBC/NBB PDF internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Groep stad Antwerpen / PZA / AGSO / other members",
            "stated_goal": "Local dual residual AGB map VL JR2025 municipal ICT vehicle",
            "measured_outcome": "assets 73.605m / surplus 0.110m / vs 2024 75.856m -0.693m / member omzet 221.900m / PDF opaque",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish BBC+NBB PDFs + reconcile 73.61m BS vs 221.90m omzet + 0.11m surplus FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary GR+KBO HTML; not TE-additive without city GE; cash/fin debt/VTE/BBR/AFM unknown",
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
                "BBC+NBB JR2025 PDFs (GR 2026_GR_00616 / RVB 29.04.2026) working URL + "
                "J2/J4/J5/T2-T4 + NBB (AFM, BBR year/cum, cash, fin debt 31.12.2025, EV, "
                "omzet outturn vs member 221.899609m, personnel/VTE vs MJP 45.458m, "
                "expl/invest/fin); CBS 2026 college analog of 2025_CBS_03534; why BS "
                "73.605124m beside member omzet 221.899609m; why surplus 0.109871m after "
                "2024 deficit 0.692714m; city 2025 cash vs lock 75.201407+53.527674"
            ),
            "why_it_matters": (
                "Largest remaining Antwerp Entity II ICT vehicle after Zorgbedrijf / Vespa / "
                "AGSO / CIA / EBF: member omzet 221.90m and MJP 245.61m sit beside a "
                "73.61m balance sheet and 0.11m surplus; city lock 75.20m (2025) / 38.81m "
                "(2026) is only a slice of stad recharge 138.02m; BBC JR2025 approved "
                "29.06.2026 but PDFs not retrievable (ebesluit TLS / NBB 403 / org site empty). "
                "Distinct from District09 Gent."
            ),
            "priority": "8",
            "recipient_body": "AG Digipolis Antwerpen / Stad Antwerpen",
            "recipient_email": "info@digipolis.be",
            "recipient_postal": "Grote Markt 1 2000 Antwerpen / Francis Wellesplein 1 2018 Antwerpen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_digipolis_bs_vs_omzet_221_9m_2025",
            "linked_leaderboard_id": "lb_digipolis_bs_vs_member_omzet_221_9m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1265",
    "title": "AG Digipolis Antwerpen JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AG Digipolis GR 00616 BBC headlines + JR2024 compare + KBO; "
        "KBO 0751.541.350 BBC; assets 73.605m surplus 0.110m vs 2024 75.856m / -0.693m; "
        "member omzet 221.900m; PDFs opaque"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T08:15:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1265 AG Digipolis JR2025 dual residual; KBO 0751.541.350 BBC; "
        "assets 73.605m surplus 0.110m vs 2024 assets 75.856m deficit 0.693m "
        "= drop 2.251m / swing +0.803m; member omzet 2025 221.900m / MJP 2026 245.610m; "
        "city 2025 75.201m+PZA 53.528m; PDFs opaque ebesluit TLS + NBB 403; FOI ready "
        "not sent; distinct District09 Gent; next rq_1266 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1266",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(Gent dual AGB cluster 1255-1259 + AG Vespa 1260 + AGSO 1261 + AG CIA Erfgoed 1262 "
        "+ AG CIA Kunsten 1263 + AG Energiebesparingsfonds 1264 + AG Digipolis Antwerpen 1265 "
        "done; prefer vzw Integratie & Inburgering Antwerpen / Atlas JR2025 GR 2026_GR_00622 "
        "KBO 0421.722.346 or other unmined AGB/zorg with direct PDF/NBB; WAGSO Waregem already "
        "mined tick1199; skip Mobil-O/AG EOS inactive; skip Woonzorgnetwerk Edegem / "
        "Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat unpublished; ebesluit TLS — "
        "prefer org sites / NBB / city HTML)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1265 after AG Digipolis JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1265", rq_new, rq_spawn)
print("research_queue 1265", found, "spawned_1266", spawned)

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
            "last_unit_id": "rq_1265",
            "ticks_completed": "1265",
            "paused": "no",
            "notes": (
                "tick1265 AG Digipolis Antwerpen JR2025 dual residual; KBO 0751.541.350 BBC; "
                "assets 73.605m surplus 0.110m vs 2024 75.856m / -0.693m; member omzet 221.900m; "
                "PDFs opaque; FOI ready; next rq_1266 residual dual L5 VL "
                "(prefer Atlas/Integratie JR2025); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1265 - 2026-08-17 - rq_1265 AG Digipolis Antwerpen dual residual
- Unit: AG Digipolis Antwerpen JR2025 Entity II ICT cost-sharing AGB after EBF tick1264 (KBO 0751.541.350; BBC; RVB 29.04.2026 / GR 29.06.2026 `2026_GR_00616`). **Distinct from AGB District09 Gent** (KBO 0749.998.654, tick1258). Seat Grote Markt 1, 2000 Antwerpen; vestiging Francis Wellesplein 1, 2018 Antwerpen (VE 2.309.779.836). Ticks 213/225/226 already had MJP 245.610m / member omzet / city+PZA locks. WAGSO already mined tick1199.
- EUR strong (GR HTML BBC headlines + prior MJP/city dual; PDF internals unknown): assets **73.605m** (was **75.856m**, drop **2.251m**); surplus **0.110m** (vs 2024 deficit **0.693m**, swing **+0.803m**); member omzet 2025 **221.900m** / MJP 2026 **245.610m**; city 2025 package **75.201m** + PZA **53.528m** = dual **128.729m**; city 2026 lock **38.814m** vs stad recharge **138.021m**. BBC/NBB PDFs not retrieved (ebesluit TLS + NBB 403 + org site empty). CBS 2026 college analog not found.
- CSVs: sources+3/entities(patch+city note)/budgets+8/commitments+7/leaderboard+6 + FOI ready `gap_digipolis_jr2025_pdf_opaque_assets_73_61m_surplus_0_11m_l5` (not sent); rq_1265=done; spawn rq_1266; ticks=1265. No every-10 (1265 not a *0 tick).
- Next: rq_1266 residual dual L5 VL JR2025 hole_fill (prefer vzw Integratie & Inburgering Antwerpen / Atlas JR2025 GR 2026_GR_00622 KBO 0421.722.346 or other unmined AGB/zorg with direct PDF).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")

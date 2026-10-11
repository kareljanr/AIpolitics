# -*- coding: utf-8 -*-
"""Tick 1318 — surgical append/patch only. APB GKC JR2025 leftover APB residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1318"
UTC = "2026-08-17T18:05:00Z"
ENT = "apb_gkc"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>GKC"
GAP = "gap_gkc_st_recv_526k_dotatie_50k_l5"
SRC = "src_gkc_jr2025_pdf"
SRC2 = "src_gkc_jaarverslag_2025"
SRC3 = "src_kbo_gkc_0684472976"
SRC4 = "src_gkc_foi_page"
SRC_URL = "https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/20500/2025-apb_gkc.ed391ce32b71.pdf"
SRC2_URL = "https://publicaties.provincieantwerpen.be/gouverneur-kinsbergencentrum-jaarverslag-2025/in-cijfers"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0684472976"
SRC4_URL = "https://www.provincieantwerpen.be/nl/provinciebestuur/werking-provincie/provinciegriffier/inzagerecht"
FOI_EMAIL = "openbaarheid@provincieantwerpen.be"
FOI_POSTAL = "Koningin Elisabethlei 22 2018 Antwerpen"
DRAFT = "docs/doge/foi/drafts/gap_gkc_st_recv_526k_dotatie_50k_l5.md"


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


def patch_last_rq_and_spawn(path, target_id, new_target, spawn_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    with path.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        chunk = min(size, 131072)
        f.seek(size - chunk)
        tail = f.read()
    if tail.endswith(b"\n"):
        search = tail[:-1]
    else:
        search = tail
    last_nl = search.rfind(b"\n")
    last_line = search[last_nl + 1 :] if last_nl != -1 else search
    last_text = last_line.decode("utf-8")
    if not last_text.startswith(target_id + ","):
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:160]))
    last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
    spawn_id = spawn_row.get("task_id")
    if spawn_id and spawn_id.encode("utf-8") in tail:
        raise SystemExit("spawn id already in tail")
    payload = (csv_line(fields, new_target) + "\n" + csv_line(fields, spawn_row) + "\n").encode("utf-8")
    with path.open("r+b") as f:
        f.seek(last_start)
        f.truncate()
        f.write(payload)
    return True, True


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "APB GKC jaarrekening 2025 (official BBC text PDF)",
            "url": SRC_URL,
            "publisher": "APB GKC / Provincie Antwerpen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1318; Foleon BBC text PDF 0.80MB print 31.03.2026 volgnr 416856; "
                "KBO 0684.472.976; assets 2666888.01 cash 2105179.73 ST recv 526229.54 "
                "ST pay 574019.21 BBR +88733.74 AFM +88733.74 PnL +148210.12; primary BBC text"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Gouverneur Kinsbergencentrum jaarverslag 2025 in cijfers (official Foleon link)",
            "url": SRC2_URL,
            "publisher": "Provincie Antwerpen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1318; publicaties.provincieantwerpen.be/gouverneur-kinsbergencentrum-jaarverslag-2025/in-cijfers "
                "links the same BBC PDF; leftover sister APB of mined provincie Antwerpen"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO APB GKC 0684.472.976",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1318; KBO 0684.472.976 actief APB since 07.11.2017; zetel Koningin "
                "Elisabethlei 22 2018 since 01.07.2026; 1 VE; bestuurder Luk Lemmens since "
                "02.12.2024; NACE 88.105; RSZ since 01.01.2022; scarlett.deurinck@provincieantwerpen.be; no KBO finance"
            ),
        },
        {
            "source_id": SRC4,
            "title": "Provincie Antwerpen openbaarheid van bestuur (FOI channel)",
            "url": SRC4_URL,
            "publisher": "Provincie Antwerpen",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1318; FOI openbaarheid@provincieantwerpen.be / provinciegriffier; "
                "Koningin Elisabethlei 22 2018"
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
            "name_nl": "APB Gouverneur Kinsbergen Centrum (APB GKC)",
            "name_fr": "APB Centre Gouverneur Kinsbergen",
            "name_en": "APB Governor Kinsbergen Centre",
            "level": "apb",
            "parent_id": "prov_antwerpen",
            "community_language": "nl",
            "website": "https://publicaties.provincieantwerpen.be/gouverneur-kinsbergencentrum-jaarverslag-2025",
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1318 JR2025 leftover sister APB residual; KBO 0684.472.976; assets 2666888 "
                "fin debt 0 ST recv 526230 ST pay 574019 BBR +88734 AFM +88734 "
                "PnL +148210 cash 2105180 equity 2092869; FOI ready"
            ),
        },
    ],
)
print("entities", n)

budget_rows = [
    ("bud_gkc_assets_2025", "2025", "2666888", "YE2025 assets 2666888.01 was 2949095.80 DROP; tick1318; primary BBC J4"),
    ("bud_gkc_assets_2024", "2024", "2949096", "YE2024 assets 2949095.80; tick1318; primary BBC J4"),
    ("bud_gkc_cash_2025", "2025", "2105180", "YE2025 cash 2105179.73 was 2327580.27 DROP; tick1318; primary BBC J4"),
    ("bud_gkc_cash_2024", "2024", "2327580", "YE2024 cash 2327580.27; tick1318; primary BBC J4"),
    ("bud_gkc_current_2025", "2025", "2666888", "YE2025 vlottende activa 2666888.01 ALL current; tick1318; primary BBC J4"),
    ("bud_gkc_recv_st_2025", "2025", "526230", "YE2025 ST recv 526229.54 (ruil 20799.70 + niet-ruil 505429.84); tick1318; primary BBC J4"),
    ("bud_gkc_recv_nietruil_2025", "2025", "505430", "YE2025 ST niet-ruil recv 505429.84; tick1318; primary BBC J4"),
    ("bud_gkc_recv_ruil_2025", "2025", "20800", "YE2025 ST ruil recv 20799.70; tick1318; primary BBC J4"),
    ("bud_gkc_fixed_2025", "2025", "0", "YE2025 vaste activa 0 (FVA/MVA/IVA/leasing 0); tick1318; primary BBC J4/T5"),
    ("bud_gkc_schulden_2025", "2025", "574019", "YE2025 schulden 574019.21 ALL ST was 1004437.12; tick1318; primary BBC J4"),
    ("bud_gkc_pay_ruil_2025", "2025", "132065", "YE2025 non-fin ST ruil pay 132065.03 was 441441.31; tick1318; primary BBC J4"),
    ("bud_gkc_accruals_2025", "2025", "441954", "YE2025 overlopend passief 441954.18; tick1318; primary BBC J4"),
    ("bud_gkc_fin_debt_2025", "2025", "0", "YE2025 T4 fin debt 0; no new loans no afl; tick1318; primary BBC T4"),
    ("bud_gkc_equity_2025", "2025", "2092869", "YE2025 nettoactief 2092868.80 was 1944658.68; tick1318; primary BBC J4/T5"),
    ("bud_gkc_cum_pnl_2025", "2025", "2092869", "YE2025 gecumuleerd overschot 2092868.80 was 1944658.68; tick1318; primary BBC J4/T5"),
    ("bud_gkc_pnl_2025", "2025", "148210", "2025 J5 PnL +148210.12 (ops +129507.40 / fin +18702.72); tick1318; primary BBC J5"),
    ("bud_gkc_expl_saldo_2025", "2025", "88734", "2025 expl saldo +88733.74 (ontv 1400129.82 / uitg 1311396.08); tick1318; primary BBC J2"),
    ("bud_gkc_expl_ontv_2025", "2025", "1400130", "2025 expl ontv 1400129.82; tick1318; primary BBC J2"),
    ("bud_gkc_expl_uitg_2025", "2025", "1311396", "2025 expl uitg 1311396.08; tick1318; primary BBC J2"),
    ("bud_gkc_bbr_2025", "2025", "88734", "2025 BBR year +88733.74; tick1318; primary BBC J2"),
    ("bud_gkc_cum_bbr_2025", "2025", "2499344", "YE2025 cum BBR 2499344.24 was 2410610.50; tick1318; primary BBC J2"),
    ("bud_gkc_afm_2025", "2025", "88734", "2025 AFM +88733.74 = gecorr AFM; no afl; tick1318; primary BBC J2"),
    ("bud_gkc_pers_2025", "2025", "886607", "2025 J5 pers 886606.91 / T2 cash 884785.31; VTE unpublished FOI; tick1318; primary BBC"),
    ("bud_gkc_goods_2025", "2025", "487258", "2025 J5 goederen/diensten 487258.48 / T2 426253.57; tick1318; primary BBC"),
    ("bud_gkc_werksub_out_2025", "2025", "0", "2025 toegestane werksub 0 was 372000.00 DROP; tick1318; primary BBC J5/T2"),
    ("bud_gkc_werksub_in_2025", "2025", "1185753", "2025 J5 werksub ontv 1185752.50 (alg 776006.00 + spec 409746.50); tick1318; primary BBC J5"),
    ("bud_gkc_werksub_prov_2025", "2025", "726006", "2025 T2 alg werksub van de provincie 726006.00 vs J5 alg 776006.00; tick1318; primary BBC T2"),
    ("bud_gkc_other_ops_2025", "2025", "298979", "2025 J5 andere operationele opbrengsten 298979.23; tick1318; primary BBC J5"),
    ("bud_gkc_fin_inc_2025", "2025", "18967", "2025 J5 financiele opbrengsten 18967.22; tick1318; primary BBC J5"),
    ("bud_gkc_costs_2025", "2025", "1374130", "2025 J5 costs 1374129.89; tick1318; primary BBC J5"),
    ("bud_gkc_rev_2025", "2025", "1522340", "2025 J5 opbrengsten 1522340.01; tick1318; primary BBC J5"),
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
            "basis": "executed",
            "source_id": SRC,
            "confidence": "strong",
            "notes": notes,
        }
        for bid, year, amt, notes in budget_rows
    ],
)
print("budgets", n)

n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "comm_gkc_jr2025_dual",
            "title": "APB GKC JR2025 leftover APB dual (cash 2.11m / ST recv 526k / provincie T2 726k vs J5 776k)",
            "entity_id": ENT,
            "beneficiary": "zorg/welzijn education projects + provincie Antwerpen dual",
            "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid",
            "decision_date": "",
            "start_year": "2025",
            "end_year": "2029",
            "total_envelope_eur": "2666888",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Provincial zorg-arbeidsmarkt expertise centre (anders leren / anders werken)",
            "cut_option": "Publish named ST recv ledger + dual provincie dotatie recon + VTE + Fabcom/Capable envelopes; shrink leftover APB if intra-group",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": "tick1318; assets 2666888 ST recv 526230 ST pay 574019 BBR +88734 AFM +88734 PnL +148210; FOI ready not sent",
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_gkc_cash_2_11m_recv_526k_dotatie_50k",
            "name": "APB GKC JR2025 leftover APB: 2.67m assets / 2.11m cash / 526k ST recv / provincie J5 776k vs T2 726k",
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": "1311396",
            "total_cost_eur": "2666888",
            "tco_notes": "Leftover dual APB shell: assets 2.67m / cash 2.11m / equity 2.09m; expl uitg 1.31m; do not treat 2.67m as TE-additive of 348bn",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "zorg/welzijn education projects + provincie Antwerpen dual",
            "stated_goal": "Provincial zorg-arbeidsmarkt expertise centre",
            "measured_outcome": "Official BBC PDF 2026-08-17: BBR +88.7k / AFM +88.7k / PnL +148.2k; cash 2.11m; VTE unpublished; J5 vs T2 provincie 50k gap",
            "absurdity_score": "5.5",
            "cost_score": "4.5",
            "difficulty": "3.0",
            "priority_index": "5.2",
            "cut_proposal": "Publish named ST recv + dual provincie dotatie recon; shrink leftover APB if intra-group",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1318; leftover sister APB of mined provincie Antwerpen; FOI ready not sent; not TE-additive of 348bn",
        }
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
                "Named counterparties behind ST recv 526229.54 (niet-ruil 505429.84 + ruil 20799.70) "
                "and ST non-fin ruil pay 132065.03 + recon dual provincie dotatie J5 alg 776006.00 vs "
                "T2 726006.00 (50k) and J5 werksub 1185752.50 vs T2 1060603.57 + named other-ops "
                "298979.23 + VTE behind pers 886606.91 + Fabcom/Capable envelopes + provincieraad "
                "vaststelling JR2025 + NBB non-filing legal basis"
            ),
            "why_it_matters": (
                "Leftover unmapped sister APB of already-mined provincie Antwerpen after honest residual "
                "dual hunt (PSES 1317 done). KBO 0684.472.976 active. Official BBC PDF now downloads (Foleon). "
                "2.67m leftover APB shell with 2.11m cash and 50k J5/T2 provincie mismatch. Sister leftover "
                "APB Havencentrum/KampC PDFs also live. Do not invent euros."
            ),
            "priority": "7",
            "recipient_body": "APB GKC / Provincie Antwerpen / provinciegriffier",
            "recipient_email": FOI_EMAIL,
            "recipient_postal": FOI_POSTAL,
            "draft_letter_path": DRAFT,
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_gkc_jr2025_dual",
            "linked_leaderboard_id": "lb_gkc_cash_2_11m_recv_526k_dotatie_50k",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1318",
    "title": "APB GKC JR2025 dual residual leftover APB",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: APB GKC JR2025 leftover sister APB after honest hunt; KBO 0684.472.976; "
        "official BBC PDF downloads; assets 2.67m / cash 2.11m / ST recv 526k / "
        "BBR +88.7k / AFM +88.7k / PnL +148.2k; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T17:50:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1318 APB GKC JR2025 leftover sister APB residual; KBO 0684.472.976; "
        "assets 2666888 ST recv 526230 ST pay 574019 BBR +88734 AFM +88734 "
        "PnL +148210; FOI ready not sent; next rq_1319 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1319",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1318 done including APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB / "
        "Stad+OCMW Ranst 1316 FOI-unpublished / Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 "
        "FOI-unpublished / AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / "
        "AGB Maaseik 1311 / APB VERA 1310); prefer other unmined AGB/zorg/EVA with direct "
        "PDF (sister leftover APB Havencentrum / KampC JR2025 Foleon PDFs now live — "
        "take if still unmined; AGB Blankenberge only if a PDF actually downloads); "
        "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
        "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
        "skip already-mined APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 "
        "(FOI TLS) / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / "
        "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
        "Ternat / Oostkamp / Wetteren / Poperinge / Haacht / Bilzen-Hoeselt / AGB Sport Geel / Zwevegem; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
        "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); not every-10"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1318 after APB GKC JR2025 leftover sister APB; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1318", rq_new, rq_spawn)
print("research_queue 1318", found, "spawned_1319", spawned)

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
        lineterminator="\r\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_1318",
            "ticks_completed": "1318",
            "paused": "no",
            "notes": (
                "tick1318 APB GKC JR2025 leftover sister APB residual; KBO 0684.472.976; "
                "assets 2.67m cash 2.11m ST recv 526k ST pay 574k BBR +88.7k AFM +88.7k PnL +148.2k; "
                "FOI ready; next rq_1319 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1318 - 2026-08-17 - rq_1318 APB GKC dual residual leftover sister APB
- Unit: APB Gouverneur Kinsbergen Centrum (APB GKC) JR2025 leftover sister APB/EVA of already-mined provincie Antwerpen after residual dual hunt (KBO **0684.472.976**; official BBC text PDF on Foleon 25p / 0.80MB; print **31.03.2026**; volgnr **416856**; Jnl. via CSrapportaal). PREFER leftover sister APBs of provincie Antwerpen whose Foleon JR2025 PDFs are already known live from tick 1317: first unmined of APB GKC / Havencentrum / KampC. Distinct from already-mined APB PSES 1317 / APB VERA 1310 / Westtoer / APB Mercator. Operational seat Doornstraat 331 2610 Wilrijk; KBO zetel Koningin Elisabethlei 22 2018 since 01.07.2026. Bestuurder Luk Lemmens since 02.12.2024. NACE 88.105; RSZ-werkgever; 1 VE; scarlett.deurinck@provincieantwerpen.be. APB states not an onderneming — no NBB filing. Hunt leftover AGB first: AGB Blankenberge official still **JR2019-only** (unmined, no JR2025 PDF); AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek still no fetchable JR2025. Sister leftover APB **Havencentrum / KampC** JR2025 Foleon PDFs also live — left for later. provincieantwerpen.be 403 from this box (Foleon OK). Skip already-mined PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **2.666.888,01** (was 2.949.095,80) DROP; cash **2.105.179,73** vs 2.327.580,27 DROP; ST recv **526.229,54** (ruil **20.799,70** + niet-ruil **505.429,84**); fixed **0**; FVA **0**; MVA/leasing **0**; schulden **574.019,21** ALL ST; fin debt T4 **0**; non-fin ST ruil pay **132.065,03**; accruals **441.954,18**; equity **2.092.868,80**; cum surplus **2.092.868,80**; expl **+88.733,74** (ontv **1.400.129,82** / uitg **1.311.396,08**); invest **0**; fin **0**; BBR year **+88.733,74**; cum BBR **2.499.344,24**; AFM/gecorr **+88.733,74**; PnL **+148.210,12**; pers J5 **886.606,91**; werksub granted **0** DROP vs 372.000,00; werksub received J5 **1.185.752,50** (provincie T2 alg **726.006,00** vs J5 alg **776.006,00**); other ops **298.979,23**. VTE unpublished. Fabcom 2025–2029 / Capable 2025–2028.
- CSVs: sources+4/entities+1/budgets+31/commitments+1/leaderboard+1 + FOI ready `gap_gkc_st_recv_526k_dotatie_50k_l5` (not sent); rq_1318=done; spawn rq_1319; ticks=1318. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB GKC leftover sister APB). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1319 residual dual L5 VL JR2025 hole_fill (prefer sister leftover APB Havencentrum / KampC JR2025 Foleon PDFs now live; leftover AGB Blankenberge only if a PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB GKC 1318 / APB PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1318 write done")

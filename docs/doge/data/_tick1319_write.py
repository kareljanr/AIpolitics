# -*- coding: utf-8 -*-
"""Tick 1319 — surgical append/patch only. APB Havencentrum JR2025 leftover APB residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1319"
UTC = "2026-08-17T18:20:00Z"
ENT = "apb_hc"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>Havencentrum"
GAP = "gap_hc_st_recv_609k_havenwereld_395k_l5"
SRC = "src_hc_jr2025_pdf"
SRC2 = "src_hc_jaarverslag_2025"
SRC3 = "src_kbo_hc_0443423820"
SRC4 = "src_hc_foi_page"
SRC_URL = "https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/20500/2025-apb_hc.21071b4dad22.pdf"
SRC2_URL = "https://publicaties.provincieantwerpen.be/havencentrum-jaarverslag-2025/in-cijfers"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0443423820"
SRC4_URL = "https://www.provincieantwerpen.be/nl/provinciebestuur/werking-provincie/provinciegriffier/inzagerecht"
FOI_EMAIL = "openbaarheid@provincieantwerpen.be"
FOI_POSTAL = "Koningin Elisabethlei 22 2018 Antwerpen"
DRAFT = "docs/doge/foi/drafts/gap_hc_st_recv_609k_havenwereld_395k_l5.md"


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
            "title": "APB Havencentrum jaarrekening 2025 (official BBC text PDF)",
            "url": SRC_URL,
            "publisher": "APB Havencentrum / Provincie Antwerpen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1319; Foleon BBC text PDF 0.79MB print 31.03.2026 volgnr 1065115; "
                "KBO 0443.423.820; assets 973939.17 cash 364168.68 ST recv 609360.19 "
                "ST pay 230034.17 BBR +178173.31 AFM +178173.31 PnL +70226.07; primary BBC text"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Havencentrum jaarverslag 2025 in cijfers (official Foleon link)",
            "url": SRC2_URL,
            "publisher": "Provincie Antwerpen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1319; publicaties.provincieantwerpen.be/havencentrum-jaarverslag-2025/in-cijfers "
                "links the same BBC PDF; leftover sister APB of mined provincie Antwerpen"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO APB Havencentrum 0443.423.820",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1319; KBO 0443.423.820 actief APB since 01.01.2014 start 13.12.1990; "
                "zetel Koningin Elisabethlei 22 2018 since 15.06.2023; VE 2.159.573.554 "
                "Scheldelaan 444 2040 since 16.05.2008; bestuurder Luk Lemmens since "
                "15.12.2021; aanbestedende overheid; 1 VE; no KBO e-mail/NACE/finance"
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
                "tick1319; FOI openbaarheid@provincieantwerpen.be / provinciegriffier; "
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
            "name_nl": "APB Havencentrum",
            "name_fr": "APB Centre portuaire",
            "name_en": "APB Port Centre (Havencentrum / Havenwereld)",
            "level": "apb",
            "parent_id": "prov_antwerpen",
            "community_language": "nl",
            "website": "https://publicaties.provincieantwerpen.be/havencentrum-jaarverslag-2025",
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1319 JR2025 leftover sister APB residual; KBO 0443.423.820; assets 973939 "
                "fin debt 0 ST recv 609360 ST pay 230034 BBR +178173 AFM +178173 "
                "PnL +70226 cash 364169 equity 743905; FOI ready"
            ),
        },
    ],
)
print("entities", n)

budget_rows = [
    ("bud_hc_assets_2025", "2025", "973939", "YE2025 assets 973939.17 was 969517.26; tick1319; primary BBC J4"),
    ("bud_hc_assets_2024", "2024", "969517", "YE2024 assets 969517.26; tick1319; primary BBC J4"),
    ("bud_hc_cash_2025", "2025", "364169", "YE2025 cash 364168.68 was 610559.33 DROP; tick1319; primary BBC J4"),
    ("bud_hc_cash_2024", "2024", "610559", "YE2024 cash 610559.33; tick1319; primary BBC J4"),
    ("bud_hc_current_2025", "2025", "973790", "YE2025 vlottende activa 973790.43; tick1319; primary BBC J4"),
    ("bud_hc_recv_st_2025", "2025", "609360", "YE2025 ST recv 609360.19 (ruil 400926.48 + niet-ruil 208433.71) was 237919.59; tick1319; primary BBC J4"),
    ("bud_hc_recv_nietruil_2025", "2025", "208434", "YE2025 ST niet-ruil recv 208433.71; tick1319; primary BBC J4"),
    ("bud_hc_recv_ruil_2025", "2025", "400926", "YE2025 ST ruil recv 400926.48 was 101919.58; tick1319; primary BBC J4"),
    ("bud_hc_fixed_2025", "2025", "149", "YE2025 vaste activa 148.74 was 136635.09; tick1319; primary BBC J4/T5"),
    ("bud_hc_fva_2025", "2025", "149", "YE2025 FVA 148.74 andere; MVA/IVA 0; tick1319; primary BBC J4/T5"),
    ("bud_hc_schulden_2025", "2025", "230034", "YE2025 schulden 230034.17 ALL ST was 295838.33; tick1319; primary BBC J4"),
    ("bud_hc_pay_ruil_2025", "2025", "228615", "YE2025 non-fin ST ruil pay 228614.60 was 256293.62; tick1319; primary BBC J4"),
    ("bud_hc_accruals_2025", "2025", "1420", "YE2025 overlopend passief 1419.57; tick1319; primary BBC J4"),
    ("bud_hc_fin_debt_2025", "2025", "0", "YE2025 T4 fin debt 0; no new loans no afl; tick1319; primary BBC T4"),
    ("bud_hc_equity_2025", "2025", "743905", "YE2025 nettoactief 743905.00 was 673678.93; tick1319; primary BBC J4/T5"),
    ("bud_hc_cum_pnl_2025", "2025", "743905", "YE2025 gecumuleerd overschot 743905.00 was 673678.93; tick1319; primary BBC J4/T5"),
    ("bud_hc_pnl_2025", "2025", "70226", "2025 J5 PnL +70226.07 (ops +67169.95 / fin +3056.12); tick1319; primary BBC J5"),
    ("bud_hc_expl_saldo_2025", "2025", "178173", "2025 expl saldo +178173.31 (ontv 1367830.77 / uitg 1189657.46); tick1319; primary BBC J2"),
    ("bud_hc_expl_ontv_2025", "2025", "1367831", "2025 expl ontv 1367830.77; tick1319; primary BBC J2"),
    ("bud_hc_expl_uitg_2025", "2025", "1189657", "2025 expl uitg 1189657.46; tick1319; primary BBC J2"),
    ("bud_hc_bbr_2025", "2025", "178173", "2025 BBR year +178173.31; tick1319; primary BBC J2"),
    ("bud_hc_cum_bbr_2025", "2025", "744914", "YE2025 cum BBR 744914.27 was 566740.96; tick1319; primary BBC J2"),
    ("bud_hc_afm_2025", "2025", "178173", "2025 AFM +178173.31 = gecorr AFM; no afl; tick1319; primary BBC J2"),
    ("bud_hc_pers_2025", "2025", "402734", "2025 J5/T2 pers 402733.90 was 708929.38 DROP; VTE unpublished FOI; tick1319; primary BBC"),
    ("bud_hc_goods_2025", "2025", "397180", "2025 J5 goederen/diensten 397179.96 / T2 391479.55; tick1319; primary BBC"),
    ("bud_hc_werksub_out_2025", "2025", "395000", "2025 toegestane werksub 395000.00 to Havenwereld vzw (cash 750000 R/C corr 355000); tick1319; primary BBC J5/T2/bijlage"),
    ("bud_hc_werksub_in_2025", "2025", "1269593", "2025 J5 werksub ontv 1269593.00 (alg 1233926.00 + spec 35667.00); tick1319; primary BBC J5"),
    ("bud_hc_werksub_prov_2025", "2025", "1233926", "2025 T2 alg werksub van de provincie 1233926.00 = J5 alg; T2 spec 0 vs J5 spec 35667; tick1319; primary BBC T2"),
    ("bud_hc_other_ops_2025", "2025", "46224", "2025 J5 andere operationele opbrengsten 46223.66; tick1319; primary BBC J5"),
    ("bud_hc_fin_inc_2025", "2025", "3200", "2025 J5 financiele opbrengsten 3200.13; tick1319; primary BBC J5"),
    ("bud_hc_costs_2025", "2025", "1331844", "2025 J5 costs 1331844.22; tick1319; primary BBC J5"),
    ("bud_hc_rev_2025", "2025", "1402070", "2025 J5 opbrengsten 1402070.29; tick1319; primary BBC J5"),
    ("bud_hc_deprec_2025", "2025", "136486", "2025 J5 afschrijvingen 136486.35; T5 write-off/transfer 90868.21+45618.14; tick1319; primary BBC"),
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
            "commitment_id": "comm_hc_jr2025_dual",
            "title": "APB Havencentrum JR2025 leftover APB dual (cash 364k / ST recv 609k / Havenwereld 395k)",
            "entity_id": ENT,
            "beneficiary": "Havenwereld vzw + provincie Antwerpen / POAB dual education-harbour",
            "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid",
            "decision_date": "",
            "start_year": "2025",
            "end_year": "2027",
            "total_envelope_eur": "973939",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Harbour education/experience centre (Havencentrum to Havenwereld; opening 2H 2026)",
            "cut_option": "Publish named ST recv ledger + Havenwereld vzw envelope + J5/T2 spec 35.7k recon + VTE; shrink leftover APB if intra-group",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": "tick1319; assets 973939 ST recv 609360 ST pay 230034 BBR +178173 AFM +178173 PnL +70226; FOI ready not sent",
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_hc_cash_364k_recv_609k_havenwereld_395k",
            "name": "APB Havencentrum JR2025 leftover APB: 0.97m assets / 364k cash / 609k ST recv / 395k to Havenwereld vzw",
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": "1189657",
            "total_cost_eur": "973939",
            "tco_notes": "Leftover dual APB shell: assets 0.97m / cash 364k / equity 744k; expl uitg 1.19m; 395k granted to Havenwereld vzw; do not treat 0.97m as TE-additive of 348bn",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Havenwereld vzw + provincie Antwerpen / POAB dual",
            "stated_goal": "Harbour education/experience centre (Havenwereld opening 2H 2026)",
            "measured_outcome": "Official BBC PDF 2026-08-17: BBR +178.2k / AFM +178.2k / PnL +70.2k; cash 364k DROP; ST recv 609k UP; VTE unpublished; J5 spec 35.7k vs T2 0",
            "absurdity_score": "5.5",
            "cost_score": "4.0",
            "difficulty": "3.0",
            "priority_index": "5.0",
            "cut_proposal": "Publish named ST recv + Havenwereld vzw envelope; shrink leftover APB if intra-group",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1319; leftover sister APB of mined provincie Antwerpen; FOI ready not sent; not TE-additive of 348bn",
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
                "Named counterparties behind ST recv 609360.19 (ruil 400926.48 + niet-ruil 208433.71) "
                "and ST non-fin ruil pay 228614.60 + recon J5 spec werksub 35667.00 vs T2 0 and J5 "
                "werksub 1269593.00 vs T2 1233926.00 + full Havenwereld vzw envelope behind granted "
                "395000.00 (cash 750000 + R/C corr 355000) + VTE behind pers 402733.90 + provincieraad "
                "vaststelling JR2025 + NBB non-filing legal basis"
            ),
            "why_it_matters": (
                "Leftover unmapped sister APB of already-mined provincie Antwerpen after honest residual "
                "dual hunt (GKC 1318 / PSES 1317 done). KBO 0443.423.820 active. Official BBC PDF now "
                "downloads (Foleon). 0.97m leftover APB shell with cash DROP to 364k, ST recv UP to 609k, "
                "and 395k granted to Havenwereld vzw. Sister leftover APB KampC PDF also live. Do not invent euros."
            ),
            "priority": "7",
            "recipient_body": "APB Havencentrum / Provincie Antwerpen / provinciegriffier",
            "recipient_email": FOI_EMAIL,
            "recipient_postal": FOI_POSTAL,
            "draft_letter_path": DRAFT,
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_hc_jr2025_dual",
            "linked_leaderboard_id": "lb_hc_cash_364k_recv_609k_havenwereld_395k",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1319",
    "title": "APB Havencentrum JR2025 dual residual leftover APB",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: APB Havencentrum JR2025 leftover sister APB after honest hunt; KBO 0443.423.820; "
        "official BBC PDF downloads; assets 0.97m / cash 364k / ST recv 609k / "
        "BBR +178.2k / AFM +178.2k / PnL +70.2k; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T18:05:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1319 APB Havencentrum JR2025 leftover sister APB residual; KBO 0443.423.820; "
        "assets 973939 ST recv 609360 ST pay 230034 BBR +178173 AFM +178173 "
        "PnL +70226; FOI ready not sent; next rq_1320 every-10 + residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1320",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "EVERY-10 tick: first refresh docs/doge/data/progress_every_10_ticks.md (coverage % layers A-E) "
        "and docs/doge/data/doge_waste_top10_current.md (top 10 by priority_index), then residual dual "
        "L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1319 done including APB Havencentrum 1319 leftover sister APB / APB GKC 1318 leftover sister APB / "
        "APB PSES 1317 leftover APB / Stad+OCMW Ranst 1316 FOI-unpublished / Stad+OCMW Lievegem 1315 FOI-TLS / "
        "AGB Sport Hulshout 1314 FOI-unpublished / AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / "
        "AGB Maaseik 1311 / APB VERA 1310); prefer other unmined AGB/zorg/EVA with direct "
        "PDF (sister leftover APB KampC JR2025 Foleon PDF now live — "
        "take if still unmined; AGB Blankenberge only if a PDF actually downloads); "
        "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
        "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
        "skip already-mined APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 "
        "(FOI TLS) / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / "
        "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
        "Ternat / Oostkamp / Wetteren / Poperinge / Haacht / Bilzen-Hoeselt / AGB Sport Geel / Zwevegem; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
        "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); IS every-10"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1319 after APB Havencentrum JR2025 leftover sister APB; next every-10 + residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1319", rq_new, rq_spawn)
print("research_queue 1319", found, "spawned_1320", spawned)

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
            "last_unit_id": "rq_1319",
            "ticks_completed": "1319",
            "paused": "no",
            "notes": (
                "tick1319 APB Havencentrum JR2025 leftover sister APB residual; KBO 0443.423.820; "
                "assets 0.97m cash 364k ST recv 609k ST pay 230k BBR +178.2k AFM +178.2k PnL +70.2k; "
                "FOI ready; next rq_1320 every-10 + residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1319 - 2026-08-17 - rq_1319 APB Havencentrum dual residual leftover sister APB
- Unit: APB Havencentrum JR2025 leftover sister APB/EVA of already-mined provincie Antwerpen after residual dual hunt (KBO **0443.423.820**; official BBC text PDF on Foleon 25p / 0.79MB; print **31.03.2026**; volgnr **1065115**; Jnl. via CSrapportaal). PREFER leftover sister APBs of provincie Antwerpen whose Foleon JR2025 PDFs are already known live from ticks 1317-1318: first unmined of APB Havencentrum / KampC. Distinct from already-mined APB GKC 1318 / APB PSES 1317 / APB VERA 1310 / Westtoer / APB Mercator. KBO zetel Koningin Elisabethlei 22 2018 since 15.06.2023; operational VE Scheldelaan 444 2040 (VE **2.159.573.554**). Bestuurder Luk Lemmens since 15.12.2021. APB since 01.01.2014; start 13.12.1990; aanbestedende overheid; 1 VE; no KBO e-mail/NACE. APB states not an onderneming — no NBB filing. Brand shift 2025 to Havenwereld (provincie + POAB); building opening 2H 2026. Hunt leftover AGB first: AGB Blankenberge official still **JR2019-only** (unmined, no JR2025 PDF); AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek still no fetchable JR2025. Sister leftover APB **KampC** JR2025 Foleon PDF also live — left for later. provincieantwerpen.be 403 from this box (Foleon OK). Skip already-mined GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **973.939,17** (was 969.517,26); cash **364.168,68** vs 610.559,33 DROP; ST recv **609.360,19** (ruil **400.926,48** + niet-ruil **208.433,71**) UP vs 237.919,59; fixed **148,74**; FVA **148,74**; MVA/IVA **0**; schulden **230.034,17** ALL ST; fin debt T4 **0**; non-fin ST ruil pay **228.614,60**; accruals **1.419,57**; equity **743.905,00**; cum surplus **743.905,00**; expl **+178.173,31** (ontv **1.367.830,77** / uitg **1.189.657,46**); invest **0**; fin **0**; BBR year **+178.173,31**; cum BBR **744.914,27**; AFM/gecorr **+178.173,31**; PnL **+70.226,07**; pers J5/T2 **402.733,90**; werksub granted **395.000,00** to Havenwereld vzw (cash 750.000 + R/C 355.000); werksub received J5 **1.269.593,00** (provincie T2 alg **1.233.926,00** = J5 alg; J5 spec **35.667,00** vs T2 **0**); other ops **46.223,66**. VTE unpublished.
- CSVs: sources+4/entities+1/budgets+33/commitments+1/leaderboard+1 + FOI ready `gap_hc_st_recv_609k_havenwereld_395k_l5` (not sent); rq_1319=done; spawn rq_1320; ticks=1319. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Havencentrum leftover sister APB). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1320 EVERY-10 + residual dual L5 VL JR2025 hole_fill (refresh progress_every_10_ticks.md + doge_waste_top10_current.md first; then prefer sister leftover APB KampC JR2025 Foleon PDF now live; leftover AGB Blankenberge only if a PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1319 write done")

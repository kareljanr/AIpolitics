# -*- coding: utf-8 -*-
"""Tick 1317 — surgical append/patch only. APB PSES JR2025 leftover APB residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1317"
UTC = "2026-08-17T17:50:00Z"
ENT = "apb_pses"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>PSES"
GAP = "gap_pses_st_recv_165m_pay_174m_bbr_neg_1_29m_l5"
SRC = "src_pses_jr2025_pdf"
SRC2 = "src_pses_jaarverslag_2025"
SRC3 = "src_kbo_pses_0541413220"
SRC4 = "src_pses_foi_page"
SRC_URL = "https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/20500/2025-apb_pses.52c03ee5538e.pdf"
SRC2_URL = "https://publicaties.provincieantwerpen.be/pses-jaarverslag-2025/in-cijfers"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0541413220"
SRC4_URL = "https://www.provincieantwerpen.be/nl/provinciebestuur/werking-provincie/provinciegriffier/inzagerecht"
FOI_EMAIL = "openbaarheid@provincieantwerpen.be"
FOI_POSTAL = "Koningin Elisabethlei 22 2018 Antwerpen"
DRAFT = "docs/doge/foi/drafts/gap_pses_st_recv_165m_pay_174m_bbr_neg_1_29m_l5.md"


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
            "title": "APB PSES jaarrekening 2025 (official BBC text PDF)",
            "url": SRC_URL,
            "publisher": "APB PSES / Provincie Antwerpen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1317; Foleon BBC text PDF 0.79MB print 31.03.2026 volgnr 660349; "
                "KBO 0541.413.220; assets 186522315.29 fin debt 0 ST recv 165307224.48 "
                "ST pay 184099383.81 BBR -1286053.60 AFM -1352547 PnL +846358.84; primary BBC text"
            ),
        },
        {
            "source_id": SRC2,
            "title": "PSES jaarverslag 2025 in cijfers (official Foleon link)",
            "url": SRC2_URL,
            "publisher": "Provincie Antwerpen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1317; publicaties.provincieantwerpen.be/pses-jaarverslag-2025/in-cijfers "
                "links the same BBC PDF; leftover APB of mined provincie Antwerpen"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO APB PSES 0541.413.220",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1317; KBO 0541.413.220 actief APB since 26.09.2013; zetel Koningin "
                "Elisabethlei 22 2018; 1 VE; bestuurder Jan De Haes since 05.12.2024; "
                "gedelegeerd bestuurder Bart Van Ballaert since 01.02.2025; NACE 84.113; "
                "RSZ since 01.01.2022; aanbestedende overheid; europa@provincieantwerpen.be; no KBO finance"
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
                "tick1317; FOI openbaarheid@provincieantwerpen.be / provinciegriffier Maarten Puls "
                "T 03 240 54 28; Koningin Elisabethlei 22 2018"
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
            "name_nl": "APB Provinciaal Secretariaat Europese Structuurfondsen (APB PSES)",
            "name_fr": "APB Secretariat provincial des fonds structurels europeens",
            "name_en": "APB Provincial Secretariat for European Structural Funds",
            "level": "apb",
            "parent_id": "prov_antwerpen",
            "community_language": "nl",
            "website": "https://publicaties.provincieantwerpen.be/pses-jaarverslag-2025",
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1317 JR2025 leftover APB residual; KBO 0541.413.220; assets 186522315 "
                "fin debt 0 ST recv 165307224 ST pay 184099384 BBR -1286054 AFM -1352547 "
                "PnL +846359 cash 21117661 equity 2422931; FOI ready"
            ),
        },
    ],
)
print("entities", n)

budget_rows = [
    ("bud_pses_assets_2025", "2025", "186522315", "YE2025 assets 186522315.29 was 228500982.54 DROP; tick1317; primary BBC J4"),
    ("bud_pses_assets_2024", "2024", "228500983", "YE2024 assets 228500982.54; tick1317; primary BBC J4"),
    ("bud_pses_cash_2025", "2025", "21117661", "YE2025 cash 21117661.47 was 23939274.32 DROP; tick1317; primary BBC J4"),
    ("bud_pses_cash_2024", "2024", "23939274", "YE2024 cash 23939274.32; tick1317; primary BBC J4"),
    ("bud_pses_current_2025", "2025", "186518167", "YE2025 vlottende activa 186518166.54; tick1317; primary BBC J4"),
    ("bud_pses_recv_st_2025", "2025", "165307224", "YE2025 ST recv 165307224.48 (ruil 165251919.95 + niet-ruil 55304.53); tick1317; primary BBC J4"),
    ("bud_pses_recv_ruil_2025", "2025", "165251920", "YE2025 ST ruil recv 165251919.95 was 204411144.46; tick1317; primary BBC J4"),
    ("bud_pses_fixed_2025", "2025", "4149", "YE2025 vaste activa 4148.75 (LT recv 4000.01 + FVA 148.74); tick1317; primary BBC J4"),
    ("bud_pses_fva_2025", "2025", "149", "YE2025 FVA 148.74 andere; tick1317; primary BBC J4/T5"),
    ("bud_pses_schulden_2025", "2025", "184099384", "YE2025 schulden 184099383.81 ALL ST was 226924409.90; tick1317; primary BBC J4"),
    ("bud_pses_pay_ruil_2025", "2025", "174158343", "YE2025 non-fin ST ruil pay 174158342.87 was 214797822.10; tick1317; primary BBC J4"),
    ("bud_pses_accruals_2025", "2025", "9941041", "YE2025 overlopend passief 9941040.94; tick1317; primary BBC J4"),
    ("bud_pses_fin_debt_2025", "2025", "0", "YE2025 T4 fin debt 0; no new loans no afl; tick1317; primary BBC T4"),
    ("bud_pses_equity_2025", "2025", "2422931", "YE2025 nettoactief 2422931.48 was 1576572.64; tick1317; primary BBC J4/T5"),
    ("bud_pses_cum_pnl_2025", "2025", "2413410", "YE2025 gecumuleerd overschot 2413410.22 was 1567051.38; tick1317; primary BBC J4/T5"),
    ("bud_pses_pnl_2025", "2025", "846359", "2025 J5 PnL +846358.84 (ops +629491.15 / fin +216867.69); tick1317; primary BBC J5"),
    ("bud_pses_expl_saldo_2025", "2025", "-1352547", "2025 expl saldo -1352547.00 (ontv 2115993.07 / uitg 3468540.07); tick1317; primary BBC J2"),
    ("bud_pses_expl_ontv_2025", "2025", "2115993", "2025 expl ontv 2115993.07; tick1317; primary BBC J2"),
    ("bud_pses_expl_uitg_2025", "2025", "3468540", "2025 expl uitg 3468540.07; tick1317; primary BBC J2"),
    ("bud_pses_fin_saldo_2025", "2025", "66493", "2025 fin saldo +66493.40 vereffening vooruitbetalingen WAAI/MarktWaarde; tick1317; primary BBC J2/T2"),
    ("bud_pses_bbr_2025", "2025", "-1286054", "2025 BBR year -1286053.60; tick1317; primary BBC J2"),
    ("bud_pses_cum_bbr_2025", "2025", "12266543", "YE2025 cum BBR 12266543.08 was 13552596.68; tick1317; primary BBC J2"),
    ("bud_pses_afm_2025", "2025", "-1352547", "2025 AFM -1352547.00 = gecorr AFM; no afl; tick1317; primary BBC J2"),
    ("bud_pses_pers_2025", "2025", "1777971", "2025 J5 pers 1777971.23 / T2 cash 1774048.94; VTE unpublished FOI; tick1317; primary BBC"),
    ("bud_pses_goods_2025", "2025", "1338207", "2025 J5 goederen/diensten 1338206.69 / T2 1370542.58; tick1317; primary BBC"),
    ("bud_pses_werksub_out_2025", "2025", "323074", "2025 toegestane werksub 323073.78 was 1621536.53 DROP andere begunstigden; tick1317; primary BBC J5/T2"),
    ("bud_pses_werksub_in_2025", "2025", "1777929", "2025 J5 werksub ontv 1777929.09 (alg 1242378.93 + spec 535550.16); tick1317; primary BBC J5"),
    ("bud_pses_werksub_prov_2025", "2025", "1232820", "2025 T2 alg werksub van de provincie 1232820.00; tick1317; primary BBC T2"),
    ("bud_pses_other_ops_2025", "2025", "2290814", "2025 J5 andere operationele opbrengsten 2290813.76; tick1317; primary BBC J5"),
    ("bud_pses_fin_inc_2025", "2025", "217742", "2025 J5 financiele opbrengsten 217742.46; tick1317; primary BBC J5"),
    ("bud_pses_costs_2025", "2025", "3440126", "2025 J5 costs 3440126.47; tick1317; primary BBC J5"),
    ("bud_pses_rev_2025", "2025", "4286485", "2025 J5 opbrengsten 4286485.31; tick1317; primary BBC J5"),
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
            "commitment_id": "comm_pses_jr2025_passthrough",
            "title": "APB PSES JR2025 leftover APB EU-funds pass-through (ST recv 165.31m / ST pay 174.16m)",
            "entity_id": ENT,
            "beneficiary": "Interreg / EU structural-fund beneficiaries + provincie Antwerpen dual",
            "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid; Interreg Vlaanderen-Nederland",
            "decision_date": "",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": "186522315",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Provincial cofinancing + Interreg TB secretariat legal shell for EU projects",
            "cut_option": "Publish named ST recv/pay ledger + dual provincie dotatie recon + VTE; shrink pass-through shell if counterparties are intra-group",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": "tick1317; assets 186522315 ST recv 165307224 ST pay 184099384 BBR -1286054 AFM -1352547 PnL +846359; FOI ready not sent",
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_pses_passthrough_186m_bbr_neg_1_29m",
            "name": "APB PSES JR2025 leftover APB: 186.52m assets / 165.31m ST recv / 174.16m ST pay / BBR -1.29m",
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": "3468540",
            "total_cost_eur": "186522315",
            "tco_notes": "Pass-through EU-funds shell: assets 186.52m vs equity 2.42m; expl uitg 3.47m; do not treat 186m as TE-additive of 348bn",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Interreg / EU structural-fund beneficiaries + provincie Antwerpen dual",
            "stated_goal": "Provincial cofinancing + Interreg TB secretariat legal shell",
            "measured_outcome": "Official BBC PDF 2026-08-17: BBR -1.29m / AFM -1.35m while PnL +0.85m; cash 21.12m; VTE unpublished",
            "absurdity_score": "7.0",
            "cost_score": "8.0",
            "difficulty": "4.0",
            "priority_index": "6.8",
            "cut_proposal": "Publish named ST recv/pay ledger + dual provincie dotatie recon; shrink shell if intra-group",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1317; leftover APB of mined provincie Antwerpen; FOI ready not sent; not TE-additive of 348bn",
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
                "Named counterparties behind ST ruil recv 165251919.95 and ST non-fin ruil pay "
                "174158342.87 (Interreg TB / EU-funds) + recon BBR -1286053.60 / AFM -1352547 "
                "vs PnL +846358.84 and cash 21117661.47 + dual provincie dotatie T2 1232820 vs "
                "J5 alg 1242378.93 + spec 535550.16 + VTE behind pers 1777971.23 + provincieraad "
                "vaststelling JR2025 + NBB non-filing legal basis"
            ),
            "why_it_matters": (
                "Leftover unmapped APB of already-mined provincie Antwerpen after honest residual "
                "dual hunt. KBO 0541.413.220 active. Official BBC PDF now downloads (Foleon). "
                "186.52m pass-through shell with thin equity 2.42m and BBR -1.29m. Sister leftover "
                "APB GKC/Havencentrum/KampC PDFs also live. Do not invent euros."
            ),
            "priority": "8",
            "recipient_body": "APB PSES / Provincie Antwerpen / provinciegriffier",
            "recipient_email": FOI_EMAIL,
            "recipient_postal": FOI_POSTAL,
            "draft_letter_path": DRAFT,
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_pses_jr2025_passthrough",
            "linked_leaderboard_id": "lb_pses_passthrough_186m_bbr_neg_1_29m",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1317",
    "title": "APB PSES JR2025 dual residual leftover APB",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: APB PSES JR2025 leftover APB after honest hunt; KBO 0541.413.220; "
        "official BBC PDF downloads; assets 186.52m / ST recv 165.31m / ST pay 184.10m / "
        "BBR -1.29m / AFM -1.35m / PnL +0.85m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T17:35:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1317 APB PSES JR2025 leftover APB residual; KBO 0541.413.220; "
        "assets 186522315 ST recv 165307224 ST pay 184099384 BBR -1286054 AFM -1352547 "
        "PnL +846359; FOI ready not sent; next rq_1318 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1318",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1317 done including APB PSES 1317 leftover APB / Stad+OCMW Ranst 1316 "
        "FOI-unpublished / Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 "
        "FOI-unpublished / AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / "
        "AGB Maaseik 1311 / APB VERA 1310); prefer other unmined AGB/zorg/EVA with direct "
        "PDF (sister leftover APB GKC / Havencentrum / KampC JR2025 Foleon PDFs now live — "
        "take if still unmined; AGB Blankenberge only if a PDF actually downloads); "
        "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
        "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
        "skip already-mined APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 "
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
    "notes": "spawned tick1317 after APB PSES JR2025 leftover APB; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1317", rq_new, rq_spawn)
print("research_queue 1317", found, "spawned_1318", spawned)

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
            "last_unit_id": "rq_1317",
            "ticks_completed": "1317",
            "paused": "no",
            "notes": (
                "tick1317 APB PSES JR2025 leftover APB residual; KBO 0541.413.220; "
                "assets 186.52m ST recv 165.31m ST pay 184.10m BBR -1.29m AFM -1.35m PnL +0.85m; "
                "FOI ready; next rq_1318 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1317 - 2026-08-17 - rq_1317 APB PSES dual residual leftover APB
- Unit: APB Provinciaal Secretariaat Europese Structuurfondsen (APB PSES) JR2025 leftover APB/EVA of already-mined provincie Antwerpen after residual dual hunt (KBO **0541.413.220**; official BBC text PDF on Foleon 25p / 0.79MB; print **31.03.2026**; volgnr **660349**; Jnl. via CSrapportaal). PREFER AGB/zorg/EVA/IGS: first leftover APB whose JR2025 BBC PDF actually downloads. Distinct from already-mined APB VERA 1310 / Westtoer 988 / APB Mercator. Seat Koningin Elisabethlei 22 2018. Bestuurder Jan De Haes since 05.12.2024 / gedelegeerd bestuurder Bart Van Ballaert since 01.02.2025. NACE 84.113; RSZ-werkgever; aanbestedende overheid; 1 VE; europa@provincieantwerpen.be. APB states not an onderneming — no NBB filing. Hunt leftover AGB first: AGB Blankenberge official still **JR2019-only** (unmined, no JR2025 PDF); AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek still no fetchable JR2025. Sister leftover APB **GKC / Havencentrum / KampC** JR2025 Foleon PDFs also live — left for later. provincieantwerpen.be 403 from this box (Foleon OK). Skip already-mined Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM/AGB Maaseik 1311-1312. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **186.522.315,29** (was 228.500.982,54) DROP; cash **21.117.661,47** vs 23.939.274,32 DROP; ST recv **165.307.224,48** (ruil **165.251.919,95**); fixed **4.148,75**; FVA **148,74**; MVA/leasing **0**; schulden **184.099.383,81** ALL ST; fin debt T4 **0**; non-fin ST ruil pay **174.158.342,87**; accruals **9.941.040,94**; equity **2.422.931,48**; cum surplus **2.413.410,22**; expl **−1.352.547,00** (ontv **2.115.993,07** / uitg **3.468.540,07**); invest **0**; fin **+66.493,40**; BBR year **−1.286.053,60**; cum BBR **12.266.543,08**; AFM/gecorr **−1.352.547,00**; PnL **+846.358,84**; pers J5 **1.777.971,23**; werksub granted **323.073,78** DROP vs 1.621.536,53; werksub received J5 **1.777.929,09** (provincie T2 alg **1.232.820,00**); other ops **2.290.813,76**. VTE unpublished.
- CSVs: sources+4/entities+1/budgets+32/commitments+1/leaderboard+1 + FOI ready `gap_pses_st_recv_165m_pay_174m_bbr_neg_1_29m_l5` (not sent); rq_1317=done; spawn rq_1318; ticks=1317. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB PSES leftover APB). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1318 residual dual L5 VL JR2025 hole_fill (prefer sister leftover APB GKC / Havencentrum / KampC JR2025 Foleon PDFs now live; leftover AGB Blankenberge only if a PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1317 write done")

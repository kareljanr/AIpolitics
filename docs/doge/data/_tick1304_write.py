# -*- coding: utf-8 -*-
"""Tick 1304 (research_queue patched surgically — last line + spawn only).
AGB Pepingen JR2025 Entity II residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
sys.path.insert(0, str(DATA))
from _tick1304_hdr import *  # noqa: F401,F403


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


assert abs((CURRENT + FIXED) - ASSETS) <= 1
assert abs((FVA + MVA) - FIXED) <= 1
assert abs((EQUITY + SCHULDEN) - ASSETS) <= 1
assert abs((CAP_SUBS + CUM_PNL + OTHER_EQ) - EQUITY) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((CUM_PREV + BBR) - CUM_BBR) <= 1
assert abs((REVENUE - COSTS) - PNL) <= 1
assert FIN_DEBT == 0 and NEW_LOANS == 0 and INVEST == 0
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "AGB Pepingen BBC jaarrekening 2025 deel 1 (official PDF)",
            "url": SRC_URL,
            "publisher": "Autonoom Gemeentebedrijf Pepingen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1304; BBC text PDF 70p / 5.89MB pepingen.be; RVB 22.06.2026; "
                "pub 24.06.2026; Jnl Budg 2858 Alg 107; KBO 0839.927.156; "
                "assets 180707 AFM -3219 PnL -3685 cash 1492 DROP"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AGB Pepingen RVB 22.06.2026 vaststelling jaarrekening 2025",
            "url": SRC2_URL,
            "publisher": "Autonoom Gemeentebedrijf Pepingen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1304; uittreksel RVB 22.06.2026; voorzitter Suzanne De Cort / "
                "secretaris Leen Deneyer; BBC+NBB vastgesteld; not sent FOI"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB Pepingen 0839.927.156",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1304; AGB KBO 0839.927.156 / city 0207.512.197; "
                "seat Ninoofsesteenweg 116 1670; 0 VE; NACE 93.110; "
                "AD Deneyer / FD Kestens / burgemeester Van Cutsem"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": CITY,
            "name_nl": "Gemeente Pepingen",
            "name_fr": "Commune de Pepingen",
            "name_en": "Municipality of Pepingen",
            "level": "municipality",
            "parent_id": "",
            "community_language": "nl",
            "website": "https://www.pepingen.be",
            "foi_email": "info@pepingen.be",
            "foi_postal": "Ninoofsesteenweg 116 1670 Pepingen",
            "notes": (
                "tick1304 stub; KBO 0207.512.197; burgemeester Peter Van Cutsem; "
                "AGB Pepingen mined 1304; city+OCMW GE JR2025 still unmined"
            ),
        },
        {
            "entity_id": ENT,
            "name_nl": "Autonoom Gemeentebedrijf Pepingen",
            "name_fr": "Regie communale autonome Pepingen",
            "name_en": "Autonomous municipal company Pepingen",
            "level": "municipal_agency",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC_PAGE,
            "foi_email": "info@pepingen.be",
            "foi_postal": "Ninoofsesteenweg 116 1670 Pepingen",
            "notes": (
                "tick1304 JR2025 Entity II residual; KBO 0839.927.156; 0 VE; "
                "sportaccommodaties; assets 180707 AFM -3219 PnL -3685 cash 1492 DROP; "
                "fin debt 0; city GE unmined; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_agbpep_assets_2025", "2025", ASSETS, "J4 assets 180706.60 vs 210677.34 DROP"),
    ("bud_agbpep_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 210677.34"),
    ("bud_agbpep_cash_2025", "2025", CASH, "J4 cash 1492.05 vs 3835.74 DROP"),
    ("bud_agbpep_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 3835.74"),
    ("bud_agbpep_fva_2025", "2025", FVA, "J4 FVA IGS 25.00"),
    ("bud_agbpep_mva_2025", "2025", MVA, "J4 MVA 171412.98 terreinen/gebouwen; leasing 0"),
    ("bud_agbpep_equity_2025", "2025", EQUITY, "J4 nettoactief 172313.05 vs 204079.73 DROP"),
    ("bud_agbpep_cap_subs_2025", "2025", CAP_SUBS, "J4 kapitaalsubsidies 168615.41 vs 196697.11"),
    ("bud_agbpep_cum_pnl_2025", "2025", CUM_PNL, "J4 cum PnL 1197.64 vs 4882.62"),
    ("bud_agbpep_schulden_2025", "2025", SCHULDEN, "J4 ST schulden 8393.55; LT 0; fin debt 0"),
    ("bud_agbpep_fin_debt_2025", "2025", FIN_DEBT, "J4/T4 fin debt 0; new loans 0"),
    ("bud_agbpep_expl_2025", "2025", EXPL, "J2 exploitatiesaldo -3219"),
    ("bud_agbpep_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 11961 vs MJP 14672"),
    ("bud_agbpep_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 15180 vs MJP 14672"),
    ("bud_agbpep_invest_2025", "2025", INVEST, "J2 invest 0"),
    ("bud_agbpep_bbr_2025", "2025", BBR, "J2 BBR boekjaar -3219"),
    ("bud_agbpep_cum_bbr_2025", "2025", CUM_BBR, "J2 gecumuleerd BBR 747 (prev 3966)"),
    ("bud_agbpep_afm_2025", "2025", AFM, "J2 AFM -3219 NEG"),
    ("bud_agbpep_gecorr_2025", "2025", GECORR, "J2 gecorr AFM -3219 NEG"),
    ("bud_agbpep_pnl_2025", "2025", PNL, "J5 PnL -3685 vs +296"),
    ("bud_agbpep_costs_2025", "2025", COSTS, "J5 kosten 43728 (goods 14431 + depr 28549)"),
    ("bud_agbpep_revenue_2025", "2025", REVENUE, "J5 opbrengsten 40043 (ops 11961 + fin 28082)"),
    ("bud_agbpep_depr_2025", "2025", DEPR, "J5 afschrijvingen 28549 vs cap-sub amort 28082"),
    ("bud_agbpep_fin_rev_2025", "2025", FIN_REV, "J5 financiele opbrengsten 28082"),
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
            "notes": note + f"; tick{TICK}; primary BBC",
        }
        for bid, year, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_agbpep_afm_neg_3_22k_2025",
        "AGB Pepingen YE2025 AFM -3.219 NEG",
        "3219",
        "J2 AFM -3219 = expl -3219; ontv 11961 vs MJP 14672; uitg 15180; gecorr -3219; BBR year -3219 / cum 747",
        "Publish 2026-2031 AFM recovery pad + expl gap vs MJP FOI",
    ),
    (
        "comm_agbpep_pnl_neg_3_69k_2025",
        "AGB Pepingen YE2025 PnL -3.685 NEG",
        "3685",
        "J5 PnL -3685 (ops -31759 / fin +28074); depr 28549 vs cap-sub amort 28082; cum 1198 vs 4883",
        "Publish amort vs depr note + 2026-2031 resultaatstoewijzing FOI",
    ),
    (
        "comm_agbpep_mva_0_17m_2025",
        "AGB Pepingen YE2025 MVA 171.413 buildings",
        "171413",
        "J4 MVA 171413 terreinen/gebouwen vs 199962; leasing 0; cap subs 168615; FVA IGS 25",
        "Publish building inventory + cap-sub remaining schedule FOI",
    ),
    (
        "comm_agbpep_cash_drop_1_49k_2025",
        "AGB Pepingen YE2025 cash 1.492 DROP",
        "1492",
        "J4 cash 1492 vs 3836 DROP; ST schulden 8394; kengetallen prijssubsidie blank; pers/VTE unpublished",
        "Publish liquidity pad + prijssubsidie + VTE FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Pepingen / AGB sportaccommodatie",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 AGB Pepingen vastgesteld 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": env,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local AGB Entity II residual map VL JR2025 Pepingen",
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": note + f"; tick{TICK}; primary BBC",
        }
        for cid, title, env, note, cut in crows
    ],
)
print("commitments", n)

lb_rows = [
    (
        "lb_agbpep_afm_neg_3_22k_2025",
        "AGB Pepingen YE2025 AFM -3.22k NEG",
        "3219",
        "7.5",
        "4.0",
        "Publish 2026-2031 AFM recovery pad",
        "AFM -3219 = expl -3219; ontv 11961 vs MJP 14672; BBR year -3219 / cum 747",
    ),
    (
        "lb_agbpep_pnl_neg_3_69k_2025",
        "AGB Pepingen YE2025 PnL -3.69k NEG",
        "3685",
        "7.0",
        "4.0",
        "Publish amort vs depr note",
        "PnL -3685; ops -31759 / fin +28074; depr 28549 vs cap-sub amort 28082",
    ),
    (
        "lb_agbpep_cash_drop_1_49k_2025",
        "AGB Pepingen YE2025 cash 1.49k DROP",
        "1492",
        "6.5",
        "3.5",
        "Publish liquidity pad + prijssubsidie + VTE",
        "cash 1492 vs 3836 DROP; ST schulden 8394; prijssubsidie blank; pers unpublished",
    ),
    (
        "lb_agbpep_mva_0_17m_2025",
        "AGB Pepingen YE2025 MVA 0.17m buildings",
        "171413",
        "5.0",
        "5.5",
        "Publish building inventory + cap-sub remaining",
        "MVA 171413 vs 199962; leasing 0; cap subs 168615; FVA IGS 25",
    ),
]
n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": amt,
            "total_cost_eur": amt,
            "tco_notes": tco,
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Inwoners Pepingen / AGB sportaccommodatie",
            "stated_goal": "Local AGB Entity II residual map VL JR2025 Pepingen",
            "measured_outcome": (
                "assets 180707 / AFM -3219 / PnL -3685 / cash 1492 DROP / "
                "MVA 171413 / fin debt 0 / cum BBR 747"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "5.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; AGB FOI",
        }
        for iid, name, amt, absu, cost, cut, tco in lb_rows
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
                "J2 AFM -3219 NEG (expl ontv 11961 vs MJP 14672 / uitg 15180) + "
                "J5 PnL -3685 (ops -31759 / fin +28074; depr 28549 vs cap-sub amort 28082) + "
                "cash DROP 1492 vs 3836 + J2 beschikbaar BBR unpublished vs cum 747 + "
                "kengetallen prijssubsidie gemeente blank + VTE vs pers unpublished + "
                "city+OCMW Pepingen GE JR2025 still unmined"
            ),
            "why_it_matters": (
                "Unmined leftover AGB Pepingen Entity II. Official BBC PDF now downloads "
                "on pepingen.be. Tiny sport AGB: assets 180707 DROP, AFM -3219, PnL -3685, "
                "cash 1492 DROP, fin debt 0. City GE still unmined. Cum BBR 747 thin."
            ),
            "priority": "8",
            "recipient_body": "AGB Pepingen / Gemeente Pepingen",
            "recipient_email": "info@pepingen.be",
            "recipient_postal": "Ninoofsesteenweg 116 1670 Pepingen",
            "draft_letter_path": "docs/doge/foi/drafts/gap_agbpep_afm_neg_3_22k_pnl_neg_3_69k_cash_drop_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbpep_afm_neg_3_22k_2025",
            "linked_leaderboard_id": "lb_agbpep_afm_neg_3_22k_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1304",
    "title": "AGB Pepingen JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Pepingen JR2025 BBC text + KBO; "
        "KBO 0839.927.156; assets 180707 / AFM -3219 / PnL -3685 / cash 1492 DROP; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T13:50:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1304 AGB Pepingen JR2025 Entity II residual; KBO 0839.927.156; "
        "assets 180707 AFM -3219 PnL -3685 cash 1492 DROP MVA 171413 fin debt 0 "
        "BBR -3219 cum 747 expl -3219; city GE still unmined; FOI ready not sent; "
        "next rq_1305 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1305",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1304 done including AGB Pepingen 1304 / Stad+OCMW Edegem 1303 / "
        "Stad+OCMW Wommelgem 1302 / Stad+OCMW Zonhoven 1301 / Stad+OCMW Kortenaken 1300 / "
        "AGB Kortenaken 1299); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined AGB Pepingen 1304 / city Edegem 1303 / AGB Edegem 1239 / "
        "city Wommelgem 1302 / city Zonhoven 1301 / city Kortenaken 1300 / AGB Kortenaken 1299 / "
        "city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / "
        "AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / Deerlijk 981 / "
        "Zonnebeke 963 / AGB MMP1917 964 / Lochristi 927 / Tervuren 1226 / AGB Bexit 1225; "
        "leftover Maarkedal/Meulebeke still unmined — take only if PDF fetches; "
        "Londerzeel/Holsbeek/Merchtem/Zwalm/Wortegem-Petegem and city Pepingen GE JR2025 only if PDF fetches; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Oostkamp 1131; "
        "skip Kuurne city already 957; skip Ternat/Lubbeek already mined; "
        "skip AGB Kapellen / Nieuwerkerken 1102 already mined; "
        "skip AGB Sport Hulshout JR2024-only; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1304 after AGB Pepingen JR2025 Entity II residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1304", rq_new, rq_spawn)
print("research_queue 1304", found, "spawned_1305", spawned)

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
            "last_unit_id": "rq_1304",
            "ticks_completed": "1304",
            "paused": "no",
            "notes": (
                "tick1304 AGB Pepingen JR2025 Entity II residual; KBO 0839.927.156; "
                "assets 180707 AFM -3219 PnL -3685 cash 1492 DROP; "
                "FOI ready; next rq_1305 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1304_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")

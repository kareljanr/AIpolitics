# tick 238 Famiwal + private AF caisses dual channel map from EPCO
import csv, os, json

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src = "src_wal_epco_famiwal_caisses_2026"
url = "https://finances.wallonie.be/files/Budget%202026/Budget%202026/coppieters/epco.pdf"
utc = "2026-07-29T06:05:00Z"

# Famiwal (kEUR -> EUR)
fw_total = 1118794000
fw_prest = 1080918000
fw_fonct = 36976000
fw_dot_rw = 36359000
fw_pers = 17737000 + 9641000 + 745000  # remun + ONSS + other social
fw_it = 2656000
fw_cap = 2541000

# KidsLife
kl_prest = 360167000
kl_fonct_eng = 7981000
kl_total_dep = 368148000
kl_dot = 7712000

# Camille
ca_prest = 579645000
ca_fonct = 12198000
ca_total_dep = 585946000
ca_rec_fonct = 12286000  # includes RW subvention class

# Parentia
pa_prest = 992756000
pa_fonct = 24175000
pa_total_dep = 1016931000
pa_dot = 21258000

# AViQ AF envelope (prior tick)
aviq_af = 3008488000
aviq_caisses_rem = 41351000

prest_sum4 = fw_prest + kl_prest + ca_prest + pa_prest
fonct_private = kl_fonct_eng + ca_fonct + pa_fonct  # approx
fonct_all_caf = fw_fonct + fonct_private

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src,
            "Wallonie EPCO 2026 UAP Famiwal KidsLife Camille Parentia AF budgets",
            url,
            "SPW Finances / Ministre Coppieters",
            "2026-07-29",
            "budget_justification",
            "Famiwal total 1118.8m prest 1080.9m fonct 37.0m; KidsLife prest 360.2m; Camille 579.6m; Parentia 992.8m; prest sum4 3013.5m ~AViQ AF 3008.5m; tick238",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "famiwal",
            "FAMIWAL openbare kinderbijslagkas Wallonie",
            "FAMIWAL caisse publique wallonne allocations familiales",
            "Walloon public family benefits fund",
            "parastatal",
            "aviq",
            "fr",
            "https://www.famiwal.be",
            "",
            "",
            "UAP type2; total 1.119bn 2026 prest 1.081bn fonct 37.0m; dual private caisses; tick238",
        ]
    )
    w.writerow(
        [
            "kidslife_wal",
            "KidsLife Wallonie CAF",
            "KidsLife Wallonie caisse allocations familiales",
            "KidsLife private family benefits fund Wallonia",
            "parastatal",
            "aviq",
            "fr",
            "https://www.kidslife.be",
            "",
            "",
            "UAP type3; prest 360.2m 2026; RW fonct sub 7.7m; tick238",
        ]
    )
    w.writerow(
        [
            "camille_wal",
            "Camille Wallonie CAF",
            "Camille caisse allocations familiales Wallonie",
            "Camille private family benefits fund Wallonia",
            "parastatal",
            "aviq",
            "fr",
            "https://www.camille.be",
            "",
            "",
            "UAP type3; prest 579.6m 2026; fonct 12.2m; tick238",
        ]
    )
    w.writerow(
        [
            "parentia_wal",
            "Parentia Wallonie CAF",
            "Parentia Wallonie caisse allocations familiales",
            "Parentia private family benefits fund Wallonia",
            "parastatal",
            "aviq",
            "fr",
            "https://www.parentia.be",
            "",
            "",
            "UAP type3; prest 992.8m 2026; RW fonct sub 21.3m; largest private; tick238",
        ]
    )

rows_b = [
    ("bud_famiwal_total_2026", "famiwal", 2026, fw_total, "", "", "budgeted", src, "strong", "Famiwal total recettes=depenses 1118.794m"),
    ("bud_famiwal_prest_2026", "famiwal", 2026, fw_prest, "", "", "budgeted", src, "strong", "Prestations familiales a payer 1080.918m (~36pct of 4-caisse prest sum)"),
    ("bud_famiwal_fonct_2026", "famiwal", 2026, fw_fonct, "", "", "budgeted", src, "strong", "Budget fonctionnement 36.976m; RW subvention 36.359m"),
    ("bud_famiwal_personnel_2026", "famiwal", 2026, fw_pers, "", "", "budgeted", src, "strong", "Personnel package remun+ONSS+other social 28.123m"),
    ("bud_famiwal_dot_rw_2026", "famiwal", 2026, fw_dot_rw, "", "", "budgeted", src, "strong", "DF 093.008 / recette CO 46.10 RW subvention fonctionnement 36.359m"),
    ("bud_kidslife_prest_2026", "kidslife_wal", 2026, kl_prest, "", "", "budgeted", src, "strong", "KidsLife prestations 360.167m"),
    ("bud_kidslife_total_2026", "kidslife_wal", 2026, kl_total_dep, "", "", "budgeted", src, "strong", "KidsLife total dep 368.148m"),
    ("bud_kidslife_fonct_2026", "kidslife_wal", 2026, kl_fonct_eng, "", "", "budgeted", src, "strong", "KidsLife fonct eng class 7.981m; RW sub 7.712m"),
    ("bud_camille_prest_2026", "camille_wal", 2026, ca_prest, "", "", "budgeted", src, "strong", "Camille prestations 579.645m"),
    ("bud_camille_total_2026", "camille_wal", 2026, ca_total_dep, "", "", "budgeted", src, "strong", "Camille total dep 585.946m"),
    ("bud_camille_fonct_2026", "camille_wal", 2026, ca_fonct, "", "", "budgeted", src, "strong", "Camille fonct 12.198m"),
    ("bud_parentia_prest_2026", "parentia_wal", 2026, pa_prest, "", "", "budgeted", src, "strong", "Parentia prestations 992.756m largest private ~33pct of 4-caisse"),
    ("bud_parentia_total_2026", "parentia_wal", 2026, pa_total_dep, "", "", "budgeted", src, "strong", "Parentia total dep 1016.931m"),
    ("bud_parentia_fonct_2026", "parentia_wal", 2026, pa_fonct, "", "", "budgeted", src, "strong", "Parentia fonct 24.175m; RW sub 21.258m"),
    ("bud_wal_af_prest_sum4_2026", "aviq", 2026, prest_sum4, "", "", "budgeted", src, "strong", f"Sum 4 CAF prestations {prest_sum4}; reconciles AViQ AF 3008.5m (+regulator path)"),
    ("bud_wal_af_admin_caf_2026", "aviq", 2026, fonct_all_caf, "", "", "budgeted", src, "strong", f"Sum CAF fonctionnement Famiwal+3 private ~{fonct_all_caf}; dual AViQ rem caisses 41.4m private subset"),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash = json.dumps(
    {
        "famiwal_total": fw_total,
        "famiwal_prest": fw_prest,
        "famiwal_fonct": fw_fonct,
        "famiwal_share_prest_pct": round(100 * fw_prest / prest_sum4, 1),
        "kidslife_prest": kl_prest,
        "camille_prest": ca_prest,
        "parentia_prest": pa_prest,
        "parentia_share_prest_pct": round(100 * pa_prest / prest_sum4, 1),
        "prest_sum4": prest_sum4,
        "aviq_af_dot": aviq_af,
        "aviq_private_caisses_rem": aviq_caisses_rem,
        "fonct_famiwal": fw_fonct,
        "fonct_private3": fonct_private,
        "admin_bps_famiwal": round(1e4 * fw_fonct / fw_prest, 1),
        "admin_bps_private_blended": round(1e4 * fonct_private / (kl_prest + ca_prest + pa_prest), 1),
        "dual_iriscare_af": 1081400000,
        "note": "Strong EPCO UAP tables; AF multi-caisse dual public/private; do not double-count with AViQ AF envelope",
    }
)

with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_wal_af_caf_channels_2026",
            "Wallonie AF multi-caisse channel map 2026 Famiwal+private",
            "aviq",
            "Households children Wallonia via 4 CAF",
            "Budget RW 2026 EPCO UAP type2/3 CAF tables",
            "2025-10-20",
            "2026",
            "2026",
            prest_sum4,
            cash,
            0,
            "active",
            url,
            "Deliver family benefits via public+private payment organisms",
            "Publish dual unit admin cost per dossier; open market-share series",
            src,
            "strong",
            "Wallonie>AVIQ>AF>CAF_channels",
            "tick238 dual Iriscare AF 1.08bn",
        ]
    )
    w.writerow(
        [
            "cmt_famiwal_2026",
            "Famiwal public CAF package 2026",
            "famiwal",
            "Public-channel family benefit recipients Wallonia",
            "EPCO UAP type2 Famiwal BI2026",
            "2025-10-20",
            "2026",
            "2026",
            fw_total,
            json.dumps(
                {
                    "total": fw_total,
                    "prest": fw_prest,
                    "fonct": fw_fonct,
                    "dot_rw": fw_dot_rw,
                    "personnel": fw_pers,
                    "note": "Public dual to Parentia KidsLife Camille",
                }
            ),
            0,
            "active",
            url,
            "Public family benefits payment organism",
            "Publish FTE and unit cost vs private CAF",
            src,
            "strong",
            "Wallonie>AVIQ>FAMIWAL",
            "tick238",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_famiwal_1_12bn",
            "Famiwal public CAF 1.12bn 2026",
            "Wallonia",
            "ops",
            "Wallonie>AF>FAMIWAL",
            fw_total,
            fw_total,
            "Strong EPCO: total 1118.8m prest 1080.9m fonct 37.0m; ~36pct of 4-caisse prest; dual private Parentia largest",
            "strong",
            src,
            "Public-channel AF recipients Wallonia",
            "Public family benefits payment",
            "Core statutory transfer channel; admin dual vs private CAF",
            3,
            8.0,
            4,
            5.8,
            "Publish dual unit admin cost per dossier vs Parentia/KidsLife/Camille",
            "seed",
            "",
            "tick238",
        ]
    )
    w.writerow(
        [
            "lb_wal_af_prest_3_01bn",
            "Wallonie AF prestations 4-caisse sum 3.01bn 2026",
            "Wallonia",
            "transfer",
            "Wallonie>AF>prestations",
            prest_sum4,
            prest_sum4,
            "Strong: Famiwal 1080.9 + Parentia 992.8 + Camille 579.6 + KidsLife 360.2 = 3013.5m; matches AViQ AF 3008.5m class",
            "strong",
            src,
            "All children Wallonia",
            "Family benefits multi-caisse delivery",
            "Statutory transfer not pure waste; dual channel admin residual",
            2,
            9.0,
            3,
            5.7,
            "Keep statutory; open admin unit-cost dual public/private",
            "seed",
            "",
            "tick238",
        ]
    )
    w.writerow(
        [
            "lb_parentia_993m",
            "Parentia private CAF prest 992.8m 2026",
            "Wallonia",
            "ops",
            "Wallonie>AF>Parentia",
            pa_prest,
            pa_total_dep,
            "Strong: largest private CAF ~33pct prest; fonct 24.2m RW sub 21.3m",
            "strong",
            src,
            "Parentia-channel AF recipients",
            "Private family benefits payment organism",
            "Core delivery; dual public Famiwal",
            3,
            8.0,
            4,
            5.8,
            "Publish dual unit cost vs Famiwal",
            "seed",
            "",
            "tick238",
        ]
    )
    w.writerow(
        [
            "lb_af_dual_channels_be",
            "AF dual payment channels WAL multi-caisse vs BRU Iriscare",
            "Belgium",
            "ops",
            "BE>AF>dual_channels",
            0,
            0,
            "Strong dual: WAL 3.01bn via 4 CAF (public Famiwal 36pct + private); BRU Iriscare AF 1.08bn; VL residual FOI; multi-caisse admin dual",
            "strong",
            src,
            "Households with children BE",
            "Family benefits payment organism dual",
            "Institutional dual/multi-caisse mechanism; admin opacity residual",
            5,
            8.5,
            5,
            6.55,
            "Map dual unit cost all regions; open market-share series",
            "seed",
            "",
            "tick238 dual not additive",
        ]
    )

# residual FOI: unit costs per dossier by caisse - optional medium prio
gap_id = "gap_wal_af_caf_unit_cost"
with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_id,
            "Wallonie>AVIQ>AF>CAF_unit_cost",
            "aviq",
            "Dossiers handled and admin cost per dossier by CAF 2023-2026 (Famiwal KidsLife Camille Parentia); reconcile AViQ rem 41.4m to private fonct lines",
            "Totals strong EPCO; dual public/private unit costs still opaque for waste map",
            5,
            "AViQ / FAMIWAL / SPW publicite",
            "",
            "https://www.wallonie.be",
            f"docs/doge/foi/drafts/{gap_id}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_wal_af_caf_channels_2026",
            "lb_af_dual_channels_be|lb_famiwal_1_12bn",
            utc,
            utc,
            "tick238 draft ready human send; public channel totals filled",
        ]
    )

rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_229":
            row["status"] = "done"
            row["updated_utc"] = utc
            row["blocked_gap_id"] = gap_id
            row["notes"] = (
                f"tick238: Famiwal 1118.8m prest 1080.9m; 4-CAF prest sum {prest_sum4}; Parentia 992.8m; dual Iriscare AF; FOI unit-cost ready; spawn rq_230"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_230",
        "title": "Continuous FOI-adjacent public hole-fill batch + progress@240 prep",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (Mons ASBL L5 if public; FPS taxex utilities SOE; "
            "VL AF/Groeipakket dual; other large FOI-adjacent). Note tick 240 is mandatory "
            "progress coverage % + waste top10. Do not idle while public work remains."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick238 after Famiwal AF dual; rq_116 SWA deferred; progress@240 in 2 ticks",
    }
)

with open(os.path.join(base, "research_queue.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(os.path.join(base, "loop_state.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            utc,
            "rq_229",
            238,
            "no",
            "Scheduler 60s. Next prio5 rq_230; rq_116 SWA deferred. FOI ready human send. tick238 Famiwal 1.12bn AF 4-CAF 3.01bn dual.",
        ]
    )

print("tick238 OK prest_sum4", prest_sum4, "famiwal", fw_total, "admin_bps_fw", round(1e4 * fw_fonct / fw_prest, 1))

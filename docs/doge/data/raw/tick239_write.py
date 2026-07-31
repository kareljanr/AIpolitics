# tick 239 VL Groeipakket dual AF map
import csv, os, json

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src_opg = "src_opgroeien_groeipakket_2025"
src_bbt = "src_vl_bbt_wvga_2026_tech_gp"
url_opg = "https://www.opgroeien.be/kennis/cijfers-en-onderzoek/vlaams-groeipakket"
url_bbt = "https://docs.vlaamsparlement.be/pfile?id=2247883"
utc = "2026-07-29T06:35:00Z"

gp_awarded_2025 = 4700000000  # approx 4.7bn official
children_eoy_2025 = 1600000  # more than 1.6m
families_eoy_2025 = 930010
vutg_admin_2026 = 42565000
zorgtoeslag_2026 = 144500000
private_cut_2026 = 1500000
recoveries_2026 = 34836000
cgpa_invest = 2500000
sociale_toeslag_children = 522148
zorgtoeslag_children = 51261

# dual comparators from prior ticks
wal_af_prest = 3013486000
bru_iriscare_af = 1081400000
wal_famiwal_admin = 36976000

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src_opg,
            "Opgroeien Vlaams Groeipakket cijferrapport 2025 awards and counts",
            url_opg,
            "Agentschap Opgroeien / VUTG",
            "2026-07-29",
            "official_statistics",
            "2025 awards ~4.7bn via payment actors; >1.6m children 930010 families eoy2025; sociale toeslag 522148 children; zorgtoeslag 51261; tick239",
        ]
    )
    w.writerow(
        [
            src_bbt,
            "BBT opmaak WVGA 2026 technische vragen Groeipakket VUTG",
            url_bbt,
            "Vlaams Parlement / Departement Zorg",
            "2026-07-29",
            "parliament",
            "VUTG BO26 uitgavenbudget 42.565m; zorgtoeslagen 144.5m 2026; private UA -1.5m; recoveries 34.836m; CGPA invest 2.5m; tick239; raw vl_bbt_wvga_2026_tech.pdf",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "vutg",
            "Agentschap Uitbetaling Groeipakket VUTG",
            "Agence paiement Pack croissance",
            "Flanders Agency for Payment of Growth Package",
            "agency",
            "opgroeien",
            "nl",
            "https://www.groeipakket.be",
            "openbaarheid@vlaanderen.be",
            "",
            "Public payment actor dual private FONS etc; admin BO26 42.565m; tick239",
        ]
    )

rows_b = [
    ("bud_groeipakket_awarded_2025", "opgroeien", 2025, gp_awarded_2025, 4650000000, 4750000000, "outturn", src_opg, "strong", "Opgroeien official: approx 4.7bn awarded 2025 via uitbetalingsactoren; range band for approx wording"),
    ("bud_vutg_admin_2026", "vutg", 2026, vutg_admin_2026, "", "", "budgeted", src_bbt, "strong", "VUTG BO26 uitgavenbudget 42.565m personnel+werking+invest public payment actor"),
    ("bud_groeipakket_zorgtoeslag_2026", "opgroeien", 2026, zorgtoeslag_2026, "", "", "budgeted", src_bbt, "strong", "Zorgtoeslagen budget 144.5m 2026 (+3.4m vs 2025 incl index)"),
    ("bud_groeipakket_private_ua_cut_2026", "opgroeien", 2026, private_cut_2026, "", "", "budgeted", src_bbt, "strong", "Efficiency cut 1.5m on private payment actors werkingsenveloppe BO2026"),
    ("bud_groeipakket_recoveries_2026", "opgroeien", 2026, recoveries_2026, "", "", "budgeted", src_bbt, "strong", "GDF-BGEFAQB-OW terugvorderingen raming 34.836m based on 2024 outturn private actors"),
    ("bud_groeipakket_cgpa_invest_2026", "vutg", 2026, cgpa_invest, "", "", "budgeted", src_bbt, "strong", "Centrale Groeipakketapplicatie invest budget 2.5m"),
    ("bud_be_af_dual_vl_wal_bru_class", "gg_belgium", 2025, 0, "", "", "synthesis", src_opg, "medium", "Dual AF class: VL ~4.7bn 2025 + WAL 3.01bn 2026 + BRU Iriscare 1.08bn 2026; do not sum years/perimeters; tick239 synthesis"),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash = json.dumps(
    {
        "awarded_2025_approx": gp_awarded_2025,
        "children_eoy_2025": children_eoy_2025,
        "families_eoy_2025": families_eoy_2025,
        "sociale_toeslag_children_dec2025": sociale_toeslag_children,
        "zorgtoeslag_children_eoy2025": zorgtoeslag_children,
        "vutg_admin_2026": vutg_admin_2026,
        "zorgtoeslag_budget_2026": zorgtoeslag_2026,
        "private_ua_cut_2026": private_cut_2026,
        "recoveries_2026": recoveries_2026,
        "admin_bps_vutg_vs_4_7bn": round(1e4 * vutg_admin_2026 / gp_awarded_2025, 2),
        "dual_wal_af_prest_2026": wal_af_prest,
        "dual_bru_iriscare_af_2026": bru_iriscare_af,
        "dual_wal_famiwal_admin": wal_famiwal_admin,
        "note": "Strong outturn 2025 awards; BO2026 full GEF2QY line residual FOI; dual multi-caisse WAL and Iriscare BRU",
    }
)

with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_groeipakket_2025_26",
            "Flanders Groeipakket awards + payment dual 2025-26",
            "opgroeien",
            "Families children Flanders via VUTG+private payment actors",
            "Opgroeien statistics + BBT WVGA 2026 tech Q",
            "2026-01-01",
            "2025",
            "2026",
            gp_awarded_2025,
            cash,
            0,
            "active",
            url_opg,
            "Universal family benefits Growth Package Flanders",
            "Publish exact BO2026 GEF2QY/FONS matrix; dual unit-cost VUTG vs private vs Famiwal",
            src_opg,
            "strong",
            "Vlaanderen>Opgroeien>Groeipakket",
            "tick239 dual WAL AF 3.01bn BRU Iriscare 1.08bn",
        ]
    )
    w.writerow(
        [
            "cmt_vutg_admin_2026",
            "VUTG public payment actor admin 2026",
            "vutg",
            "Public-channel Groeipakket recipients",
            "BBT WVGA BO2026 tech answers",
            "2025-12-01",
            "2026",
            "2026",
            vutg_admin_2026,
            json.dumps(
                {
                    "admin": vutg_admin_2026,
                    "cgpa_invest": cgpa_invest,
                    "private_cut": private_cut_2026,
                    "note": "Public dual private UA; private -1.5m efficiency",
                }
            ),
            0,
            "active",
            url_bbt,
            "Public Groeipakket payment organism admin",
            "Publish unit cost per dossier dual private",
            src_bbt,
            "strong",
            "Vlaanderen>Opgroeien>VUTG",
            "tick239",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_groeipakket_4_7bn",
            "Flanders Groeipakket awards ~4.7bn 2025",
            "Flanders",
            "transfer",
            "Vlaanderen>Groeipakket",
            gp_awarded_2025,
            gp_awarded_2025,
            "Strong Opgroeien: ~4.7bn awarded 2025 via payment actors; >1.6m children; dual WAL 3.01bn BRU 1.08bn",
            "strong",
            src_opg,
            "Families children Flanders",
            "Universal family benefits",
            "Statutory transfer not pure waste; multi-actor payment dual residual",
            2,
            9.5,
            3,
            6.0,
            "Publish exact BO2026 credit line; dual unit-cost payment actors",
            "seed",
            "",
            "tick239",
        ]
    )
    w.writerow(
        [
            "lb_vutg_admin_43m",
            "VUTG public Groeipakket admin 42.6m 2026",
            "Flanders",
            "ops",
            "Vlaanderen>Groeipakket>VUTG",
            vutg_admin_2026,
            vutg_admin_2026,
            "Strong BBT: 42.565m BO26; ~90 bps of 4.7bn awards class; dual private UA cut -1.5m",
            "strong",
            src_bbt,
            "Public-channel recipients",
            "Public payment organism admin",
            "Admin dual public/private; unit cost FOI residual",
            3,
            6.0,
            3,
            4.5,
            "Open unit cost per dossier dual private FONS",
            "seed",
            "",
            "tick239",
        ]
    )
    w.writerow(
        [
            "lb_be_af_triple_map",
            "BE family benefits triple VL~4.7bn WAL 3.01bn BRU 1.08bn",
            "Belgium",
            "transfer",
            "BE>AF>triple_community",
            0,
            0,
            "Strong dual map: VL Groeipakket ~4.7bn 2025 awards; WAL 4-CAF 3.01bn 2026; BRU Iriscare AF 1.08bn 2026; different years/perimeters do not sum",
            "strong",
            src_opg,
            "All children BE",
            "Community dual family benefits systems",
            "Institutional triple AF mechanism; payment-organism dual each region",
            4,
            9.5,
            5,
            6.7,
            "Publish same-year dual unit-cost all entities",
            "seed",
            "",
            "tick239 dual not additive",
        ]
    )
    w.writerow(
        [
            "lb_groeipakket_zorgtoeslag_145m",
            "Groeipakket zorgtoeslag 144.5m 2026",
            "Flanders",
            "transfer",
            "Vlaanderen>Groeipakket>zorgtoeslag",
            zorgtoeslag_2026,
            zorgtoeslag_2026,
            "Strong BBT: 144.5m 2026; 51261 children eoy2025 with zorgtoeslag",
            "strong",
            src_bbt,
            "Children with care needs Flanders",
            "Care supplement in Growth Package",
            "Statutory care-linked transfer",
            2,
            6.5,
            3,
            4.4,
            "Publish dual vs WAL handicap supplements",
            "seed",
            "",
            "tick239",
        ]
    )

gap_id = "gap_vl_groeipakket_bo2026_line"
with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_id,
            "Vlaanderen>Opgroeien>Groeipakket>BO2026_GEF2QY",
            "opgroeien",
            "Exact BO2026 VAK/VEK for GB0-1GEF2QX-IS and GB0-1GEF2QY-IS Groeipakket lines; private vs public payment actor admin cash-by-year 2023-2026; unit cost per dossier",
            "2025 awards ~4.7bn strong; VUTG admin 42.6m strong; full BO line codes and dual unit costs thin",
            5,
            "Opgroeien / VUTG / Team Openbaarheid",
            "openbaarheid@vlaanderen.be",
            "Havenlaan 88 bus 20 1000 Brussel",
            f"docs/doge/foi/drafts/{gap_id}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_groeipakket_2025_26",
            "lb_groeipakket_4_7bn|lb_be_af_triple_map",
            utc,
            utc,
            "tick239 draft ready human send",
        ]
    )

rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_230":
            row["status"] = "done"
            row["updated_utc"] = utc
            row["blocked_gap_id"] = gap_id
            row["notes"] = (
                "tick239: Groeipakket ~4.7bn 2025 awards; VUTG admin 42.6m; dual WAL 3.01bn BRU 1.08bn; FOI BO line ready; spawn rq_231; next tick progress@240"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_231",
        "title": "Mandatory progress@240 coverage % + waste top10",
        "sprint": "continuous",
        "priority": "6",
        "status": "open",
        "hierarchy_target": "L0",
        "entity_id": "gg_belgium",
        "instructions": (
            "When ticks_completed hits 240: refresh progress_every_10_ticks.md layers A-E "
            "vs EUR 347.956bn TE and doge_waste_top10_current.md by priority_index; "
            "append log; no invent euros."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick239; progress due tick 240",
    }
)
rows.append(
    {
        "task_id": "rq_232",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (Mons ASBL L5 if public; FPS taxex utilities SOE; "
            "other large FOI-adjacent) if new PDFs appear; else next open rq after progress@240."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick239 after Groeipakket dual; rq_116 SWA deferred",
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
            "rq_230",
            239,
            "no",
            "Scheduler 60s. Next: progress@240 (rq_231 prio6) then rq_232. rq_116 SWA deferred. tick239 Groeipakket 4.7bn dual AF.",
        ]
    )

print("tick239 OK")

# tick 236 VAPH dual Phare + VSB + Opgroeien from VL uitgavenbegroting 2026 decree
import csv, os, json

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src = "src_vl_uitgaven_decreet_2026_vaph"
url = "https://themis.vlaanderen.be/files/8cdc2070-aabe-11f0-9b44-3797f8128cc9/download"
utc = "2026-07-29T05:05:00Z"
gap_id = "gap_vaph_pvb_l5"

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src,
            "Ontwerp decreet uitgavenbegroting Vlaamse Gemeenschap 2026 (VAPH VSB Opgroeien totals)",
            url,
            "Vlaamse Regering / Vlaams Parlement (Themis)",
            "2026-07-29",
            "budget_decree",
            "Art37 VAPH rec 2865.4m VAK 3151.2m VEK 2865.4m; Art35 VSB 4748.5m; Art36 Opgroeien 7611.4m; PR GG 3121.8/2819.6m kEUR; dual Phare 210m; tick236; raw vaph_budget_2026.pdf",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "vaph",
            "Vlaams Agentschap voor Personen met een Handicap VAPH",
            "Agence flamande pour les personnes handicapees",
            "Flanders Agency for Persons with Disabilities",
            "agency",
            "sec_flanders",
            "nl",
            "https://www.vaph.be",
            "openbaarheid@vlaanderen.be",
            "Havenlaan 88 bus 20 1000 Brussel",
            "IVA; rec/VEK 2.865bn VAK 3.151bn 2026; dual Phare COCOF 0.21bn; tick236",
        ]
    )
    w.writerow(
        [
            "vsb",
            "Agentschap Vlaamse Sociale Bescherming VSB",
            "Agence flamande Protection sociale",
            "Flanders Social Protection Agency",
            "agency",
            "sec_flanders",
            "nl",
            "https://www.vlaamsesocialebescherming.be",
            "openbaarheid@vlaanderen.be",
            "",
            "IVA; rec/VEK 4.748bn VAK 4.382bn 2026; care budgets WZC; tick236",
        ]
    )
    w.writerow(
        [
            "opgroeien",
            "Agentschap Opgroeien / Opgroeien regie",
            "Agence Croissance",
            "Flanders Growing Up agency (childcare family youth)",
            "agency",
            "sec_flanders",
            "nl",
            "https://www.opgroeien.be",
            "openbaarheid@vlaanderen.be",
            "",
            "IVA Opgroeien regie; rec/VEK 7.611bn VAK 7.579bn 2026; Groeipakket open-end; tick236",
        ]
    )

rows_b = [
    ("bud_vaph_rec_2026", "vaph", 2026, 2865400000, "", "", "budgeted", src, "strong", "VAPH ontvangsten 2865.4m decree art37"),
    ("bud_vaph_vak_2026", "vaph", 2026, 3151217000, "", "", "budgeted", src, "strong", "VAPH uitgaven vastleggingen 3151.217m"),
    ("bud_vaph_vek_2026", "vaph", 2026, 2865400000, "", "", "budgeted", src, "strong", "VAPH uitgaven vereffeningen 2865.4m (=rec balanced cash class)"),
    ("bud_vl_pr_gg_beperking_vak_2026", "vaph", 2026, 3121780000, "", "", "budgeted", src, "strong", "PR GG Personen met een beperking VAK 3121.780m kEUR programme perimeter may exceed pure VAPH"),
    ("bud_vl_pr_gg_beperking_vek_2026", "vaph", 2026, 2819590000, "", "", "budgeted", src, "strong", "PR GG Personen met een beperking VEK 2819.590m kEUR"),
    ("bud_vsb_rec_2026", "vsb", 2026, 4748450000, "", "", "budgeted", src, "strong", "VSB ontvangsten 4748.45m art35"),
    ("bud_vsb_vak_2026", "vsb", 2026, 4381513000, "", "", "budgeted", src, "strong", "VSB uitgaven VAK 4381.513m"),
    ("bud_vsb_vek_2026", "vsb", 2026, 4748450000, "", "", "budgeted", src, "strong", "VSB uitgaven VEK 4748.45m"),
    ("bud_opgroeien_rec_2026", "opgroeien", 2026, 7611411000, "", "", "budgeted", src, "strong", "Opgroeien regie ontvangsten 7611.411m art36"),
    ("bud_opgroeien_vak_2026", "opgroeien", 2026, 7578928000, "", "", "budgeted", src, "strong", "Opgroeien regie VAK 7578.928m"),
    ("bud_opgroeien_vek_2026", "opgroeien", 2026, 7611411000, "", "", "budgeted", src, "strong", "Opgroeien regie VEK 7611.411m"),
    ("bud_vl_wvg_triple_iva_vek_2026", "sec_flanders", 2026, 15225261000, "", "", "budgeted", src, "strong", "Sum VEK VAPH+VSB+Opgroeien 2.865+4.748+7.611=15.225bn class; not additive with WVG programme double-count caution"),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash_vaph = json.dumps(
    {
        "rec": 2865400000,
        "vak": 3151217000,
        "vek": 2865400000,
        "pr_gg_vak": 3121780000,
        "pr_gg_vek": 2819590000,
        "dual_phare_cocof_liq": 210270000,
        "scale_ratio_vek_vs_phare": round(2865400000 / 210270000, 1),
        "note": "Strong decree art37; dual Phare COCOF ~14x smaller; PVB L5 residual FOI",
    }
)
cash_vsb = json.dumps(
    {
        "rec": 4748450000,
        "vak": 4381513000,
        "vek": 4748450000,
        "note": "Strong art35; WZC/care open-end; dual federal residual",
    }
)
cash_opg = json.dumps(
    {
        "rec": 7611411000,
        "vak": 7578928000,
        "vek": 7611411000,
        "berrefonds_max": 207163,
        "note": "Strong art36; Groeipakket open-end; youth delinquency transfer to Justitie 2026",
    }
)

with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_vaph_budget_2026",
            "VAPH disability agency package 2026 dual Phare",
            "vaph",
            "Persons with disabilities Flanders PVB care providers",
            "Uitgavendecreet VL 2026 art37",
            "2025-10-01",
            "2026",
            "2026",
            3151217000,
            cash_vaph,
            0,
            "active",
            url,
            "Personal budgets and care for persons with disabilities Flanders",
            "Publish PVB top operators L5; dual unit-cost vs Phare COCOF/AViQ",
            src,
            "strong",
            "Vlaanderen>WVG>VAPH",
            "tick236; dual Phare 210m",
        ]
    )
    w.writerow(
        [
            "cmt_vsb_budget_2026",
            "Vlaamse Sociale Bescherming agency package 2026",
            "vsb",
            "Elderly care WZC short-stay day-care insureds",
            "Uitgavendecreet VL 2026 art35",
            "2025-10-01",
            "2026",
            "2026",
            4748450000,
            cash_vsb,
            0,
            "active",
            url,
            "Flanders social protection care budgets",
            "Open end-receiver L5 care providers; dual federal RIZIV residual",
            src,
            "strong",
            "Vlaanderen>WVG>VSB",
            "tick236",
        ]
    )
    w.writerow(
        [
            "cmt_opgroeien_budget_2026",
            "Opgroeien regie agency package 2026",
            "opgroeien",
            "Families children childcare youth Flanders",
            "Uitgavendecreet VL 2026 art36",
            "2025-10-01",
            "2026",
            "2026",
            7611411000,
            cash_opg,
            0,
            "active",
            url,
            "Childcare family youth Groeipakket open-end",
            "Publish Groeipakket cash path; dual COCOM family benefits residual",
            src,
            "strong",
            "Vlaanderen>WVG>Opgroeien",
            "tick236",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_vaph_2_87bn",
            "VAPH disability VEK 2.87bn 2026 dual Phare",
            "Flanders",
            "ops",
            "Vlaanderen>WVG>VAPH",
            2865400000,
            3151217000,
            "Strong decree: rec=VEK 2.865bn VAK 3.151bn; dual Phare COCOF 0.21bn ~14x; core social not pure waste",
            "strong",
            src,
            "Persons with disabilities Flanders",
            "Personal budgets disability care",
            "Core social duty; waiting lists public issue; L5 PVB operators residual",
            3,
            9.0,
            5,
            6.8,
            "Open PVB top operators; dual unit-cost Phare/AViQ",
            "seed",
            "",
            "tick236",
        ]
    )
    w.writerow(
        [
            "lb_vsb_4_75bn",
            "Vlaamse Sociale Bescherming 4.75bn 2026",
            "Flanders",
            "ops",
            "Vlaanderen>WVG>VSB",
            4748450000,
            4748450000,
            "Strong art35: rec=VEK 4.748bn VAK 4.382bn; WZC care open-end",
            "strong",
            src,
            "Elderly and care recipients Flanders",
            "Social protection care financing",
            "Core social; dual federal residual",
            2,
            9.0,
            4,
            6.2,
            "Publish provider L5 matrix",
            "seed",
            "",
            "tick236",
        ]
    )
    w.writerow(
        [
            "lb_opgroeien_7_61bn",
            "Opgroeien regie 7.61bn 2026",
            "Flanders",
            "ops",
            "Vlaanderen>WVG>Opgroeien",
            7611411000,
            7611411000,
            "Strong art36: rec=VEK 7.611bn VAK 7.579bn; Groeipakket open-end dominant class",
            "strong",
            src,
            "Families children Flanders",
            "Child family youth agency",
            "Core social/transfer; dual COCOM AF residual",
            2,
            9.5,
            4,
            6.45,
            "Publish Groeipakket multi-year path",
            "seed",
            "",
            "tick236",
        ]
    )
    w.writerow(
        [
            "lb_disability_dual_vaph_phare",
            "Disability dual VAPH 2.87bn vs Phare 0.21bn",
            "Belgium",
            "ops",
            "BE>Disability>dual_VL_BRU",
            0,
            0,
            "Strong dual: Flanders VAPH VEK 2.865bn vs COCOF Phare 0.210bn 2026; not population-adjusted unit-cost; dual AViQ residual",
            "strong",
            src,
            "Persons with disabilities BE",
            "Community dual disability systems",
            "Institutional dual layer mechanism; scale gap not pure waste claim without unit costs",
            5,
            8.5,
            5,
            6.55,
            "Publish dual unit-cost per beneficiary; open L5 both sides",
            "seed",
            "",
            "tick236 dual not additive",
        ]
    )

with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_id,
            "Vlaanderen>VAPH>PVB_operators_L5",
            "vaph",
            "Top PVB/zorgaanbieder named EUR cash 2024-2026; waiting list stock EUR class; reconcile VAK 3.151bn vs VEK 2.865bn underbenutting path",
            "Agency totals strong public; end-receiver L5 and dual unit-cost vs Phare opaque",
            6,
            "VAPH / Team Openbaarheid Vlaanderen",
            "openbaarheid@vlaanderen.be",
            "Havenlaan 88 bus 20 1000 Brussel",
            f"docs/doge/foi/drafts/{gap_id}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_vaph_budget_2026",
            "lb_vaph_2_87bn|lb_disability_dual_vaph_phare",
            utc,
            utc,
            "tick236 draft ready human send; dual Phare mapped",
        ]
    )

rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_227":
            row["status"] = "done"
            row["updated_utc"] = utc
            row["blocked_gap_id"] = gap_id
            row["notes"] = (
                "tick236: VAPH VEK 2.865bn VAK 3.151bn dual Phare 210m; VSB 4.748bn; Opgroeien 7.611bn; FOI PVB L5 ready; spawn rq_228"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_228",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (AViQ Wallonia dual VAPH; Mons ASBL L5 if public; "
            "FPS taxex utilities SOE; other large FOI-adjacent) if new PDFs appear; "
            "else next open rq; do not idle while public work remains."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick236 after VAPH 2.87bn VSB 4.75bn Opgroeien 7.61bn; rq_116 SWA deferred",
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
            "rq_227",
            236,
            "no",
            "Scheduler 60s. Next prio5 rq_228; rq_116 SWA deferred. FOI ready human send. tick236 VAPH 2.87bn VSB 4.75bn Opgroeien 7.61bn dual Phare.",
        ]
    )

print("tick236 OK")

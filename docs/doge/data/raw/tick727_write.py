# tick727 — internal security dual-use + antifraud delivery residual dual L5 (rq_718)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T00:15:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

SRC = "src_ccrek_fed_aju2026_intsec_antifraud_residual"
SRC_DUAL = "src_dual_intsec_antifraud_tick727"

budgets = [
    # Antifraud fiscal yields (recon + residual delivery)
    ("bud_antifraud_fiscal_yield_2026", "sec_federal", 2026, 300000000, "", "", "budgeted", SRC, "strong", "Fiscal fraud yield claim 300m structural 2026 CoA; no method from FPS Finance; tick727"),
    ("bud_antifraud_fiscal_yield_2029", "sec_federal", 2029, 600000000, "", "", "budgeted", SRC, "strong", "Fiscal fraud yield claim 600m 2029 path; method still missing at aju; tick727"),
    ("bud_antifraud_social_yield_2026", "sec_ss", 2026, 300000000, "", "", "budgeted", SRC, "strong", "Social fraud additional yield claim 300m 2026 unchanged since early 2025; no measure split; tick727"),
    ("bud_antifraud_social_yield_2027", "sec_ss", 2027, 375000000, "", "", "budgeted", SRC, "strong", "Social fraud path 375m 2027 (+75); tick727"),
    ("bud_antifraud_social_yield_2028", "sec_ss", 2028, 450000000, "", "", "budgeted", SRC, "strong", "Social fraud path 450m 2028 (+75); tick727"),
    ("bud_antifraud_social_yield_2029", "sec_ss", 2029, 600000000, "", "", "budgeted", SRC, "strong", "Social fraud path 600m 2029 (+150); no L5 measure matrix CoA; tick727"),
    ("bud_antifraud_dual_pack_2026", "sec_federal", 2026, 600000000, "", "", "budgeted", SRC, "strong", "Dual fiscal+social antifraud booked 600m 2026; method dual opaque; tick727"),
    ("bud_antifraud_dual_pack_2029", "sec_federal", 2029, 1200000000, "", "", "budgeted", SRC, "strong", "Dual antifraud path 1.2bn 2029 (600 fiscal + 600 social); tick727"),
    ("bud_parquet_financier_yield_2029_recon", "fod_justice", 2029, 196000000, "", "", "budgeted", SRC, "weak", "Financial parket yield claim 196m 2029; no execution/method; bill DOC56 1536/001 just filed; tick727"),
    # Staffing residual (counts + delivery lag)
    ("bud_antifraud_fte_bbi_150", "fod_finance", 2026, 150, "", "", "budgeted", SRC, "strong", "COUNT planned BBI VTE 150 antifraud; CoA: FPS Finance recruit NOT started; tick727"),
    ("bud_antifraud_fte_justice_107", "fod_justice", 2026, 107, "", "", "budgeted", SRC, "strong", "COUNT planned Justice VTE 107 antifraud; CoA: recruit NOT started; tick727"),
    ("bud_antifraud_fte_police_130", "police_federale", 2026, 130, "", "", "budgeted", SRC, "strong", "COUNT planned Federal Police VTE 130 antifraud; tick727"),
    ("bud_antifraud_fte_total_387", "sec_federal", 2026, 387, "", "", "budgeted", SRC, "strong", "COUNT planned antifraud staff 150+107+130=387; tick727"),
    ("bud_antifraud_fte_police_live_18_oct2026", "police_federale", 2026, 18, "", "", "outturn", SRC, "strong", "COUNT Federal Judicial Police only 18 staff by 1 Oct 2026 via internal mobility; tick727"),
    ("bud_antifraud_fte_police_gap_112", "police_federale", 2026, 112, "", "", "estimate", SRC, "strong", "COUNT police staffing gap 130-18=112 residual vs plan; tick727"),
    ("bud_antifraud_fte_finance_justice_started_0", "sec_federal", 2026, 0, "", "", "outturn", SRC, "strong", "COUNT recruit procedures FPS Finance+Justice NOT started at CoA aju; tick727"),
    # Internal security dual-use residual
    ("bud_intsec_sect16_177m_2026", "mod_defensie", 2026, 177000000, "", "", "budgeted", SRC, "strong", "Internal security from sect16 VEK 177m 2026 (5pct additional defence if NATO-class); tick727 recon"),
    ("bud_intsec_nato_trust_45m_fa", "fod_foreign_affairs", 2026, 45000000, "", "", "budgeted", SRC, "strong", "NATO trust fund 45m in FA sect14 (not sect16 as initially planned); tick727"),
    ("bud_intsec_pack_222m_2026", "mod_defensie", 2026, 222000000, "", "", "budgeted", SRC, "strong", "Internal security pack 177+45=222m if trust included per MR 18Jul2025; tick727"),
    ("bud_intsec_scattered_ba_tracking_hard", "mod_defensie", 2026, 177000000, "", "", "budgeted", SRC, "strong", "177m assigned to existing programmes/BAs of sect16 — tracking difficult CoA; tick727"),
    ("bud_security_return_prov_546m_recon", "sec_federal", 2026, 546000000, "", "", "budgeted", SRC, "strong", "ID provisie security services+return 546m VEK Justice/IBZ/Police; tick727 recon"),
    ("bud_security_return_prov_carry_179m", "sec_federal", 2026, 179000000, "", "", "budgeted", SRC, "strong", "Unused 2025 security/return credits +179m loaded on 2026 provisie; tick727"),
    ("bud_support_cell_security_prov_plus_178_8m", "fod_bosa", 2026, 178800000, "", "", "budgeted", SRC, "strong", "Support cell: security provisie +178.8m BC vs IB; tick727"),
    ("bud_support_cell_id_prov_minus_207_4m", "fod_bosa", 2026, -207400000, "", "", "budgeted", SRC, "strong", "Support cell: ID provisies transferred out -207.4m; tick727"),
    ("bud_support_cell_index_minus_485_2m", "fod_bosa", 2026, -485200000, "", "", "budgeted", SRC, "strong", "Support cell: index provisie allocated out -485.2m; tick727"),
    ("bud_support_cell_new_policy_plus_40_6m", "fod_bosa", 2026, 40600000, "", "", "budgeted", SRC, "strong", "Support cell: new policy provisie +40.6m; tick727"),
    ("bud_authority_cell_plus_390m", "sec_federal", 2026, 390000000, "", "", "budgeted", SRC, "strong", "Authority cell VEK +390m (Def +188.2 Interior +100 Justice +81); tick727"),
    ("bud_justice_section_2925m_aju", "fod_justice", 2026, 2925000000, "", "", "budgeted", SRC, "strong", "Justice section VEK 2925m aju (+81); of which personnel +39.5m; tick727"),
    ("bud_interior_plus_100m_aju", "fod_interior", 2026, 100000000, "", "", "budgeted", SRC, "strong", "Interior +100m aju of which Fedasil 41.6; tick727"),
    ("bud_defence_sect16_plus_188_2m", "mod_defensie", 2026, 188200000, "", "", "budgeted", SRC, "strong", "Defence sect16 +188.2m for NATO 2pct path; tick727"),
    # Named dual-use items (amounts Unknown — flag as 0 with note; no invent)
    ("bud_intsec_fed_police_heli_class", "police_federale", 2026, 0, "", "", "unknown", SRC, "medium", "Named dual-use: Fed Police helicopter purchase in intsec pack; military share unclear CoA; EUR FOI; tick727"),
    ("bud_intsec_belspo_plane_class", "belspo", 2026, 0, "", "", "unknown", SRC, "medium", "Named dual-use: BELSPO plane in intsec pack; military share unclear CoA; EUR FOI; tick727"),
    ("bud_intsec_cuas_police_class", "police_federale", 2026, 0, "", "", "unknown", SRC, "medium", "Named dual-use: C-UAS police credits (drone detect/neutralise) in intsec; military share unclear; EUR FOI; tick727"),
    ("bud_intsec_bsc_class", "mod_defensie", 2026, 0, "", "", "unknown", SRC, "medium", "Named dual-use: Belgian Secure Communications (BSC AR 17Jul2024) credits in intsec; military share unclear; EUR FOI; tick727"),
    ("bud_intsec_fipa_no_reimburse_class", "mod_defensie", 2026, 0, "", "", "budgeted", SRC, "strong", "MR 20Mar2026: Defence support Fed Police mixed rail patrols + FIPA Brussels charged to intsec without Police reimburse (law 7Dec1998); amount in 177 pack; tick727"),
    # Dual
    ("bud_dual_intsec_antifraud_soft_pack", "gg_belgium", 2026, 822000000, "", "", "estimate", SRC_DUAL, "medium", "Dual class: intsec 222m + antifraud 600m 2026 soft/opaque packs not TE-additive pure waste; tick727"),
    ("bud_nato_effort_bc_13296m", "mod_defensie", 2026, 13296000000, "", "", "budgeted", SRC, "strong", "NATO effort BC 13296m (GDP 664778); fill 13246 gap ~50; tick727 recon"),
    ("bud_nato_fill_budget_10958m", "mod_defensie", 2026, 10958000000, "", "", "budgeted", SRC, "strong", "Defence budget fill 10958m BC; tick727"),
    ("bud_nato_fill_external_2288m", "mod_defensie", 2026, 2288000000, "", "", "budgeted", SRC, "strong", "External defence effort 2288m (pens 1988 -40 FPD; norm 168; COFOG 131); tick727"),
    ("bud_nato_fill_total_13246m", "mod_defensie", 2026, 13246000000, "", "", "budgeted", SRC, "strong", "Total defence effort fill 13246m vs target 13296 gap ~50m; tick727"),
    ("bud_primary_vek_cells_92050m", "sec_federal", 2026, 92050000000, "", "", "budgeted", SRC, "strong", "Primary VEK cells total BC 92050 (+41 vs IB 92009); tick727"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_antifraud_staffing_lag_2026",
        "Antifraud staffing lag 387 FTE plan vs almost zero live recruit",
        "sec_federal",
        "Taxpayers compliant firms workers",
        "CoA 2026_22 s3.2.3 antifraud residual",
        "2026-05-21",
        2026,
        2029,
        0,
        '{"bbi_vte":150,"justice_vte":107,"police_vte":130,"total":387,"finance_recruit_started":false,"justice_recruit_started":false,"police_live_by_2026_10_01":18,"police_via":"internal_mobility","fiscal_yield_2026_m":300,"fiscal_2029_m":600,"social_2026_m":300,"social_2029_m":600,"parquet_2029_m":196,"bill":"DOC56_1536/001","method":"missing"}',
        0,
        "active",
        URL,
        "Raise compliance revenue via staffed controls",
        "Do not book yields until staff live + method published FOI",
        SRC,
        "strong",
        "Federal>antifraud>staffing_lag",
        "tick727 residual dual intsec",
    ),
    (
        "cmt_intsec_dual_use_177m_named",
        "Internal security 177m dual-use mixed civil-military named items",
        "mod_defensie",
        "Police BELSPO Defence taxpayers NATO",
        "CoA 2026_22 s2.3.2 + MR Apr/Jul/Dec2025 Mar2026",
        "2025-04-11",
        2026,
        2026,
        222000000,
        '{"sect16_m":177,"nato_trust_fa_m":45,"pack_m":222,"scattered_ba":true,"named":["fed_police_heli","belspo_plane","C-UAS_police","BSC"],"military_share":"unclear","fipa_no_reimburse":true,"mr_fipa":"2026-03-20","specialty_risk":true,"normering_needed":true}',
        0,
        "active",
        URL,
        "Internal resilience if NATO-classifiable 5pct rule",
        "Publish military-share matrix + EUR per named item FOI; restore specialty",
        SRC,
        "strong",
        "Federal>Defence>internal_security_dual_use",
        "tick727",
    ),
    (
        "cmt_security_return_prov_546_carry",
        "Security/return ID provisie 546m +179 carry specialty dual Justice IBZ Police",
        "sec_federal",
        "Justice Interior Federal Police return chain",
        "CoA 2026_22 s2.1.1 + support cell table",
        "2025-12-12",
        2026,
        2029,
        546000000,
        '{"prov_m":546,"carry_2025_m":179,"support_security_plus_m":178.8,"split_depts":["Justice","Interior","Police"],"specialty_breach":true}',
        0,
        "active",
        URL,
        "Reinforce security services and return policy",
        "Move known amounts to sections; L5 project list FOI",
        SRC,
        "strong",
        "Federal>BOSA>security_return_provisie",
        "tick727",
    ),
    (
        "cmt_parquet_financier_bill_196m",
        "Financial parket yield 196m 2029 bill just filed no execution path",
        "fod_justice",
        "Financial crime cases taxpayers",
        "CoA 2026_22 + DOC 56 1536/001",
        "2026-05-21",
        2026,
        2029,
        196000000,
        '{"yield_2029_m":196,"method":"missing","execution":"unknown","bill":"DOC56_1536/001","status":"just_filed"}',
        196000000,
        "active",
        URL,
        "Independent financial crime prosecution capacity",
        "Link yield to staff/org chart FOI before booking",
        SRC,
        "strong",
        "Federal>Justice>parquet_financier",
        "tick727",
    ),
    (
        "cmt_fipa_mixed_patrols_no_reimburse",
        "FIPA + mixed rail patrols Defence support without Police reimburse",
        "mod_defensie",
        "Brussels territory + rail police zone",
        "MR 20 Mar 2026 point16 + law 7 Dec 1998 + CoA 2.3.2",
        "2026-03-20",
        2026,
        2026,
        0,
        '{"charged_to":"internal_security_budget","reimburse":false,"legal_basis_law":"1998-12-07","command":"Federal_Police","note":"amount inside 177m pack FOI"}',
        0,
        "active",
        URL,
        "Joint security operations",
        "Invoice or disclose unit cost FOI dual specialty",
        SRC,
        "strong",
        "Federal>Defence_Police>FIPA",
        "tick727",
    ),
    (
        "cmt_dual_intsec_antifraud_tick727",
        "Dual internal security dual-use opacity + antifraud soft yields",
        "gg_belgium",
        "Federal taxpayers security compliance",
        "CoA 2026_22 residual dual",
        "2026-05-21",
        2026,
        2029,
        822000000,
        '{"intsec_pack_m":222,"antifraud_2026_m":600,"staff_live_near_zero":true,"named_dual_use":true,"note":"not TE-additive; both soft/opaque delivery"}',
        0,
        "active",
        URL,
        "Honest dual security and compliance accounting",
        "Publish L5 military share + antifraud method FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>intsec_antifraud",
        "tick727",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_antifraud_staffing_dead_2026",
        "Antifraud 600m 2026 booked while Finance/Justice recruit not started",
        "federal",
        "ops",
        "Federal>antifraud>staffing_dead",
        600000000,
        1200000000,
        "Strong CoA residual: 150+107+130 FTE planned; Finance+Justice procedures not started; Police only 18 by Oct2026; yields methodless",
        "strong",
        SRC,
        "Taxpayers",
        "Compliance revenue",
        "Soft yield booking without staff delivery",
        8.5,
        8.0,
        4,
        7.75,
        "Unbook until staff live + method L5",
        "seed",
        "",
        "tick727",
    ),
    (
        "lb_antifraud_police_18_of_130",
        "Federal Judicial Police antifraud only 18 of 130 FTE by Oct2026",
        "federal",
        "ops",
        "Federal>Police>antifraud_FTE",
        0,
        0,
        "Strong CoA: 18 via internal mobility by 1 Oct 2026 vs plan 130; gap 112",
        "strong",
        SRC,
        "Compliance enforcement",
        "Staffed fraud investigation",
        "14pct of planned police FTE path",
        7.5,
        5.5,
        4,
        6.55,
        "Accelerate external hire FOI calendar",
        "seed",
        "",
        "tick727",
    ),
    (
        "lb_intsec_dual_use_opaque_177m",
        "Internal security 177m dual-use military share unclear (heli/plane/C-UAS/BSC)",
        "federal",
        "ops",
        "Federal>Defence>intsec_dual_use",
        177000000,
        222000000,
        "Strong CoA: named mixed civil-military items without clear military component; scatters across BAs; specialty risk; NATO definition issue",
        "strong",
        SRC,
        "NATO/COFOG classifiers taxpayers",
        "Accountable internal resilience spend",
        "Dual-use opacity inside defence section",
        8.0,
        7.0,
        5,
        7.15,
        "Military-share matrix + named EUR FOI",
        "seed",
        "",
        "tick727",
    ),
    (
        "lb_intsec_fipa_no_reimburse",
        "FIPA/mixed patrols Defence cost on intsec without Police reimburse",
        "federal",
        "governance",
        "Federal>Defence_Police>FIPA",
        0,
        0,
        "Strong CoA+MR 20Mar2026: charged to intsec budget; law 1998 no reimburse; amount inside 177m",
        "strong",
        SRC,
        "Brussels rail security",
        "Joint ops with honest costing",
        "Cross-dept free-ride accounting",
        7.0,
        5.0,
        4,
        6.15,
        "Disclose unit cost or invoice FOI",
        "seed",
        "",
        "tick727",
    ),
    (
        "lb_security_return_prov_546_specialty",
        "Security/return provisie 546m +179 carry specialty breach dual 3 depts",
        "federal",
        "governance",
        "Federal>BOSA>security_provisie",
        546000000,
        725000000,
        "Strong CoA: ID provisie Justice/Interior/Police; specialty hollow; support cell security +178.8m",
        "strong",
        SRC,
        "Parliament specialty principle",
        "Transparent security financing",
        "Off-section opacity multi-dept",
        7.5,
        8.0,
        5,
        7.15,
        "Inscribe known uses in sections FOI L5",
        "seed",
        "",
        "tick727",
    ),
    (
        "lb_parquet_financier_196m_soft",
        "Financial parket 196m 2029 yield soft — bill just filed no method",
        "federal",
        "ops",
        "Federal>Justice>parquet_financier",
        196000000,
        196000000,
        "Strong CoA: yield claim without execution path; DOC56 1536/001 just submitted",
        "strong",
        SRC,
        "Financial crime victims taxpayers",
        "Independent financial crime capacity",
        "Booked yield before org exists",
        8.0,
        6.5,
        4,
        7.15,
        "Gate yield on enacted law + staff plan FOI",
        "seed",
        "",
        "tick727",
    ),
    (
        "lb_dual_intsec_antifraud_soft_2026",
        "Dual intsec dual-use 222m + antifraud 600m soft packs 2026",
        "Belgium",
        "ops",
        "Belgium>dual>intsec_antifraud",
        822000000,
        0,
        "Strong dual residual: both delivery-opaque; staffing near-zero vs booked yields; not TE-additive",
        "strong",
        SRC_DUAL,
        "Federal fiscal honesty",
        "Honest security+compliance path",
        "Stacked soft savings/spend opacity",
        8.0,
        7.5,
        5,
        7.35,
        "Publish dual L5 method+staff calendar",
        "seed",
        "",
        "tick727",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

sources = [
    (
        SRC,
        "CoA federal BA2026 residual internal security dual-use + antifraud staffing (2026_22 s2.3.2 + s3.2.3)",
        URL,
        "Cour des comptes / Rekenhof AG 21 May 2026",
        "2026-08-02",
        "court_of_audit",
        "Strong tick727 residual: intsec 177/222 named heli plane C-UAS BSC FIPA; security provisie 546+179; antifraud fiscal 300/600 social 300-600; parquet 196 bill 1536; FTE 150/107/130 with Finance+Justice recruit not started Police 18/130; support cell security +178.8; raw ccrek_2026_22_fed_aju.pdf",
    ),
    (
        SRC_DUAL,
        "Dual internal security dual-use opacity + antifraud soft yields tick727",
        URL,
        "DOGE synthesis CoA 2026_22 residual dual",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: intsec 222m dual-use + antifraud 600m methodless with dead staffing; tick727",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in sources:
        w.writerow(r)
print("sources +", len(sources))

# research_queue
rq_path = DATA / "research_queue.csv"
rows = []
with open(rq_path, encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_718":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick727 intsec dual-use residual: 177/222 named heli/plane/C-UAS/BSC FIPA; "
                "antifraud staffing dead 387 plan Police 18; FOI gap_intsec_dual_use_antifraud_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_719",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: new CoA/primary PDF not yet mined or WAL UAP residual or "
        "named intsec EUR matrix if published or Entity II dual residual"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick727 after rq_718",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_718=done spawn rq_719")

foi_row = (
    "gap_intsec_dual_use_antifraud_l5",
    "Federal>Defence_Police_Finance>intsec_dual_use_antifraud_L5",
    "sec_federal",
    (
        "Named EUR amounts and military-share percentages for internal security items inside sect16 177m "
        "(Fed Police helicopter; BELSPO plane; C-UAS police; BSC; FIPA/mixed rail patrol unit costs); "
        "BA-level map of 177m scatter; security/return provisie 546m L5 split Justice/IBZ/Police cash path; "
        "antifraud hiring calendar cash for 150 BBI + 107 Justice + 130 Police with current headcount; "
        "method notes for fiscal 300/600 and social 300-600 yield claims; financial parket org chart vs 196m path"
    ),
    (
        "CoA residual dual-use and soft antifraud yields material: NATO classification integrity + "
        "1.2bn dual antifraud path with near-zero live recruit"
    ),
    "8",
    "Ministerie van Landsverdediging / Federale Politie / FOD Financiën BBI / FOD Justitie / FOD BOSA",
    "",
    "https://www.ibz.be/nl/openbaarheid-van-bestuur",
    "docs/doge/foi/drafts/gap_intsec_dual_use_antifraud_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_intsec_dual_use_177m_named|cmt_antifraud_staffing_lag_2026|cmt_fipa_mixed_patrols_no_reimburse",
    "lb_intsec_dual_use_opaque_177m|lb_antifraud_staffing_dead_2026|lb_dual_intsec_antifraud_soft_2026",
    UTC,
    UTC,
    "tick727 CoA residual dual; not sent; related gap_antifraud_method_l5 + gap_fed_aju2026_defence_nato_l5 remain ready",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi +1 ready")

# loop_state
with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    rows_s = list(csv.reader(f))
header, row = rows_s[0], rows_s[1]
row[3] = UTC
row[4] = "rq_718"
row[5] = "727"
row[7] = (
    "tick727 intsec dual-use + antifraud staffing residual; next rq_719; "
    "progress@730 in 3; rq_116 deferred"
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(header)
    w.writerow(row)
print("loop_state ticks=727 DONE")

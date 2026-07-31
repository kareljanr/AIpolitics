# tick 316 — HR Rail dual deepen via Infrabel AR2024 FTE + payroll charge
from pathlib import Path

base = Path("docs/doge/data")

def append(name: str, text: str) -> None:
    path = base / name
    with open(path, "a", encoding="utf-8", newline="") as f:
        if not text.endswith("\n"):
            text += "\n"
        f.write(text)

append(
    "sources.csv",
    "src_infrabel_ar2024_en_fte,Infrabel Annual Report 2024 EN key figures FTE payroll services,"
    "https://infrabel.be/sites/default/files/generated/files/report/INFRABEL_Annual%20Report%202024_EN.pdf,"
    "Infrabel,2026-07-30,primary,"
    '"Strong: YE FTE 9402.1 2024 / 9536 2023; avg FTE salary series 2020-24; payroll under services '
    '809.61m 2024 / 775.76m 2023; HR Rail stake 49pct; raw infrabel_ar2024_en.pdf"\n'
    "src_hr_rail_companyweb_nbb_2025_refresh,HR Rail NV PR Companyweb NBB multi-year refresh YE2025,"
    "https://www.companyweb.be/nl/0541691352/hr-rail; https://consult.cbso.nbb.be/consult-enterprise/0541691352,"
    "Companyweb (NBB CBSO),2026-07-30,nbb,"
    '"Strong-medium: omzet 2078/2206/2305/2368m 2022-25; FTE 27435/27524/27568/27811; '
    'net 9.20/2.96/0.69/1.57m; equity 28.3m 2025; filing 10-06-2026"',
)

# entity note refresh
ents = (base / "entities.csv").read_text(encoding="utf-8")
old_ent = (
    "hr_rail,HR Rail NV van publiek recht,HR Rail SA de droit public,"
    "HR Rail public limited company,parastatal,sec_federal,bi,https://www.hr-rail.be,,"
    "Frankrijkstraat 85 1060 Sint-Gillis,"
    "Legal employer all NMBS+Infrabel staff (KB 11 Dec 2013); omzet ~2.37bn 2025 pass-through payroll; "
    "FTE 27811; dual rail structure; tick166"
)
new_ent = (
    "hr_rail,HR Rail NV van publiek recht,HR Rail SA de droit public,"
    "HR Rail public limited company,parastatal,sec_federal,bi,https://www.hr-rail.be,,"
    "Frankrijkstraat 85 1060 Sint-Gillis,"
    "Legal employer all NMBS+Infrabel staff (KB 11 Dec 2013); omzet 2.368bn 2025; FTE 27811; "
    "Infrabel YE FTE 9402 dual residual ~18k NMBS class; Infrabel payroll services 809.6m 2024; "
    "Infrabel owns 49pct HR Rail; tick166+316"
)
if old_ent not in ents:
    raise SystemExit("hr_rail entity row not found")
(base / "entities.csv").write_text(ents.replace(old_ent, new_ent), encoding="utf-8")

append(
    "budgets.csv",
    "bud_infrabel_fte_ye_2024,infrabel,2024,9402,,,outturn,src_infrabel_ar2024_en_fte,strong,"
    "Infrabel staff YE 31/12/2024 9402.1 FTE (9536 YE2023) AR2024 key figures\n"
    "bud_infrabel_fte_ye_2023,infrabel,2023,9536,,,outturn,src_infrabel_ar2024_en_fte,strong,"
    "Infrabel staff YE 31/12/2023 9536 FTE AR2024\n"
    "bud_infrabel_fte_avg_2024,infrabel,2024,8966,,,outturn,src_infrabel_ar2024_en_fte,strong,"
    "Infrabel average FTE for salary calc 8966.13 2024 (series 9399.84/8947.67/8736.07/8864.56/8966.13 2020-24)\n"
    "bud_infrabel_payroll_services_2024,infrabel,2024,809610000,,,outturn,src_infrabel_ar2024_en_fte,strong,"
    "Payroll costs under Services and other goods 809.61m 2024 (HR Rail recharge path)\n"
    "bud_infrabel_payroll_services_2023,infrabel,2023,775760000,,,outturn,src_infrabel_ar2024_en_fte,strong,"
    "Payroll costs under Services 775.76m 2023 AR2024 income statement\n"
    "bud_hr_rail_omzet_2025_refresh,hr_rail,2025,2368227721,,,outturn,src_hr_rail_companyweb_nbb_2025_refresh,strong-medium,"
    "HR Rail omzet 2368227721 EUR 2025 NBB-derived Companyweb confirmed tick316\n"
    "bud_hr_rail_fte_2025_refresh,hr_rail,2025,27811,,,outturn,src_hr_rail_companyweb_nbb_2025_refresh,strong-medium,"
    "HR Rail FTE 27811 2025 confirmed\n"
    "bud_hr_rail_profit_2025_refresh,hr_rail,2025,1568042,,,outturn,src_hr_rail_companyweb_nbb_2025_refresh,strong-medium,"
    "HR Rail net 1568042 EUR 2025 (pass-through near-zero)\n"
    "bud_hr_rail_nmbs_fte_residual_2024,hr_rail,2024,18166,,,estimate,src_infrabel_ar2024_en_fte,medium,"
    "Implied residual FTE class 27568.5 HR - 9402 Infrabel YE ~18166 NMBS+HR-core class 2024; not official split\n"
    "bud_hr_rail_infrabel_share_omzet_2024,hr_rail,2024,809610000,,,estimate,src_infrabel_ar2024_en_fte,medium,"
    "Infrabel payroll-in-services 809.61m as proxy HR re-invoice share 2024; residual HR omzet 2305m-810m~1495m NMBS class",
)

cash_hr = (
    '"{""2022_omzet"":2077763226,""2023_omzet"":2205907450,'
    '""2024_omzet"":2304846457,""2025_omzet"":2368227721,'
    '""2024_fte_hr"":27568.5,""2025_fte_hr"":27811,'
    '""2024_fte_infrabel_ye"":9402.1,""2024_fte_nmbs_residual_class"":18166,'
    '""2024_infrabel_payroll_services"":809610000,'
    '""2024_nmbs_omzet_share_class"":1495000000}"'
)

append(
    "commitments.csv",
    "cmt_hr_rail_dual_fte_charge_2024,HR Rail dual FTE and charge split Infrabel vs NMBS residual 2024,"
    "hr_rail,NMBS Infrabel staff via HR Rail,"
    "KB 11 Dec 2013 + Infrabel AR2024 + NBB HR filings,"
    f"2013-11-04,2024,2025,2368227721,{cash_hr},,active,,"
    "Legal employer pass-through payroll dual rail structure,"
    "Publish official charge matrix NMBS vs Infrabel EUR and FTE; free NBB PDF,"
    "src_infrabel_ar2024_en_fte,medium-strong,Federal>Mobiliteit>HR_Rail>dual_charge,"
    "tick316: Infrabel YE 9402 FTE + payroll services 809.6m strong; residual ~18.2k FTE / ~1.50bn omzet class medium; FOI L5 remains",
)

append(
    "leaderboard.csv",
    "lb_hr_rail_infrabel_fte_9402,Infrabel staff via HR Rail ~9402 FTE YE2024,federal,ops,"
    "Federal>Mobiliteit>Infrabel>FTE_HR,9402,9536,"
    "Strong AR2024: 9402.1 FTE YE2024 (9536 YE2023); avg salary FTE 8966; dual HR total 27568,"
    "strong,src_infrabel_ar2024_en_fte,Rail network staff taxpayers,"
    "Infrastructure manager workforce via dual HR employer,"
    "Core ops not pure waste; dual structure opacity on charge vs NMBS,"
    "3,7.0,4,5.2,Publish joint FTE matrix with NMBS; simplify dual HR,seed,,tick316 dual\n"
    "lb_hr_rail_infrabel_payroll_810m,Infrabel HR payroll charge in services 809.6m 2024,federal,ops,"
    "Federal>Mobiliteit>Infrabel>HR_payroll_charge,809610000,809610000,"
    "Strong AR2024 income statement: Payroll costs under Services 809.61m 2024 / 775.76m 2023; proxy re-invoice from HR Rail,"
    "strong,src_infrabel_ar2024_en_fte,Rail users taxpayers,"
    "Staff cost path through dual employer,"
    "Core payroll; dual accounting (services vs own personnel line); residual NMBS share FOI,"
    "4,8.0,4,6.0,Open full charge matrix both companies,seed,,tick316\n"
    "lb_hr_rail_nmbs_residual_fte_18k,NMBS residual FTE class ~18.2k via HR Rail 2024,federal,ops,"
    "Federal>Mobiliteit>NMBS>FTE_HR_residual,18166,18166,"
    "Medium residual: HR 27568.5 - Infrabel YE 9402 ~18166; not official NMBS publication; omzet share class ~1.50bn,"
    "medium,src_infrabel_ar2024_en_fte,Passengers taxpayers,"
    "Implied NMBS workforce share under dual employer,"
    "Dual opacity; FOI official split still needed,"
    "5,7.5,5,6.0,NMBS publish FTE and charge EUR series,seed,,tick316 residual class",
)

# update FOI gap notes for partial fill
foi = (base / "foi_queue.csv").read_text(encoding="utf-8")
old_gap = (
    "gap_hr_rail_charge_matrix,Federal>Mobiliteit>HR_Rail>charge_matrix,hr_rail,"
    "Free official NBB CBSO full jaarrekening PDF 2023-2025; annual staff charge re-invoice L5 split "
    "NMBS vs Infrabel vs other; FTE by entity and statute; admin overhead of HR Rail entity itself,"
    "Institutional omzet/FTE now medium via aggregator; dual structure charge L5 and free primary PDF still needed,"
    "5,HR Rail / FOD Mobiliteit / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_hr_rail_charge_matrix.md,ready,2026-07-28,,,,,"
    "cmt_hr_rail_payroll_pass_through,lb_hr_rail_payroll_2_4bn,"
    "2026-07-28T05:25:00Z,2026-07-28T05:25:00Z,tick166 draft ready human send"
)
new_gap = (
    "gap_hr_rail_charge_matrix,Federal>Mobiliteit>HR_Rail>charge_matrix,hr_rail,"
    "Free official NBB CBSO full jaarrekening PDF 2023-2025; annual staff charge re-invoice official L5 split "
    "NMBS vs Infrabel vs other (Infrabel payroll-in-services 809.6m 2024 and YE FTE 9402 now public proxy); "
    "FTE by entity and statute; admin overhead of HR Rail entity itself,"
    "Omzet/FTE multi-year strong-medium; Infrabel side partial strong; official NMBS charge and free NBB PDF residual,"
    "5,HR Rail / FOD Mobiliteit / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_hr_rail_charge_matrix.md,ready,2026-07-28,,,,,"
    "cmt_hr_rail_payroll_pass_through|cmt_hr_rail_dual_fte_charge_2024,lb_hr_rail_payroll_2_4bn|lb_hr_rail_infrabel_payroll_810m,"
    "2026-07-28T05:25:00Z,2026-07-30T20:45:00Z,"
    "tick166 draft | tick316: Infrabel FTE 9402 + payroll 809.6m partial; residual official NMBS matrix + free NBB PDF human send"
)
if old_gap not in foi:
    raise SystemExit("gap_hr_rail_charge_matrix not found")
(base / "foi_queue.csv").write_text(foi.replace(old_gap, new_gap), encoding="utf-8")

# research_queue
rq_path = base / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_307,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; HR Rail deepen dual; other FOI-adjacent). "
    "Prefer before idle.,,2026-07-30T20:15:00Z,,Spawned tick315 after Cipal; rq_116 SWA deferred"
)
new = (
    "rq_307,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; HR Rail deepen dual; other FOI-adjacent). "
    "Prefer before idle.,gap_hr_rail_charge_matrix,"
    "2026-07-30T20:15:00Z,2026-07-30T20:45:00Z,"
    "tick316: Infrabel FTE 9402 + payroll services 809.6m dual HR residual ~18k FTE; FOI L5 remains; spawn rq_308\n"
    "rq_308,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; NMBS FTE dual HR Rail; other FOI-adjacent). "
    "Prefer before idle.,,2026-07-30T20:45:00Z,,Spawned tick316 after HR Rail dual; rq_116 SWA deferred"
)
if old not in text:
    raise SystemExit("rq_307 not found")
rq_path.write_text(text.replace(old, new), encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T20:45:00Z,rq_307,316,no,"
    "Scheduler 60s. Next prio5 rq_308; rq_116 SWA deferred. FOI ready. "
    "tick316 HR Rail dual Infrabel 9402 FTE + 809.6m payroll.\n",
    encoding="utf-8",
)

print("tick316 CSV writes OK")

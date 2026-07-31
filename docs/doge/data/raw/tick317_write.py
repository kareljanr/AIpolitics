# tick 317 — NMBS FTE dual HR Rail recon (closes Infrabel side from tick316)
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
    "src_nmbs_companyweb_fte_zero,NMBS NV PR Companyweb shows 0 FTE statutory (employment via HR Rail),"
    "https://www.companyweb.be/nl/0203430576/nmbs; https://consult.cbso.nbb.be/consult-enterprise/0203430576,"
    "Companyweb (NBB CBSO),2026-07-30,nbb,"
    '"Strong dual evidence: statutory NMBS reports 0 FTE; omzet 2.560/2.615bn 2024-25; '
    'all staff legal employment via HR Rail KB 2013"\n'
    "src_nmbs_results_staff_2026_01,NMBS Resultaten 2025 page staff headcount 16976 on 2026-01-01,"
    "https://www.belgiantrain.be/nl/about-sncb/corporate/2026/financial-results-2025,"
    "NMBS/SNCB,2026-07-30,official_press,"
    '"Strong: more than 1100 hires 2025; 16976 medewerkers on 1 Jan 2026; dual with HR Rail FTE 27811"',
)

# entity nmbs note if exists
ents = (base / "entities.csv").read_text(encoding="utf-8")
# find nmbs line
import re
m = re.search(r"^nmbs,.*$", ents, re.M)
if m:
    old_line = m.group(0)
    if "tick317" not in old_line:
        # append note fragment carefully - replace trailing notes field
        parts = old_line.rstrip("\n").split(",")
        # last field is notes - append
        if len(parts) >= 12:
            parts[-1] = parts[-1] + "; statutory 0 FTE dual HR; ops headcount 16976 2026-01-01; tick317"
            new_line = ",".join(parts)
            ents = ents.replace(old_line, new_line)
            (base / "entities.csv").write_text(ents, encoding="utf-8")

append(
    "budgets.csv",
    "bud_nmbs_statutory_fte_2025,nmbs,2025,0,,,outturn,src_nmbs_companyweb_fte_zero,strong,"
    "NMBS statutory jaarrekening FTE 0 (legal employer is HR Rail) Companyweb/NBB\n"
    "bud_nmbs_ops_headcount_2026_01,nmbs,2026,16976,,,outturn,src_nmbs_results_staff_2026_01,strong,"
    "NMBS operational headcount 16976 medewerkers 2026-01-01 official results (after 1100+ hires 2025)\n"
    "bud_rail_dual_fte_sum_class_2024,gg_belgium,2024,26378,,,estimate,src_nmbs_results_staff_2026_01,medium,"
    "Sum NMBS ops headcount 16976 (2026-01) + Infrabel YE FTE 9402 (2024) = 26378 vs HR FTE 27568 2024 residual ~1.2k class\n"
    "bud_rail_dual_fte_sum_class_2025,gg_belgium,2025,26378,,,estimate,src_nmbs_results_staff_2026_01,medium,"
    "Same sum 26378 vs HR FTE 27811 2025 residual ~1.4k (HR Rail own admin + FTE vs headcount + date mix)\n"
    "bud_nmbs_hr_payroll_share_class_2024,nmbs,2024,1495236457,,,estimate,src_infrabel_ar2024_en_fte,medium,"
    "HR omzet 2304.8m - Infrabel payroll-services 809.6m = residual 1495.2m class NMBS HR re-invoice 2024\n"
    "bud_nmbs_unit_cost_fte_class_2024,nmbs,2024,88100,,,estimate,src_nmbs_results_staff_2026_01,medium,"
    "Implied ~1.495bn / ~17k ~EUR 88k per head class 2024; Infrabel ~810m/9.4k ~86k; method-sensitive",
)

cash_dual = (
    '"{""hr_fte_2024"":27568.5,""hr_fte_2025"":27811,'
    '""infrabel_fte_ye_2024"":9402.1,""nmbs_headcount_2026_01"":16976,'
    '""sum_nmbs_infrabel"":26378,""hr_residual_class_2025"":1433,'
    '""nmbs_statutory_fte"":0,""infrabel_payroll_2024"":809610000,'
    '""nmbs_payroll_share_class_2024"":1495236457,'
    '""hr_omzet_2024"":2304846457,""hr_omzet_2025"":2368227721}"'
)

append(
    "commitments.csv",
    "cmt_rail_dual_fte_recon_2024_26,Rail dual employer FTE recon NMBS+Infrabel vs HR Rail,"
    "hr_rail,NMBS Infrabel passengers taxpayers,"
    "KB 11 Dec 2013 dual structure + AR2024 + NMBS results 2025 + NBB statutory,"
    f"2013-11-04,2024,2026,2368227721,{cash_dual},,active,,"
    "Map legal employer HR Rail to operational entities NMBS and Infrabel,"
    "Publish joint official FTE+EUR charge matrix; free NBB PDF; simplify dual HR,"
    "src_nmbs_results_staff_2026_01,medium-strong,Federal>Mobiliteit>rail>dual_HR_FTE,"
    "tick317: NMBS ops 16976 + statutory 0 FTE strong; Infrabel 9402 strong; HR 27811; residual ~1.4k medium; EUR charge NMBS FOI",
)

append(
    "leaderboard.csv",
    "lb_nmbs_ops_headcount_17k,NMBS operational headcount 16976 on 2026-01-01,federal,ops,"
    "Federal>Mobiliteit>NMBS>headcount,16976,16976,"
    "Strong official results: 16976 medewerkers 1 Jan 2026 after 1100+ hires 2025; dual HR Rail 27811 total,"
    "strong,src_nmbs_results_staff_2026_01,Passengers taxpayers,"
    "National passenger rail workforce,"
    "Core ops; statutory filing shows 0 FTE (legal employer HR Rail) dual opacity,"
    "4,7.5,3,5.7,Publish multi-year FTE series and HR charge EUR,seed,,tick317 dual HR\n"
    "lb_nmbs_statutory_fte_zero,NMBS statutory jaarrekening FTE 0 dual HR Rail,federal,ops,"
    "Federal>Mobiliteit>NMBS>statutory_FTE_zero,0,0,"
    "Strong NBB-derived: NMBS reports 0 FTE while ops 17k and omzet 2.6bn; all staff legally at HR Rail,"
    "strong,src_nmbs_companyweb_fte_zero,Taxpayers transparency,"
    "Dual employer accounting structure,"
    "Not pure waste but major dual-structure opacity; workforce invisible on operator statutory accounts,"
    "7,6.0,4,6.0,Require joint disclosure FTE+charge on NMBS and Infrabel accounts,seed,,tick317 dual absurdity\n"
    "lb_rail_dual_fte_recon_27k,Rail dual FTE recon HR 27.8k = NMBS 17k + Infrabel 9.4k + residual,federal,ops,"
    "Federal>Mobiliteit>rail>dual_FTE_map,26378,27811,"
    "Medium-strong: sum ops counts 26378 vs HR 27811 residual ~1.4k class (HR admin + method); EUR NMBS share ~1.50bn class 2024,"
    "medium-strong,src_nmbs_results_staff_2026_01,Rail users taxpayers,"
    "Full dual employer workforce map,"
    "Core structure; residual FOI for official NMBS charge EUR and same-date FTE,"
    "5,8.5,4,6.5,Joint NMBS-Infrabel-HR annual FTE+EUR table,seed,,tick317 closes dual map class",
)

# update gap_hr_rail notes
foi = (base / "foi_queue.csv").read_text(encoding="utf-8")
old_gap = (
    "tick166 draft | tick316: Infrabel FTE 9402 + payroll 809.6m partial; residual official NMBS matrix + free NBB PDF human send"
)
new_gap = (
    "tick166|316|317: NMBS ops 16976 + statutory FTE 0 strong; Infrabel 9402+809.6m strong; residual official NMBS payroll EUR charge series + free NBB PDF + same-date FTE human send"
)
if old_gap not in foi:
    raise SystemExit("gap note fragment not found")
(base / "foi_queue.csv").write_text(foi.replace(old_gap, new_gap), encoding="utf-8")

# also tighten what_is_missing on gap if we can find the row start
# research_queue
rq_path = base / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_308,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; NMBS FTE dual HR Rail; other FOI-adjacent). "
    "Prefer before idle.,,2026-07-30T20:45:00Z,,Spawned tick316 after HR Rail dual; rq_116 SWA deferred"
)
new = (
    "rq_308,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; NMBS FTE dual HR Rail; other FOI-adjacent). "
    "Prefer before idle.,gap_hr_rail_charge_matrix,"
    "2026-07-30T20:45:00Z,2026-07-30T21:15:00Z,"
    "tick317: NMBS ops 16976 + statutory FTE 0 dual HR 27811; residual ~1.4k; FOI NMBS EUR charge; spawn rq_309\n"
    "rq_309,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; other FOI-adjacent dual/L5). Prefer before idle. "
    "Note progress@320 soon.,,2026-07-30T21:15:00Z,,Spawned tick317 after NMBS dual FTE; rq_116 SWA deferred"
)
if old not in text:
    raise SystemExit("rq_308 not found")
rq_path.write_text(text.replace(old, new), encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T21:15:00Z,rq_308,317,no,"
    "Scheduler 60s. Next prio5 rq_309; progress@320 in 3 ticks; rq_116 SWA deferred. "
    "tick317 NMBS 16976 dual HR FTE 0 statutory.\n",
    encoding="utf-8",
)

print("tick317 CSV writes OK")

# tick 307 — rq_298 FIRM + CTRG deepen + Kamer 56K0983 approved 2026 full table
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T16:15:00Z"
unit = "rq_298"

src_line = (
    "src_kamer_56k0983_approved_2026,"
    "Kamer 56K0983/001 approved vs requested 2026 full 9-institution table + FIRM CTRG narrative,"
    "docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf; "
    "https://www.dekamer.be/FLWB/PDF/56/0983/56K0983001.pdf,"
    "Belgische Kamer van volksvertegenwoordigers commissie Comptabiliteit,"
    "2026-07-30,official_budget,"
    "Approved 2026: total kred 149.280m / dotatie 133.134m (req 153.967/137.771); "
    "FIRM 5.084/3.223; CTRG 6.694/6.075; GBA 15.885/12.754; tick307\n"
)
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_line)

# entities
ent_path = ROOT / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
# update firm_ifdh notes
lines = []
for L in ent_text.splitlines(True):
    if L.startswith("firm_ifdh,") and "tick307" not in L:
        L = (
            "firm_ifdh,Federaal Instituut voor de rechten van de mens (FIRM),"
            "Institut federal des droits humains (IFDH),Federal Institute for Human Rights,"
            "agency,sec_federal,bi,https://institutfederaldroitshumains.be,,Brussels,"
            "Kamer-dotatie NHRI; 2026 approved kred 5.084m dot 3.223m; 2024 kred 4.349m surplus 1.860m; "
            "staff 24->27 ETP; dual Unia VMRI IEFH MNP; tick307\n"
        )
    lines.append(L)
ent_text = "".join(lines)
if "ctr_gevangeniswezen" not in ent_text:
    ent_text = ent_text.rstrip("\n") + "\n"
    ent_text += (
        "ctr_gevangeniswezen,Centrale Toezichtsraad Gevangeniswezen CTRG,"
        "Conseil central de surveillance penitentiaire CCSP,"
        "Central Prison Monitoring Council,agency,sec_federal,bi,"
        "https://ccsp.be,,,,"
        "Kamer-dotatie prison oversight; 2026 approved kred 6.694m (req 8.340m cut); "
        "surplus 2024 0.671m; dual FIRM MNP; tick307\n"
    )
ent_path.write_text(ent_text, encoding="utf-8")

# budgets — FIRM deepen + CTRG + full approved table rows
bud_rows = [
    # FIRM
    "bud_firm_kred_2024,firm_ifdh,2024,4348733,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Kamer: 2024 uitgavenbegroting 4.348.73278; financed dotatie 4.111m + boni 2022 0.238m",
    "bud_firm_dotatie_2024,firm_ifdh,2024,4111000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Dotatie 2024 4.111m",
    "bud_firm_surplus_2024,firm_ifdh,2024,1859949,,,outturn,src_kamer_56k0983_approved_2026,strong,"
    "Comptes 2024 surplus 1.859949m (vs 1.3214m 2023)",
    "bud_firm_kred_2025,firm_ifdh,2025,4983893,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "2025 kredieten 4.983893m (Kamer narrative)",
    "bud_firm_kred_req_2026,firm_ifdh,2026,5628682,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Requested 2026 kred 5.628682m (+12.9pct vs 2025)",
    "bud_firm_kred_approved_2026,firm_ifdh,2026,5083571,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Commission approved kred 5.083571m 2026",
    "bud_firm_dotatie_req_2026,firm_ifdh,2026,3769000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Requested dotatie 3.769m (frozen at 2025 via boni narrative)",
    "bud_firm_dotatie_approved_2026,firm_ifdh,2026,3223000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Commission approved dotatie 3.223m 2026",
    "bud_firm_staff_2025,firm_ifdh,2025,24,,,outturn,src_kamer_56k0983_approved_2026,strong,"
    "Current cadre 24 ETP; target 27 eoy2025; original Justice path 22; not EUR",
    # CTRG
    "bud_ctrg_surplus_2024,ctr_gevangeniswezen,2024,670678,,,outturn,src_kamer_56k0983_approved_2026,strong,"
    "Comptes 2024 surplus 670678; boni extinguishing path since 2022 exp>dotatie",
    "bud_ctrg_adjust_2025,ctr_gevangeniswezen,2025,172570,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Budget adjustment 2025 +172570 (jetons 70120 + maternity cover 55000 class)",
    "bud_ctrg_kred_req_2026,ctr_gevangeniswezen,2026,8340000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Requested kred 8.340m 2026 (+27pct narrative)",
    "bud_ctrg_dotatie_req_2026,ctr_gevangeniswezen,2026,7670000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Requested dotatie 7.670m 2026 (+34pct narrative)",
    "bud_ctrg_kred_approved_2026,ctr_gevangeniswezen,2026,6694495,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Commission approved kred 6.694495m (cut vs request)",
    "bud_ctrg_dotatie_approved_2026,ctr_gevangeniswezen,2026,6075000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Commission approved dotatie 6.075m 2026",
    # GBA Kamer 2026 refresh
    "bud_gba_kred_req_2026,gba_apd,2026,16828000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Requested kred 16.828m 2026 (incl +10 ETP request narrative)",
    "bud_gba_kred_approved_2026,gba_apd,2026,15885072,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Commission approved kred 15.885072m 2026",
    "bud_gba_dotatie_req_2026,gba_apd,2026,13697000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Requested dotatie 13.697m 2026",
    "bud_gba_dotatie_approved_2026,gba_apd,2026,12754000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Commission approved dotatie 12.754m 2026",
    # Full pack totals
    "bud_kamer_dotatie_pack_req_2026,gg_belgium,2026,153966800,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Sum requested kredieten 9 institutions 153.9668m 2026",
    "bud_kamer_dotatie_pack_approved_2026,gg_belgium,2026,149280371,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Sum commission-approved kredieten 9 institutions 149.280371m 2026",
    "bud_kamer_dotatie_sum_req_2026,gg_belgium,2026,137770500,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Sum requested dotaties 9 institutions 137.7705m 2026",
    "bud_kamer_dotatie_sum_approved_2026,gg_belgium,2026,133134000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Sum commission-approved dotaties 9 institutions 133.134m 2026 (+0.78pct Moesen narrative excl ComiteP billing error)",
    # refresh approved for peers from tick306
    "bud_rekenhof_kred_approved_2026,rekenhof,2026,70999700,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved=requested 70.9997m",
    "bud_rekenhof_dotatie_approved_2026,rekenhof,2026,65552500,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved=requested 65.5525m",
    "bud_gwh_kred_approved_2026,grondwettelijk_hof,2026,14520720,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved kred 14.52072m (req 14.593m)",
    "bud_gwh_dotatie_approved_2026,grondwettelijk_hof,2026,13760000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved dotatie 13.760m (req 13.830m)",
    "bud_hrj_kred_approved_2026,hrj_csj,2026,7369500,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved kred 7.3695m",
    "bud_hrj_dotatie_approved_2026,hrj_csj,2026,6873500,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved dotatie 6.8735m",
    "bud_comite_p_kred_approved_2026,comite_p,2026,14272213,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved kred 14.272213m (req 14.961m)",
    "bud_comite_p_dotatie_approved_2026,comite_p,2026,14025000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved dotatie 14.025m",
    "bud_comite_i_kred_approved_2026,comite_i,2026,6187100,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved kred 6.1871m after -750k digitisation tranche holdback",
    "bud_comite_i_dotatie_approved_2026,comite_i,2026,4118000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved dotatie 4.118m after -750k digitisation holdback",
    "bud_fed_ombuds_kred_approved_2026,fed_ombudsman,2026,8268000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved=requested 8.268m",
    "bud_fed_ombuds_dotatie_approved_2026,fed_ombudsman,2026,6753000,,,budgeted,src_kamer_56k0983_approved_2026,strong,"
    "Approved=requested 6.753m",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

cmt_rows = [
    (
        "cmt_firm_kamer_2024_26,FIRM IFDH Kamer-dotatie path deepen 2024-26,firm_ifdh,"
        "NHRI MNP partners Myria Unia,Wet 12 mei 2019 FIRM + Kamer Comptabiliteit,"
        "2019-05-12,2024,2026,14418797,"
        '"{""kred_2024"":4348733,""dotatie_2024"":4111000,""surplus_2024"":1859949,'
        '""kred_2025"":4983893,""kred_req_2026"":5628682,""kred_approved_2026"":5083571,'
        '""dotatie_req_2026"":3769000,""dotatie_approved_2026"":3223000,'
        '""staff_etp"":24,""staff_target_eoy2025"":27,""mnp_protocol"":""22Apr2025"","'
        '""note"":""Large surplus funds freeze path; dual Unia VMRI IEFH Myria MNP stack""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "Federal NHRI residual Paris Principles + MNP coordination,"
        "Track surplus burn; dual equality stack; FOI L5 still gap_firm_funding_detail,"
        "src_kamer_56k0983_approved_2026,strong,BE>FIRM_IFDH>dotatie,tick307 deepen"
    ),
    (
        "cmt_ctrg_package_2024_26,CTRG CCSP prison oversight Kamer-dotatie,ctr_gevangeniswezen,"
        "Detainees prison system parliament,Prison monitoring council organic law,"
        "2019-01-01,2024,2026,6694495,"
        '"{""surplus_2024"":670678,""adjust_2025"":172570,'
        '""kred_req_2026"":8340000,""dotatie_req_2026"":7670000,'
        '""kred_approved_2026"":6694495,""dotatie_approved_2026"":6075000,'
        '""req_growth_kred_pct"":27,""req_growth_dot_pct"":34,'
        '""etp_request_extra"":11,""note"":""Commission cut hard vs +27/+34pct request; boni extinguishing""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "External prison oversight and complaint right,"
        "Right-size growth vs prison expansion path; dual FIRM MNP,"
        "src_kamer_56k0983_approved_2026,strong,Federal>Parlement>CTRG,tick307"
    ),
    (
        "cmt_kamer_dotatie_9inst_approved_2026,Kamer-dotatie 9 institutions commission-approved 2026 pack,"
        "gg_belgium,All Kamer-dotatie democratic control institutions,"
        "Kamer Comptabiliteit DOC 56 0983/001 deliberation,2025-07-15,2026,2026,149280371,"
        '"{""kred_req_sum"":153966800,""kred_approved_sum"":149280371,'
        '""dotatie_req_sum"":137770500,""dotatie_approved_sum"":133134000,'
        '""rekenhof_kred"":70999700,""gba_kred"":15885072,""comite_p_kred"":14272213,'
        '""gwh_kred"":14520720,""fed_ombuds_kred"":8268000,""hrj_kred"":7369500,'
        '""ctrg_kred"":6694495,""comite_i_kred"":6187100,""firm_kred"":5083571,'
        '""moesen_dot_growth_pct"":0.78,""kred_growth_pct"":0.34,'
        '""note"":""Moesen almost met excl ComiteP late billing 0.815m; full pack replaces 5-peer ~115m""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "Consolidated parliamentary-dotation democratic control spend,"
        "Publish permanent open table; dual avoid double-count entity rows,"
        "src_kamer_56k0983_approved_2026,strong,Federal>Parlement>dotatie_9pack,tick307"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

lb_rows = [
    (
        "lb_kamer_dotatie_9pack_149m,Kamer-dotatie 9 institutions approved kred ~149.3m 2026,federal,ops,"
        "Federal>Parlement>dotatie_9pack,149280371,149280371,"
        "Strong Kamer table: approved kred 149.28m / dotatie 133.13m; req 154.0/137.8m; Moesen +0.78pct dots,"
        "strong,src_kamer_56k0983_approved_2026,Taxpayers democracy,Democratic control infrastructure pack,"
        "Material consolidated pack; dual individual entities not additive double-count,"
        "3,8.0,2,5.1,Publish permanent open data table all years,"
        "seed,,tick307 supersedes 5-peer ~115m"
    ),
    (
        "lb_firm_approved_5_1m,FIRM IFDH approved kred ~5.08m 2026,federal,ops,"
        "Federal>Parlement>FIRM,5083571,5083571,"
        "Strong Kamer: approved 5.084m kred / 3.223m dot; surplus 1.86m 2024; staff 24 ETP; dual Unia,"
        "strong,src_kamer_56k0983_approved_2026,Rights holders,Federal NHRI residual mandate,"
        "Surplus-funded freeze; dual equality/HR stack,"
        "3,4.0,2,3.3,Track surplus burn dual Unia IEFH,"
        "seed,,tick307"
    ),
    (
        "lb_ctrg_approved_6_7m,CTRG prison oversight approved ~6.69m 2026,federal,ops,"
        "Federal>Parlement>CTRG,6694495,6694495,"
        "Strong Kamer: approved 6.694m (req 8.340m cut); surplus 0.671m 2024; dual FIRM MNP,"
        "strong,src_kamer_56k0983_approved_2026,Detainees,External prison monitoring,"
        "Commission cut vs +27pct request; growth vs prison expansion tension,"
        "4,4.5,3,4.0,Right-size ETP; dual MNP FIRM Myria,"
        "seed,,tick307"
    ),
    (
        "lb_gba_approved_15_9m,GBA APD approved kred ~15.89m 2026,federal,ops,"
        "Federal>Parlement>GBA,15885072,15885072,"
        "Strong Kamer: approved 15.885m kred / 12.754m dot (req 16.828/13.697); dual AR werkings ~15.3m 2025,"
        "strong,src_kamer_56k0983_approved_2026,Data subjects,GDPR supervision,"
        "Commission trim vs +10 ETP request; dual AR 2025 15.3m,"
        "2,5.5,2,3.6,Keep core; dual AR financing mix,"
        "seed,,tick307 refresh tick304"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

# update FOI gap notes
foi_path = ROOT / "foi_queue.csv"
foi = foi_path.read_text(encoding="utf-8")
old_note = "tick306 draft ready human send"
new_note = (
    "tick306 draft ready human send | tick307: full 9-inst approved table filled "
    "149.28m kred / 133.13m dots; residual machine-readable multi-year still human send"
)
if old_note in foi:
    foi = foi.replace(old_note, new_note)
    foi_path.write_text(foi, encoding="utf-8")

# research_queue
rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_298,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Kamer 56K0983 residual FIRM CTRG deepen if numbers; Raad van State; AGMJ if extractable). Prefer before idle.,,"
    "2026-07-30T15:45:00Z,,Spawned tick306 after Kamer dotatie pack; rq_116 SWA deferred"
)
new = (
    "rq_298,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Kamer 56K0983 residual FIRM CTRG deepen if numbers; Raad van State; AGMJ if extractable). Prefer before idle.,"
    "gap_kamer_dotatie_pack_l5,2026-07-30T15:45:00Z,2026-07-30T16:15:00Z,"
    "tick307: FIRM 5.08m + CTRG 6.69m approved; full 9-inst pack kred 149.3m / dots 133.1m; spawn rq_299"
)
if old not in text:
    raise SystemExit("rq_298 not found")
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_299,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Raad van State budget; AGMJ if extractable; other FOI-adjacent). Prefer before idle. Note progress@310 soon.,,"
    "2026-07-30T16:15:00Z,,Spawned tick307 after FIRM/CTRG + full Kamer table; rq_116 SWA deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},307,no,"
    "Scheduler 60s. Next prio5 rq_299; progress@310 in 3 ticks; rq_116 SWA deferred. "
    "tick307 Kamer 9-inst pack approved kred 149.3m.\n",
    encoding="utf-8",
)
print("OK")

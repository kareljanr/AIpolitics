# tick 277 — CoA 182e OISZ accounts + SS consolidated dual eHealth
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T01:15:00Z"

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_ss_182e_2025,Rekenhof 182e Boek deel II Boek 2025 Sociale Zekerheid OISZ rekeningen,"
        "docs/doge/data/raw/ccrek_ss_182e_b_II.pdf,Rekenhof / Cour des comptes,2026-07-30,court_audit,"
        "SS consol 139.3/139.8bn 2024 beheers 2.8bn; eHealth beheer 15.9m 2023; FEDRIS beheer 54.2m; "
        "HZIV beheer 38.8m total 634.3m; RVA beheer 277.9m; RJV 6.38bn 2024; FSO 838.7m 2024; tick277\n"
    )

# entities
ents = [
    "fedris,Federaal agentschap voor beroepsrisicos Fedris,Agence federale des risques professionnels,"
    "Federal Agency for Occupational Risks,parastatal,sec_ss,bi,https://www.fedris.be,,,"
    "Work accidents occupational diseases; beheer 54.2m 2023; FPS exp 596.4m 2024; tick277",
    "hziv,Hulpkas voor Ziekte- en Invaliditeitsverzekering HZIV,Caisse auxiliaire d assurance maladie-invalidite,"
    "Auxiliary Fund for Sickness and Disability Insurance,parastatal,sec_ss,bi,https://www.caami-hziv.fgov.be,,,"
    "Public mutual VI; total costs 634.3m 2023 beheer 38.8m; dual landsbond admin; tick277",
    "rva,Rijksdienst voor Arbeidsvoorziening RVA,Office national de l emploi ONEM,"
    "National Employment Office,parastatal,sec_ss,bi,https://www.rva.be,,,"
    "Unemployment admin; beheer 277.9m 2023; opdrachten 6.745bn; tick277",
    "rjv,Rijksdienst voor Jaarlijkse Vakantie RJV,Office national des vacances annuelles ONVA,"
    "National Office for Annual Vacation,parastatal,sec_ss,bi,https://www.onva-rjv.fgov.be,,,"
    "Worker holiday pay; exp 6.381bn 2024; beheer 23.6m 2023; tick277",
    "fso,Fonds Sluiting Ondernemingen FSO,Fonds de fermeture des entreprises,"
    "Company Closure Fund,parastatal,sec_ss,bi,https://www.fonds-sluiting.be,,,"
    "Closure compensations; exp 838.7m 2024; beheer 7.7m 2023; tick277",
    "rsvz,Rijksinstituut voor de Sociale Verzekeringen der Zelfstandigen RSVZ,"
    "Institut national d assurances sociales pour travailleurs independants INASTI,"
    "National Institute for Social Insurance of Self-employed,parastatal,sec_ss,bi,https://www.rsvz.be,,,"
    "Self-employed SS; beheer 106.9m 2023; tick277",
    "hvw,Hulpkas voor Werkloosheidsuitkeringen HVW,Caisse auxiliaire de paiement des allocations de chomage,"
    "Auxiliary Fund for Unemployment Benefits,parastatal,sec_ss,bi,https://www.capac-hvw.fgov.be,,,"
    "Public unemployment payment channel; beheer 47.9m 2023; prestaties 735.7m; tick277",
]
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    for e in ents:
        f.write(e + "\n")
    # update ehealth note via append if no duplicate - check
# ehealth already exists - skip re-add

bud = [
    # SS consolidated
    "bud_ss_consol_uitgaven_2024,sec_ss,2024,139300000000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: geconsolideerde SS uitgaven 139.3bn 2024",
    "bud_ss_consol_ontvangsten_2024,sec_ss,2024,139800000000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: geconsolideerde SS ontvangsten 139.8bn 2024",
    "bud_ss_beheerskosten_2024,sec_ss,2024,2800000000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA graphic: Beheerskosten 2.8bn of SS 2024",
    "bud_ss_bijdragen_2024,sec_ss,2024,80400000000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: sociale bijdragen 80.4bn (~57.5pct of receipts)",
    "bud_ss_prestaties_pensioenen_2024,sec_ss,2024,66800000000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA graphic prestaties pensioenen 66.8bn class",
    "bud_ss_prestaties_geneesk_2024,sec_ss,2024,37000000000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA graphic geneeskundige verzorging 37.0bn class",
    # eHealth institutional dual
    "bud_ehealth_beheer_2022,ehealth_platform,2022,15300000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA tabel34: beheer uitgaven 15.3m 2022",
    "bud_ehealth_beheer_2023,ehealth_platform,2023,15900000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer 15.9m 2023; dual INAMI stack 132.5m 2025 different perimeter",
    "bud_ehealth_opbrengsten_2023,ehealth_platform,2023,17400000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA alg boekh opbrengsten 17.4m 2023",
    # FEDRIS
    "bud_fedris_beheer_2022,fedris,2022,50100000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer uitgaven 50.1m 2022",
    "bud_fedris_beheer_2023,fedris,2023,54200000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer 54.2m 2023",
    "bud_fedris_opdrachten_2023,fedris,2023,1084600000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: opdrachten uitgaven 1.0846bn 2023",
    "bud_fedris_fps_exp_2024,fedris,2024,596400000,,,outturn,src_ccrek_ss_182e_2025,strong,FPS SZ feb2025: begrotingsuitgaven total 596.4m 2024 (globaal 541.9 + buiten 54.5)",
    # HZIV
    "bud_hziv_beheer_2023,hziv,2023,38800000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer uitgaven 38.8m 2023",
    "bud_hziv_kosten_2023,hziv,2023,634300000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: total kosten 634.3m 2023 (+10.3pct vs 575.1m 2022)",
    "bud_hziv_opdrachten_2023,hziv,2023,593900000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: opdrachten uitgaven 593.9m 2023",
    # RVA HVW
    "bud_rva_beheer_2023,rva,2023,277900000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer uitgaven 277.9m 2023",
    "bud_rva_opdrachten_2023,rva,2023,6744800000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: opdrachten 6.7448bn 2023",
    "bud_hvw_beheer_2023,hvw,2023,47900000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer 47.9m 2023 (prior site 6.084m different line)",
    "bud_hvw_opdrachten_2023,hvw,2023,735700000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: sociale prestaties/opdrachten 735.7m 2023",
    # RJV FSO RSVZ
    "bud_rjv_exp_2024,rjv,2024,6381200000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA/FPS: RJV uitgaven 6.3812bn 2024",
    "bud_rjv_rec_2024,rjv,2024,6481300000,,,outturn,src_ccrek_ss_182e_2025,strong,RJV ontvangsten 6.4813bn 2024",
    "bud_rjv_beheer_2023,rjv,2023,23600000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer 23.6m 2023",
    "bud_fso_exp_2024,fso,2024,838700000,,,outturn,src_ccrek_ss_182e_2025,strong,FPS: FSO uitgaven 838.7m 2024 (+56pct)",
    "bud_fso_rec_2024,fso,2024,522900000,,,outturn,src_ccrek_ss_182e_2025,strong,FSO ontvangsten 522.9m 2024",
    "bud_fso_beheer_2023,fso,2023,7700000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer 7.7m 2023",
    "bud_rsvz_beheer_2023,rsvz,2023,106900000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA: beheer 106.9m 2023",
    "bud_ksz_beheer_2023_coa,ksz,2023,17400000,,,outturn,src_ccrek_ss_182e_2025,strong,CoA KSZ beheer 17.4m 2023; dual site 19.8m 2025 path",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

cash_ss = {
    "uitgaven_2024_bn": 139.3,
    "ontvangsten_2024_bn": 139.8,
    "beheerskosten_2024_bn": 2.8,
    "bijdragen_2024_bn": 80.4,
    "pensioenen_class_bn": 66.8,
    "geneesk_class_bn": 37.0,
    "note": "CoA 182e Boek 2025 over SS; 90.5pct prestaties",
}
cash_ehealth = {
    "beheer_2022_m": 15.3,
    "beheer_2023_m": 15.9,
    "opbrengsten_2023_m": 17.4,
    "kosten_2023_m": 15.7,
    "dual_inami_stack_2025_m": 132.548,
    "note": "Institutional eHealth ADBA/parastatal vs INAMI financing lines different perimeter not additive",
}
cash_fedris = {
    "beheer_2023_m": 54.2,
    "opdrachten_2023_m": 1084.6,
    "fps_exp_2024_m": 596.4,
    "globaal_2024_m": 541.9,
    "buiten_globaal_2024_m": 54.5,
}
cash_pack = {
    "hziv_beheer_2023_m": 38.8,
    "hziv_total_2023_m": 634.3,
    "rva_beheer_2023_m": 277.9,
    "hvw_beheer_2023_m": 47.9,
    "rjv_beheer_2023_m": 23.6,
    "rjv_exp_2024_bn": 6.381,
    "fso_beheer_2023_m": 7.7,
    "fso_exp_2024_m": 838.7,
    "rsvz_beheer_2023_m": 106.9,
    "beheer_sum_sample_m": 38.8 + 277.9 + 47.9 + 23.6 + 54.2 + 7.7 + 106.9 + 15.9 + 17.4,
    "note": "Sample OISZ beheer from CoA 2023 tables; not full SS beheers 2.8bn",
}

def cmt_row(cid, title, ent, ben, basis, env, cash, goal, cut, path, notes):
    cash_csv = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
    return (
        f"{cid},{title},{ent},{ben},{basis},2022-01-01,2022,2024,{env},"
        f"{cash_csv},0,active,docs/doge/data/raw/ccrek_ss_182e_b_II.pdf,"
        f"{goal},{cut},src_ccrek_ss_182e_2025,strong,{path},{notes}\n"
    )

with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt_row(
        "cmt_ss_consol_2024_coa",
        "Social security consolidated receipts expenditure 2024 CoA",
        "sec_ss", "All SS beneficiaries", "CoA 182e Boek 2025 over Sociale Zekerheid",
        139300000000, cash_ss,
        "Map total SS envelope vs GG TE",
        "Track beheers 2.8bn efficiency dual OISZ",
        "SS>consolidated>2024", "tick277 primary CoA",
    ))
    f.write(cmt_row(
        "cmt_ehealth_institutional_2022_23",
        "eHealth platform institutional beheer dual INAMI stack",
        "ehealth_platform", "Healthcare providers patients",
        "Wet 21 aug 2008 eHealth + CoA 182e",
        15900000, cash_ehealth,
        "Electronic health data exchange platform operations",
        "Reconcile institutional 15.9m vs INAMI 132.5m; FOI Smals L5",
        "Federal>eHealth>institutional", "tick277 dual INAMI 132.5m not additive",
    ))
    f.write(cmt_row(
        "cmt_fedris_budget_2023_24",
        "Fedris occupational risks package dual OISZ",
        "fedris", "Work accident and occupational disease victims",
        "Wet Fedris 2017 fusion FAO FMP",
        596400000, cash_fedris,
        "Compensate occupational risks",
        "FOI 2024-25 full jaarrekening; beheer efficiency",
        "SS>Fedris>package", "tick277",
    ))
    f.write(cmt_row(
        "cmt_oisz_beheer_sample_2023",
        "OISZ management budgets sample CoA 2023 dual",
        "sec_ss", "SS institutions staff",
        "CoA 182e OISZ account controls 2023",
        590300000, cash_pack,
        "Administrative capacity of public SS institutions",
        "Publish full OISZ beheer matrix multi-year; lag FOI",
        "SS>OISZ>beheer_sample", "tick277 sample not exhaustive",
    ))

lb = [
    "lb_ss_consol_139bn,SS consolidated expenditure 139.3bn 2024,federal,ops,SS>consolidated>exp,139300000000,139300000000,Strong CoA 182e: geconsolideerde SS uitgaven 139.3bn / ontvangsten 139.8bn 2024; core entitlement system not pure waste,strong,src_ccrek_ss_182e_2025,All insured persons,Social protection financing,Largest SS map vs GG TE 348bn,2,10.0,3,5.9,Track multi-year; dual Entity I,seed,,tick277",
    "lb_ss_beheers_2_8bn,SS beheerskosten 2.8bn 2024 CoA,federal,ops,SS>consolidated>beheers,2800000000,2800000000,Strong CoA graphic: Beheerskosten 2.8bn of SS 2024; dual OISZ beheer sample ~0.59bn partial,strong,src_ccrek_ss_182e_2025,OISZ mutualities,SS administration overhead,Admin layer dual mutual 1.38bn VI admin,5,9.0,5,6.5,Publish full OISZ beheer breakdown; dual CDZ,seed,,tick277",
    "lb_ehealth_institutional_15_9m,eHealth institutional beheer 15.9m 2023 dual INAMI,federal,ops,Federal>eHealth>institutional,15900000,15900000,Strong CoA: eHealth beheer 15.9m 2023 (15.3m 2022); dual INAMI e-health stack 132.5m 2025 different perimeter not additive; Smals L5 residual,strong,src_ccrek_ss_182e_2025,Providers patients,Platform operations,Core digital health ops dual Smals KSZ,3,6.0,3,4.95,Reconcile INAMI lines; FOI Smals share,seed,,tick277 dual",
    "lb_fedris_beheer_54m,Fedris management 54.2m 2023,federal,ops,SS>Fedris>beheer,54200000,54200000,Strong CoA: beheer 54.2m 2023; FPS benefit exp 596.4m 2024; dual occupational risk stack,strong,src_ccrek_ss_182e_2025,Victims employers,Agency administration,Core admin not pure waste; accounting findings residual,3,6.0,4,4.9,FOI 2024 jaarrekening; dual unit-cost,seed,,tick277",
    "lb_hziv_634m,HZIV total costs 634.3m 2023 dual mutual,federal,ops,SS>HZIV>total,634300000,634300000,Strong CoA: kosten 634.3m 2023 of which beheer 38.8m; public VI dual landsbond admin 1.38bn,strong,src_ccrek_ss_182e_2025,Affiliates without private mutual,Public health insurance channel,Core SS payment dual mutual admin FOI L5,3,8.0,4,5.7,FOI L5; dual CDZ VI table,seed,,tick277",
    "lb_rva_beheer_278m,RVA management 277.9m 2023 dual HVW,federal,ops,SS>RVA>beheer,277900000,277900000,Strong CoA: RVA beheer 277.9m + HVW beheer 47.9m 2023; opdrachten RVA 6.74bn HVW 0.74bn,strong,src_ccrek_ss_182e_2025,Unemployed,Unemployment administration dual payment channels,Core dual channel; unit cost FOI residual,4,8.0,5,5.9,FOI unit cost gap_unemp still; dual HVW,seed,,tick277",
    "lb_fso_839m_2024,FSO company closure fund 838.7m exp 2024,federal,ops,SS>FSO>exp,838700000,838700000,Strong FPS via CoA: uitgaven 838.7m 2024 (+56pct) rec 522.9m deficit; beheer 7.7m 2023,strong,src_ccrek_ss_182e_2025,Dismissed workers closures,Closure compensations,Cyclical benefit spike not pure waste; recovery path,4,8.0,4,5.7,Track multi-year recoveries,seed,,tick277",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# FOI: OISZ multi-year lag
foi_path = base / "foi_queue.csv"
lines = foi_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
out = []
for line in lines:
    if line.startswith("gap_ehealth_l5_vendors,") and "tick277" not in line:
        line = line.rstrip() + " | tick277: eHealth institutional beheer 15.9m CoA 2023 filled; residual Smals L5 still ready"
    if line.startswith("gap_unemp_pay_unit_cost,") and "tick277" not in line:
        line = line.rstrip() + " | tick277: HVW beheer 47.9m + RVA 277.9m CoA 2023; residual per-union L5 still ready"
    out.append(line)
gap = "gap_oisz_jaarrekeningen_2024_25"
if not any(l.startswith(gap + ",") for l in out):
    out.append(
        f"{gap},SS>OISZ>jaarrekeningen_2024_25,sec_ss,"
        "Machine-readable jaarrekeningen/outturns 2024-2025 for OISZ sample (Fedris HZIV RVA HVW RJV FSO RSVZ RSZ FPD RIZIV) "
        "with beheer vs opdrachten split; CoA notes chronic filing lag (0/12 2023 filed to CoA by Jul 2025 for some),"
        "CoA 2023 tables strong; multi-year 2024-25 and full beheer matrix vs 2.8bn residual,"
        "6,FOD Sociale Zekerheid / OISZ openbaarheid / Rekenhof,,"
        "https://www.socialsecurity.be,"
        f"docs/doge/foi/drafts/{gap}.md,ready,2026-07-30,,,,,,"
        f"cmt_oisz_beheer_sample_2023,lb_ss_beheers_2_8bn,{now},{now},"
        "tick277 draft ready human send; 2023 sample filled"
    )
foi_path.write_text("\n".join(out) + "\n", encoding="utf-8")

# research_queue
rq_path = base / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq:
    if line.startswith("rq_268,"):
        out.append(
            "rq_268,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after KSZ).,"
            f"gap_oisz_jaarrekeningen_2024_25,2026-07-30T00:45:00Z,{now},"
            "tick277: CoA OISZ eHealth 15.9m + SS 139.3bn + beheer sample; spawn rq_269"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_269,") for l in out):
    out.append(
        "rq_269,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CoA OISZ).,,"
        f"{now},,Spawned tick277 after CoA OISZ; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_268,277,no,"
    "Scheduler 60s. Next prio5 rq_269; rq_116 SWA deferred. FOI ready human send. tick277 CoA OISZ eHealth 15.9m SS 139.3bn.\n",
    encoding="utf-8",
)
print("OK tick277")

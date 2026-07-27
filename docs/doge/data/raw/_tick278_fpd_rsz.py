# tick 278 — FPD + RSZ beheer + pension path + OISZ wage matrix CoA
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T01:45:00Z"
src = "src_ccrek_ss_182e_2025"  # already seeded tick277; add note line

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_ss_182e_fpd_rsz,Rekenhof 182e FPD RSZ tables + pensioen path + loonmatrix,"
        "docs/doge/data/raw/ccrek_ss_182e_b_II.pdf#p70-p98,Rekenhof,2026-07-30,court_audit,"
        "FPD beheer 287.7m opdrachten 67.95bn 2023; RSZ beheer 282.8m opdrachten 106.87bn; "
        "pensioenen total 66.764bn 2024; OISZ wage matrix; tick278\n"
    )

with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "fpd,Federale Pensioendienst FPD,Service federal des Pensions SFP,"
        "Federal Pension Service,parastatal,sec_ss,bi,https://www.sfpd.fgov.be,,,"
        "Worker public IGO pensions payment; beheer 287.7m 2023; opdrachten ~68bn; tick278\n"
    )
    f.write(
        "rsz,Rijksdienst voor Sociale Zekerheid RSZ,Office national de securite sociale ONSS,"
        "National Social Security Office,parastatal,sec_ss,bi,https://www.rsz.be,,,"
        "Centralises employee SS funds Globaal Beheer; beheer 282.8m 2023; opdrachten 106.9bn; tick278\n"
    )

bud = [
    "bud_fpd_beheer_2022,fpd,2022,222300000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA tabel29: beheer uitgaven 222.3m 2022",
    "bud_fpd_beheer_2023,fpd,2023,287700000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: beheer 287.7m 2023 (+29.4pct)",
    "bud_fpd_opdrachten_2022,fpd,2022,61753300000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: opdrachten 61.7533bn 2022",
    "bud_fpd_opdrachten_2023,fpd,2023,67947600000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: opdrachten 67.9476bn 2023",
    "bud_fpd_lonen_class,fpd,2023,171300000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA tabel22 loonmatrix: FPD lonen 171.3m (rubriek 621 class)",
    "bud_rsz_beheer_2022,rsz,2022,251900000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA tabel28: beheer 251.9m 2022",
    "bud_rsz_beheer_2023,rsz,2023,282800000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: beheer 282.8m 2023",
    "bud_rsz_opdrachten_2022,rsz,2022,99492800000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: opdrachten 99.4928bn 2022",
    "bud_rsz_opdrachten_2023,rsz,2023,106869700000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: opdrachten 106.8697bn 2023",
    "bud_rsz_lonen_class,rsz,2023,158100000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA loonmatrix: RSZ lonen 158.1m",
    "bud_pensioen_werknemers_2024,sec_ss,2024,40125200000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA tabel3: werknemerspensioenen 40.1252bn 2024",
    "bud_pensioen_overheid_2024,sec_ss,2024,21041000000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: overheidspensioenen 21.041bn 2024",
    "bud_pensioen_zelfstandigen_2024,sec_ss,2024,5597800000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: zelfstandigenpensioenen 5.5978bn 2024",
    "bud_pensioen_total_2024,sec_ss,2024,66764000000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: total pensioenen 66.764bn 2024 (+6.09pct)",
    "bud_pensioen_total_2023,sec_ss,2023,62931400000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA: total pensioenen 62.9314bn 2023",
    "bud_ss_saldo_2024,sec_ss,2024,537300000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA tabel1: SS saldo +537.3m 2024 (was +1322m 2023)",
    "bud_oisz_lonen_rva,rva,2023,210900000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA loonmatrix RVA 210.9m",
    "bud_oisz_lonen_riziv,sec_ss,2023,118200000,,,outturn,src_ccrek_ss_182e_fpd_rsz,medium,CoA loonmatrix RIZIV 118.2m (2023 unaudited note)",
    "bud_oisz_lonen_rsvz,rsvz,2023,66900000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA loonmatrix RSVZ 66.9m",
    "bud_oisz_lonen_hziv,hziv,2023,27300000,,,outturn,src_ccrek_ss_182e_fpd_rsz,strong,CoA loonmatrix HZIV 27.3m",
    "bud_oisz_lonen_sum_sample,sec_ss,2023,848000000,,,outturn,src_ccrek_ss_182e_fpd_rsz,medium,Sum CoA loonmatrix sample ~848m (RSZ RVA Fedris HVW RJV HZIV FPD RSVZ KSZ eHealth RIZIV); not full SS wage bill",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

def cmt(cid, title, ent, ben, env, cash, goal, cut, path, notes):
    j = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
    return (
        f"{cid},{title},{ent},{ben},CoA 182e Boek 2025 SS,2022-01-01,2022,2024,{env},"
        f"{j},0,active,docs/doge/data/raw/ccrek_ss_182e_b_II.pdf,"
        f"{goal},{cut},src_ccrek_ss_182e_fpd_rsz,strong,{path},{notes}\n"
    )

with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt(
        "cmt_fpd_budget_2022_23",
        "Federal Pension Service FPD package dual pension path",
        "fpd", "Pensioners IGO beneficiaries",
        67947600000,
        {
            "beheer_2022_m": 222.3,
            "beheer_2023_m": 287.7,
            "opdrachten_2022_bn": 61.753,
            "opdrachten_2023_bn": 67.948,
            "lonen_m": 171.3,
            "note": "Pays worker public local HR-Rail IGO + self-employed pensions payment channel",
        },
        "Award and pay statutory pensions",
        "FOI 2024-25 jaarrekening; dual unit-cost per pensioner",
        "SS>FPD>package",
        "tick278",
    ))
    f.write(cmt(
        "cmt_rsz_budget_2022_23",
        "RSZ Globaal Beheer treasury dual OISZ financing",
        "rsz", "Employee SS branches OISZ",
        106869700000,
        {
            "beheer_2022_m": 251.9,
            "beheer_2023_m": 282.8,
            "opdrachten_2022_bn": 99.493,
            "opdrachten_2023_bn": 106.870,
            "lonen_m": 158.1,
            "globaal_beheer_costs_class_2023_bn": 87.9,
            "smals_voorschot_gap_m": 2.4,
            "note": "Centralises contributions subsidies alt finance; CoA Smals advance follow-up residual",
        },
        "Collect and distribute employee SS funds",
        "FOI Smals advances L5; dual unit-cost",
        "SS>RSZ>globaal_beheer",
        "tick278 dual Smals",
    ))
    f.write(cmt(
        "cmt_pension_path_2022_24",
        "Belgium statutory pensions multi-regime path CoA",
        "sec_ss", "Retirees workers public self-employed",
        66764000000,
        {
            "total_2022_bn": 57.469,
            "total_2023_bn": 62.931,
            "total_2024_bn": 66.764,
            "werknemers_2024_bn": 40.125,
            "overheid_2024_bn": 21.041,
            "zelfstandigen_2024_bn": 5.598,
            "fpd_beheer_2023_m": 287.7,
            "note": "Dual FPD payment admin; entitlement not pure waste",
        },
        "Income security in old age",
        "Track growth vs demographics; FPD efficiency",
        "SS>pensioenen>multi_regime",
        "tick278",
    ))
    f.write(cmt(
        "cmt_oisz_wage_matrix_coa",
        "OISZ personnel cost matrix CoA wage reconciliation",
        "sec_ss", "OISZ staff",
        848000000,
        {
            "rsz_m": 158.1,
            "rva_m": 210.9,
            "fedris_m": 37.7,
            "hvw_m": 36.6,
            "rjv_m": 17.2,
            "hziv_m": 27.3,
            "fpd_m": 171.3,
            "rsvz_m": 66.9,
            "ksz_m": 3.2,
            "ehealth_m": 0.2,
            "riziv_m": 118.2,
            "sum_sample_m": 848.0,
            "note": "CoA tabel22 rubriek 621 class; FSO n/a no own staff; not full SS wage bill",
        },
        "Map OISZ staffing cost transparency",
        "Complete multi-year wage matrix all OISZ",
        "SS>OISZ>lonen_matrix",
        "tick278",
    ))

lb = [
    "lb_fpd_beheer_288m,FPD management 287.7m 2023 dual pensions,federal,ops,SS>FPD>beheer,287700000,287700000,Strong CoA: beheer 287.7m 2023 (222.3m 2022 +29pct); opdrachten 67.95bn; lonen 171.3m; core pension admin not pure waste,strong,src_ccrek_ss_182e_fpd_rsz,Pensioners,Pension award and payment administration,Core SS admin dual 66.8bn pensions,3,8.0,4,5.7,FOI 2024-25; unit cost per beneficiary,seed,,tick278",
    "lb_rsz_beheer_283m,RSZ management 282.8m 2023 dual Globaal Beheer,federal,ops,SS>RSZ>beheer,282800000,282800000,Strong CoA: beheer 282.8m 2023; opdrachten 106.87bn; lonen 158.1m; Smals advance residual 2.4m CoA finding,strong,src_ccrek_ss_182e_fpd_rsz,Employers OISZ branches,Central SS fund collection distribution,Core treasury dual Smals,3,8.0,4,5.7,FOI Smals advances; dual KSZ,seed,,tick278",
    "lb_pensions_66_8bn,Statutory pensions total 66.8bn 2024,federal,ops,SS>pensioenen>total,66764000000,66764000000,Strong CoA: 66.764bn 2024 (werkn 40.1 + overheid 21.0 + zelfst 5.6); core entitlement not pure waste,strong,src_ccrek_ss_182e_fpd_rsz,Retirees,Old-age income security,Largest SS prestatie block dual FPD,2,10.0,3,5.9,Track multi-year vs demographics,seed,,tick278",
    "lb_oisz_wages_848m,OISZ wage matrix sample ~848m CoA,federal,ops,SS>OISZ>lonen,848000000,848000000,Medium-strong CoA tabel22: sample sum ~848m across 11 OISZ (RVA 211 FPD 171 RSZ 158 RIZIV 118); FSO no staff; not full SS,strong,src_ccrek_ss_182e_fpd_rsz,OISZ employees,Staff cost transparency,Personnel dual beheer packages,4,8.0,4,5.7,Publish annual full matrix; reconcile beheer,seed,,tick278",
    "lb_fpd_rsz_beheer_dual,FPD+RSZ beheer 570.5m 2023 dual OISZ top,federal,ops,SS>OISZ>fpd_rsz_beheer,570500000,570500000,Strong dual: FPD 287.7 + RSZ 282.8 = 570.5m beheer 2023; among largest OISZ admin after prior RVA 278m,strong,src_ccrek_ss_182e_fpd_rsz,Taxpayers SS system,Largest OISZ admin pair,Institutional dual not additive with RVA,4,8.5,4,6.05,Joint efficiency review; dual unit-cost,seed,,tick278 dual not additive",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# update FOI oisz gap
foi_path = base / "foi_queue.csv"
lines = foi_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
out = []
for line in lines:
    if line.startswith("gap_oisz_jaarrekeningen_2024_25,") and "tick278" not in line:
        line = line.rstrip() + " | tick278: FPD+RSZ 2023 beheer filled CoA; residual 2024-25 still ready"
    if line.startswith("gap_smals_l5_members,") and "tick278" not in line:
        line = line.rstrip() + " | tick278: CoA RSZ Smals voorschot residual 2.4m note"
    out.append(line)
foi_path.write_text("\n".join(out) + "\n", encoding="utf-8")

rq_path = base / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq:
    if line.startswith("rq_269,"):
        out.append(
            "rq_269,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CoA OISZ).,"
            f"gap_oisz_jaarrekeningen_2024_25,2026-07-30T01:15:00Z,{now},"
            "tick278: FPD beheer 287.7m RSZ 282.8m pensions 66.8bn wage matrix; spawn rq_270 progress@280"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_270,") for l in out):
    out.append(
        "rq_270,Mandatory progress@280 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
        "When ticks_completed hits 280: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
        "and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
        f"{now},,Spawned tick278; progress in 2 ticks; rq_116 SWA deferred"
    )
if not any(l.startswith("rq_271,") for l in out):
    out.append(
        "rq_271,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills after progress@280 (AGMJ wage if public; other FOI-adjacent).,,"
        f"{now},,Spawned tick278 after FPD RSZ; run after rq_270"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_269,278,no,"
    "Scheduler 60s. Next prio5 rq_271 or progress rq_270@280; rq_116 SWA deferred. tick278 FPD 287.7m RSZ 282.8m pensions 66.8bn.\n",
    encoding="utf-8",
)
print("OK tick278")

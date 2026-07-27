# tick 306 — rq_297 Kamer 56K0983 peer dotatie institutions pack
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T15:45:00Z"
unit = "rq_297"

# --- sources ---
src_line = (
    "src_kamer_56k0983_peer_dotaties,"
    "Kamer 56K0983/001 Comptabiliteit peer dotatie institutions Hof Rekenhof CSJ ComiteP ComiteI,"
    "docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf; "
    "https://www.dekamer.be/FLWB/PDF/56/0983/56K0983001.pdf,"
    "Belgische Kamer van volksvertegenwoordigers commissie Comptabiliteit,"
    "2026-07-30,official_budget,"
    "Hof 2025/26 kred 14.236/14.593m dot 13.573m; Rekenhof 2024 exp 64.847m 2026 kred 71.0m dot freeze 64.563m; "
    "ComiteP 2026 14.961m; CSJ 2026 7.411m; ComiteI 2026 6.937m; tick306\n"
)
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_line)

# --- entities ---
ent_rows = [
    (
        "grondwettelijk_hof,Grondwettelijk Hof,Cour constitutionnelle,"
        "Belgian Constitutional Court,court,sec_federal,bi,"
        "https://www.const-court.be,,,,"
        "Kamer-dotatie; kredieten 14.236m 2025 / 14.593m 2026; staff 96 incl judges; admin 57 eoy2024; "
        "pers ~87.7pct; Regie fee 238k; tick306"
    ),
    (
        "hrj_csj,Hoge Raad voor de Justitie HRJ,Conseil superieur de la Justice CSJ,"
        "High Council of Justice magistrate appointments and audits,agency,sec_federal,bi,"
        "https://hrj.be,,,,"
        "Kamer-dotatie; 2026 kred 7.411m dot 6.915m; ~80pct wages; surplus 2024 0.634m; tick306"
    ),
    (
        "comite_p,Vast Comite P politietoezicht,Comite permanent P controle police,"
        "Standing Police Monitoring Committee,agency,sec_federal,bi,"
        "https://comitep.be,,,,"
        "Kamer-dotatie; 2026 exp 14.961m; pers 93.88pct; late detach billing 1.088m 2024; tick306"
    ),
    (
        "comite_i,Vast Comite I inlichtingendiensten,Comite permanent R renseignement,"
        "Standing Intelligence Services Monitoring Committee,agency,sec_federal,bi,"
        "https://comiteri.be,,,,"
        "Kamer-dotatie; 2026 exp 6.937m; dotatie 4.867m + boni 2.070m; tick306"
    ),
]
# update rekenhof entity notes
ent_path = ROOT / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
old_rh = (
    "rekenhof,Rekenhof,Cour des comptes,Court of Audit,other,gg_belgium,bi,"
    "https://www.ccrek.be,,,Audit source not a spend entity"
)
new_rh = (
    "rekenhof,Rekenhof,Cour des comptes,Court of Audit,agency,gg_belgium,bi,"
    "https://www.ccrek.be,,,,"
    "Kamer-dotatie spend entity: 2024 exp 64.847m; 2026 kred 71.0m; freeze dot 64.563m; "
    "payroll ~82pct; Regie fee 2.04m; tick306"
)
if old_rh in ent_text:
    ent_text = ent_text.replace(old_rh, new_rh)
else:
    # try partial match line
    lines = ent_text.splitlines(True)
    out = []
    for L in lines:
        if L.startswith("rekenhof,") and "tick306" not in L:
            L = (
                "rekenhof,Rekenhof,Cour des comptes,Court of Audit,agency,gg_belgium,bi,"
                "https://www.ccrek.be,,,,"
                "Kamer-dotatie spend entity: 2024 exp 64.847m; 2026 kred 71.0m; freeze dot 64.563m; "
                "payroll ~82pct; Regie fee 2.04m; tick306\n"
            )
        out.append(L)
    ent_text = "".join(out)
with ent_path.open("w", encoding="utf-8", newline="") as f:
    f.write(ent_text)
with ent_path.open("a", encoding="utf-8", newline="") as f:
    for r in ent_rows:
        f.write(r + "\n")

# --- budgets ---
bud_rows = [
    # Grondwettelijk Hof
    "bud_gwh_kred_2025,grondwettelijk_hof,2025,14236000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Kamer: credits/uitgavenbegroting 14.236m 2025 (after -150k commission cut)",
    "bud_gwh_kred_2026,grondwettelijk_hof,2026,14593000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Kamer ontwerp 2026 credits 14.593m (+2.5pct); personnel ~87.7pct",
    "bud_gwh_dotatie_2025,grondwettelijk_hof,2025,13573000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Dotatie 2025 13.573m used as freeze baseline in deficit calc",
    "bud_gwh_boni_for_2026,grondwettelijk_hof,2024,768164,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Cumul result eoy2024 1.431m less 663.2k for 2025 = 768.164k available for 2026",
    "bud_gwh_staff_admin_2024,grondwettelijk_hof,2024,57,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Admin effectifs eoy2024 57 (29 statut 26 contract 2 detaches); total with function holders 96",
    "bud_gwh_regie_fee,grondwettelijk_hof,2026,238000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Occupation fee Regie des Batiments 238k; only Hof+Rekenhof still pay among dotatie institutions",
    # Rekenhof
    "bud_rekenhof_exp_2024,rekenhof,2024,64847000,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Kamer: 2024 expenses 64.847m (+8.6pct vs 2023)",
    "bud_rekenhof_receipts_2024,rekenhof,2024,65375100,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Kamer: 2024 receipts 65.3751m (+7.0pct vs 2023)",
    "bud_rekenhof_boni_2024,rekenhof,2024,4709200,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Boni 4.7092m fully applied to finance 2026",
    "bud_rekenhof_kred_2026,rekenhof,2026,70999700,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "2026 expenditure credits 70.9997m; payroll 58.198m (82pct)",
    "bud_rekenhof_dotatie_freeze_2025,rekenhof,2025,64562800,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Dotatie frozen at 2025 level 64.5628m (Moesen); requested raise to 65.5525m for 2026",
    "bud_rekenhof_dotatie_request_2026,rekenhof,2026,65552500,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Requested dotatie 65.5525m to close ~0.99m deficit class under freeze",
    "bud_rekenhof_regie_fee_2026,rekenhof,2026,2041600,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Regie des Batiments occupation fee 2.0416m 2026",
    # HRJ / CSJ
    "bud_hrj_surplus_2024,hrj_csj,2024,633649,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Comptes 2024 positive balance 633648.88; 150k to 2025 then 483648 for 2026",
    "bud_hrj_kred_2024,hrj_csj,2024,7225000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Credits 7.225m 2024 (baseline in Kamer narrative)",
    "bud_hrj_kred_2026,hrj_csj,2026,7411000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "2026 requested credits 7.411m (+2.5pct vs 2024)",
    "bud_hrj_dotatie_2026,hrj_csj,2026,6915000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Dotatie 6.915m + boni 483.648k + divers 12.351k",
    # Comité P
    "bud_comite_p_surplus_2024,comite_p,2024,245171,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Comptes 2024 surplus 245170.79; personnel 93.88pct of exp",
    "bud_comite_p_exp_2026,comite_p,2026,14961000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "2026 total exp estimated 14.961m",
    "bud_comite_p_dotatie_2026,comite_p,2026,14715829,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Dotatie 14.715829m + boni 245.171k; includes littera C underbudget correction",
    "bud_comite_p_late_billing_2024,comite_p,2024,1088244,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "Late salary billing detaches: federal police 706728.48 + local zone 372782.50 = 1088244 littera C",
    # Comité I
    "bud_comite_i_surplus_2024,comite_i,2024,2069890,,,outturn,src_kamer_56k0983_peer_dotaties,strong,"
    "2024 positive balance 2.06989m (recruitment lag / underspend)",
    "bud_comite_i_exp_2025,comite_i,2025,6393803,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "2025 expenditure baseline 6.393803m",
    "bud_comite_i_exp_2026,comite_i,2026,6937100,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "2026 exp 6.9371m incl digitisation tranche 850k",
    "bud_comite_i_dotatie_2025,comite_i,2025,5180000,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Dotatie 2025 5.180m",
    "bud_comite_i_dotatie_2026,comite_i,2026,4867210,,,budgeted,src_kamer_56k0983_peer_dotaties,strong,"
    "Dotatie 2026 4.86721m (-6.4pct) + boni 2.069889m",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

# --- commitments ---
cmt_rows = [
    (
        "cmt_gwh_package_2025_26,Grondwettelijk Hof Kamer-dotatie package,grondwettelijk_hof,"
        "Constitutional litigants democracy,Special law 6 Jan 1989 Cour constitutionnelle,"
        "1989-01-06,2025,2026,28829000,"
        '"{""kred_2025"":14236000,""kred_2026"":14593000,""dotatie_2025"":13573000,'
        '""boni_for_2026"":768164,""deficit_if_freeze_2026"":252000,'
        '""staff_total_incl_judges"":96,""admin_eoy2024"":57,""pers_pct"":87.7,'
        '""regie_fee"":238000,""note"":""Moesen freeze + boni exhaustion risk from 2027""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "Constitutional review of laws and decrees,"
        "Core judiciary; FOI multi-year littera optional; dual Rekenhof Regie fee,"
        "src_kamer_56k0983_peer_dotaties,strong,Federal>Parlement>Grondwettelijk_Hof,tick306"
    ),
    (
        "cmt_rekenhof_package_2024_26,Rekenhof Court of Audit Kamer-dotatie package,rekenhof,"
        "Parliament taxpayers audited entities,Court of Audit organic law,"
        "1831-01-01,2024,2026,200746800,"
        '"{""exp_2024"":64847000,""receipts_2024"":65375100,""boni_2024"":4709200,'
        '""kred_2026"":70999700,""dotatie_freeze_2025"":64562800,""dotatie_request_2026"":65552500,'
        '""payroll_2026"":58198300,""pers_pct"":82.0,""regie_fee_2026"":2041600,'
        '""deficit_class_freeze"":989700,""note"":""Largest Kamer-dotatie spend body; dual Hof Regie fee""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "External audit of public finances,"
        "Core control institution; publish multi-year freeze impact; not pure waste,"
        "src_kamer_56k0983_peer_dotaties,strong,Federal>Parlement>Rekenhof,tick306"
    ),
    (
        "cmt_comite_p_package_2024_26,Comite P police oversight Kamer-dotatie,comite_p,"
        "Citizens police accountability,Standing Committee police control law,"
        "1991-07-18,2024,2026,14961000,"
        '"{""surplus_2024"":245171,""exp_2026"":14961000,""dotatie_2026"":14715829,'
        '""pers_pct"":93.88,""late_billing_detaches_2024"":1088244,'
        '""note"":""Littera C underbudget from unbilled detaches federal+local police""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "External control of police services,"
        "Fix detach billing controls; dual Comite I intelligence,"
        "src_kamer_56k0983_peer_dotaties,strong,Federal>Parlement>Comite_P,tick306"
    ),
    (
        "cmt_hrj_package_2024_26,Hoge Raad voor de Justitie CSJ Kamer-dotatie,hrj_csj,"
        "Magistrates judicial system,High Council of Justice law,"
        "1998-12-22,2024,2026,14636000,"
        '"{""kred_2024"":7225000,""kred_2026"":7411000,""dotatie_2026"":6915000,'
        '""surplus_2024"":633649,""boni_for_2026"":483648,""diverse_2026"":12351,'
        '""wage_share_class"":0.80}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "Magistrate selection training audits citizen complaints justice,"
        "Core judicial governance; dual Hof ComiteP,"
        "src_kamer_56k0983_peer_dotaties,strong,Federal>Parlement>HRJ,tick306"
    ),
    (
        "cmt_comite_i_package_2024_26,Comite I intelligence oversight Kamer-dotatie,comite_i,"
        "Parliamentary intelligence control,Standing Committee intelligence services,"
        "1991-07-18,2024,2026,13330903,"
        '"{""surplus_2024"":2069890,""exp_2025"":6393803,""exp_2026"":6937100,'
        '""dotatie_2025"":5180000,""dotatie_2026"":4867210,""digitisation_tranche"":850000,'
        '""note"":""Dotatie -6.4pct funded by large 2024 boni; no new staff 2026""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "External control of intelligence and security services,"
        "Dual Comite P police; FOI L5 digitisation optional,"
        "src_kamer_56k0983_peer_dotaties,strong,Federal>Parlement>Comite_I,tick306"
    ),
    (
        "cmt_kamer_dotatie_oversight_pack_2026,Kamer-dotatie oversight pack 2026 (5 peers excl GBA Ombuds FIRM),gg_belgium,"
        "Parliament democratic control institutions,Kamer Comptabiliteit cycle 56K0983,"
        "2025-06-04,2026,2026,114871800,"
        '"{""rekenhof_kred_2026"":70999700,""comite_p_2026"":14961000,""gwh_2026"":14593000,'
        '""hrj_2026"":7411000,""comite_i_2026"":6937100,'
        '""sum_5"":114871800,""excl"":""GBA~15m FedOmbuds~8.3m FIRM~3.5m already mapped"",'
        '""moesen"":""nominal freeze legislative institutions CM 14Feb2025""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "Map material Kamer-dotatie democratic control spend,"
        "Publish consolidated table; dual avoid double-count with entity rows,"
        "src_kamer_56k0983_peer_dotaties,strong,Federal>Parlement>dotatie_pack,tick306"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

# --- leaderboard ---
lb_rows = [
    (
        "lb_rekenhof_budget_71m,Rekenhof Court of Audit budget class ~65-71m,federal,ops,"
        "Federal>Parlement>Rekenhof,64847000,70999700,"
        "Strong Kamer: 2024 exp 64.847m; 2026 kred 71.0m; freeze dot 64.563m; payroll 82pct; Regie 2.04m,"
        "strong,src_kamer_56k0983_peer_dotaties,Taxpayers parliament,External audit public finances,"
        "Core control institution; freeze vs wage drift tension,"
        "2,7.0,2,4.1,Keep; publish freeze impact multi-year; not waste,"
        "seed,,tick306 largest Kamer-dotatie spend"
    ),
    (
        "lb_gwh_budget_14_5m,Grondwettelijk Hof budget ~14.2-14.6m,federal,ops,"
        "Federal>Parlement>Grondwettelijk_Hof,14236000,14593000,"
        "Strong Kamer: 14.236m 2025 / 14.593m 2026; dot 13.573m; staff 96; pers 87.7pct; Regie 238k,"
        "strong,src_kamer_56k0983_peer_dotaties,Constitutional litigants,Constitutional review,"
        "Core judiciary; Moesen freeze deficit risk 252k 2026,"
        "2,5.5,2,3.6,Keep; dual Rekenhof Regie fee anomaly,"
        "seed,,tick306"
    ),
    (
        "lb_comite_p_15m,Comite P police oversight ~15.0m 2026,federal,ops,"
        "Federal>Parlement>Comite_P,14961000,14961000,"
        "Strong Kamer: 2026 exp 14.961m; pers 93.88pct; late detach billing 1.088m 2024,"
        "strong,src_kamer_56k0983_peer_dotaties,Citizens police,External police control,"
        "Billing control failure on detaches; dual Comite I,"
        "5,5.5,3,5.0,Fix detach billing; dual intelligence Comite I,"
        "seed,,tick306"
    ),
    (
        "lb_hrj_7_4m,Hoge Raad Justitie CSJ ~7.4m 2026,federal,ops,"
        "Federal>Parlement>HRJ,7411000,7411000,"
        "Strong Kamer: 7.411m 2026 (7.225m 2024); dot 6.915m; surplus 0.634m 2024,"
        "strong,src_kamer_56k0983_peer_dotaties,Magistrates citizens,Magistrate selection and justice audits,"
        "Core judicial governance,"
        "2,4.5,2,3.1,Keep; dual Hof,"
        "seed,,tick306"
    ),
    (
        "lb_comite_i_6_9m,Comite I intelligence oversight ~6.9m 2026,federal,ops,"
        "Federal>Parlement>Comite_I,6937100,6937100,"
        "Strong Kamer: 6.937m 2026; dot 4.867m + boni 2.07m; surplus 2.07m 2024,"
        "strong,src_kamer_56k0983_peer_dotaties,Parliament intelligence control,Intelligence services oversight,"
        "Large boni from underspend; dual Comite P,"
        "3,4.5,2,3.5,Fill or right-size; dual police Comite P,"
        "seed,,tick306"
    ),
    (
        "lb_kamer_dotatie_pack_115m,Kamer-dotatie oversight pack 5 peers ~115m 2026,federal,ops,"
        "Federal>Parlement>dotatie_pack_5,114871800,114871800,"
        "Strong sum Rekenhof 71.0 + ComiteP 15.0 + Hof 14.6 + HRJ 7.4 + ComiteI 6.9 = 114.9m; excl GBA Ombuds FIRM,"
        "strong,src_kamer_56k0983_peer_dotaties,Taxpayers democracy,Democratic control infrastructure,"
        "Material parliamentary-dotation spend cluster; Moesen freeze,"
        "3,7.5,3,5.2,Publish consolidated open table all dotatie institutions,"
        "seed,,tick306 dual GBA~15m FedOmbuds~8.3m"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

# --- foi ---
foi_line = (
    "gap_kamer_dotatie_pack_l5,Federal>Parlement>dotatie_institutions>L5_pack,gg_belgium,"
    "Machine-readable multi-year table 2023-2026 for all Kamer-dotatie institutions: kredieten outturn "
    "dotatie boni FTE by institution (Hof Rekenhof CSJ ComiteP ComiteI GBA Ombuds FIRM CTRG etc); "
    "littera A/B/C personnel vs ops where material,"
    "Pack totals strong from 56K0983 narrative; no single public consolidated L5 CSV; Moesen freeze tracking,"
    "5,Kamer van volksvertegenwoordigers commissie Comptabiliteit,,"
    "https://www.dekamer.be,"
    "docs/doge/foi/drafts/gap_kamer_dotatie_pack_l5.md,ready,2026-07-30,,,,,,"
    "cmt_kamer_dotatie_oversight_pack_2026,lb_kamer_dotatie_pack_115m,"
    "2026-07-30T15:45:00Z,2026-07-30T15:45:00Z,tick306 draft ready human send\n"
)
with (ROOT / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

# --- research_queue ---
rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_297,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Kamer 56K0983 peer institutions: Grondwettelijk Hof Rekenhof FIRM CTRG HRJ; AGMJ if extractable). Prefer before idle.,,"
    "2026-07-30T15:15:00Z,,Spawned tick305 after Federale Ombudsman; rq_116 SWA deferred"
)
new = (
    "rq_297,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Kamer 56K0983 peer institutions: Grondwettelijk Hof Rekenhof FIRM CTRG HRJ; AGMJ if extractable). Prefer before idle.,"
    "gap_kamer_dotatie_pack_l5,2026-07-30T15:15:00Z,2026-07-30T15:45:00Z,"
    "tick306: pack Hof 14.6m Rekenhof 71m ComiteP 15.0m HRJ 7.4m ComiteI 6.9m sum~115m; FOI consolidated L5; spawn rq_298"
)
if old not in text:
    raise SystemExit("rq_297 not found:\n" + repr(text[-400:]))
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_298,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Kamer 56K0983 residual FIRM CTRG deepen if numbers; Raad van State; AGMJ if extractable). Prefer before idle.,,"
    "2026-07-30T15:45:00Z,,Spawned tick306 after Kamer dotatie pack; rq_116 SWA deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

# --- loop_state ---
(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},306,no,"
    "Scheduler 60s. Next prio5 rq_298; rq_116 SWA deferred. FOI ready. "
    "tick306 Kamer-dotatie pack ~115m (Rekenhof 71m).\n",
    encoding="utf-8",
)

print("CSV updates OK")

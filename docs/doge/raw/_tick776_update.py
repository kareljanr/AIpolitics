from pathlib import Path
import re

base = Path(r"docs/doge/data")
utc = "2026-08-03T12:00:00Z"
src = "src_kamer_saca_1281_021_2026"
src_dual = "src_dual_saca_eid_consular_tick776"

# --- entities ---
ents = base / "entities.csv"
ent_rows = [
"saca_eid_rrn,ADBA eID en Rijksregister EN_61023,SACA cartes d identite et Registre national EN_61023,SACA eID and National Register,agency,fod_ibz,bi,https://www.ibz.be,,,Pers 14.851m ops 56.307 Smals/Belnet 2.404 invest 2.667 rec public 73.578m 2026; tick776",
"fedorest,FEDOREST EN_61038 federale restaurant- en cateringdienst,FEDOREST EN_61038,Federal staff restaurants SACA FEDOREST,agency,sec_federal,bi,,,Federal staff catering SACA; total rec/exp class 35.972m 2026; tick776",
"saca_consulaires,ADBA Consulaire zaken,SACA Activites consulaires,SACA Consular affairs,agency,fod_foreign_affairs,bi,https://diplomatie.belgium.be,,,Pers 13.278m ops 34.303m passport/visa personalisation 2026; tick776",
"saca_ans,ADBA Nationale Veiligheidsoverheid EN_61049,SACA Autorite Nationale de Securite EN_61049,National Security Authority SACA,agency,sec_federal,bi,,,Ops 1.79m + servers 0.06 + invest 0.4; retributions 2.25m 2026; tick776",
"saca_defence_horeca,Restauratie- en hoteldienst Defensie EN_61042,Service restauration et hotellerie Defense EN_61042,Defence restaurant and hotel service SACA,agency,defence,bi,,,Ops n.lim 11.625m + lim 0.035m 2026; tick776",
"residence_palace,Internationaal Perscentrum Residence Palace EN_61019,Centre de Presse international Residence Palace,International Press Centre Residence Palace,agency,fod_kanselarij,bi,https://www.presscenter.org,,,Staff 0.527m; building ops class ~2.3m narrative 2026; tick776",
"nicc,Nationaal Instituut voor Criminalistiek en Criminologie NICC,Institut national de criminalistique et de criminologie INCC,National Institute of Criminalistics and Criminology,agency,fod_justice,bi,https://nicc.fgov.be,,,SACA transfer 16.025m 2026; personnel on dot class 11.199m; tick776",
"orb,Koninklijke Sterrenwacht van Belgie ORB,Observatoire royal de Belgique ORB,Royal Observatory of Belgium,agency,belspo,bi,https://www.astro.oma.be,,,Pers on dot 8.695m 2026 SACA 021; tick776",
"saca_cc_egmont,ADBA CC Egmont,SACA CC Egmont,SACA Conference Centre Egmont,agency,fod_foreign_affairs,bi,,,Ops 0.339m + Sablon 0.015m 2026; tick776",
"saca_activites_sociales,SACA Activites sociales,SACA Activites sociales,SACA Social activities federal staff,agency,sec_federal,bi,,,Ops class 0.614m / 0.585m; dot 29k 2026; tick776",
]
text = ents.read_text(encoding="utf-8")
for row in ent_rows:
    eid = row.split(",")[0]
    if f"\n{eid}," not in text and not text.startswith(f"{eid},"):
        with ents.open("a", encoding="utf-8", newline="\n") as f:
            f.write(row + "\n")
        print("entity +", eid)
    else:
        print("entity exists", eid)

# --- sources ---
src_path = base / "sources.csv"
src_rows = [
f"{src},Kamer DOC 56 1281/021 SACA ADBA residual budgets 2026 (non-RGA),https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,Kamer / Chambre,2026-08-03,parliamentary,Strong tick776: 248p; eID/RRN EN_61023 pers 14.851 ops 56.307 Smals 2.404 invest 2.667 rec 73.578; consular 13.278+34.303; FEDOREST 35.972; BELNET transfer 22.367; HDA pers 6.948 ops 2.678+0.483 dot 10.109; ANS 1.79; Def horeca 11.625; scientific dots; RGA already tick755; raw 56K1281021_saca.pdf",
f"{src_dual},Dual SACA eID/RRN vs consular passport/visa + Smals/Belnet residual tick776,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,DOGE synthesis Kamer 1281/021,2026-08-03,synthesis,Strong dual not TE-additive: eID/RRN ~76.2m spend class vs consular 47.6m document personalisation; Smals/Belnet eID 2.404 dual Belnet 22.367",
]
st = src_path.read_text(encoding="utf-8")
for row in src_rows:
    sid = row.split(",")[0]
    if f"\n{sid}," not in st:
        with src_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(row + "\n")
        print("source +", sid)

# --- budgets ---
bud = base / "budgets.csv"
bud_rows = [
f"bud_saca_eid_rrn_pers_2026,saca_eid_rrn,2026,14850892,,,budgeted,{src},strong,11.00.00 pers eID+RRN 14.851m 2026; tick776",
f"bud_saca_eid_rrn_ops_2026,saca_eid_rrn,2026,56306666,,,budgeted,{src},strong,12.11.00 ops 56.307m 2026 card production class; tick776",
f"bud_saca_eid_rrn_smals_belnet_2026,saca_eid_rrn,2026,2403849,,,budgeted,{src},strong,12.21.00 eGOV Smals Belnet Regie 2.404m 2026; tick776",
f"bud_saca_eid_rrn_invest_2026,saca_eid_rrn,2026,2667000,,,budgeted,{src},strong,74.22 invest RRN+eID 2.667m 2026; tick776",
f"bud_saca_eid_rrn_spend_class_2026,saca_eid_rrn,2026,76228407,,,budgeted,{src},strong,Sum pers+ops+12.21+invest 76.228m 2026 class; tick776",
f"bud_saca_eid_rrn_rec_public_2026,saca_eid_rrn,2026,73577750,,,budgeted,{src},strong,16.20 rec public sector card cost recovery 73.578m 2026; tick776",
f"bud_saca_eid_rrn_rec_enterprise_2026,saca_eid_rrn,2026,5368900,,,budgeted,{src},strong,16.11 rec enterprises 5.369m 2026; tick776",
f"bud_saca_cons_pers_2026,saca_consulaires,2026,13277991,,,budgeted,{src},strong,11.xx pers 13.278m 2026 consular contracts+agents; tick776",
f"bud_saca_cons_ops_2026,saca_consulaires,2026,34303086,,,budgeted,{src},strong,12.11 ops 34.303m passport visa personalisation; tick776",
f"bud_saca_cons_ops_core_2026,saca_consulaires,2026,34260162,,,budgeted,{src},strong,12.11.00/001 FF core 34.260m 2026; tick776",
f"bud_saca_cons_stack_2026,saca_consulaires,2026,47581077,,,budgeted,{src},strong,Pers+ops stack 47.581m 2026; tick776",
f"bud_saca_cons_telework_2026,saca_consulaires,2026,42924,,,budgeted,{src},strong,Telework forfait 42.924 2026; tick776",
f"bud_fedorest_total_2026,fedorest,2026,35972000,,,budgeted,{src},strong,Total rec/exp class 35.972m 2026 (sales+transfer); tick776",
f"bud_fedorest_transfer_2026,fedorest,2026,30772000,,,budgeted,{src},strong,46.10 institutional transfer 30.772m 2026; tick776",
f"bud_fedorest_sales_2026,fedorest,2026,5200000,,,budgeted,{src},strong,16.12+16.20 sales 4.6+0.6=5.2m 2026; tick776",
f"bud_fedorest_pers_base_2026,fedorest,2026,17886140,,,budgeted,{src},strong,11.11 baremes 17.886m 2026; tick776",
f"bud_fedorest_ops_ext_2026,fedorest,2026,2951000,,,budgeted,{src},strong,12.11 external ops 2.951m 2026; tick776",
f"bud_fedorest_invest_mat_2026,fedorest,2026,1511000,,,budgeted,{src},strong,74.22 materiel 1.511m 2026; tick776",
f"bud_def_horeca_ops_nlim_2026,saca_defence_horeca,2026,11625000,,,budgeted,{src},strong,12.11 n.lim food/ops 11.625m 2026; tick776",
f"bud_def_horeca_ops_lim_2026,saca_defence_horeca,2026,35000,,,budgeted,{src},strong,12.11 lim software maint 35k 2026; tick776",
f"bud_saca_ans_ops_2026,saca_ans,2026,1790000,,,budgeted,{src},strong,12.11 ops 1.79m 2026; tick776",
f"bud_saca_ans_servers_2026,saca_ans,2026,60000,,,budgeted,{src},strong,12.21 public server rent 60k 2026; tick776",
f"bud_saca_ans_invest_2026,saca_ans,2026,400000,,,budgeted,{src},strong,74.22 invest 0.4m 2026; tick776",
f"bud_saca_ans_spend_class_2026,saca_ans,2026,2311200,,,budgeted,{src},strong,Ops+servers+withholding 61.2k+invest ~2.311m 2026; tick776",
f"bud_saca_ans_retrib_2026,saca_ans,2026,2250000,,,budgeted,{src},strong,16.11 security clearance retributions 2.25m 2026; tick776",
f"bud_saca_ans_interest_2026,saca_ans,2026,204000,,,budgeted,{src},strong,26.20 debt agency interest 0.204m 2026; tick776",
f"bud_hda_pers_saca_2026,hda,2026,6948204,,,budgeted,{src},strong,11.00 pers 6.948m 2026 incl eHealth Sciensano transfer +6m CM 12/12/2025; tick776",
f"bud_hda_ops_ext_saca_2026,hda,2026,2677812,,,budgeted,{src},strong,12.11 ops 2.678m 2026; tick776",
f"bud_hda_ops_public_saca_2026,hda,2026,482984,,,budgeted,{src},strong,12.21 public-sector ops 0.483m 2026; tick776",
f"bud_hda_ops_total_saca_2026,hda,2026,3160796,,,budgeted,{src},strong,Ops total 3.161m 2026; tick776",
f"bud_hda_dot_saca_confirm_2026,hda,2026,10109000,,,budgeted,{src},strong,46.10 dot 10.109m 2026 confirms 014 path (eHealth fusion); tick776",
f"bud_belnet_transfer_saca_2026,belnet,2026,22367000,,,budgeted,{src},strong,46.10 post-conclave transfer 22.367m 2026 SACA 021; tick776",
f"bud_belnet_pers_dot_2026,belnet,2026,4832262,,,budgeted,{src},strong,Pers on Belnet dot 4.832m 2026; tick776",
f"bud_belnet_ops_dot_2026,belnet,2026,16526218,,,budgeted,{src},strong,Ops on Belnet dot 16.526m 2026; tick776",
f"bud_belnet_services_rec_2026,belnet,2026,7124000,,,budgeted,{src},strong,Services sales class 7.124m 2026; tick776",
f"bud_kbr_pers_dot_2026,kbr,2026,12613643,,,budgeted,{src},strong,11.00/001 pers on dot 12.614m 2026; tick776",
f"bud_kbr_ops_dot_2026,kbr,2026,3956357,,,budgeted,{src},strong,12.11 dot ops+telework 3.881+0.075=3.956m 2026; tick776",
f"bud_ara_pers_dot_2026,ara,2026,14688903,,,budgeted,{src},strong,11.00/001 pers on dot 14.689m 2026; tick776",
f"bud_ara_dot_2026,ara,2026,16128000,,,budgeted,{src},strong,46.10 Belspo dot 16.128m 2026; tick776",
f"bud_kmi_pers_dot_2026,kmi,2026,10283753,,,budgeted,{src},strong,11.04 pers on dot 10.284m incl STCE -3.6pct 2026; tick776",
f"bud_kmi_dot_stack_2026,kmi,2026,14674000,,,budgeted,{src},strong,46.10 CF_01 stack 14.674m 2026; tick776",
f"bud_bira_pers_dot_2026,bira,2026,7286457,,,budgeted,{src},strong,Pers on dot 7.286m 2026; tick776",
f"bud_bira_dot_2026,bira,2026,6871000,,,budgeted,{src},strong,46.10 Belspo dot 6.871m 2026; tick776",
f"bud_kbin_dot_2026,kbin,2026,23652000,,,budgeted,{src},strong,46.10 main stack 23.652m 2026 (gen+Belgica class); tick776",
f"bud_kbin_pers_dot_2026,kbin,2026,17064607,,,budgeted,{src},strong,Pers on dot 17.065m 2026; tick776",
f"bud_kmma_dot_saca_2026,kmma,2026,11784000,,,budgeted,{src},strong,46.10 CF_01 11.784m 2026 confirms 018; tick776",
f"bud_kmkg_dot_2026,kmkg,2026,14587000,,,budgeted,{src},strong,46.10 CF_01 14.587m 2026; tick776",
f"bud_kmskb_pers_dot_2026,kmskb,2026,8041724,,,budgeted,{src},strong,Pers on dot 8.042m 2026; tick776",
f"bud_kik_dot_saca_2026,kik,2026,6705000,,,budgeted,{src},strong,46.10 table 6.705m 2026 (narrative 6.810 class); tick776",
f"bud_nicc_transfer_2026,nicc,2026,16025000,,,budgeted,{src},strong,46.10 transfer 16.025m 2026; tick776",
f"bud_nicc_pers_dot_core_2026,nicc,2026,11199111,,,budgeted,{src},strong,Baremes on dot core 11.199m of 16.679m pers stack; tick776",
f"bud_orb_pers_dot_2026,orb,2026,8695439,,,budgeted,{src},strong,Pers on dot 8.695m 2026; tick776",
f"bud_residence_palace_pers_2026,residence_palace,2026,527000,,,budgeted,{src},strong,Staff envelope 0.527m 2026; tick776",
f"bud_residence_palace_ops_narrative_2026,residence_palace,2026,2345000,,,budgeted,{src},medium,Narrative ops 1.15 building+0.245 maint+0.95 tech AV class ~2.345m; tables partial kEUR scale; tick776",
f"bud_cc_egmont_ops_2026,saca_cc_egmont,2026,338754,,,budgeted,{src},strong,Ops 0.339m + Sablon 15k in table; tick776",
f"bud_saca_social_ops_2026,saca_activites_sociales,2026,614000,,,budgeted,{src},strong,Ops 0.614m 2026; tick776",
f"bud_saca_social_dot_2026,saca_activites_sociales,2026,29000,,,budgeted,{src},strong,Dot 29k 2026; tick776",
]
bt = bud.read_text(encoding="utf-8")
added_b = 0
with bud.open("a", encoding="utf-8", newline="\n") as f:
    for row in bud_rows:
        bid = row.split(",")[0]
        if f"\n{bid}," not in bt and not bt.startswith(f"{bid},"):
            f.write(row + "\n")
            added_b += 1
        else:
            print("bud exists", bid)
print("budgets added", added_b)

# --- commitments ---
cmt = base / "commitments.csv"
cmt_rows = [
f'cmt_saca_eid_rrn_2026,SACA eID/RRN spend class 76.2m 2026,saca_eid_rrn,citizens communes,KB RRN fees + eID cost recovery,2026-01-28,2026,2026,76228407,"{{""pers"": 14850892, ""ops"": 56306666, ""smals_belnet_regie"": 2403849, ""invest"": 2667000, ""rec_public"": 73577750}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,eID card and National Register production cost recovery,Smals dual FOI,{src},strong,Federal>IBZ>eID_RRN,tick776',
f'cmt_saca_consular_2026,SACA Consular affairs 47.6m 2026,saca_consulaires,passports visas,ADBA Consulaire zaken,2026-01-28,2026,2026,47581077,"{{""pers"": 13277991, ""ops"": 34303086}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,Passport visa personalisation and consular staff,Dual eID FOI,{src},strong,Federal>BZ>consular_saca,tick776',
f'cmt_fedorest_2026,FEDOREST federal restaurants 36.0m 2026,fedorest,federal staff,EN-61038 FEDOREST,2026-01-28,2026,2026,35972000,"{{""transfer"": 30772000, ""sales"": 5200000}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,Staff catering SACA,Benchmark FOI,{src},strong,Federal>FEDOREST,tick776',
f'cmt_def_horeca_2026,Defence HORECA SACA ops 11.6m 2026,saca_defence_horeca,Defence personnel,EN_61042,2026-01-28,2026,2026,11660000,"{{""ops_nlim"": 11625000, ""ops_lim"": 35000}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,Defence catering hotelling,Dual FEDOREST,{src},strong,Federal>Defence>horeca,tick776',
f'cmt_hda_ehealth_transfer_2026,HDA eHealth Sciensano transfer +6m 2026,hda,HDA,CM 12/12/2025 notification,2025-12-12,2026,2026,6000000,"{{""pers_total"": 6948204, ""dot"": 10109000, ""ops"": 3160796, ""note"": ""+6m eHealth from Sciensano -0.382m subsidies to FPS""}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,eHealth service transfer to HDA,FTE FOI,{src},strong,Federal>HDA>eHealth,tick776',
f'cmt_belnet_saca_2026,BELNET SACA transfer 22.367m 2026,belnet,research network,EN_61018,2026-01-28,2026,2026,22367000,"{{""transfer"": 22367000, ""pers_dot"": 4832262, ""ops_dot"": 16526218, ""services"": 7124000}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,NREN public transfer,Dual eID Smals,{src},strong,Federal>BELSPO>BELNET,tick776',
f'cmt_scientific_saca_dots_2026,Scientific ADBA Belspo dots stack 2026,belspo,FWI museums institutes,Kamer 1281/021,2026-01-28,2026,2026,0,"{{""kbr"": 17.056, ""ara"": 16.128, ""kmi"": 14.674, ""bira"": 6.871, ""kbin"": 23.652, ""kmma"": 11.784, ""kmkg"": 14.587, ""kik"": 6.705, ""nicc"": 16.025, ""kmskb_pers_dot"": 8.042, ""note_mEUR"": true, ""not_sum_TE"": true}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,Map federal scientific SACA dots,L5 FOI,{src},strong,Federal>BELSPO>scientific_saca,tick776',
f'cmt_dual_saca_eid_consular_tick776,Dual eID/RRN vs consular document channels tick776,gg_belgium,SACA dual map,Kamer 1281/021,2026-01-28,2026,2026,0,"{{""eid_rrn_spend_m"": 76.228, ""consular_m"": 47.581, ""fedorest_m"": 35.972, ""belnet_m"": 22.367, ""hda_dot_m"": 10.109, ""note"": ""not TE-additive""}}",0,active,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281021.pdf,Map dual document identity channels,L5 FOI,{src},strong,Belgium>dual>saca_eid_consular,tick776',
]
ct = cmt.read_text(encoding="utf-8")
added_c = 0
with cmt.open("a", encoding="utf-8", newline="\n") as f:
    for row in cmt_rows:
        cid = row.split(",")[0]
        if f"\n{cid}," not in ct:
            f.write(row + "\n")
            added_c += 1
print("commitments added", added_c)

# --- leaderboard ---
lb = base / "leaderboard.csv"
lb_rows = [
f"lb_saca_eid_rrn_76m_2026,SACA eID/RRN spend class 76.2m 2026,L5,ops,Federal>IBZ>eID_RRN,76228407,76228407,Strong pers 14.85 + ops 56.31 + Smals 2.40 + invest 2.67; rec 73.58 public,strong,{src},citizens,see,primary Kamer,4.0,8.5,3.0,5.7,Smals dual FOI,active,,tick776",
f"lb_saca_consular_47_6m_2026,SACA Consular 47.6m 2026,L5,ops,Federal>BZ>consular,47581077,47581077,Strong pers 13.28 + ops 34.30 passport/visa personalisation,strong,{src},travelers,see,primary Kamer,3.5,7.5,3.0,5.0,Dual eID FOI,active,,tick776",
f"lb_fedorest_36m_2026,FEDOREST federal restaurants 36.0m 2026,L5,ops,Federal>FEDOREST,35972000,35972000,Strong total 35.972m transfer 30.772 sales 5.2,strong,{src},federal staff,see,primary Kamer,4.5,7.0,2.5,5.15,Benchmark FOI,active,,tick776",
f"lb_def_horeca_11_6m_2026,Defence HORECA SACA 11.6m 2026,L5,ops,Federal>Defence>horeca,11625000,11625000,Strong n.lim food ops 11.625m dual FEDOREST,strong,{src},defence staff,see,primary Kamer,4.0,5.5,2.5,4.45,Dual catering FOI,active,,tick776",
f"lb_belnet_transfer_22_4m_2026,BELNET transfer 22.367m 2026,L5,transfer,Federal>BELSPO>BELNET,22367000,22367000,Strong post-conclave SACA transfer dual eID Smals,strong,{src},research network,see,primary Kamer,3.0,6.5,3.0,4.55,Dual ICT FOI,active,,tick776",
f"lb_hda_dot_10_1m_2026,HDA dot 10.109m + eHealth transfer 2026,L5,transfer,Federal>HDA,10109000,10109000,Strong +6m Sciensano eHealth; pers 6.948 ops 3.161,strong,{src},health data,see,primary Kamer,3.5,5.5,3.0,4.45,FTE FOI,active,,tick776",
f"lb_nicc_16m_2026,NICC SACA transfer 16.025m 2026,L5,transfer,Federal>Justice>NICC,16025000,16025000,Strong forensic institute transfer; pers core 11.199m,strong,{src},justice,see,primary Kamer,3.0,6.0,3.0,4.4,L5 FOI,active,,tick776",
f"lb_kbin_dot_23_7m_2026,KBIN scientific SACA dot 23.652m 2026,L5,transfer,Federal>BELSPO>KBIN,23652000,23652000,Strong largest scientific ADBA; Belgica/JEMU class in stack,strong,{src},science,see,primary Kamer,2.5,6.5,3.0,4.35,L5 FOI,active,,tick776",
f"lb_saca_ans_2_3m_2026,ANS National Security Authority ~2.3m 2026,L5,ops,Federal>ANS,2311200,2311200,Strong ops 1.79+0.06+0.4; retributions 2.25,strong,{src},security clearances,see,primary Kamer,3.5,3.5,2.0,3.3,Transparency FOI,active,,tick776",
f"lb_dual_saca_eid_consular_2026,Dual SACA eID/RRN vs consular document map,L5,transfer,Belgium>dual>saca_eid_consular,76228407,0,Strong dual not TE-additive document identity stack,strong,{src_dual},public,see,primary Kamer,4.5,8.0,3.0,5.55,L5 FOI,active,,tick776",
]
lt = lb.read_text(encoding="utf-8")
added_l = 0
with lb.open("a", encoding="utf-8", newline="\n") as f:
    for row in lb_rows:
        lid = row.split(",")[0]
        if f"\n{lid}," not in lt:
            f.write(row + "\n")
            added_l += 1
print("leaderboard added", added_l)

# --- foi_queue ---
foi = base / "foi_queue.csv"
gap = "gap_saca_eid_consular_fedorest_l5"
foi_row = (
    f"{gap},Federal>SACA>eID_consular_FEDOREST_L5,saca_eid_rrn,"
    "eID/RRN unit cost and Smals/Belnet FTE behind 76.2m; consular passport volume behind 47.6m; "
    "FEDOREST meal unit cost/staff FTE behind 36m; HDA eHealth transfer FTE; BELNET dual recharge; ANS retribution tariff,"
    "Large SACA document and catering channels public at aggregate only,8,"
    "FOD IBZ / FOD BZ / BOSA / Defensie FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{gap}.md,ready,2026-08-03,,,,,"
    "cmt_saca_eid_rrn_2026|cmt_saca_consular_2026|cmt_fedorest_2026|cmt_dual_saca_eid_consular_tick776,"
    "lb_saca_eid_rrn_76m_2026|lb_saca_consular_47_6m_2026|lb_fedorest_36m_2026|lb_dual_saca_eid_consular_2026,"
    f"{utc},{utc},tick776 Kamer 1281/021 primary; human send only"
)
ft = foi.read_text(encoding="utf-8")
if f"\n{gap}," not in ft:
    with foi.open("a", encoding="utf-8", newline="\n") as f:
        f.write(foi_row + "\n")
    print("foi added")
else:
    print("foi exists")

# --- research_queue ---
rq = base / "research_queue.csv"
rqt = rq.read_text(encoding="utf-8")
old = "rq_767,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: SACA 021 residual dual (non-RGA) or Entity II or FOI-adjacent hole-fill; Royal 001 filled tick775,,2026-08-03T11:00:00Z,,spawned tick775 after rq_766"
new = "rq_767,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Next residual: SACA 021 residual dual (non-RGA) or Entity II or FOI-adjacent hole-fill; Royal 001 filled tick775,,2026-08-03T11:00:00Z,2026-08-03T12:00:00Z,tick776: SACA 021 non-RGA eID/RRN 76.2 consular 47.6 FEDOREST 36 BELNET 22.4 HDA 10.1; spawn rq_768"
if old in rqt:
    rqt = rqt.replace(old, new)
    print("rq_767 marked done")
else:
    print("WARN rq_767 pattern not found")
    # try status-only
    rqt = rqt.replace(
        "rq_767,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
        "rq_767,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    )
rq_768 = "rq_768,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: Entity II dual hole-fill or unmined Kamer 011/012/016 or FOI-adjacent L5; SACA 021 non-RGA filled tick776,,2026-08-03T12:00:00Z,,spawned tick776 after rq_767\n"
if "rq_768," not in rqt:
    rqt = rqt.rstrip("\n") + "\n" + rq_768
    print("rq_768 spawned")
rq.write_text(rqt, encoding="utf-8", newline="\n")

# loop_state
ls = base / "loop_state.csv"
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_767,776,no,"
    "tick776 SACA 021 non-RGA eID/RRN 76.2 consular 47.6 FEDOREST 36 BELNET 22.4; "
    "next rq_768 EntityII/Kamer residual; progress@780 in 4; rq_116 deferred\n",
    encoding="utf-8",
    newline="\n",
)
print("loop_state ok")

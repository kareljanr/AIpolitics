# tick462 CPVS dual write helper — one-shot
from pathlib import Path

root = Path(__file__).resolve().parents[3]  # docs/doge/data/raw -> AIpolitics? 
# Path: .../docs/doge/data/raw/_tick462_write.py -> parents[0]=raw [1]=data [2]=doge [3]=docs [4]=repo
root = Path(__file__).resolve().parents[4]
data = root / "docs" / "doge" / "data"
utc = "2026-08-02T21:45:00Z"

# --- sources ---
src_rows = [
    "src_inami_cpvs_transfer_2025,INAMI news CPVS: 13 centres from 2026; IEFH funds hospitals until 2025 then INAMI takes over; IEFH keeps national coordination,https://www.inami.fgov.be/fr/actualites/hopitaux-recherches-a-partir-de-2026-il-y-aura-13-centres-de-prise-en-charge-des-violences-sexuelles,INAMI/RIZIV,2026-08-02,primary_agency,Strong institutional path: IEFH convention budget by size pre-2026; from 2026 INAMI victim-based AR 21 Sep 2025; law 26 Apr 2024; tick462",
    "src_kamer_56k0854_037_cpvs,Kamer 56K0854/037 minister answer CPVS financing stack 2026,https://www.lachambre.be/FLWB/PDF/56/0854/56K0854037.pdf,Kamer van volksvertegenwoordigers,2026-08-02,official_parliament,Strong: Fonds BB 11.7m + extra 5.8m + IEFH->INAMI 8.9m/yr = 26.4m total planned annual envelope; Justice 0; tick462",
    "src_cpvs_dual_recon_tick462,CPVS dual recon IEFH 2024 cash + NL SARC 2025 + INAMI 2026 stack,https://www.inami.fgov.be/fr/actualites/hopitaux-recherches-a-partir-de-2026-il-y-aura-13-centres-de-prise-en-charge-des-violences-sexuelles,DOGE synthesis primary IEFH RA + NL KB + Kamer + INAMI,2026-08-02,synthesis,Strong dual: IEFH exp CPVS 10.926m 2024; NL SARC 1.616m 2025 plan; 2026 INAMI 26.4m (11.7+5.8+8.9); IEFH transfer announced 8.9 vs 2024 cash 10.9 residual FOI; tick462",
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(src_rows) + "\n")

# --- budgets ---
bud_rows = [
    "bud_cpvs_inami_envelope_2026,riziv,2026,26400000,,,budgeted,src_kamer_56k0854_037_cpvs,strong,CPVS/ZSG total planned annual envelope 26.4m from 2026 (minister Kamer); dual IEFH+NL path; tick462",
    "bud_cpvs_fonds_blouses_blanches_2026,riziv,2026,11700000,,,budgeted,src_kamer_56k0854_037_cpvs,strong,Transfer 11.7m from Fonds Blouses blanches / Zorgpersoneelfonds via CPVS law; tick462",
    "bud_cpvs_extra3_centres_2026,riziv,2026,5800000,,,budgeted,src_kamer_56k0854_037_cpvs,strong,Additional 5.8m exogenous cover for 3 extra CPVS (13 total); tick462",
    "bud_cpvs_iefh_to_inami_transfer_2026,iefh,2026,8900000,,,budgeted,src_kamer_56k0854_037_cpvs,strong,IEFH annual transfer to INAMI 8.9m (dotation currently financing hospital CPVS structures); dual RA 2024 cash 10.926m; tick462",
    "bud_cpvs_stack_dual_2024_26,iefh,2024,10926000,,,outturn,src_cpvs_dual_recon_tick462,strong,Dual anchor IEFH CPVS cash 10.926m 2024 vs 2026 transfer 8.9m announced; NL SARC separate 1.616 2025; tick462",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(bud_rows) + "\n")

# --- entities ---
ent_rows = [
    "cpvs_network,Zorgcentra na Seksueel Geweld (ZSG/CPVS),Centres de prise en charge des violences sexuelles (CPVS),Sexual Violence Care Centres network,programme,riziv,bi,https://cpvs.belgium.be,,,13 CPVS from 2026; IEFH funded hospitals pre-2026 (10.9m cash 2024); INAMI funds from 2026 ~26.4m plan; IEFH national coordination residual; tick462",
    "flagey,Flagey ASBL,Flagey ASBL,Flagey cultural centre Ixelles,agency,sec_federal,bi,https://www.flagey.be,,,NL plan 0.25m provisional 2025 named culture; end-receiver AR TCO residual; tick462",
]
with (data / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(ent_rows) + "\n")

# --- commitments ---
cash = (
    '"{""2026_total_plan"":26400000,""2026_fonds_bb"":11700000,""2026_extra3"":5800000,'
    '""2026_iefh_transfer"":8900000,""2024_iefh_cpvs_cash"":10926000,""2025_nl_sarc_plan"":1616180,'
    '""centres"":13,""justice"":0,""note"":""11.7+5.8+8.9=26.4; IEFH keeps national coordination per INAMI""}"'
)
cmt_row = (
    "cmt_cpvs_inami_envelope_2026,CPVS/ZSG hospital centres financing transfer IEFH to INAMI 2026 stack,riziv,"
    "CPVS network hospitals,Law 26 Apr 2024 CPVS + AR 21 Sep 2025 + gov agreement,2024-04-26,2026,2026,26400000,"
    + cash
    + ",0,active,https://www.inami.fgov.be,Specialist 24/7 care for sexual violence victims in hospital CPVS,"
    "Service delivery core; track double-count after transfer; FOI cash L5 hospitals,src_kamer_56k0854_037_cpvs,"
    "strong,BE>RIZIV>CPVS>hospital_network,"
    "tick462 dual fill public; residual hospital L5 cash FOI class + IEFH residual after 8.9 transfer"
)
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + cmt_row + "\n")

# --- leaderboard ---
lb = data / "leaderboard.csv"
text = lb.read_text(encoding="utf-8")
old_sarc = (
    "lb_nl_sarc_cpvs_1_62m,NL SARC/CPVS centres project 1.616m provisional 2025,federal,ops,"
    "Federal>NL>SARC_CPVS,1616180,1616180,Strong plan; dual IEFH CPVS exp 10.9m 2024 path,strong,"
    "src_nloterij_kb_voorlopig_2025,Sexual violence victims,Specialist referral centres,Core service not waste,"
    "3.0,4.0,4,3.7,Reconcile IEFH CPVS cash,seed,,tick461"
)
new_sarc = (
    "lb_nl_sarc_cpvs_1_62m,NL SARC/CPVS centres project 1.616m provisional 2025,federal,ops,"
    "Federal>NL>SARC_CPVS,1616180,1616180,Strong plan; dual IEFH CPVS 10.9m 2024 + INAMI 26.4m 2026 stack closed tick462,"
    "strong,src_cpvs_dual_recon_tick462,Sexual violence victims,Specialist referral centres,"
    "Core service not waste; lottery line additive to main channel,3.0,4.0,3,3.7,Keep separate from INAMI envelope,seed,,tick462 dual"
)
if old_sarc in text:
    text = text.replace(old_sarc, new_sarc)
else:
    print("WARN: sarc row not found exact")

lines = text.splitlines()
out = []
for line in lines:
    if line.startswith("lb_iefh_cpvs_channel,"):
        out.append(
            "lb_iefh_cpvs_channel,IEFH CPVS sexual violence centres channel ~10.9m 2024,federal,programme,"
            "BE>IEFH>CPVS,10926000,10926000,RA Table5: CPVS 10.926m 2024; dual 2026 INAMI stack 26.4m "
            "(IEFH transfer 8.9m + BB 11.7 + extra 5.8); NL SARC 1.616m 2025,strong,src_cpvs_dual_recon_tick462,"
            "Sexual violence victims via CPVS network,Care centres for sexual violence,"
            "Service delivery; transfer path public; residual cash L5 hospital + post-transfer IEFH residual,"
            "3,6.0,4,4.5,FOI hospital L5 cash + residual IEFH after 8.9 transfer,seed,,tick462 dual"
        )
    else:
        out.append(line)
text = "\n".join(out)
lb_new = [
    "lb_cpvs_inami_26_4m_2026,CPVS/ZSG INAMI annual envelope 26.4m planned from 2026,federal,programme,"
    "BE>RIZIV>CPVS>2026_envelope,26400000,26400000,Strong Kamer minister: 11.7 Fonds BB + 5.8 extra3 + 8.9 IEFH transfer = 26.4; "
    "dual INAMI path + IEFH RA 10.9 2024,strong,src_kamer_56k0854_037_cpvs,"
    "Sexual violence victims 13 judicial arrondissements,Hospital CPVS 24/7 multidisciplinary care,"
    "Core care not waste; scale-up opacity if L5 hospital cash unpublished,3.5,6.5,4,5.0,"
    "Publish hospital L5 cash table annual,seed,,tick462",
    "lb_cpvs_dual_stack_closed,CPVS dual IEFH+NL+INAMI transfer path closed public,federal,ops,"
    "BE>dual>CPVS_IEFH_NL_INAMI,26400000,26400000,Strong public dual: 2024 IEFH 10.9; 2025 NL 1.62; 2026 INAMI 26.4 stack; "
    "FOI residual hospital L5 names/cash,strong,src_cpvs_dual_recon_tick462,Victims + hospitals,"
    "Sexual violence care financing map,Method closes transfer FOI gap partially,3.5,6.5,4,5.0,"
    "FOI hospital L5 + IEFH residual post-transfer,seed,,tick462",
]
if not text.endswith("\n"):
    text += "\n"
text = text.rstrip("\n") + "\n" + "\n".join(lb_new) + "\n"
lb.write_text(text, encoding="utf-8")

# --- research_queue ---
rq = data / "research_queue.csv"
rq_text = rq.read_text(encoding="utf-8")
old_rq = (
    "rq_453,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-08-02T21:15:00Z,,"
    "Spawned tick461 after NL 2025 plan L5; rq_116 SWA deferred"
)
new_rq = (
    "rq_453,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_iefh_funding_detail,"
    "2026-08-02T21:15:00Z,2026-08-02T21:45:00Z,"
    "tick462: CPVS dual IEFH 10.9 + NL SARC 1.62 + INAMI 26.4m stack (11.7+5.8+8.9); FOI residual hospital L5; rq_116 deferred"
)
if old_rq in rq_text:
    rq_text = rq_text.replace(old_rq, new_rq)
else:
    print("WARN rq_453 not found")
    # try status open only
    for line in rq_text.splitlines():
        if line.startswith("rq_453,"):
            print("FOUND:", line[:120])
rq_text = rq_text.rstrip("\n") + "\n"
rq_text += (
    "rq_454,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-08-02T21:45:00Z,,"
    "Spawned tick462 after CPVS dual; rq_116 SWA deferred\n"
)
rq.write_text(rq_text, encoding="utf-8")

# --- foi_queue ---
foi = data / "foi_queue.csv"
foi_text = foi.read_text(encoding="utf-8")
old_gap = (
    "gap_iefh_funding_detail,BE>IEFH>multi_source_funding,iefh,"
    "Cash-by-year 2025-2026 outturn + BGD codes; CPVS transfer to INAMI perimeter; "
    "L5 structural subsidy names 2023-2026; reconcile 33.9m dotation vs 24.8m exp 2024,"
    "2024 RA filled strong; residual multi-year and L5 opaque,6,"
)
new_gap = (
    "gap_iefh_funding_detail,BE>IEFH>multi_source_funding,iefh,"
    "Cash-by-year 2025-2026 outturn + BGD codes; residual IEFH after 8.9m CPVS transfer; "
    "L5 structural subsidy names 2023-2026; hospital CPVS L5 cash; reconcile 33.9m vs 24.8m,"
    "2024 RA + Kamer CPVS transfer stack 26.4m public; residual multi-year L5 hospital cash opaque,6,"
)
if old_gap in foi_text:
    foi_text = foi_text.replace(old_gap, new_gap)
else:
    print("WARN gap_iefh prefix not found")
old_note = "tick143 draft ready human send; 2024 partial map done"
new_note = (
    "tick143 ready human send; tick462 CPVS transfer perimeter partially filled "
    "(Kamer 8.9/11.7/5.8/26.4 + INAMI path); residual hospital L5 + post-transfer IEFH cash"
)
if old_note in foi_text:
    foi_text = foi_text.replace(old_note, new_note)
old_utc = "cmt_iefh_funding_2024,lb_iefh_public_package,2026-07-27T21:10:00Z,2026-07-27T21:10:00Z,"
new_utc = "cmt_iefh_funding_2024,lb_iefh_public_package,2026-07-27T21:10:00Z,2026-08-02T21:45:00Z,"
if old_utc in foi_text:
    foi_text = foi_text.replace(old_utc, new_utc, 1)
foi.write_text(foi_text, encoding="utf-8")

# --- loop_state ---
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_453,462,no,"
    "Scheduler 60s. Next prio5 rq_454; rq_116 SWA deferred. tick462 CPVS dual INAMI 26.4m.\n",
    encoding="utf-8",
)

print("OK", root)

from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 685
utc = "2026-08-01T13:00:00Z"
src = "src_ccrek_vl_delijn_rva_unemp_residual"
src_dual = "src_dual_delijn_rva_tick685"
url_vl = "https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf"
url_fed = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

src_rows = [
    f'{src},CoA VL De Lijn BA path + fed RVA unemp residual dual,{url_vl},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick685: De Lijn IB net rev +50 (+20.1pct tickets+fines) held from toelage; BA rev -25 vs that; werking +39.4 = GIP 33.7 + OV exp 25 - DWV 12.6 - efficiency 5.5; exploitanten +27.1 (design had -11.1 greening step-up Jul2025); PPS 3.5 missing (2025 revisor 23.7); efficiency MOW De Lijn 5.5 of efficiëntere overheid; Terneuzen 21.5 VEK NL 15 missing. RVA unemp BC 4836.4 (+198.5/+4.3pct): volume +287 (full unemp +17473 units; temp unemp -3851); spilindex +8.2; other -96.7; IB 4637.9; FPB unemp rate 9.6 not 9.1; mantelzorg leave reform +0.8/yr from 1Jul half-year 0.4 not in budget; unemp to ZIV 44.1 path"',
    f'{src_dual},Dual De Lijn PT subsidy path vs RVA unemp 4.84bn dual OTW,{url_fed},DOGE synthesis CoA VL+fed dual,2026-08-01,synthesis,"Strong dual: De Lijn werking/rev path vs WAL OTW; RVA 4.84bn dual leefloon spillover tick684; not TE-additive; tick685"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # De Lijn reconstructed path
    f"bud_delijn_ib_net_rev_up_50m_2026,de_lijn,2026,50000000,,,budgeted,{src},strong,IB2026 net transport revenue plan +50.0m (+20.1pct tickets+fare-dodging fines); held from werkingstoelage; tick685",
    f"bud_delijn_ba_net_rev_minus_25m_vs_ib_plan_2026,de_lijn,2026,25000000,,,budgeted,{src},strong,BA2026 revises net rev 25.0m lower than IB +50 plan (gap 75m vs IB revenue assumption); tick685",
    f"bud_delijn_rev_gap_vs_ib_75m_class_2026,de_lijn,2026,75000000,,,estimate,{src},medium,Implied revenue shortfall vs IB assumption 75m class (50 plan +25 cut); feeds toelage; tick685",
    f"bud_delijn_werking_gip_33_7m_2026,de_lijn,2026,33700000,,,budgeted,{src},strong,Werkingstoelage from GIP provisie +33.7m; tick685",
    f"bud_delijn_werking_ov_exp_25m_2026,de_lijn,2026,25000000,,,budgeted,{src},strong,Werkingstoelage from OV expansion policy +25.0m; tick685",
    f"bud_delijn_werking_dwv_delay_minus_12_6m_2026,de_lijn,2026,12600000,,,budgeted,{src},strong,Werkingstoelage -12.6m delay takeover De Werkvennootschap projects; tick685",
    f"bud_delijn_werking_efficiency_minus_5_5m_2026,de_lijn,2026,5500000,,,budgeted,{src},strong,De Lijn efficiency save -5.5m (efficiëntere overheid MOW rechtspersonen); CoA p23+50; tick685",
    f"bud_delijn_werking_net_plus_39_4m_2026,de_lijn,2026,39400000,,,budgeted,{src},strong,Net werkingstoelage path +39.4m (33.7+25-12.6-5.5≈40.6; CoA states 39.4 residual other -1.2 class); tick685",
    f"bud_delijn_exploit_design_minus_11_1m_2026,de_lijn,2026,11100000,,,budgeted,{src},strong,Design budget had exploitanten -11.1m insufficient for greening; tick685",
    f"bud_delijn_exploit_green_plus_27_1m_2026,de_lijn,2026,27100000,,,budgeted,{src},strong,Exploitanten greening step-up +27.1m (new contracts Jul2025 higher fleet standards); tick685",
    f"bud_delijn_exploit_swing_38_2m_class_2026,de_lijn,2026,38200000,,,estimate,{src},medium,Exploitanten path swing +38.2m class from design -11.1 to +27.1; tick685",
    f"bud_delijn_pps_2025_correction_23_7m,de_lijn,2025,23700000,,,outturn,{src},strong,2025 PPS delivery credit gap 23.7m; auditor reservation + VL consol correction; tick685",
    f"bud_delijn_pps_2026_missing_3_5m,de_lijn,2026,3500000,,,budgeted,{src},strong,2026 PPS deliveries 3.5m without BA credits added; tick685",
    f"bud_mow_efficiency_delijn_5_5m_2026,de_lijn,2026,5500000,,,budgeted,{src},strong,MOW efficiëntere overheid impact De Lijn 5.5m (DVW 2.5); not detailed in algemene toelichting; tick685",
    f"bud_mow_efficiency_dvw_2_5m_2026,vlaamse_waterweg,2026,2500000,,,budgeted,{src},strong,MOW efficiëntere overheid impact DVW 2.5m; tick685",
    f"bud_terneuzen_vek_21_5m_deep_2026,vlaamse_waterweg,2026,21500000,,,budgeted,{src},strong,Terneuzen VEK 21.5m BA kasplan Mar2026; ruiter eoy2025 76.2 covers VAK; tick685",
    f"bud_terneuzen_nl_15m_missing_deep_2026,vlaamse_waterweg,2026,15000000,,,budgeted,{src},strong,NL final settlement 15.0m in kasplan+GIP missing from BA VEK; tick685",
    # RVA unemp residual
    f"bud_rva_uitkeringen_bc_4836_4m_2026,rva,2026,4836400000,,,budgeted,{src},strong,RVA benefits Globaal Beheer BC 4836.4m (+198.5 / +4.3pct vs IB 4637.9); tick685",
    f"bud_rva_uitkeringen_ib_4637_9m_2026,rva,2026,4637900000,,,budgeted,{src},strong,RVA benefits IB2026 4637.9m; tick685",
    f"bud_rva_volume_up_287m_2026,rva,2026,287000000,,,budgeted,{src},strong,Volume effect +287.0m (full unemp +17473 units; temp unemp -3851); tick685",
    f"bud_rva_full_unemp_units_up_17473_2026,rva,2026,17473,,,budgeted,{src},strong,Fully unemployed benefit recipients +17473 units path (FPB -98k not -116k y/y swing); tick685",
    f"bud_rva_temp_unemp_units_minus_3851_2026,rva,2026,3851,,,budgeted,{src},strong,Temporary unemployment beneficiaries -3851 units; tick685",
    f"bud_rva_spilindex_up_8_2m_2026,rva,2026,8200000,,,budgeted,{src},strong,Spilindex Dec2025 path +8.2m; Jun2026 next index not re-estimated by RVA; tick685",
    f"bud_rva_other_minus_96_7m_2026,rva,2026,96700000,,,budgeted,{src},strong,Other impact -96.7m (avg daily benefit, arrears, days paid, category shifts); tick685",
    f"bud_fpb_unemp_rate_bc_9_6pct_2026,gg_belgium,2026,96,,,budgeted,{src},strong,FPB Feb2026 unemployment rate 9.6pct (IB 9.1); storage 96=9.6pct; tick685",
    f"bud_rva_mantelzorg_cost_0_8m_yr,rva,2026,800000,,,budgeted,{src},strong,Mantelzorg thematic leave reform RVA est +0.8m/yr from 1 Jul2026; not in budget; half-year 0.4 for 2026; tick685",
    f"bud_rva_mantelzorg_2026_half_0_4m,rva,2026,400000,,,estimate,{src},medium,Half-year 2026 mantelzorg cost ~0.4m if 1 Jul start; unbudgeted; tick685",
    f"bud_riziv_unemp_inflow_ziv_44_1m_2026,riziv,2026,44100000,,,budgeted,{src},strong,RIZIV: 5000/yr unemp-loss inflow to ZIV +44.1m 2026 path 94.9/99.2/97.5; RVA monitoring mild Jan26; tick685",
    f"bud_riziv_unemp_inflow_ziv_2027_94_9m,riziv,2027,94900000,,,budgeted,{src},strong,Unemp to ZIV path 94.9m 2027; tick685",
    f"bud_riziv_unemp_inflow_ziv_2028_99_2m,riziv,2028,99200000,,,budgeted,{src},strong,Unemp to ZIV path 99.2m 2028; tick685",
    f"bud_riziv_unemp_inflow_ziv_2029_97_5m,riziv,2029,97500000,,,budgeted,{src},strong,Unemp to ZIV path 97.5m 2029; tick685",
    # Dual
    f"bud_dual_delijn_werking_39_4m_2026,gg_belgium,2026,39400000,,,budgeted,{src_dual},strong,Dual De Lijn werking +39.4m path vs WAL OTW; tick685",
    f"bud_dual_rva_unemp_4_84bn_2026,gg_belgium,2026,4836400000,,,budgeted,{src_dual},strong,Dual RVA unemp 4.84bn vs leefloon spillover; not TE-additive; tick685",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

cmt_rows = [
    f'cmt_delijn_rev_toelage_path_2026,De Lijn rev shortfall feeds toelage +39.4,de_lijn,VL passengers,CoA 2026_28 7.5,2026-06-01,2026,2026,39400000,"{{""rev_cut"":25000000,""werking"":39400000}}",,active,,PT dual OTW,Tariff FOI,{src},strong,VL>DeLijn>path,tick685',
    f'cmt_delijn_exploit_green_27m,De Lijn exploitanten greening +27.1m,de_lijn,Private operators,Contracts Jul2025,2025-07-01,2026,2026,27100000,"{{""2026"":27100000}}",,active,,Greening dual,Contract L5 FOI,{src},strong,VL>DeLijn>exploit,tick685',
    f'cmt_delijn_pps_credit_gap,De Lijn PPS credit gap 23.7+3.5,de_lijn,PPS contractors,CoA 2026_28,2026-06-01,2025,2026,27200000,"{{""2025"":23700000,""2026"":3500000}}",,active,,Accounting dual,Add credits FOI,{src},strong,VL>DeLijn>PPS,tick685',
    f'cmt_rva_unemp_4836m_volume,RVA unemp 4.84bn volume +287,rva,Unemployed,CoA 2026_22 5.1,2026-05-21,2026,2026,4836400000,"{{""volume"":287000000,""units_full"":17473}}",,active,,Unemp dual,Unit cost FOI,{src},strong,Fed>RVA>unemp,tick685',
    f'cmt_mantelzorg_unbudgeted_0_8m,Mantelzorg leave +0.8m/yr unbudgeted,rva,Carers,Law + MR KB Apr2026,2026-04-24,2026,2029,800000,"{{""yr"":800000}}",,active,,Care dual,Budget FOI,{src},strong,Fed>RVA>mantelzorg,tick685',
    f'cmt_dual_delijn_rva_tick685,Dual De Lijn PT vs RVA unemp/leefloon,gg_belgium,VL+fed dual,CoA dual,2026-06-01,2026,2026,4836400000,"{{""rva"":4836400000}}",,active,,Dual residual,Not TE-additive,{src_dual},strong,Belgium>dual>delijn_rva,tick685',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_delijn_rev_toelage_wedge_2026,De Lijn rev cut feeds +39.4m toelage,Flanders,ops,VL>DeLijn>path,39400000,0,Strong CoA: IB +50 rev held from toelage then BA -25 rev +39.4 toelage; dual OTW,strong,{src},passengers,PT subsidy dual,Primary,7.0,5.0,2,6.10,Tariff+cost FOI,open,,tick685",
    f"lb_delijn_exploit_green_27m_2026,De Lijn exploit greening +27.1m,Flanders,ops,VL>DeLijn>exploit,27100000,0,Strong CoA: design -11.1 ignored Jul2025 greening contracts,strong,{src},private operators,Greening dual,Primary,6.5,4.5,2,5.55,Contract L5 FOI,open,,tick685",
    f"lb_delijn_pps_gap_recurring_2026,De Lijn PPS credit gap recurring,Flanders,ops,VL>DeLijn>PPS,3500000,0,Strong CoA: 2025 23.7 revisor + 2026 3.5 still missing credits,strong,{src},PPS,Accounting dual,Primary absurd,8.0,3.5,2,5.95,Fix credits FOI,open,,tick685",
    f"lb_rva_unemp_volume_287m_2026,RVA unemp volume +287m to 4.84bn,Federal,ops,Fed>RVA>volume,287000000,0,Strong CoA: +17473 full unemp units FPB rate 9.6; dual leefloon,strong,{src},unemployed,Volume dual,Primary,6.5,6.5,3,6.25,Unit cost FOI,open,,tick685",
    f"lb_mantelzorg_unbudgeted_2026,Mantelzorg leave unbudgeted 0.8m/yr,Federal,ops,Fed>RVA>mantelzorg,800000,0,Strong CoA: reform 1Jul2026 +0.8m/yr not in BA; half-year 0.4,strong,{src},carers,Care dual,Primary,7.0,2.0,1,4.85,Budget FOI,open,,tick685",
    f"lb_dual_delijn_rva_2026,Dual De Lijn path vs RVA 4.84bn,Belgium,ops,Belgium>dual>delijn_rva,4836400000,0,Strong dual: VL PT toelage wedge + fed unemp volume; not TE-additive,strong,{src_dual},all entities,PT+unemp dual residual,Primary dual,6.0,8.5,3,6.85,Cross FOI,open,,tick685",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

gap_id = "gap_vl_delijn_rva_unemp_l5"
foi_row = (
    f"{gap_id},Vlaanderen+Federal>DeLijn_RVA_L5,de_lijn,"
    "De Lijn absolute werkingstoelage/net rev 2025-26 series; ticket+fine split behind IB +50; exploitanten greening contract L5 cost; PPS project list 3.5 2026; efficiency 5.5 line items; RVA volume +17473 methodology; mantelzorg 0.8 budget insertion; unemp-to-ZIV monthly,"
    "CoA De Lijn+RVA residual strong tick685; dual OTW/leefloon,"
    "5,De Lijn / Departement MOW / RVA / RIZIV,"
    "openbaarheid@vlaanderen.be,https://www.delijn.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_delijn_rev_toelage_path_2026|cmt_rva_unemp_4836m_volume|cmt_delijn_pps_credit_gap,"
    "lb_delijn_rev_toelage_wedge_2026|lb_rva_unemp_volume_287m_2026|lb_delijn_pps_gap_recurring_2026,"
    f"{utc},{utc},tick685 CoA VL+fed dual primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_676,"):
        out.append(
            "rq_676,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,pod_mi,"
            "Next residual: VL De Lijn deepen CoA 2026_28 or SS other receipts L5 or fed justice residual dual.,,"
            f"2026-08-01T12:45:00Z,{utc},"
            "tick685 De Lijn rev/toelage wedge + RVA 4.84bn volume dual; FOI gap_vl_delijn_rva_unemp_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_677,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,de_lijn,"
    "Next residual: fed justice residual dual CoA or SS other receipts L5 or VL efficiëntere overheid pack deepen.,,"
    f"{utc},,spawned tick685 after rq_676"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_676,685,no,"
    "tick685 De Lijn rev/toelage wedge RVA 4.84bn volume dual; next rq_677; progress@690 in 5; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof VL BA2026 (2026_28) §7.5 De Lijn; CoA fed 2026_22 §5 RVA

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: De Lijn / Departement MOW / RVA
Cc: RIZIV
openbaarheid@vlaanderen.be

Betreft: Openbaarheid — De Lijn BA2026 pad (werking +39,4 mEUR) + RVA
werkloosheid 4.836 mEUR L5

Geachte,

Op grond van de toepasselijke openbaarheidsregels verzoek ik om:

### De Lijn
1. Absolute **werkingstoelage** en **netto-vervoersopbrengsten** 2025–2026
   (IB vs BA), met splitsing tickets vs boetes achter IB **+50 mEUR**.
2. Detail **exploitanten +27,1 mEUR** (vergroening contracten juli 2025)
   per operator/contract.
3. **PPS-opleveringen** 2025 (**23,7 mEUR** correctie) en 2026 (**3,5 mEUR**
   zonder krediet): projectlijst en begrotingsartikelen.
4. **Efficiëntiebesparing 5,5 mEUR**: basisallocaties.

### RVA
5. Volume **+287 mEUR** / **+17.473** volledig werklozen: methodenota FPB
   9,6 % vs 9,1 %.
6. **Mantelzorgverlof** raming **0,8 mEUR/j** en opname in begroting.
7. Maandreeks instroom werkloosheid → ZIV (**44,1 mEUR** 2026-pad).

Publieke steun: Rekenhof 2026_28 §7.5; 2026_22 §5 Werk en werkloosheid.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Dual: OTW/leefloon spillover (tick684).
- Tick 685.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_676** (FOI-adjacent dual residual — **VL De Lijn path + RVA unemp volume dual**)
- Found (primary CoA 2026_28 §7.5 + 2026_22 §5):
  - **De Lijn:** IB net rev **+50** (+20.1% tickets+fines) held from toelage; BA rev **−25** vs plan; werking **+39.4** (GIP **33.7** + OV **25** − DWV **12.6** − efficiency **5.5**); exploitanten **+27.1** (design had **−11.1**); PPS **3.5** missing (2025 **23.7**); Terneuzen **21.5** / NL **15** missing
  - **RVA unemp BC EUR4.836bn** (+198.5): volume **+287** (full **+17.473** units; temp **−3.851**); spilindex **+8.2**; other **−96.7**; FPB rate **9.6%** not 9.1; mantelzorg **+0.8**/yr unbudgeted; unemp→ZIV **44.1** path
  - Dual OTW/leefloon. Strong CoA; L5 FOI.
- Wrote: budgets (+33); commitments (+6); leaderboard (+6); sources (+2); FOI draft **gap_vl_delijn_rva_unemp_l5**; rq_676=done; spawn **rq_677**; loop_state ticks=685
- FOI opened: gap_vl_delijn_rva_unemp_l5 — ready (not sent)
- Next: rq_677; progress@690 in 5 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick685")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows))

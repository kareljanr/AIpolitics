# tick511 — CoA 2026_22 residual energy L5 deep + federal debt path dual
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fed_aju_energy_debt_2026,CoA fed budget aju 2026 energy L5 + debt path residual 2026_22,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Rekenhof AG 21 May 2026,2026-07-29,court_of_audit,"
        "Strong residual tick511: energy 2.6bn L5 (DG 1.2 + funds 1.4); CfD 583.6; energienorm 249; "
        "fed debt 577.5bn 2026->731 2031 interest 12.3->22.6; dual prior energy/debt; tick511\n"
    )
    f.write(
        "src_dual_energy_debt_tick511,Dual federal energy assignment stack + debt interest path,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "DOGE synthesis CoA 2026_22 residual energy+debt,2026-07-29,synthesis,"
        "Strong dual: energy opacity 2.6bn via assignment funds vs debt interest 12.3bn rising to 22.6; tick511\n"
    )

buds = [
    # Energy L5 residual
    "bud_fed_energy_total_2_6bn_2026,sec_federal,2026,2600000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal energy policy total class ~2.6bn CoA (DG Energie 1.2 + assignment funds 1.4); tick511",
    "bud_dg_energie_1_2bn_2026,sec_federal,2026,1200000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,DG Energie FOD Economie credits ~1.2bn of energy stack; tick511",
    "bud_energy_assign_funds_1_4bn_2026,sec_federal,2026,1400000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Fiscal assignment funds to CREG Elia NIRAS Hedera ~1.4bn; opacity CoA; tick511",
    "bud_energienorm_249m_2026,sec_federal,2026,249000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Energienorm law 24 Apr 2026 industry power support credits 249m (maintains IB); tick511",
    "bud_fluxys_contrib_100m_2026,sec_federal,2026,100000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Fluxys exceptional contribution 100m/yr 2026-28 financing energienorm; tick511",
    "bud_creg_social_tariff_168m_2026,sec_federal,2026,168600000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,CREG fiscal transfer share for social tariff protected clients 168.6m; tick511",
    "bud_energy_temp_support_20m_2026,sec_federal,2026,20000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Temp energy support MR 22 Apr 2026 max 20m (CREG 7.5 stookolie 7.5 travel provis 5); tick511",
    "bud_phoenix_cfd_583m_2026,sec_federal,2026,583600000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Phoenix CfD Doel4/Tihange3 583.6m 2026 budgeted; strike price negotiation status unknown to CoA; tick511",
    "bud_niras_passiva_assign_259m_2026,sec_federal,2026,258600000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Assignment CREG->NIRAS nuclear passiva Belgoprocess+SCK 258.6m; tick511",
    "bud_niras_btw_passiva_62m_2026,sec_federal,2026,62500000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,NIRAS assignment funds VAT on passiva works 62.5m; tick511",
    "bud_nuclear_decom_contrib_100m_2026,sec_federal,2026,100000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,medium,Energy sector decommissioning contribution est 100m 2026; method unexplained; ends 2027 via Phoenix; tick511",
    # Centenindex residual
    "bud_centenindex_e1_yield_24m_2026,sec_federal,2026,24000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Two-cent indexation Entity I net yield 24m 2026 path to 363m 2029 (FPB Apr); tick511",
    "bud_centenindex_e1_yield_363m_2029,sec_federal,2029,363000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Two-cent indexation Entity I net yield 363m 2029; tick511",
    # Federal debt + interest path
    "bud_fed_debt_stock_577_5bn_2026,sec_federal,2026,577500000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal state debt stock BC2026 577.5bn eoy (+5.6 vs IB; +31.4 vs 2025 550.6); tick511",
    "bud_fed_debt_stock_731bn_2031,sec_federal,2031,731000000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal debt path 731.0bn 2031 CoA/Debt Agency; tick511",
    "bud_fed_interest_12_3bn_bc_2026,sec_federal,2026,12300000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal interest charges BC2026 12.3bn (IB 12.2; 2025 10.8); tick511",
    "bud_fed_interest_22_6bn_2031,sec_federal,2031,22600000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal interest path 22.6bn 2031 (implied rate 2.0->3.1pct); tick511",
    "bud_fed_debt_pct_gdp_86_9_2026,sec_federal,2026,869,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal debt 86.9pct GDP BC2026 (85.6 2025 path 94.5 2031); ratio stored as 0.1pct points? USE pct*10 no - store as notes only; amount_eur=869000000 placeholder wrong",
]
# Fix debt pct - don't invent placeholder euros for ratios; drop that bad row and use notes-only via commitments
buds = [b for b in buds if "bud_fed_debt_pct_gdp" not in b]
buds += [
    "bud_fed_cash_receipts_167_2bn_2026,sec_federal,2026,167159000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal cash receipts total BC 167.159bn (+2.725 vs IB); tick511",
    "bud_fed_fiscal_cash_159_3bn_2026,sec_federal,2026,159310000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal fiscal cash receipts BC 159.310bn (+1.367); tick511",
    "bud_fed_nonfiscal_cash_7_8bn_2026,sec_federal,2026,7849000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal non-fiscal cash receipts BC 7.849bn (+1.358); tick511",
    "bud_fed_transfers_out_94_5bn_2026,sec_federal,2026,94515000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Federal transfers to EU/regions/SS/other BC 94.515bn (56.5pct receipts); tick511",
    "bud_fed_middelen_72_6bn_2026,sec_federal,2026,72644000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Middelenbegroting after transfers BC 72.644bn; tick511",
    "bud_fed_fiscal_esr_164_5bn_2026,sec_federal,2026,164541200000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Fiscal receipts ESR after conclave 164.541bn; tick511",
    "bud_fiscal_measures_net_1_83bn_2026,sec_federal,2026,1830800000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Net fiscal measures impact +1830.8m 2026 (prior +1099.9 + conclave +730.9); tick511",
    "bud_pillar2_slip_87m_2026,sec_federal,2026,-87000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,Pillar2 minimum tax BC -87m (was +32 IB; slip -119); tick511",
    "bud_vat_reform_impact_177m_2026,sec_federal,2026,177000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,VAT reform impact BC 177m (was 580.5; slip -403.5); tick511",
    "bud_russian_assets_venb_1016m_2026,sec_federal,2026,1016000000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,strong,VenB prepayments include 1016m frozen Russian assets related; tick511",
    "bud_vvpr_exceptional_402m_2026,sec_federal,2026,402100000,,,budgeted,src_ccrek_fed_aju_energy_debt_2026,medium,RV exceptional VVPR-bis distributions 402.1m at 15pct due delayed progwet; tick511",
    "bud_dual_energy_debt_2026,gg_belgium,2026,2600000000,,,derived,src_dual_energy_debt_tick511,strong,Dual energy 2.6bn stack vs debt interest 12.3bn; tick511",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_fed_energy_l5_deep_2026,Federal energy policy 2.6bn L5 assignment funds + Phoenix CfD,"
        "sec_federal,Industry protected clients Engie,"
        "CoA 2026_22 §energy + law 24 Apr 2026,"
        "2026-04-24,2026,2028,2600000000,"
        '"{""total_m"":2600,""dg_energie_m"":1200,""assign_funds_m"":1400,'
        '""energienorm_m"":249,""fluxys_m"":100,""social_tariff_m"":168.6,'
        '""temp_support_m"":20,""cfd_m"":583.6,""niras_passiva_m"":258.6,'
        '""niras_vat_m"":62.5,""decom_contrib_m"":100,'
        '""note"":""Strong CoA; strike price unknown; assignment fund opacity""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Transparent energy financing,Publish fund L5 + CfD strike FOI,"
        "src_ccrek_fed_aju_energy_debt_2026,strong,Federal>Energy>L5_2026,tick511"
    ),
    (
        "cmt_fed_debt_path_577_731,Federal state debt stock path 577.5bn 2026 to 731bn 2031,"
        "sec_federal,Bondholders taxpayers,"
        "CoA 2026_22 Debt Agency tables,"
        "2026-05-21,2025,2031,577500000000,"
        '"{""stock_2025_bn"":550.6,""stock_bc2026_bn"":577.5,""stock_2031_bn"":731.0,'
        '""interest_2025_bn"":10.8,""interest_bc2026_bn"":12.3,""interest_2031_bn"":22.6,'
        '""implied_rate_2025_pct"":2.0,""implied_rate_2031_pct"":3.1,'
        '""snowball_r_g_2026_pct"":-0.91,""snowball_r_g_2031_pct"":-0.06,'
        '""note"":""Strong CoA/Debt Agency; primary still negative ~2.2pct GDP""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Debt sustainability path,Primary surplus path + dual E1/E2,"
        "src_ccrek_fed_aju_energy_debt_2026,strong,Federal>Debt>path_2026_31,tick511"
    ),
    (
        "cmt_fed_receipts_fiscal_2026,Federal cash and ESR fiscal receipts BC2026 + measures,"
        "sec_federal,Taxpayers,"
        "CoA 2026_22 Deel II Ch I,"
        "2026-04-03,2026,2026,167159000000,"
        '"{""cash_total_m"":167159,""fiscal_cash_m"":159310,""nonfiscal_m"":7849,'
        '""transfers_out_m"":94515,""middelen_m"":72644,""fiscal_esr_m"":164541.2,'
        '""measures_net_m"":1830.8,""pillar2_m"":-87,""vat_reform_m"":177,'
        '""russian_venb_m"":1016,""vvpr_m"":402.1,'
        '""note"":""Strong CoA; municipal opcentiemen excluded""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Federal revenue base,Track Pillar2/VAT/PB reform slips,"
        "src_ccrek_fed_aju_energy_debt_2026,strong,Federal>Receipts>BC2026,tick511"
    ),
    (
        "cmt_dual_energy_debt_aju,Dual energy assignment opacity + debt interest path,"
        "gg_belgium,Energy users taxpayers,"
        "CoA 2026_22 residual dual,"
        "2026-05-21,2026,2031,2600000000,"
        '"{""energy_m"":2600,""interest_2026_bn"":12.3,""interest_2031_bn"":22.6,'
        '""debt_2026_bn"":577.5,'
        '""note"":""not additive pure TE; dual financing pressure""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Map dual fiscal pressure energy+debt,FOI CfD+funds L5,"
        "src_dual_energy_debt_tick511,strong,BE>dual>energy_debt,tick511"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_fed_energy_2_6bn_l5,Federal energy policy stack ~2.6bn 2026 L5,federal,ops,Federal>Energy>policy_stack_2026,2600000000,2600000000,Strong CoA: DG 1.2bn + assignment funds 1.4bn opaque; dual prior,strong,src_ccrek_fed_aju_energy_debt_2026,Industry households,Energy policy financing,Assignment fund opacity,6.5,9.0,6,7.05,Publish fund L5 FOI,seed,,tick511",
    "lb_phoenix_cfd_584m,Phoenix nuclear CfD 583.6m 2026,federal,ops,Federal>Energy>Phoenix_CfD,583600000,583600000,Strong CoA: budgeted 583.6m; strike price unknown at report close; dual Hedera 15bn,strong,src_ccrek_fed_aju_energy_debt_2026,Engie Be-NUC,LTO CfD risk sharing,Contingent fiscal risk,7.0,7.5,6,6.95,Publish strike FOI,seed,,tick511",
    "lb_energienorm_249m,Energienorm industry power support 249m,federal,subsidy,Federal>Energy>energienorm,249000000,249000000,Strong CoA: law 24 Apr 2026; Fluxys 100m/yr cofinance 2026-28,strong,src_ccrek_fed_aju_energy_debt_2026,Energy-intensive firms,Competitiveness power price,Large firm energy subsidy,5.5,7.5,5,6.35,Evaluate targeting FOI,seed,,tick511",
    "lb_creg_social_tariff_169m,CREG social tariff protected clients 168.6m,federal,ops,Federal>Energy>social_tariff,168600000,168600000,Strong CoA: assignment fund share social tariff,strong,src_ccrek_fed_aju_energy_debt_2026,Protected energy clients,Energy poverty support,Social tariff channel,3.0,7.0,4,5.15,Keep transparent,seed,,tick511",
    "lb_fed_debt_577_5bn_2026,Federal state debt stock 577.5bn eoy2026,federal,ops,Federal>Debt>stock_2026,0,577500000000,Strong CoA/Debt Agency: 577.5bn (+31.4 vs 2025); path 731bn 2031; annual=0 stock,strong,src_ccrek_fed_aju_energy_debt_2026,Bondholders,Sovereign financing,Debt stock not annual waste,4.0,9.5,7,6.35,Primary surplus path,seed,,tick511",
    "lb_fed_interest_12_3bn_2026,Federal interest charges 12.3bn BC2026,federal,ops,Federal>Debt>interest_2026,12300000000,22600000000,Strong CoA: 12.3bn 2026 path 22.6bn 2031; dual energy stack,strong,src_ccrek_fed_aju_energy_debt_2026,Taxpayers bondholders,Debt service,Snowball pressure rising,5.0,9.5,6,7.15,Cut primary deficit,seed,,tick511",
    "lb_fed_cash_receipts_167bn,Federal cash receipts 167.2bn BC2026,federal,ops,Federal>Receipts>cash_2026,167159000000,167159000000,Strong CoA: 167.2bn cash; fiscal 159.3 nonfiscal 7.8; transfers out 94.5,strong,src_ccrek_fed_aju_energy_debt_2026,Taxpayers,Federal revenue base,Core financing,2.0,9.5,6,6.3,Track measure slips,seed,,tick511",
    "lb_dual_energy_debt,Dual energy 2.6bn + debt interest 12.3bn,multi,ops,BE>dual>energy_debt,2600000000,12300000000,Strong dual CoA residual financing pressure,strong,src_dual_energy_debt_tick511,Taxpayers energy users,Dual fiscal pressure map,Scale dual,5.5,9.0,5,6.95,Honest fund+debt FOI,seed,,tick511",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_phoenix_cfd_strike_l5,Federal>Energy>Phoenix_CfD_strike_L5,sec_federal,"
    "Strike price (uitoefenprijs) status and cash scenarios 2026-2035 for Phoenix CfD Doel4/Tihange3; "
    "Fluxys 100m exceptional contribution legal basis and actual cash 2026; decommissioning contribution "
    "100m calculation method; L5 split assignment funds CREG/Elia/NIRAS/Hedera cash-by-year 2024-26,"
    "CoA 2026_22: CfD 583.6m booked without strike transparency; assignment fund opacity dual prior FOI,8,"
    "FOD Economie DG Energie / Be-NUC / Engie liaison / CREG,info@economie.fgov.be,"
    ",docs/doge/foi/drafts/gap_phoenix_cfd_strike_l5.md,"
    "ready,2026-07-29,,,,,cmt_fed_energy_l5_deep_2026,"
    "lb_phoenix_cfd_584m|lb_fed_energy_2_6bn_l5,"
    "2026-07-29T00:20:00Z,2026-07-29T00:20:00Z,"
    "tick511: CoA 2026_22 residual energy L5 + debt; FOI CfD strike human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_502,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T00:05:00Z,,Spawned tick510 after progress@510; rq_116 deferred"
)
new = (
    "rq_502,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_phoenix_cfd_strike_l5,"
    "2026-07-29T00:05:00Z,2026-07-29T00:20:00Z,"
    "tick511: CoA 2026_22 residual energy L5 2.6bn CfD 584m + debt 577.5bn dual; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_502 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_503,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T00:20:00Z,,Spawned tick511 after CoA energy/debt residual; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T00:20:00Z,rq_502,511,no,"
    "Tick511 CoA energy L5 2.6bn CfD 584m debt 577.5bn dual; next prio5 rq_503; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick511 OK")

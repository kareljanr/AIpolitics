# tick512 — CoA 2026_22 residual new fiscal measures + nonfiscal + primary exp cells dual
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fed_aju_fiscal_nonfisc_2026,CoA fed budget aju 2026 new fiscal measures + nonfiscal residual 2026_22,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Rekenhof AG 21 May 2026,2026-07-29,court_of_audit,"
        "Strong residual tick512: conclave fiscal +730.9m; customs e-comm 400.7+handling 77.4; VVPR +334.5; "
        "nonfiscal 7.829bn (+CREG 285 RSZ 548); primary exp cells 92.05bn; dual prior receipts; tick512\n"
    )
    f.write(
        "src_dual_fiscal_nonfisc_tick512,Dual new fiscal measures pack + nonfiscal one-offs dual debt path,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "DOGE synthesis CoA 2026_22 residual fiscal/nonfiscal,2026-07-29,synthesis,"
        "Strong dual: conclave +0.73bn fiscal + nonfiscal refunds vs interest 12.3bn path; tick512\n"
    )

buds = [
    # New fiscal measures conclave
    "bud_fiscal_conclave_new_731m_2026,sec_federal,2026,730900000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,New fiscal measures conclave Apr 2026 positive impact +730.9m; tick512",
    "bud_customs_ecommerce_impact_401m_2026,sec_federal,2026,400700000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,Customs reform e-commerce packages <=150eur from 1 Jul 2026 impact class +400.7m; CoA data not inspected; tick512",
    "bud_eu_handling_fee_77m_2026,sec_federal,2026,77400000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,EU handling fee est ~2eur from 1 Nov 2026 yield 77.4m as unallocated correction; law not final; tick512",
    "bud_customs_retention_112m_2026,sec_federal,2026,112300000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,MS keep 25pct collection fee on customs +112.3m nonfiscal (from +449 customs gross dual EU transfer -449); tick512",
    "bud_customs_vat_volume_loss_48m_2026,sec_federal,2026,-48000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,Expected VAT volume loss -48m from consumer price rise e-comm customs; tick512",
    "bud_vvpr_bis_reest_335m_2026,sec_federal,2026,334500000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,VVPR-bis re-estimate +334.5m conclave (behavior anticipation delayed progwet; Jan-Apr +406.3 vs 2025); future years risk; tick512",
    "bud_insurance_tax_36m_2026,sec_federal,2026,36400000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Insurance tax 9.6pct vs 9.25 yield +36.4m BC (was 51 IB; 1 Apr start; further delay risk); tick512",
    "bud_nonres_opcentiemen_78m_risk,sec_federal,2026,78000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,Non-resident 7pct opcentiemen ~78m/yr; CJEU C-119/24 illegal; refunds open from 2022 assessments; no solution; tick512",
    "bud_employer_km_credit_60m_class_2026,sec_federal,2026,60000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,Employer km commute tax credit May-Jul 20m/month class 60m; FPS no data; claimed VAT-neutral disputed; tick512",
    "bud_service_km_provis_5m_2026,sec_federal,2026,5000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,Service travel forfait km raise Q2 2026 provision 5m (1.7m/month); FPS no data; tick512",
    "bud_pillar2_slip_2027_184m,sec_federal,2027,-184000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Pillar2 re-estimate slip -184m 2027 (plus -119 2026); OECD SbS package; tick512",
    # Non-fiscal
    "bud_nonfiscal_total_7829m_2026,sec_federal,2026,7829000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Non-fiscal middelenbegroting 7829m BC (+1358 vs IB); note cash table 7849 slight perimeter; tick512",
    "bud_nonfiscal_b9_6886m_2026,sec_federal,2026,6886000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Non-fiscal with Entity I B9 impact 6886m (+1036 vs IB); tick512",
    "bud_rsz_eq_refund_548m_2026,sec_federal,2026,548000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,RSZ equilibrium overfinance refund +548m nonfiscal sect 24; tick512",
    "bud_riziv_covid_refund_187m_2026,sec_federal,2026,187000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,RIZIV COVID-19 subsidy refund +187m nonfiscal sect 24; tick512",
    "bud_creg_energy_refund_285m_2026,sec_federal,2026,285000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,CREG energy crisis premium refund +285m sect 32 (could reach 412 if suppliers repay); no B9 impact; tick512",
    "bud_customs_collection_fee_1014m_2026,sec_federal,2026,1013800000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Customs collection fee retention 25pct 1013.8m (+229.3 vs IB); tick512",
    "bud_plates_concession_delay_42m_2026,sec_federal,2026,-42200000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Number plate production contract delay to 2027 cancels -42.2m receipt; old concession +4.3m rebooked; tick512",
    "bud_sfpim_dividend_actual_78m_2026,sec_federal,2026,78400000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,SFPIM dividend actual 78.4m; budget books only 55.8 (under by 22.6); tick512",
    # Primary expenditure cells
    "bud_fed_primary_exp_cells_92050m_2026,sec_federal,2026,92050000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Primary settlement credits cells total BC 92050m (+41 vs IB 92009); tick512",
    "bud_fed_cell_support_3722m_2026,sec_federal,2026,3722000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Support cell credits 3722m (-497; index provis -485.2 ID provis -207.4 + security 178.8 + new policy 40.6); tick512",
    "bud_fed_cell_authority_23049m_2026,sec_federal,2026,23049000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Authority cell 23049m (+390; Def +188.2 Interior +100 Justice +81); tick512",
    "bud_fed_cell_economic_6580m_2026,sec_federal,2026,6580000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Economic cell 6580m (-34; Phoenix -50 energy +15 Mobility -12 BELSPO +8.6); tick512",
    "bud_fed_cell_social_34611m_2026,sec_federal,2026,34611000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Social cell 34611m (+82; POD MI +60 FOD Health +29.3); tick512",
    "bud_fed_cell_specific_24087m_2026,sec_federal,2026,24087000000,,,budgeted,src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Specific budget sections 24087m (+100; 6th reform dots +61.5 debt ops +44 EU -59.4); tick512",
    "bud_fuel_price_btw_extra_42m_class_2026,sec_federal,2026,41900000,,,derived,src_ccrek_fed_aju_fiscal_nonfisc_2026,medium,FPS est fuel VAT extra 41.9m 1 Mar-15 Apr at constant volume; -6m if consumption -5pct; dual km credit neutrality claim; tick512",
    "bud_dual_fiscal_nonfisc_2026,gg_belgium,2026,730900000,,,derived,src_dual_fiscal_nonfisc_tick512,strong,Dual conclave fiscal pack + nonfiscal refunds stack; tick512",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_fiscal_conclave_new_731m,New fiscal measures conclave Apr 2026 pack +730.9m,"
        "sec_federal,Importers multinationals shareholders,"
        "CoA 2026_22 §2.4.2 + general toelichting table4,"
        "2026-04-03,2026,2026,730900000,"
        '"{""total_m"":730.9,""customs_ecomm_m"":400.7,""handling_fee_m"":77.4,'
        '""customs_retention_m"":112.3,""vat_loss_m"":48,""vvpr_reest_m"":334.5,'
        '""insurance_tax_m"":36.4,""nonres_opcent_m"":78,'
        '""note"":""Strong CoA; customs calc not inspected; VVPR front-load risk future years""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Revenue pack e-commerce+VVPR,Monitor import shift FOI,"
        "src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Federal>Fiscal>conclave_2026,tick512"
    ),
    (
        "cmt_nonfiscal_refunds_2026,Non-fiscal receipts refunds RSZ RIZIV CREG + customs fee,"
        "sec_federal,RSZ RIZIV CREG SFPIM,"
        "CoA 2026_22 §3 nonfiscal,"
        "2026-05-21,2026,2026,7829000000,"
        '"{""total_m"":7829,""b9_impact_m"":6886,""rsz_eq_m"":548,""riziv_covid_m"":187,'
        '""creg_energy_m"":285,""creg_max_m"":412,""customs_fee_m"":1013.8,'
        '""sfpim_actual_m"":78.4,""sfpim_booked_m"":55.8,""plates_delay_m"":-42.2,'
        '""note"":""Strong CoA; CREG refund no B9; SFPIM under-booked 22.6""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "One-off nonfiscal cleanup,Book SFPIM true dividend,"
        "src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Federal>Nonfiscal>BC2026,tick512"
    ),
    (
        "cmt_fed_primary_exp_cells_2026,Federal primary expenditure cells BC2026 92.05bn,"
        "sec_federal,Federal departments,"
        "CoA 2026_22 Deel II Ch II table,"
        "2026-05-21,2026,2026,92050000000,"
        '"{""total_m"":92050,""support_m"":3722,""authority_m"":23049,""economic_m"":6580,'
        '""social_m"":34611,""specific_m"":24087,'
        '""note"":""Strong CoA BOSA; near-flat +41m vs IB""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Map federal primary spend cells,Dual prior Justice/Fedasil,"
        "src_ccrek_fed_aju_fiscal_nonfisc_2026,strong,Federal>Primary_exp>cells_2026,tick512"
    ),
    (
        "cmt_dual_fiscal_nonfisc_aju,Dual conclave fiscal pack + nonfiscal one-offs vs debt interest,"
        "gg_belgium,Taxpayers importers,"
        "CoA 2026_22 residual dual,"
        "2026-05-21,2026,2026,730900000,"
        '"{""conclave_m"":730.9,""nonfiscal_up_m"":1358,""interest_bn"":12.3,'
        '""note"":""not additive pure TE; dual financing fill vs debt service""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Honest one-off vs structural,FOI customs calc + opcentiemen,"
        "src_dual_fiscal_nonfisc_tick512,strong,BE>dual>fiscal_nonfisc,tick512"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_fiscal_conclave_731m,New fiscal measures conclave pack +731m 2026,federal,taxex,Federal>Fiscal>conclave_pack_2026,730900000,730900000,Strong CoA: +730.9m new measures; customs+VVPR dominate; dual prior,strong,src_ccrek_fed_aju_fiscal_nonfisc_2026,Importers multinationals,Revenue measures pack,Front-load risk VVPR,5.0,7.5,5,6.25,Monitor import shift FOI,seed,,tick512",
    "lb_customs_ecommerce_401m,E-commerce customs reform impact class 401m,federal,taxex,Federal>Fiscal>customs_ecommerce,400700000,400700000,Medium CoA: +400.7m; data not inspected; dual EU transfer -449 retention +112,medium,src_ccrek_fed_aju_fiscal_nonfisc_2026,E-comm importers,Customs e-commerce fee,Import shift risk,5.5,7.5,5,6.35,Publish calc FOI,seed,,tick512",
    "lb_vvpr_frontload_335m,VVPR-bis anticipation re-estimate +335m 2026,federal,taxex,Federal>Fiscal>VVPR_frontload,334500000,334500000,Medium CoA: +334.5m behavior; Jan-Apr +406.3; future years adverse risk,medium,src_ccrek_fed_aju_fiscal_nonfisc_2026,Shareholders SMEs,Dividend withholding front-load,One-off revenue illusion,6.5,7.5,4,6.85,Do not annualise FOI,seed,,tick512",
    "lb_nonres_opcentiemen_78m,Non-resident opcentiemen ~78m/yr CJEU risk,federal,taxex,Federal>Fiscal>nonres_opcentiemen,78000000,78000000,Medium CoA: CJEU C-119/24 illegal; refunds from 2022 open; no solution,medium,src_ccrek_fed_aju_fiscal_nonfisc_2026,Non-resident workers,Illegal surcharge regime,Contingent refund liability,7.5,5.5,5,6.55,Fix law FOI exposure,seed,,tick512",
    "lb_creg_energy_refund_285m,CREG energy crisis premium refund 285m,federal,ops,Federal>Energy>CREG_refund,285000000,412000000,Strong CoA: +285m refund (max 412); no B9 impact; dual energy stack,strong,src_ccrek_fed_aju_fiscal_nonfisc_2026,State CREG suppliers,Crisis overprovision clawback,One-off nonfiscal,4.0,7.5,3,5.95,Track supplier repay FOI,seed,,tick512",
    "lb_nonfiscal_7829m,Non-fiscal middelen receipts 7.829bn BC2026,federal,ops,Federal>Nonfiscal>total_2026,7829000000,7829000000,Strong CoA: 7829m (+1358); RSZ 548 RIZIV 187 CREG 285 customs fee 1014,strong,src_ccrek_fed_aju_fiscal_nonfisc_2026,Federal entities,Nonfiscal revenue base,One-offs inflate,3.5,9.0,4,6.45,Separate structural FOI,seed,,tick512",
    "lb_fed_primary_cells_92bn,Federal primary exp cells 92.05bn BC2026,federal,ops,Federal>Primary_exp>cells_2026,92050000000,92050000000,Strong CoA: near-flat +41m; authority 23.0 social 34.6 support 3.7,strong,src_ccrek_fed_aju_fiscal_nonfisc_2026,Federal depts,Primary spend map,Core federal mass,2.5,9.5,6,6.45,Dual section FOI,seed,,tick512",
    "lb_dual_fiscal_nonfisc,Dual conclave fiscal +731m + nonfiscal refunds,multi,ops,BE>dual>fiscal_nonfisc,730900000,7829000000,Strong dual CoA residual financing fill,strong,src_dual_fiscal_nonfisc_tick512,Taxpayers,Dual revenue pack map,One-off vs structural,5.0,9.0,5,6.75,Honest one-off accounting,seed,,tick512",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_customs_vvpr_opcent_l5,Federal>Fiscal>customs_VVPR_opcent_L5,sec_federal,"
    "Customs e-commerce / handling fee calculation worksheets and import-shift sensitivity; "
    "VVPR-bis monthly cash 2025-26 and multi-year reverse risk; non-resident opcentiemen refund "
    "stock exposure and law fix path; employer km tax credit microdata basis for 20m/month claim,"
    "CoA 2026_22: customs data not inspected; VVPR front-load; CJEU 78m/yr contingent; FPS no km data,7,"
    "FOD Financiën AABEO / Douane,info@minfin.fed.be,"
    ",docs/doge/foi/drafts/gap_customs_vvpr_opcent_l5.md,"
    "ready,2026-07-29,,,,,cmt_fiscal_conclave_new_731m,"
    "lb_fiscal_conclave_731m|lb_customs_ecommerce_401m|lb_nonres_opcentiemen_78m,"
    "2026-07-29T00:40:00Z,2026-07-29T00:40:00Z,"
    "tick512: CoA 2026_22 residual fiscal/nonfiscal; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_503,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T00:20:00Z,,Spawned tick511 after CoA energy/debt residual; rq_116 deferred"
)
new = (
    "rq_503,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_customs_vvpr_opcent_l5,"
    "2026-07-29T00:20:00Z,2026-07-29T00:40:00Z,"
    "tick512: CoA 2026_22 residual fiscal conclave 731m nonfiscal dual; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_503 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_504,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T00:40:00Z,,Spawned tick512 after CoA fiscal/nonfiscal residual; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T00:40:00Z,rq_503,512,no,"
    "Tick512 CoA fiscal conclave 731m nonfiscal dual; next prio5 rq_504; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick512 OK")

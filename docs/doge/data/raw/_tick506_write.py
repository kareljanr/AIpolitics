# tick506 — CoA 2026_20 BBI bank data use + dual KMO/fraud enforcement
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_bbi_bankdata_2026,CoA Gebruik bankgegevens BBI AABBI 2026_20,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_20_BankgegevensBBI.pdf,"
        "Rekenhof AG 18 Mar 2026,2026-07-28,court_of_audit,"
        "Strong: bank auth ~700 2024; assessed 2.3bn 2015-24 collected 36m; CAP gaps; "
        "proc errors ~10pct; dual KMO/fraud; tick506\n"
    )
    f.write(
        "src_ccrek_bbi_bankdata_press_2026,CoA press BBI bank data Apr 2026,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_20_BankgegevensBBI_Persbericht.pdf,"
        "Rekenhof,2026-07-28,court_of_audit_press,"
        "Strong headlines: CAP incomplete; 2.3bn assessed 36m collected; 700 auth 2024; tick506\n"
    )
    f.write(
        "src_dual_bbi_kmo_fraud_tick506,Dual BBI bank tools vs KMO control vs fraud yield claims,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_20_BankgegevensBBI.pdf,"
        "DOGE synthesis CoA BBI + KMO VenB + fed aju fraud,2026-07-28,synthesis,"
        "Strong dual: BBI 2.3bn assess/36m cash + KMO 5.6bn uplift + fraud claim 0.3-0.6bn path; tick506\n"
    )

buds = [
    "bud_bbi_bank_assessed_2015_24,sec_federal,2024,2300000000,,,outturn,src_ccrek_bbi_bankdata_2026,strong,Taxes assessed in BBI dossiers with bank investigations 2.3bn cum 2015-2024 CoA; tick506",
    "bud_bbi_bank_collected_2015_24,sec_federal,2024,36000000,,,outturn,src_ccrek_bbi_bankdata_2026,strong,Effectively collected only 36m of 2.3bn assessed 2015-24 (preventive focus 5th dir); tick506",
    "bud_bbi_bank_auth_2024,sec_federal,2024,700,,,outturn,src_ccrek_bbi_bankdata_2026,strong,AABBI bank investigation authorizations ~700 in 2024 (mostly 5th dir + Brussels); not EUR; tick506",
    "bud_bbi_collection_rate_class,sec_federal,2024,1.6,,,estimated,src_ccrek_bbi_bankdata_2026,strong,Collection rate class ~36/2300 = 1.6pct on bank-investigation dossiers 2015-24; tick506",
    "bud_dual_bbi_assessed_vs_kmo_uplift,sec_federal,2024,2300000000,,,derived,src_dual_bbi_kmo_fraud_tick506,strong,Dual BBI assessed 2.3bn cum vs KMO VenB uplift 5.6bn 2024 different scopes; tick506",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_bbi_bankdata_audit,BBI AABBI bank data CAP and bank investigations CoA,"
        "sec_federal,Tax fraud targets FPS Finance STI,"
        "CoA 2026_20 + CAP law path + 18 Dec 2025 datamining,"
        "2011-01-01,2015,2026,2300000000,"
        '"{""assessed_2015_24_bn"":2.3,""collected_m"":36,""auth_2024_n"":700,'
        '""proc_error_pct"":10,""kpi_bank_pct"":10,""eval_since"":2018,'
        '""cap_foreign_selfreport"":true,""crypto_from"":2026,""datamining_law"":""2025-12-18"",'
        '""note"":""Strong CoA: low collection partly preventive; CAP completeness gap""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_20_BankgegevensBBI.pdf,"
        "Effective bank-data anti-fraud enforcement,Simplify procedures; CAP completeness; dual KMO,"
        "src_ccrek_bbi_bankdata_2026,strong,Federal>AABBI>bankdata,tick506"
    ),
    (
        "cmt_dual_bbi_kmo_fraud_enforcement,Dual BBI bank tools + KMO VenB + fraud budget claims,"
        "sec_federal,Taxpayers FPS Finance,"
        "CoA BBI 2026_20 + KMO 2026_29 + fed aju fraud,"
        "2015-01-01,2015,2029,7900000000,"
        '"{""bbi_assessed_bn"":2.3,""bbi_collected_m"":36,""kmo_uplift_bn"":5.6,'
        '""fraud_claim_2029_m"":600,""kmo_staff_gap_fte"":383,'
        '""note"":""not additive TE; enforcement stack dual opacity on collection vs claims""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_20_BankgegevensBBI.pdf,"
        "Map dual tax enforcement instruments,Staff+CAP+method FOI before yield claims,"
        "src_dual_bbi_kmo_fraud_tick506,strong,Federal>dual>Tax_enforcement_stack,tick506"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_bbi_assessed_2_3bn,BBI bank-investigation taxes assessed 2.3bn 2015-24,federal,enforcement,Federal>AABBI>bank_assessed,0,2300000000,Strong CoA: 2.3bn assessed cum; collected only 36m; 5th dir ~80pct preventive; annual0 multiyear,strong,src_ccrek_bbi_bankdata_2026,Fraud targets,Heavy fiscal fraud enforcement,Assessment mass >> cash; prevention rationale,6.0,9.0,5,7.15,Publish collection path FOI; dual KMO,seed,,tick506",
    "lb_bbi_collected_36m,BBI bank dossiers cash collected only 36m of 2.3bn,federal,enforcement,Federal>AABBI>bank_collected,36000000,36000000,Strong CoA: 36m collected 2015-24 (~1.6pct); preventive VAT carousel focus,strong,src_ccrek_bbi_bankdata_2026,Treasury,Cash recovery from STI cases,Low cash-out vs assessment headline,7.5,5.5,5,6.55,Track recovery L5 FOI,seed,,tick506",
    "lb_bbi_bank_auth_700,BBI bank investigation authorizations ~700 in 2024,federal,ops,Federal>AABBI>auth_2024,0,0,Strong CoA: ~700 auth 2024 mostly 5th dir carousels + Brussels domicile; annual0 count,strong,src_ccrek_bbi_bankdata_2026,STI directors,Authorize bank probes,KPI 10pct dossiers indicative only,4.0,3.5,3,4.05,Justify KPI; restart legal evaluation,seed,,tick506",
    "lb_bbi_proc_errors_10pct,BBI bank procedure errors ~10pct sample dossiers,federal,governance,Federal>AABBI>procedure_errors,0,0,Strong CoA sample: ~10pct procedure errors income tax; polyvalent IB/BTW rules conflict,strong,src_ccrek_bbi_bankdata_2026,Taxpayers courts,Legal certainty enforcement,Procedure complexity reduces effectiveness,7.0,3.5,4,5.55,Unify IB/BTW bank procedure law,seed,,tick506",
    "lb_dual_bbi_kmo_fraud,Dual BBI 2.3bn assess + KMO 5.6bn uplift + fraud claims,multi,enforcement,BE>dual>Tax_enforcement_stack,5600000000,7900000000,Strong dual CoA: BBI low cash recovery + KMO high uplifts + opaque fraud yield claims 0.3-0.6bn,strong,src_dual_bbi_kmo_fraud_tick506,Taxpayers,Tax enforcement integrity,Stack opacity dual FOI,6.5,9.5,5,7.55,Staff+CAP+method before claims,seed,,tick506",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

# entity aabbi optional
ent_path = root / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
if "\naabbi," not in ent and not ent.startswith("aabbi,"):
    with open(ent_path, "a", encoding="utf-8", newline="") as f:
        f.write(
            "aabbi,Algemene Administratie Bijzondere Belastinginspectie AABBI,"
            "Administration generale Inspection speciale des impots,"
            "Special Tax Inspectorate STI,agency,sec_federal,nl,"
            "https://financien.belgium.be,,,Bank auth ~700 2024; assessed 2.3bn/collected 36m 2015-24; tick506\n"
        )

foi = (
    "gap_bbi_bank_collection_l5,Federal>AABBI>bank_investigations>collection_L5,aabbi,"
    "Cash collection schedule by year 2015-2026 on the 2.3bn assessed in bank-investigation dossiers; "
    "CAP completeness metrics foreign/crypto; restart plan for legal annual evaluation since 2018; "
    "standard bank file format status,"
    "CoA 2026_20: assessed 2.3bn vs collected 36m strong; residual recovery path opaque,8,"
    "FOD Financiën AABBI / SPF Finances,info@minfin.fed.be,"
    ",docs/doge/foi/drafts/gap_bbi_bank_collection_l5.md,"
    "ready,2026-07-28,,,,,cmt_bbi_bankdata_audit,"
    "lb_bbi_assessed_2_3bn|lb_bbi_collected_36m,"
    "2026-07-28T22:50:00Z,2026-07-28T22:50:00Z,"
    "tick506: CoA 2026_20 primary fill; residual collection L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_497,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T22:30:00Z,,Spawned tick505 after CoA KMO VenB follow-up; rq_116 deferred"
)
new = (
    "rq_497,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_bbi_bank_collection_l5,"
    "2026-07-28T22:30:00Z,2026-07-28T22:50:00Z,"
    "tick506: CoA 2026_20 BBI bank 2.3bn assess/36m collect dual KMO; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_497 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_498,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T22:50:00Z,,Spawned tick506 after CoA BBI bank data; progress@510 soon; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T22:50:00Z,rq_497,506,no,"
    "Tick506 CoA BBI bank 2.3bn assess/36m collect dual KMO; next prio5 rq_498; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick506 OK")

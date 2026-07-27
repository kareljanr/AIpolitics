# tick 276 — KSZ financial middelen dual Smals
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T00:45:00Z"

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ksz_financiele_middelen,KSZ BCSS financiele middelen begrotingsuitvoering 2024-2025,"
        "https://www.ksz-bcss.fgov.be/nl/over-de-ksz/interne-organisatie/financiele-middelen|"
        "docs/doge/data/raw/ksz_financiele_middelen.html,KSZ BCSS,2026-07-30,agency,"
        "Ontvangsten 19.701m/19.761m 2024-25; uitgaven match; ICT werking 13.452/13.437m; "
        "pers 3.771/3.896m; RSZ+RSVZ bijd 16.781m IB2025; dual Smals; tick276\n"
    )

with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "ksz,Kruispuntbank van de Sociale Zekerheid KSZ,Banque Carrefour de la Securite Sociale BCSS,"
        "Crossroads Bank for Social Security,parastatal,sec_ss,bi,https://www.ksz-bcss.fgov.be,,,"
        "Budget ~19.8m 2025; ICT ops 13.4m dual Smals; RSZ 90pct RSVZ 10pct financing; Frank Robben dual Smals; tick276\n"
    )

bud = [
    "bud_ksz_ontvangsten_2024,ksz,2024,19701131,,,outturn,src_ksz_financiele_middelen,strong,Toewijzing 17.171.277 + eigen 2.392.344 = 19.701.131",
    "bud_ksz_ontvangsten_2025,ksz,2025,19760665,,,outturn,src_ksz_financiele_middelen,strong,Toewijzing 17.030.811 + eigen 2.729.854 = 19.760.665",
    "bud_ksz_toewijzing_2024,ksz,2024,17171277,,,outturn,src_ksz_financiele_middelen,strong,Toewijzing 17.171.277 2024",
    "bud_ksz_toewijzing_2025,ksz,2025,17030811,,,outturn,src_ksz_financiele_middelen,strong,Toewijzing 17.030.811 2025",
    "bud_ksz_eigen_ontvangsten_2024,ksz,2024,2392344,,,outturn,src_ksz_financiele_middelen,strong,Eigen ontvangsten 2.392.344",
    "bud_ksz_eigen_ontvangsten_2025,ksz,2025,2729854,,,outturn,src_ksz_financiele_middelen,strong,Eigen ontvangsten 2.729.854",
    "bud_ksz_uitgaven_2024,ksz,2024,19701131,,,outturn,src_ksz_financiele_middelen,strong,Total uitgaven 19.701.131 matches receipts",
    "bud_ksz_uitgaven_2025,ksz,2025,19760665,,,outturn,src_ksz_financiele_middelen,strong,Total uitgaven 19.760.665 matches receipts",
    "bud_ksz_personeel_2024,ksz,2024,3770950,,,outturn,src_ksz_financiele_middelen,strong,Personeelsuitgaven 3.770.950",
    "bud_ksz_personeel_2025,ksz,2025,3895650,,,outturn,src_ksz_financiele_middelen,strong,Personeelsuitgaven 3.895.650",
    "bud_ksz_werking_gewoon_2024,ksz,2024,2302010,,,outturn,src_ksz_financiele_middelen,strong,Gewone werkingsuitgaven 2.302.010",
    "bud_ksz_werking_gewoon_2025,ksz,2025,2270884,,,outturn,src_ksz_financiele_middelen,strong,Gewone werkingsuitgaven 2.270.884",
    "bud_ksz_ict_werking_2024,ksz,2024,13452190,,,outturn,src_ksz_financiele_middelen,strong,Werkingsuitgaven informatica 13.452.190 dual Smals class",
    "bud_ksz_ict_werking_2025,ksz,2025,13436557,,,outturn,src_ksz_financiele_middelen,strong,Werkingsuitgaven informatica 13.436.557 dual Smals class",
    "bud_ksz_ict_invest_2024,ksz,2024,18000,,,outturn,src_ksz_financiele_middelen,strong,Investeringsuitgaven informatica 18.000",
    "bud_ksz_ict_invest_2025,ksz,2025,14104,,,outturn,src_ksz_financiele_middelen,strong,Investeringsuitgaven informatica 14.104",
    "bud_ksz_rsz_bijdrage_ib2025,ksz,2025,15102730,,,budgeted,src_ksz_financiele_middelen,strong,RSZ 90pct financieringsbijdrage IB2025 15.102.730",
    "bud_ksz_rsvz_bijdrage_ib2025,ksz,2025,1678081,,,budgeted,src_ksz_financiele_middelen,strong,RSVZ 10pct 1.678.081; sum 16.780.811",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

cash = {
    "ontvangsten_2024": 19701131,
    "ontvangsten_2025": 19760665,
    "toewijzing_2024": 17171277,
    "toewijzing_2025": 17030811,
    "eigen_2024": 2392344,
    "eigen_2025": 2729854,
    "uitgaven_2024": 19701131,
    "uitgaven_2025": 19760665,
    "personeel_2024": 3770950,
    "personeel_2025": 3895650,
    "werking_gewoon_2024": 2302010,
    "werking_gewoon_2025": 2270884,
    "ict_werking_2024": 13452190,
    "ict_werking_2025": 13436557,
    "ict_invest_2024": 18000,
    "ict_invest_2025": 14104,
    "rsz_bijdrage_ib2025": 15102730,
    "rsvz_bijdrage_ib2025": 1678081,
    "bijdragen_sum_ib2025": 16780811,
    "ict_share_pct_2025": round(13436557 / 19760665 * 100, 1),
    "financing_law": "art35 KSZ-wet: FOD SZ dot + FOD ICT dot + OISZ + network + eHealth contrib + other",
    "note": "ICT ~68pct of spend dual Smals 579m institutional; L5 Smals share residual FOI; eHealth art18 contrib residual",
}
cash_csv = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
cmt = (
    "cmt_ksz_budget_2024_25,KSZ Crossroads Bank social security budget dual Smals e-health,"
    "ksz,Social protection network actors citizens employers,"
    "Wet 15 jan 1990 KSZ art 35 financing,2024-01-01,2024,2025,19760665,"
    + cash_csv
    + ",0,active,https://www.ksz-bcss.fgov.be/nl/over-de-ksz/interne-organisatie/financiele-middelen,"
    "Coordinate social data exchange network Only-once,"
    "FOI ICT L5 Smals vs other under 13.4m; open eHealth contribution cash,"
    "src_ksz_financiele_middelen,strong,SS>KSZ>budget,tick276 dual Smals ICT stack\n"
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt)

lb = [
    "lb_ksz_budget_19_8m,KSZ budget 19.8m 2025 dual Smals,federal,ops,SS>KSZ>budget,19760665,19760665,Strong KSZ site: ontvangsten=uitgaven 19.761m 2025 (19.701m 2024); RSZ+RSVZ IB 16.781m; core SS data exchange not pure waste,strong,src_ksz_financiele_middelen,SS institutions citizens,Social data network coordination,Core infrastructure dual Smals 579m,3,6.5,3,5.15,Publish ICT vendor L5; dual unit-cost Smals,seed,,tick276",
    "lb_ksz_ict_13_4m,KSZ ICT werkingsuitgaven 13.4m 2025 dual Smals,federal,ops,SS>KSZ>ICT,13436557,13436557,Strong: informatica werking 13.437m 2025 (13.452m 2024) = ~68pct of KSZ spend; dual Smals member recharge class residual FOI,strong,src_ksz_financiele_middelen,KSZ Smals ICT providers,SS network ICT operations,Middleman ICT dual Smals; not pure waste if scale real,4,7.0,4,5.7,FOI Smals share of 13.4m; dual gap_smals_l5,seed,,tick276 dual Smals",
    "lb_ksz_pers_3_9m,KSZ personnel 3.9m 2025,federal,ops,SS>KSZ>personnel,3895650,3895650,Strong: personeelsuitgaven 3.896m 2025 (3.771m 2024); small vs ICT 13.4m,strong,src_ksz_financiele_middelen,KSZ staff,Core network staff,Lean staff vs ICT pass-through pattern,2,4.5,2,3.85,Track multi-year FTE,seed,,tick276",
    "lb_ksz_smals_ehealth_triple,KSZ 19.8m dual Smals 579m dual e-health 132.5m,federal,ops,BE>SS_Health>triple_digital,0,0,Strong triple map: KSZ ~19.8m + Smals omzet 578.9m + INAMI e-health 132.5m; KSZ ICT 13.4m is subset path into Smals class; not additive,strong,src_ksz_financiele_middelen,Citizens SS health system,Digital SS and e-health stack,Institutional multi-layer digital SS,4,8.5,5,6.55,Reconcile KSZ ICT invoices to Smals; joint transparency,seed,,tick276 dual not additive",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# FOI residual ICT L5
foi_path = base / "foi_queue.csv"
lines = foi_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
out = []
for line in lines:
    if line.startswith("gap_smals_l5_members,") and "tick276" not in line:
        line = line.rstrip() + " | tick276: KSZ ICT 13.4m public dual; residual Smals share still ready"
    out.append(line)
gap = "gap_ksz_ict_l5_smals"
if not any(l.startswith(gap + ",") for l in out):
    out.append(
        f"{gap},SS>KSZ>ICT_L5_Smals,ksz,"
        "L5 split werkingsuitgaven informatica 13.4m 2024-2025: Smals vs other vendors cash; "
        "eHealth-platform art.18 contribution amount multi-year; FOD SZ and FOD ICT annual dots if any; "
        "unit prices berichten series,"
        "KSZ totals strong public; ICT is 68pct spend and dual Smals opacity; eHealth financing residual,"
        "5,KSZ BCSS openbaarheid / Beheerscomité / IBZ FOI,,"
        "https://www.ksz-bcss.fgov.be,"
        f"docs/doge/foi/drafts/{gap}.md,ready,2026-07-30,,,,,,"
        f"cmt_ksz_budget_2024_25,lb_ksz_ict_13_4m,{now},{now},"
        "tick276 draft ready human send; totals filled"
    )
foi_path.write_text("\n".join(out) + "\n", encoding="utf-8")

# research_queue
rq_path = base / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq:
    if line.startswith("rq_267,"):
        out.append(
            "rq_267,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CDZ/HDA).,"
            f"gap_ksz_ict_l5_smals,2026-07-30T00:15:00Z,{now},"
            "tick276: KSZ 19.8m ICT 13.4m dual Smals; spawn rq_268"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_268,") for l in out):
    out.append(
        "rq_268,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after KSZ).,,"
        f"{now},,Spawned tick276 after KSZ; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_267,276,no,"
    "Scheduler 60s. Next prio5 rq_268; rq_116 SWA deferred. FOI ready human send. tick276 KSZ 19.8m ICT 13.4m dual Smals.\n",
    encoding="utf-8",
)
print("OK tick276")

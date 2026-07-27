# tick 279 — CREG + BIPT dual federal regulators
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T02:15:00Z"

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_creg_ar_2023,CREG Jaarverslag 2023 rekeningen lasten personeel,"
        "docs/doge/data/raw/creg_ar_2023.pdf,CREG,2026-07-30,agency,"
        "Lasten 22.409m 2023 (16.041m 2022); personeel 14.685m; accijns finance; "
        "overwinsten env 4.119m spent 2.161m; tick279\n"
    )
    f.write(
        "src_bipt_ar_2024,BIPT Annual Report 2024 financial accounts staff,"
        "docs/doge/data/raw/bipt_ar_2024.pdf,BIPT,2026-07-30,agency,"
        "Rev 78.463m exp 79.755m 2024; payroll pack ~27.4m; licence fees 55.1m; "
        "staff 251/242 FTE; ombuds postal 2.35m telecom 2.70m; tick279\n"
    )
    f.write(
        "src_kamer_creg_budget_2026_press,Kamer CREG budget 2026 24.396m vote secondary,"
        "https://www.dekamer.be/FLWB/PDF/56/1192/56K1192001.pdf,Kamer Energy commission,2026-07-30,secondary,"
        "Vote summary CREG budget 2026 24.396072m incl; medium pending full PDF extract; tick279\n"
    )

with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "creg,Commissie voor de Regulering van de Elektriciteit en het Gas CREG,"
        "Commission de regulation de l electricite et du gaz,"
        "Belgian federal energy regulator,agency,sec_federal,bi,https://www.creg.be,,,"
        "Lasten 22.4m 2023; accijns finance not TE; dual VREG BRUGEL CWaPE; tick279\n"
    )
    f.write(
        "bipt,Belgisch Instituut voor postdiensten en telecommunicatie BIPT,"
        "Institut belge des services postaux et des telecommunications IBPT,"
        "Belgian postal and telecom regulator,agency,sec_federal,bi,https://www.bipt.be,,,"
        "Exp 79.8m 2024 licence-fee financed; staff 251; dual CREG; tick279\n"
    )

bud = [
    "bud_creg_lasten_2022,creg,2022,16040616,,,outturn,src_creg_ar_2023,strong,AR: total lasten 16.040.616",
    "bud_creg_lasten_2023,creg,2023,22408653,,,outturn,src_creg_ar_2023,strong,AR: total lasten 22.408.653",
    "bud_creg_personeel_2022,creg,2022,12881408,,,outturn,src_creg_ar_2023,strong,Personeelskosten 12.881.408",
    "bud_creg_personeel_2023,creg,2023,14685471,,,outturn,src_creg_ar_2023,strong,Personeelskosten 14.685.471 (~65.5pct of lasten)",
    "bud_creg_externe_experts_2023,creg,2023,1736137,,,outturn,src_creg_ar_2023,strong,Externe experts 1.736.137",
    "bud_creg_algemene_kosten_2023,creg,2023,3603804,,,outturn,src_creg_ar_2023,strong,Algemene kosten 3.603.804",
    "bud_creg_overwinsten_spent_2023,creg,2023,2161354,,,outturn,src_creg_ar_2023,strong,Opdracht Overwinsten spent 2.161.354 of envelope 4.118.512",
    "bud_creg_accijnzen_gross_2023,creg,2023,26195311,,,outturn,src_creg_ar_2023,strong,Accijnzen elektriciteit en aardgas gross 26.195.311 before regularisaties",
    "bud_creg_budget_2026,creg,2026,24396072,,,budgeted,src_kamer_creg_budget_2026_press,medium,Kamer vote summary 24.396.072 2026; verify full PDF",
    "bud_bipt_rev_2024,bipt,2024,78463148,,,outturn,src_bipt_ar_2024,strong,AR: total revenues 78.463.148",
    "bud_bipt_exp_2024,bipt,2024,79754796,,,outturn,src_bipt_ar_2024,strong,AR: total expenditure 79.754.796",
    "bud_bipt_payroll_2024,bipt,2024,15853419,,,outturn,src_bipt_ar_2024,strong,Payroll 15.853.419",
    "bud_bipt_ssc_pensions_2024,bipt,2024,10604194,,,outturn,src_bipt_ar_2024,strong,SSC and pensions 10.604.194",
    "bud_bipt_pers_pack_2024,bipt,2024,27356499,,,outturn,src_bipt_ar_2024,strong,Payroll+SSC+benefits 15.853+10.604+0.899=27.356m",
    "bud_bipt_public_licence_fees_2024,bipt,2024,55123176,,,outturn,src_bipt_ar_2024,strong,Public licence fees 55.123.176",
    "bud_bipt_private_radio_fees_2024,bipt,2024,19419768,,,outturn,src_bipt_ar_2024,strong,Licence monitoring private radio 19.419.768",
    "bud_bipt_staff_2024,bipt,2024,251,,,outturn,src_bipt_ar_2024,strong,Staff 251 (242.2 FTE); amount is headcount",
    "bud_ombuds_postal_2024,bipt,2024,2354355,,,outturn,src_bipt_ar_2024,strong,Ombudsman postal sector exp 2.354.355 (sector contribution)",
    "bud_ombuds_telecom_2024,bipt,2024,2695248,,,outturn,src_bipt_ar_2024,strong,Ombudsman telecom exp 2.695.248",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

def cmt(cid, title, ent, ben, env, cash, goal, cut, path, notes, conf="strong", src="src_creg_ar_2023"):
    j = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
    return (
        f"{cid},{title},{ent},{ben},Sector law + AR primary,2022-01-01,2022,2026,{env},"
        f"{j},0,active,docs/doge/data/raw/{'creg_ar_2023.pdf' if 'creg' in ent else 'bipt_ar_2024.pdf'},"
        f"{goal},{cut},{src},{conf},{path},{notes}\n"
    )

with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt(
        "cmt_creg_budget_2022_26",
        "CREG federal energy regulator package dual BIPT",
        "creg", "Electricity gas market consumers TSO DSO",
        22408653,
        {
            "lasten_2022": 16040616,
            "lasten_2023": 22408653,
            "personeel_2023": 14685471,
            "externe_2023": 1736137,
            "overwinsten_env_2023": 4118512,
            "overwinsten_spent_2023": 2161354,
            "budget_2026_medium": 24396072,
            "finance": "special excise electricity gas via FPS Finance not TE",
            "note": "Dual regional VREG BRUGEL CWaPE; fund pass-through large separate",
        },
        "Independent energy market regulation",
        "FOI 2024-25 full AR; dual unit-cost regional regulators",
        "Federal>Energy>CREG",
        "tick279 dual BIPT",
    ))
    f.write(cmt(
        "cmt_bipt_budget_2024",
        "BIPT postal telecom regulator package dual CREG",
        "bipt", "Operators end-users spectrum postal",
        79754796,
        {
            "rev_2024": 78463148,
            "exp_2024": 79754796,
            "pers_pack_2024": 27356499,
            "public_licence_fees": 55123176,
            "private_radio_fees": 19419768,
            "staff": 251,
            "fte": 242.2,
            "ombuds_postal": 2354355,
            "ombuds_telecom": 2695248,
            "finance": "licence and monitoring fees sector not TE",
            "note": "USO funds not activated 2024; dual CREG energy regulator",
        },
        "Regulate postal electronic communications spectrum",
        "FOI multi-year path; dual unit-cost CREG",
        "Federal>Telecom>BIPT",
        "tick279 dual CREG",
        "strong",
        "src_bipt_ar_2024",
    ))

lb = [
    "lb_creg_lasten_22_4m,CREG operating lasten 22.4m 2023 dual BIPT,federal,ops,Federal>Energy>CREG,22408653,22408653,Strong AR: lasten 22.409m 2023 (16.041m 2022); personeel 14.685m 65pct; accijns finance; core regulator not pure waste,strong,src_creg_ar_2023,Market participants consumers,Energy market regulation,Core independent regulator dual BIPT,3,6.5,3,5.15,FOI 2024-25 AR; dual regional,seed,,tick279",
    "lb_creg_overwinsten_2_2m,CREG overwinsten assignment spent 2.2m 2023,federal,ops,Federal>Energy>CREG>overwinsten,2161354,2161354,Strong AR: special envelope 4.119m Kamer spent 2.161m on surplus profits task; residual capacity,strong,src_creg_ar_2023,State energy producers,Surplus profit levy support,One-off policy task; under-spend,4,4.0,3,4.1,Track multi-year if prolonged,seed,,tick279",
    "lb_bipt_exp_79_8m,BIPT expenditure 79.8m 2024 dual CREG,federal,ops,Federal>Telecom>BIPT,79754796,79754796,Strong AR: exp 79.755m rev 78.463m 2024; licence-fee financed; staff 251; core regulator not pure waste,strong,src_bipt_ar_2024,Operators end-users,Postal telecom spectrum regulation,Core dual energy/telecom regulators,3,7.5,3,5.55,Publish multi-year path; dual CREG unit-cost,seed,,tick279",
    "lb_bipt_pers_27_4m,BIPT personnel package 27.4m 2024,federal,ops,Federal>Telecom>BIPT>personnel,27356499,27356499,Strong AR: payroll 15.853 + SSC/pensions 10.604 + benefits 0.899 = 27.357m; ~34pct of exp,strong,src_bipt_ar_2024,BIPT staff,Regulator staffing,Core capacity dual CREG 14.7m personnel,3,6.5,3,5.15,Track FTE multi-year,seed,,tick279",
    "lb_regulators_dual_creg_bipt,Federal regulators dual CREG 22.4m + BIPT 79.8m,federal,ops,BE>Regulators>dual_CREG_BIPT,0,0,Strong dual: CREG lasten 22.4m 2023 + BIPT exp 79.8m 2024; both sector-fee financed not TE; not additive,strong,src_bipt_ar_2024,Markets consumers,Independent economic regulation stack,Institutional dual energy/telecom,4,8.0,4,5.7,Publish joint fee transparency matrix,seed,,tick279 dual not additive",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# FOI residual multi-year
foi_path = base / "foi_queue.csv"
lines = foi_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
out = lines[:]
gap = "gap_creg_bipt_2024_26"
if not any(l.startswith(gap + ",") for l in out):
    out.append(
        f"{gap},Federal>Regulators>CREG_BIPT_2024_26,creg,"
        "CREG full jaarrekening/AR 2024-2025 and Kamer-approved budgets 2025-2026 line detail; "
        "BIPT multi-year 2022-2025 path same structure; L5 external experts top vendors; "
        "reconcile medium 24.396m 2026 Kamer claim,"
        "2023 CREG + 2024 BIPT strong; multi-year dual path residual,"
        "4,CREG / BIPT openbaarheid / Kamer Energy-Telecom,,"
        "https://www.creg.be,"
        f"docs/doge/foi/drafts/{gap}.md,ready,2026-07-30,,,,,,"
        f"cmt_creg_budget_2022_26|cmt_bipt_budget_2024,lb_regulators_dual_creg_bipt,{now},{now},"
        "tick279 draft ready human send; primary years filled"
    )
foi_path.write_text("\n".join(out) + "\n", encoding="utf-8")

rq_path = base / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq:
    if line.startswith("rq_271,"):
        out.append(
            "rq_271,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after FPD/RSZ). Prefer this over rq_270 until ticks=280.,"
            f"gap_creg_bipt_2024_26,2026-07-30T01:45:00Z,{now},"
            "tick279: CREG 22.4m 2023 + BIPT 79.8m 2024 dual regulators; spawn rq_272; progress@280 next"
        )
    elif line.startswith("rq_270,"):
        # elevate priority for next tick (280)
        out.append(
            "rq_270,Mandatory progress@280 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
            "When ticks_completed hits 280: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
            "and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
            f"2026-07-30T01:45:00Z,{now},Elevated prio6 after tick279 for tick280 progress run"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_272,") for l in out):
    out.append(
        "rq_272,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills after progress@280 (AGMJ wage if public; Fedasil; FSMA; other FOI-adjacent).,,"
        f"{now},,Spawned tick279 after CREG BIPT; run after rq_270 progress"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_271,279,no,"
    "Scheduler 60s. Next MANDATORY progress rq_270@280; then rq_272. FOI ready human send. tick279 CREG 22.4m BIPT 79.8m.\n",
    encoding="utf-8",
)
print("OK tick279")

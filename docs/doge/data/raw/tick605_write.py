# tick 605 — AWAC dual VEKA climate agency hole-fill
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T17:00:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


# update entity awac
ent = (root / "entities.csv").read_text(encoding="utf-8")
old = (
    "awac,Agence wallonne de l Air et du Climat AWAC,Agence wallonne de l Air et du Climat,"
    "Walloon air and climate agency dual VEKA climate,agency,wallonie_gov,fr,"
    "https://www.awac.be,,,Budget 2025 annex dep 37.376m rec 17.471m Art.90 EPNE; tick355"
)
new = (
    "awac,Agence wallonne de l Air et du Climat AWAC,Agence wallonne de l Air et du Climat,"
    "Walloon air and climate agency dual VEKA climate,agency,wallonie_gov,fr,"
    "https://www.awac.be,,,SACA; BI2025 SEC rec 19.428m dep 19.333m solde +0.095m CoA; "
    "BI2024 rec 19.664m dep 23.142m solde -3.478m; dual VEKA VL E&K domain; tick605"
)
if old not in ent:
    if "awac,Agence wallonne" in ent:
        ent = ent.replace(
            "Budget 2025 annex dep 37.376m rec 17.471m Art.90 EPNE; tick355",
            "SACA; BI2025 SEC rec 19.428m dep 19.333m CoA; dual VEKA; tick605",
        )
    else:
        raise SystemExit("awac entity missing")
else:
    ent = ent.replace(old, new)
(root / "entities.csv").write_text(ent, encoding="utf-8")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_awac_budget_bi2025,Cour des comptes Budget RW 2024A2025I Table33 AWAC SEC,"
        "https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,"
        "Cour des comptes Wallonie,2026-07-31,official_audit,"
        "Strong tick605 p75: AWAC SACA BI2025 rec SEC 19428000 dep 19333000 solde +95000; "
        "BI2024 rec 19664000 dep 23142000 solde -3478000; dual VEKA; raw ccrek_budget_rw_2024a2025i.pdf\n"
    )
    f.write(
        "src_awac_budget_ajust_2025_art15,Decret RW ajust budget 2025 Art15 AWAC,"
        "https://wallex.wallonie.be/eli/loi-decret/2025/07/09/2025006092,"
        "Parlement wallon / Wallex,2026-07-31,official_budget,"
        "Strong tick605 Art15: budget ajuste AWAC 2025 recettes 19428000 depenses 19333000 EUR\n"
    )
    f.write(
        "src_dual_climate_awac_veka_tick605,Dual climate AWAC WAL + VEKA Flanders,"
        "docs/doge/raw/ccrek_budget_rw_2024a2025i.pdf,DOGE synthesis AWAC CoA + VEKA domain,"
        "2026-07-31,synthesis,"
        "Strong dual: AWAC SACA SEC dep 19.3m BI2025 vs VEKA dual climate Flanders E&K domain "
        "VEK 1.105bn class (much larger package); agency-scale dual; tick605\n"
    )

bud_rows = [
    ("bud_awac_rec_sec_2025", 2025, 19428000, "AWAC recettes SEC BI2025 19.428m CoA/decret; tick605", "src_ccrek_awac_budget_bi2025"),
    ("bud_awac_dep_sec_2025", 2025, 19333000, "AWAC depenses SEC BI2025 19.333m CoA/decret; tick605", "src_ccrek_awac_budget_bi2025"),
    ("bud_awac_solde_sec_2025", 2025, 95000, "AWAC solde SEC BI2025 +0.095m CoA; tick605", "src_ccrek_awac_budget_bi2025"),
    ("bud_awac_rec_sec_2024", 2024, 19664000, "AWAC recettes SEC BI2024 19.664m CoA; tick605", "src_ccrek_awac_budget_bi2025"),
    ("bud_awac_dep_sec_2024", 2024, 23142000, "AWAC depenses SEC BI2024 23.142m CoA; tick605", "src_ccrek_awac_budget_bi2025"),
    ("bud_awac_solde_sec_2024", 2024, -3478000, "AWAC solde SEC BI2024 -3.478m CoA; tick605", "src_ccrek_awac_budget_bi2025"),
    ("bud_awac_rec_ajust_2025", 2025, 19428000, "AWAC budget ajuste 2025 recettes 19.428m Art15; tick605", "src_awac_budget_ajust_2025_art15"),
    ("bud_awac_dep_ajust_2025", 2025, 19333000, "AWAC budget ajuste 2025 depenses 19.333m Art15; tick605", "src_awac_budget_ajust_2025_art15"),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, year, amt, note, src in bud_rows:
        f.write(f"{bid},awac,{year},{amt},,,outturn,{src},strong,{note}\n")

cmt = {
    "2025_rec_sec": 19428000,
    "2025_dep_sec": 19333000,
    "2025_solde_sec": 95000,
    "2024_rec_sec": 19664000,
    "2024_dep_sec": 23142000,
    "2024_solde_sec": -3478000,
    "note": "SACA air climate dual VEKA; SEC budget CoA primary; staff RA residual FOI",
}
cmt_dual = {
    "awac_dep_2025_m": 19.333,
    "awac_rec_2025_m": 19.428,
    "veka_domain_vek_2026_m": 1105.0,
    "note": "Dual climate: AWAC WAL agency 19.3m vs VEKA Flanders E&K domain ~1.1bn package",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_awac_budget_2024_25,AWAC dual VEKA climate SACA 2024-25,awac,'
        f'Wallonie climate ETS policy,RW SEC budget SACA,'
        f'2024-01-01,2024,2030,19333000,"{esc_json(cmt)}",0,active,'
        f'https://www.awac.be,Air climate inventory ETS Wallonia,'
        f'Publish RA staff L5 FOI residual,'
        f'src_ccrek_awac_budget_bi2025,strong,Wallonie>Climate>AWAC,tick605 CoA+decret primary deepen\n'
    )
    f.write(
        f'cmt_dual_climate_awac_veka_2025,Dual climate AWAC WAL + VEKA Flanders 2025,gg_belgium,'
        f'Regional climate energy dual,AWAC SEC + VEKA domain class,'
        f'2025-01-01,2025,2026,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual climate agencies,FOI dual unit-cost climate,'
        f'src_dual_climate_awac_veka_tick605,strong,BE>dual>climate_AWAC_VEKA,tick605\n'
    )

lb = [
    (
        "lb_awac_dep_19_3m_2025",
        "AWAC depenses SEC 19.3m recettes 19.4m BI2025 dual VEKA",
        "Wallonia",
        "ops",
        "Wallonie>Climate>AWAC>dep_19_3m",
        19333000,
        19333000,
        "Strong CoA/decret: SEC dep 19.333m rec 19.428m solde +0.095m SACA dual VEKA domain",
        "src_ccrek_awac_budget_bi2025",
        3,
        7.0,
        4,
        5.05,
        "RA staff FOI residual",
    ),
    (
        "lb_awac_dep_23_1m_2024",
        "AWAC depenses SEC 23.1m solde -3.5m BI2024",
        "Wallonia",
        "ops",
        "Wallonie>Climate>AWAC>dep_23_1m_2024",
        23142000,
        23142000,
        "Strong CoA: BI2024 dep 23.142m rec 19.664m solde -3.478m; path improves 2025",
        "src_ccrek_awac_budget_bi2025",
        3,
        7.0,
        4,
        5.05,
        "Outturn recon FOI",
    ),
    (
        "lb_awac_solde_turnaround_2025",
        "AWAC SEC solde turnaround -3.5m to +0.1m 2024-25",
        "Wallonia",
        "ops",
        "Wallonie>Climate>AWAC>solde_turnaround",
        95000,
        3573000,
        "Strong CoA: solde path +3.573m improvement BI2024 to BI2025",
        "src_ccrek_awac_budget_bi2025",
        3,
        5.5,
        4,
        4.40,
        "Explain cut path FOI",
    ),
    (
        "lb_dual_climate_awac_veka_2025",
        "Dual climate AWAC 19.3m + VEKA domain 1.1bn class",
        "multi",
        "ops",
        "BE>dual>climate_AWAC_VEKA_2025",
        19333000,
        1105000000,
        "Strong dual: AWAC WAL SACA 19.3m agency vs VEKA Flanders E&K domain VEK ~1.1bn package scale",
        "src_dual_climate_awac_veka_tick605",
        4,
        8.5,
        5,
        6.35,
        "FOI dual climate matrix",
    ),
    (
        "lb_awac_saca_status_2025",
        "AWAC SACA autonomous accounting dual climate",
        "Wallonia",
        "ops",
        "Wallonie>Climate>AWAC>saca_status",
        0,
        0,
        "Strong CoA: SACA like AWaP OPW; own budget distinct SPW; dual governance layer",
        "src_ccrek_awac_budget_bi2025",
        3,
        5.0,
        4,
        4.15,
        "Governance dual FOI",
    ),
    (
        "lb_awac_rec_19_4m_2025",
        "AWAC recettes SEC 19.4m BI2025",
        "Wallonia",
        "ops",
        "Wallonie>Climate>AWAC>rec_19_4m",
        19428000,
        19428000,
        "Strong: SEC income 19.428m nearly balances dep 19.333m",
        "src_ccrek_awac_budget_bi2025",
        3,
        7.0,
        3,
        5.05,
        "Income mix FOI",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        lid, title, jur, cat, hpath, annual, stock, note, src, prio, scale, opac, pidx, hook = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"WAL climate policy,Air climate inventory ETS,Core public climate dual,"
            f"{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick605\n"
        )

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_awac_ra_staff_l5_2025,Wallonie>AWAC>RA_staff_L5_2025,awac,"
        "Activity report + staff ETP 2024-25; income mix recon to SEC 19.4m; outturn vs BI; "
        "dual unit-cost vs VEKA; ETS admin L5,"
        "CoA SEC budget strong tick605; RA staff residual,5,"
        "AWAC / SPW / openabilite wallonne,,https://www.awac.be,"
        "docs/doge/foi/drafts/gap_awac_ra_staff_l5_2025.md,ready,2026-07-31,,,,"
        "cmt_awac_budget_2024_25|cmt_dual_climate_awac_veka_2025,"
        "lb_awac_dep_19_3m_2025|lb_dual_climate_awac_veka_2025,"
        f"{utc},{utc},tick605 AWAC CoA+decret primary; residual RA staff human send\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_596,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:45:00Z,,Spawned tick604 after AWaP dual OE; rq_116 deferred; progress@610 in 6"
)
new = (
    "rq_596,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:45:00Z,2026-07-31T17:00:00Z,"
    "tick605: AWAC SEC 19.3m dual VEKA climate; spawn rq_597; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_596 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_597,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T17:00:00Z,,Spawned tick605 after AWAC dual VEKA; rq_116 deferred; progress@610 in 5\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_596,605,no,"
    "tick605 AWAC SEC 19.3m dual VEKA; next rq_597; progress@610 in 5; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick605 CSV writes OK")

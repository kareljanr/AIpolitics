# -*- coding: utf-8 -*-
"""Tick 162 — rq_157 hole-fill: FOREM Wallonie budget 2026 L5 programme 130 (EP Jeholet)."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
TICK = 162
UNIT = "rq_157"
UTC = "2026-07-28T04:05:00Z"

# All amounts EUR; EP table in kEUR * 1000
L5 = {
    "sesam": 106945000,
    "aides_emploi_forem": 2170000,
    "aides_emploi_autres": 6215000,
    "allocation_activation": 76237000,
    "primes_complements": 672000,
    "ape": 1279282000,
    "titres_services": 568406000,
    "promo_emploi_ltd_nonmarchand": 3551000,
    "conge_education_paye": 21000000,
    "aides_formation_forem": 26735000,
    "aides_formation_autres": 13055000,
    "fonctionnement_forem": 419714000,
    "fonctionnement_autres": 27867000,
    "partenariat_general": 24669000,
    "partenariat_pkpl": 282000,
    "partenariat_cisp": 104325000,
    "cellules_reconversion": 7287000,
    "droits_tirage_onss": 136777000,
    "invest_hors_cdc": 6813000,
    "invest_cdc": 1617000,
}
TOTAL = sum(L5.values())  # 2833619000


def read_text(p: Path) -> str:
    raw = p.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def write_text(p: Path, text: str) -> None:
    p.write_bytes(text.encode("utf-8", errors="replace"))


def append_if_missing(p: Path, rows: list[str]) -> None:
    text = read_text(p)
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        if row.split(",", 1)[0] not in text:
            text += row + "\n"
    write_text(p, text)


def replace_line_startswith(p: Path, prefix: str, new_line: str) -> bool:
    text = read_text(p)
    lines = text.splitlines()
    out, found = [], False
    for L in lines:
        if L.startswith(prefix):
            out.append(new_line)
            found = True
        else:
            out.append(L)
    write_text(p, "\n".join(out) + "\n")
    return found


assert TOTAL == 2833619000, TOTAL

srcs = [
    'src_wal_ep_jeholet_2026,Wallonie Expose particulier budget 2026 Emploi Jeholet FOREM prog 130,https://finances.wallonie.be/files/Budget%202026/Budget%202026/jeholet/epje.pdf,SPW Finances / Parlement wallon,2026-07-28,budget,"Prog 18.130 FOREM 2.833619bn eng=liq 2026 L5: APE 1.279bn titres 568.4m fonct 419.7m SESAM 106.9m ONSS draw 136.8m CISP 104.3m activation 76.2m; tick162"',
]
append_if_missing(DATA / "sources.csv", srcs)

# budgets — keep existing total id amount; add L5 lines
bud = [
    f"bud_forem_prog130_total_2026,forem,2026,{TOTAL},,,budgeted,src_wal_ep_jeholet_2026,strong,EP Jeholet prog 130 sum of 20 AB lines eng=liq 2.833619bn 2026 (matches ExpGen 18.130; dual PES)",
    f"bud_forem_ape_2026,forem,2026,{L5['ape']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.006 Aides emploi Dispositif APE 1.279282bn 2026 (largest L5 block)",
    f"bud_forem_titres_services_2026,forem,2026,{L5['titres_services']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.007 Titres-services subventions 568.406m 2026",
    f"bud_forem_fonctionnement_2026,forem,2026,{L5['fonctionnement_forem']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.012 Depenses fonctionnement FOREM 419.714m 2026 (contrat de gestion)",
    f"bud_forem_sesam_2026,forem,2026,{L5['sesam']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.001 SESAM primes entreprises 106.945m 2026",
    f"bud_forem_droits_tirage_onss_2026,forem,2026,{L5['droits_tirage_onss']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.018 Droits de tirage reductions cotisations ONSS groupes cibles 136.777m 2026",
    f"bud_forem_partenariat_cisp_2026,forem,2026,{L5['partenariat_cisp']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.016 Partenariat CISP 104.325m 2026",
    f"bud_forem_allocation_activation_2026,forem,2026,{L5['allocation_activation']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.004 Allocation activation 76.237m 2026",
    f"bud_forem_fonctionnement_autres_2026,forem,2026,{L5['fonctionnement_autres']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.013 Fonctionnement autres 27.867m 2026",
    f"bud_forem_aides_formation_forem_2026,forem,2026,{L5['aides_formation_forem']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.010 Aides formation FOREM 26.735m 2026",
    f"bud_forem_partenariat_general_2026,forem,2026,{L5['partenariat_general']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.014 Partenariat general 24.669m 2026",
    f"bud_forem_cep_2026,forem,2026,{L5['conge_education_paye']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.009 Congé education paye 21.0m 2026",
    f"bud_forem_aides_formation_autres_2026,forem,2026,{L5['aides_formation_autres']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.011 Aides formation autres (cheques formation etc) 13.055m 2026",
    f"bud_forem_invest_total_2026,forem,2026,{L5['invest_hors_cdc']+L5['invest_cdc']},,,budgeted,src_wal_ep_jeholet_2026,strong,AB 130.019+130.020 invest 6.813+1.617=8.430m 2026",
    # 2025 legacy split programmes (pre-rationalisation) for comparison
    "bud_forem_prog12_2025,forem,2025,370072000,,,budgeted,src_wal_ep_jeholet_2026,strong,Prog 12 FOREM 2025 MA/MP 370.072m (2026 lines zeroed transferred to prog 130)",
    "bud_forem_titres_services_2025,forem,2025,567614000,,,budgeted,src_wal_ep_jeholet_2026,strong,Prog 17 Titres services FOREM 567.614m 2025 MA/MP",
    "bud_forem_formation_prog22_2025,forem,2025,344624000,,,budgeted,src_wal_ep_jeholet_2026,strong,Prog 22 Forem Formation 344.624m 2025 MA/MP (folded into 130 in 2026)",
    "bud_forem_reductions_groupes_2025,forem,2025,187610000,,,budgeted,src_wal_ep_jeholet_2026,strong,Prog 18 reductions cotisations groupes cibles FOREM 187.610m 2025",
]
append_if_missing(DATA / "budgets.csv", bud)

# correct note on existing ExpGen row if present — leave amount (same 2833619000)
replace_line_startswith(
    DATA / "budgets.csv",
    "bud_wal_forem_prog_2026,",
    f"bud_wal_forem_prog_2026,forem,2026,{TOTAL},,,budgeted,src_wal_ep_jeholet_2026,strong,"
    "Prog 18.130/130 Nouveau FOREM eng=liq 2.833619bn 2026 confirmed EP Jeholet L5 sum (was ExpGen same total)",
)

import json

detail = json.dumps({k: v for k, v in L5.items()}, separators=(",", ":"))
# escape for CSV
detail_csv = detail.replace('"', '""')

cmts = [
    (
        f'cmt_forem_prog130_2026,FOREM Wallonie programme 130 full L5 2026,forem,Jobseekers employers Wallonia,'
        f'SPW budget EP Jeholet DO18 prog 130,2026-01-01,2026,2026,{TOTAL},'
        f'"{detail_csv}",0,active,'
        f'https://finances.wallonie.be/files/Budget%202026/Budget%202026/jeholet/epje.pdf,'
        f'PES Wallonia dual VDAB/Actiris,Publish RA 2024-25 outturn same split; unit costs,'
        f'src_wal_ep_jeholet_2026,strong,Wallonie>Emploi>FOREM>prog130,'
        f'tick162: APE 1.279bn + titres 568m dominate; functioning 420m vs VDAB 0.75bn VL krediet apples-oranges'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

lbs = [
    (
        f'lb_forem_ape_2026,FOREM APE device 1.279bn 2026,Wallonia,ops,Wallonie>Emploi>FOREM>APE,'
        f"{L5['ape']},{L5['ape']},"
        f'EP Jeholet AB 130.006 strong 1.279282bn; largest single FOREM L5; employment-aid passthrough not pure PES ops,'
        f'strong,src_wal_ep_jeholet_2026,Walloon employers non-profit/public,Employment promotion APE,'
        f'Mass envelope; dual architecture vs Flanders; reform risk,5,9.5,7,7.2,'
        f'Publish beneficiary L5 top; track reform savings,seed,,tick162'
    ),
    (
        f'lb_forem_titres_services_2026,FOREM titres-services 568m 2026,Wallonia,ops,Wallonie>Emploi>FOREM>titres_services,'
        f"{L5['titres_services']},{L5['titres_services']},"
        f'AB 130.007 568.406m 2026 (567.614m 2025); household service cheques subsidy,'
        f'strong,src_wal_ep_jeholet_2026,Households employers TS workers,Service cheques,'
        f'Large demand-side subsidy; parallel Flanders dienstencheques,4,9.0,7,6.8,'
        f'Reconcile user co-pay vs public share; dual region compare,seed,,tick162'
    ),
    (
        f'lb_forem_fonctionnement_2026,FOREM operating grant 420m 2026,Wallonia,ops,Wallonie>Emploi>FOREM>fonctionnement,'
        f"{L5['fonctionnement_forem']},{L5['fonctionnement_forem']},"
        f'AB 130.012 419.714m contrat de gestion; closest apples-to-apples vs VDAB ops (not total 2.83bn),'
        f'strong,src_wal_ep_jeholet_2026,Walloon jobseekers,PES operating,'
        f'Core agency ops; dual PES overhead vs VDAB,5,8.5,6,6.4,'
        f'Unit cost per jobseeker vs VDAB/Actiris; FTE,seed,,tick162'
    ),
    (
        f'lb_forem_prog130_2026,FOREM consolidated prog 130 2.834bn 2026,Wallonia,ops,Wallonie>Emploi>FOREM,'
        f'{TOTAL},{TOTAL},'
        f'EP L5 sum 2.833619bn; APE+titres+ONSS draw dominate; dual PES vs VDAB 0.75bn,'
        f'strong,src_wal_ep_jeholet_2026,Walloon jobseekers employers,PES + employment aids,'
        f'Not pure waste; perimeter ≠ VDAB; RA outturn still FOI,4,9.5,7,7.0,'
        f'Publish RA 2024-25; end-receiver L5 APE,seed,,tick162'
    ),
]
append_if_missing(DATA / "leaderboard.csv", lbs)

# programmes
progs = [
    f"forem_prog130_2026,forem,,FOREM-130,FOREM programme 130 consolidated 2026,10.5,2026,{TOTAL},src_wal_ep_jeholet_2026,strong,Wallonie>FOREM,Rationalised single programme initial 2026",
    f"forem_ape_2026,forem,forem_prog130_2026,FOREM-APE,APE employment promotion device,10.5,2026,{L5['ape']},src_wal_ep_jeholet_2026,strong,Wallonie>FOREM>APE,Largest L5 block 45pct of prog",
    f"forem_titres_2026,forem,forem_prog130_2026,FOREM-TS,Titres-services subsidies,10.5,2026,{L5['titres_services']},src_wal_ep_jeholet_2026,strong,Wallonie>FOREM>titres,20pct of prog",
    f"forem_ops_2026,forem,forem_prog130_2026,FOREM-OPS,Fonctionnement FOREM,10.5,2026,{L5['fonctionnement_forem']},src_wal_ep_jeholet_2026,strong,Wallonie>FOREM>ops,15pct of prog; contrat gestion",
]
append_if_missing(DATA / "programmes.csv", progs)

# FOI residual update
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_forem_budget,",
    "gap_forem_budget,Wallonie>Emploi>Forem,forem,"
    "FOREM institutional RA/outturn 2024-2025 same structure as 2023 (aides vs fonctionnement FTE); "
    "2026 budget L5 now public via EP prog 130; residual: cash outturn vs budget and end-receiver APE top,"
    "2023 RA + 2026 budget L5 filled strong; 2024-25 institutional outturn still missing,"
    "5,SPW / Forem,,,docs/doge/foi/drafts/gap_forem_budget.md,ready,2026-07-19,,,,,"
    f"cmt_forem_budget_2023|cmt_forem_prog130_2026,,2026-07-19T19:00:00Z,{UTC},"
    "tick132 RA2023 |tick162: EP2026 L5 full; residual RA2024-25 + APE beneficiary L5 human send",
)

# research queue
replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_157,",
    f"rq_157,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    f"\"Prefer public primary fills for ready FOI topics (FOREM 2024-26 RA De Lijn full 2025-26 perimeter Antwerp register "
    f"univ per-institution VIPA named Mons BI2026) if new PDFs appear; else next highest open rq; do not idle while public work remains.\","
    f"gap_forem_budget,{UTC},{UTC},"
    f"\"tick162: FOREM EP Jeholet prog130 L5 2.834bn APE 1.279bn titres 568m fonct 420m; residual RA2024-25 FOI; spawn rq_158\"",
)
rq_158 = (
    f"rq_158,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    f"\"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register univ per-institution VIPA Mons BI2026 "
    f"bpost USO HR Rail) if new PDFs appear; else next open rq; do not idle while public work remains.\","
    f",{UTC},,"
    f"\"Spawned tick162 after FOREM L5; rq_116 SWA deferred Oct-Dec 2026\""
)
append_if_missing(DATA / "research_queue.csv", [rq_158])

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{UNIT},162,no,"
    "\"Scheduler 60s. Next prio5 rq_158 hole-fill De Lijn/Antwerp/univ; rq_116 SWA deferred. "
    "FOI ready human send. tick162 FOREM prog130 L5.\"\n",
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log = read_text(log_path)
entry = f"""
### {UTC} — tick 162
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **FOREM Wallonie budget 2026 programme 130 L5**)
- Found (strong primary EP Jeholet DO18, kEUR table eng=liq):
  - **Total prog 130: EUR 2.833619bn** (sum of 20 AB lines; matches ExpGen 18.130).
  - **APE 1.279bn** (45%) · **titres-services 568.4m** · **fonctionnement FOREM 419.7m** · SESAM **106.9m** · ONSS draw **136.8m** · CISP **104.3m** · activation **76.2m**.
  - 2025 legacy: prog12 **370.1m** · titres **567.6m** · formation prog22 **344.6m** (folded into 130 in 2026).
  - Dual PES: pure ops ~420m vs VDAB VL krediet ~0.75bn; total 2.83bn is aids-heavy (not apples-to-apples).
  - FOREM RA 2024-25 still not public this tick.
- Wrote: sources 1; budgets ~18; cmt 1; lb 4; programmes 4; gap_forem notes partial; rq_157=done; seeded **rq_158**.
- FOI: gap_forem residual RA2024-25 + APE beneficiary L5 still **ready** human send.
- Next: prio5 **rq_158**; deferred **rq_116** SWA.
"""
if "tick 162" not in log[-2500:]:
    write_text(log_path, log.rstrip() + "\n" + entry)

print("tick162 OK total", TOTAL)

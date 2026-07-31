# -*- coding: utf-8 -*-
"""Tick 675: federal CoA BA2026 SS RIZIV 43.9bn + arbeidsongeschiktheid residual dual — rq_666."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T10:30:00Z"
TICK = 675
RQ = "rq_666"
NEXT_RQ = "rq_667"
GAP = "gap_fed_aju2026_ss_riziv_ao_l5"
SRC = "src_ccrek_fed_aju2026_ss_riziv_ao"
SRC_DUAL = "src_dual_ss_riziv_ao_tick675"


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


def append_rows(path: Path, rows: list[str]) -> int:
    text = read_text(path)
    existing = text
    added = 0
    for row in rows:
        key = row.split(",", 1)[0]
        if key and any(
            L.startswith(key + ",") or L.startswith("\ufeff" + key + ",")
            for L in existing.splitlines()
        ):
            print(f"SKIP exists {key}")
            continue
        if not text.endswith("\n"):
            text += "\n"
        text += row + "\n"
        existing = text
        added += 1
        print(f"ADD {key}")
    path.write_bytes(text.encode("utf-8"))
    return added


def update_rq_done(path: Path, rq_id: str, notes: str) -> None:
    text = read_text(path)
    lines = text.splitlines()
    out = []
    for L in lines:
        if L.startswith(rq_id + ",") or L.startswith("\ufeff" + rq_id + ","):
            parts = L.split(",")
            if len(parts) >= 5:
                parts[4] = "done"
            if len(parts) >= 11:
                parts[10] = NOW
            if len(parts) >= 12:
                parts[11] = notes.replace(",", ";")
            else:
                parts.append(notes.replace(",", ";"))
            L = ",".join(parts)
            print(f"RQ done {rq_id}")
        out.append(L)
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


def spawn_rq(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    if any(L.startswith(key + ",") for L in text.splitlines()):
        print(f"SKIP spawn {key}")
        return
    if not text.endswith("\n"):
        text += "\n"
    text += row + "\n"
    path.write_bytes(text.encode("utf-8"))
    print(f"SPAWN {key}")


def set_loop_state(path: Path) -> None:
    header = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes"
    notes = (
        f"tick{TICK} SS exp 148.0bn RIZIV care 43.9bn AO save slip dual; "
        f"next {NEXT_RQ}; progress@680 in 5; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


def update_foi(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    lines = text.splitlines()
    out = []
    found = False
    for L in lines:
        if L.startswith(key + ",") or L.startswith("\ufeff" + key + ","):
            out.append(row)
            found = True
            print(f"FOI update {key}")
        else:
            out.append(L)
    if not found:
        out.append(row)
        print(f"FOI add {key}")
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


ent_rows = []  # riziv, sec_ss already exist

src_rows = [
    f"{SRC},CoA federal BA2026 SS exp table RIZIV care 43.9bn AO measures dual,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,Cour des comptes / Rekenhof,2026-08-01,audit,"
    "Strong tick675: SS total exp BC 148026.6 path +168.1; prestaties 137624.3 +2132; GB emp 63267.1 pens emp 43036.6 AO emp 14839.4 unemp 4836.4 +198.5; GB self 6945.3; care 43857.4 +2560.2 (doel 44103.5 +2806.3 hospital into doel; nonuse 246.1); gov pens 22526.8 -300.7; beheer 3006.8; other exp 7395.5 -1974.4; RIZIV save miss 183.1 of 801.4 (pharma 145.7); AO measures impact 2026 -129.3 path 2029 -323.4; versterkte opvolging -110.2 excl 4197; solid 98.4 -24; maatwerk -3.5; ziektepens RIZIV 9.3; responsab 137 (mutual 77 worker 10 doc 50); unemp to ZIV +44.1; pension reform save 2212 by 2030",
    f"{SRC_DUAL},Dual SS RIZIV care AO vs VL WVG WAL AViQ dual,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,DOGE synthesis CoA SS dual Entity II,2026-08-01,synthesis,"
    "Strong dual: RIZIV care 43.9bn dual AViQ/WVG; AO 14.8bn dual; unemp 4.84bn dual; not TE-additive; tick675",
]

bud_rows = [
    # SS total table
    f"bud_ss_total_exp_bc2026,sec_ss,2026,148026600000,,,budgeted,{SRC},strong,SS consolidated exp BC2026 148026.6m path +168.1 (+0.1pct) vs IB; tick675",
    f"bud_ss_total_exp_ib2026,sec_ss,2026,147858500000,,,budgeted,{SRC},strong,SS total exp IB2026 147858.5m; tick675",
    f"bud_ss_prestaties_bc2026,sec_ss,2026,137624300000,,,budgeted,{SRC},strong,Sociale prestaties BC 137624.3m path +2132.0 (+1.6pct); tick675",
    f"bud_ss_gb_werknemers_bc2026,sec_ss,2026,63267100000,,,budgeted,{SRC},strong,Globaal Beheer werknemers BC 63267.1m path -74.9; tick675",
    f"bud_ss_pens_werknemers_bc2026,sec_ss,2026,43036600000,,,budgeted,{SRC},strong,Pensioenen werknemers BC 43036.6m path -234.1; tick675",
    f"bud_ss_ao_werknemers_bc2026,sec_ss,2026,14839400000,,,budgeted,{SRC},strong,Arbeidsongeschiktheid werknemers BC 14839.4m path -40.0; tick675",
    f"bud_ss_werkloosheid_bc2026,sec_ss,2026,4836400000,,,budgeted,{SRC},strong,Werkloosheid BC 4836.4m path +198.5 (+4.3pct); tick675",
    f"bud_ss_gb_zelfstandigen_bc2026,sec_ss,2026,6945300000,,,budgeted,{SRC},strong,Globaal Beheer zelfstandigen BC 6945.3m path -66.8; tick675",
    f"bud_ss_pens_zelfstandigen_bc2026,sec_ss,2026,5857300000,,,budgeted,{SRC},strong,Pensioenen zelfstandigen BC 5857.3m path -62.6; tick675",
    f"bud_ss_ao_zelfstandigen_bc2026,sec_ss,2026,1064600000,,,budgeted,{SRC},strong,AO zelfstandigen BC 1064.6m path -5.4; tick675",
    f"bud_ss_geneeskundige_verzorging_bc2026,riziv,2026,43857400000,,,budgeted,{SRC},strong,Geneeskundige verzorging BC 43857.4m path +2560.2 (+6.2pct); dual AViQ/WVG; tick675",
    f"bud_ss_overheidspensioenen_bc2026,sec_ss,2026,22526800000,,,budgeted,{SRC},strong,Overheidspensioenen BC 22526.8m path -300.7; tick675",
    f"bud_ss_beheer_kosten_bc2026,sec_ss,2026,3006800000,,,budgeted,{SRC},strong,Beheer- en betalingskosten BC 3006.8m path +10.5; tick675",
    f"bud_ss_andere_uitgaven_bc2026,sec_ss,2026,7395500000,,,budgeted,{SRC},strong,Andere uitgaven BC 7395.5m path -1974.4 (-21.1pct); tick675",
    f"bud_ss_prestaties_2025_prov,sec_ss,2025,132212000000,,,outturn,{SRC},strong,Sociale prestaties 2025 provisional 132212.0m; tick675",
    # RIZIV care residual
    f"bud_riziv_doelstelling_bc2026,riziv,2026,44103500000,,,budgeted,{SRC},strong,RIZIV begrotingsdoelstelling BC 44103.5m path +2806.3 (hospital state share into doel); tick675",
    f"bud_riziv_hospital_into_doel_2806m,riziv,2026,2806300000,,,budgeted,{SRC},strong,Staatsgedeelte ziekenhuisfinanciering 2806.3m moved into care doelstelling from transfers 2026; tick675",
    f"bud_riziv_niet_aanwendbaar_246_1m,riziv,2026,246100000,,,budgeted,{SRC},strong,Niet-aanwendbaar binnen doelstelling 246.1m path +4.6 (was NAP-AMR now FOD VG direct); tick675",
    f"bud_riziv_save_package_ib_801_4m,riziv,2026,801400000,,,budgeted,{SRC},strong,RIZIV save package IB2026 801.4m; tick675",
    f"bud_riziv_save_miss_183_1m_bc,riziv,2026,183100000,,,budgeted,{SRC},strong,RIZIV of 801.4 save 183.1m not realized 2026 BC (pharma 145.7; klin bio -11.2 imaging -23.6 lower); tick675",
    f"bud_riziv_pharma_save_miss_145_7m,riziv,2026,145700000,,,budgeted,{SRC},strong,Geneesmiddelen save measures not yet designed 145.7m of miss; tick675",
    # AO measures
    f"bud_ao_measures_impact_2026_minus_129_3m,riziv,2026,-129300000,,,budgeted,{SRC},strong,AO measures re-estimate total budget impact 2026 -129.3m vs IB; tick675",
    f"bud_ao_measures_impact_2029_minus_323_4m,riziv,2029,-323400000,,,budgeted,{SRC},strong,AO measures cum impact 2029 -323.4m (less save / less revenue); tick675",
    f"bud_ao_versterkte_opvolging_save_slip_110_2m,riziv,2026,-110200000,,,budgeted,{SRC},strong,Versterkte opvolging AO save slip -110.2m 2026 (emp 103.3 self 6.9); 4 months not full year; tick675",
    f"bud_ao_versterkte_opvolging_excl_4197,riziv,2026,4197,,,budgeted,{SRC},strong,Excluded invalidity persons 4197 (7667 emp + 526 self) vs prior higher plan -8193 delta; tick675",
    f"bud_ao_versterkte_opvolging_path_2029_minus_197m,riziv,2029,-197100000,,,budgeted,{SRC},strong,Versterkte opvolging save path 2029 -197.1m vs IB; start planned 1Sep2026; tick675",
    f"bud_ao_hercontrole_path_2029_minus_46_6m,riziv,2029,-46600000,,,budgeted,{SRC},strong,Hercontrole/thematische overestimate fix path -46.6m 2029; tick675",
    f"bud_ao_solidariteit_contrib_98_4m_2026,sec_ss,2026,98400000,,,budgeted,{SRC},strong,Solidariteitsbijdrage employers >50 FTE months 2-3 AO: 98.4m 2026 path -24 vs IB; tick675",
    f"bud_ao_solidariteit_m4_5_yield_53m_2027,sec_ss,2027,53000000,,,budgeted,{SRC},strong,Solidarity months 4-5 from 2027 yield 53m (path -19 vs plan; offsets SSC cut); law not ready; tick675",
    f"bud_ao_maatwerk_save_slip_3_5m,riziv,2026,-3500000,,,budgeted,{SRC},strong,Maatwerk cumulatie measure delay to 1Jul2026: -3.5m 2026; cum 2029 -3.9; tick675",
    f"bud_ao_ziektepensioen_riziv_exp_9_3m,riziv,2026,9300000,,,budgeted,{SRC},strong,Ziektepensioen transition RIZIV exp BC 9.3m (path -7.7 vs IB; actual start 1Jul overstates); tick675",
    f"bud_ao_responsab_total_137m_2026,riziv,2026,137000000,,,budgeted,{SRC},strong,Responsabilisering mutualities+workers+doctors 137.0m 2026 path 398 2029; tick675",
    f"bud_ao_responsab_mutual_77m,riziv,2026,77000000,,,budgeted,{SRC},strong,Responsabilisering ziekenfondsen 77m 2026 path 248 2029; tick675",
    f"bud_ao_responsab_workers_10m,riziv,2026,10000000,,,budgeted,{SRC},strong,Responsabilisering werknemers 10m 2026 path 25 2029; tick675",
    f"bud_ao_responsab_doctors_50m,riziv,2026,50000000,,,budgeted,{SRC},strong,Responsabilisering artsen 50m 2026 (law incomplete - full save at risk); path 125 2029; tick675",
    f"bud_ao_unemp_inflow_ziv_44_1m_2026,riziv,2026,44100000,,,budgeted,{SRC},strong,RIZIV: 5000/yr unemp-loss inflow to ZIV cost 44.1m 2026 path ~97.5 2029; RVA monitoring mild so far; tick675",
    f"bud_ao_prestaties_path_minus_45_3m,riziv,2026,-45300000,,,budgeted,{SRC},strong,AO prestaties total path -45.3m vs IB (emp -40 self -5.3) from fewer primary days; tick675",
    # Pension multi-year save path residual
    f"bud_pens_reform_save_path_2030_2212m,fpd_pensioenen,2030,2212000000,,,budgeted,{SRC},strong,Pension reform laws package save path 2212m by 2030 (IB 2229); tick675",
    f"bud_pens_gelijkstelling_save_2027_7m,fpd_pensioenen,2027,7000000,,,budgeted,{SRC},strong,Gelijkgestelde perioden limit save 7m 2027 (IB 12; older plan 48); 2030 69; tick675",
    # Dual
    f"bud_dual_riziv_care_43_9bn_2026,gg_belgium,2026,43857400000,,,budgeted,{SRC_DUAL},strong,Dual RIZIV care 43.86bn vs VL WVG WZC 2.74 + WAL AViQ 7+ class (not sum); tick675",
    f"bud_dual_ao_14_8bn_2026,gg_belgium,2026,14839400000,,,budgeted,{SRC_DUAL},strong,Dual AO werknemers 14.84bn residual reform slip; tick675",
]

cmt_rows = [
    f"cmt_ss_exp_148bn_bc2026,SS total exp 148.0bn BC dual,sec_ss,SS consolidated,CoA 2026_22 III.II.1,2026-05-21,2026,2026,148026600000,\"{{\"\"2026\"\":148026600000}}\",,active,,SS map dual,Spilindex not updated,{SRC},strong,SS>exp>BC2026,tick675",
    f"cmt_riziv_care_43_9bn_hospital_shift,RIZIV care 43.9bn hospital into doel dual,riziv,RIZIV-GV,CoA 2026_22 III.II.3,2026-05-21,2026,2026,43857400000,\"{{\"\"2026\"\":43857400000}}\",,active,,Care dual AViQ,Save miss 183m,{SRC},strong,SS>RIZIV>care,tick675",
    f"cmt_ao_save_slip_129m_2026,AO measures save slip -129m 2026 dual,riziv,RIZIV AO,CoA 2026_22 III.II.4,2026-05-21,2026,2029,129300000,\"{{\"\"2026\"\":129300000,\"\"2029\"\":323400000}}\",,active,,Invalidity reform dual,Sep2026 start risk,{SRC},strong,SS>AO>measures,tick675",
    f"cmt_ao_responsab_137m,AO responsabilisering 137m dual mutualities,riziv,mutualities+doctors,CoA 2026_22,2026-05-21,2026,2029,137000000,\"{{\"\"2026\"\":137000000,\"\"2029\"\":398000000}}\",,active,,Governance dual,Doctors law incomplete,{SRC},strong,SS>AO>responsab,tick675",
    f"cmt_dual_ss_riziv_tick675,Dual SS RIZIV AO vs Entity II care,gg_belgium,SS+E2 dual,CoA SS dual,2026-05-21,2026,2026,43857400000,\"{{\"\"2026\"\":43857400000}}\",,active,,Dual care residual,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>ss_riziv,tick675",
    f"cmt_unemp_inflow_ziv_44m,Unemp to ZIV inflow 44.1m dual RVA,riziv,RIZIV+RVA,CoA 2026_22 4.3,2026-05-21,2026,2029,44100000,\"{{\"\"2026\"\":44100000}}\",,active,,Spillover dual,Monitor FOI,{SRC},strong,SS>unemp>ZIV,tick675",
]

lb_rows = [
    f"lb_ss_exp_148bn_2026,SS consolidated exp 148.0bn,Federal,ops,SS>total,148026600000,0,Strong CoA table BC; prestaties 137.6bn; dual Entity II,strong,{SRC},SS recipients,SS total dual,Primary,5.0,9.5,3,6.95,Publish spilindex update,open,,tick675",
    f"lb_riziv_care_43_9bn_2026,RIZIV geneeskundige verzorging 43.86bn,Federal,ops,SS>RIZIV>care,43857400000,0,Strong CoA +2.56bn; hospital 2.81bn into doel; dual AViQ/WVG,strong,{SRC},patients,Care dual,Primary,5.5,9.5,3,7.15,L5 pharma save FOI,open,,tick675",
    f"lb_riziv_save_miss_183m_2026,RIZIV save miss 183m of 801m,Federal,ops,SS>RIZIV>saves,183100000,0,Strong CoA: pharma 146m measures not designed; dual waste,strong,{SRC},pharma,Save opacity,Primary,8.0,6.5,2,6.85,Deliver compensating measures,open,,tick675",
    f"lb_ao_save_slip_129m_2026,AO reform save slip -129m 2026,Federal,ops,SS>AO>reform,129300000,0,Strong CoA: versterkte opvolging -110; path 2029 -323; dual invalidity,strong,{SRC},invalidity recipients,Reform delivery,Primary,7.5,6.5,3,6.65,Law+doctor protocol FOI,open,,tick675",
    f"lb_ss_unemp_4_84bn_2026,SS werkloosheid 4.84bn path +198m,Federal,ops,SS>werkloosheid,4836400000,0,Strong CoA +4.3pct; dual RVA reform residual,strong,{SRC},unemployed,Unemp dual,Primary,5.5,8.5,3,6.55,Unit cost FOI,open,,tick675",
    f"lb_dual_ss_riziv_2026,Dual SS RIZIV 43.9bn vs E2 care,Belgium,ops,Belgium>dual>ss_riziv,43857400000,0,Strong dual: care+AO+unemp vs VL WVG WAL AViQ; not TE-additive,strong,{SRC_DUAL},all entities,SS dual residual,Primary dual,6.0,9.0,3,7.05,Cross FOI,open,,tick675",
]

foi_row = (
    f"{GAP},Federal>Aju2026>SS_RIZIV_AO_L5,sec_ss,"
    "RIZIV care 43.9bn L5 top lines + pharma 145.7 save design; AO versterkte opvolging protocol 1Sep2026; responsabilisering artsen law; solidariteitsbijdrage Q timing; unemp-to-ZIV monthly series; spilindex Jun impact on SS exp,"
    "CoA fed BA2026 SS RIZIV AO strong tick675; L5 dual,"
    f"5,FOD Sociale Zekerheid / RIZIV / RVA / openbaarheid,openbaarheid@socialsecurity.fgov.be,https://socialsecurity.belgium.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_riziv_care_43_9bn_hospital_shift|cmt_ao_save_slip_129m_2026|cmt_ss_exp_148bn_bc2026,"
    f"lb_riziv_care_43_9bn_2026|lb_riziv_save_miss_183m_2026|lb_ao_save_slip_129m_2026,"
    f"{NOW},{NOW},tick675 CoA fed SS primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22) Deel III

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: FOD Sociale Zekerheid / RIZIV / RVA
openbaarheid@socialsecurity.fgov.be

Betreft: Openbaarheid — aju 2026 sociale zekerheid (RIZIV 43,9 mrd + AO-maatregelen) L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. RIZIV geneeskundige verzorging 43.857,4 mEUR: top 20 uitgavenlijnen en
   detail niet-aanwendbaar 246,1 mEUR.
2. Besparingspakket 801,4 mEUR: status van 183,1 mEUR niet-gerealiseerd
   (geneesmiddelen 145,7 mEUR) en compenserende maatregelen na juni 2026.
3. Versterkte opvolging AO: protocol met artsen, startdatum 1/09/2026, en
   herziening besparing -110,2 mEUR (4.197 uitsluitingen).
4. Responsabilisering artsen 50 mEUR: wettekststatus en kaspad 2026.
5. Solidariteitsbijdrage 98,4 mEUR: inningskalender RSZ Q4 2026.
6. Instroom werkloosheid->ZIV: maandreeksen 2025-2026 (5.000/jr hypothese).
7. Impact junispilindex op SS-uitgaven (niet in BC-parameters).

Période: 2025-01-01 tot 2029-12-31.
Vorm: CSV/XLSX bij voorkeur.

Met vriendelijke groet,
[Naam]
```

## Notes agent
- Primary: CoA 2026_22 Deel III tick675.
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **federal CoA BA2026 SS RIZIV care 43.9bn + AO measures dual**)
- Found (primary CoA 2026_22): **SS total exp EUR148.027bn** path **+168m**; prestaties **137.624** (+2132). Matrix: pens emp **43.037** AO emp **14.839** unemp **4.836** (+198.5) care **43.857** (+2560) gov pens **22.527** beheer **3.007**. **RIZIV:** doel **44.104** (hospital **+2806** into doel); nonuse **246.1**; save miss **183.1**/801.4 (pharma **145.7**). **AO measures** impact **2026 -129.3** path **2029 -323.4**; versterkte opvolging **-110.2** excl **4197**; solid **98.4**; responsab **137** (mutual 77/doc 50); unemp->ZIV **+44.1**. Dual AViQ/WVG. Strong CoA; L5 FOI.
- Wrote: budgets (+40); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@680 in 5 ticks; rq_116 deferred
"""


def main() -> None:
    n_ent = append_rows(ROOT / "entities.csv", ent_rows) if ent_rows else 0
    n_src = append_rows(ROOT / "sources.csv", src_rows)
    n_bud = append_rows(ROOT / "budgets.csv", bud_rows)
    n_cmt = append_rows(ROOT / "commitments.csv", cmt_rows)
    n_lb = append_rows(ROOT / "leaderboard.csv", lb_rows)
    update_foi(ROOT / "foi_queue.csv", foi_row)
    draft_path = FOI_DRAFTS / f"{GAP}.md"
    draft_path.write_bytes(foi_draft.encode("utf-8"))
    print(f"DRAFT {draft_path}")

    update_rq_done(
        ROOT / "research_queue.csv",
        RQ,
        f"tick{TICK} SS 148bn RIZIV care 43.9bn AO save slip -129m dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,sec_ss,"
        f"Next residual: fed CoA energy ch4 dual or SS receipts residual or VL BA fonds residual.,,"
        f"{NOW},,spawned tick{TICK} after {RQ}",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log = read_text(LOG)
    if f"tick {TICK}" not in log[-2500:]:
        if not log.endswith("\n"):
            log += "\n"
        log += log_entry
        LOG.write_bytes(log.encode("utf-8"))
        print("LOG appended")
    else:
        print("LOG skip duplicate")

    print(f"DONE tick{TICK}: ent={n_ent} src={n_src} bud={n_bud} cmt={n_cmt} lb={n_lb}")


if __name__ == "__main__":
    main()

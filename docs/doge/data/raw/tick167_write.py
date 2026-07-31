# -*- coding: utf-8 -*-
"""Tick 167: VIPA 2026 envelope + De Lijn MJR path (BO2026 official)."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T05:45:00Z"
TICK = 167
UNIT = "rq_162"


def append_lines(path: Path, lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def replace_line_startswith(path: Path, prefix: str, new_line: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    found = False
    for line in lines:
        if line.startswith(prefix):
            out.append(new_line if new_line.endswith("\n") else new_line + "\n")
            found = True
        else:
            out.append(line)
    if not found:
        raise SystemExit(f"prefix not found: {prefix}")
    path.write_text("".join(out), encoding="utf-8", newline="\n")


append_lines(
    DATA / "sources.csv",
    [
        "src_vl_mjr_2025_2030,Vlaanderen Meerjarenraming 2025-2030 BO2026 context,"
        "https://themis.vlaanderen.be/files/fc642160-b09d-11f0-9b44-3797f8128cc9/download,"
        "Departement FB Vlaanderen,2026-07-28,budget,"
        '"De Lijn ESR-ontvangsten 264.3m BA2025 / 313.8m BO2026 / constant 263.8m; e-bus VAK +400m; OV savings path -50/-125m; '
        'VIPA strategisch forfait path +97.7m to 2030; instandhouding +35.7m; tick167"',
        "src_vl_parl_wvg_vipa_2026,Vlaams Parlement commissie WVG VIPA/zorginfrastructuur BO2026 (Gennez),"
        "https://docs.vlaamsparlement.be/files/pfile?id=2248413,"
        "Vlaams Parlement / minister Gennez,2026-07-28,official_parliament,"
        '"VIPA total 180m 2026 no +20m expansion path to 295m 2029; hosp forfait 77.3m 2025 to 89.6m 2026; '
        'ouderen ~40m; handicap auth 16.8m; instandhouding +27.2m; classic VEK underfund; tick167"',
        "src_vl_begroting_publicatie_2026,Vlaamse begroting 2026 publicatie samenvatting tables,"
        "https://publicaties.vlaanderen.be/view-file/77922,"
        "Vlaamse overheid,2026-07-28,budget,"
        '"VIPA instandhoudingsforfait 27.692m; De Lijn VEK actualisatie -61.325m; MOW De Lijn 30m measure; tick167"',
    ],
)

# --- budgets VIPA ---
append_lines(
    DATA / "budgets.csv",
    [
        "bud_vipa_total_envelope_2026,vipa,2026,180000000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "VIPA total krediet envelope 180m 2026 (no +20m expansion; minister Gennez)",
        "bud_vipa_total_path_2029,vipa,2029,295000000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "VIPA envelope path to 295m 2029 for investment calendar",
        "bud_vipa_hosp_forfait_2025,vipa,2025,77300000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "VIPA ziekenhuizen forfait (strategisch class) 77.3m 2025",
        "bud_vipa_hosp_forfait_2026,vipa,2026,89600000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "VIPA ziekenhuizen forfait 89.6m 2026 (in-use dependent; +14.5m room new awards)",
        "bud_vipa_hosp_new_awards_room_2026,vipa,2026,14500000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "Remaining room new hospital forfait awards 14.5m 2026",
        "bud_vipa_ouderen_forfait_2025,vipa,2025,35000000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "VIPA forfait ouderen 35m 2025",
        "bud_vipa_ouderen_forfait_2026,vipa,2026,40000000,,,budgeted,src_vl_parl_wvg_vipa_2026,medium,"
        "VIPA forfait ouderen almost 40m 2026 (minister almost 40m)",
        "bud_vipa_handicap_auth_2026,vipa,2026,16800000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "VIPA handicap forfait machtiging 16.8m 2026",
        "bud_vipa_instandhouding_delta_2026,vipa,2026,27200000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "Instandhoudingsforfait +27.2m 2026 (commissie; table 27.692m class)",
        "bud_vipa_instandhouding_table_2026,vipa,2026,27692000,,,budgeted,src_vl_begroting_publicatie_2026,strong,"
        "VIPA Instandhoudingsforfait 27.692m BO2026 publication table",
        "bud_vipa_ziekenhuis_fin_delta_2026,vipa,2026,6600000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "Ziekenhuisfinanciering +6.6m 2026 commissie",
        "bud_vipa_expansion_cut_2026,vipa,2026,20000000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "VIPA uitbreidingsbeleid cut -20m 2026 (klassiek+zorgforfait)",
        "bud_vipa_classic_vek_budgeted_2026,vipa,2026,33000000,,,budgeted,src_vl_parl_wvg_vipa_2026,medium,"
        "Classic VIPA VEK only 33m 2026 vs VIPA need claim 68.2m (underfund narrative)",
        "bud_vipa_kinderopvang_shift_2026,vipa,2026,60000000,,,budgeted,src_vl_parl_wvg_vipa_2026,strong,"
        "One-off 60m VIPA shift kinderopvang infrastructuur compensation class 2026",
        "bud_vipa_kinderopvang_awards_2025,vipa,2025,16500000,,,outturn,src_vl_parl_wvg_vipa_2026,strong,"
        "Kinderopvang infrastructure awards 16.5m 2025",
        # De Lijn
        "bud_de_lijn_esr_receipts_ba2025,de_lijn,2025,264262000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "De Lijn ESR-ontvangsten (own revenue tickets etc) 264.262m BA2025 - NOT Vlaamse toelage",
        "bud_de_lijn_esr_receipts_bo2026,de_lijn,2026,313813000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "De Lijn ESR-ontvangsten 313.813m BO2026 Algemene Toelichting (incl measures)",
        "bud_de_lijn_esr_receipts_const_2026,de_lijn,2026,263813000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "De Lijn ESR-ontvangsten constant beleid 263.813m 2026",
        "bud_de_lijn_esr_receipts_2030,de_lijn,2030,250913000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "De Lijn ESR-ontvangsten path 250.913m 2030 constant",
        "bud_de_lijn_ebus_vak_extra_2026,de_lijn,2026,400000000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "Extra investeringen De Lijn e-bus class VAK +400m path 2026-2030 vs 2025",
        "bud_de_lijn_ov_savings_2026,de_lijn,2026,50000000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "Openbaar vervoer De Lijn & VoM savings path -50m 2026 (vs 2025)",
        "bud_de_lijn_ov_savings_2029,de_lijn,2029,125000000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "OV De Lijn & VoM savings path -125m 2029-2030",
        "bud_de_lijn_mow_punctual_save_2026,de_lijn,2026,30000000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "MOW punctual measure De Lijn 30m/yr 2026-2030 (hervormingen table)",
        "bud_de_lijn_vek_peak_2027,de_lijn,2027,145400000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "De Lijn ESR-VEK peak +145.4m 2027 (e-bus delivery calendar)",
        "bud_de_lijn_vek_peak_2028,de_lijn,2028,59100000,,,budgeted,src_vl_mjr_2025_2030,strong,"
        "De Lijn ESR-VEK +59.1m 2028 vs path",
        "bud_de_lijn_vek_actualisatie_2026,de_lijn,2026,-61325000,,,budgeted,src_vl_begroting_publicatie_2026,strong,"
        "De Lijn Actualisatie VEK-kalender -61.325m BO2026 publication",
    ],
)

append_lines(
    DATA / "commitments.csv",
    [
        'cmt_vipa_envelope_2026_29,VIPA zorginfrastructuur multi-year envelope and forfaits 2025-2029,vipa,'
        "Flemish hospitals WZC handicap providers,VIPA / Departement Zorg BO2026 + commissie Gennez,"
        "2025-01-01,2025,2029,295000000,"
        '"{""2026_total"":180000000,""2029_total"":295000000,""2025_hosp_forfait"":77300000,""2026_hosp_forfait"":89600000,'
        '""2026_hosp_new_room"":14500000,""2025_ouderen"":35000000,""2026_ouderen_class"":40000000,'
        '""2026_handicap_auth"":16800000,""2026_instandhouding_delta"":27200000,""2026_instandhouding_table"":27692000,'
        '""2026_expansion_cut"":20000000,""2026_classic_vek_budgeted"":33000000,""2026_kinderopvang_shift"":60000000,'
        '""note"":""named L5 beneficiaries still FOI; Jessa 500m multi-year already mapped; NBB D.92 192-280m cash class""}",'
        "0,active,https://docs.vlaamsparlement.be/files/pfile?id=2248413,"
        "Care infrastructure subsidies Flanders,"
        "Publish named top awards; close underfund VEK gap; reform forfaits,"
        "src_vl_parl_wvg_vipa_2026,strong,Vlaanderen>VIPA,"
        "tick167 partial close gap_vipa_named_l5 envelopes; residual names FOI",
        'cmt_de_lijn_mjr_path_2026_30,De Lijn BO2026 multi-year path own receipts invest savings,de_lijn,'
        "VVM De Lijn passengers Flanders,ODC + BO2026 MJR + punctual measures,"
        "2025-01-01,2025,2030,400000000,"
        '"{""esr_receipts_ba2025"":264262000,""esr_receipts_bo2026"":313813000,""esr_receipts_const2026"":263813000,'
        '""esr_receipts_2030"":250913000,""ebus_vak_extra"":400000000,""ov_save_2026"":50000000,""ov_save_2029"":125000000,'
        '""mow_punctual_30m"":30000000,""vek_peak_2027"":145400000,""vek_peak_2028"":59100000,""vek_actualisatie_2026"":-61325000,'
        '""note"":""ESR-ontvangsten are own revenue NOT Vlaamse toelage; full exp+inv toelage perimeter still FOI gap_de_lijn""}",'
        "0,active,https://themis.vlaanderen.be/files/fc642160-b09d-11f0-9b44-3797f8128cc9/download,"
        "Flanders bus tram public service multi-year,"
        "Publish full 2025-26 exp+inv toelage comparable PQ955; deliver e-bus VEK peaks,"
        "src_vl_mjr_2025_2030,strong,Vlaanderen>MOW>De_Lijn,"
        "tick167 path fill; residual full toelage FOI",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_vipa_envelope_180m,VIPA total envelope 180m 2026 path 295m 2029,Flanders,ops,"
        "Vlaanderen>VIPA>envelope,180000000,295000000,"
        "Strong parliament+MJR: 180m 2026 no expansion; path 295m 2029; dual NBB D.92 cash 192-280m hospitals,"
        "strong,src_vl_parl_wvg_vipa_2026,Care providers patients VL,"
        "Care infrastructure public subsidies,"
        "Core infra not pure waste; classic VEK underfund vs need; named L5 thin,"
        "5,9.0,7,7.0,"
        "Open named awards; match VEK to encours; reform forfaits to build costs,"
        "seed,,tick167",
        "lb_vipa_hosp_forfait,VIPA hospital strategisch forfait 77-90m/yr,Flanders,ops,"
        "Vlaanderen>VIPA>ziekenhuizen_forfait,77300000,89600000,"
        "Strong: 77.3m 2025 / 89.6m 2026; +14.5m new room; Jessa package separate multi-year,"
        "strong,src_vl_parl_wvg_vipa_2026,Flemish hospitals,"
        "Hospital infrastructure annual forfait,"
        "Core health infra; coverage only ~20-64pct build costs sector claim,"
        "4,8.5,6,6.2,"
        "Publish per-hospital forfait list; reconcile NBB D.92,"
        "seed,,tick167",
        "lb_de_lijn_ebus_400m_path,De Lijn e-bus invest path +400m VAK 2026-30,Flanders,ops,"
        "Vlaanderen>MOW>De_Lijn>ebus,400000000,400000000,"
        "Strong MJR extra investeringen table; VEK peaks 145m 2027 / 59m 2028; dual savings -50 to -125m OV,"
        "strong,src_vl_mjr_2025_2030,Flanders passengers,"
        "Zero-emission bus fleet,"
        "Capex not pure waste; full toelage perimeter still partial FOI,"
        "4,9.0,6,6.5,"
        "Deliver VEK peaks; publish full exp+inv toelage 2025-26,"
        "seed,,tick167",
    ],
)

# FOI updates
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_vipa_named_l5,",
    "gap_vipa_named_l5,Vlaanderen>VIPA>ziekenhuizen>named_L5,vipa,"
    "Named VIPA hospital awards 2023-2026 with envelopes cash-by-year and BBT codes; reconcile NBB D.92 192-280m; "
    "Jessa 500m payment calendar; list of 14.5m new 2026 room awardees,"
    "Envelope totals+forfaits 77.3/89.6m strong tick167; bulk named top-10 still thin,"
    "6,Departement Zorg VIPA / Team Openbaarheid,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
    "docs/doge/foi/drafts/gap_vipa_named_l5.md,ready,2026-07-27,,,,,"
    "cmt_vipa_envelope_2026_29|cmt_vipa_hospitals_d92,lb_vipa_envelope_180m,"
    "2026-07-27T22:50:00Z,2026-07-28T05:45:00Z,"
    "tick148 partial |tick167 envelopes filled; residual named L5 human send\n",
)

replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_de_lijn_dotatie,",
    "gap_de_lijn_dotatie,Vlaanderen>MOW>De_Lijn>dotatie,de_lijn,"
    "Full 2025-2026 exploitatie+investering Vlaamse toelage comparable to 2019-2024 Vervoersautoriteit table "
    "(PQ955 + MJR own receipts 264-314m + e-bus 400m VAK + savings 30-125m filled; JV PDF still blocked),"
    "2019-24 series strong; 2025-26 path metrics strong; absolute total exp+inv toelage perimeter still partial,"
    "5,Vlaamse overheid Team Openbaarheid / De Lijn,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
    "docs/doge/foi/drafts/gap_de_lijn_dotatie.md,ready,2026-07-20,,,,,"
    "cmt_de_lijn_mjr_path_2026_30|cmt_de_lijn_dotatie_annual,lb_de_lijn_ebus_400m_path,"
    "2026-07-20T01:00:00Z,2026-07-28T05:45:00Z,"
    "tick126|161|167: MJR path fill; residual full toelage perimeter human send\n",
)

replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_162,",
    "rq_162,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_vipa_named_l5,2026-07-28T05:25:00Z,2026-07-28T05:45:00Z,"
    '"tick167: VIPA 180m 2026 path 295m 2029 hosp forfait 77.3-89.6m; De Lijn ESR receipts 264-314m e-bus +400m savings 30-125m; residual named/toelage FOI; spawn rq_163"\n',
)

rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_163," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_163,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV if unblocked other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T05:45:00Z,,"
            '"Spawned tick167 after VIPA+De Lijn path; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_163 hole-fill Antwerp/Mons/other; rq_116 SWA deferred. FOI ready human send. tick167 VIPA+De Lijn path."\n',
    encoding="utf-8",
    newline="\n",
)

log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **VIPA 2026 envelope + De Lijn MJR path**)
- Found (strong primary: MJR 2025-30 + VP commissie Gennez + begroting tables):
  - **VIPA total:** **EUR 180m 2026** (no +20m expansion) · path **295m 2029**.
  - **Hospital forfait:** **77.3m 2025 → 89.6m 2026** (+14.5m room new awards).
  - Ouderen forfait **~35→40m** · handicap auth **16.8m** · instandhouding **+27.2m** (table 27.692m).
  - Expansion cut **−20m** · classic VEK budgeted **33m** vs need claim 68m · kinderopvang shift **60m**.
  - **De Lijn ESR-ontvangsten (own, not toelage):** BA2025 **264.3m** · BO2026 **313.8m** · const **263.8m** · 2030 **250.9m**.
  - E-bus VAK extra **+400m** path · OV savings **−50m 2026** → **−125m 2029** · MOW punctual **30m/yr** · VEK peaks **+145m 2027** / **+59m 2028** · VEK actualisatie **−61.3m**.
- Antwerp register / Mons BI2026 still not newly filled.
- Wrote: sources 3; budgets 26; cmt 2; lb 3; FOI gaps vipa+de_lijn notes; rq_162=done; seeded **rq_163**.
- FOI: named VIPA L5 + full De Lijn toelage still **ready** human send.
- Next: prio5 **rq_163**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")
print("tick167 OK")

# -*- coding: utf-8 -*-
"""Tick 674: federal CoA BA2026 multi-year E1 path + pension residual dual E2 — rq_665."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T10:15:00Z"
TICK = 674
RQ = "rq_665"
NEXT_RQ = "rq_666"
GAP = "gap_fed_aju2026_multiyear_pension_l5"
SRC = "src_ccrek_fed_aju2026_multiyear_pension"
SRC_DUAL = "src_dual_e1_e2_path_tick674"


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
        f"tick{TICK} fed E1 path -24.5 to -36.2bn interest 17.5 dual E2; "
        f"next {NEXT_RQ}; progress@680 in 6; rq_116 deferred"
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


ent_rows = [
    "fpd_pensioenen,Federale Pensioendienst FPD,Service federal des Pensions,Federal Pension Service dual,agency,sec_federal,nl,https://www.sfpd.fgov.be,,,CoA aju2026 MyPension IT +5m; pension reform implementation dual; tick674",
]

src_rows = [
    f"{SRC},CoA federal BA2026 multi-year E1 path pension residual dual E2,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,Cour des comptes / Rekenhof,2026-08-01,audit,"
    "Strong tick674: E1 deficit aju 24.5bn (init 24.6) path 2029 36.2bn (-5pct GDP); primary 12.2->18.7 exp +21.2 rec +12.8; interest 12.3->17.5; MR 3Apr +615 (tech 517 + pol 98); VAT takeaway scrap 475 e-comm handling 210 pension 3rd read 51.6 (1.8bn 2029); reinteg -112; personnel control cancel +179; Fedasil +41 cyber +40 energy +20; spilindex SS -360.3 contrib +164.2; E1 -3.7pct GDP defence 1.6pct; BE saldo AT -4.9 2026 to -5.5 2029 vs MTFSP -3.0 gap -2.5pp; snowball gap -0.91 2026 to -0.06 2031; ME impact cum ~6.7bn to 2029; Engie nuclear unpriced; pension: overleving -16 IGO 13 not 26 ziektepens 32 limited idx 53.5 MyPension 5",
    f"{SRC_DUAL},Dual E1 path 24.5-36.2bn vs E2 VL/WAL/FWB aju dual,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,DOGE synthesis CoA fed+E2 dual,2026-08-01,synthesis,"
    "Strong dual: E1 -24.5bn 2026 path -36.2 2029; E2 VL -3.64 WAL -2.02 FWB -1.75 class; BE -4.9pct GDP; not TE-additive; tick674",
]

bud_rows = [
    # E1 multi-year path
    f"bud_fed_e1_deficit_aju_24_5bn_2026,sec_federal,2026,-24500000000,,,budgeted,{SRC},strong,Entity I financing deficit aju 24.5bn (-3.7pct GDP) after MR measures (init 24.6); tick674",
    f"bud_fed_e1_deficit_path_36_2bn_2029,sec_federal,2029,-36200000000,,,budgeted,{SRC},strong,Entity I deficit path 2029 36.2bn (-5pct GDP); worsen 11.7bn vs 2026 (init path only 6.6); tick674",
    f"bud_fed_e1_primary_deficit_12_2bn_2026,sec_federal,2026,-12200000000,,,budgeted,{SRC},strong,E1 primary deficit 2026 12.2bn path to 18.7 2029; tick674",
    f"bud_fed_e1_primary_deficit_18_7bn_2029,sec_federal,2029,-18700000000,,,budgeted,{SRC},strong,E1 primary deficit 2029 18.7bn (exp +21.2 rec +12.8 2026-29); tick674",
    f"bud_fed_interest_path_17_5bn_2029,sec_federal,2029,17500000000,,,budgeted,{SRC},strong,Interest charges path 17.5bn 2029 from 12.3bn 2026 (+5.2); tick674",
    f"bud_fed_exp_share_gdp_2026,sec_federal,2026,32.4,,,budgeted,{SRC},strong,E1 exp share GDP 32.4pct 2026 (stable 32.5 2029); tick674",
    f"bud_fed_rec_share_gdp_2026,sec_federal,2026,30.4,,,budgeted,{SRC},strong,E1 rec share GDP 30.4pct 2026 path 29.5 2029 (2022 was 30.8); tick674",
    f"bud_fed_rec_share_gdp_2029,sec_federal,2029,29.5,,,budgeted,{SRC},strong,E1 rec share GDP 29.5pct 2029 falling fiscal pressure; tick674",
    # MR 3 Apr residual detail
    f"bud_fed_mr_tech_517m_2026,sec_federal,2026,517000000,,,budgeted,{SRC},strong,MR 3Apr technical improve ~517m of +615 total (customs reest + VVPRbis 475 + prison/space defer 187 - reinteg -112); tick674",
    f"bud_fed_mr_policy_98m_2026,sec_federal,2026,98000000,,,budgeted,{SRC},strong,MR 3Apr policy net ~98m (cancel personnel control hit +179; Regie 50; Fedasil -41 cyber -40 energy -20); tick674",
    f"bud_fed_vvprbis_customs_reest_475m,sec_federal,2026,475000000,,,budgeted,{SRC},strong,VVPRbis + EU customs reestimation cluster ~475m technical; tick674",
    f"bud_fed_prison_space_defer_187m,sec_federal,2026,187000000,,,budgeted,{SRC},strong,Prison overcrowding + EU space policy spend defer to 2027 187m; tick674",
    f"bud_fed_reinteg_sick_minus_112m,sec_federal,2026,-112000000,,,budgeted,{SRC},strong,Long-term sick reintegration receipts -112m vs plan; tick674",
    f"bud_fed_personnel_control_cancel_179m,sec_federal,2026,179000000,,,budgeted,{SRC},strong,Cancel negative impact of staff cuts on fiscal/social controls +179m (FOD Finance calc); tick674",
    f"bud_fed_regie_invest_plus_50m,sec_federal,2026,50000000,,,budgeted,{SRC},strong,Regie der Gebouwen invest program adjust +50m saldo improve; tick674",
    f"bud_fed_fedasil_path_plus_41m,sec_federal,2026,41000000,,,budgeted,{SRC},strong,Refugee reception decision -41m on saldo; tick674",
    f"bud_fed_cyber_plus_40m,sec_federal,2026,40000000,,,budgeted,{SRC},strong,Cybersecurity +40m spend; tick674",
    f"bud_fed_energy_support_plus_20m,sec_federal,2026,20000000,,,budgeted,{SRC},strong,Energy support measures +20m; tick674",
    # Scrapped/delayed measures
    f"bud_fed_vat_takeaway_scrap_475m,sec_federal,2026,475000000,,,budgeted,{SRC},strong,VAT rate change takeaway/non-alc/sport scrap cost 475m vs BO plan; tick674",
    f"bud_fed_ecommerce_handling_scrap_210m,sec_federal,2026,210000000,,,budgeted,{SRC},strong,E-commerce handling fee scrap pending EU 210m; tick674",
    f"bud_fed_pension_3rd_read_cost_51_6m_2026,sec_federal,2026,51600000,,,budgeted,{SRC},strong,Pension reform 3rd reading adjustments cost 51.6m 2026 (most from 2027; yield 1.8bn 2029); tick674",
    f"bud_fed_pension_reform_yield_1_8bn_2029,sec_federal,2029,1800000000,,,budgeted,{SRC},strong,Pension reform package expected yield 1.8bn 2029; tick674",
    # Spilindex
    f"bud_fed_spilindex_ss_benefits_minus_360m,sec_ss,2026,-360300000,,,budgeted,{SRC},strong,FOD SZ: earlier spilindex (Jun vs Nov) impact benefits -360.3m 2026 (3 months centenindex); tick674",
    f"bud_fed_spilindex_ss_contrib_plus_164m,sec_ss,2026,164200000,,,budgeted,{SRC},strong,FOD SZ: earlier spilindex contrib +164.2m; tick674",
    f"bud_fed_spilindex_ss_net_minus_196m,sec_ss,2026,-196100000,,,budgeted,{SRC},strong,Net SS spilindex impact -196.1m (benefits -360.3 + contrib +164.2); not in aju receipts/exp fully; tick674",
    # BE saldo % dual MTFSP
    f"bud_be_saldo_pct_at_2026,gg_belgium,2026,-4.9,,,budgeted,{SRC},strong,BE saldo AT toelichting -4.9pct GDP 2026 (MTFSP -4.6; APR -4.9); tick674",
    f"bud_be_saldo_pct_at_2029,gg_belgium,2029,-5.5,,,budgeted,{SRC},strong,BE saldo AT path -5.5pct GDP 2029 vs MTFSP -3.0 gap -2.5pp; tick674",
    f"bud_be_saldo_pct_mtfsp_2029,gg_belgium,2029,-3.0,,,budgeted,{SRC},strong,MTFSP Mar2025 BE saldo target -3.0pct GDP 2029; tick674",
    f"bud_be_saldo_pct_2025_apr,gg_belgium,2025,-5.2,,,budgeted,{SRC},strong,BE saldo 2025 -5.2pct GDP (APR/AT); tick674",
    f"bud_e1_saldo_pct_gdp_2026,sec_federal,2026,-3.7,,,budgeted,{SRC},strong,Entity I saldo -3.7pct GDP 2026; defence ESR spend 1.6pct GDP (+0.2pp); tick674",
    f"bud_defence_share_gdp_1_6pct_2026,sec_federal,2026,1.6,,,budgeted,{SRC},strong,Defence ESR-attributable exp 1.6pct GDP 2026; tick674",
    # Snowball
    f"bud_be_implicit_rate_2026,gg_belgium,2026,2.41,,,budgeted,{SRC},strong,Implicit interest rate GG debt 2.41pct 2026 path 2.96 2031; tick674",
    f"bud_be_nominal_gdp_growth_2026,gg_belgium,2026,3.32,,,budgeted,{SRC},strong,Nominal GDP growth 3.32pct 2026; tick674",
    f"bud_be_snowball_gap_2026,gg_belgium,2026,-0.91,,,budgeted,{SRC},strong,Snowball differential i-g -0.91pp 2026 path -0.06 2031 (still negative = not triggering); tick674",
    f"bud_be_snowball_gap_2031,gg_belgium,2031,-0.06,,,budgeted,{SRC},strong,Snowball i-g gap path -0.06pp 2031 nearly zero; tick674",
    f"bud_fed_me_macro_cum_effort_6_7bn,sec_federal,2029,6700000000,,,budgeted,{SRC},strong,BOSA 15Apr: ME macro param worsen may require ~6.7bn cumulative extra effort to end-2029; tick674",
    f"bud_fed_gdp_slow_0_5_impact_1_4bn,sec_federal,2026,1400000000,,,budgeted,{SRC},strong,Sensitivity: 0.5pp GDP slow worsens E1 saldo ~1.4bn 2026; tick674",
    # Pension residual L5
    f"bud_pens_overleving_cancel_16m,fpd_pensioenen,2026,-16000000,,,budgeted,{SRC},strong,Overlevingspensioen->overgangsuitkering not 2026: save cancel -16m (spend stays); tick674",
    f"bud_pens_igo_save_13m_ba,fpd_pensioenen,2026,13000000,,,budgeted,{SRC},strong,IGO control+residence save BA 13m (BO 26m; law not ready; KB path); tick674",
    f"bud_pens_ziektepensioen_save_32m,fpd_pensioenen,2026,32000000,,,budgeted,{SRC},strong,Uitdoven ziektepensioen ambtenaren save 32m (BO 26; delay to 1Jun but moratorium); RIZIV +9m offset; tick674",
    f"bud_pens_limited_index_save_53_5m,fpd_pensioenen,2026,53500000,,,budgeted,{SRC},strong,Limited index high pensions save BA 53.5m (BO 39.9); may understate if Jun spilindex; tick674",
    f"bud_pens_riziv_ziekte_offset_9m,riziv,2026,9000000,,,budgeted,{SRC},strong,RIZIV extra from ziektepensioen reform 9m 2026; tick674",
    f"bud_fpd_mypension_it_plus_5m,fpd_pensioenen,2026,5000000,,,budgeted,{SRC},strong,FPD MyPension+legacy IT +5m; tick674",
    # Dual E1+E2
    f"bud_dual_e1_e2_saldo_class_2026,gg_belgium,2026,-31911000000,,,budgeted,{SRC_DUAL},strong,Dual class E1 -24.5bn + VL -3.643 + WAL -2.015 + FWB -1.753 ~ -31.9bn (metrics differ ESR/SEC; not TE-additive); tick674",
    f"bud_dual_be_mtfsp_gap_2_5pp_2029,gg_belgium,2029,-2.5,,,budgeted,{SRC_DUAL},strong,Dual: AT BE saldo -5.5 vs MTFSP -3.0 = -2.5pp gap 2029; tick674",
]

cmt_rows = [
    f"cmt_fed_e1_path_24_5_to_36_2,E1 deficit path 24.5 to 36.2bn dual E2,sec_federal,Entity I,CoA 2026_22 chI.3,2026-05-21,2026,2029,24500000000,\"{{\"\"2026\"\":24500000000,\"\"2029\"\":36200000000}}\",,active,,Federal multi-year dual,Interest+primary,{SRC},strong,Federal>E1>path,tick674",
    f"cmt_fed_interest_path_17_5bn,Interest 12.3 to 17.5bn dual debt,sec_federal,Debt Agency,CoA 2026_22,2026-05-21,2026,2029,12300000000,\"{{\"\"2026\"\":12300000000,\"\"2029\"\":17500000000}}\",,active,,Snowball dual,Rate path,{SRC},strong,Federal>interest,tick674",
    f"cmt_fed_pension_reform_residual,Pension reform residual L5 dual,fpd_pensioenen,FPD,CoA 2026_22 III.2,2026-05-21,2026,2029,1800000000,\"{{\"\"2026\"\":51500000,\"\"2029\"\":1800000000}}\",,active,,Reform delivery FOI,Laws pending,{SRC},strong,Federal>pensions,tick674",
    f"cmt_be_saldo_vs_mtfsp_gap,BE saldo path -5.5 vs MTFSP -3.0 dual,gg_belgium,Belgium GG,CoA 2026_22 chII,2026-05-21,2026,2029,0,\"{{\"\"2026\"\":-4.9,\"\"2029\"\":-5.5}}\",,active,,EU governance dual,Effort gap,{SRC},strong,Belgium>saldo>MTFSP,tick674",
    f"cmt_dual_e1_e2_tick674,Dual E1+E2 aju path residual,gg_belgium,Entity I+II,CoA fed+E2 dual,2026-05-21,2026,2026,31911000000,\"{{\"\"2026\"\":31911000000}}\",,active,,Full Entity dual map,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>e1_e2_path,tick674",
    f"cmt_spilindex_ss_net_196m,Spilindex SS net -196m not fully in aju,sec_ss,FOD SZ,CoA 2026_22 macro,2026-05-05,2026,2026,196100000,\"{{\"\"2026\"\":196100000}}\",,active,,Index residual dual,Update aju,{SRC},strong,SS>spilindex,tick674",
]

lb_rows = [
    f"lb_fed_e1_path_36_2bn_2029,E1 deficit path 36.2bn 2029 dual,Federal,ops,Federal>E1>path,36200000000,0,Strong CoA: 24.5->36.2 (-5pct GDP); primary+interest dual E2,strong,{SRC},Entity I,Multi-year fiscal dual,Primary,7.0,9.5,3,7.55,Publish undivided measures,open,,tick674",
    f"lb_fed_interest_17_5bn_2029,Interest path 17.5bn 2029,Federal,ops,Federal>interest,17500000000,0,Strong CoA +5.2bn from 12.3; snowball gap to -0.06 2031 dual,strong,{SRC},bondholders,Debt service dual,Primary,6.5,9.5,2,7.25,Rate sensitivity FOI,open,,tick674",
    f"lb_be_mtfsp_gap_2_5pp_2029,BE vs MTFSP gap -2.5pp 2029,Belgium,ops,Belgium>MTFSP>gap,0,0,Strong CoA AT -5.5 vs MTFSP -3.0; dual governance failure,strong,{SRC},all entities,EU plan gap,Primary,8.0,7.5,3,7.25,Entity effort split FOI,open,,tick674",
    f"lb_fed_pension_reform_1_8bn_2029,Pension reform yield path 1.8bn 2029,Federal,ops,Federal>pensions>reform,1800000000,0,Strong CoA: 2026 residual IGO/overleving slip; dual SS,strong,{SRC},pensioners,Reform delivery,Primary,6.5,8.0,3,6.85,Law calendar FOI,open,,tick674",
    f"lb_spilindex_ss_net_196m_2026,Spilindex SS net -196m,Federal,ops,SS>spilindex,196100000,0,Strong CoA FOD SZ: benefits -360 contrib +164 not fully in aju dual,strong,{SRC},SS recipients,Index residual,Primary,6.5,6.5,2,6.1,Reopen aju params,open,,tick674",
    f"lb_dual_e1_e2_path_2026,Dual E1+E2 saldo class ~32bn,Belgium,ops,Belgium>dual>e1_e2_path,31911000000,0,Strong dual: E1 24.5 + VL 3.64 + WAL 2.02 + FWB 1.75; not TE-additive,strong,{SRC_DUAL},all entities,Entity dual residual,Primary dual,6.5,9.0,3,7.2,Cross FOI,open,,tick674",
]

foi_row = (
    f"{GAP},Federal>Aju2026>multiyear_pension_L5,sec_federal,"
    "Undivided measures 2026-29 path; interest rate assumptions to 17.5bn; pension law calendar IGO/overleving/split; BOSA follow-up note withheld; Engie nuclear fiscal impact; ME 6.7bn sensitivity detail; Entity II composition behind BE -5.5pct,"
    "CoA fed BA2026 multi-year pension strong tick674; L5 dual E2,"
    f"5,FOD BOSA / FOD SZ / FPD / openbaarheid federaal,openbaarheid@bosa.be,https://bosa.belgium.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_fed_e1_path_24_5_to_36_2|cmt_fed_pension_reform_residual|cmt_be_saldo_vs_mtfsp_gap,"
    f"lb_fed_e1_path_36_2bn_2029|lb_fed_interest_17_5bn_2029|lb_dual_e1_e2_path_2026,"
    f"{NOW},{NOW},tick674 CoA fed 2026_22 primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22)

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: FOD BOSA / FOD Sociale Zekerheid / Federale Pensioendienst
openbaarheid@bosa.be

Betreft: Openbaarheid — aju 2026 meerjarenpad Entiteit I + pensioenrestanten L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. Meerjarenpad Entiteit I: opbouw van -24,5 mrd (2026) naar -36,2 mrd (2029),
   inclusief niet-verdeelde maatregelen (% bbp).
2. Rentelastenpad 12,3 -> 17,5 mrd: renteassumpties en schuldgraad.
3. Pensioenhervorming: wetgevingskalender IGO/overleving/pensioensplit en
   onderbouwing IGO-besparing 13 mEUR (i.p.v. 26).
4. BOSA-opvolgingsnota begrotingsmaatregelen (Rekenhof niet ontvangen).
5. Intentiebrief Engie nucleair: budgettaire raming of bevestiging ontbreken.
6. Sensitivity Midden-Oosten ~6,7 mrd cumulatief tot 2029: detail per jaar.
7. Samenstelling Entiteit II achter BE-saldo -5,5% bbp 2029.

Période: 2025-01-01 tot 2031-12-31.
Vorm: CSV/XLSX bij voorkeur.

Met vriendelijke groet,
[Naam]
```

## Notes agent
- Primary: CoA 2026_22 federal BA2026 tick674. Dual with E2 VL/WAL/FWB wave.
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **federal CoA BA2026 multi-year E1 path -24.5 to -36.2bn + pension dual E2**)
- Found (primary CoA 2026_22): **E1 deficit aju EUR24.5bn** (-3.7pct GDP) path **2029 EUR36.2bn** (-5pct); primary **12.2->18.7**; interest **12.3->17.5**; MR **+615** (tech 517 pol 98). Scrapped VAT takeaway **475** e-comm **210**; pension 3rd read **51.6** (yield **1.8bn 2029**). Spilindex SS **-360.3/+164.2** net **-196**. BE saldo AT **-4.9** path **-5.5 2029** vs MTFSP **-3.0**. Snowball i-g **-0.91->-0.06**. ME cum effort **~6.7bn**. Pension L5: overleving cancel **16**; IGO **13** not 26; ziektepens **32**; limited idx **53.5**. Dual E1+E2 class **~32bn**. Strong CoA; L5 FOI.
- Wrote: entities (+1); budgets (+45); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@680 in 6 ticks; rq_116 deferred
"""


def main() -> None:
    n_ent = append_rows(ROOT / "entities.csv", ent_rows)
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
        f"tick{TICK} fed E1 path 24.5-36.2bn interest 17.5 pension residual dual E2; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,sec_federal,"
        f"Next residual: fed CoA SS ch residual RIZIV/arbeidsongeschiktheid or energy ch4 or VL BA fonds residual.,,"
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

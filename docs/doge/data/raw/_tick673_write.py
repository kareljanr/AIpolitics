# -*- coding: utf-8 -*-
"""Tick 673: VL BA2026 WVG WZC/VIPA + Lantis residual dual WAL AViQ — rq_664."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T10:00:00Z"
TICK = 673
RQ = "rq_664"
NEXT_RQ = "rq_665"
GAP = "gap_vl_ba2026_wvg_lantis_l5"
SRC = "src_ccrek_vl_ba2026_wvg_lantis"
SRC_DUAL = "src_dual_vl_wvg_lantis_tick673"


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
        f"tick{TICK} VL WZC 2.74bn CoA gap 36m VIPA shortfall 27m Lantis VAK 2.48bn dual; "
        f"next {NEXT_RQ}; progress@680 in 7; rq_116 deferred"
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
    "vipa,VIPA zorginfrastructuur,Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden,Flanders care infra dual WAL,agency,vlaanderen_gov,nl,https://www.vipa.be,,,CoA BA2026 systeembuffer stop 22.9m; VEK need 63.9 vs budget 37.3 shortfall 26.6; tick673",
    "lantis,Lantis BAM Antwerpen,Beheersmaatschappij Antwerpen Mobiel Lantis,Oosterweel delivery dual Sofico,agency,vlaanderen_gov,nl,https://www.lantis.be,,,CoA BA2026 VAK 2479.4 PFAS 842.8 loan 1650 herijking 2822.3; tick673",
]

src_rows = [
    f"{SRC},CoA Flanders BA2026 WVG Table19 WZC VIPA + Lantis residual dual AViQ,https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf,Cour des comptes / Rekenhof,2026-08-01,audit,"
    "Strong tick673: WZC VEK BA 2737.7 BO 2765.6 CoA min 2773.6 gap 35.9; BTZ existing BA 2677.5 CoA 2717.4; growth BA 16.1 CoA 8.0; controls -8 not feasible; incontinence 12.7 young dem 4.0 short stay 6.8 add fin BA 28.4 CoA 24.5; reserves save 12 (Zorg 7-1.4 to VAPH 1 Opgroeien 0.4) unlikely 2026; VIPA buffer stop 22.9 need VEK 63.9 budget 37.3 short 26.6; Lantis VAK 2479.4 (exog 1006.8 PFAS 842.8 overkap 629.8); loan 1650 herijk 2035 min takeover 2822.3; VEK 1196.8 path +107; loan draw 1158 +261.1; GIP one-year 3685 (-179 vs start); Waterweg -73 Scheldebrug; dual AViQ MR",
    f"{SRC_DUAL},Dual VL WZC/VIPA/Lantis vs WAL AViQ OTW dual,https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf,DOGE synthesis CoA VL BA dual WAL,2026-08-01,synthesis,"
    "Strong dual: VL WZC 2.74bn dual AViQ elderly; Lantis 2.48bn VAK dual Oosterweel/Sofico; not TE-additive; tick673",
]

bud_rows = [
    # WZC Table19
    f"bud_vl_wzc_total_vek_ba2026,vlaanderen_gov,2026,2737700000,,,budgeted,{SRC},strong,WZC total VEK BA2026 2737.7m (BO 2765.6; CoA min est 2773.6 gap 35.9); open-end; dual AViQ; tick673",
    f"bud_vl_wzc_total_vek_bo2026,vlaanderen_gov,2026,2765600000,,,budgeted,{SRC},strong,WZC total VEK BO2026 2765.6m; tick673",
    f"bud_vl_wzc_coa_min_est_2773_6m,vlaanderen_gov,2026,2773600000,,,budgeted,{SRC},strong,CoA minimum WZC VEK est 2773.6m; tick673",
    f"bud_vl_wzc_gap_coa_vs_ba_35_9m,vlaanderen_gov,2026,35900000,,,budgeted,{SRC},strong,CoA vs BA WZC shortfall 35.9m (matches prior BTZ gap seed); tick673",
    f"bud_vl_wzc_btz_existing_ba2026,vlaanderen_gov,2026,2677500000,,,budgeted,{SRC},strong,WZC BTZ existing beds 31/12/2025 BA 2677.5 (BO 2702.7; CoA 2717.4); tick673",
    f"bud_vl_wzc_btz_existing_coa,vlaanderen_gov,2026,2717400000,,,budgeted,{SRC},strong,WZC BTZ existing CoA est 2717.4m (Dec2025 days + BTZ 1Jan2026); tick673",
    f"bud_vl_wzc_btz_growth_ba2026,vlaanderen_gov,2026,16100000,,,budgeted,{SRC},strong,WZC/CVK bed growth 2026 BA 16.1 (BO 17.9; CoA half 8.0); tick673",
    f"bud_vl_wzc_btz_growth_coa_8m,vlaanderen_gov,2026,8000000,,,budgeted,{SRC},strong,CoA assumes only half planned bed growth = 8.0m; tick673",
    f"bud_vl_wzc_btz_total_a_ba2026,vlaanderen_gov,2026,2685600000,,,budgeted,{SRC},strong,BTZ WZC/CVK total A BA 2685.6 (CoA 2725.4); tick673",
    f"bud_vl_wzc_controls_save_8m_not_feasible,vlaanderen_gov,2026,-8000000,,,budgeted,{SRC},strong,Sterkere controles indicatiestelling -8.0m not feasible CoA (excl from CoA est); tick673",
    f"bud_vl_wzc_incontinentie_ba2026,vlaanderen_gov,2026,12700000,,,budgeted,{SRC},strong,Tegemoetkoming incontinentiemateriaal BA 12.7m; tick673",
    f"bud_vl_wzc_jongdementie_4m,vlaanderen_gov,2026,4000000,,,budgeted,{SRC},strong,Projecten jongdementie 4.0m flat; tick673",
    f"bud_vl_wzc_orient_kortverblijf_6_8m,vlaanderen_gov,2026,6800000,,,budgeted,{SRC},strong,Orientierend kortverblijf BA 6.8 (BO 7.6); tick673",
    f"bud_vl_wzc_aanvullende_fin_ba_28_4m,vlaanderen_gov,2026,28400000,,,budgeted,{SRC},strong,Aanvullende financiering WZC BA 28.4 (CoA 24.5); tick673",
    f"bud_vl_wzc_measures_save_claim_45_3m,vlaanderen_gov,2026,45300000,,,budgeted,{SRC},strong,Claimed WZC measures package 45.3m VAK/VEK (open-end re-estimate); tick673",
    # Reserves + VIPA
    f"bud_vl_wvg_reserves_save_12m_detail,vlaanderen_gov,2026,12000000,,,budgeted,{SRC},strong,WVG reserves activate save 12.0m; Zorg 7.0 after -1.4 reshuffle to VAPH 1.0 + Opgroeien 0.4; decree pending unlikely 2026; tick673",
    f"bud_vipa_buffer_stop_save_22_9m,vipa,2026,22900000,,,budgeted,{SRC},strong,VIPA systeembuffer stop save 22.9m VAK/VEK BO; VEK not immediately realizable; tick673",
    f"bud_vipa_vek_need_63_9m,vipa,2026,63900000,,,budgeted,{SRC},strong,VIPA needed VEK est 63.9m for past awards; tick673",
    f"bud_vipa_vek_budget_ba_37_3m,vipa,2026,37300000,,,budgeted,{SRC},strong,VIPA VEK in BA only 37.3m; tick673",
    f"bud_vipa_vek_shortfall_26_6m,vipa,2026,26600000,,,budgeted,{SRC},strong,VIPA VEK shortfall 26.6m (need 63.9 - budget 37.3); admin says eat carried result; tick673",
    # Lantis residual
    f"bud_lantis_vak_ba2026_2479_4m,lantis,2026,2479400000,,,budgeted,{SRC},strong,Lantis VAK BA 2479.4m to lock remaining Sep2024 award (Oosterweelknoop+Rechteroever); tick673",
    f"bud_lantis_exogeen_1006_8m,lantis,2026,1006800000,,,budgeted,{SRC},strong,Lantis exogenous within main works 1006.8m (2024 est 985 prijspeil jan2024); tick673",
    f"bud_lantis_pfas_842_8m_confirm,lantis,2026,842800000,,,budgeted,{SRC},strong,Lantis direct PFAS remediation 842.8m (2024 est ~1207 less 399 funded + optim); tick673",
    f"bud_lantis_overkapping_629_8m,lantis,2026,629800000,,,budgeted,{SRC},strong,Lantis second overkapping package 629.8m via overkappingsruiter (2024 est 643); tick673",
    f"bud_lantis_loan_subordinated_1650m,lantis,2026,1650000000,,,budgeted,{SRC},strong,Second subordinated loan 1650m replaces VL grant for exog+PFAS pending tolls; CoA not repayable from tolls; tick673",
    f"bud_lantis_herijk_2035_takeover_min_2822m,lantis,2035,2822300000,,,budgeted,{SRC},strong,CoA: at 2035 reprice VL must take over min 2822.3m subordinated debt to match toll model; tick673",
    f"bud_lantis_vek_ba2026_1196_8m,lantis,2026,1196800000,,,budgeted,{SRC},strong,Lantis invest VEK BA 1196.8 path +107 from BO 1089.8; tick673",
    f"bud_lantis_vek_bo2026_1089_8m,lantis,2026,1089800000,,,budgeted,{SRC},strong,Lantis invest VEK BO 1089.8m; tick673",
    f"bud_lantis_loan_draw_1158m_ba2026,lantis,2026,1158000000,,,budgeted,{SRC},strong,Lantis loan draw receipt BA 1158.0 path +261.1 vs BO; partial draw second loan; tick673",
    f"bud_vl_gip_one_year_3685m,vlaanderen_gov,2026,3685000000,,,budgeted,{SRC},strong,GIP one-year project total 3685.0m (-179 vs start-2026 estimate); differs from 3864 planned figure; tick673",
    f"bud_vl_gip_reduce_179m_vs_start,vlaanderen_gov,2026,-179000000,,,budgeted,{SRC},strong,GIP 2026 reduce 179m vs investment cell start estimate (maint 77 off GIP + Waterweg -73 Scheldebrug); tick673",
    f"bud_waterweg_scheldebrug_path_minus_73m,vlaanderen_gov,2026,-73000000,,,budgeted,{SRC},strong,De Vlaamse Waterweg overkapping leefbaarheid -73.0m Scheldebrug Antwerp partial delay; tick673",
    f"bud_waterweg_vs_gip_plus_21_3m,vlaanderen_gov,2026,21300000,,,budgeted,{SRC},strong,Waterweg 21.3m more invest than GIP line CoA flag; tick673",
    # Dual
    f"bud_dual_wzc_aviq_elderly_2026,gg_belgium,2026,2737700000,,,budgeted,{SRC_DUAL},strong,Dual VL WZC VEK 2.74bn vs WAL AViQ elderly/MR channel (not sum); tick673",
    f"bud_dual_lantis_oosterweel_vak_2026,gg_belgium,2026,2479400000,,,budgeted,{SRC_DUAL},strong,Dual Lantis VAK 2.48bn Oosterweel vs WAL DO14/Sofico infra class; not TE-additive; tick673",
]

cmt_rows = [
    f"cmt_vl_wzc_2_74bn_coa_gap,VL WZC VEK 2.74bn CoA gap 35.9m dual AViQ,vlaanderen_gov,WZC open-end,CoA BA2026 Table19,2026-06-19,2026,2026,2737700000,\"{{\"\"2026\"\":2737700000}}\",,active,,Elderly care dual,Fund gap or cut beds,{SRC},strong,Vlaanderen>WVG>WZC,tick673",
    f"cmt_vipa_vek_shortfall_26_6m,VIPA VEK shortfall 26.6m buffer stop,vipa,VIPA,CoA BA2026 7.3,2026-01-01,2026,2026,26600000,\"{{\"\"2026\"\":26600000}}\",,active,,Care infra opacity,Inscribe full VEK,{SRC},strong,Vlaanderen>VIPA,need 63.9 budget 37.3; tick673",
    f"cmt_lantis_vak_2_48bn_loan_1650,Lantis VAK 2.48bn loan 1.65bn dual Oosterweel,lantis,Lantis,CoA BA2026 7.5,2024-09-01,2026,2035,2479400000,\"{{\"\"2026\"\":2479400000}}\",,active,,Mega project dual,Convert loan to equity now,{SRC},strong,Vlaanderen>Lantis,herijk 2822m 2035; tick673",
    f"cmt_lantis_herijk_2822m_2035,Lantis herijk 2035 min debt takeover 2.82bn,lantis,VL-Lantis financing,CoA Toekomstverbond follow-up,2025-12-01,2035,2035,2822300000,\"{{\"\"2035\"\":2822300000}}\",,active,,Hidden stock dual,Capital injection,{SRC},strong,Vlaanderen>Lantis>loan,tick673",
    f"cmt_dual_wzc_lantis_tick673,Dual VL WZC+Lantis vs WAL AViQ/OTW,gg_belgium,Entity II dual,CoA VL BA dual,2026-06-19,2026,2026,2737700000,\"{{\"\"2026\"\":2737700000}}\",,active,,Dual care+infra,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>wzc_lantis,tick673",
    f"cmt_gip_3685_unrealistic,GIP 2026 3.685bn unrealistic CoA,vlaanderen_gov,MOW GIP,CoA BA2026 7.5,2026-05-22,2026,2026,3685000000,\"{{\"\"2026\"\":3685000000}}\",,active,,Infra planning fail,Autumn revision,{SRC},strong,Vlaanderen>GIP,monthly pre-lists; tick673",
]

lb_rows = [
    f"lb_vl_wzc_2_74bn_2026,VL WZC VEK 2.74bn CoA gap 36m dual AViQ,Flanders,ops,Vlaanderen>WVG>WZC,2737700000,0,Strong CoA Table19 open-end; CoA min 2.77bn; dual AViQ elderly,strong,{SRC},WZC residents,Elderly care dual,Primary,5.5,8.5,3,6.55,Fund CoA gap,open,,tick673",
    f"lb_vipa_shortfall_27m_2026,VIPA VEK shortfall 26.6m,Flanders,ops,Vlaanderen>VIPA,26600000,0,Strong CoA: buffer stop 22.9 save but VEK underfunded vs past awards,strong,{SRC},care projects,Infra VEK opacity,Primary,7.5,5.5,2,6.25,Inscribe 63.9 VEK,open,,tick673",
    f"lb_lantis_vak_2_48bn_2026,Lantis VAK 2.48bn award lock dual,Flanders,ops,Vlaanderen>Lantis>VAK,2479400000,0,Strong CoA: PFAS 843 + exog 1.01bn + overkap 630; dual Oosterweel,strong,{SRC},contractors,Mega project dual,Primary,6.5,8.5,3,6.85,Loan to equity FOI,open,,tick673",
    f"lb_lantis_loan_1650_herijk_2822,Lantis loan 1.65bn herijk takeover 2.82bn,Flanders,ops,Vlaanderen>Lantis>loan,1650000000,0,Strong CoA: tolls cannot repay; 2035 min 2.82bn VL takeover; dual debt stock,strong,{SRC},bond/loan,Hidden debt dual,Primary,8.0,8.0,3,7.4,Immediate capital raise,open,,tick673",
    f"lb_gip_3685_unrealistic_2026,GIP 2026 3.685bn unrealistic,Flanders,ops,Vlaanderen>GIP,3685000000,0,Strong CoA: monthly pre-lists; autumn rewrite expected; dual Sofico,strong,{SRC},AWV DVW,Planning opacity,Primary,7.5,8.5,3,7.15,Publish executable GIP,open,,tick673",
    f"lb_dual_wzc_lantis_2026,Dual VL WZC+Lantis vs WAL,Belgium,ops,Belgium>dual>wzc_lantis,2737700000,0,Strong dual: WZC 2.74bn + Lantis 2.48bn VAK vs AViQ/Oosterweel class; not TE-additive,strong,{SRC_DUAL},Entity II dual,Care+infra dual,Primary dual,6.5,8.5,3,6.85,Cross FOI,open,,tick673",
]

foi_row = (
    f"{GAP},Vlaanderen>BA2026>WVG_Lantis_L5,vlaanderen_gov,"
    "WZC CoA gap 35.9 methodology + bed growth; VIPA VEK 63.9 vs 37.3; reserves decree status; Lantis loan 1650 terms + herijk 2822 calc; overkapping 629.8 cash path; GIP 3685 project list executable,"
    "CoA VL BA2026 WVG Lantis strong tick673; L5 dual AViQ,"
    f"5,Departement WVG / VIPA / Lantis / MOW / openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,https://www.vlaanderen.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_vl_wzc_2_74bn_coa_gap|cmt_vipa_vek_shortfall_26_6m|cmt_lantis_vak_2_48bn_loan_1650,"
    f"lb_vl_wzc_2_74bn_2026|lb_lantis_vak_2_48bn_2026|lb_lantis_loan_1650_herijk_2822,"
    f"{NOW},{NOW},tick673 CoA VL BA2026 primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof VL BA2026 (2026_28) §7.3 Table19 + §7.5 Lantis

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: Departement WVG / VIPA / Lantis / MOW / Team Openbaarheid
openbaarheid@vlaanderen.be

Betreft: Openbaarheid — BA2026 WVG (WZC/VIPA) + Lantis Oosterweel L5

Geachte,

Op grond van het Bestuursdecreet verzoek ik om:

1. WZC VEK: reconciliatie BA 2.737,7 vs Rekenhof-minimum 2.773,6 mEUR
   (bestaande beds, aangroei, controles -8 mEUR).
2. VIPA: onderbouwing VEK-behoefte 63,9 vs begroot 37,3 mEUR en inzet
   overgedragen resultaat.
3. Reserves WVG 12 mEUR: stand ontwerpbesluit financiele verslaggeving.
4. Lantis: voorwaarden 2e achtergestelde lening 1.650 mEUR; berekening
   herijking 2035 (min. 2.822,3 mEUR overname).
5. Overkappingspakket 629,8 mEUR: kaspad via overkappingsruiter tot 2030.
6. GIP 2026 3.685 mEUR: uitvoerbare projectlijst vs maandelijkse voorafnames.

Période: 2024-01-01 tot 2035-12-31.
Vorm: CSV/XLSX bij voorkeur.

Met vriendelijke groet,
[Naam]
```

## Notes agent
- Primary: CoA 2026_28 VL BA2026 tick673.
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **VL BA2026 WVG WZC/VIPA + Lantis VAK 2.48bn dual AViQ**)
- Found (primary CoA 2026_28): **WZC VEK BA EUR2.738bn** (BO 2.766; CoA min **2.774** gap **35.9**); BTZ existing BA **2677.5** CoA **2717.4**; growth BA **16.1** CoA half **8.0**; controls **-8** not feasible; **VIPA** buffer stop **22.9** need VEK **63.9** budget **37.3** shortfall **26.6**; reserves **12** unlikely 2026. **Lantis VAK EUR2.479bn** (exog **1006.8** PFAS **842.8** overkap **629.8**); loan **1650** herijk 2035 min takeover **2822.3**; VEK **1196.8** (+107); draw **1158** (+261). **GIP** one-year **3685** (-179). Dual AViQ/Oosterweel. Strong CoA; L5 FOI.
- Wrote: entities (+2); budgets (+35); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@680 in 7 ticks; rq_116 deferred
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
        f"tick{TICK} VL WZC 2.74bn CoA gap 36m VIPA shortfall 27m Lantis VAK 2.48bn dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,vlaanderen_gov,"
        f"Next residual: federal CoA 2026_22 dual or VL BA2026 fonds/efficiency residual or Lantis addendum detail FOI-adjacent.,,"
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

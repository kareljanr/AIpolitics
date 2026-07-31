# -*- coding: utf-8 -*-
"""Tick 671: Flanders CoA BA2026 residual dual WAL/FWB ratings GIP Digisprong — rq_662."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T09:30:00Z"
TICK = 671
RQ = "rq_662"
NEXT_RQ = "rq_663"
GAP = "gap_vl_ba2026_residual_l5"
SRC = "src_ccrek_vl_ba2026_residual"
SRC_DUAL = "src_dual_vl_wal_fwb_ba_aju_tick671"


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
        f"tick{TICK} VL BA2026 residual dual Moody A1 Fitch AA- GIP shortfall 82m Digisprong; "
        f"next {NEXT_RQ}; progress@680 in 9; rq_116 deferred"
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
    "finocas,Finocas Vlaanderen,Finocas,Flanders capital vehicle dual WAL WE,agency,vlaanderen_gov,nl,https://www.vlaanderen.be,,,CoA BA2026 capital inject plan 177.5m; prior 140m 2025 not executed; dual WE; tick671",
    "viapass,Viapass kilometerheffing,Viapass,Road charging operator dual WAL,agency,vlaanderen_gov,nl,https://www.viapass.be,,,CoA BA2026 availability fee 99.3m path +5.2; save 10m not contract-feasible; tick671",
    "asobv,ASOBV Antwerp Symphony Opera Ballet,ASOBV fusie ASO+OBV,Flanders culture fusion dual FWB culture,agency,vlaanderen_gov,nl,,,CoA BA2026 fusion save 0.8m wages retro 1Jan2026; dual FWB culture; tick671",
]

src_rows = [
    f"{SRC},CoA Flanders BA2026 residual debt ratings GIP Digisprong dual WAL/FWB,https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf,Cour des comptes / Rekenhof,2026-08-01,audit,"
    "Strong tick671: saldo BA -3642.7 path -742.6 vs BO -2900.1; rec +665.4 dep +1080.5 onderbenutting -299.8; doel -2180.8 after Oosterweel 986.7 VV rec 324.9 dep 800.1; debt consol 56971.1 direct 49801.6 +6799.1 vs 2025; Fitch AA- Moody A1 S&P AA-; ratio 91.6pct receipts; SKF correction +113.5m CoA; buffer provisie +58.5 specialty; index under 48.3 + health 7.0; Finocas 177.5 unclear; Viapass 99.3; Digisprong raid 24.0 for edu fail; volwassenen 50 save fail; WVG reserves 12; BTZ gap 35.9; ASOBV 0.8; VRT nieuwbouw -1.3 life; GIP 2026 3864 vs 2424 shortfall 82.4 (onteig 35 AWV 24.5 safety 26.2); Lantis PFAS 842.8 off GIP; Fluvius VEK 1100; MijnVerbouw VAK +350.3",
    f"{SRC_DUAL},Dual VL BA2026 Moody A1/Fitch AA- vs WAL Baa1 FWB A3,https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf,DOGE synthesis CoA VL+WAL+FWB ratings dual,2026-08-01,synthesis,"
    "Strong dual: VL rating AA-/A1 vs WAL Moody Baa1 FWB A3; saldo VL -3.64bn WAL -2.02 FWB -1.75; not TE-additive; tick671",
]

bud_rows = [
    # Saldo path detail
    f"bud_vl_ba2026_saldo_exact,vlaanderen_gov,2026,-3642700000,,,budgeted,{SRC},strong,ESR vorderingensaldo BA2026 -3642.7m path -742.6 vs BO -2900.1; tick671",
    f"bud_vl_ba2026_saldo_bo,vlaanderen_gov,2026,-2900100000,,,budgeted,{SRC},strong,ESR saldo BO2026 -2900.1m; tick671",
    f"bud_vl_ba2026_rec_path_plus_665m,vlaanderen_gov,2026,665400000,,,budgeted,{SRC},strong,ESR ontvangsten path +665.4m (VG 550.1 + RP 115.3); tick671",
    f"bud_vl_ba2026_dep_path_plus_1081m,vlaanderen_gov,2026,1080500000,,,budgeted,{SRC},strong,ESR uitgaven path +1080.5m (VG 732.5 + RP 348.1); tick671",
    f"bud_vl_ba2026_onderbenutting_path_minus_300m,vlaanderen_gov,2026,-299800000,,,budgeted,{SRC},strong,Onderbenutting path -299.8m (lower under-exec worsens saldo); tick671",
    f"bud_vl_ba2026_doel_minus_2181m,vlaanderen_gov,2026,-2180800000,,,budgeted,{SRC},strong,Saldo vs evenwichtsdoel BA -2180.8m after excl Oosterweel 986.7 + VV; tick671",
    f"bud_vl_ba2026_oosterweel_bouw_986_7m,vlaanderen_gov,2026,986700000,,,budgeted,{SRC},strong,Oosterweel bouwkost excl from doel 986.7m (BO 889.9 path +96.8); still in EU NPE; tick671",
    f"bud_vl_ba2026_vv_rec_324_9m,vlaanderen_gov,2026,324900000,,,budgeted,{SRC},strong,Vlaamse Veerkracht rec BA 324.9m (BO 163.4); tick671",
    f"bud_vl_ba2026_vv_dep_800_1m,vlaanderen_gov,2026,800100000,,,budgeted,{SRC},strong,Vlaamse Veerkracht dep BA 800.1m (BO 436.4); tick671",
    # Debt Table14 residual detail
    f"bud_vl_debt_consol_ba2026,vlaanderen_gov,2026,56971100000,,,budgeted,{SRC},strong,Maastricht geconsolideerde schuld BA2026 56971.1m path +6799.1 vs 2025 50171.9; tick671",
    f"bud_vl_debt_direct_ba2026,vlaanderen_gov,2026,49801600000,,,budgeted,{SRC},strong,Directe schuld MVG BA 49801.6m path +7405.0 vs 2025 42396.6; tick671",
    f"bud_vl_debt_consol_2025,vlaanderen_gov,2025,50171900000,,,outturn,{SRC},strong,Geconsolideerde schuld realisatie 2025 50171.9m; tick671",
    f"bud_vl_debt_entities_ba2026,vlaanderen_gov,2026,7169500000,,,budgeted,{SRC},strong,Financiele schulden geconsolideerde entiteiten BA 7169.5m path -605.8; tick671",
    f"bud_vl_debt_pps_ba2026,vlaanderen_gov,2026,635200000,,,budgeted,{SRC},strong,Geconsolideerde PPS-schuld BA 635.2m; tick671",
    f"bud_vl_debt_gsc_ba2026,vlaanderen_gov,2026,553200000,,,budgeted,{SRC},strong,Groene stroom certificaten schuld 553.2m flat; tick671",
    f"bud_vl_debt_intrasector_corr_ba2026,vlaanderen_gov,2026,-10796800000,,,budgeted,{SRC},strong,Intrasectorale correctie S1312 -10796.8m; tick671",
    f"bud_vl_debt_ratio_receipts_91_6pct,vlaanderen_gov,2026,91.6,,,budgeted,{SRC},strong,Schuld/lopende ontvangsten 91.6pct BA2026; tick671",
    f"bud_vl_net_asset_2024,vlaanderen_gov,2024,-13300000000,,,outturn,{SRC},strong,Netto-actiefpositie 2024 -13.3bn (target positive); tick671",
    f"bud_vl_skf_coa_corr_113_5m,vlaanderen_gov,2026,113500000,,,budgeted,{SRC},strong,CoA: schuldgroei 113.5m higher vs gov (SKF EU receipts not correctly neutralized); tick671",
    f"bud_vl_hospital_debt_non_maastricht,vlaanderen_gov,2026,2184300000,,,outturn,{SRC},strong,Ziekenhuisinfrastructuur schuld 2184.3m non-Maastricht federal claim (not in toelichting); tick671",
    f"bud_vl_autonomie_factor_non_maastricht,vlaanderen_gov,2026,473800000,,,outturn,{SRC},strong,Autonomiefactor 473.8m non-Maastricht federal claim; tick671",
    # Ratings dual
    f"bud_vl_fitch_aa_minus_2026,vlaanderen_gov,2026,0,,,budgeted,{SRC},strong,Fitch AA- stable confirmed 15May2026 (downgrade 20Jun2025 from AA after fed A+); tick671",
    f"bud_vl_moody_a1_apr2026,vlaanderen_gov,2026,0,,,budgeted,{SRC},strong,Moody A1 stable Apr2026 (from Aa3 path; dual WAL Baa1 FWB A3); tick671",
    f"bud_vl_sp_aa_minus_apr2026,vlaanderen_gov,2026,0,,,budgeted,{SRC},strong,S&P AA- stable Apr2026 dual; tick671",
    # FB residual
    f"bud_vl_buffer_provisie_plus_58_5m,vlaanderen_gov,2026,58500000,,,budgeted,{SRC},strong,Buffer/Monitoring provisie VEK +58.5m no specialty (CoA flags); tick671",
    f"bud_vl_index_provisie_under_48_3m,vlaanderen_gov,2026,48300000,,,budgeted,{SRC},strong,Index provisie understated 48.3m (spilindex Jun vs Jul BFP); tick671",
    f"bud_vl_gezondheidsindex_under_7m,vlaanderen_gov,2026,7000000,,,budgeted,{SRC},strong,Gezondheidsindex 3.2pct vs BA 2.7 impact ~7.0m extra; tick671",
    f"bud_finocas_capital_plan_177_5m,finocas,2026,177500000,,,budgeted,{SRC},strong,Finocas capital inject BA plan 177.5m; prior 140m 2025 not executed CoA unclear; tick671",
    f"bud_viapass_availability_99_3m,viapass,2026,99300000,,,budgeted,{SRC},strong,Viapass beschikbaarheidsvergoeding 99.3m path +5.2 (CO2 tariff); save 10m not realizable; tick671",
    f"bud_viapass_save_10m_not_realizable,viapass,2026,10000000,,,budgeted,{SRC},strong,Viapass 10m save retained but CoA says not contract-feasible; tick671",
    # Education residual
    f"bud_vl_levensbeschouwing_hold_save,vlaanderen_gov,2026,-9400000,,,budgeted,{SRC},strong,Levensbeschouwelijke vakken save -9.4 basisonderwijs wages on hold (RvS); wrong cut; tick671",
    f"bud_vl_levensbeschouwing_sec_hold,vlaanderen_gov,2026,-17500000,,,budgeted,{SRC},strong,Levensbeschouwelijke vakken -17.5m sec wages on hold; compensated Digisprong -22.3 + kwaliteit -4.6; tick671",
    f"bud_vl_digisprong_raid_24m,vlaanderen_gov,2026,-24000000,,,budgeted,{SRC},strong,Digisprong provisie raided total 24.0m to cover failed education saves (22.3+1.7); Digiplan risk; tick671",
    f"bud_vl_volwassenen_save_fail_50m,vlaanderen_gov,2026,50000000,,,budgeted,{SRC},strong,Volwassenenonderwijs rationalisatie target save 50m not met (wages -16.9-10.7 fees -19.6); one-off AGION/Digi/kwaliteit; tick671",
    f"bud_vl_volwassenen_fees_path_minus_19_6m,vlaanderen_gov,2026,-19600000,,,budgeted,{SRC},strong,Inschrijvingsgelden volwassenen path -19.6m (BO +33.4 to BA +13.8); tick671",
    # WVG residual
    f"bud_vl_wvg_reserves_save_12m,vlaanderen_gov,2026,12000000,,,budgeted,{SRC},strong,WVG activate historic reserves save 12.0m (Zorg 7.0 residual after 1.4 reshuffle); uncertain CoA; tick671",
    f"bud_vl_btz_gap_est_35_9m,vlaanderen_gov,2026,35900000,,,budgeted,{SRC},strong,CoA est BTZ basistegemoetkoming zorg shortfall 35.9m (half planned beds + control lag); tick671",
    # Culture media
    f"bud_asobv_fusion_save_0_8m,asobv,2026,800000,,,budgeted,{SRC},strong,ASOBV fusion wage save 0.8m (prior ASO+OBV cuts) retro 1Jan2026; dual FWB culture; tick671",
    f"bud_vrt_nieuwbouw_life_deficit_1_3m,vrt,2026,-1300000,,,budgeted,{SRC},strong,VRT nieuwbouw intertemporal deficit -1.3m over 2014-2044 (improved 4.6); autofinance claim; tick671",
    f"bud_vrt_nieuwbouw_repower_minus_7_1m,vrt,2026,-7100000,,,budgeted,{SRC},strong,VRT nieuwbouw RePowerEU subsidy path -7.1m in updated plan; tick671",
    # MOW GIP
    f"bud_vl_gip_2026_planned_3864m,vlaanderen_gov,2026,3864000000,,,budgeted,{SRC},strong,GIP actualisatie 2026 planned 3864m (GIP 2025-27 had 2424 for 2026); Oosterweel/leefbaarheid; tick671",
    f"bud_vl_gip_2026_baseline_2424m,vlaanderen_gov,2026,2424000000,,,budgeted,{SRC},strong,GIP 2025-2027 Jul2025 figure for 2026 was 2424m; tick671",
    f"bud_vl_gip_budget_shortfall_82_4m,vlaanderen_gov,2026,82400000,,,budgeted,{SRC},strong,CoA: at least 82.4m underfunded vs GIP 2026 (onteig 35 + AWV 24.5 + safety 26.2); tick671",
    f"bud_vl_gip_buffer_13_8m,vlaanderen_gov,2026,13800000,,,budgeted,{SRC},strong,GIP article residual buffer 13.8m price/expropriation; tick671",
    f"bud_lantis_pfas_842_8m,vlaanderen_gov,2026,842800000,,,budgeted,{SRC},strong,Lantis PFAS uitgaven 842.8m not in GIP; dual Oosterweel; tick671",
    # Credits residual
    f"bud_vl_mijnverbouw_vak_plus_350_3m,vlaanderen_gov,2026,350300000,,,budgeted,{SRC},strong,MijnVerbouwLening VAK +350.3m (280.2 rebook 2025 + 70.1 energy crisis); no VEK yet; tick671",
    f"bud_vl_school_energy_loans_vak_100m,vlaanderen_gov,2026,100000000,,,budgeted,{SRC},strong,Energieleningen scholen VAK +100m VEK unchanged; tick671",
    f"bud_vl_basiskoten_loans_vak_100m,vlaanderen_gov,2026,100000000,,,budgeted,{SRC},strong,Renteloze leningen basiskoten VAK +100m VEK unchanged; tick671",
    f"bud_vl_fluvius_vek_1100m_confirm,vlaanderen_gov,2026,1100000000,,,budgeted,{SRC},strong,Fluvius VEK 1100m of 1560 VAK multi-year equity reinforce; dual grid; tick671",
    # Dual package
    f"bud_dual_ratings_vl_wal_fwb_2026,gg_belgium,2026,0,,,budgeted,{SRC_DUAL},strong,Dual ratings 2026: VL Fitch AA-/Moody A1/SP AA- vs WAL Moody Baa1 vs FWB Moody A3; tick671",
    f"bud_dual_saldo_e2_vl_wal_fwb_2026,gg_belgium,2026,-7407500000,,,budgeted,{SRC_DUAL},strong,Dual Entity II saldo class VL -3.643 + WAL SEC -2.015 + FWB SEC -1.753 = -7.411bn (not TE-additive; metrics differ ESR/SEC); tick671",
]

cmt_rows = [
    f"cmt_vl_ba2026_saldo_debt_ratings,VL BA2026 saldo -3.64bn debt 57bn ratings dual,vlaanderen_gov,MVG,CoA BA2026 ch3+5,2026-06-19,2026,2026,56971100000,\"{{\"\"2026\"\":56971100000}}\",,active,,Debt+rating dual,Compare WAL/FWB,{SRC},strong,Vlaanderen>BA2026>debt,Direct 49.8bn Moody A1 Fitch AA-; tick671",
    f"cmt_vl_gip_shortfall_82m,GIP 2026 shortfall 82.4m dual Sofico,vlaanderen_gov,MOW GIP,CoA BA2026 7.5,2026-05-22,2026,2026,82400000,\"{{\"\"2026\"\":82400000}}\",,active,,Infra planning gap,Fund or cut GIP,{SRC},strong,Vlaanderen>MOW>GIP,GIP plan 3.86bn vs 2.42; Lantis PFAS 843m off; tick671",
    f"cmt_vl_digisprong_raid_24m,Digisprong provisie raided 24m for edu fail dual,vlaanderen_gov,OV Digiplan,CoA BA2026 7.2,2026-01-01,2026,2026,24000000,\"{{\"\"2026\"\":24000000}}\",,active,,Education save opacity,Restore Digiplan,{SRC},strong,Vlaanderen>OV>Digisprong,Levensbeschouwing hold + volwassenen fail; tick671",
    f"cmt_vl_fluvius_vek_1_1bn,Fluvius VEK 1.1bn equity dual grids,vlaanderen_gov,Fluvius via PMV,CoA BA2026,2025-09-19,2026,2029,1100000000,\"{{\"\"2026\"\":1100000000}}\",,active,,DSO equity dual,Outcome metrics,{SRC},strong,Vlaanderen>Fluvius,VAK multi-year 1.56bn; tick671",
    f"cmt_dual_vl_wal_fwb_ratings_2026,Dual ratings VL A1/AA- WAL Baa1 FWB A3,gg_belgium,Entity II ratings,CoA VL+WAL+FWB 2026,2026-04-01,2026,2026,0,\"{{\"\"2026\"\":0}}\",,active,,Rating dual map,Not euros,{SRC_DUAL},strong,Belgium>dual>ratings_2026,tick671",
    f"cmt_dual_e2_saldo_vl_wal_fwb_2026,Dual Entity II saldo VL+WAL+FWB ~7.4bn class,gg_belgium,Entity II,CoA BA/aju 2026,2026-06-30,2026,2026,7411000000,\"{{\"\"2026\"\":7411000000}}\",,active,,Dual deficit map,Metrics ESR vs SEC,{SRC_DUAL},strong,Belgium>dual>e2_saldo_2026,Not TE-additive; tick671",
]

lb_rows = [
    f"lb_vl_ba2026_saldo_3_64bn,VL BA2026 ESR saldo -3.64bn dual,Flanders,ops,Vlaanderen>BA2026>saldo,3642700000,0,Strong CoA: path -743m; doel -2.18bn after Oosterweel/VV; dual WAL/FWB SEC,strong,{SRC},MVG,Flanders deficit path,Primary,6.0,8.5,3,6.65,Publish onderbenutting detail,open,,tick671",
    f"lb_vl_debt_57bn_moody_a1_2026,VL debt 57bn Moody A1 Fitch AA- dual,Flanders,ops,Vlaanderen>schuld,56971100000,0,Strong CoA Table14 direct 49.8bn; Moody A1 dual WAL Baa1 FWB A3; ratio 91.6pct,strong,{SRC},bondholders,Debt dual ratings,Primary,6.5,9.0,2,6.95,SKF +113.5m corr FOI,open,,tick671",
    f"lb_vl_gip_shortfall_82m_2026,GIP 2026 budget shortfall 82.4m,Flanders,ops,Vlaanderen>MOW>GIP,82400000,0,Strong CoA: plan 3.86bn vs prior 2.42; underfund onteig/AWV/safety; dual Sofico,strong,{SRC},AWV Lantis,Infra planning opacity,Primary,7.5,6.0,2,6.55,Align GIP to budget,open,,tick671",
    f"lb_vl_digisprong_raid_24m_2026,Digisprong provisie raided 24m,Flanders,ops,Vlaanderen>OV>Digisprong,24000000,0,Strong CoA: covers failed levensbeschouwing+volwassenen saves; Digiplan risk dual,strong,{SRC},schools,Provisie specialty,Primary,8.0,5.5,2,6.55,Restore digital plan,open,,tick671",
    f"lb_lantis_pfas_843m_2026,Lantis PFAS 842.8m off GIP,Flanders,ops,Vlaanderen>Oosterweel>PFAS,842800000,0,Strong CoA not in GIP; dual Oosterweel stock,strong,{SRC},Lantis,Environmental liability,Primary,7.0,7.5,3,6.85,Disclose cash path,open,,tick671",
    f"lb_dual_e2_ratings_saldo_2026,Dual Entity II ratings+saldo VL/WAL/FWB,Belgium,ops,Belgium>dual>e2_2026,7411000000,0,Strong dual: VL -3.64 WAL -2.02 FWB -1.75; ratings AA-/A1 vs Baa1 vs A3; not TE-additive,strong,{SRC_DUAL},Entity II,Dual fiscal residual,Primary dual,6.5,8.5,3,6.85,Cross FOI,open,,tick671",
]

foi_row = (
    f"{GAP},Vlaanderen>BA2026>residual_L5,vlaanderen_gov,"
    "GIP 82.4m shortfall project list; Digisprong 24m raid destinations; Finocas 177.5/140m status; Viapass 10m save contract; BTZ 35.9m methodology; Lantis PFAS 842.8 cash path; SKF 113.5m neutralization; non-Maastricht hospital/autonomie stocks,"
    "CoA VL BA2026 residual strong tick671; L5 dual WAL/FWB,"
    f"5,Departement FB / MOW / OV / openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,https://www.vlaanderen.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_vl_gip_shortfall_82m|cmt_vl_digisprong_raid_24m|cmt_vl_ba2026_saldo_debt_ratings,"
    f"lb_vl_gip_shortfall_82m_2026|lb_vl_digisprong_raid_24m_2026|lb_vl_debt_57bn_moody_a1_2026,"
    f"{NOW},{NOW},tick671 CoA VL BA2026 primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Onderzoek aanpassing Vlaamse begroting 2026 (2026_28)

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: Departement Financiën en Begroting / MOW / Onderwijs / Team Openbaarheid
openbaarheid@vlaanderen.be
Herman Teirlinckgebouw Havenlaan 88 bus 20 1000 Brussel

Betreft: Openbaarheid — BA2026 residual (GIP, Digisprong, Finocas, Lantis PFAS, ratings)

Geachte,

Op grond van het Bestuursdecreet verzoek ik om:

1. GIP 2026: detail van de minstens 82,4 mEUR ondervoorziening (onteigening 35 /
   AWV 24,5 / verkeersveiligheid 26,2) en aansluiting begrotingsartikelen.
2. Digisprong-provisie: besteding van de 24,0 mEUR die elders is ingezet
   (levensbeschouwing hold + volwassenenonderwijs).
3. Finocas: stand van zaken kapitaalinbreng 177,5 mEUR 2026 en niet-uitgevoerde
   140 mEUR 2025.
4. Viapass: contractuele onderbouwing van de 10 mEUR besparing (Rekenhof:
   niet realiseerbaar).
5. Lantis PFAS 842,8 mEUR: kaspad 2025-2028 en relatie tot GIP/Oosterweel.
6. SKF-neutralisatie: berekening van de 113,5 mEUR schuldcorrectie Rekenhof.
7. Non-Maastricht: actualisatie ziekenhuisinfrastructuur 2.184,3 mEUR en
   autonomiefactor 473,8 mEUR.

Période: 2024-01-01 tot 2027-12-31.
Vorm: CSV/XLSX bij voorkeur.

Met vriendelijke groet,
[Naam]
```

## Notes agent
- Primary: CoA 2026_28 VL BA2026 (tick671). Dual ratings/saldo with WAL/FWB aju.
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **Flanders CoA BA2026 debt ratings GIP Digisprong dual WAL/FWB**)
- Found (primary CoA 2026_28): **Saldo BA -EUR3.643bn** path **-742.6** (rec **+665.4** dep **+1080.5** onderbenutting **-299.8**); doel **-EUR2.181bn** after Oosterweel **986.7** VV rec **324.9**/dep **800.1**. **Debt** consol **EUR56.971bn** direct **49.802** path **+6.799**; ratio **91.6%**; CoA SKF corr **+113.5m**; non-Maastricht hospital **2.184** autonomie **0.474**. **Ratings:** Fitch **AA-** / Moody **A1** / S&P **AA-** (dual WAL **Baa1** FWB **A3**). **FB:** buffer **+58.5** specialty; index under **48.3+7.0**; Finocas **177.5** unclear; Viapass **99.3**. **OV:** Digisprong raid **24.0** (levensbeschouwing hold + volwassenen fail **50**). **WVG:** reserves **12**; BTZ gap est **35.9**. **MOW:** GIP **3864** vs **2424** shortfall **82.4**; Lantis PFAS **842.8** off GIP; Fluvius VEK **1100**. Dual Entity II. Strong CoA; L5 FOI.
- Wrote: entities (+3); budgets (+50); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@680 in 9 ticks; rq_116 deferred
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
        f"tick{TICK} VL BA2026 residual dual ratings GIP Digisprong; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,vlaanderen_gov,"
        f"Next residual: VL BA2026 ch6 receipts residual or Omgeving/energie/wonen L5 or federal CoA 2026_22 dual.,,"
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

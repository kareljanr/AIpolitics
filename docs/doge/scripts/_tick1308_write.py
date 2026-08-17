#!/usr/bin/env python3
"""Surgical tick 1308 writes. Does NOT rewrite research_queue.csv wholesale."""
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-17T16:45:00Z"
SRC = "src_brsge_jr2025_bbc"
URL = "https://www.beerse.be/file/download/fc278cf7-4de5-419f-9e72-9d89ed7a4ff2/xBw9aZtcxpceeDvKf5AHoiVrUn7LtfQPj3m4NZo1o83d.pdf"
HP = "Vlaanderen>Gemeenten>Beerse>jr2025_L5"
GAP = "gap_brsge_fin_debt_13_82m_tussen_4_19m_pers_30_67m_l5"

def append_lf(path: Path, rows: list[str]) -> None:
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def patch_research_queue() -> None:
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if raw.endswith(b"\n"):
        body, last = raw[:-1].rsplit(b"\n", 1)
    else:
        body, last = raw.rsplit(b"\n", 1)
    last_s = last.decode("utf-8")
    if not last_s.startswith("rq_1308,"):
        raise SystemExit(f"expected last row rq_1308, got {last_s[:80]!r}")
    done = (
        "rq_1308,Stad+OCMW Beerse JR2025 GE residual,hole_fill,5,done,L5,city_beerse,"
        "Completed: Stad+OCMW Beerse JR2025 BBC text + GR + KBO; KBO 0207.505.764 / 0212.238.374; assets 103960480 / fin debt 13817644 / tussen 4186158 / pers 30670713 JUMP / AFM +2573644; FOI ready,"
        f"{GAP},"
        f"2026-08-17T16:00:00Z,{TS},"
        "tick1308 Stad+OCMW Beerse JR2025 GE residual; KBO 0207.505.764/0212.238.374; assets 103960480 fin debt 13817644 tussen 4186158 pers 30670713 JUMP AFM +2573644 gecorr +3052500 BBR -982836 cum 9264208 cash 9445482 DROP PnL +278410 OCMW expl -3572293 new loans 331504 leasing; AGB EVA 0 already 1307 werksub 300067 toegestane 799075; FOI ready not sent; next rq_1309 residual dual L5 VL"
    )
    spawn = (
        "rq_1309,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined (prior 1255-1308 done including Stad+OCMW Beerse 1308 / AGB Beerse 1307 / Stad+OCMW Vleteren 1306 / Stad+OCMW Pepingen 1305 / AGB Pepingen 1304 / Stad+OCMW Edegem 1303 / Stad+OCMW Wommelgem 1302 / Stad+OCMW Zonhoven 1301 / Stad+OCMW Kortenaken 1300 / AGB Kortenaken 1299); prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; leftover Maarkedal/Meulebeke/Londerzeel/Holsbeek/Merchtem/Zwalm/Wortegem-Petegem still unmined — take only if PDF fetches; Tervuren city / AGB Bexit if unmined and PDF downloads; skip already-mined Stad+OCMW Beerse 1308 / AGB Beerse 1307 / city Vleteren 1306 / city Pepingen 1305 / AGB Pepingen 1304 / city Edegem 1303 / AGB Edegem 1239 / city Wommelgem 1302 / city Zonhoven 1301 / city Kortenaken 1300 / AGB Kortenaken 1299 / city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / Deerlijk 981 / Zonnebeke 963 / AGB MMP1917 964 / Lochristi 927 / Tervuren 1226 / AGB Bexit 1225 / AGB Kinrooi 1230 / AGB Vilvoorde 1229 / AGB Beersel 1223; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht/Pelt AGB; skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Oostkamp 1131; skip Kuurne city already 957; skip Ternat/Lubbeek already mined; skip AGB Kapellen / Nieuwerkerken 1102 already mined; skip AGB Sport Hulshout JR2024-only; ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF,,"
        f"{TS},{TS},"
        "spawned tick1308 after Stad+OCMW Beerse JR2025 GE residual; next residual dual L5 VL"
    )
    new = body + b"\n" + done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n"
    p.write_bytes(new)
    print("research_queue patched: rq_1308=done + rq_1309 spawned; bytes", len(new))

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1308 Stad+OCMW Beerse JR2025 GE residual; KBO 0207.505.764/0212.238.374; assets 103960480 fin debt 13817644 tussen 4186158 pers 30670713 JUMP; FOI ready; next rq_1309 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\r\n"
        f"main,continuous,hole_fill,{TS},rq_1308,1308,no,{notes}\r\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten CRLF ticks=1308")

def append_sources() -> None:
    rows = [
        f"{SRC},Stad+OCMW Beerse BBC jaarrekening 2025 (official PDF),{URL},Lokaal bestuur Beerse,2026-08-17,budget,tick1308; BBC text PDF 139p / 8.1MB beerse.be; GR 28.05.2026 2026_GR_00079; RMW 28.05.2026 2026_RMW_00028; pub 01.06.2026; Jnl Budg 146968 Alg 4050078863; KBO 0207.505.764/0212.238.374; assets 103960480 fin debt 13817644 tussen 4186158 pers 30670713",
        "src_brsge_jr2025_gr,Gemeenteraad Beerse 28.05.2026 vaststelling JR2025 GE,https://www.beerse.be/file/download/f56ff831-947e-4b41-a014-4173a3543cd9/FVvejWhVpxWuzQSwYogBUGeHNfF8nDFcq2lWXHQ3d.pdf,Gemeenteraad Beerse,2026-08-17,budget,tick1308; 2026_GR_00079 goedgekeurd 20-3; BBR -982836 / cum 9264208 / AFM 2573644; AD Elle Verwaest / burgemeester Bart Craane / schepen financiën Bart Smans",
        "src_kbo_brsge_0207505764,KBO Gemeente Beerse 0207.505.764,https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207505764,KBO Public Search FOD Economie,2026-08-17,official_register,tick1308; city KBO 0207.505.764 / OCMW 0212.238.374; seat Heilaarstraat 6 / Gasthuisstraat 49 2340; NIS 13004; AD Verwaest / FD Hendrickx / burgemeester Craane",
    ]
    append_lf(DATA / "sources.csv", rows)
    print("sources +3")

def patch_entities() -> None:
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    old = (
        "city_beerse,Gemeente Beerse,Commune de Beerse,Municipality of Beerse,municipality,vlaanderen_gov,nl,https://www.beerse.be,info@beerse.be,Heilaarstraat 6 2340 Beerse,stub tick1307 for AGB dual residual parent; KBO 0207.505.764 / OCMW 0212.238.374; NIS 13004; city+OCMW JR2025 8.1MB live on beerse.be detail/624 — left unmined; distinct from city_beersel"
    )
    new = (
        "city_beerse,Gemeente Beerse,Commune de Beerse,Municipality of Beerse,municipality,vlaanderen_gov,nl,https://www.beerse.be,info@beerse.be,Heilaarstraat 6 2340 Beerse,tick1308 JR2025 GE residual; KBO 0207.505.764; NIS 13004; AD Elle Verwaest / FD Rob Hendrickx / burgemeester Bart Craane; assets 103960480 fin debt 13817644 tussen 4186158 pers 30670713 JUMP AFM +2573644; AGB already 1307; distinct from city_beersel; FOI ready"
    )
    if old.encode("utf-8") not in raw:
        raise SystemExit("city_beerse stub line not found for surgical patch")
    raw = raw.replace(old.encode("utf-8"), new.encode("utf-8"), 1)
    p.write_bytes(raw)
    ocmw = (
        "ocmw_beerse,OCMW Beerse,CPAS de Beerse,OCMW Beerse,municipality,city_beerse,nl,https://www.beerse.be,info@beerse.be,Gasthuisstraat 49 2340 Beerse,tick1308 JR2025 GE residual; KBO 0212.238.374; J3 expl -3572293 / T5 PnL -4155439 / cum +3449773 / equity 6315857; tussenkomst 4186158; FOI ready"
    )
    append_lf(p, [ocmw])
    print("entities city_beerse patched + ocmw_beerse")

def append_budgets() -> None:
    rows = [
        f"bud_brsge_assets_2025,city_beerse,2025,103960480,,,executed,{SRC},strong,J4 assets 103960480 vs 103736399; tick1308; primary BBC",
        f"bud_brsge_assets_2024,city_beerse,2024,103736399,,,executed,{SRC},strong,J4 YE2024 assets 103736399; tick1308; primary BBC",
        f"bud_brsge_cash_2025,city_beerse,2025,9445482,,,executed,{SRC},strong,J4 cash 9445482 vs 11625987 DROP; tick1308; primary BBC",
        f"bud_brsge_fva_2025,city_beerse,2025,25816911,,,executed,{SRC},strong,J4 FVA 25816911 (EVA 0 IGS 25580005 OCMW-ver 3450 other 233455); tick1308; primary BBC",
        f"bud_brsge_fva_igs_2025,city_beerse,2025,25580005,,,executed,{SRC},strong,J4/T5 IGS 25580005 reval 0; tick1308; primary BBC",
        f"bud_brsge_mva_2025,city_beerse,2025,59697273,,,executed,{SRC},strong,J4 MVA 59697273 leasing 1268200; tick1308; primary BBC",
        f"bud_brsge_leasing_2025,city_beerse,2025,1268200,,,executed,{SRC},strong,J4 leasing gemeenschapsgoederen 1268200; tick1308; primary BBC",
        f"bud_brsge_equity_2025,city_beerse,2025,77970176,,,executed,{SRC},strong,J4 nettoactief 77970176 (city 71654319 / OCMW 6315857); tick1308; primary BBC",
        f"bud_brsge_schulden_2025,city_beerse,2025,25990304,,,executed,{SRC},strong,J4 schulden 25990304; tick1308; primary BBC",
        f"bud_brsge_fin_debt_2025,city_beerse,2025,13817644,,,executed,{SRC},strong,J4/T4 fin debt 13817644 (LT 12068017 + ST due 1749628) vs 15179344; tick1308; primary BBC",
        f"bud_brsge_new_loans_2025,city_beerse,2025,331504,,,executed,{SRC},strong,T4/J3 new loans 331504 leasing; bank 0; tick1308; primary BBC",
        f"bud_brsge_afl_2025,city_beerse,2025,1693204,,,executed,{SRC},strong,J2/T4 periodieke afl 1693204; tick1308; primary BBC",
        f"bud_brsge_expl_2025,city_beerse,2025,4141175,,,executed,{SRC},strong,J2 exploitatiesaldo +4141175; tick1308; primary BBC",
        f"bud_brsge_expl_ontv_2025,city_beerse,2025,50252678,,,executed,{SRC},strong,J2 expl ontv 50252678 vs MJP 44473781; tick1308; primary BBC",
        f"bud_brsge_expl_uitg_2025,city_beerse,2025,46111502,,,executed,{SRC},strong,J2 expl uitg 46111502 vs MJP 42661049; tick1308; primary BBC",
        f"bud_brsge_expl_city_2025,city_beerse,2025,7713468,,,executed,{SRC},strong,Kengetallen/J3 city expl +7713468; tick1308; primary BBC",
        f"bud_brsge_expl_ocmw_2025,ocmw_beerse,2025,-3572293,,,executed,{SRC},strong,Kengetallen/J3 OCMW expl -3572293; tick1308; primary BBC",
        f"bud_brsge_invest_2025,city_beerse,2025,-3088909,,,executed,{SRC},strong,J2 invest -3088909 vs MJP -2968158; tick1308; primary BBC",
        f"bud_brsge_bbr_2025,city_beerse,2025,-982836,,,executed,{SRC},strong,J2/GR BBR boekjaar -982836 vs MJP -3286406; tick1308; primary BBC",
        f"bud_brsge_cum_bbr_2025,city_beerse,2025,9264208,,,executed,{SRC},strong,J2 gecumuleerd BBR 9264208 (prev 10247045); tick1308; primary BBC",
        f"bud_brsge_avail_bbr_2025,city_beerse,2025,6601822,,,executed,{SRC},strong,J2 beschikbaar BBR 6601822; tick1308; primary BBC",
        f"bud_brsge_afm_2025,city_beerse,2025,2573644,,,executed,{SRC},strong,J2/GR AFM +2573644 vs MJP 265514; tick1308; primary BBC",
        f"bud_brsge_gecorr_2025,city_beerse,2025,3052500,,,executed,{SRC},strong,J2 gecorr AFM +3052500; tick1308; primary BBC",
        f"bud_brsge_pnl_2025,city_beerse,2025,278410,,,executed,{SRC},strong,J5 PnL +278410 (ops -754573 / fin +1032982); tick1308; primary BBC",
        f"bud_brsge_pnl_city_2025,city_beerse,2025,4433849,,,executed,{SRC},strong,T5 city PnL +4433849; tick1308; primary BBC",
        f"bud_brsge_pnl_ocmw_2025,ocmw_beerse,2025,-4155439,,,executed,{SRC},strong,T5 OCMW PnL -4155439; tick1308; primary BBC",
        f"bud_brsge_tussen_2025,city_beerse,2025,4186158,,,executed,{SRC},strong,Kengetallen/T5 tussenkomst OCMW 4186158; tick1308; primary BBC",
        f"bud_brsge_pers_2025,city_beerse,2025,30670713,,,executed,{SRC},strong,J5/T2 bezoldigingen 30670713 JUMP vs 23520867; onderwijs other 10356195; tick1308; primary BBC",
        f"bud_brsge_pension_2025,city_beerse,2025,5963840,,,executed,{SRC},strong,J4 pension LT 5963840 vs 5258847; tick1308; primary BBC",
        f"bud_brsge_fiscal_2025,city_beerse,2025,20774849,,,executed,{SRC},strong,T2 fiscale ontvangsten 20774849; tick1308; primary BBC",
        f"bud_brsge_fiscal_ov_2025,city_beerse,2025,10515734,,,executed,{SRC},strong,T2 opcentiemen OV 10515734; tick1308; primary BBC",
        f"bud_brsge_fiscal_apb_2025,city_beerse,2025,8256453,,,executed,{SRC},strong,T2 APB 8256453; tick1308; primary BBC",
        f"bud_brsge_gemeentefonds_2025,city_beerse,2025,4736800,,,executed,{SRC},strong,T2 gemeentefonds 4736800; tick1308; primary BBC",
        f"bud_brsge_politie_2025,city_beerse,2025,3016457,,,executed,{SRC},strong,T2 politiezone werksub 3016457 + invest 155046; tick1308; primary BBC",
        f"bud_brsge_hvz_2025,city_beerse,2025,1252668,,,executed,{SRC},strong,T2 HVZ werksub 1252668 + invest 263587; tick1308; primary BBC",
        f"bud_brsge_agb_werksub_2025,city_beerse,2025,300067,,,executed,{SRC},strong,T2 AGB werksub 300067; AGB already 1307; tick1308; primary BBC",
        f"bud_brsge_toegestane_agb_2025,city_beerse,2025,799075,,,executed,{SRC},strong,Kengetallen/J3 toegestane leningen AGB 799075; tick1308; primary BBC",
        f"bud_brsge_intrest_2025,city_beerse,2025,441305,,,executed,{SRC},strong,Kengetallen intresten 441305; tick1308; primary BBC",
        f"bud_brsge_iva_2025,city_beerse,2025,1145965,,,executed,{SRC},strong,J4 IVA 1145965; tick1308; primary BBC",
        f"bud_brsge_st_schuld_2025,city_beerse,2025,7958447,,,executed,{SRC},strong,J4 ST schulden 7958447 vs 7315869; tick1308; primary BBC",
    ]
    append_lf(DATA / "budgets.csv", rows)
    print("budgets +40")

def append_commitments() -> None:
    legal = "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Beerse vastgesteld 28.05.2026"
    base = f"city_beerse,Inwoners Beerse / OCMW,{legal},2026-05-28,2025,2031"
    rows = [
        f"comm_brsge_fin_debt_13_82m_2025,Stad+OCMW Beerse YE2025 fin debt 13.818m,{base},13817644,,13817644,active,{URL},Local city+OCMW GE residual map VL JR2025 Beerse,Publish T4 per-loan creditors + city-to-AGB 0.799m,{SRC},strong,{HP},tick1308; LT 12068017 + ST due 1749628 vs 15179344; new loans 331504 leasing; primary BBC",
        f"comm_brsge_tussen_4_19m_2025,Stad+OCMW Beerse 2025 OCMW tussenkomst 4.186m,{base},4186158,,4186158,active,{URL},Local city+OCMW GE residual map VL JR2025 Beerse,Publish OCMW expl vs tussenkomst cashflow,{SRC},strong,{HP},tick1308; tussen 4186158 vs OCMW expl -3572293 / PnL -4155439; primary BBC",
        f"comm_brsge_pers_30_67m_2025,Stad+OCMW Beerse 2025 personnel 30.671m JUMP,{base},30670713,,30670713,active,{URL},Local city+OCMW GE residual map VL JR2025 Beerse,Publish VTE + onderwijs-other 10.356m recon,{SRC},strong,{HP},tick1308; pers 30670713 vs 23520867; onderwijs other 10356195 vs forfait 5000000; primary BBC",
        f"comm_brsge_politie_3_02m_2025,Stad+OCMW Beerse 2025 politiezone 3.016m,{base},3016457,,3016457,active,{URL},Local city+OCMW GE residual map VL JR2025 Beerse,Publish zone name + 2026-2031 pad,{SRC},strong,{HP},tick1308; politie 3016457 + HVZ 1252668; primary BBC",
        f"comm_brsge_bbr_neg_0_98m_2025,Stad+OCMW Beerse YE2025 BBR -0.983m,{base},982836,,982836,active,{URL},Local city+OCMW GE residual map VL JR2025 Beerse,Publish cash DROP vs invest path,{SRC},strong,{HP},tick1308; BBR -982836 / cum 9264208 / cash 9445482 DROP vs 11625987; primary BBC",
        f"comm_brsge_agb_loan_0_80m_2025,Stad+OCMW Beerse 2025 city-to-AGB loan 0.799m,{base},799075,,799075,active,{URL},Local city+OCMW GE residual map VL JR2025 Beerse,Publish beheersovereenkomst vs AGB 1307,{SRC},strong,{HP},tick1308; toegestane 799075 + AGB werksub 300067; AGB already 1307; primary BBC",
    ]
    append_lf(DATA / "commitments.csv", rows)
    print("commitments +6")

def append_leaderboard() -> None:
    meas = "assets 103960480 / fin debt 13817644 / tussen 4186158 / pers 30670713 / AFM +2573644 / BBR -982836"
    note = "tick1308; primary BBC JR2025 PDF; not TE-additive of 348bn; city GE FOI; distinct from AGB Beerse 1307"
    rows = [
        f"lb_brsge_fin_debt_13_82m_2025,Stad+OCMW Beerse YE2025 fin debt 13.82m,L5,local_budget_line,{HP},13817644,13817644,fin debt 13817644 (LT 12068017 + ST due 1749628) vs 15179344; new loans 331504 leasing,strong,{SRC},Inwoners Beerse / OCMW,Local city+OCMW GE residual map VL JR2025 Beerse,{meas},7.5,8.0,4.0,6.5,Publish T4 per-loan creditors + city-to-AGB 0.799m,active,,{note}",
        f"lb_brsge_tussen_4_19m_2025,Stad+OCMW Beerse 2025 OCMW tussenkomst 4.19m,L5,local_budget_line,{HP},4186158,4186158,tussenkomst 4186158 vs OCMW expl -3572293 / PnL -4155439; OCMW BBR 0,strong,{SRC},Inwoners Beerse / OCMW,Local city+OCMW GE residual map VL JR2025 Beerse,{meas},7.5,7.0,3.5,6.0,Publish OCMW expl vs tussenkomst cashflow,active,,{note}",
        f"lb_brsge_pers_30_67m_2025,Stad+OCMW Beerse 2025 personnel 30.67m JUMP,L5,local_budget_line,{HP},30670713,30670713,pers 30670713 JUMP vs 23520867; onderwijs other 10356195 vs forfait 5000000,strong,{SRC},Inwoners Beerse / OCMW,Local city+OCMW GE residual map VL JR2025 Beerse,{meas},7.0,8.5,3.5,6.0,Publish VTE + onderwijs-other recon,active,,{note}",
        f"lb_brsge_politie_3_02m_2025,Stad+OCMW Beerse 2025 politiezone 3.02m,L5,local_budget_line,{HP},3016457,3016457,politie werksub 3016457 + invest 155046; HVZ 1252668 + invest 263587,strong,{SRC},Inwoners Beerse / OCMW,Local city+OCMW GE residual map VL JR2025 Beerse,{meas},6.5,6.5,3.0,5.5,Publish zone name + 2026-2031 pad,active,,{note}",
        f"lb_brsge_bbr_neg_0_98m_2025,Stad+OCMW Beerse YE2025 BBR -0.98m,L5,local_budget_line,{HP},982836,982836,BBR year -982836 / cum 9264208 / avail 6601822; cash 9445482 DROP vs 11625987,strong,{SRC},Inwoners Beerse / OCMW,Local city+OCMW GE residual map VL JR2025 Beerse,{meas},6.0,6.0,3.0,5.0,Publish cash DROP vs invest path,active,,{note}",
        f"lb_brsge_pension_5_96m_2025,Stad+OCMW Beerse YE2025 pension LT 5.96m,L5,local_budget_line,{HP},5963840,5963840,pension LT 5963840 vs 5258847; city/OCMW split unpublished,strong,{SRC},Inwoners Beerse / OCMW,Local city+OCMW GE residual map VL JR2025 Beerse,{meas},6.0,6.5,3.5,5.5,Publish city/OCMW split + respo,active,,{note}",
        f"lb_brsge_igs_25_58m_2025,Stad+OCMW Beerse YE2025 IGS FVA 25.58m,L5,local_budget_line,{HP},25580005,25580005,IGS 25580005 reval 0; EVA 0 on city books; AGB already 1307,strong,{SRC},Inwoners Beerse / OCMW,Local city+OCMW GE residual map VL JR2025 Beerse,{meas},5.5,8.0,3.0,5.0,Publish IGS inventory per deelneming,active,,{note}",
    ]
    append_lf(DATA / "leaderboard.csv", rows)
    print("leaderboard +7")

def append_foi() -> None:
    row = (
        f"{GAP},"
        f"{HP},city_beerse,"
        "T4 per-loan creditors for fin debt 13817644 (new loans 331504 leasing; city-to-AGB 799075 already 1307) + J4 pension LT 5963840 city/OCMW split + responsabilisering + OCMW tussenkomst 4186158 vs expl -3572293 / PnL -4155439 + IGS FVA 25580005 inventory (reval 0; EVA 0) + VTE vs pers 30670713 JUMP (onderwijs other 10356195) + politiezone name behind 3016457 / HVZ 1252668 pad,"
        "Unmined leftover city+OCMW Beerse GE after AGB 1307 left the city package unmined. Official BBC PDF still downloads on beerse.be. Fin debt 13.818m declining. Tussenkomst 4.186m. Pers 30.671m JUMP. BBR year -0.983m / cash DROP 2.181m. AGB EVA 0 already 1307.,"
        "8,Lokaal Bestuur Beerse (gemeente + OCMW),info@beerse.be,Heilaarstraat 6 2340 Beerse,"
        f"docs/doge/foi/drafts/{GAP}.md,"
        "ready,2026-08-17,,,,,comm_brsge_fin_debt_13_82m_2025,lb_brsge_fin_debt_13_82m_2025,"
        f"{TS},{TS},tick1308; ready not sent; do not send without human OK; primary BBC euros"
    )
    append_lf(DATA / "foi_queue.csv", [row])
    print("foi_queue +1 ready")

def append_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    block = f"""
### Tick 1308 - 2026-08-17 - rq_1308 Stad+OCMW Beerse GE residual
- Unit: Stad + OCMW Beerse JR2025 GE package after residual dual hunt (KBO 0207.505.764 / 0212.238.374; BBC text PDF on beerse.be 139p / 8.1MB; GR 28.05.2026 2026_GR_00079; RMW 28.05.2026 2026_RMW_00028; pub 01.06.2026; Jnl. Budg. 146968 / Alg. 4050078863). PREFER NEXT leftover city GE after AGB 1307 confirmed the PDF live on the same bekendmaking detail/624. Has AGB (T5 EVA 0 on city books; T2 AGB werksub 300067; city-to-AGB toegestane leningen 799075 already mined as AGB new loans 1307). Seat city Heilaarstraat 6 / OCMW Gasthuisstraat 49 2340. AD Elle Verwaest / FD Rob Hendrickx / burgemeester Bart Craane / schepen financiën Bart Smans. NIS 13004. Distinct from AGB Beerse 1307 / AGB Beersel 1223 / city Beersel 905. Hunt skipped already-mined AGB cluster + Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS / already-mined AGB Beerse 1307 / city Vleteren 1306 / city Pepingen 1305. Leftover Maarkedal official still JR2024-only; Meulebeke fused into Tielt (JR2024-only); Londerzeel / Holsbeek / Merchtem / Zwalm / Wortegem-Petegem still no JR2025 PDF. Official city BBC PDF still downloads. Not an every-10 tick.
- EUR strong (primary BBC J2 / J3 / J4 / J5 / T2 / T4 / T5 + GR/RMW): assets 103.960.480 (was 103.736.399); cash 9.445.482 vs 11.625.987 DROP; FVA 25.816.911 (EVA 0 + IGS 25.580.005 + OCMW-ver 3.450 + other 233.455; IGS reval 0); MVA 59.697.273 leasing 1.268.200; fin debt 13.817.644 (LT 12.068.017 + ST due 1.749.628) vs 15.179.344; new loans 331.504 leasing; periodieke afl 1.693.204; pension LT 5.963.840 vs 5.258.847; expl +4.141.175 (ontv 50.252.678 / uitg 46.111.502; city +7.713.468 / OCMW −3.572.293); invest −3.088.909 vs MJP −2.968.158; BBR year −982.836 / cum 9.264.208 (prev 10.247.045); avail 6.601.822; AFM +2.573.644 / gecorr +3.052.500; PnL +278.410 (city +4.433.849 / OCMW −4.155.439; ops −754.573 / fin +1.032.982); tussenkomst 4.186.158; OCMW cum +3.449.773 / equity +6.315.857; pers 30.670.713 JUMP vs 23.520.867; fiscal 20.774.849 (OV 10.515.734 + APB 8.256.453); gemeentefonds 4.736.800; politie 3.016.457 + HVZ 1.252.668; AGB werksub 300.067. VTE unpublished. Politiezone-naam unpublished in extract.
- CSVs: sources+3/entities(update city stub + new OCMW)/budgets+40/commitments+6/leaderboard+7 + FOI ready `{GAP}` (not sent); rq_1308=done; spawn rq_1309; ticks=1308. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (Stad+OCMW Beerse). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1309 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; leftover Maarkedal/Meulebeke/Londerzeel/Holsbeek/Merchtem/Zwalm/Wortegem-Petegem only if a PDF now downloads; Tervuren city / AGB Bexit if unmined and PDF downloads; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS / already-mined city Beerse 1308 / AGB Beerse 1307 / city Vleteren 1306 / city Pepingen 1305 / AGB Pepingen 1304 unless a fetchable JR appears).
"""
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

def main() -> None:
    patch_research_queue()
    write_loop_state()
    append_sources()
    patch_entities()
    append_budgets()
    append_commitments()
    append_leaderboard()
    append_foi()
    append_log()
    print("tick1308 write OK")

if __name__ == "__main__":
    main()

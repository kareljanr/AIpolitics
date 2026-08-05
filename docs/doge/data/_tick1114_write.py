# -*- coding: utf-8 -*-
"""tick 1114 — Gemeente+OCMW Evergem JR2025 dual residual"""
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

TICK = 1114
UTC = "2026-08-11T22:30:00Z"
SRC = "src_evergem_jr2025"
ENT = "city_evergem"
GAP = "gap_eve_ocmw_toelagen_pension_invest_l5"
URL = "https://www.evergem.be/jaarrekening"
# primary: file/download/113865 Beleidsrapport GR 22.06.2026

F = dict(
    assets=241166720,
    assets_was=227675045,
    equity=206730657,
    debt_total=34436063,
    fin_debt=4147958,
    fin_debt_lt=3373446,
    fin_debt_st=774512,
    fin_debt_was=4234070,
    new_loans=740610,
    repayments=826723,
    cash=52226980,
    cash_was=52309650,
    pension_lt=19387493,
    pension_was=18186696,
    fva_igs=28644716,
    fva_eva=1299678,
    fva_ocmw_ver=3587974,
    herwaard=6927462,
    leasing_mva=3184388,  # 2625181+559207
    expl_ont=76223374,
    expl_uit=62491238,
    expl_saldo=13732135,
    afm=13453260,
    afm_gecorr=13941257,
    bbr=56969420,
    budget_result=1433447,
    cum_br=57216527,
    onbeschikbaar=247107,
    pnl=6807318,
    fiscal=35482997,
    personnel=33035476,
    toelagen=10960303,
    police=5828444,
    fire=1924694,
    agb_toel=1438047,
    welzijn=1023091,
    eredienst=219809,
    andere_toel=526217,
    hulp_ocmw=2071582,
    invest_uit=16264210,
    invest_capex=15614964,
    invest_ont=3807087,
    invest_saldo=-12457123,
    invest_mjp=18562390,
    invest_subs=649246,
    ocmw_cover=3667402,
    ocmw_pnl=-6298569,
    ocmw_equity_total=-3549794,
    ocmw_expl_gap=3067912,  # from kengetallen OCMW expl saldo neg
    agb_bbr=3074040,
    agb_afm=121634,
    mjp_debt_2026=5358183,
    mjp_debt_2027=9068389,
    mjp_new_2026=2141123,
    mjp_new_2027=4641123,
    debt_per_capita=113,
    goederen=15793230,
    fin_exp=89160,
)


def append_csv(path: Path, rows: list[str]):
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")


def main():
    bud = []
    def b(bid, amt, note):
        bud.append(f"{bid},{ENT},2025,{amt},,,bbc_jr_realized,{SRC},strong,{note}")

    b("bud_eve_assets_2025", F["assets"], "Assets YE2025 241.167m JUMP (was 227.675m); tick1114")
    b("bud_eve_equity_2025", F["equity"], "Nettoactief YE2025 206.731m JUMP; tick1114")
    b("bud_eve_debt_total_2025", F["debt_total"], "Total schulden YE2025 34.436m JUMP; tick1114")
    b("bud_eve_fin_debt_2025", F["fin_debt"], "Fin debt YE2025 4.148m LOW DECLINE FOI (was 4.234m); tick1114")
    b("bud_eve_fin_debt_lt_2025", F["fin_debt_lt"], "Fin debt LT YE2025 3.373m; tick1114")
    b("bud_eve_fin_debt_st_2025", F["fin_debt_st"], "Fin debt ST due YE2025 0.775m; tick1114")
    b("bud_eve_new_loans_2025", F["new_loans"], "New loans 0.741m modest; tick1114")
    b("bud_eve_repayments_2025", F["repayments"], "Periodieke aflossingen 0.827m; tick1114")
    b("bud_eve_cash_2025", F["cash"], "Cash YE2025 52.227m VERY HIGH stable; tick1114")
    b("bud_eve_pension_lt_2025", F["pension_lt"], "Pension LT 19.387m JUMP FOI (was 18.187m); tick1114")
    b("bud_eve_fva_igs_2025", F["fva_igs"], "FVA IGS YE2025 28.645m HIGH FOI; tick1114")
    b("bud_eve_fva_eva_2025", F["fva_eva"], "FVA EVA/AGB 1.300m FOI; tick1114")
    b("bud_eve_fva_ocmw_ver_2025", F["fva_ocmw_ver"], "FVA OCMW-verenigingen 3.588m FOI; tick1114")
    b("bud_eve_herwaard_2025", F["herwaard"], "Herwaarderingsreserves 6.927m; tick1114")
    b("bud_eve_leasing_mva_2025", F["leasing_mva"], "Leasing MVA YE2025 3.184m; tick1114")
    b("bud_eve_expl_ontvangsten_2025", F["expl_ont"], "Exploitatie ontvangsten 76.223m; tick1114")
    b("bud_eve_expl_uitgaven_2025", F["expl_uit"], "Exploitatie uitgaven 62.491m; tick1114")
    b("bud_eve_expl_saldo_2025", F["expl_saldo"], "Exploitatiesaldo +13.732m VERY STRONG; tick1114")
    b("bud_eve_afm_2025", F["afm"], "AFM +13.453m VERY STRONG; tick1114")
    b("bud_eve_afm_gecorr_2025", F["afm_gecorr"], "AFM gecorrigeerd +13.941m VERY STRONG; tick1114")
    b("bud_eve_bbr_2025", F["bbr"], "BBR 56.969m VERY HIGH; tick1114")
    b("bud_eve_budget_result_2025", F["budget_result"], "Budget +1.433m POS (MJP was -5.187m); tick1114")
    b("bud_eve_pnl_2025", F["pnl"], "P&L +6.807m FLIP FOI (was -3.320m); tick1114")
    b("bud_eve_fiscal_2025", F["fiscal"], "Fiscale opbrengsten 35.483m; tick1114")
    b("bud_eve_personnel_2025", F["personnel"], "Personeel 33.035m; tick1114")
    b("bud_eve_toelagen_2025", F["toelagen"], "Toegestane werkingssubsidies 10.960m FOI; tick1114")
    b("bud_eve_police_2025", F["police"], "Politiezone toelage 5.828m FOI; tick1114")
    b("bud_eve_fire_2025", F["fire"], "HVZ toelage 1.925m; tick1114")
    b("bud_eve_agb_toelagen_2025", F["agb_toel"], "AGB toelagen 1.438m FOI; tick1114")
    b("bud_eve_welzijn_toelagen_2025", F["welzijn"], "Welzijnsverenigingen toelage 1.023m FOI; tick1114")
    b("bud_eve_andere_toelagen_2025", F["andere_toel"], "Andere toelagen 0.526m FOI; tick1114")
    b("bud_eve_hulp_ocmw_2025", F["hulp_ocmw"], "OCMW individuele hulp 2.072m; tick1114")
    b("bud_eve_invest_uitgaven_2025", F["invest_uit"], "Invest 16.264m vs MJP 18.562m UNDERSPEND FOI; tick1114")
    b("bud_eve_invest_capex_2025", F["invest_capex"], "Investeringen (capex kengetallen) 15.615m; tick1114")
    b("bud_eve_invest_mjp_2025", F["invest_mjp"], "MJP invest uitgaven 18.562m; tick1114")
    b("bud_eve_invest_subs_2025", F["invest_subs"], "Toegestane invest-subs 0.649m; tick1114")
    b("bud_eve_ocmw_cover_2025", F["ocmw_cover"], "OCMW cover 3.667m FULL FOI (OCMW P&L -6.299m DEEP); tick1114")
    b("bud_eve_ocmw_pnl_2025", F["ocmw_pnl"], "OCMW P&L -6.299m DEEP FOI; tick1114")
    b("bud_eve_ocmw_equity_2025", F["ocmw_equity_total"], "OCMW total equity -3.550m DEEP FOI; tick1114")
    b("bud_eve_ocmw_expl_gap_2025", F["ocmw_expl_gap"], "OCMW expl saldo -3.068m FOI; tick1114")
    b("bud_eve_agb_bbr_2025", F["agb_bbr"], "AGB BBR consol 3.074m FOI; tick1114")
    b("bud_eve_mjp_debt_2027", F["mjp_debt_2027"], "MJP fin debt YE2027 9.068m RAMP FOI; tick1114")
    b("bud_eve_debt_per_capita_2025", F["debt_per_capita"], "Schuld per inwoner 113 EUR VERY LOW; tick1114")
    b("bud_eve_goederen_2025", F["goederen"], "Goederen en diensten 15.793m; tick1114")
    append_csv(DATA / "budgets.csv", bud)

    under = F["invest_mjp"] - F["invest_uit"]
    pen_jump = F["pension_lt"] - F["pension_was"]
    debt_ramp = F["mjp_debt_2027"] - F["fin_debt"]

    comm = [
        f"comm_eve_fin_debt_2025,Evergem fin debt stock YE2025 4.148m LOW,{ENT},creditors,BBC JR2025,,2025,2045,{F['fin_debt']},{{2025:{F['fin_debt']}}},{F['fin_debt']},active,,Capital finance LOW DECLINE,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>debt,tick1114; debt/capita 113 EUR",
        f"comm_eve_cash_2025,Evergem cash 52.227m VERY HIGH 2025,{ENT},treasury,BBC JR2025,,2025,2025,{F['cash']},{{2025:{F['cash']}}},0,active,,Cash VERY HIGH FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>cash,tick1114",
        f"comm_eve_ocmw_cover_2025,Evergem OCMW cover FULL 3.667m 2025,{ENT},OCMW Evergem,BBC JR2025,,2025,2025,{F['ocmw_cover']},{{2025:{F['ocmw_cover']}}},0,active,,Cover FULL FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>ocmw,tick1114; OCMW P&L -6.299m equity -3.550m",
        f"comm_eve_toelagen_2025,Evergem toelagen werking 10.960m 2025,{ENT},PZ/HVZ/AGB/other,BBC JR2025 T2,,2025,2025,{F['toelagen']},{{2025:{F['toelagen']}}},0,active,,Named matrix FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>toelagen,tick1114; police 5.828",
        f"comm_eve_pension_2025,Evergem pension LT 19.387m JUMP 2025,{ENT},pension provision,BBC JR2025,,2025,2025,{F['pension_lt']},{{2025:{F['pension_lt']}}},0,active,,Pension JUMP FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>pension,tick1114; was 18.187m",
        f"comm_eve_invest_underspend_2025,Evergem invest 16.26 vs MJP 18.56 UNDERSPEND 2025,{ENT},Capital program,BBC JR2025,,2025,2025,{F['invest_uit']},{{2025:{F['invest_uit']}}},0,active,,UNDERSPEND FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>invest,tick1114",
        f"comm_eve_mjp_debt_ramp_2027,Evergem MJP fin debt ramp YE2027 9.068m,{ENT},creditors,BBC JR2025 T4 MJP,,2026,2027,{F['mjp_debt_2027']},{{2026:{F['mjp_debt_2026']},2027:{F['mjp_debt_2027']}}},{F['mjp_debt_2027']},planned,,Debt ramp FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>debt_mjp,tick1114",
        f"comm_eve_agb_bbr_2025,Evergem AGB BBR consol 3.074m 2025,{ENT},AGB Evergem,BBC JR2025 J2 consol,,2025,2025,{F['agb_bbr']},{{2025:{F['agb_bbr']}}},0,active,,AGB dual FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB,tick1114",
    ]
    append_csv(DATA / "commitments.csv", comm)

    lb_note = "tick1114; primary Evergem JR2025; dual residual after Langemark-Poelkapelle; not TE-additive"

    def lb(iid, name, annual, abs_s, cost_s, diff_s, pri, cut):
        return (
            f"{iid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>Evergem_L5,"
            f"{annual},{annual},JR2025 dual residual map VL,strong,{SRC},"
            f"Evergem residents,Local dual residual map VL JR2025,"
            f"JR2025 BBC Evergem GEOC realized figures,"
            f"{abs_s},{cost_s},{diff_s},{pri},{cut},active,,{lb_note}"
        )

    lbs = [
        lb("lb_eve_cash_52_23m_2025", "Evergem cash 52.23m VERY HIGH FOI residual",
           F["cash"], 6.0, 7.5, 3.5, 6.55, "Treasury FOI"),
        lb("lb_eve_bbr_56_97m_2025", "Evergem BBR 56.97m VERY HIGH FOI residual",
           F["bbr"], 5.5, 7.5, 3.5, 6.35, "Keep BBR path"),
        lb("lb_eve_afm_13_45m_2025", "Evergem AFM +13.45m VERY STRONG FOI residual",
           F["afm"], 5.0, 5.5, 3.0, 5.45, "Keep AFM path"),
        lb("lb_eve_ocmw_cover_3_67m_2025", "Evergem OCMW cover FULL 3.67m FOI residual",
           F["ocmw_cover"], 8.5, 5.0, 3.5, 6.75, "Cover policy FOI"),
        lb("lb_eve_ocmw_pnl_neg_6_30m_2025", "Evergem OCMW P&L -6.30m DEEP FOI residual",
           abs(F["ocmw_pnl"]), 9.0, 5.5, 3.5, 7.0, "OCMW structural FOI"),
        lb("lb_eve_toelagen_10_96m_2025", "Evergem toelagen 10.96m FOI residual",
           F["toelagen"], 7.0, 5.5, 3.5, 6.15, "Named matrix FOI"),
        lb("lb_eve_pension_19_39m_2025", "Evergem pension LT 19.39m JUMP FOI residual",
           F["pension_lt"], 7.5, 5.5, 3.5, 6.35, "Pension path FOI"),
        lb("lb_eve_police_5_83m_2025", "Evergem police toelage 5.83m FOI residual",
           F["police"], 6.0, 5.5, 3.5, 5.75, "PZ path FOI"),
        lb("lb_eve_invest_underspend_2025", "Evergem invest 16.26 vs MJP 18.56 UNDERSPEND FOI residual",
           under, 7.0, 4.5, 3.5, 5.85, "Invest path FOI"),
        lb("lb_eve_mjp_debt_ramp_2027", "Evergem MJP fin debt ramp YE2027 9.07m FOI residual",
           debt_ramp, 7.5, 5.0, 3.5, 6.25, "Debt ramp FOI"),
        lb("lb_eve_fin_debt_4_15m_2025", "Evergem fin debt 4.15m LOW FOI residual",
           F["fin_debt"], 5.0, 5.0, 3.5, 5.0, "Debt stock FOI"),
        lb("lb_eve_pnl_flip_6_81m_2025", "Evergem P&L flip +6.81m FOI residual",
           F["pnl"], 7.0, 5.5, 3.0, 6.25, "Keep FLIP path"),
    ]
    append_csv(DATA / "leaderboard.csv", lbs)

    src_row = (
        f"{SRC},Gemeente+OCMW Evergem BBC Jaarrekening 2025,{URL},"
        f"Gemeente Evergem,2026-08-11,primary_pdf,"
        f"tick1114; 499p text; KBO GE 0207.451.128 / OCMW 0212.212.244; NIS 44019; "
        f"AD Danny Coene FD Christ Coquyt; F. De Kokerlaan 11 9940 Evergem; GR 22.06.2026; "
        f"assets 241.167m cash 52.227m VERY HIGH fin debt 4.148m LOW AFM +13.453m BBR 56.969m "
        f"budget +1.433m P&L +6.807m FLIP toelagen 10.960m police 5.828m OCMW cover 3.667m FULL "
        f"OCMW P&L -6.299m DEEP equity -3.550m pension 19.387m; "
        f"primary PDF staged docs/doge/data/_tmp/evergem_jr2025.pdf"
    )
    append_csv(DATA / "sources.csv", [src_row])

    ent_row = (
        f"{ENT},Gemeente Evergem,Commune d'Evergem,Municipality of Evergem,"
        f"municipality,vlaanderen_gov,nl,https://www.evergem.be,info@evergem.be,"
        f"F. De Kokerlaan 11 9940 Evergem,"
        f"JR2025 dual residual tick1114; KBO 0207.451.128 / OCMW 0212.212.244; "
        f"assets 241.167m cash 52.227m VERY HIGH fin debt 4.148m LOW AFM +13.453m BBR 56.969m "
        f"toelagen 10.960m OCMW cover 3.667m FULL OCMW P&L -6.299m DEEP; "
        f"AD Danny Coene FD Christ Coquyt"
    )
    append_csv(DATA / "entities.csv", [ent_row])

    foi_row = (
        f"{GAP},Vlaanderen>Gemeenten>Evergem>ocmw_toelagen_pension_invest_L5,{ENT},"
        f"\"OCMW cover FULL 3.667m vs OCMW P&L -6.299m DEEP and total equity -3.550m multi-year path; "
        f"toelagen matrix within 10.960m (police 5.828 / fire 1.925 / AGB 1.438 / welzijn 1.023 / andere "
        f"0.526) named >=50k; pension JUMP 18.187to19.387m actuarial; invest underspend 16.26 vs MJP "
        f"18.56; MJP debt ramp YE2027 9.068m (new 2.141m 2026 + 4.641m 2027); FVA IGS 28.645 + OCMW-ver "
        f"3.588 + EVA 1.300 composition; AGB full JR residual\","
        f"\"Large Oost-Vl muni with VERY HIGH cash 52m / AFM +13m / BBR 57m and VERY LOW debt/capita "
        f"113 EUR but DEEP OCMW structural hole FOI-adjacent dual residual\","
        f"9,Gemeente Evergem,info@evergem.be,F. De Kokerlaan 11 9940 Evergem,"
        f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-11,,,,,"
        f"comm_eve_ocmw_cover_2025,lb_eve_ocmw_pnl_neg_6_30m_2025,"
        f"{UTC},{UTC},tick1114; ready not sent; do not send without human OK"
    )
    append_csv(DATA / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = f"""# FOI draft — {GAP}

**Status:** ready (NOT sent)  
**Gap ID:** {GAP}  
**Tick:** {TICK}  

## Recipient

- Gemeente Evergem openbaarheid / financieel directeur Christ Coquyt  
- E-mail: info@evergem.be  
- Adres: F. De Kokerlaan 11, 9940 Evergem  

## Subject

Openbaarheid — Jaarrekening 2025 Gemeente/OCMW Evergem: OCMW, toelagen, pensioen, investeringen

## Body (NL)

```text
[Naam]
[Adres]
[E-mail]
[Datum]

Aan: Gemeente Evergem
t.a.v. de financieel directeur

Betreft: Verzoek openbaarheid — jaarrekening 2025 Gemeente en OCMW Evergem

Geachte,

Op grond van de regels inzake openbaarheid van bestuur vraag ik de volgende
documenten en toelichtingen.

### 1. Reeds openbaar (BBC JR2025; evergem.be; GR 22.06.2026)

- Activa **EUR241,167m JUMP**; nettoactief **EUR206,731m**; fin. schuld
  **EUR4,148m LOW** (LT 3,373 / ST 0,775; schuld/inwoner **EUR113**); nieuwe
  leningen **EUR0,741m**; cash **EUR52,227m VERY HIGH**; pensioen LT
  **EUR19,387m JUMP** (was 18,187m); FVA IGS **EUR28,645m** + OCMW-ver
  **EUR3,588m** + EVA **EUR1,300m**; AFM **+EUR13,453m**; BBR **EUR56,969m
  VERY HIGH**; budget **+EUR1,433m**; P&L **+EUR6,807m FLIP**; toelagen
  **EUR10,960m** (politie **EUR5,828m** / HVZ **EUR1,925m** / AGB
  **EUR1,438m** / welzijn **EUR1,023m** / andere **EUR0,526m**); invest
  **EUR16,264m** vs MJP **EUR18,562m UNDERSPEND**; OCMW-tussenkomst
  **EUR3,667m FULL** (OCMW P&L **−EUR6,299m DEEP**; OCMW equity
  **−EUR3,550m DEEP**); AGB BBR consol **EUR3,074m**; MJP fin. schuld YE2027
  **EUR9,068m**.

### 2. Gevraagde stukken / toelichtingen

1. **OCMW cover FULL EUR3,667m** vs OCMW P&L −EUR6,299m en equity −EUR3,550m:
   multi-year liquiditeitspad 2020–2026, WZC/thuiszorg drivers.
2. **Toelagen-matrix** binnen EUR10,960m: nominatieve lijst ≥ EUR50k (politie,
   HVZ, AGB, welzijnsverenigingen, andere).
3. **Pensioen LT JUMP** 18,187 → 19,387m: actuariële aannames / responsabilisering.
4. **Invest underspend** 16,26 vs MJP 18,56m: projectenlijst en overdrachten 2026.
5. **MJP schuld-ramp YE2027 EUR9,068m** (nieuwe leningen 2026–2027): projecten
   en kredietgevers.
6. **FVA IGS / OCMW-ver / EVA**: deelnemingenmatrix.
7. **AGB full JR2025 residual** (BBR EUR3,074m; AFM +EUR0,122m): performance vs
   toelage.

Gelieve te antwoorden binnen de wettelijke termijn. Digitaal leveren (PDF) heeft
de voorkeur.

Met vriendelijke groeten,

[Naam]
[Contact]
```

## Notes

- Primary source: BBC JR2025 Gemeente+OCMW Evergem (499p; GR 22.06.2026; AD Coene FD Coquyt).  
- **Do not send** without human OK.  
- Tick 1114 dual residual after Langemark-Poelkapelle (tick1113).
"""
    (FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

    rq_path = DATA / "research_queue.csv"
    lines = rq_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("rq_1114,"):
            out.append(
                "rq_1114,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
                "Evergem GE+OCMW JR2025 dual residual,"
                f"{GAP},2026-08-11T22:00:00Z,{UTC},"
                "tick1114 Evergem assets 241.167m cash 52.227m VERY HIGH fin debt 4.148m LOW AFM +13.453m "
                "BBR 56.969m OCMW cover 3.667m FULL OCMW P&L -6.299m DEEP toelagen 10.960m; FOI ready"
            )
        else:
            out.append(line)
    out.append(
        "rq_1115,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
        "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen login-blocked / Vorselaar docs-only / "
        "Kalmthout / Bornem JR2024-only / De Panne OCR / Schelle GE+OCMW if published / Erpe-Mere if public / other); "
        "prefer FOI-adjacent L5; skip rq_116,"
        f",2026-08-11T22:30:00Z,{UTC},"
        "spawned tick1114 after Evergem dual residual; next residual dual L5; progress@1120 in 6"
    )
    rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    state = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{UTC},rq_1114,1114,no,"
        "tick1114 Evergem GE+OCMW JR2025 dual residual; FOI gap_eve_ocmw_toelagen_pension_invest_l5 prio9 ready; "
        "assets 241.167m cash 52.227m VERY HIGH equity 206.731m fin debt 4.148m LOW debt/capita 113 AFM +13.453m "
        "BBR 56.969m VERY HIGH budget +1.433m P&L +6.807m FLIP toelagen 10.960m police 5.828m OCMW cover 3.667m FULL "
        "OCMW P&L -6.299m DEEP equity -3.550m pension 19.387m JUMP; next residual dual L5 rq_1115; "
        "progress@1120 in 6; rq_116 deferred\n"
    )
    (DATA / "loop_state.csv").write_text(state, encoding="utf-8")

    log_entry = f"""
### Tick 1114 - {UTC}

- Unit: **rq_1114** (FOI-adjacent residual dual - **Gemeente+OCMW Evergem Jaarrekening 2025** + Langemark-Poelkapelle dual residual)
- Found (strong primary BBC JR2025 499p text; evergem.be; GR 22.06.2026; KBO GE 0207.451.128 / OCMW 0212.212.244; NIS 44019; F. De Kokerlaan 11 9940; AD Danny Coene FD Christ Coquyt; GE+OCMW + AGB consol):
  - Assets **EUR241.167m JUMP** (was **EUR227.675m**) / equity **EUR206.731m JUMP** / debt total **EUR34.436m** / fin debt **EUR4.148m LOW DECLINE FOI** (LT **EUR3.373m** / ST due **EUR0.775m**; was **EUR4.234m**; debt/capita **EUR113 VERY LOW**)
  - New loans **EUR0.741m** / repayments **EUR0.827m**
  - Cash **EUR52.227m VERY HIGH** stable (was **EUR52.310m**) / pension **EUR19.387m JUMP FOI** (was **EUR18.187m**)
  - FVA IGS **EUR28.645m** / FVA EVA **EUR1.300m** / FVA OCMW-ver **EUR3.588m** / herwaard **EUR6.927m** / leasing MVA **EUR3.184m**
  - Exploitatie: ontvangsten **EUR76.223m** / uitgaven **EUR62.491m** / saldo **+EUR13.732m VERY STRONG**
  - AFM **+EUR13.453m VERY STRONG** (gecorr **+EUR13.941m**) / BBR **EUR56.969m VERY HIGH** / onbeschikbaar **EUR0.247m** / budget **+EUR1.433m POS** (MJP was **−EUR5.187m**) / P&L **+EUR6.807m FLIP FOI** (was **−EUR3.320m**)
  - Fiscal **EUR35.483m** / personnel **EUR33.035m**
  - Toelagen **EUR10.960m FOI** (police **EUR5.828m** / fire **EUR1.925m** / AGB **EUR1.438m** / welzijn **EUR1.023m** / eredienst **EUR0.220m** / andere **EUR0.526m**)
  - Invest **EUR16.264m** vs MJP **EUR18.562m UNDERSPEND FOI** / invest-subs **EUR0.649m**
  - OCMW cover **EUR3.667m FULL FOI** / OCMW P&L **−EUR6.299m DEEP FOI** / OCMW total equity **−EUR3.550m DEEP** / OCMW expl gap **−EUR3.068m** / OCMW hulp **EUR2.072m**
  - AGB BBR consol **EUR3.074m** / AGB AFM **+EUR0.122m**
  - MJP debt YE2026 **EUR5.358m** / YE2027 **EUR9.068m RAMP FOI** (new **EUR2.141m** / **EUR4.641m**)
- Dual: Langemark FVA/herwaard MASSIVE / budget NEG (tick1113) - not TE-additive
- Note: Oosterzele / Nijlen login-blocked / Vorselaar docs-only / Kalmthout / Bornem JR2024-only / De Panne OCR residual next; progress@1120 in 6
- Wrote: budgets +44 (bud_eve_*); commitments +8; leaderboard +12; sources +1; entity city_evergem; FOI **gap_eve_ocmw_toelagen_pension_invest_l5** prio9 ready + draft; PDF primary (not committed 17.6MB); rq_1114=done; spawn **rq_1115**; ticks=1114
- FOI: ready only - **do not send**
- Next: prio5 **rq_1115** residual dual L5; deferred **rq_116**; progress@1120 in 6
"""
    log_text = LOG.read_text(encoding="utf-8")
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding="utf-8")

    print("tick1114 write OK")
    print("budgets", len(bud), "commitments", len(comm), "lbs", len(lbs))
    print("gap", GAP)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""tick 1112 — Gemeente+OCMW Knokke-Heist JR2025 dual residual"""
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

TICK = 1112
UTC = "2026-08-11T21:30:00Z"
SRC = "src_knokke_heist_jr2025"
ENT = "city_knokke_heist"
GAP = "gap_kh_loans_toelagen_ocmw_agso_invest_l5"
URL = "https://www.knokke-heist.be/gemeente-en-bestuur/beleidsrapporten/gemeente-en-ocmw/jaarrekening-gemeente-en-ocmw"
# primary: Vaststelling Jaarrekening2025 DEF GR (555p; GR 25.06.2026)

F = dict(
    assets=393798159,
    equity=351420643,
    debt_total=42377516,
    fin_debt=17014158,
    fin_debt_lt=14346860,
    fin_debt_st=2667298,
    fin_debt_was=12247290,
    new_loans=8371273,
    new_loans_bank=7000000,
    new_loans_lease=1371273,
    repayments=3604405,
    cash=30552512,
    cash_was=26750376,
    pension_lt=10983212,
    pension_was=12411393,
    fva_igs=32386006,
    fva_eva=24190760,
    herwaard=11628649,
    leasing_mva=8124051,
    expl_ont=137767511,
    expl_uit=109795268,
    expl_saldo=27972243,
    afm=24957837,
    afm_gecorr=27582459,
    bbr=31698701,
    budget_result=2873054,
    cum_br=31889362,
    onbeschikbaar=190661,
    pnl=13733044,
    fiscal=89164766,
    op=62534722,
    personnel=43865365,
    toelagen=35694984,
    police=16009071,
    fire=3897701,
    agb_toel=5853392,
    welzijn=742640,
    igs_toel=39973,
    eredienst=500821,
    andere_toel=8651386,
    hulp_ocmw=2283792,
    invest_uit=33199034,
    invest_ont=770622,
    invest_saldo=-32428413,
    invest_mjp=55110326,
    invest_subs=6879341,
    invest_subs_agb=5768720,
    ocmw_cover=4415950,
    ocmw_cover_was=3810438,
    ocmw_pnl=-2985617,
    ocmw_equity_cum=-5747230,
    agso_bbr=-1086540,
    mjp_debt_2026=39163476,
    mjp_new_2026=25868900,
    goederen=25979854,
    fin_exp=491907,
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

    b("bud_kh_assets_2025", F["assets"], "Assets YE2025 393.798m JUMP (was 372.882m); tick1112")
    b("bud_kh_equity_2025", F["equity"], "Nettoactief YE2025 351.421m JUMP; tick1112")
    b("bud_kh_debt_total_2025", F["debt_total"], "Total schulden YE2025 42.378m JUMP; tick1112")
    b("bud_kh_fin_debt_2025", F["fin_debt"], "Fin debt YE2025 17.014m JUMP FOI (was 12.247m); tick1112")
    b("bud_kh_fin_debt_lt_2025", F["fin_debt_lt"], "Fin debt LT YE2025 14.347m (Belfius/KBC/Fluvius lease); tick1112")
    b("bud_kh_fin_debt_st_2025", F["fin_debt_st"], "Fin debt ST due YE2025 2.667m; tick1112")
    b("bud_kh_new_loans_2025", F["new_loans"], "New loans 8.371m MASSIVE FOI (KBC 7.000 + Fluvius lease 1.371); tick1112")
    b("bud_kh_repayments_2025", F["repayments"], "Periodieke aflossingen 3.604m; tick1112")
    b("bud_kh_cash_2025", F["cash"], "Cash YE2025 30.553m JUMP (was 26.750m); tick1112")
    b("bud_kh_pension_lt_2025", F["pension_lt"], "Pension LT 10.983m DECLINE FOI (was 12.411m); tick1112")
    b("bud_kh_fva_igs_2025", F["fva_igs"], "FVA IGS YE2025 32.386m HIGH FOI; tick1112")
    b("bud_kh_fva_eva_2025", F["fva_eva"], "FVA EVA/AGSO-class 24.191m FOI; tick1112")
    b("bud_kh_herwaard_2025", F["herwaard"], "Herwaarderingsreserves 11.629m; tick1112")
    b("bud_kh_leasing_mva_2025", F["leasing_mva"], "Leasing MVA YE2025 8.124m; tick1112")
    b("bud_kh_expl_ontvangsten_2025", F["expl_ont"], "Exploitatie ontvangsten 137.768m; tick1112")
    b("bud_kh_expl_uitgaven_2025", F["expl_uit"], "Exploitatie uitgaven 109.795m; tick1112")
    b("bud_kh_expl_saldo_2025", F["expl_saldo"], "Exploitatiesaldo +27.972m VERY STRONG; tick1112")
    b("bud_kh_afm_2025", F["afm"], "AFM +24.958m VERY STRONG; tick1112")
    b("bud_kh_afm_gecorr_2025", F["afm_gecorr"], "AFM gecorrigeerd +27.582m VERY STRONG; tick1112")
    b("bud_kh_bbr_2025", F["bbr"], "BBR 31.699m VERY HIGH; tick1112")
    b("bud_kh_budget_result_2025", F["budget_result"], "Budget +2.873m POS; tick1112")
    b("bud_kh_pnl_2025", F["pnl"], "P&L +13.733m POS; tick1112")
    b("bud_kh_fiscal_2025", F["fiscal"], "Fiscale opbrengsten 89.165m coastal; tick1112")
    b("bud_kh_op_2025", F["op"], "Onroerende voorheffing opcentiemen 62.535m; tick1112")
    b("bud_kh_personnel_2025", F["personnel"], "Personeel 43.865m; tick1112")
    b("bud_kh_toelagen_2025", F["toelagen"], "Toegestane werkingssubsidies 35.695m MASSIVE FOI; tick1112")
    b("bud_kh_police_2025", F["police"], "Politiezone toelage 16.009m FOI; tick1112")
    b("bud_kh_fire_2025", F["fire"], "HVZ toelage 3.898m; tick1112")
    b("bud_kh_agb_toelagen_2025", F["agb_toel"], "AGB toelagen 5.853m FOI; tick1112")
    b("bud_kh_andere_toelagen_2025", F["andere_toel"], "Andere toelagen 8.651m HIGH FOI; tick1112")
    b("bud_kh_welzijn_toelagen_2025", F["welzijn"], "Welzijnsverenigingen toelage 0.743m FOI; tick1112")
    b("bud_kh_hulp_ocmw_2025", F["hulp_ocmw"], "OCMW individuele hulp 2.284m; tick1112")
    b("bud_kh_invest_uitgaven_2025", F["invest_uit"], "Invest 33.199m vs MJP 55.110m MASSIVE UNDERSPEND FOI; tick1112")
    b("bud_kh_invest_mjp_2025", F["invest_mjp"], "MJP invest uitgaven 55.110m; tick1112")
    b("bud_kh_invest_subs_2025", F["invest_subs"], "Toegestane invest-subs 6.879m JUMP FOI (AGB 5.769m); tick1112")
    b("bud_kh_ocmw_cover_2025", F["ocmw_cover"], "OCMW cover 4.416m FULL JUMP FOI (was 3.810m); tick1112")
    b("bud_kh_ocmw_pnl_2025", F["ocmw_pnl"], "OCMW P&L -2.986m FOI; tick1112")
    b("bud_kh_ocmw_equity_cum_2025", F["ocmw_equity_cum"], "OCMW cum equity -5.747m DEEP FOI; tick1112")
    b("bud_kh_agso_bbr_2025", F["agso_bbr"], "AGSO BBR consol -1.087m NEG FOI; tick1112")
    b("bud_kh_mjp_debt_2026", F["mjp_debt_2026"], "MJP fin debt YE2026 39.163m MASSIVE RAMP FOI; tick1112")
    b("bud_kh_mjp_new_2026", F["mjp_new_2026"], "MJP new loans 2026 25.869m MASSIVE FOI; tick1112")
    b("bud_kh_goederen_2025", F["goederen"], "Goederen en diensten 25.980m; tick1112")
    b("bud_kh_fin_exp_2025", F["fin_exp"], "Financiele kosten 0.492m; tick1112")
    append_csv(DATA / "budgets.csv", bud)

    comm = [
        f"comm_kh_fin_debt_2025,Knokke-Heist fin debt stock YE2025 17.014m JUMP,{ENT},creditors,BBC JR2025,,2025,2045,{F['fin_debt']},{{2025:{F['fin_debt']}}},{F['fin_debt']},active,,Capital finance JUMP FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>debt,tick1112; was 12.247m; KBC 7m + Fluvius lease",
        f"comm_kh_new_loans_2025,Knokke-Heist new loans 8.371m MASSIVE 2025,{ENT},creditors,BBC JR2025 T4,,2025,2025,{F['new_loans']},{{2025:{F['new_loans']}}},0,active,,KBC 7.000m + Fluvius lease 1.371m FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>loans,tick1112",
        f"comm_kh_mjp_debt_ramp_2026,Knokke-Heist MJP fin debt ramp YE2026 39.163m,{ENT},creditors,BBC JR2025 T4 MJP,,2026,2026,{F['mjp_debt_2026']},{{2026:{F['mjp_debt_2026']}}},{F['mjp_debt_2026']},planned,,MASSIVE debt ramp FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>debt_mjp,tick1112; new 25.869m 2026",
        f"comm_kh_toelagen_2025,Knokke-Heist toelagen werking 35.695m 2025,{ENT},PZ/HVZ/AGB/other,BBC JR2025 T2,,2025,2025,{F['toelagen']},{{2025:{F['toelagen']}}},0,active,,Named matrix FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>toelagen,tick1112; police 16.009 AGB 5.853 andere 8.651",
        f"comm_kh_ocmw_cover_2025,Knokke-Heist OCMW cover FULL 4.416m JUMP 2025,{ENT},OCMW Knokke-Heist,BBC JR2025,,2025,2025,{F['ocmw_cover']},{{2025:{F['ocmw_cover']}}},0,active,,Cover FULL JUMP FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>ocmw,tick1112; was 3.810m; equity -5.747m",
        f"comm_kh_invest_underspend_2025,Knokke-Heist invest 33.20 vs MJP 55.11 MASSIVE UNDERSPEND 2025,{ENT},Capital program,BBC JR2025,,2025,2025,{F['invest_uit']},{{2025:{F['invest_uit']}}},0,active,,UNDERSPEND FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>invest,tick1112",
        f"comm_kh_agso_bbr_neg_2025,Knokke-Heist AGSO BBR consol -1.087m NEG 2025,{ENT},AGSO Knokke-Heist,BBC JR2025 J2 consol,,2025,2025,{F['agso_bbr']},{{2025:{F['agso_bbr']}}},0,active,,AGSO NEG BBR FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>AGSO,tick1112",
        f"comm_kh_invest_subs_agb_2025,Knokke-Heist invest-subs AGB 5.769m JUMP 2025,{ENT},AGB,BBC JR2025 T2,,2025,2025,{F['invest_subs_agb']},{{2025:{F['invest_subs_agb']}}},0,active,,AGB invest-subs FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>KnokkeHeist>AGB,tick1112",
    ]
    append_csv(DATA / "commitments.csv", comm)

    under = F["invest_mjp"] - F["invest_uit"]
    debt_jump = F["fin_debt"] - F["fin_debt_was"]
    ramp = F["mjp_debt_2026"] - F["fin_debt"]
    pen_drop = F["pension_was"] - F["pension_lt"]
    lb_note = "tick1112; primary Knokke-Heist JR2025; dual residual after De Haan; not TE-additive"

    def lb(iid, name, annual, abs_s, cost_s, diff_s, pri, cut):
        return (
            f"{iid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>KnokkeHeist_L5,"
            f"{annual},{annual},JR2025 dual residual map VL,strong,{SRC},"
            f"Knokke-Heist residents,Local dual residual map VL JR2025,"
            f"JR2025 BBC Knokke-Heist GEOC realized figures,"
            f"{abs_s},{cost_s},{diff_s},{pri},{cut},active,,{lb_note}"
        )

    lbs = [
        lb("lb_kh_toelagen_35_69m_2025", "Knokke-Heist toelagen 35.69m MASSIVE FOI residual",
           F["toelagen"], 8.0, 7.5, 3.5, 7.3, "Named matrix FOI"),
        lb("lb_kh_mjp_debt_ramp_39_16m_2026", "Knokke-Heist MJP fin debt ramp YE2026 39.16m MASSIVE FOI residual",
           ramp, 9.0, 7.5, 3.5, 7.65, "Debt ramp FOI project/lender"),
        lb("lb_kh_new_loans_8_37m_2025", "Knokke-Heist new loans 8.37m MASSIVE FOI residual",
           F["new_loans"], 8.5, 5.5, 3.5, 6.95, "KBC+Fluvius FOI"),
        lb("lb_kh_invest_underspend_2025", "Knokke-Heist invest 33.2 vs MJP 55.1 MASSIVE UNDERSPEND FOI residual",
           under, 8.5, 7.0, 3.5, 7.3, "Invest path FOI"),
        lb("lb_kh_police_16_01m_2025", "Knokke-Heist police toelage 16.01m FOI residual",
           F["police"], 6.5, 5.5, 3.5, 5.95, "PZ path FOI"),
        lb("lb_kh_ocmw_cover_4_42m_2025", "Knokke-Heist OCMW cover FULL 4.42m JUMP FOI residual",
           F["ocmw_cover"], 8.5, 5.0, 3.5, 6.75, "Cover policy FOI"),
        lb("lb_kh_afm_24_96m_2025", "Knokke-Heist AFM +24.96m VERY STRONG FOI residual",
           F["afm"], 5.0, 7.5, 3.0, 6.55, "Keep AFM path"),
        lb("lb_kh_cash_30_55m_2025", "Knokke-Heist cash 30.55m JUMP FOI residual",
           F["cash"], 5.5, 7.5, 3.5, 6.35, "Treasury FOI"),
        lb("lb_kh_agso_bbr_neg_1_09m_2025", "Knokke-Heist AGSO BBR -1.09m NEG FOI residual",
           abs(F["agso_bbr"]), 8.5, 4.0, 3.5, 6.55, "AGSO path FOI"),
        lb("lb_kh_fin_debt_17_01m_2025", "Knokke-Heist fin debt 17.01m JUMP FOI residual",
           F["fin_debt"], 6.5, 5.5, 3.5, 5.95, "Debt stock FOI"),
        lb("lb_kh_andere_toelagen_8_65m_2025", "Knokke-Heist andere toelagen 8.65m FOI residual",
           F["andere_toel"], 8.0, 5.5, 3.5, 6.8, "Named >=50k FOI"),
        lb("lb_kh_invest_subs_agb_5_77m_2025", "Knokke-Heist invest-subs AGB 5.77m JUMP FOI residual",
           F["invest_subs_agb"], 8.0, 5.5, 3.5, 6.8, "AGB capital FOI"),
    ]
    append_csv(DATA / "leaderboard.csv", lbs)

    src_row = (
        f"{SRC},Gemeente+OCMW Knokke-Heist BBC Jaarrekening 2025,{URL},"
        f"Gemeente Knokke-Heist,2026-08-11,primary_pdf,"
        f"tick1112; 555p text; KBO GE 0207.691.252 / OCMW 0212.334.582; NIS 31043; "
        f"AD Miet Gobert FD Stein Moyersons; GR 25.06.2026; "
        f"assets 393.798m cash 30.553m fin debt 17.014m JUMP new loans 8.371m (KBC 7m) "
        f"AFM +24.958m BBR 31.699m toelagen 35.695m police 16.009m OCMW cover 4.416m FULL "
        f"invest 33.2 vs MJP 55.1 UNDERSPEND AGSO BBR -1.087m MJP debt YE2026 39.163m; "
        f"primary PDF staged docs/doge/data/_tmp/knokke_Vaststelling__Jaarrekening2025_-DEF_GR_0.pdf"
    )
    append_csv(DATA / "sources.csv", [src_row])

    ent_row = (
        f"{ENT},Gemeente Knokke-Heist,Commune de Knokke-Heist,Municipality of Knokke-Heist,"
        f"municipality,vlaanderen_gov,nl,https://www.knokke-heist.be,info@knokke-heist.be,"
        f"Alfred Verweeplein 1 8300 Knokke-Heist,"
        f"JR2025 dual residual tick1112; KBO 0207.691.252 / OCMW 0212.334.582; "
        f"assets 393.798m cash 30.553m fin debt 17.014m JUMP new loans 8.371m AFM +24.958m "
        f"BBR 31.699m toelagen 35.695m police 16.009m OCMW cover 4.416m FULL AGSO BBR NEG; "
        f"AD Miet Gobert FD Stein Moyersons"
    )
    append_csv(DATA / "entities.csv", [ent_row])

    foi_row = (
        f"{GAP},Vlaanderen>Gemeenten>KnokkeHeist>loans_toelagen_ocmw_agso_invest_L5,{ENT},"
        f"\"New loans 8.371m (KBC 7.000 + Fluvius lease 1.371) purpose/rate/schedule; MJP fin debt "
        f"ramp YE2026 39.163m (new 25.869m) project map; toelagen matrix within 35.695m (police "
        f"16.009 / AGB 5.853 / andere 8.651 / fire 3.898 / welzijn 0.743) named >=50k; OCMW cover "
        f"FULL 4.416m JUMP vs P&L -2.986m and equity -5.747m path; AGSO BBR consol -1.087m full JR; "
        f"invest underspend 33.2 vs MJP 55.1; invest-subs AGB 5.769m JUMP terms; pension DROP "
        f"12.411to10.983m actuarial; FVA IGS 32.386 + EVA 24.191 composition\","
        f"\"Largest coastal dual residual this decade: VERY STRONG AFM +25m and BBR 32m under "
        f"MASSIVE toelagen 36m + debt JUMP/ramp + OCMW/AGSO dual opacity\","
        f"9,Gemeente Knokke-Heist,info@knokke-heist.be,Alfred Verweeplein 1 8300 Knokke-Heist,"
        f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-11,,,,,"
        f"comm_kh_new_loans_2025,lb_kh_toelagen_35_69m_2025,"
        f"{UTC},{UTC},tick1112; ready not sent; do not send without human OK"
    )
    append_csv(DATA / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = f"""# FOI draft — {GAP}

**Status:** ready (NOT sent)  
**Gap ID:** {GAP}  
**Tick:** {TICK}  

## Recipient

- Gemeente Knokke-Heist openbaarheid / financieel directeur Stein Moyersons  
- E-mail: info@knokke-heist.be  
- Adres: Alfred Verweeplein 1, 8300 Knokke-Heist  

## Subject

Openbaarheid — Jaarrekening 2025 Gemeente/OCMW Knokke-Heist: leningen, toelagen, OCMW, AGSO, investeringen

## Body (NL)

```text
[Naam]
[Adres]
[E-mail]
[Datum]

Aan: Gemeente Knokke-Heist
t.a.v. de financieel directeur

Betreft: Verzoek openbaarheid — jaarrekening 2025 Gemeente en OCMW Knokke-Heist

Geachte,

Op grond van de regels inzake openbaarheid van bestuur vraag ik de volgende
documenten en toelichtingen.

### 1. Reeds openbaar (BBC JR2025; GR 25.06.2026)

- Activa **EUR393,798m JUMP**; nettoactief **EUR351,421m**; fin. schuld
  **EUR17,014m JUMP** (was 12,247m; LT 14,347 / ST 2,667); nieuwe leningen
  **EUR8,371m** (KBC **EUR7,000m** + Fluvius lease **EUR1,371m**); cash
  **EUR30,553m JUMP**; pensioen LT **EUR10,983m DROP** (was 12,411m); FVA IGS
  **EUR32,386m** + EVA **EUR24,191m**; AFM **+EUR24,958m**; BBR
  **EUR31,699m**; budget **+EUR2,873m**; P&L **+EUR13,733m**; toelagen
  **EUR35,695m** (politie **EUR16,009m** / AGB **EUR5,853m** / andere
  **EUR8,651m** / HVZ **EUR3,898m** / welzijn **EUR0,743m**); invest
  **EUR33,199m** vs MJP **EUR55,110m MASSIVE UNDERSPEND**; invest-subs
  **EUR6,879m** (AGB **EUR5,769m**); OCMW-tussenkomst **EUR4,416m FULL JUMP**
  (OCMW P&L **−EUR2,986m**; cum equity **−EUR5,747m**); AGSO BBR consol
  **−EUR1,087m NEG**; MJP fin. schuld YE2026 **EUR39,163m** (nieuwe leningen
  **EUR25,869m**).

### 2. Gevraagde stukken / toelichtingen

1. **Nieuwe leningen EUR8,371m** (KBC 7m + Fluvius lease 1,371m): doel, rente,
   aflossingsplan; aansluiting fin. schuld 17,014m.
2. **MJP schuld-ramp YE2026 EUR39,163m** (nieuwe leningen EUR25,869m):
   projectenlijst en kredietgevers.
3. **Toelagen-matrix** binnen EUR35,695m: nominatieve lijst ≥ EUR50k (politie,
   AGB, andere EUR8,651m, HVZ, welzijnsverenigingen).
4. **OCMW cover FULL EUR4,416m JUMP** vs P&L −EUR2,986m en equity −EUR5,747m:
   multi-year liquiditeitspad 2020–2026.
5. **AGSO BBR −EUR1,087m NEG**: volledige AGSO-jaarrekening 2025 en consol-
   impact.
6. **Invest underspend** 33,2 vs MJP 55,1m + invest-subs AGB EUR5,769m JUMP:
   projectenlijst en overdrachten 2026.
7. **Pensioen DROP** 12,411 → 10,983m: actuariële aannames / vrijval.

Gelieve te antwoorden binnen de wettelijke termijn. Digitaal leveren (PDF) heeft
de voorkeur.

Met vriendelijke groeten,

[Naam]
[Contact]
```

## Notes

- Primary source: BBC JR2025 Gemeente+OCMW Knokke-Heist (555p; GR 25.06.2026; AD Gobert FD Moyersons).  
- **Do not send** without human OK.  
- Tick 1112 dual residual after De Haan (tick1111).
"""
    (FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

    rq_path = DATA / "research_queue.csv"
    lines = rq_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("rq_1112,"):
            out.append(
                "rq_1112,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
                "Knokke-Heist GE+OCMW JR2025 dual residual,"
                f"{GAP},2026-08-11T21:00:00Z,{UTC},"
                "tick1112 Knokke-Heist assets 393.798m cash 30.553m fin debt 17.014m JUMP new loans 8.371m "
                "AFM +24.958m toelagen 35.695m police 16.009m OCMW cover 4.416m FULL AGSO BBR NEG "
                "MJP debt YE2026 39.163m; FOI ready"
            )
        else:
            out.append(line)
    out.append(
        "rq_1113,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
        "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen login-blocked / Vorselaar docs-only / "
        "Kalmthout / Bornem JR2024-only / Langemark bundel staged / De Panne OCR / Schelle GE+OCMW if published / other); "
        "prefer FOI-adjacent L5; skip rq_116,"
        f",2026-08-11T21:30:00Z,{UTC},"
        "spawned tick1112 after Knokke-Heist dual residual; next residual dual L5; progress@1120 in 8"
    )
    rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    state = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{UTC},rq_1112,1112,no,"
        "tick1112 Knokke-Heist GE+OCMW JR2025 dual residual; FOI gap_kh_loans_toelagen_ocmw_agso_invest_l5 prio9 ready; "
        "assets 393.798m cash 30.553m JUMP equity 351.421m fin debt 17.014m JUMP new loans 8.371m (KBC 7m) "
        "pension 10.983m DROP FVA IGS 32.386m AFM +24.958m BBR 31.699m VERY HIGH budget +2.873m P&L +13.733m "
        "toelagen 35.695m police 16.009m OCMW cover 4.416m FULL AGSO BBR -1.087m NEG invest 33.2 vs MJP 55.1 "
        "UNDERSPEND MJP debt YE2026 39.163m; next residual dual L5 rq_1113; progress@1120 in 8; rq_116 deferred\n"
    )
    (DATA / "loop_state.csv").write_text(state, encoding="utf-8")

    log_entry = f"""
### Tick 1112 - {UTC}

- Unit: **rq_1112** (FOI-adjacent residual dual - **Gemeente+OCMW Knokke-Heist Jaarrekening 2025** + De Haan dual residual)
- Found (strong primary BBC JR2025 555p text; knokke-heist.be; GR 25.06.2026; KBO GE 0207.691.252 / OCMW 0212.334.582; NIS 31043; AD Miet Gobert FD Stein Moyersons; GE+OCMW + AGSO consol):
  - Assets **EUR393.798m JUMP** (was **EUR372.882m**) / equity **EUR351.421m JUMP** / debt total **EUR42.378m JUMP** / fin debt **EUR17.014m JUMP FOI** (LT **EUR14.347m** Belfius/KBC/Fluvius / ST due **EUR2.667m**; was **EUR12.247m**)
  - New loans **EUR8.371m MASSIVE FOI** (KBC **EUR7.000m** + Fluvius lease **EUR1.371m**) / repayments **EUR3.604m**
  - Cash **EUR30.553m JUMP** (was **EUR26.750m**) / pension **EUR10.983m DECLINE FOI** (was **EUR12.411m**)
  - FVA IGS **EUR32.386m** / FVA EVA **EUR24.191m** / herwaard **EUR11.629m** / leasing MVA **EUR8.124m**
  - Exploitatie: ontvangsten **EUR137.768m** / uitgaven **EUR109.795m** / saldo **+EUR27.972m VERY STRONG**
  - AFM **+EUR24.958m VERY STRONG** (gecorr **+EUR27.582m**) / BBR **EUR31.699m VERY HIGH** / onbeschikbaar **EUR0.191m** / budget **+EUR2.873m POS** / P&L **+EUR13.733m POS**
  - Fiscal **EUR89.165m** coastal / OP **EUR62.535m** / personnel **EUR43.865m**
  - Toelagen **EUR35.695m MASSIVE FOI** (police **EUR16.009m** / AGB **EUR5.853m** / andere **EUR8.651m HIGH** / fire **EUR3.898m** / welzijn **EUR0.743m** / eredienst **EUR0.501m**)
  - Invest **EUR33.199m** vs MJP **EUR55.110m MASSIVE UNDERSPEND FOI** / invest-subs **EUR6.879m JUMP** (AGB **EUR5.769m**)
  - OCMW cover **EUR4.416m FULL JUMP FOI** (was **EUR3.810m**) / OCMW P&L **−EUR2.986m** / OCMW cum equity **−EUR5.747m DEEP** / OCMW hulp **EUR2.284m**
  - **AGSO BBR consol −EUR1.087m NEG FOI** (AGSO AFM +1.825m)
  - **MJP T4 debt ramp MASSIVE FOI:** YE2026 fin debt **EUR39.163m** (new **EUR25.869m**)
- Dual: De Haan cash VERY HIGH / OCMW FULL (tick1111) - not TE-additive
- Note: Oosterzele / Nijlen login-blocked / Vorselaar docs-only / Kalmthout / Bornem JR2024-only / Langemark bundel staged / De Panne OCR residual next; progress@1120 in 8
- Wrote: budgets +43 (bud_kh_*); commitments +8; leaderboard +12; sources +1; entity city_knokke_heist; FOI **gap_kh_loans_toelagen_ocmw_agso_invest_l5** prio9 ready + draft; PDF primary (not committed 9.3MB); rq_1112=done; spawn **rq_1113**; ticks=1112
- FOI: ready only - **do not send**
- Next: prio5 **rq_1113** residual dual L5; deferred **rq_116**; progress@1120 in 8
"""
    log_text = LOG.read_text(encoding="utf-8")
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding="utf-8")

    print("tick1112 write OK")
    print("budgets", len(bud), "commitments", len(comm), "lbs", len(lbs))
    print("gap", GAP)


if __name__ == "__main__":
    main()

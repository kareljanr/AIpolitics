# -*- coding: utf-8 -*-
"""tick 1111 — Gemeente+OCMW De Haan JR2025 dual residual"""
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

TICK = 1111
UTC = "2026-08-11T21:00:00Z"
SRC = "src_dehaan_jr2025"
ENT = "city_dehaan"
GAP = "gap_dha_toelagen_pension_ocmw_invest_l5"
URL = "https://www.dehaan.be"
# local primary extract from official JR2025 bundel (staged docs/doge/raw/dehaan_jr2025.pdf)

F = dict(
    assets=150723610,
    equity=116904013,
    debt_total=33819596,
    fin_debt=12527697,
    fin_debt_lt=11006758,
    fin_debt_st=1520939,
    new_loans=1228118,
    repayments=1584416,
    cash=34540861,
    pension_lt=14673056,
    pension_was=13751168,
    fva_igs=29999118,
    herwaard=6735942,
    leasing_mva=9152078,
    expl_ont=40162482,
    expl_uit=33417849,
    expl_saldo=6744634,
    afm=5396434,
    afm_gecorr=5948691,
    bbr=32730464,
    budget_result=1629117,
    cum_br=32730464,
    pnl=1937058,
    fiscal=27014831,
    pb=3991933,
    op=12405996,
    personnel=16408368,
    toelagen=7817954,
    police=6038500,
    fire=1024651,
    igs_toel=399276,
    eredienst=51533,
    andere_toel=303994,
    hulp_ocmw=1797046,
    invest_uit=5958379,
    invest_ont=1200763,
    invest_saldo=-4757617,
    invest_mjp=7819873,
    invest_subs=706432,
    ocmw_cover=1713222,
    ocmw_pnl=-1576793,
    ocmw_equity_cum=-3311764,
    loans_granted_igs=237817,
    goederen=6586181,
    fin_exp=323128,
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

    b("bud_dha_assets_2025", F["assets"], "Assets YE2025 150.724m (was 147.496m); tick1111")
    b("bud_dha_equity_2025", F["equity"], "Nettoactief YE2025 116.904m; tick1111")
    b("bud_dha_debt_total_2025", F["debt_total"], "Total schulden YE2025 33.820m; tick1111")
    b("bud_dha_fin_debt_2025", F["fin_debt"], "Fin debt YE2025 12.528m DECLINE (was 12.902m); tick1111")
    b("bud_dha_fin_debt_lt_2025", F["fin_debt_lt"], "Fin debt LT YE2025 11.007m; tick1111")
    b("bud_dha_fin_debt_st_2025", F["fin_debt_st"], "Fin debt ST due YE2025 1.521m; tick1111")
    b("bud_dha_new_loans_2025", F["new_loans"], "New loans/leasing 1.228m FOI; tick1111")
    b("bud_dha_repayments_2025", F["repayments"], "Periodieke aflossingen 1.584m; tick1111")
    b("bud_dha_cash_2025", F["cash"], "Cash YE2025 34.541m VERY HIGH; tick1111")
    b("bud_dha_pension_lt_2025", F["pension_lt"], "Pension LT 14.673m JUMP FOI (was 13.751m); tick1111")
    b("bud_dha_fva_igs_2025", F["fva_igs"], "FVA IGS YE2025 29.999m HIGH FOI; tick1111")
    b("bud_dha_herwaard_2025", F["herwaard"], "Herwaarderingsreserves 6.736m; tick1111")
    b("bud_dha_leasing_mva_2025", F["leasing_mva"], "Leasing MVA YE2025 9.152m; tick1111")
    b("bud_dha_expl_ontvangsten_2025", F["expl_ont"], "Exploitatie ontvangsten 40.162m; tick1111")
    b("bud_dha_expl_uitgaven_2025", F["expl_uit"], "Exploitatie uitgaven 33.418m; tick1111")
    b("bud_dha_expl_saldo_2025", F["expl_saldo"], "Exploitatiesaldo +6.745m VERY STRONG; tick1111")
    b("bud_dha_afm_2025", F["afm"], "AFM +5.396m VERY STRONG; tick1111")
    b("bud_dha_afm_gecorr_2025", F["afm_gecorr"], "AFM gecorrigeerd +5.949m VERY STRONG; tick1111")
    b("bud_dha_bbr_2025", F["bbr"], "BBR 32.730m VERY HIGH; tick1111")
    b("bud_dha_budget_result_2025", F["budget_result"], "Budget +1.629m POS (MJP was -1.718m); tick1111")
    b("bud_dha_pnl_2025", F["pnl"], "P&L +1.937m FLIP FOI (was -2.175m); tick1111")
    b("bud_dha_fiscal_2025", F["fiscal"], "Fiscale opbrengsten 27.015m; tick1111")
    b("bud_dha_pb_2025", F["pb"], "Personenbelasting 3.992m; tick1111")
    b("bud_dha_op_2025", F["op"], "Onroerende voorheffing opcentiemen 12.406m; tick1111")
    b("bud_dha_personnel_2025", F["personnel"], "Personeel 16.408m; tick1111")
    b("bud_dha_toelagen_2025", F["toelagen"], "Toegestane werkingssubsidies 7.818m FOI; tick1111")
    b("bud_dha_police_2025", F["police"], "Politiezone toelage 6.039m FOI; tick1111")
    b("bud_dha_fire_2025", F["fire"], "HVZ toelage 1.025m; tick1111")
    b("bud_dha_igs_toelagen_2025", F["igs_toel"], "IGS toelagen 0.399m FOI; tick1111")
    b("bud_dha_andere_toelagen_2025", F["andere_toel"], "Andere toelagen 0.304m FOI; tick1111")
    b("bud_dha_hulp_ocmw_2025", F["hulp_ocmw"], "OCMW individuele hulp 1.797m; tick1111")
    b("bud_dha_invest_uitgaven_2025", F["invest_uit"], "Invest uitgaven 5.958m vs MJP 7.820m UNDERSPEND FOI; tick1111")
    b("bud_dha_invest_mjp_2025", F["invest_mjp"], "MJP invest uitgaven 7.820m; tick1111")
    b("bud_dha_invest_subs_2025", F["invest_subs"], "Toegestane invest-subs 0.706m JUMP FOI (was 0.348m); tick1111")
    b("bud_dha_ocmw_cover_2025", F["ocmw_cover"], "OCMW cover 1.713m FULL FOI (OCMW P&L -1.577m); tick1111")
    b("bud_dha_ocmw_pnl_2025", F["ocmw_pnl"], "OCMW P&L -1.577m FOI; tick1111")
    b("bud_dha_ocmw_equity_cum_2025", F["ocmw_equity_cum"], "OCMW cum equity -3.312m DEEP FOI; tick1111")
    b("bud_dha_loans_granted_igs_2025", F["loans_granted_igs"], "Toegestane leningen IGS 0.238m FOI; tick1111")
    b("bud_dha_goederen_2025", F["goederen"], "Goederen en diensten 6.586m; tick1111")
    b("bud_dha_fin_exp_2025", F["fin_exp"], "Financiele kosten 0.323m; tick1111")
    append_csv(DATA / "budgets.csv", bud)

    comm = [
        f"comm_dha_fin_debt_2025,De Haan fin debt stock YE2025 12.528m,{ENT},creditors,BBC JR2025,,2025,2045,{F['fin_debt']},{{2025:{F['fin_debt']}}},{F['fin_debt']},active,,Capital finance stock DECLINE,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>debt,tick1111; LT 11.007 ST 1.521 new 1.228",
        f"comm_dha_cash_2025,De Haan cash 34.541m VERY HIGH 2025,{ENT},treasury,BBC JR2025,,2025,2025,{F['cash']},{{2025:{F['cash']}}},0,active,,Cash VERY HIGH FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>cash,tick1111",
        f"comm_dha_pension_2025,De Haan pension LT 14.673m JUMP 2025,{ENT},pension provision,BBC JR2025,,2025,2025,{F['pension_lt']},{{2025:{F['pension_lt']}}},0,active,,Pension JUMP FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>pension,tick1111; was 13.751m",
        f"comm_dha_fva_igs_2025,De Haan FVA IGS 29.999m 2025,{ENT},IGS/Fluvius-class,BBC JR2025,,2025,2025,{F['fva_igs']},{{2025:{F['fva_igs']}}},0,active,,FVA IGS HIGH FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>fva,tick1111",
        f"comm_dha_ocmw_cover_2025,De Haan OCMW cover FULL 1.713m 2025,{ENT},OCMW De Haan,BBC JR2025,,2025,2025,{F['ocmw_cover']},{{2025:{F['ocmw_cover']}}},0,active,,Cover FULL FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>ocmw,tick1111; OCMW equity -3.312m",
        f"comm_dha_toelagen_2025,De Haan toelagen werking 7.818m 2025,{ENT},PZ/HVZ/IGS/other,BBC JR2025,,2025,2025,{F['toelagen']},{{2025:{F['toelagen']}}},0,active,,Named matrix FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>toelagen,tick1111; police 6.039 fire 1.025",
        f"comm_dha_invest_underspend_2025,De Haan invest 5.96 vs MJP 7.82 UNDERSPEND 2025,{ENT},Capital program,BBC JR2025,,2025,2025,{F['invest_uit']},{{2025:{F['invest_uit']}}},0,active,,UNDERSPEND FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>invest,tick1111",
        f"comm_dha_police_2025,De Haan police toelage 6.039m 2025,{ENT},politiezone,BBC JR2025 T2,,2025,2025,{F['police']},{{2025:{F['police']}}},0,active,,Police toelage FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>DeHaan>police,tick1111",
    ]
    append_csv(DATA / "commitments.csv", comm)

    under = F["invest_mjp"] - F["invest_uit"]
    pen_jump = F["pension_lt"] - F["pension_was"]
    lb_note = "tick1111; primary De Haan JR2025; dual residual after Schelle AGB; not TE-additive"

    def lb(iid, name, annual, abs_s, cost_s, diff_s, pri, cut):
        return (
            f"{iid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>DeHaan_L5,"
            f"{annual},{annual},JR2025 dual residual map VL,strong,{SRC},"
            f"De Haan residents,Local dual residual map VL JR2025,"
            f"JR2025 BBC De Haan GEOC realized figures,"
            f"{abs_s},{cost_s},{diff_s},{pri},{cut},active,,{lb_note}"
        )

    lbs = [
        lb("lb_dha_cash_34_54m_2025", "De Haan cash 34.54m VERY HIGH FOI residual",
           F["cash"], 6.5, 7.5, 3.5, 6.7, "Treasury policy FOI"),
        lb("lb_dha_fva_igs_30_00m_2025", "De Haan FVA IGS 30.00m HIGH FOI residual",
           F["fva_igs"], 7.5, 7.5, 3.5, 7.05, "FVA IGS matrix FOI"),
        lb("lb_dha_bbr_32_73m_2025", "De Haan BBR 32.73m VERY HIGH FOI residual",
           F["bbr"], 5.5, 7.5, 3.5, 6.35, "Keep BBR path"),
        lb("lb_dha_toelagen_7_82m_2025", "De Haan toelagen 7.82m FOI residual (police 6.04m)",
           F["toelagen"], 7.0, 5.5, 3.5, 6.15, "Named matrix FOI"),
        lb("lb_dha_police_6_04m_2025", "De Haan police toelage 6.04m FOI residual",
           F["police"], 6.5, 5.5, 3.5, 5.95, "PZ path FOI"),
        lb("lb_dha_pension_jump_2025", "De Haan pension LT jump 13.75 to 14.67m FOI residual",
           pen_jump, 8.0, 4.0, 3.5, 6.05, "Pension path FOI"),
        lb("lb_dha_ocmw_cover_1_71m_2025", "De Haan OCMW cover FULL 1.71m FOI residual",
           F["ocmw_cover"], 8.0, 4.0, 3.5, 6.05, "Cover policy FOI"),
        lb("lb_dha_afm_5_40m_2025", "De Haan AFM +5.40m VERY STRONG FOI residual",
           F["afm"], 5.0, 5.5, 3.0, 5.45, "Keep AFM path"),
        lb("lb_dha_invest_underspend_2025", "De Haan invest 5.96 vs MJP 7.82 UNDERSPEND FOI residual",
           under, 7.0, 4.0, 3.5, 5.55, "Invest path FOI"),
        lb("lb_dha_fin_debt_12_53m_2025", "De Haan fin debt 12.53m FOI residual",
           F["fin_debt"], 5.5, 5.5, 3.5, 5.4, "Debt stock FOI"),
    ]
    append_csv(DATA / "leaderboard.csv", lbs)

    src_row = (
        f"{SRC},Gemeente+OCMW De Haan BBC Jaarrekening 2025,{URL},"
        f"Gemeente De Haan,2026-08-11,primary_pdf,"
        f"tick1111; 209p text extract; KBO GE 0216.770.848 / OCMW 0216.770.947; NIS 35029; "
        f"AD Kimberley Carton FD Bart Dewulf; Leopoldlaan 24 8420 De Haan; "
        f"assets 150.724m cash 34.541m VERY HIGH fin debt 12.528m DECLINE new loans 1.228m "
        f"pension 14.673m JUMP FVA IGS 29.999m AFM +5.396m BBR 32.730m VERY HIGH budget +1.629m "
        f"P&L +1.937m FLIP toelagen 7.818m police 6.039m OCMW cover 1.713m FULL; "
        f"primary PDF staged docs/doge/raw/dehaan_jr2025.pdf"
    )
    append_csv(DATA / "sources.csv", [src_row])

    ent_row = (
        f"{ENT},Gemeente De Haan,Commune de De Haan,Municipality of De Haan,"
        f"municipality,vlaanderen_gov,nl,https://www.dehaan.be,info@dehaan.be,"
        f"Leopoldlaan 24 8420 De Haan,"
        f"JR2025 dual residual tick1111; KBO 0216.770.848 / OCMW 0216.770.947; "
        f"assets 150.724m cash 34.541m VERY HIGH fin debt 12.528m AFM +5.396m BBR 32.730m "
        f"pension 14.673m toelagen 7.818m police 6.039m OCMW cover 1.713m FULL; "
        f"AD Kimberley Carton FD Bart Dewulf"
    )
    append_csv(DATA / "entities.csv", [ent_row])

    foi_row = (
        f"{GAP},Vlaanderen>Gemeenten>DeHaan>toelagen_pension_ocmw_invest_L5,{ENT},"
        f"\"Toelagen matrix detail within 7.818m (police 6.039 / fire 1.025 / IGS 0.399 / andere 0.304) "
        f"named >=50k; pension JUMP 13.751to14.673m actuarial; OCMW cover FULL 1.713m vs OCMW P&L "
        f"-1.577m and cum equity -3.312m multi-year path; invest underspend 5.958 vs MJP 7.820; "
        f"invest-subs JUMP 0.706m (HVZ 0.205 / eredienst 0.296 / andere 0.206); new loans/leasing "
        f"1.228m purpose; FVA IGS 29.999m composition; toegestane leningen IGS 0.238m terms\","
        f"\"Coastal muni with VERY HIGH cash 34.5m and BBR 32.7m + strong AFM +5.4m but large police "
        f"toelage 6.0m + pension JUMP + OCMW structural cover FOI-adjacent\","
        f"9,Gemeente De Haan,info@dehaan.be,Leopoldlaan 24 8420 De Haan,"
        f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-11,,,,,"
        f"comm_dha_toelagen_2025,lb_dha_toelagen_7_82m_2025,"
        f"{UTC},{UTC},tick1111; ready not sent; do not send without human OK"
    )
    append_csv(DATA / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = f"""# FOI draft — {GAP}

**Status:** ready (NOT sent)  
**Gap ID:** {GAP}  
**Tick:** {TICK}  

## Recipient

- Gemeente De Haan openbaarheid / financieel directeur Bart Dewulf  
- E-mail: info@dehaan.be  
- Adres: Leopoldlaan 24, 8420 De Haan  

## Subject

Openbaarheid — Jaarrekening 2025 Gemeente/OCMW De Haan: toelagen, pensioen, OCMW, investeringen

## Body (NL)

```text
[Naam]
[Adres]
[E-mail]
[Datum]

Aan: Gemeente De Haan
t.a.v. de financieel directeur

Betreft: Verzoek openbaarheid — jaarrekening 2025 Gemeente en OCMW De Haan

Geachte,

Op grond van de regels inzake openbaarheid van bestuur vraag ik de volgende
documenten en toelichtingen.

### 1. Reeds openbaar (BBC JR2025; De Haan)

- Activa **EUR150,724m**; nettoactief **EUR116,904m**; fin. schuld **EUR12,528m**
  (LT 11,007 / ST 1,521; DECLINE vs 12,902m); nieuwe leningen/leasing
  **EUR1,228m**; cash **EUR34,541m VERY HIGH**; pensioen LT **EUR14,673m JUMP**
  (was 13,751m); FVA IGS **EUR29,999m**; herwaard **EUR6,736m**; AFM
  **+EUR5,396m**; BBR **EUR32,730m VERY HIGH**; budget **+EUR1,629m**; P&L
  **+EUR1,937m FLIP**; toelagen **EUR7,818m** (politie **EUR6,039m** / HVZ
  **EUR1,025m** / IGS **EUR0,399m** / andere **EUR0,304m**); invest
  **EUR5,958m** vs MJP **EUR7,820m UNDERSPEND**; OCMW-tussenkomst
  **EUR1,713m FULL** (OCMW P&L **−EUR1,577m**; cum equity **−EUR3,312m**).

### 2. Gevraagde stukken / toelichtingen

1. **Toelagen-matrix** binnen EUR7,818m: nominatieve lijst ≥ EUR50k (politiezone-
   detail, HVZ, IGS, eredienst, andere).
2. **Pensioenvoorzieningen JUMP** 13,751 → 14,673m: actuariële aannames, vrijval/
   dotatie 2025, impact op P&L.
3. **OCMW cover FULL EUR1,713m** vs OCMW P&L −EUR1,577m en cum equity
   −EUR3,312m: liquiditeitsbeleid en meerjarenpad 2020–2026.
4. **Invest underspend** 5,96 vs MJP 7,82m + invest-subs JUMP 0,706m (HVZ/eredienst/
   andere): projectenlijst en overdrachten 2026.
5. **Nieuwe leningen/leasing EUR1,228m** en **toegestane leningen IGS EUR0,238m**:
   kredietgever, doel, looptijd.
6. **FVA IGS EUR29,999m**: deelnemingenmatrix (Fluvius/andere).

Gelieve te antwoorden binnen de wettelijke termijn. Digitaal leveren (PDF) heeft
de voorkeur.

Met vriendelijke groeten,

[Naam]
[Contact]
```

## Notes

- Primary source: BBC JR2025 Gemeente+OCMW De Haan (209p text; AD Carton FD Dewulf).  
- **Do not send** without human OK.  
- Tick 1111 dual residual after Schelle AGB (tick1110).
"""
    (FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

    # research queue
    rq_path = DATA / "research_queue.csv"
    lines = rq_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("rq_1111,"):
            out.append(
                "rq_1111,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
                "De Haan GE+OCMW JR2025 dual residual,"
                f"{GAP},2026-08-11T20:30:00Z,{UTC},"
                "tick1111 De Haan assets 150.724m cash 34.541m VERY HIGH AFM +5.396m BBR 32.730m "
                "pension 14.673m JUMP toelagen 7.818m police 6.039m OCMW cover 1.713m FULL; FOI ready"
            )
        else:
            out.append(line)
    out.append(
        "rq_1112,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
        "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen login-blocked / Vorselaar docs-only / "
        "Kalmthout / Bornem JR2024-only / Schelle GE+OCMW if published / De Panne OCR-blocked if OCR / other); "
        "prefer FOI-adjacent L5; skip rq_116,"
        f",2026-08-11T21:00:00Z,{UTC},"
        "spawned tick1111 after De Haan dual residual; next residual dual L5; progress@1120 in 9"
    )
    rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    state = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{UTC},rq_1111,1111,no,"
        "tick1111 De Haan GE+OCMW JR2025 dual residual; FOI gap_dha_toelagen_pension_ocmw_invest_l5 prio9 ready; "
        "assets 150.724m cash 34.541m VERY HIGH equity 116.904m fin debt 12.528m DECLINE new loans 1.228m "
        "pension 14.673m JUMP FVA IGS 29.999m AFM +5.396m BBR 32.730m VERY HIGH budget +1.629m P&L +1.937m FLIP "
        "toelagen 7.818m police 6.039m OCMW cover 1.713m FULL; next residual dual L5 rq_1112; "
        "progress@1120 in 9; rq_116 deferred\n"
    )
    (DATA / "loop_state.csv").write_text(state, encoding="utf-8")

    log_entry = f"""
### Tick 1111 - {UTC}

- Unit: **rq_1111** (FOI-adjacent residual dual - **Gemeente+OCMW De Haan Jaarrekening 2025** + Schelle AGB dual residual)
- Found (strong primary BBC JR2025 209p text; dehaan.be; KBO GE 0216.770.848 / OCMW 0216.770.947; NIS 35029; Leopoldlaan 24 8420; AD Kimberley Carton FD Bart Dewulf; GE+OCMW):
  - Assets **EUR150.724m** (was **EUR147.496m**) / equity **EUR116.904m** / debt total **EUR33.820m** / fin debt **EUR12.528m DECLINE FOI** (LT **EUR11.007m** / ST due **EUR1.521m**; was **EUR12.902m**)
  - New loans/leasing **EUR1.228m FOI** / repayments **EUR1.584m**
  - Cash **EUR34.541m VERY HIGH FOI** (was **EUR33.653m**) / pension **EUR14.673m JUMP FOI** (was **EUR13.751m**; +**EUR0.922m**)
  - FVA IGS **EUR29.999m HIGH FOI** / herwaard **EUR6.736m** / leasing MVA **EUR9.152m**
  - Exploitatie: ontvangsten **EUR40.162m** / uitgaven **EUR33.418m** / saldo **+EUR6.745m VERY STRONG**
  - AFM **+EUR5.396m VERY STRONG** (gecorr **+EUR5.949m**) / BBR **EUR32.730m VERY HIGH** / budget **+EUR1.629m POS** (MJP was **−EUR1.718m**) / P&L **+EUR1.937m FLIP FOI** (was **−EUR2.175m**)
  - Fiscal **EUR27.015m** / PB **EUR3.992m** / OP **EUR12.406m** / personnel **EUR16.408m**
  - Toelagen **EUR7.818m FOI** (police **EUR6.039m** / fire **EUR1.025m** / IGS **EUR0.399m** / eredienst **EUR0.052m** / andere **EUR0.304m**)
  - Invest **EUR5.958m** vs MJP **EUR7.820m UNDERSPEND FOI** / invest-subs **EUR0.706m JUMP** (was **EUR0.348m**; HVZ **EUR0.205m** / eredienst **EUR0.296m** / andere **EUR0.206m**)
  - OCMW cover **EUR1.713m FULL FOI** / OCMW P&L **−EUR1.577m** / OCMW cum equity **−EUR3.312m DEEP** / OCMW hulp **EUR1.797m**
  - Toegestane leningen IGS **EUR0.238m FOI**
- Dual: Schelle AGB MJP debt ramp YE2027 EUR5.84m / cash CRITICAL (tick1110) - not TE-additive
- Note: Oosterzele / Nijlen login-blocked / Vorselaar docs-only / Kalmthout / Bornem JR2024-only / De Panne OCR-blocked / Schelle GE+OCMW residual next; progress@1120 in 9
- Wrote: budgets +40 (bud_dha_*); commitments +8; leaderboard +10; sources +1; entity city_dehaan; FOI **gap_dha_toelagen_pension_ocmw_invest_l5** prio9 ready + draft; PDF primary (not committed 4.5MB); rq_1111=done; spawn **rq_1112**; ticks=1111
- FOI: ready only - **do not send**
- Next: prio5 **rq_1112** residual dual L5; deferred **rq_116**; progress@1120 in 9
"""
    log_text = LOG.read_text(encoding="utf-8")
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding="utf-8")

    print("tick1111 write OK")
    print("budgets", len(bud), "commitments", len(comm), "lbs", len(lbs))
    print("gap", GAP)


if __name__ == "__main__":
    main()

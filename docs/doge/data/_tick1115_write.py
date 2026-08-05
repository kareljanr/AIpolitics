# -*- coding: utf-8 -*-
"""tick 1115 — AGB Evergem JR2025 Entity II dual residual after Evergem GE+OCMW"""
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

TICK = 1115
UTC = "2026-08-11T23:00:00Z"
SRC = "src_evergem_agb_jr2025"
ENT = "agb_evergem"
CITY = "city_evergem"
GAP = "gap_eve_agb_city_toelage_loans_invest_l5"
URL = "https://www.evergem.be/jaarrekening"
# primary: file/download/113719 AGB Beleidsrapport RvB 15.06.2026

F = dict(
    assets=7813612,
    assets_was=7327464,
    equity=3606504,
    debt_total=4207108,
    fin_debt=2459726,
    fin_debt_lt=1949826,
    fin_debt_st=509901,
    fin_debt_was=2689573,
    new_loans=301500,
    repayments=531347,
    cash=3201356,
    cash_was=2229784,
    expl_ont=3555658,
    expl_uit=2902677,
    expl_saldo=652981,
    afm=121634,
    afm_gecorr=437815,
    bbr=3074040,
    budget_result=155941,
    cum_br=3074040,
    pnl=231511,
    dividend=100000,
    omzet=3542379,
    goederen=2619186,
    fin_exp=57399,
    invest_uit=301500,
    invest_ont=34306,
    invest_saldo=-267194,
    invest_mjp=414904,
    city_toelage_from_ge=1438047,  # from GE T2 AGB line tick1114
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

    b("bud_eveagb_assets_2025", F["assets"], "AGB assets YE2025 7.814m JUMP (was 7.327m); tick1115")
    b("bud_eveagb_equity_2025", F["equity"], "Nettoactief YE2025 3.607m; tick1115")
    b("bud_eveagb_debt_total_2025", F["debt_total"], "Total schulden YE2025 4.207m; tick1115")
    b("bud_eveagb_fin_debt_2025", F["fin_debt"], "Fin debt YE2025 2.460m DECLINE FOI (was 2.690m); tick1115")
    b("bud_eveagb_fin_debt_lt_2025", F["fin_debt_lt"], "Fin debt LT YE2025 1.950m; tick1115")
    b("bud_eveagb_fin_debt_st_2025", F["fin_debt_st"], "Fin debt ST due YE2025 0.510m; tick1115")
    b("bud_eveagb_new_loans_2025", F["new_loans"], "New loans 0.302m FOI (=invest); tick1115")
    b("bud_eveagb_repayments_2025", F["repayments"], "Periodieke aflossingen 0.531m; tick1115")
    b("bud_eveagb_cash_2025", F["cash"], "Cash YE2025 3.201m JUMP FOI (was 2.230m); tick1115")
    b("bud_eveagb_expl_ontvangsten_2025", F["expl_ont"], "Exploitatie ontvangsten 3.556m; tick1115")
    b("bud_eveagb_expl_uitgaven_2025", F["expl_uit"], "Exploitatie uitgaven 2.903m; tick1115")
    b("bud_eveagb_expl_saldo_2025", F["expl_saldo"], "Exploitatiesaldo +0.653m STRONG; tick1115")
    b("bud_eveagb_afm_2025", F["afm"], "AFM +0.122m FLIP FOI (MJP was -0.205m); tick1115")
    b("bud_eveagb_afm_gecorr_2025", F["afm_gecorr"], "AFM gecorrigeerd +0.438m; tick1115")
    b("bud_eveagb_bbr_2025", F["bbr"], "BBR 3.074m HIGH; tick1115")
    b("bud_eveagb_budget_result_2025", F["budget_result"], "Budget +0.156m POS (MJP was -0.205m); tick1115")
    b("bud_eveagb_pnl_2025", F["pnl"], "P&L +0.232m POS; tick1115")
    b("bud_eveagb_dividend_2025", F["dividend"], "Uitgekeerde winst 0.100m FOI residual; tick1115")
    b("bud_eveagb_omzet_2025", F["omzet"], "Omzet/werking 3.542m; tick1115")
    b("bud_eveagb_goederen_2025", F["goederen"], "Goederen en diensten 2.619m (no personnel); tick1115")
    b("bud_eveagb_invest_uitgaven_2025", F["invest_uit"], "Invest 0.302m vs MJP 0.415m UNDERSPEND FOI; tick1115")
    b("bud_eveagb_invest_mjp_2025", F["invest_mjp"], "MJP invest uitgaven 0.415m; tick1115")
    b("bud_eveagb_city_toelage_2025", F["city_toelage_from_ge"], "City AGB toelage from GE 1.438m FOI residual (GE T2); tick1115")
    append_csv(DATA / "budgets.csv", bud)

    under = F["invest_mjp"] - F["invest_uit"]
    comm = [
        f"comm_eveagb_fin_debt_2025,Evergem AGB fin debt YE2025 2.460m DECLINE,{ENT},creditors,BBC JR2025,,2025,2045,{F['fin_debt']},{{2025:{F['fin_debt']}}},{F['fin_debt']},active,,AGB capital finance DECLINE,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB>debt,tick1115",
        f"comm_eveagb_city_toelage_2025,Evergem AGB city toelage 1.438m 2025,{CITY},{ENT},BBC GE JR2025 T2,,2025,2025,{F['city_toelage_from_ge']},{{2025:{F['city_toelage_from_ge']}}},0,active,,City-AGB toelage FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB>toelage,tick1115; from GE toelagen matrix",
        f"comm_eveagb_dividend_2025,Evergem AGB dividend 0.100m 2025,{ENT},Gemeente Evergem,BBC JR2025,,2025,2025,{F['dividend']},{{2025:{F['dividend']}}},0,active,,Dividend FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB>dividend,tick1115",
        f"comm_eveagb_afm_flip_2025,Evergem AGB AFM flip +0.122m 2025,{ENT},AGB operations,BBC JR2025,,2025,2025,{F['afm']},{{2025:{F['afm']}}},0,active,,AFM FLIP FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB>afm,tick1115; MJP was -0.205m",
        f"comm_eveagb_cash_jump_2025,Evergem AGB cash 3.201m JUMP 2025,{ENT},treasury,BBC JR2025,,2025,2025,{F['cash']},{{2025:{F['cash']}}},0,active,,Cash JUMP FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB>cash,tick1115",
        f"comm_eveagb_invest_underspend_2025,Evergem AGB invest 0.302 vs MJP 0.415 UNDERSPEND 2025,{ENT},Capital program,BBC JR2025,,2025,2025,{F['invest_uit']},{{2025:{F['invest_uit']}}},0,active,,UNDERSPEND FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB>invest,tick1115",
        f"comm_eveagb_new_loans_2025,Evergem AGB new loans 0.302m 2025,{ENT},creditors,BBC JR2025 T4,,2025,2025,{F['new_loans']},{{2025:{F['new_loans']}}},0,active,,New loans=invest FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Evergem>AGB>loans,tick1115",
    ]
    append_csv(DATA / "commitments.csv", comm)

    lb_note = "tick1115; primary Evergem AGB JR2025; Entity II dual residual after Evergem GE+OCMW; not TE-additive"

    def lb(iid, name, annual, abs_s, cost_s, diff_s, pri, cut):
        return (
            f"{iid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>Evergem_AGB_L5,"
            f"{annual},{annual},JR2025 AGB dual residual map VL,strong,{SRC},"
            f"Evergem residents,Local AGB dual residual map VL JR2025,"
            f"JR2025 BBC AGB Evergem realized figures,"
            f"{abs_s},{cost_s},{diff_s},{pri},{cut},active,,{lb_note}"
        )

    lbs = [
        lb("lb_eveagb_city_toelage_1_44m_2025", "Evergem AGB city toelage 1.44m FOI residual",
           F["city_toelage_from_ge"], 8.0, 4.0, 3.0, 5.9, "Beheersovereenkomst FOI"),
        lb("lb_eveagb_bbr_3_07m_2025", "Evergem AGB BBR 3.07m FOI residual",
           F["bbr"], 5.5, 4.5, 3.0, 5.15, "Keep BBR path"),
        lb("lb_eveagb_cash_3_20m_2025", "Evergem AGB cash 3.20m JUMP FOI residual",
           F["cash"], 6.0, 4.5, 3.0, 5.35, "Treasury FOI"),
        lb("lb_eveagb_fin_debt_2_46m_2025", "Evergem AGB fin debt 2.46m FOI residual",
           F["fin_debt"], 5.5, 4.5, 3.5, 5.1, "Debt stock FOI"),
        lb("lb_eveagb_afm_flip_0_12m_2025", "Evergem AGB AFM flip +0.12m FOI residual",
           F["afm"], 7.5, 2.5, 3.0, 5.15, "Keep AFM path"),
        lb("lb_eveagb_dividend_0_10m_2025", "Evergem AGB dividend 0.10m FOI residual",
           F["dividend"], 7.0, 2.0, 3.0, 4.7, "Dividend policy FOI"),
        lb("lb_eveagb_invest_underspend_2025", "Evergem AGB invest 0.30 vs MJP 0.41 UNDERSPEND FOI residual",
           under, 7.0, 2.5, 3.5, 4.85, "Invest path FOI"),
        lb("lb_eveagb_omzet_3_54m_2025", "Evergem AGB omzet 3.54m FOI residual",
           F["omzet"], 5.0, 4.5, 3.0, 4.95, "Volume FOI"),
        lb("lb_eveagb_pnl_0_23m_2025", "Evergem AGB P&L +0.23m FOI residual",
           F["pnl"], 5.5, 2.5, 3.0, 4.25, "Keep P&L path"),
    ]
    append_csv(DATA / "leaderboard.csv", lbs)

    src_row = (
        f"{SRC},AGB Evergem BBC Jaarrekening 2025,{URL},"
        f"AGB Evergem / Gemeente Evergem,2026-08-11,primary_pdf,"
        f"tick1115; 128p text; KBO 0878.328.763; AD Danny Coene FD Christ Coquyt Voorzitter Kenny Ketels; "
        f"F. De Kokerlaan 11 9940; RvB 15.06.2026; assets 7.814m cash 3.201m JUMP fin debt 2.460m DECLINE "
        f"AFM +0.122m FLIP BBR 3.074m budget +0.156m P&L +0.232m dividend 0.100m no personnel "
        f"city toelage from GE 1.438m; primary PDF staged docs/doge/data/_tmp/evergem_agb_jr2025.pdf"
    )
    append_csv(DATA / "sources.csv", [src_row])

    ent_row = (
        f"{ENT},AGB Evergem,Régie communale autonome Evergem,Autonomous municipal company Evergem,"
        f"municipal_agency,{CITY},nl,{URL},christ.coquyt@evergem.be,"
        f"F. De Kokerlaan 11 9940 Evergem,"
        f"JR2025 Entity II dual residual tick1115; KBO 0878.328.763; assets 7.814m cash 3.201m "
        f"fin debt 2.460m AFM +0.122m FLIP BBR 3.074m city toelage 1.438m no staff; "
        f"AD Danny Coene FD Christ Coquyt"
    )
    append_csv(DATA / "entities.csv", [ent_row])

    foi_row = (
        f"{GAP},Vlaanderen>Gemeenten>Evergem>agb_city_toelage_loans_invest_L5,{CITY},"
        f"\"AGB city toelage 1.438m beheersovereenkomst KPI/performance 2025-2031; new loans 0.302m "
        f"lender/purpose (=invest alignment); dividend 0.100m policy multi-year; invest underspend 0.302 "
        f"vs MJP 0.415; cash JUMP 2.230to3.201m treasury vs city cash 52.2m; zero personnel model "
        f"outsourcing detail; AFM FLIP path sustain\","
        f"\"Entity II residual after Evergem GE+OCMW: AGB healthy AFM flip under city toelage 1.4m while "
        f"GE carries DEEP OCMW hole; dual FOI-adjacent\","
        f"9,Gemeente Evergem / AGB Evergem,info@evergem.be,F. De Kokerlaan 11 9940 Evergem,"
        f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-11,,,,,"
        f"comm_eveagb_city_toelage_2025,lb_eveagb_city_toelage_1_44m_2025,"
        f"{UTC},{UTC},tick1115; ready not sent; do not send without human OK"
    )
    append_csv(DATA / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = f"""# FOI draft — {GAP}

**Status:** ready (NOT sent)  
**Gap ID:** {GAP}  
**Tick:** {TICK}  

## Recipient

- Gemeente Evergem / AGB Evergem openbaarheid / financieel directeur Christ Coquyt  
- E-mail: info@evergem.be / christ.coquyt@evergem.be  
- Adres: F. De Kokerlaan 11, 9940 Evergem  

## Subject

Openbaarheid — AGB Evergem jaarrekening 2025: gemeentetoelage, leningen, dividend, investeringen

## Body (NL)

```text
[Naam]
[Adres]
[E-mail]
[Datum]

Aan: Gemeente Evergem / AGB Evergem
t.a.v. de financieel directeur

Betreft: Verzoek openbaarheid — jaarrekening 2025 AGB Evergem

Geachte,

Op grond van de regels inzake openbaarheid van bestuur vraag ik de volgende
documenten en toelichtingen.

### 1. Reeds openbaar (BBC JR2025 AGB; evergem.be; RvB 15.06.2026)

- AGB activa **EUR7,814m**; nettoactief **EUR3,607m**; fin. schuld **EUR2,460m
  DECLINE** (LT 1,950 / ST 0,510; was 2,690m); nieuwe leningen **EUR0,302m**;
  cash **EUR3,201m JUMP** (was 2,230m); AFM **+EUR0,122m FLIP** (MJP was
  −EUR0,205m); BBR **EUR3,074m**; budget **+EUR0,156m**; P&L **+EUR0,232m**;
  uitgekeerde winst **EUR0,100m**; omzet **EUR3,542m**; goederen/diensten
  **EUR2,619m** (geen personeel); invest **EUR0,302m** vs MJP **EUR0,415m
  UNDERSPEND**.
- Vanuit JR2025 Gemeente+OCMW: AGB-toelage gemeente **EUR1,438m**.

### 2. Gevraagde stukken / toelichtingen

1. **Gemeentetoelage EUR1,438m:** beheersovereenkomst 2025–2031, KPI’s,
   meerjarenpad en relatie tot AGB-dividend EUR0,100m.
2. **Nieuwe leningen EUR0,302m** (= invest): kredietgever, doel, looptijd;
   aansluiting fin. schuld 2,460m.
3. **Dividend EUR0,100m:** resultaatsbestemming multi-year policy.
4. **Cash JUMP** 2,230 → 3,201m: liquiditeitsbeleid vs gemeentelijke cash
   EUR52,2m.
5. **Zero-personnel model:** outsourcing/contractantenmatrix goederen/diensten
   EUR2,619m.
6. **Invest underspend** 0,302 vs MJP 0,415m: uitgestelde projecten 2026.
7. **AFM FLIP** sustain-pad 2026–2031.

Gelieve te antwoorden binnen de wettelijke termijn. Digitaal leveren (PDF) heeft
de voorkeur.

Met vriendelijke groeten,

[Naam]
[Contact]
```

## Notes

- Primary source: BBC JR2025 AGB Evergem (128p; KBO 0878.328.763; AD Coene FD Coquyt).  
- Dual residual after Evergem GE+OCMW (tick1114).  
- **Do not send** without human OK.  
- Tick 1115.
"""
    (FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

    rq_path = DATA / "research_queue.csv"
    lines = rq_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("rq_1115,"):
            out.append(
                "rq_1115,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
                "Evergem AGB JR2025 Entity II dual residual,"
                f"{GAP},2026-08-11T22:30:00Z,{UTC},"
                "tick1115 Evergem AGB assets 7.814m cash 3.201m JUMP fin debt 2.460m AFM +0.122m FLIP "
                "BBR 3.074m city toelage 1.438m dividend 0.100m; FOI ready"
            )
        else:
            out.append(line)
    out.append(
        "rq_1116,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
        "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen login-blocked / Vorselaar docs-only / "
        "Kalmthout / Bornem JR2024-only / De Panne OCR / Schelle GE+OCMW if published / Erpe-Mere docs-only 2025 / other); "
        "prefer FOI-adjacent L5; skip rq_116,"
        f",2026-08-11T23:00:00Z,{UTC},"
        "spawned tick1115 after Evergem AGB Entity II dual residual; next residual dual L5; progress@1120 in 5"
    )
    rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    state = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{UTC},rq_1115,1115,no,"
        "tick1115 Evergem AGB JR2025 Entity II dual residual after Evergem GE+OCMW; "
        "FOI gap_eve_agb_city_toelage_loans_invest_l5 prio9 ready; assets 7.814m cash 3.201m JUMP "
        "fin debt 2.460m DECLINE AFM +0.122m FLIP BBR 3.074m budget +0.156m P&L +0.232m dividend 0.100m "
        "city toelage 1.438m no personnel; next residual dual L5 rq_1116; progress@1120 in 5; rq_116 deferred\n"
    )
    (DATA / "loop_state.csv").write_text(state, encoding="utf-8")

    log_entry = f"""
### Tick 1115 - {UTC}

- Unit: **rq_1115** (FOI-adjacent residual dual - **AGB Evergem Jaarrekening 2025** Entity II + Evergem GE+OCMW dual residual)
- Found (strong primary BBC JR2025 AGB 128p text; evergem.be; RvB 15.06.2026; KBO 0878.328.763; F. De Kokerlaan 11 9940; AD Danny Coene FD Christ Coquyt Voorzitter Kenny Ketels; AGB only — dual after GE+OCMW tick1114):
  - Assets **EUR7.814m JUMP** (was **EUR7.327m**) / equity **EUR3.607m** / debt total **EUR4.207m** / fin debt **EUR2.460m DECLINE FOI** (LT **EUR1.950m** / ST due **EUR0.510m**; was **EUR2.690m**)
  - New loans **EUR0.302m FOI** (=invest) / repayments **EUR0.531m**
  - Cash **EUR3.201m JUMP FOI** (was **EUR2.230m**)
  - Exploitatie: ontvangsten **EUR3.556m** / uitgaven **EUR2.903m** / saldo **+EUR0.653m STRONG**
  - AFM **+EUR0.122m FLIP FOI** (MJP was **−EUR0.205m**; gecorr **+EUR0.438m**) / BBR **EUR3.074m HIGH** / budget **+EUR0.156m POS** / P&L **+EUR0.232m POS**
  - Omzet **EUR3.542m** / goederen **EUR2.619m** / **personeel EUR0 ZERO** (outsourcing model FOI)
  - **Uitgekeerde winst / dividend EUR0.100m FOI**
  - Invest **EUR0.302m** vs MJP **EUR0.415m UNDERSPEND FOI**
  - **City AGB toelage from GE EUR1.438m FOI** (GE T2 tick1114)
- Dual: Evergem GE cash VERY HIGH / OCMW DEEP hole (tick1114) - not TE-additive
- Note: Oosterzele / Nijlen login-blocked / Vorselaar docs-only / Kalmthout / Bornem JR2024-only / De Panne OCR / Erpe-Mere docs-only 2025 residual next; progress@1120 in 5
- Wrote: budgets +23 (bud_eveagb_*); commitments +7; leaderboard +9; sources +1; entity agb_evergem; FOI **gap_eve_agb_city_toelage_loans_invest_l5** prio9 ready + draft; PDF primary (not committed 6.5MB); rq_1115=done; spawn **rq_1116**; ticks=1115
- FOI: ready only - **do not send**
- Next: prio5 **rq_1116** residual dual L5; deferred **rq_116**; progress@1120 in 5
"""
    log_text = LOG.read_text(encoding="utf-8")
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding="utf-8")

    print("tick1115 write OK")
    print("budgets", len(bud), "commitments", len(comm), "lbs", len(lbs))
    print("gap", GAP)


if __name__ == "__main__":
    main()

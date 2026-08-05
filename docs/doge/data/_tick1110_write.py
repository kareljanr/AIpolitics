# -*- coding: utf-8 -*-
"""tick 1110 — progress@1110 decade + Schelle AGB Fluctus JR2025 dual residual"""
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

TICK = 1110
UTC = "2026-08-11T20:30:00Z"
SRC = "src_schelle_agb_jr2025"
ENT = "agb_schelle_fluctus"
CITY = "city_schelle"
GAP = "gap_sch_agb_debt_ramp_prijssub_geocmw_l5"
URL = "https://www.schelle.be/wp-content/uploads/2026/07/JAARREKENING_AGB_2025-1.pdf"
PAGE = "https://www.schelle.be/bestuur-beleid/agb-fluctus-schelle/"

# AGB Fluctus Schelle BBC JR2025 (kengetallen / J2 / J4 / J5 / T4)
F = dict(
    assets=1207624,
    equity=624259,
    debt_total=583365,
    fin_debt=530865,
    fin_debt_lt=406330,  # financial LT from J4 (passiva LT fin)
    fin_debt_st=124535,  # ST due within year
    new_loans=53068,
    repayments=129694,
    cash=51165,
    expl_ont=883586,
    expl_uit=663339,
    expl_saldo=220247,
    afm=90553,
    afm_gecorr=171647,
    bbr=173792,
    budget_result=87636,
    cum_br=173792,
    pnl=84951,
    personnel=373770,  # J5 bezoldigingen
    personnel_was=512882,
    prijssub=565988,  # prijssubsidie gemeente kengetallen
    werkingsub=101349,  # werkingssubsidies J5
    invest_uit=53068,
    invest_ont=-2917,
    invest_saldo=-55984,
    invest_mjp=206000,
    omzet=708225,
    fin_exp=3359,
    mjp_debt_2026=1911119,
    mjp_new_2026=1516000,
    mjp_debt_2027=5844135,
    mjp_new_2027=4016000,
)


def append_csv(path: Path, rows: list[str]):
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")


def main():
    # --- budgets ---
    bud = []
    def b(bid, amt, note):
        bud.append(f"{bid},{ENT},2025,{amt},,,bbc_jr_realized,{SRC},strong,{note}")

    b("bud_schagb_assets_2025", F["assets"], "AGB assets YE2025 1.208m slight DROP (was 1.249m); tick1110")
    b("bud_schagb_equity_2025", F["equity"], "Nettoactief YE2025 0.624m JUMP (was 0.544m); tick1110")
    b("bud_schagb_debt_total_2025", F["debt_total"], "Total schulden YE2025 0.583m DECLINE (was 0.705m); tick1110")
    b("bud_schagb_fin_debt_2025", F["fin_debt"], "Fin debt (leningen) YE2025 0.531m DECLINE FOI (was 0.607m); tick1110")
    b("bud_schagb_fin_debt_lt_2025", F["fin_debt_lt"], "Fin debt LT YE2025 0.406m; tick1110")
    b("bud_schagb_fin_debt_st_2025", F["fin_debt_st"], "Fin debt ST due YE2025 0.125m; tick1110")
    b("bud_schagb_new_loans_2025", F["new_loans"], "New loans 0.053m modest; tick1110")
    b("bud_schagb_repayments_2025", F["repayments"], "Periodieke aflossingen 0.130m; tick1110")
    b("bud_schagb_cash_2025", F["cash"], "Cash YE2025 0.051m CRITICAL LOW FOI; tick1110")
    b("bud_schagb_expl_ontvangsten_2025", F["expl_ont"], "Exploitatie ontvangsten 0.884m; tick1110")
    b("bud_schagb_expl_uitgaven_2025", F["expl_uit"], "Exploitatie uitgaven 0.663m; tick1110")
    b("bud_schagb_expl_saldo_2025", F["expl_saldo"], "Exploitatiesaldo +0.220m STRONG; tick1110")
    b("bud_schagb_afm_2025", F["afm"], "AFM +0.091m (was near-zero MJP 0.0003m); tick1110")
    b("bud_schagb_afm_gecorr_2025", F["afm_gecorr"], "AFM gecorrigeerd +0.172m VERY STRONG; tick1110")
    b("bud_schagb_bbr_2025", F["bbr"], "Beschikbaar budgettair resultaat 0.174m; tick1110")
    b("bud_schagb_budget_result_2025", F["budget_result"], "Budgettair resultaat +0.088m POS; tick1110")
    b("bud_schagb_pnl_2025", F["pnl"], "P&L overschot +0.085m FLIP FOI (was -0.021m); tick1110")
    b("bud_schagb_personnel_2025", F["personnel"], "Personeel 0.374m DECLINE FOI (was 0.513m); tick1110")
    b("bud_schagb_prijssub_2025", F["prijssub"], "Prijssubsidie gemeente 0.566m FOI residual; tick1110")
    b("bud_schagb_werkingssub_2025", F["werkingsub"], "Werkingssubsidies 0.101m; tick1110")
    b("bud_schagb_invest_uitgaven_2025", F["invest_uit"], "Investeringsuitgaven 0.053m vs MJP 0.206m UNDERSPEND FOI; tick1110")
    b("bud_schagb_invest_mjp_2025", F["invest_mjp"], "MJP invest uitgaven 0.206m; tick1110")
    b("bud_schagb_omzet_2025", F["omzet"], "Omzet 0.708m DROP -15.7pct FOI (was 0.840m); tick1110")
    b("bud_schagb_mjp_debt_2026", F["mjp_debt_2026"], "MJP fin debt YE2026 1.911m MASSIVE RAMP FOI; tick1110")
    b("bud_schagb_mjp_new_2026", F["mjp_new_2026"], "MJP new loans 2026 1.516m MASSIVE FOI; tick1110")
    b("bud_schagb_mjp_debt_2027", F["mjp_debt_2027"], "MJP fin debt YE2027 5.844m MASSIVE RAMP FOI; tick1110")
    b("bud_schagb_mjp_new_2027", F["mjp_new_2027"], "MJP new loans 2027 4.016m MASSIVE FOI; tick1110")
    append_csv(DATA / "budgets.csv", bud)

    # --- commitments ---
    comm = [
        f"comm_schagb_fin_debt_2025,Schelle AGB Fluctus fin debt YE2025 0.531m,{ENT},creditors,BBC JR2025,,2025,2045,{F['fin_debt']},{{2025:{F['fin_debt']}}},{F['fin_debt']},active,,AGB capital finance DECLINE,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Schelle>AGB>debt,tick1110; LT 0.406 ST 0.125 new 0.053",
        f"comm_schagb_prijssub_2025,Schelle AGB prijssubsidie gemeente 0.566m 2025,{CITY},{ENT},BBC JR2025,,2025,2025,{F['prijssub']},{{2025:{F['prijssub']}}},0,active,,City price-subsidy to AGB FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Schelle>AGB>prijssub,tick1110",
        f"comm_schagb_mjp_debt_ramp_2027,Schelle AGB MJP fin debt ramp to 5.844m YE2027,{ENT},creditors,BBC JR2025 T4 MJP,,2026,2027,{F['mjp_debt_2027']},{{2026:{F['mjp_debt_2026']},2027:{F['mjp_debt_2027']}}},{F['mjp_debt_2027']},planned,,MASSIVE debt ramp FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Schelle>AGB>debt_mjp,tick1110; new 1.516m 2026 + 4.016m 2027",
        f"comm_schagb_pnl_flip_2025,Schelle AGB P&L flip +0.085m 2025,{ENT},AGB operations,BBC JR2025,,2025,2025,{F['pnl']},{{2025:{F['pnl']}}},0,active,,P&L FLIP FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Schelle>AGB>pnl,tick1110; was -0.021m",
        f"comm_schagb_invest_underspend_2025,Schelle AGB invest 0.053 vs MJP 0.206 UNDERSPEND 2025,{ENT},Capital program,BBC JR2025,,2025,2025,{F['invest_uit']},{{2025:{F['invest_uit']}}},0,active,,UNDERSPEND FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Schelle>AGB>invest,tick1110",
        f"comm_schagb_cash_low_2025,Schelle AGB cash 0.051m CRITICAL LOW 2025,{ENT},treasury,BBC JR2025,,2025,2025,{F['cash']},{{2025:{F['cash']}}},0,active,,Cash LOW FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Schelle>AGB>cash,tick1110",
        f"comm_schagb_omzet_drop_2025,Schelle AGB omzet 0.708m DROP -15.7pct 2025,{ENT},sport/leisure ops,BBC JR2025,,2025,2025,{F['omzet']},{{2025:{F['omzet']}}},0,active,,Omzet DROP FOI,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Schelle>AGB>omzet,tick1110",
    ]
    append_csv(DATA / "commitments.csv", comm)

    # --- leaderboard ---
    under = F["invest_mjp"] - F["invest_uit"]
    ramp = F["mjp_debt_2027"] - F["fin_debt"]
    lb_note = "tick1110; primary Schelle AGB Fluctus JR2025; Entity II dual residual after Zele; not TE-additive"

    def lb(iid, name, annual, abs_s, cost_s, diff_s, pri, cut):
        return (
            f"{iid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>Schelle_AGB_L5,"
            f"{annual},{annual},JR2025 AGB dual residual map VL,strong,{SRC},"
            f"Schelle residents,Local AGB dual residual map VL JR2025,"
            f"JR2025 BBC AGB Fluctus Schelle realized figures,"
            f"{abs_s},{cost_s},{diff_s},{pri},{cut},active,,{lb_note}"
        )

    lbs = [
        lb("lb_schagb_mjp_debt_ramp_5_84m_2027", "Schelle AGB MJP fin debt ramp to 5.84m YE2027 MASSIVE FOI residual",
           ramp, 9.0, 5.5, 3.5, 7.0, "Debt ramp FOI project/lender"),
        lb("lb_schagb_prijssub_0_57m_2025", "Schelle AGB prijssubsidie gemeente 0.57m FOI residual",
           F["prijssub"], 8.0, 3.5, 3.0, 5.85, "Publish beheersovereenkomst performance"),
        lb("lb_schagb_pnl_flip_0_085m_2025", "Schelle AGB P&L flip +0.085m FOI residual",
           F["pnl"], 7.5, 3.0, 3.0, 5.35, "Keep FLIP path public"),
        lb("lb_schagb_invest_underspend_2025", "Schelle AGB invest 0.053 vs MJP 0.206 UNDERSPEND FOI residual",
           under, 7.5, 3.0, 3.5, 5.25, "Invest path FOI"),
        lb("lb_schagb_cash_0_051m_2025", "Schelle AGB cash 0.051m CRITICAL LOW FOI residual",
           F["cash"], 8.5, 2.5, 3.0, 5.5, "Treasury plan FOI"),
        lb("lb_schagb_omzet_drop_2025", "Schelle AGB omzet 0.708m DROP -15.7pct FOI residual",
           F["omzet"], 7.0, 3.5, 3.0, 5.3, "Volume/pricing FOI"),
        lb("lb_schagb_fin_debt_0_53m_2025", "Schelle AGB fin debt 0.53m FOI residual",
           F["fin_debt"], 5.5, 3.5, 3.5, 4.7, "Debt stock FOI"),
        lb("lb_schagb_afm_0_091m_2025", "Schelle AGB AFM +0.091m FOI residual",
           F["afm"], 5.0, 2.5, 3.0, 4.15, "Keep AFM path"),
        lb("lb_schagb_personnel_drop_2025", "Schelle AGB personnel drop 0.513 to 0.374m FOI residual",
           F["personnel_was"] - F["personnel"], 7.0, 3.0, 3.5, 5.15, "FTE path FOI"),
    ]
    append_csv(DATA / "leaderboard.csv", lbs)

    # --- sources ---
    src_row = (
        f"{SRC},AGB Fluctus Schelle BBC Jaarrekening 2025,{URL},"
        f"AGB Fluctus Schelle / Gemeente Schelle,2026-08-11,primary_pdf,"
        f"tick1110; 144p text; KBO 0879.775.746; Fabiolalaan 55 2627 Schelle; "
        f"AD Leen Wyn FD Nicole Rypens; GR 18.06.2026 pub 01.07.2026; "
        f"assets 1.208m equity 0.624m fin debt 0.531m DECLINE cash 0.051m CRITICAL "
        f"AFM +0.091m BBR 0.174m budget +0.088m P&L +0.085m FLIP prijssub 0.566m "
        f"invest 0.053 UNDERSPEND vs MJP 0.206; MJP debt ramp YE2027 5.844m "
        f"(new 1.516m 2026 + 4.016m 2027); page {PAGE}"
    )
    append_csv(DATA / "sources.csv", [src_row])

    # --- entities ---
    ent_agb = (
        f"{ENT},AGB Fluctus Schelle,Régie communale autonome Fluctus Schelle,"
        f"Autonomous municipal company Fluctus Schelle,"
        f"municipal_agency,{CITY},nl,{PAGE},info@schelle.be,"
        f"Fabiolalaan 55 2627 Schelle,"
        f"JR2025 Entity II dual residual tick1110; KBO 0879.775.746; "
        f"assets 1.208m fin debt 0.531m cash 0.051m CRITICAL AFM +0.091m "
        f"P&L FLIP +0.085m prijssub 0.566m MJP debt ramp YE2027 5.844m; "
        f"AD Leen Wyn FD Nicole Rypens"
    )
    ent_city = (
        f"{CITY},Gemeente Schelle,Commune de Schelle,Municipality of Schelle,"
        f"municipality,vlaanderen_gov,nl,https://www.schelle.be,info@schelle.be,"
        f"Fabiolalaan 55 2627 Schelle,"
        f"tick1110 residual: GE+OCMW JR2025 not yet public (JR2024 only on portal); "
        f"AGB Fluctus JR2025 public; FOI gap_sch_agb_debt_ramp_prijssub_geocmw_l5"
    )
    append_csv(DATA / "entities.csv", [ent_agb, ent_city])

    # --- FOI ---
    foi_row = (
        f"{GAP},Vlaanderen>Gemeenten>Schelle>agb_debt_ramp_prijssub_geocmw_L5,{CITY},"
        f"\"AGB Fluctus MJP fin debt ramp YE2026 1.911m (new 1.516m) to YE2027 5.844m "
        f"(new 4.016m) project/lender/rate; prijssubsidie gemeente 0.566m beheersovereenkomst "
        f"performance; cash 0.051m CRITICAL treasury plan; omzet DROP 0.840to0.708m; "
        f"personnel DROP 0.513to0.374m FTE; invest underspend 0.053 vs MJP 0.206; "
        f"FULL BBC JR2025 Gemeente+OCMW Schelle (not yet public — only JR2024 on portal)\","
        f"\"Small Antwerp municipality AGB with healthy 2025 AFM/P&L flip but MASSIVE planned "
        f"debt 11x ramp by 2027 under city prijssubsidie; GE+OCMW JR2025 opacity\","
        f"9,Gemeente Schelle,info@schelle.be,Fabiolalaan 55 2627 Schelle,"
        f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-11,,,,,"
        f"comm_schagb_mjp_debt_ramp_2027,lb_schagb_mjp_debt_ramp_5_84m_2027,"
        f"{UTC},{UTC},tick1110; ready not sent; do not send without human OK"
    )
    append_csv(DATA / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = f"""# FOI draft — {GAP}

**Status:** ready (NOT sent)  
**Gap ID:** {GAP}  
**Tick:** {TICK}  

## Recipient

- Gemeente Schelle openbaarheid / financieel directeur  
- E-mail: info@schelle.be  
- Adres: Fabiolalaan 55, 2627 Schelle  

## Subject

Openbaarheid — AGB Fluctus JR2025 schuld-ramp + prijssubsidie + JR2025 Gemeente/OCMW

## Body (NL)

```text
[Naam]
[Adres]
[E-mail]
[Datum]

Aan: Gemeente Schelle
t.a.v. de financieel directeur / dienst openbaarheid

Betreft: Verzoek openbaarheid — AGB Fluctus jaarrekening 2025 en
jaarrekening 2025 Gemeente en OCMW Schelle

Geachte,

Op grond van de regels inzake openbaarheid van bestuur vraag ik de volgende
documenten en toelichtingen.

### 1. Reeds openbaar (BBC JR2025 AGB Fluctus; schelle.be)

- AGB activa **EUR1,208m**; nettoactief **EUR0,624m**; fin. schuld **EUR0,531m**
  (LT 0,406 / ST 0,125; was 0,607m); nieuwe leningen **EUR0,053m**; cash
  **EUR0,051m CRITICAL LOW**; AFM **+EUR0,091m** (gecorr **+EUR0,172m**);
  BBR **EUR0,174m**; budget **+EUR0,088m**; P&L **+EUR0,085m FLIP** (was
  −EUR0,021m); prijssubsidie gemeente **EUR0,566m**; omzet **EUR0,708m DROP
  −15,7%**; personeel **EUR0,374m DROP** (was 0,513m); invest **EUR0,053m** vs
  MJP **EUR0,206m UNDERSPEND**.
- **MJP T4 schuld-ramp:** YE2026 fin. schuld **EUR1,911m** (nieuwe leningen
  **EUR1,516m**); YE2027 **EUR5,844m** (nieuwe leningen **EUR4,016m**).

### 2. Gevraagde stukken / toelichtingen

1. **MJP schuld-ramp 0,531 → 5,844m (2025–2027):** projectenlijst, kredietgevers,
   rente, aflossingsplan; aansluiting met gemeentelijke borgstellingen.
2. **Prijssubsidie gemeente EUR0,566m:** beheersovereenkomst 2025, KPI’s,
   meerjarentraject 2026–2031.
3. **Cash EUR0,051m CRITICAL:** liquiditeitsplan en relatie tot prijssubsidie.
4. **Omzet DROP −15,7%** en **personeel DROP 0,513 → 0,374m:** volume, tarieven,
   FTE-pad (sport/vrije tijd).
5. **Invest underspend** 0,053 vs MJP 0,206m: uitgestelde projecten 2026–2027.
6. **Volledige BBC-jaarrekening 2025 Gemeente + OCMW Schelle** (op de
   gemeentelijke portal stond bij onderzoek enkel JR2024 GE+OCMW; AGB 2025 wel
   openbaar): PDF-publicatie of digitaal afschrift.

Gelieve te antwoorden binnen de wettelijke termijn. Digitaal leveren (PDF) heeft
de voorkeur.

Met vriendelijke groeten,

[Naam]
[Contact]
```

## Notes

- Primary source: BBC JR2025 AGB Fluctus Schelle (144p; schelle.be; GR 18.06.2026).  
- GE+OCMW Schelle JR2025 not found public this tick (JR2024 only).  
- **Do not send** without human OK.  
- Tick 1110 dual residual after Zele; progress@1110 decade.
"""
    (FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

    # --- research queue: close rq_1110, spawn rq_1111 ---
    rq_path = DATA / "research_queue.csv"
    lines = rq_path.read_text(encoding="utf-8").splitlines()
    out = []
    found = False
    for line in lines:
        if line.startswith("rq_1110,"):
            found = True
            out.append(
                "rq_1110,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
                "PROGRESS@1110 decade + Schelle AGB Fluctus JR2025 Entity II dual residual,"
                f"{GAP},2026-08-11T20:00:00Z,{UTC},"
                "tick1110 progress decade + Schelle AGB assets 1.208m fin debt 0.531m cash 0.051m CRITICAL "
                "AFM +0.091m P&L FLIP +0.085m prijssub 0.566m MJP debt ramp YE2027 5.844m; FOI ready"
            )
        else:
            out.append(line)
    if not found:
        out.append(
            "rq_1110,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
            f"PROGRESS@1110 + Schelle AGB,{GAP},2026-08-11T20:00:00Z,{UTC},tick1110"
        )
    out.append(
        "rq_1111,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
        "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen login-blocked / Vorselaar docs-only full JR / "
        "Kalmthout / Bornem JR2024-only / Schelle GE+OCMW JR2025 if published / other); prefer FOI-adjacent L5; skip rq_116,"
        f",2026-08-11T20:30:00Z,{UTC},"
        "spawned tick1110 after Schelle AGB dual + progress@1110; next residual dual L5"
    )
    rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    # --- loop_state ---
    state = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{UTC},rq_1110,1110,no,"
        "tick1110 PROGRESS@1110 decade + Schelle AGB Fluctus JR2025 Entity II dual residual; "
        "FOI gap_sch_agb_debt_ramp_prijssub_geocmw_l5 prio9 ready; assets 1.208m equity 0.624m "
        "fin debt 0.531m cash 0.051m CRITICAL AFM +0.091m P&L FLIP +0.085m prijssub 0.566m "
        "MJP debt ramp YE2027 5.844m (new 1.516m 2026 + 4.016m 2027); GE+OCMW JR2025 not public; "
        "next residual dual L5 rq_1111; progress@1120 in 10; rq_116 deferred\n"
    )
    (DATA / "loop_state.csv").write_text(state, encoding="utf-8")

    # --- progress@1110 ---
    progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## How to read the % figures

| Layer | Meaning | “End stop of money”? |
|-------|---------|----------------------|
| **A. L0 total** | Official GG TE known | No — single top line |
| **B. L1 subsector** | TE split federal / SS / state / local | No — still aggregates |
| **C. L2 entity totals** | Named institutions with primary budget totals (De Lijn, FOREM, ORES, …) | **Partial** — who holds the money |
| **D. L5 end-receivers** | Named third party / project / ASBL / firm with € | **Yes** — where possible |
| **E. FOI residual** | Known gap, draft ready for human send | Tracked, not yet answered |

**Honest claim:** A+B are essentially complete. C is large but incomplete. **D is still a small share of €348 bn** — that is structural (payroll, pensions, debt interest, formula grants are not “projects”).

---

## Snapshot at **tick 1110** (2026-08-11)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1101-1109 + Entity II 1110: Heers / Nieuwerkerken / Herk-de-Stad / Wellen / Riemst **EUR128.1m** / Kaprijke **EUR51.2m** / Keerbergen **EUR75.4m** / Halen **EUR64.1m** / **Zele EUR192.4m** · **Schelle AGB Fluctus EUR1.2m** Entity II · prior 1091-1100 stack retained |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1101-1110 is VL residual dual L5 (not near-complete of 348bn):** personnel Zele **EUR25.3m** / Riemst **EUR14.2m** / Keerbergen **EUR13.8m** · FOI-adjacent: **FVA/herwaard JUMP cluster** (Halen FVA IGS **EUR20.9m** / herwaard **EUR10.7m**; Riemst FVA **EUR36.4m** / herwaard **EUR17.0m**; Wellen FVA **EUR10.8m**) · **new loans MASSIVE** (Zele **EUR5.42m** / Keerbergen **EUR5.46m** / Riemst **EUR3.25m**) · **pension JUMP** Zele **EUR19.7m** / Keerbergen **EUR7.7m** · **invest extremes** Halen underspend **1.42 vs MJP 8.92** / Zele OVER **10.33 vs 6.40** · **OCMW cover** FULL Zele **EUR2.77m** / Kaprijke **EUR1.04m** vs ZERO Wellen · **Entity II Schelle AGB** P&L FLIP + cash CRITICAL + **MJP debt ramp YE2027 EUR5.84m** under prijssub **EUR0.57m** |
| **E. FOI-ready gaps** | **~757** drafts ready | Human send only; answered **~9**; partial **~27**; total FOI rows **~799** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** (KUL **EUR3.4bn** / Brugge **EUR1.46bn** / **Zele EUR192m** / Riemst **EUR128m** / Keerbergen **EUR75m** / Halen **EUR64m** / Kaprijke **EUR51m** / prior dual stack retained not full TE) · **AGB dual AFM near-zero/NEG + Schelle AGB MJP debt ramp EUR5.84m** · **LUWA PPP EUR590m** · **VitaS/Peer contingent borg ~EUR43m** · private gambling **EUR31.5bn** market · Moody/S&P ratings (not euros).

### Inventory (tick 1110)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~29185 |
| commitments.csv | ~3654 |
| leaderboard.csv | ~5628 |
| entities.csv | ~828 |
| sources.csv | ~2020 |
| FOI ready | ~757 |
| FOI answered | ~9 |
| FOI partial | ~27 |
| FOI total rows | ~799 |
| research_queue open | rq_116 deferred + rq_1111 hole-fill after progress |

### What improved since tick 1100

- **VL residual dual JR2025 (tick1101-1109):** Heers / Nieuwerkerken / Herk-de-Stad / Wellen / Riemst / Kaprijke / Keerbergen / Halen / **Zele EUR192.4m**.
- **Entity II (tick1110):** **Schelle AGB Fluctus** — healthy 2025 AFM/P&L FLIP but **cash CRITICAL EUR0.05m**, city **prijssubsidie EUR0.57m**, and **MJP debt ramp to EUR5.84m YE2027** (11× stock). GE+OCMW Schelle JR2025 still not public (JR2024 only).
- **Dual map:** Fluvius-class FVA/herwaard continues (Halen/Riemst/Wellen) · new-loan cluster (Zele/Keerbergen/Riemst) · invest OVER (Zele) vs MASSIVE UNDERSPEND (Halen) · OCMW FULL vs ZERO cover split · Kaprijke WZC/uitzend FOI · AGB dual AFM path (Zele AGB gecorr NEG; Schelle AGB P&L FLIP + debt ramp).
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---

## Snapshot at **tick 1100** (2026-08-11)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1091-1099: Hamont-Achel **EUR126.0m** / Hechtel-Eksel **EUR71.8m** / Bree **EUR168.5m** / Pelt **EUR305.3m** / Lummen **EUR147.3m** / Tessenderlo-Ham **EUR312.8m** (first fusion) / Alken **EUR61.6m** / Dilsen-Stokkem **EUR191.0m** / **Peer EUR146.2m** · prior 1081-1090 stack retained |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1091-1099 is VL residual dual L5 (not near-complete of 348bn):** personnel Bree **EUR14.01m** / Pelt path / Tessenderlo-Ham **EUR31.92m** · FOI-adjacent: **Fluvius-class FVA/herwaard JUMP cluster** (Hamont-Achel herwaard **EUR17.1m** / Bree **EUR23.5m** / Pelt **EUR36.4m** / Lummen **EUR25.8m** / Tessenderlo-Ham **EUR42.1m** / Alken **EUR12.8m** / Dilsen **EUR25.1m**) vs **Peer FVA STABLE** (no reval) · **Pelt fin debt JUMP EUR38.0m** / cash loan-driven **EUR18.8m** / OCMW equity **-EUR23.5m ZERO cover** · **Dilsen OCMW equity -EUR21.0m ZERO cover** · **Tessenderlo-Ham cash EUR43.8m MASSIVE + pension EUR16.8m** · **Peer VitaS EUR1.48m JUMP + borg ~EUR42.9m contingent** · invest underspend extremes (Hamont-Achel 5.0 vs MJP 26.8 / Peer 6.4 vs 20.0) · ZERO-cover cluster expands (Pelt / Lummen / Dilsen) vs FULL (Hamont-Achel / Hechtel-Eksel / Bree **EUR3.3m** / Alken **EUR2.05m**) |
| **E. FOI-ready gaps** | **~747** drafts ready | Human send only; answered **~9**; partial **~27**; total FOI rows **~789** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** (KUL **EUR3.4bn** / Brugge **EUR1.46bn** / **Tessenderlo-Ham EUR313m** / **Pelt EUR305m** / Dilsen **EUR191m** / Bree **EUR168m** / Peer **EUR146m** / prior dual stack retained not full TE) · **AGB dual AFM near-zero/NEG** · **LUWA PPP EUR590m** · **VitaS/Peer contingent borg ~EUR43m** · private gambling **EUR31.5bn** market · Moody/S&P ratings (not euros).

### Inventory (tick 1100)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~28742 |
| commitments.csv | ~3583 |
| leaderboard.csv | ~5536 |
| entities.csv | ~817 |
| sources.csv | ~2010 |
| FOI ready | ~747 |
| FOI answered | ~9 |
| FOI partial | ~27 |
| FOI total rows | ~789 |
| research_queue open | rq_116 deferred + rq_1101 hole-fill after progress |

### What improved since tick 1090

- **VL residual dual JR2025 (tick1091-1099):** Hamont-Achel / Hechtel-Eksel / Bree / Pelt / Lummen / **Tessenderlo-Ham first fusion EUR312.8m** / Alken / Dilsen-Stokkem / **Peer EUR146.2m**.
- **Dual map:** **Fluvius FVA/herwaard JUMP wave** across most Limburg duals (Pelt/Lummen/Dilsen/Bree/Alken/Tessenderlo-Ham/Hamont-Achel) vs **Peer stable FVA** · **Pelt + Dilsen deep OCMW equity holes with ZERO cover** (−23.5m / −21.0m) vs FULL cover (Bree **EUR3.3m** / Alken **EUR2.05m** / Hamont / Hechtel) · **Tessenderlo-Ham** fusion cash/pension/FVA extremes · **Peer VitaS loss cover JUMP + multi-bn-class contingent borg** · invest underspend still systemic · Pelt fin-debt JUMP outlier.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---

## Snapshot at **tick 1090** (2026-08-11)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1081-1089: **Herent EUR161.8m** / Zoutleeuw **EUR57.0m** / Linter **EUR47.4m** / Bertem **EUR78.8m** / Kortenberg **EUR139.9m** / Glabbeek **EUR51.6m** / Hoegaarden **EUR60.7m** / Geetbets **EUR46.1m** / **Torhout EUR152.1m** · prior 1071-1080 stack retained |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1081-1089 is VL residual dual L5 (not near-complete of 348bn):** personnel Torhout **EUR30.43m** / Herent path / Kortenberg **EUR20.59m** · FOI-adjacent: **Zoutleeuw AFM −EUR0.85m NEG / BBR −EUR4.37m NEG EXTREME** / ST treasury **EUR5.70m** / cash **EUR0.35m critical** · **Herent cash EUR70.05m VERY HIGH** / AFM **+EUR10.34m** / pension JUMP **EUR11.27m** / BBR **EUR69.6m EXTREME** · **Kortenberg cash MASSIVE DROP EUR17.35m (was 24.81)** / budget **−EUR5.57m** / pension JUMP **+EUR2.83m** / OCMW **0** · **Bertem pension JUMP +EUR1.65m** / cash LOW **EUR1.89m** / OCMW **0** · **Glabbeek ST debt balloon EUR2.82m** / Fluvius herwaard **EUR5.64m** · **Hoegaarden balance CLEAR** (assets 79→61m) / andere opbr JUMP / P&L FLIP · **Geetbets FVA IGS 10.48m JUMP / herwaard 7.08m** · **Torhout pension JUMP EUR13.49m** / andere FVA **EUR23.73m opaque** / cash DROP / budget **−EUR1.58m** · ZERO-cover cluster expands (Zoutleeuw / Linter / Bertem / Kortenberg / Glabbeek / Hoegaarden) vs FULL-ish (Herent path / Torhout **EUR1.50m** / Geetbets **EUR0.20m** principle) |
| **E. FOI-ready gaps** | **~738** drafts ready | Human send only; answered **~9**; partial **~27**; total FOI rows **~780** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** (KUL **EUR3.4bn** / Brugge **EUR1.46bn** / **Herent EUR162m** / **Torhout EUR152m** / Kortenberg **EUR140m** / prior dual stack retained not full TE) · **AGB dual AFM near-zero/NEG** · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market · Moody/S&P ratings (not euros).

### Inventory (tick 1090)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~28262 |
| commitments.csv | ~3520 |
| leaderboard.csv | ~5461 |
| entities.csv | ~808 |
| sources.csv | ~2001 |
| FOI ready | ~738 |
| FOI answered | ~9 |
| FOI partial | ~27 |
| FOI total rows | ~780 |
| research_queue open | rq_116 deferred + rq_1091 hole-fill after progress |

### What improved since tick 1080

- **VL residual dual JR2025 (tick1081-1089):** Herent / Zoutleeuw / Linter / Bertem / Kortenberg / Glabbeek / Hoegaarden / Geetbets / **Torhout EUR152.1m**.
- **Dual map:** **Zoutleeuw** as AFM/BBR NEG EXTREME + ST-treasury balloon vs **Herent** cash/AFM/BBR VERY HIGH surplus · cash extremes (Herent **EUR70m** vs Zoutleeuw **EUR0.35m** / Kortenberg DROP **−EUR7.5m** / Torhout DROP) · pension JUMP cluster (Herent / Bertem / Kortenberg / Torhout) · FVA reval path (Zoutleeuw / Geetbets / Glabbeek Fluvius) · Hoegaarden one-off balance CLEAR + P&L FLIP · ZERO OCMW-cover still dominant (6/9 explicit zero) vs Torhout FULL **EUR1.50m** / Geetbets principle **EUR0.20m**.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.
"""
    (DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

    # --- waste top10 ---
    waste = """# DOGE waste ranking — current top 10

**As-of:** tick **1110** (2026-08-11) · **~5628** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **WE consol €6.38bn** · **SOFICO €3.02bn** · **university/city balance sheets** (KUL **€3.4bn** / Brugge **€1.46bn** / **Zele €192m** / Riemst **€128m** / Keerbergen **€75m** / Halen **€64m** / dual stack retained) · **AGB dual AFM near-zero/NEG + Schelle AGB MJP debt ramp €5.84m** · **LUWA PPP €590m** · **Peer VitaS borg ~€43m contingent** · private gambling stakes **€31.5bn** market · city debt/MJP/loan/pension/OCMW stocks **Halen FVA IGS €20.9m + herwaard €10.7m + invest underspend 1.42 vs MJP 8.92** / **Riemst FVA €36.4m + herwaard €17.0m + new loans €3.25m** / **Zele pension €19.7m + new loans €5.42m + invest OVER** / **Keerbergen new loans €5.46m + invest-subs €3.15m** / **Wellen budget NEG + cash DROP + OCMW ZERO** / **Schelle AGB cash CRITICAL €0.05m + prijssub €0.57m + MJP debt YE2027 €5.84m**.

**Change vs tick 1100:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). **Major NEW residual 1101–1110 (off pure top10 / dual):** Limburg/Oost-Vl dual stack (Heers→Zele) with **FVA/herwaard JUMP** (Halen/Riemst/Wellen) · **new-loan cluster** (Zele/Keerbergen/Riemst) · **invest OVER vs UNDERSPEND extremes** · OCMW FULL/ZERO split · **Entity II Schelle AGB MJP debt ramp €5.84m** under city prijssubsidie. Gain is **local dual FVA/debt/OCMW/AGB residual** more than FFS reshuffle.

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| — | `lb_metro3_overrun_477pct` | **stock** | **9.05** | STOCK filtered |
| — | `lb_owv_sub_snowball_27bn_2083` | **stock-as-ann** | **8.55** | STOCK filtered eoy2083 |
| — | `lb_vl_gsc_pv_legacy_7_078bn` | **~708 m** class | **8.05** | GSC PV legacy oversubsidy |
| — | `lb_fed_consultancy_2_5bn_coa` | **~842 m/yr** | **8.00** | CoA 2.525bn/3y |
| — | `lb_schagb_mjp_debt_ramp_5_84m_2027` | **~5.3 m ramp** | **~7.0** | **NEW 1110** AGB MJP debt |
| — | `lb_hal_fva_igs_20_93m_2025` | **20.9 m stock** | **~7.3** | **1108** FVA MASSIVE |
| — | `lb_zel_pension` path | **19.7 m stock** | **~7.0** | **1109** pension JUMP |
| — | `lb_zou_bbr_neg_4_37m_2025` | **4.4 m NEG** | **~7.8** | **1082** BBR NEG EXTREME |
| — | `lb_peer_borg_vitas_42_94m_2025` | **42.9 m stock** | **~7.2** | **1099** VitaS borg contingent |
| — | `lb_dil_ocmw_equity_21_03m_2025` | **21.0 m stock** | **~7.2** | **1098** OCMW equity DEEP ZERO cover |

### High-absurdity shortlist (not pure annual cost rank)

| ID | Abs | Note |
|----|----:|------|
| `lb_metro3_overrun_477pct` | **9.5** | Metro3 cost +477pct |
| `lb_vl_wassalon_podcast` | **9.5** | VL gelijke kansen vodcast |
| `lb_isi_bank_inquiry_1_57pct_recovery` | **9.0** | Bank-inquiry recovery 1.57% |
| `lb_police_ipolice_ssg_eval` | **9.0** | i-Police SSG evaluation |
| `lb_vl_gip_monitor_fail_2_5bn` | **9.0** | GIP without VEK public report |
| `lb_oaa_consol_reporte_300_6m` | **9.0** | Reporté solde fiction |
| `lb_zou_bbr_neg_4_37m_2025` | **9.5** | **1082** BBR NEG EXTREME |
| `lb_schagb_mjp_debt_ramp_5_84m_2027` | **9.0** | **NEW 1110** AGB debt 11× by 2027 |
| `lb_schagb_cash_0_051m_2025` | **8.5** | **NEW 1110** cash CRITICAL |
| `lb_hal_fva_igs_20_93m_2025` | **9.0** | **1108** FVA IGS MASSIVE JUMP |
| `lb_hal_invest_underspend_2025` | **8.5** | **1108** invest 1.42 vs MJP 8.92 |
| `lb_zel_pension` / loans path | **8.5** | **1109** pension+loans JUMP |
"""
    (DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

    # --- loop_log append ---
    log_entry = f"""
### Tick 1110 - {UTC}

- Unit: **rq_1110** (**PROGRESS@1110 decade** + FOI-adjacent residual dual - **AGB Fluctus Schelle Jaarrekening 2025** Entity II + Zele dual residual)
- Progress@1110: refreshed `progress_every_10_ticks.md` + `doge_waste_top10_current.md` (layers A–E; inventory; residual 1101-1110 map). Pure annual waste top10 **stable** (GIP/fossil/cars/cheque/reporté).
- Found (strong primary BBC JR2025 AGB 144p text; schelle.be; GR 18.06.2026 pub 01.07.2026; KBO 0879.775.746; Fabiolalaan 55 2627; AD Leen Wyn FD Nicole Rypens; AGB only — GE+OCMW JR2025 **not public** this tick, JR2024 only on portal):
  - Assets **EUR1.208m** slight DROP (was **EUR1.249m**) / equity **EUR0.624m JUMP** (was **EUR0.544m**) / debt total **EUR0.583m DECLINE** / fin debt **EUR0.531m DECLINE FOI** (LT **EUR0.406m** / ST due **EUR0.125m**; was **EUR0.607m**)
  - New loans **EUR0.053m** / repayments **EUR0.130m**
  - Cash **EUR0.051m CRITICAL LOW FOI** (was **EUR0.052m**)
  - Exploitatie: ontvangsten **EUR0.884m** / uitgaven **EUR0.663m** / saldo **+EUR0.220m STRONG**
  - AFM **+EUR0.091m** (gecorr **+EUR0.172m VERY STRONG**; MJP AFM was ~**EUR0.0003m**) / BBR **EUR0.174m** / budget **+EUR0.088m POS** / P&L **+EUR0.085m FLIP FOI** (was **−EUR0.021m**)
  - Omzet **EUR0.708m DROP −15.7% FOI** (was **EUR0.840m**) / personeel **EUR0.374m DROP FOI** (was **EUR0.513m**)
  - **Prijssubsidie gemeente EUR0.566m FOI** / werkingssubsidies **EUR0.101m**
  - Invest **EUR0.053m** vs MJP **EUR0.206m UNDERSPEND FOI**
  - **MJP T4 debt ramp MASSIVE FOI:** YE2026 fin debt **EUR1.911m** (new **EUR1.516m**) → YE2027 **EUR5.844m** (new **EUR4.016m**) ≈ **11×** 2025 stock
- Dual: Zele pension/loans/OCMW FULL/AGB JUMP (tick1109) - not TE-additive
- Note: Oosterzele / Nijlen login-blocked / Vorselaar docs-only (toelagen **EUR2.30m** 2025 partial; no full BBC J2/J4 public) / Kalmthout / Bornem JR2024-only / Schelle GE+OCMW JR2025 if published residual next; progress@1120 in 10
- Wrote: budgets +27 (bud_schagb_*); commitments +7; leaderboard +9; sources +1; entities agb_schelle_fluctus + city_schelle; FOI **gap_sch_agb_debt_ramp_prijssub_geocmw_l5** prio9 ready + draft; progress@1110 + waste top10; PDF primary (not committed 4.4MB); rq_1110=done; spawn **rq_1111**; ticks=1110
- FOI: ready only - **do not send**
- Next: prio5 **rq_1111** residual dual L5; deferred **rq_116**; progress@1120 in 10
"""
    log_text = LOG.read_text(encoding="utf-8")
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding="utf-8")

    print("tick1110 write OK")
    print("budgets", len(bud), "commitments", len(comm), "lbs", len(lbs))
    print("gap", GAP)
    print("next rq_1111")


if __name__ == "__main__":
    main()

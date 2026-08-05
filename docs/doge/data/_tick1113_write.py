# -*- coding: utf-8 -*-
"""tick 1113 — Gemeente+OCMW Langemark-Poelkapelle JR2025 dual residual"""
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

TICK = 1113
UTC = "2026-08-11T22:00:00Z"
SRC = "src_langemark_jr2025"
ENT = "city_langemark_poelkapelle"
GAP = "gap_lp_fva_herwaard_budget_ocmw_invest_l5"
URL = "https://www.langemark-poelkapelle.be/jaarrekening-2025"
# primary bundel: /file/download/9459dece-6874-4e76-8ac0-84e6d8773996/...

F = dict(
    assets=73204610,
    assets_was=65220556,
    equity=61810493,
    debt_total=11394118,
    fin_debt=5444011,
    fin_debt_lt=4359479,
    fin_debt_st=1084532,
    fin_debt_was=6313012,
    new_loans=178103,
    repayments=1047105,
    cash=10258209,
    cash_was=11080340,
    pension_lt=1221748,
    pension_was=813380,
    fva_igs=15998232,
    fva_igs_was=10249890,
    herwaard=8785663,
    herwaard_was=2495807,
    leasing_mva=828756,
    expl_ont=21918248,
    expl_uit=18471400,
    expl_saldo=3446847,
    afm=2715007,
    afm_gecorr=3257071,
    bbr=9198343,
    budget_result=-964675,
    cum_br=9198343,
    pnl=979112,
    fiscal=7193357,
    pb=3141493,
    op=3414955,
    personnel=12316479,
    toelagen=1304067,
    police=630535,
    fire=371774,
    igs_toel=53010,
    eredienst=77350,
    andere_toel=171399,
    hulp_ocmw=512959,
    invest_uit=5753538,
    invest_ont=2207740,
    invest_saldo=-3545799,
    invest_mjp=7643454,
    invest_subs=243131,
    ocmw_cover=2148891,
    ocmw_pnl=-1008398,
    ocmw_equity_cum=-214519,
    goederen=3920336,
    fin_exp=269224,
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

    b("bud_lp_assets_2025", F["assets"], "Assets YE2025 73.205m JUMP FOI (was 65.221m; FVA herwaard); tick1113")
    b("bud_lp_equity_2025", F["equity"], "Nettoactief YE2025 61.810m JUMP; tick1113")
    b("bud_lp_debt_total_2025", F["debt_total"], "Total schulden YE2025 11.394m stable; tick1113")
    b("bud_lp_fin_debt_2025", F["fin_debt"], "Fin debt YE2025 5.444m DECLINE (was 6.313m); tick1113")
    b("bud_lp_fin_debt_lt_2025", F["fin_debt_lt"], "Fin debt LT YE2025 4.359m; tick1113")
    b("bud_lp_fin_debt_st_2025", F["fin_debt_st"], "Fin debt ST due YE2025 1.085m; tick1113")
    b("bud_lp_new_loans_2025", F["new_loans"], "New loans 0.178m modest; tick1113")
    b("bud_lp_repayments_2025", F["repayments"], "Periodieke aflossingen 1.047m; tick1113")
    b("bud_lp_cash_2025", F["cash"], "Cash YE2025 10.258m DROP FOI (was 11.080m); tick1113")
    b("bud_lp_pension_lt_2025", F["pension_lt"], "Pension LT 1.222m JUMP FOI (was 0.813m); tick1113")
    b("bud_lp_fva_igs_2025", F["fva_igs"], "FVA IGS YE2025 15.998m MASSIVE JUMP FOI (was 10.250m Fluvius-class); tick1113")
    b("bud_lp_herwaard_2025", F["herwaard"], "Herwaarderingsreserves 8.786m MASSIVE JUMP FOI (was 2.496m); tick1113")
    b("bud_lp_leasing_mva_2025", F["leasing_mva"], "Leasing MVA YE2025 0.829m; tick1113")
    b("bud_lp_expl_ontvangsten_2025", F["expl_ont"], "Exploitatie ontvangsten 21.918m; tick1113")
    b("bud_lp_expl_uitgaven_2025", F["expl_uit"], "Exploitatie uitgaven 18.471m; tick1113")
    b("bud_lp_expl_saldo_2025", F["expl_saldo"], "Exploitatiesaldo +3.447m STRONG; tick1113")
    b("bud_lp_afm_2025", F["afm"], "AFM +2.715m STRONG; tick1113")
    b("bud_lp_afm_gecorr_2025", F["afm_gecorr"], "AFM gecorrigeerd +3.257m STRONG; tick1113")
    b("bud_lp_bbr_2025", F["bbr"], "BBR 9.198m HIGH; tick1113")
    b("bud_lp_budget_result_2025", F["budget_result"], "Budget -0.965m NEG FOI (better than MJP -4.469m); tick1113")
    b("bud_lp_pnl_2025", F["pnl"], "P&L +0.979m POS; tick1113")
    b("bud_lp_fiscal_2025", F["fiscal"], "Fiscale opbrengsten 7.193m; tick1113")
    b("bud_lp_pb_2025", F["pb"], "Personenbelasting 3.141m; tick1113")
    b("bud_lp_op_2025", F["op"], "Onroerende voorheffing opcentiemen 3.415m; tick1113")
    b("bud_lp_personnel_2025", F["personnel"], "Personeel 12.316m; tick1113")
    b("bud_lp_toelagen_2025", F["toelagen"], "Toegestane werkingssubsidies 1.304m FOI; tick1113")
    b("bud_lp_police_2025", F["police"], "Politiezone toelage 0.631m; tick1113")
    b("bud_lp_fire_2025", F["fire"], "HVZ toelage 0.372m; tick1113")
    b("bud_lp_hulp_ocmw_2025", F["hulp_ocmw"], "OCMW individuele hulp 0.513m; tick1113")
    b("bud_lp_invest_uitgaven_2025", F["invest_uit"], "Invest 5.754m vs MJP 7.643m UNDERSPEND FOI; tick1113")
    b("bud_lp_invest_mjp_2025", F["invest_mjp"], "MJP invest uitgaven 7.643m; tick1113")
    b("bud_lp_invest_subs_2025", F["invest_subs"], "Toegestane invest-subs 0.243m; tick1113")
    b("bud_lp_ocmw_cover_2025", F["ocmw_cover"], "OCMW cover 2.149m FULL FOI (OCMW P&L -1.008m); tick1113")
    b("bud_lp_ocmw_pnl_2025", F["ocmw_pnl"], "OCMW P&L -1.008m FOI; tick1113")
    b("bud_lp_ocmw_equity_cum_2025", F["ocmw_equity_cum"], "OCMW cum equity -0.215m FOI (was -1.355m improved); tick1113")
    b("bud_lp_goederen_2025", F["goederen"], "Goederen en diensten 3.920m; tick1113")
    b("bud_lp_fin_exp_2025", F["fin_exp"], "Financiele kosten 0.269m; tick1113")
    append_csv(DATA / "budgets.csv", bud)

    fva_jump = F["fva_igs"] - F["fva_igs_was"]
    herwaard_jump = F["herwaard"] - F["herwaard_was"]
    pen_jump = F["pension_lt"] - F["pension_was"]
    under = F["invest_mjp"] - F["invest_uit"]

    comm = [
        f"comm_lp_fin_debt_2025,Langemark-Poelkapelle fin debt YE2025 5.444m DECLINE,{ENT},creditors,BBC JR2025,,2025,2045,{F['fin_debt']},{{2025:{F['fin_debt']}}},{F['fin_debt']},active,,Capital finance DECLINE,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>debt,tick1113; LT 4.359 ST 1.085",
        f"comm_lp_fva_igs_2025,Langemark-Poelkapelle FVA IGS 15.998m MASSIVE JUMP 2025,{ENT},IGS/Fluvius-class,BBC JR2025,,2025,2025,{F['fva_igs']},{{2025:{F['fva_igs']}}},0,active,,FVA reval MASSIVE FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>fva,tick1113; was 10.250m",
        f"comm_lp_herwaard_2025,Langemark-Poelkapelle herwaard 8.786m MASSIVE JUMP 2025,{ENT},equity reval,BBC JR2025,,2025,2025,{F['herwaard']},{{2025:{F['herwaard']}}},0,active,,Herwaard MASSIVE FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>herwaard,tick1113; was 2.496m",
        f"comm_lp_ocmw_cover_2025,Langemark-Poelkapelle OCMW cover FULL 2.149m 2025,{ENT},OCMW Langemark-Poelkapelle,BBC JR2025,,2025,2025,{F['ocmw_cover']},{{2025:{F['ocmw_cover']}}},0,active,,Cover FULL FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>ocmw,tick1113",
        f"comm_lp_budget_neg_2025,Langemark-Poelkapelle budget -0.965m NEG 2025,{ENT},fiscal path,BBC JR2025,,2025,2025,{abs(F['budget_result'])},{{2025:{F['budget_result']}}},0,active,,Budget NEG FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>budget,tick1113; AFM +2.715m",
        f"comm_lp_invest_underspend_2025,Langemark-Poelkapelle invest 5.75 vs MJP 7.64 UNDERSPEND 2025,{ENT},Capital program,BBC JR2025,,2025,2025,{F['invest_uit']},{{2025:{F['invest_uit']}}},0,active,,UNDERSPEND FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>invest,tick1113",
        f"comm_lp_pension_jump_2025,Langemark-Poelkapelle pension LT jump 0.813 to 1.222m 2025,{ENT},pension provision,BBC JR2025,,2025,2025,{F['pension_lt']},{{2025:{F['pension_lt']}}},0,active,,Pension JUMP FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>pension,tick1113",
        f"comm_lp_toelagen_2025,Langemark-Poelkapelle toelagen 1.304m 2025,{ENT},PZ/HVZ/other,BBC JR2025 T2,,2025,2025,{F['toelagen']},{{2025:{F['toelagen']}}},0,active,,Named matrix FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>LangemarkPoelkapelle>toelagen,tick1113",
    ]
    append_csv(DATA / "commitments.csv", comm)

    lb_note = "tick1113; primary Langemark-Poelkapelle JR2025; dual residual after Knokke-Heist; not TE-additive"

    def lb(iid, name, annual, abs_s, cost_s, diff_s, pri, cut):
        return (
            f"{iid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>LangemarkPoelkapelle_L5,"
            f"{annual},{annual},JR2025 dual residual map VL,strong,{SRC},"
            f"Langemark-Poelkapelle residents,Local dual residual map VL JR2025,"
            f"JR2025 BBC Langemark-Poelkapelle GEOC realized figures,"
            f"{abs_s},{cost_s},{diff_s},{pri},{cut},active,,{lb_note}"
        )

    lbs = [
        lb("lb_lp_fva_igs_16_00m_2025", "Langemark-Poelkapelle FVA IGS 16.00m MASSIVE JUMP FOI residual",
           F["fva_igs"], 9.0, 5.5, 3.5, 7.0, "FVA Fluvius reval FOI"),
        lb("lb_lp_herwaard_8_79m_2025", "Langemark-Poelkapelle herwaard 8.79m MASSIVE JUMP FOI residual",
           F["herwaard"], 9.0, 5.5, 3.5, 7.0, "Herwaard FOI"),
        lb("lb_lp_ocmw_cover_2_15m_2025", "Langemark-Poelkapelle OCMW cover FULL 2.15m FOI residual",
           F["ocmw_cover"], 8.0, 4.5, 3.5, 6.35, "Cover policy FOI"),
        lb("lb_lp_budget_neg_0_96m_2025", "Langemark-Poelkapelle budget -0.96m NEG FOI residual",
           abs(F["budget_result"]), 8.0, 3.5, 3.5, 5.85, "Budget path FOI"),
        lb("lb_lp_invest_underspend_2025", "Langemark-Poelkapelle invest 5.75 vs MJP 7.64 UNDERSPEND FOI residual",
           under, 7.5, 4.0, 3.5, 5.75, "Invest path FOI"),
        lb("lb_lp_pension_jump_2025", "Langemark-Poelkapelle pension LT jump 0.81 to 1.22m FOI residual",
           pen_jump, 8.0, 3.0, 3.5, 5.65, "Pension path FOI"),
        lb("lb_lp_cash_drop_2025", "Langemark-Poelkapelle cash drop 11.08 to 10.26m FOI residual",
           F["cash_was"] - F["cash"], 7.0, 3.5, 3.5, 5.35, "Treasury FOI"),
        lb("lb_lp_afm_2_72m_2025", "Langemark-Poelkapelle AFM +2.72m FOI residual",
           F["afm"], 5.0, 4.5, 3.0, 4.95, "Keep AFM path"),
        lb("lb_lp_toelagen_1_30m_2025", "Langemark-Poelkapelle toelagen 1.30m FOI residual",
           F["toelagen"], 6.5, 4.0, 3.5, 5.4, "Named matrix FOI"),
        lb("lb_lp_fin_debt_5_44m_2025", "Langemark-Poelkapelle fin debt 5.44m FOI residual",
           F["fin_debt"], 5.0, 5.0, 3.5, 5.0, "Debt stock FOI"),
    ]
    append_csv(DATA / "leaderboard.csv", lbs)

    src_row = (
        f"{SRC},Gemeente+OCMW Langemark-Poelkapelle BBC Jaarrekening 2025,{URL},"
        f"Gemeente Langemark-Poelkapelle,2026-08-11,primary_pdf,"
        f"tick1113; 146p text bundel; KBO GE 0216.770.254 / OCMW 0216.770.353; "
        f"AD Jochen Vermote FD Mireille Cappelle; Kasteelstraat 1 8920; "
        f"assets 73.205m JUMP FVA IGS 15.998m MASSIVE herwaard 8.786m MASSIVE "
        f"fin debt 5.444m DECLINE cash 10.258m DROP AFM +2.715m BBR 9.198m "
        f"budget -0.965m NEG OCMW cover 2.149m FULL pension JUMP 1.222m; "
        f"primary PDF staged docs/doge/data/_tmp/langemark_jr2025_bundel.pdf"
    )
    append_csv(DATA / "sources.csv", [src_row])

    ent_row = (
        f"{ENT},Gemeente Langemark-Poelkapelle,Commune de Langemark-Poelkapelle,"
        f"Municipality of Langemark-Poelkapelle,"
        f"municipality,vlaanderen_gov,nl,https://www.langemark-poelkapelle.be,info@langemark-poelkapelle.be,"
        f"Kasteelstraat 1 8920 Langemark-Poelkapelle,"
        f"JR2025 dual residual tick1113; KBO 0216.770.254 / OCMW 0216.770.353; "
        f"assets 73.205m FVA IGS 15.998m MASSIVE herwaard 8.786m fin debt 5.444m "
        f"AFM +2.715m budget -0.965m OCMW cover 2.149m FULL; AD Jochen Vermote FD Mireille Cappelle"
    )
    append_csv(DATA / "entities.csv", [ent_row])

    foi_row = (
        f"{GAP},Vlaanderen>Gemeenten>LangemarkPoelkapelle>fva_herwaard_budget_ocmw_invest_L5,{ENT},"
        f"\"FVA IGS 15.998m MASSIVE JUMP (was 10.250m Fluvius-class reval); herwaarderingsreserves "
        f"8.786m MASSIVE JUMP (was 2.496m +6.384m toevoeging); budget -0.965m NEG under AFM +2.715m; "
        f"OCMW cover FULL 2.149m vs OCMW P&L -1.008m (equity improved -1.355to-0.215m); pension JUMP "
        f"0.813to1.222m actuarial; cash DROP 11.080to10.258m; invest underspend 5.754 vs MJP 7.643; "
        f"toelagen 1.304m named matrix\","
        f"\"West-Vl muni with Fluvius-class FVA/herwaard double and budget NEG despite strong AFM + "
        f"FULL OCMW cover FOI-adjacent dual residual\","
        f"9,Gemeente Langemark-Poelkapelle,info@langemark-poelkapelle.be,Kasteelstraat 1 8920 Langemark-Poelkapelle,"
        f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-11,,,,,"
        f"comm_lp_fva_igs_2025,lb_lp_fva_igs_16_00m_2025,"
        f"{UTC},{UTC},tick1113; ready not sent; do not send without human OK"
    )
    append_csv(DATA / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = f"""# FOI draft — {GAP}

**Status:** ready (NOT sent)  
**Gap ID:** {GAP}  
**Tick:** {TICK}  

## Recipient

- Gemeente Langemark-Poelkapelle openbaarheid / financieel directeur Mireille Cappelle  
- E-mail: info@langemark-poelkapelle.be  
- Adres: Kasteelstraat 1, 8920 Langemark-Poelkapelle  

## Subject

Openbaarheid — Jaarrekening 2025 Gemeente/OCMW Langemark-Poelkapelle: FVA/herwaard, budget, OCMW, investeringen

## Body (NL)

```text
[Naam]
[Adres]
[E-mail]
[Datum]

Aan: Gemeente Langemark-Poelkapelle
t.a.v. de financieel directeur

Betreft: Verzoek openbaarheid — jaarrekening 2025 Gemeente en OCMW
Langemark-Poelkapelle

Geachte,

Op grond van de regels inzake openbaarheid van bestuur vraag ik de volgende
documenten en toelichtingen.

### 1. Reeds openbaar (BBC JR2025; langemark-poelkapelle.be)

- Activa **EUR73,205m JUMP** (was 65,221m); nettoactief **EUR61,810m**; fin.
  schuld **EUR5,444m DECLINE** (LT 4,359 / ST 1,085); nieuwe leningen
  **EUR0,178m**; cash **EUR10,258m DROP** (was 11,080m); pensioen LT
  **EUR1,222m JUMP** (was 0,813m); FVA IGS **EUR15,998m MASSIVE JUMP** (was
  10,250m); herwaarderingsreserves **EUR8,786m MASSIVE JUMP** (was 2,496m;
  toevoeging **EUR6,384m**); AFM **+EUR2,715m**; BBR **EUR9,198m**; budget
  **−EUR0,965m NEG**; P&L **+EUR0,979m**; toelagen **EUR1,304m** (politie
  **EUR0,631m** / HVZ **EUR0,372m**); invest **EUR5,754m** vs MJP
  **EUR7,643m UNDERSPEND**; OCMW-tussenkomst **EUR2,149m FULL** (OCMW P&L
  **−EUR1,008m**; cum equity **−EUR0,215m** improved from −1,355m).

### 2. Gevraagde stukken / toelichtingen

1. **FVA IGS EUR15,998m JUMP:** deelnemingenmatrix (Fluvius/andere),
   herwaarderingsmethodiek en kasimpact vs pure reval.
2. **Herwaarderingsreserves EUR8,786m:** aansluiting met FVA-mutatie 2025
   (toevoeging EUR6,384m).
3. **Budget −EUR0,965m NEG** onder AFM +EUR2,715m: drivers en 2026-pad.
4. **OCMW cover FULL EUR2,149m** vs OCMW P&L −EUR1,008m: liquiditeitsbeleid
   2020–2026 (equity verbetering −1,355 → −0,215m).
5. **Pensioen LT JUMP** 0,813 → 1,222m: actuariële aannames.
6. **Invest underspend** 5,75 vs MJP 7,64m: projectenlijst en overdrachten 2026.
7. **Toelagen-matrix:** politie, HVZ, IGS, eredienst, andere ≥ EUR50k.

Gelieve te antwoorden binnen de wettelijke termijn. Digitaal leveren (PDF) heeft
de voorkeur.

Met vriendelijke groeten,

[Naam]
[Contact]
```

## Notes

- Primary source: BBC JR2025 Gemeente+OCMW Langemark-Poelkapelle (146p bundel; AD Vermote FD Cappelle).  
- **Do not send** without human OK.  
- Tick 1113 dual residual after Knokke-Heist (tick1112).
"""
    (FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

    rq_path = DATA / "research_queue.csv"
    lines = rq_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("rq_1113,"):
            out.append(
                "rq_1113,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
                "Langemark-Poelkapelle GE+OCMW JR2025 dual residual,"
                f"{GAP},2026-08-11T21:30:00Z,{UTC},"
                "tick1113 Langemark-Poelkapelle assets 73.205m FVA IGS 15.998m MASSIVE herwaard 8.786m "
                "fin debt 5.444m AFM +2.715m budget -0.965m NEG OCMW cover 2.149m FULL; FOI ready"
            )
        else:
            out.append(line)
    out.append(
        "rq_1114,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
        "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen login-blocked / Vorselaar docs-only / "
        "Kalmthout / Bornem JR2024-only / De Panne OCR / Schelle GE+OCMW if published / other); "
        "prefer FOI-adjacent L5; skip rq_116,"
        f",2026-08-11T22:00:00Z,{UTC},"
        "spawned tick1113 after Langemark-Poelkapelle dual residual; next residual dual L5; progress@1120 in 7"
    )
    rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    state = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{UTC},rq_1113,1113,no,"
        "tick1113 Langemark-Poelkapelle GE+OCMW JR2025 dual residual; FOI gap_lp_fva_herwaard_budget_ocmw_invest_l5 prio9 ready; "
        "assets 73.205m JUMP equity 61.810m fin debt 5.444m DECLINE cash 10.258m DROP FVA IGS 15.998m MASSIVE "
        "herwaard 8.786m MASSIVE AFM +2.715m BBR 9.198m budget -0.965m NEG P&L +0.979m OCMW cover 2.149m FULL "
        "pension JUMP 1.222m invest underspend 5.75 vs 7.64; next residual dual L5 rq_1114; progress@1120 in 7; rq_116 deferred\n"
    )
    (DATA / "loop_state.csv").write_text(state, encoding="utf-8")

    log_entry = f"""
### Tick 1113 - {UTC}

- Unit: **rq_1113** (FOI-adjacent residual dual - **Gemeente+OCMW Langemark-Poelkapelle Jaarrekening 2025** + Knokke-Heist dual residual)
- Found (strong primary BBC JR2025 146p text bundel; langemark-poelkapelle.be; KBO GE 0216.770.254 / OCMW 0216.770.353; Kasteelstraat 1 8920; AD Jochen Vermote FD Mireille Cappelle; GE+OCMW):
  - Assets **EUR73.205m JUMP FOI** (was **EUR65.221m**) / equity **EUR61.810m JUMP** / debt total **EUR11.394m** / fin debt **EUR5.444m DECLINE** (LT **EUR4.359m** / ST due **EUR1.085m**; was **EUR6.313m**)
  - New loans **EUR0.178m** / repayments **EUR1.047m**
  - Cash **EUR10.258m DROP FOI** (was **EUR11.080m**) / pension **EUR1.222m JUMP FOI** (was **EUR0.813m**; +**EUR0.408m**)
  - FVA IGS **EUR15.998m MASSIVE JUMP FOI** (was **EUR10.250m** Fluvius-class) / herwaard **EUR8.786m MASSIVE JUMP FOI** (was **EUR2.496m**; toevoeging **EUR6.384m**) / leasing MVA **EUR0.829m**
  - Exploitatie: ontvangsten **EUR21.918m** / uitgaven **EUR18.471m** / saldo **+EUR3.447m STRONG**
  - AFM **+EUR2.715m STRONG** (gecorr **+EUR3.257m**) / BBR **EUR9.198m HIGH** / budget **−EUR0.965m NEG FOI** (better than MJP **−EUR4.469m**) / P&L **+EUR0.979m POS**
  - Fiscal **EUR7.193m** / PB **EUR3.141m** / OP **EUR3.415m** / personnel **EUR12.316m**
  - Toelagen **EUR1.304m FOI** (police **EUR0.631m** / fire **EUR0.372m** / IGS **EUR0.053m** / eredienst **EUR0.077m** / andere **EUR0.171m**)
  - Invest **EUR5.754m** vs MJP **EUR7.643m UNDERSPEND FOI** / invest-subs **EUR0.243m**
  - OCMW cover **EUR2.149m FULL FOI** / OCMW P&L **−EUR1.008m** / OCMW cum equity **−EUR0.215m** (improved from **−EUR1.355m**) / OCMW hulp **EUR0.513m**
- Dual: Knokke-Heist loans/toelagen MASSIVE / AGSO NEG (tick1112) - not TE-additive
- Note: Oosterzele / Nijlen login-blocked / Vorselaar docs-only / Kalmthout / Bornem JR2024-only / De Panne OCR residual next; progress@1120 in 7
- Wrote: budgets +37 (bud_lp_*); commitments +8; leaderboard +10; sources +1; entity city_langemark_poelkapelle; FOI **gap_lp_fva_herwaard_budget_ocmw_invest_l5** prio9 ready + draft; PDF primary (not committed 4.2MB); rq_1113=done; spawn **rq_1114**; ticks=1113
- FOI: ready only - **do not send**
- Next: prio5 **rq_1114** residual dual L5; deferred **rq_116**; progress@1120 in 7
"""
    log_text = LOG.read_text(encoding="utf-8")
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding="utf-8")

    print("tick1113 write OK")
    print("budgets", len(bud), "commitments", len(comm), "lbs", len(lbs))
    print("gap", GAP)


if __name__ == "__main__":
    main()

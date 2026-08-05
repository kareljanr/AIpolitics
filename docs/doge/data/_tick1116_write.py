# -*- coding: utf-8 -*-
"""tick 1116 — WV Najaarszon Brakel (RVT) JR2025 Entity II dual residual"""
from pathlib import Path

DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
FOI_DRAFTS = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

TICK = 1116
UTC = "2026-08-11T23:30:00Z"
SRC = "src_brakel_najaarszon_jr2025"
ENT = "zorg_brakel_najaarszon"
CITY = "city_brakel"
GAP = "gap_brn_ocmw_litigation_subs_pension_l5"
URL = "https://www.brakel.be/wp-content/uploads/2026/07/Definitief_Jaarrekening_2025_Vereniging_Najaarszon.pdf"

F = dict(
    assets=5306429,
    assets_was=4590183,
    equity=920573,  # flat both years
    debt_total=4385856,
    fin_debt=162000,  # LT only; ST due 0
    fin_debt_lt=162000,
    fin_debt_st=0,
    new_loans=0,
    repayments=11250,
    cash=611281,
    cash_was=759625,
    pension_lt=1206000,
    pension_was=857349,
    receivables_kt=4355449,
    receivables_nruil=3559991,  # HIGH FOI (likely OCMW)
    expl_ont=6959388,
    expl_uit=6520527,
    expl_saldo=438862,
    afm=427612,
    afm_gecorr=425002,
    bbr=2240605,
    budget_result=328666,
    cum_br=2240605,
    invest_uit=98945,
    invest_mjp=100000,
    personnel=3990136,
    goederen=2519919,
    werkingsub=1397500,
    werkingsub_spec=1152514,
    werkingsub_alg=244987,
    omzet=5551823,
    ocmw_net_claim_interest=108586,  # FOI litigation residual as of 1 jun 2026
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

    b("bud_brn_assets_2025", F["assets"], "Assets YE2025 5.306m JUMP (was 4.590m); tick1116")
    b("bud_brn_equity_2025", F["equity"], "Nettoactief YE2025 0.921m FLAT FOI (same as 2024); tick1116")
    b("bud_brn_debt_total_2025", F["debt_total"], "Total schulden YE2025 4.386m JUMP; tick1116")
    b("bud_brn_fin_debt_2025", F["fin_debt"], "Fin debt YE2025 0.162m LOW FOI (huurwaarborg-class); tick1116")
    b("bud_brn_repayments_2025", F["repayments"], "Periodieke aflossingen 0.011m; tick1116")
    b("bud_brn_cash_2025", F["cash"], "Cash YE2025 0.611m DROP FOI (was 0.760m); tick1116")
    b("bud_brn_pension_lt_2025", F["pension_lt"], "Pension LT 1.206m JUMP FOI (was 0.857m); tick1116")
    b("bud_brn_receivables_kt_2025", F["receivables_kt"], "KT vorderingen 4.355m HIGH FOI (niet-ruil 3.560m); tick1116")
    b("bud_brn_expl_ontvangsten_2025", F["expl_ont"], "Exploitatie ontvangsten 6.959m; tick1116")
    b("bud_brn_expl_uitgaven_2025", F["expl_uit"], "Exploitatie uitgaven 6.521m; tick1116")
    b("bud_brn_expl_saldo_2025", F["expl_saldo"], "Exploitatiesaldo +0.439m STRONG; tick1116")
    b("bud_brn_afm_2025", F["afm"], "AFM +0.428m STRONG (MJP was +0.054m); tick1116")
    b("bud_brn_afm_gecorr_2025", F["afm_gecorr"], "AFM gecorrigeerd +0.425m; tick1116")
    b("bud_brn_bbr_2025", F["bbr"], "BBR 2.241m HIGH; tick1116")
    b("bud_brn_budget_result_2025", F["budget_result"], "Budget +0.329m POS (MJP was -0.046m); tick1116")
    b("bud_brn_personnel_2025", F["personnel"], "Personeel 3.990m; tick1116")
    b("bud_brn_goederen_2025", F["goederen"], "Goederen en diensten 2.520m; tick1116")
    b("bud_brn_omzet_2025", F["omzet"], "Omzet/werking 5.552m; tick1116")
    b("bud_brn_werkingssub_2025", F["werkingsub"], "Werkingssubsidies 1.398m FOI residual; tick1116")
    b("bud_brn_invest_uitgaven_2025", F["invest_uit"], "Invest 0.099m near MJP 0.100m; tick1116")
    b("bud_brn_ocmw_litigation_2025", F["ocmw_net_claim_interest"], "OCMW Brakel net claim ~0.109m FOI litigation residual (interest to 1 jun 2026); tick1116")
    append_csv(DATA / "budgets.csv", bud)

    pen_jump = F["pension_lt"] - F["pension_was"]
    comm = [
        f"comm_brn_werkingssub_2025,Brakel Najaarszon werkingssubsidies 1.398m 2025,{ENT},OCMW Brakel/other,BBC JR2025,,2025,2025,{F['werkingsub']},{{2025:{F['werkingsub']}}},0,active,,Subsidy matrix FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Brakel>Najaarszon>subs,tick1116; was 1.634m",
        f"comm_brn_pension_jump_2025,Brakel Najaarszon pension LT jump 0.857 to 1.206m 2025,{ENT},pension provision,BBC JR2025,,2025,2025,{F['pension_lt']},{{2025:{F['pension_lt']}}},0,active,,Pension JUMP FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Brakel>Najaarszon>pension,tick1116",
        f"comm_brn_ocmw_litigation_2025,Brakel Najaarszon OCMW litigation residual ~0.109m,{CITY},{ENT},court arrest FOI,,2025,2026,{F['ocmw_net_claim_interest']},{{2025:{F['ocmw_net_claim_interest']}}},0,active,,Litigation FOI residual HIGH,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Brakel>Najaarszon>litigation,tick1116; net OCMW pay 108586+interest path",
        f"comm_brn_receivables_2025,Brakel Najaarszon KT vorderingen 4.355m HIGH,{ENT},debtors,BBC JR2025,,2025,2025,{F['receivables_kt']},{{2025:{F['receivables_kt']}}},0,active,,Receivables HIGH FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Brakel>Najaarszon>receivables,tick1116; niet-ruil 3.560m",
        f"comm_brn_equity_flat_2025,Brakel Najaarszon equity flat 0.921m 2024-2025,{ENT},equity,BBC JR2025,,2025,2025,{F['equity']},{{2025:{F['equity']}}},0,active,,Equity flat FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Brakel>Najaarszon>equity,tick1116",
        f"comm_brn_afm_2025,Brakel Najaarszon AFM +0.428m 2025,{ENT},fiscal sustainability,BBC JR2025,,2025,2025,{F['afm']},{{2025:{F['afm']}}},0,active,,AFM STRONG FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Brakel>Najaarszon>afm,tick1116",
        f"comm_brn_personnel_2025,Brakel Najaarszon personnel 3.990m 2025,{ENT},staff,BBC JR2025,,2025,2025,{F['personnel']},{{2025:{F['personnel']}}},0,active,,Personnel FOI residual,FOI residual,{SRC},strong,Vlaanderen>Gemeenten>Brakel>Najaarszon>personnel,tick1116",
    ]
    append_csv(DATA / "commitments.csv", comm)

    lb_note = "tick1116; primary WV Najaarszon Brakel JR2025; Entity II dual residual care home; not TE-additive"

    def lb(iid, name, annual, abs_s, cost_s, diff_s, pri, cut):
        return (
            f"{iid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>Brakel_Najaarszon_L5,"
            f"{annual},{annual},JR2025 Entity II dual residual map VL,strong,{SRC},"
            f"Brakel residents/residents RVT,Local care-home dual residual map VL JR2025,"
            f"JR2025 BBC WV Najaarszon Brakel realized figures,"
            f"{abs_s},{cost_s},{diff_s},{pri},{cut},active,,{lb_note}"
        )

    lbs = [
        lb("lb_brn_werkingssub_1_40m_2025", "Brakel Najaarszon werkingssubsidies 1.40m FOI residual",
           F["werkingsub"], 8.0, 4.0, 3.5, 6.05, "Named subsidy matrix FOI"),
        lb("lb_brn_ocmw_litigation_0_11m_2025", "Brakel Najaarszon OCMW litigation residual ~0.11m FOI residual",
           F["ocmw_net_claim_interest"], 9.5, 2.5, 4.0, 6.25, "Litigation settlement FOI"),
        lb("lb_brn_pension_jump_2025", "Brakel Najaarszon pension LT jump 0.86 to 1.21m FOI residual",
           pen_jump, 8.5, 3.5, 3.5, 6.1, "Pension path FOI"),
        lb("lb_brn_receivables_4_36m_2025", "Brakel Najaarszon KT vorderingen 4.36m HIGH FOI residual",
           F["receivables_kt"], 8.0, 5.0, 3.5, 6.5, "Counterparty matrix FOI"),
        lb("lb_brn_personnel_3_99m_2025", "Brakel Najaarszon personnel 3.99m FOI residual",
           F["personnel"], 5.5, 5.0, 3.5, 5.3, "FTE path FOI"),
        lb("lb_brn_afm_0_43m_2025", "Brakel Najaarszon AFM +0.43m FOI residual",
           F["afm"], 5.5, 3.0, 3.0, 4.55, "Keep AFM path"),
        lb("lb_brn_equity_flat_2025", "Brakel Najaarszon equity flat 0.92m FOI residual",
           F["equity"], 8.0, 3.0, 3.5, 5.65, "Equity path FOI"),
        lb("lb_brn_cash_drop_2025", "Brakel Najaarszon cash drop 0.76 to 0.61m FOI residual",
           F["cash_was"] - F["cash"], 7.0, 2.5, 3.5, 4.85, "Treasury FOI"),
        lb("lb_brn_bbr_2_24m_2025", "Brakel Najaarszon BBR 2.24m FOI residual",
           F["bbr"], 5.0, 4.5, 3.0, 4.95, "Keep BBR path"),
    ]
    append_csv(DATA / "leaderboard.csv", lbs)

    src_row = (
        f"{SRC},WV RVT Rusthuis Najaarszon Brakel BBC Jaarrekening 2025,{URL},"
        f"Welzijnsvereniging Najaarszon / OCMW Brakel,2026-08-11,primary_pdf,"
        f"tick1116; 103p text; KBO 0886.485.770; Kasteelstraat 50 9660 Brakel; "
        f"leden OCMW Brakel + vzw Sint-Jozef; Voorzitter Bruno Schollaert; "
        f"assets 5.306m cash 0.611m DROP receivables 4.355m HIGH fin debt 0.162m "
        f"pension JUMP 1.206m AFM +0.428m BBR 2.241m budget +0.329m werkingssub 1.398m "
        f"personnel 3.990m OCMW litigation residual ~0.109m; equity flat 0.921m"
    )
    append_csv(DATA / "sources.csv", [src_row])

    ent_zorg = (
        f"{ENT},WV RVT Rusthuis Najaarszon Brakel,Association de soins Najaarszon Brakel,"
        f"Care home association Najaarszon Brakel,"
        f"ocmw_association,{CITY},nl,https://www.brakel.be,info@brakel.be,"
        f"Kasteelstraat 50 9660 Brakel,"
        f"JR2025 Entity II dual residual tick1116; KBO 0886.485.770; assets 5.306m "
        f"receivables 4.355m HIGH pension JUMP 1.206m AFM +0.428m werkingssub 1.398m "
        f"OCMW litigation residual; members OCMW Brakel + vzw Sint-Jozef"
    )
    ent_city = (
        f"{CITY},Gemeente Brakel,Commune de Brakel,Municipality of Brakel,"
        f"municipality,vlaanderen_gov,nl,https://www.brakel.be,info@brakel.be,"
        f"Marktplein 1 9660 Brakel,"
        f"tick1116 residual: GE+OCMW JR2025 not found public this tick; "
        f"WV Najaarszon RVT JR2025 mined; FOI gap_brn_ocmw_litigation_subs_pension_l5"
    )
    append_csv(DATA / "entities.csv", [ent_zorg, ent_city])

    foi_row = (
        f"{GAP},Vlaanderen>Gemeenten>Brakel>najaarszon_ocmw_litigation_subs_pension_L5,{CITY},"
        f"\"OCMW Brakel vs Najaarszon litigation residual settlement (~0.109m net + interest path as of "
        f"1 jun 2026) full status; werkingssubsidies 1.398m named matrix (was 1.634m); pension JUMP "
        f"0.857to1.206m actuarial; KT vorderingen niet-ruil 3.560m counterparties (OCMW?); equity flat "
        f"0.921m despite budget +0.329m; cash DROP 0.760to0.611m; FULL BBC JR2025 Gemeente+OCMW Brakel "
        f"(not public this tick)\","
        f"\"Care-home Entity II dual with HIGH receivables + pension JUMP + multi-year OCMW litigation "
        f"opacity while AFM +0.43m; FOI-adjacent residual\","
        f"9,Gemeente / OCMW Brakel,info@brakel.be,Marktplein 1 9660 Brakel,"
        f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-11,,,,,"
        f"comm_brn_ocmw_litigation_2025,lb_brn_ocmw_litigation_0_11m_2025,"
        f"{UTC},{UTC},tick1116; ready not sent; do not send without human OK"
    )
    append_csv(DATA / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = f"""# FOI draft — {GAP}

**Status:** ready (NOT sent)  
**Gap ID:** {GAP}  
**Tick:** {TICK}  

## Recipient

- Gemeente / OCMW Brakel openbaarheid  
- E-mail: info@brakel.be  
- Adres: Marktplein 1, 9660 Brakel  

## Subject

Openbaarheid — WV Najaarszon JR2025 + OCMW-geschil + jaarrekening Gemeente/OCMW Brakel

## Body (NL)

```text
[Naam]
[Adres]
[E-mail]
[Datum]

Aan: Gemeente / OCMW Brakel
t.a.v. de financieel directeur / dienst openbaarheid

Betreft: Verzoek openbaarheid — jaarrekening 2025 WV Najaarszon en
Gemeente/OCMW Brakel

Geachte,

Op grond van de regels inzake openbaarheid van bestuur vraag ik de volgende
documenten en toelichtingen.

### 1. Reeds openbaar (BBC JR2025 WV Najaarszon; brakel.be)

- Activa **EUR5,306m**; nettoactief **EUR0,921m FLAT**; fin. schuld
  **EUR0,162m**; cash **EUR0,611m DROP** (was 0,760m); pensioen LT
  **EUR1,206m JUMP** (was 0,857m); KT-vorderingen **EUR4,355m** (niet-ruil
  **EUR3,560m**); AFM **+EUR0,428m**; BBR **EUR2,241m**; budget
  **+EUR0,329m**; werkingssubsidies **EUR1,398m** (was 1,634m); personeel
  **EUR3,990m**.
- **Geschil OCMW ↔ Najaarszon:** JR2025 toelichting raamt nettobetaling OCMW
  aan Najaarszon ca. **EUR108.587** (incl. interest tot 1 juni 2026); OCMW-
  vertegenwoordigers betwisten cijfers.

### 2. Gevraagde stukken / toelichtingen

1. **OCMW-litigatie:** actuele afrekening, betaalstatus, interest, impact op
   OCMW- en Najaarszon-balans 2025–2026.
2. **Werkingssubsidies EUR1,398m:** nominatieve matrix (OCMW/gemeente/VIA/
   andere) ≥ EUR50k.
3. **Pensioen JUMP** 0,857 → 1,206m: actuariële aannames.
4. **KT-vorderingen niet-ruil EUR3,560m:** tegenpartijenmatrix (OCMW?).
5. **Equity FLAT EUR0,921m** ondanks budget +EUR0,329m: resultaatsbestemming.
6. **Volledige BBC-jaarrekening 2025 Gemeente + OCMW Brakel** (niet gevonden
   op publieke portal dit tick).

Gelieve te antwoorden binnen de wettelijke termijn. Digitaal leveren (PDF) heeft
de voorkeur.

Met vriendelijke groeten,

[Naam]
[Contact]
```

## Notes

- Primary source: BBC JR2025 WV RVT Najaarszon Brakel (103p; KBO 0886.485.770).  
- GE+OCMW Brakel JR2025 not found public this tick.  
- **Do not send** without human OK.  
- Tick 1116 Entity II dual residual after Evergem AGB.
"""
    (FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

    rq_path = DATA / "research_queue.csv"
    lines = rq_path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        if line.startswith("rq_1116,"):
            out.append(
                "rq_1116,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
                "Brakel WV Najaarszon RVT JR2025 Entity II dual residual,"
                f"{GAP},2026-08-11T23:00:00Z,{UTC},"
                "tick1116 Najaarszon assets 5.306m receivables 4.355m HIGH pension JUMP 1.206m "
                "AFM +0.428m werkingssub 1.398m OCMW litigation residual; FOI ready"
            )
        else:
            out.append(line)
    out.append(
        "rq_1117,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
        "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen login-blocked / Vorselaar docs-only / "
        "Kalmthout / Bornem JR2024-only / De Panne OCR / Schelle GE+OCMW if published / Erpe-Mere docs-only / "
        "Brakel GE+OCMW if published / other); prefer FOI-adjacent L5; skip rq_116,"
        f",2026-08-11T23:30:00Z,{UTC},"
        "spawned tick1116 after Brakel Najaarszon Entity II dual residual; next residual dual L5; progress@1120 in 4"
    )
    rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

    state = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{UTC},rq_1116,1116,no,"
        "tick1116 Brakel WV Najaarszon RVT JR2025 Entity II dual residual; "
        "FOI gap_brn_ocmw_litigation_subs_pension_l5 prio9 ready; assets 5.306m cash 0.611m DROP "
        "receivables 4.355m HIGH pension JUMP 1.206m AFM +0.428m BBR 2.241m budget +0.329m "
        "werkingssub 1.398m personnel 3.990m equity flat 0.921m OCMW litigation residual ~0.109m; "
        "next residual dual L5 rq_1117; progress@1120 in 4; rq_116 deferred\n"
    )
    (DATA / "loop_state.csv").write_text(state, encoding="utf-8")

    log_entry = f"""
### Tick 1116 - {UTC}

- Unit: **rq_1116** (FOI-adjacent residual dual - **WV RVT Rusthuis Najaarszon Brakel Jaarrekening 2025** Entity II + Evergem AGB dual residual)
- Found (strong primary BBC JR2025 103p text; brakel.be; KBO 0886.485.770; Kasteelstraat 50 9660; leden **OCMW Brakel + vzw Sint-Jozef**; Voorzitter Bruno Schollaert):
  - Assets **EUR5.306m JUMP** (was **EUR4.590m**) / equity **EUR0.921m FLAT FOI** (same as 2024) / debt total **EUR4.386m** / fin debt **EUR0.162m LOW**
  - Cash **EUR0.611m DROP FOI** (was **EUR0.760m**) / pension **EUR1.206m JUMP FOI** (was **EUR0.857m**; +**EUR0.349m**)
  - KT vorderingen **EUR4.355m HIGH FOI** (niet-ruil **EUR3.560m**)
  - Exploitatie: ontvangsten **EUR6.959m** / uitgaven **EUR6.521m** / saldo **+EUR0.439m STRONG**
  - AFM **+EUR0.428m STRONG** (MJP was **+EUR0.054m**) / BBR **EUR2.241m** / budget **+EUR0.329m POS** (MJP was **−EUR0.046m**)
  - Omzet **EUR5.552m** / personeel **EUR3.990m** / goederen **EUR2.520m**
  - Werkingssubsidies **EUR1.398m FOI** (was **EUR1.634m**; alg **EUR0.245m** / spec **EUR1.153m**)
  - Invest **EUR0.099m** near MJP **EUR0.100m**
  - **OCMW litigation residual HIGH FOI:** JR toelichting ramt netto OCMW-betaling ca. **EUR108.587** (+interest path to 1 jun 2026); OCMW-vertegenwoordigers betwisten cijfers
- Dual: Evergem AGB city toelage / AFM FLIP (tick1115) - not TE-additive
- Note: GE+OCMW Brakel JR2025 not public this tick; Oosterzele / Nijlen / Vorselaar / Kalmthout / Bornem / De Panne residual next; progress@1120 in 4
- Wrote: budgets +21 (bud_brn_*); commitments +7; leaderboard +9; sources +1; entities zorg_brakel_najaarszon + city_brakel; FOI **gap_brn_ocmw_litigation_subs_pension_l5** prio9 ready + draft; PDF primary (not committed 4.6MB); rq_1116=done; spawn **rq_1117**; ticks=1116
- FOI: ready only - **do not send**
- Next: prio5 **rq_1117** residual dual L5; deferred **rq_116**; progress@1120 in 4
"""
    log_text = LOG.read_text(encoding="utf-8")
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding="utf-8")

    print("tick1116 write OK")
    print("budgets", len(bud), "commitments", len(comm), "lbs", len(lbs))
    print("gap", GAP)


if __name__ == "__main__":
    main()

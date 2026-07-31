# -*- coding: utf-8 -*-
"""Tick 672: VL BA2026 ch6 receipts + Omgeving/MVP/De Lijn residual dual — rq_663."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T09:45:00Z"
TICK = 672
RQ = "rq_663"
NEXT_RQ = "rq_664"
GAP = "gap_vl_ba2026_receipts_omgeving_l5"
SRC = "src_ccrek_vl_ba2026_receipts_omgeving"
SRC_DUAL = "src_dual_vl_receipts_omgeving_tick672"


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
        f"tick{TICK} VL BA2026 receipts dot 34.8bn opcentiemen 10.8bn MVP 88m dual; "
        f"next {NEXT_RQ}; progress@680 in 8; rq_116 deferred"
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
    "vvc_vlaanderen,Vlaams Verwerkingscentrum trajectcontrole,Vlaams Verwerkingscentrum,Flanders fine processing dual fed Crossborder,agency,vlaanderen_gov,nl,,,CoA BA2026 rec plan 50m doubtful; opex cruise 5.9m no VL admin surcharge; tick672",
    "vmsw,VMSW sociaal wonen,Vlaamse Maatschappij voor Sociaal Wonen,Flanders social housing dual SWL,agency,vlaanderen_gov,nl,https://www.vmsw.be,,,CoA BA2026 basiskoten VAK +100m; FS4 interest reform dual WAL SWL; tick672",
]

src_rows = [
    f"{SRC},CoA Flanders BA2026 ch6 receipts + Omgeving MVP De Lijn dual,https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf,Cour des comptes / Rekenhof,2026-08-01,audit,"
    "Strong tick672: Table17 dotaties BA 34824.3 (gewest 3728 gemeenschap 31096.3); FPB Mar +241 Jun +516.5 not in rec; afrekening 2025 -161.9; Table18 bruto opcentiemen 10790.3 path +391.7 voorschotten 9775.7 +254.6 fiscale uitg 1036.2 afrekeningen -21.6; spelen 4.4 (was 40 cruise 16) no decree; VVC 50m doubtful; MVP transition 88.2 (38+50.2 EPC) on Energiefonds saldo; Klimaat->Energie 51.6 +31.6; Klimaatfonds VEK 57.3 from 110.3; De Lijn net rev -25 werking +39.4 exploit +27.1 PPS 3.5 missing; Sluis Terneuzen 21.5 missing NL 15; BAC net -63.7 vs plan -34 rent 79; BAISA div 7.9; O&O provisie misuse",
    f"{SRC_DUAL},Dual VL receipts opcentiemen MVP vs WAL fiscal dual,https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf,DOGE synthesis CoA VL BA dual WAL FWB,2026-08-01,synthesis,"
    "Strong dual: VL opcentiemen 10.79bn dual WAL IPP; MVP 88m dual Renopack; De Lijn dual OTW; not TE-additive; tick672",
]

bud_rows = [
    # Table17 dotaties
    f"bud_vl_dotaties_total_ba2026,vlaanderen_gov,2026,34824300000,,,budgeted,{SRC},strong,Totaal BFW dotaties BA2026 34824.3m incl afrekening 2025; tick672",
    f"bud_vl_gewestmiddelen_ba2026,vlaanderen_gov,2026,3728000000,,,budgeted,{SRC},strong,Gewestmiddelen BA 3728.0m (FPB Mar sim 3755.5 / Jun 3786.9); tick672",
    f"bud_vl_gemeenschapsmiddelen_ba2026,vlaanderen_gov,2026,31096300000,,,budgeted,{SRC},strong,Gemeenschapsmiddelen BA 31096.3m (FPB Mar 31309.8 / Jun 31553.9); tick672",
    f"bud_vl_dotaties_fpb_mar_gap_241m,vlaanderen_gov,2026,241000000,,,budgeted,{SRC},strong,If FPB Mar2026 params on receipts: +241.0m vs VL raming (asymmetry vs dep); tick672",
    f"bud_vl_dotaties_fpb_jun_gap_516_5m,vlaanderen_gov,2026,516500000,,,budgeted,{SRC},strong,If FPB Jun2026 params: +516.5m vs VL raming (inflation 3.4pct); tick672",
    f"bud_vl_afrekening_2025_on_2026,vlaanderen_gov,2026,-161900000,,,budgeted,{SRC},strong,Negatieve afrekening 2025 on 2026 receipts -161.9m (BO had -141.7); tick672",
    f"bud_vl_dotaties_year_path_plus_135_9m,vlaanderen_gov,2026,135900000,,,budgeted,{SRC},strong,Dotaties 2026 excl afrekeningen path +135.9m vs BO (growth 1.1 infl 1.9); tick672",
    # Table18 opcentiemen
    f"bud_vl_opcentiemen_bruto_ba2026,vlaanderen_gov,2026,10790300000,,,budgeted,{SRC},strong,Bruto opcentiemen BA 10790.3m path +391.7 vs BO 10398.5; dual WAL IPP; tick672",
    f"bud_vl_opcentiemen_voorschotten_ba2026,vlaanderen_gov,2026,9775700000,,,budgeted,{SRC},strong,Voorschotten gewestelijke PB BA 9775.7m path +254.6; tick672",
    f"bud_vl_fiscale_uitgaven_opcentiemen_ba2026,vlaanderen_gov,2026,1036200000,,,budgeted,{SRC},strong,Fiscale uitgaven (opcentiemen package) BA 1036.2m path +0.2; tick672",
    f"bud_vl_opcentiemen_deel_voorschotten_ba2026,vlaanderen_gov,2026,10811900000,,,budgeted,{SRC},strong,Opcentiemen deel voorschotten 10811.9m path +254.9; tick672",
    f"bud_vl_opcentiemen_afrekeningen_ba2026,vlaanderen_gov,2026,-21600000,,,budgeted,{SRC},strong,Afrekeningen vorige AJ BA -21.6m path +136.9 vs BO -158.5; tick672",
    f"bud_vl_opcentiemen_bruto_2025,vlaanderen_gov,2025,10342400000,,,outturn,{SRC},strong,Bruto opcentiemen realisatie 2025 10342.4m; tick672",
    f"bud_vl_opcentiemen_bruto_2024,vlaanderen_gov,2024,10086700000,,,outturn,{SRC},strong,Bruto opcentiemen realisatie 2024 10086.7m; tick672",
    f"bud_vl_afrekening_aj2025_ba,vlaanderen_gov,2026,-71500000,,,budgeted,{SRC},strong,Afrekening AJ2025 in BA -71.5m (BO was -207.1); tick672",
    # Spelen VVC
    f"bud_vl_spelen_weddenschappen_ba2026,vlaanderen_gov,2026,4400000,,,budgeted,{SRC},strong,Spelen/Weddenschappen BA 4.4m (BO 40m dropped; tariff 11->15pct); cruise 16.0; no decree yet; tick672",
    f"bud_vl_spelen_cruise_16m,vlaanderen_gov,2026,16000000,,,budgeted,{SRC},strong,Spelen tariff raise full-speed effect 16.0m/yr admin est; tick672",
    f"bud_vvc_rec_plan_50m_ba2026,vvc_vlaanderen,2026,50000000,,,budgeted,{SRC},strong,VVC ontvangsten plan 50.0m held BA; CoA feasibility doubts; Crossborder path no VL surcharge; tick672",
    f"bud_vvc_opex_cruise_5_9m,vvc_vlaanderen,2026,5900000,,,budgeted,{SRC},strong,VVC opex cruise ~5.9m; no VL admin surcharge on fines; tick672",
    # Omgeving energie
    f"bud_vl_mvp_transition_88_2m,vlaanderen_gov,2026,88200000,,,budgeted,{SRC},strong,MVP+EPC overgangsmaatregelen total 88.2m on Energiefonds saldo (no extra credits); tick672",
    f"bud_vl_mvp_transition_38m,vlaanderen_gov,2026,38000000,,,budgeted,{SRC},strong,Mijn VerbouwPremie transition cost 38.0m (deadline 28Feb2026); tick672",
    f"bud_vl_epc_label_transition_50_2m,vlaanderen_gov,2026,50200000,,,budgeted,{SRC},strong,EPC-labelpremie transition 50.2m (deadline 30Jun2026); tick672",
    f"bud_vl_klimaat_to_energie_51_6m,vlaanderen_gov,2026,51600000,,,budgeted,{SRC},strong,Klimaatfonds toelage aan Energiefonds 51.6m path +31.6; REG ODV use opaque; tick672",
    f"bud_vl_klimaatfonds_vek_ba2026,vlaanderen_gov,2026,57300000,,,budgeted,{SRC},strong,Vlaams Klimaatfonds provisie VEK BA 57.3m (BO 110.3 path -53; PAS calendar); tick672",
    f"bud_vl_klimaatfonds_vek_bo2026,vlaanderen_gov,2026,110300000,,,budgeted,{SRC},strong,Klimaatfonds VEK BO2026 110.3m; tick672",
    # Wonen VMSW
    f"bud_vmsw_basiskoten_vak_plus_100m,vmsw,2026,100000000,,,budgeted,{SRC},strong,VMSW basiskoten renteloze leningen HE VAK +100m BA (new policy weak toelichting); tick672",
    f"bud_vmsw_student_housing_fs3_100m,vmsw,2026,100000000,,,budgeted,{SRC},strong,VMSW FS3 student housing loans to woonmaatschappijen BO already 100m; tick672",
    # De Lijn / MOW residual
    f"bud_delijn_net_rev_path_minus_25m,de_lijn,2026,-25000000,,,budgeted,{SRC},strong,De Lijn netto-vervoersopbrengsten path -25.0m BA; tick672",
    f"bud_delijn_werkingstoelage_path_plus_39_4m,de_lijn,2026,39400000,,,budgeted,{SRC},strong,De Lijn werkingstoelage path +39.4m (GIP provisie 33.7 + uitbreiding OV 25.0 - Werkvennootschap -12.6 - efficientie -5.5); tick672",
    f"bud_delijn_exploitanten_path_plus_27_1m,de_lijn,2026,27100000,,,budgeted,{SRC},strong,De Lijn werkingsuitgaven exploitanten +27.1m (vergroening opstap new contracts); tick672",
    f"bud_delijn_pps_oplevering_3_5m_missing,de_lijn,2026,3500000,,,budgeted,{SRC},strong,De Lijn PPS oplevering 3.5m 2026 credits missing (2025 revisor 23.7m); tick672",
    f"bud_sluis_terneuzen_vek_21_5m,vlaanderen_gov,2026,21500000,,,budgeted,{SRC},strong,Nieuwe Sluis Terneuzen VEK BA 21.5m (ruiter 76.2 end2025); tick672",
    f"bud_sluis_terneuzen_nl_settle_15m_missing,vlaanderen_gov,2026,15000000,,,budgeted,{SRC},strong,Sluis Terneuzen NL eindafrekening 15.0m in kasplan/GIP but no VEK in BA CoA flag; tick672",
    # BAC / WEWIL
    f"bud_bac_dividend_ordinary_15_3m,vlaanderen_gov,2026,15300000,,,budgeted,{SRC},strong,BAC ordinary dividend 15.3m BA; tick672",
    f"bud_baisa_dividend_oneoff_7_9m,vlaanderen_gov,2026,7900000,,,budgeted,{SRC},strong,BAISA one-off dividend 7.9m; tick672",
    f"bud_bac_interest_79m,vlaanderen_gov,2026,79000000,,,budgeted,{SRC},strong,BAC participation interest cost 79.0m structural/yr; tick672",
    f"bud_bac_net_gap_63_7m,vlaanderen_gov,2026,-63700000,,,budgeted,{SRC},strong,BAC net dividend-interest -63.7m (plan -34.0; gap -29.7); with BAISA -55.8; tick672",
    f"bud_bac_plan_net_minus_34m,vlaanderen_gov,2026,-34000000,,,budgeted,{SRC},strong,BAC multi-year plan net -34.0m 2026; tick672",
    f"bud_vl_oo_provisie_bac_compensate,vlaanderen_gov,2026,33300000,,,budgeted,{SRC},strong,O&O provisie used to compensate BAC interest (BO 33.3 + BA +1.6 + Roadrunner 7.9); CoA specialty fail; tick672",
    # Dual
    f"bud_dual_opcentiemen_wal_ipp_2026,gg_belgium,2026,10790300000,,,budgeted,{SRC_DUAL},strong,Dual VL bruto opcentiemen 10.79bn vs WAL regional IPP class (not sum); tick672",
    f"bud_dual_mvp_renopack_2026,gg_belgium,2026,88200000,,,budgeted,{SRC_DUAL},strong,Dual VL MVP transition 88.2m vs WAL Renopack/Ecopack fonds; not TE-additive; tick672",
]

cmt_rows = [
    f"cmt_vl_dotaties_opcentiemen_ba2026,VL BA2026 dotaties 34.8bn opcentiemen 10.79bn dual,vlaanderen_gov,BFW+PB,CoA BA2026 Table17-18,2026-06-19,2026,2026,34824300000,\"{{\"\"2026\"\":34824300000}}\",,active,,Receipts dual WAL,FPB Jun gap 516m,{SRC},strong,Vlaanderen>ontvangsten>BA2026,tick672",
    f"cmt_vl_mvp_epc_transition_88m,MVP+EPC transition 88.2m on Energiefonds dual,vlaanderen_gov,Omgeving energie,CoA BA2026 7.6.1,2025-10-24,2026,2026,88200000,\"{{\"\"2026\"\":88200000}}\",,active,,Renovation dual WAL,Fund transparency,{SRC},strong,Vlaanderen>Omgeving>MVP,No extra credits; tick672",
    f"cmt_delijn_ba2026_path,De Lijn BA2026 werking +39.4 exploit +27.1 dual OTW,de_lijn,De Lijn,CoA BA2026 7.5,2026-01-01,2026,2026,39400000,\"{{\"\"2026\"\":39400000}}\",,active,,PES dual OTW,PPS 3.5 missing,{SRC},strong,Vlaanderen>DeLijn>BA2026,tick672",
    f"cmt_bac_interest_79m_oo_provisie,BAC interest 79m via O&O provisie specialty,vlaanderen_gov,BAC participation,CoA BA2026 7.7.1,2026-01-01,2026,2026,79000000,\"{{\"\"2026\"\":79000000}}\",,active,,Specialty breach,Proper budget article,{SRC},strong,Vlaanderen>BAC>interest,Net -63.7; tick672",
    f"cmt_dual_vl_receipts_mvp_tick672,Dual VL receipts MVP De Lijn vs WAL,gg_belgium,Entity II dual,CoA VL BA dual,2026-06-19,2026,2026,10790300000,\"{{\"\"2026\"\":10790300000}}\",,active,,Dual receipts map,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>vl_receipts_mvp,tick672",
    f"cmt_vvc_50m_doubtful,VVC fine rec 50m doubtful dual fed,vvc_vlaanderen,VVC,CoA BA2026 6.5,2026-01-01,2026,2026,50000000,\"{{\"\"2026\"\":50000000}}\",,active,,Optimistic receipt,Crossborder path,{SRC},strong,Vlaanderen>VVC,tick672",
]

lb_rows = [
    f"lb_vl_opcentiemen_10_79bn_2026,VL bruto opcentiemen 10.79bn dual WAL IPP,Flanders,ops,Vlaanderen>ontvangsten>opcentiemen,10790300000,0,Strong CoA Table18 path +392m; dual WAL regional PB; fiscale uitg 1.04bn,strong,{SRC},taxpayers,Regional PIT dual,Primary,5.0,9.0,2,6.7,Publish TE split,open,,tick672",
    f"lb_vl_dotaties_34_8bn_2026,VL BFW dotaties 34.82bn dual,Flanders,ops,Vlaanderen>ontvangsten>dotaties,34824300000,0,Strong CoA: FPB Jun would +516m; asymmetry rec/dep params dual,strong,{SRC},BFW,Institutional transfers,Primary,5.0,9.5,2,6.95,Align FPB params,open,,tick672",
    f"lb_vl_mvp_transition_88m_2026,MVP+EPC transition 88.2m Energiefonds,Flanders,ops,Vlaanderen>Omgeving>MVP,88200000,0,Strong CoA no extra credits on fonds saldo; dual Renopack WAL,strong,{SRC},households,Renovation dual,Primary,6.5,6.0,2,5.95,Separate budget lines,open,,tick672",
    f"lb_bac_interest_79m_specialty_2026,BAC interest 79m via O&O provisie,Flanders,ops,Vlaanderen>BAC>interest,79000000,0,Strong CoA specialty fail; net -63.7 vs plan -34; dual participation finance,strong,{SRC},BAC,Budget specialty,Primary,8.0,6.0,2,6.6,Move off O&O provisie,open,,tick672",
    f"lb_delijn_exploit_green_27m_2026,De Lijn exploitanten vergroening +27.1m dual OTW,Flanders,ops,Vlaanderen>DeLijn>exploitanten,27100000,0,Strong CoA path; dual OTW e-bus capital cut,strong,{SRC},private operators,PES dual,Primary,6.0,5.5,2,5.55,Unit cost FOI,open,,tick672",
    f"lb_dual_vl_receipts_mvp_2026,Dual VL receipts+MVP vs WAL,Belgium,ops,Belgium>dual>vl_receipts_mvp,10790300000,0,Strong dual: opcentiemen 10.79bn MVP 88m De Lijn vs WAL IPP/Renopack/OTW; not TE-additive,strong,{SRC_DUAL},Entity II dual,Receipts dual residual,Primary dual,6.0,8.5,3,6.65,Cross FOI,open,,tick672",
]

foi_row = (
    f"{GAP},Vlaanderen>BA2026>receipts_omgeving_L5,vlaanderen_gov,"
    "Opcentiemen fiscale uitgaven L5 split; FPB param impact cash; MVP/EPC 88.2 cash on Energiefonds; Klimaatfonds 57.3 PAS calendar; VVC 50m feasibility; BAC interest article; De Lijn PPS 3.5 + Terneuzen NL 15; VMSW basiskoten policy note,"
    "CoA VL BA2026 receipts Omgeving strong tick672; L5 dual,"
    f"5,Departement FB / Omgeving / De Lijn / openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,https://www.vlaanderen.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_vl_dotaties_opcentiemen_ba2026|cmt_vl_mvp_epc_transition_88m|cmt_bac_interest_79m_oo_provisie,"
    f"lb_vl_opcentiemen_10_79bn_2026|lb_vl_mvp_transition_88m_2026|lb_bac_interest_79m_specialty_2026,"
    f"{NOW},{NOW},tick672 CoA VL BA2026 primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof VL BA2026 (2026_28) ch.6 + §7.5–7.7

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: Departement FB / Omgeving / De Lijn / Team Openbaarheid
openbaarheid@vlaanderen.be

Betreft: Openbaarheid — BA2026 ontvangsten (opcentiemen/dotaties) + Omgeving/De Lijn L5

Geachte,

Op grond van het Bestuursdecreet verzoek ik om:

1. Bruto opcentiemen 10.790,3 mEUR: split fiscale uitgaven 1.036,2 mEUR per maatregel.
2. Simulatie impact FPB juni 2026 (+516,5 mEUR) op 2026-ontvangsten / 2027-afrekening.
3. MVP+EPC overgang 88,2 mEUR: kasuitgaven op Energiefonds per maand 2026.
4. Klimaatfonds VEK 57,3 mEUR: PAS-spreiding vs BO 110,3 mEUR.
5. VVC: onderbouwing 50 mEUR ontvangsten en stand protocollen Crossborder.
6. BAC: rentelast 79 mEUR en verplaatsing compensatie uit O&O-provisie.
7. De Lijn: ontbrekende 3,5 mEUR PPS-oplevering; Sluis Terneuzen NL 15 mEUR.

Période: 2024-01-01 tot 2027-12-31.
Vorm: CSV/XLSX bij voorkeur.

Met vriendelijke groet,
[Naam]
```

## Notes agent
- Primary: CoA 2026_28 VL BA2026 tick672.
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **VL BA2026 ch6 receipts + Omgeving MVP/De Lijn/BAC dual**)
- Found (primary CoA 2026_28): **Dotaties BA EUR34.824bn** (gewest **3.728** gemeenschap **31.096**); FPB Mar gap **+241** / Jun **+516.5** not in rec; afrekening 2025 **-161.9**. **Bruto opcentiemen EUR10.790bn** path **+391.7** (voorschotten **9775.7 +254.6**; fiscale uitg **1036.2**; afrekeningen **-21.6**). Spelen **4.4** (was 40; cruise 16) no decree; VVC **50** doubtful. **MVP+EPC transition EUR88.2m** (38+50.2) on Energiefonds; Klimaat->Energie **51.6 +31.6**; Klimaatfonds VEK **57.3** (from 110.3). **De Lijn** net rev **-25** werking **+39.4** exploit **+27.1** PPS **3.5** missing; Terneuzen **21.5** NL **15** missing. **BAC** interest **79** net **-63.7** (plan -34) via O&O provisie. Dual WAL IPP/Renopack/OTW. Strong CoA; L5 FOI.
- Wrote: entities (+2); budgets (+45); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@680 in 8 ticks; rq_116 deferred
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
        f"tick{TICK} VL BA2026 receipts 34.8bn opcentiemen 10.79bn MVP 88m De Lijn dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,vlaanderen_gov,"
        f"Next residual: VL BA2026 WVG residual deep or federal CoA 2026_22 dual or De Lijn annual accounts L5.,,"
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

from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 678
utc = "2026-08-01T11:15:00Z"
src = "src_ccrek_vl_ba2026_fonds"
src_dual = "src_dual_vl_fonds_tick678"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf"

src_rows = [
    f'{src},CoA Flanders BA2026 begrotingsfondsen Table9-10 residual dual WAL,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick678: begrotingsfondsen begin 928.7 end 856.5 (-72.2); rec 866.8 exp -608.6 desaffect -330.4; ESR impact +265.8 (rec 791.9 exp 526.1); Verkeersveiligheid end 180.2 rec 40 exp -37.4 des -2.6; Klimaat end 58.5 rec 264.5 exp -11.3 des -252.8 cum deficit ~54; Energie end 257.2 rec 218.5 (own 166.9 internal 51.6) exp -205.1 des -46.2 (admin 56.2 vs art32 max 46.2 conflict; IB was 27.8); Wedden onderwijs end 93.6 rec 147 exp -176.7; Andere end 267 rec 196.9 des -28.8; toegewezen toelichting 812.9 vs decree 866.8; Klimaat->Energie +31.6 REG; ICL 194 (-23) auction +11.7; buffer provisie +58.5 no specialty; index under 48.3+7.0; missing desaffect ODA 0.8 ESF 25.9; traffic fines 168.3 (was 202.8 -34.5) above 161.2 threshold; VCO art15 deviation personnel leave fund"',
    f'{src_dual},Dual VL begrotingsfondsen 0.86bn end vs WAL fonds stocks dual,{url},DOGE synthesis CoA VL+WAL fonds,2026-08-01,synthesis,"Strong dual: VL fonds end 856.5m + Klimaat cum deficit 54 vs WAL Kyoto/dechets/env fonds stocks class; not TE-additive; tick678"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # Totals Table 9
    f"bud_vl_begrotingsfondsen_begin_928_7m_2026,vlaanderen_gov,2026,928700000,,,budgeted,{src},strong,Begrotingsfondsen effective begin saldo 2026 928.7m (est eoy2025 IB 923.8); CoA T9; tick678",
    f"bud_vl_begrotingsfondsen_end_856_5m_2026,vlaanderen_gov,2026,856500000,,,budgeted,{src},strong,Begrotingsfondsen geraamd eindsaldo 2026 856.5m after desaffect 330.4; path -72.2 (-7.8pct); tick678",
    f"bud_vl_begrotingsfondsen_rec_866_8m_2026,vlaanderen_gov,2026,866800000,,,budgeted,{src},strong,Begrotingsfondsen receipts 866.8m 2026 (decree total incl internal); tick678",
    f"bud_vl_begrotingsfondsen_exp_608_6m_2026,vlaanderen_gov,2026,608600000,,,budgeted,{src},strong,Begrotingsfondsen VEK expenditures 608.6m 2026; tick678",
    f"bud_vl_begrotingsfondsen_desaffect_330_4m_2026,vlaanderen_gov,2026,330400000,,,budgeted,{src},strong,Desaffectaties to algemene middelen 330.4m 2026 (no ESA saldo impact); tick678",
    f"bud_vl_begrotingsfondsen_esa_impact_265_8m_2026,vlaanderen_gov,2026,265800000,,,budgeted,{src},strong,Positive ESA vorderingensaldo impact fonds 265.8m (ESR rec 791.9 - exp 526.1); tick678",
    f"bud_vl_fonds_esr_rec_791_9m_2026,vlaanderen_gov,2026,791900000,,,budgeted,{src},strong,Fonds ESR/eigen ontvangsten 791.9m of 866.8 total; tick678",
    f"bud_vl_fonds_esr_exp_526_1m_2026,vlaanderen_gov,2026,526100000,,,budgeted,{src},strong,Fonds ESR uitgaven 526.1m; tick678",
    f"bud_vl_fonds_internal_stromen_73_2m_2026,vlaanderen_gov,2026,73200000,,,budgeted,{src},strong,Fonds internal streams 73.2m (of which Energiefonds 51.6); tick678",
    f"bud_vl_toegewezen_toelichting_812_9m_2026,vlaanderen_gov,2026,812900000,,,budgeted,{src},medium,Algemene toelichting toegewezen ontvangsten 812.9m (-91.2 vs IB) CoA could not reconstitute; vs decree 866.8; tick678",
    # Per-fund Table 9
    f"bud_vl_vvf_begin_180_2m_2026,vlaanderen_gov,2026,180200000,,,budgeted,{src},strong,Verkeersveiligheidsfonds begin 180.2m (est eoy IB 213.8); tick678",
    f"bud_vl_vvf_rec_40m_2026,vlaanderen_gov,2026,40000000,,,budgeted,{src},strong,Verkeersveiligheidsfonds receipts 40.0m 2026; tick678",
    f"bud_vl_vvf_exp_37_4m_2026,vlaanderen_gov,2026,37400000,,,budgeted,{src},strong,Verkeersveiligheidsfonds exp 37.4m; tick678",
    f"bud_vl_vvf_desaffect_2_6m_2026,vlaanderen_gov,2026,2600000,,,budgeted,{src},strong,Verkeersveiligheidsfonds desaffect 2.6m; tick678",
    f"bud_vl_vvf_end_180_2m_2026,vlaanderen_gov,2026,180200000,,,budgeted,{src},strong,Verkeersveiligheidsfonds end 180.2m (flat); tick678",
    f"bud_vl_traffic_fines_est_168_3m_2026,vlaanderen_gov,2026,168300000,,,budgeted,{src},strong,FOD Fin Feb2026 traffic fines est 168.3m (was 202.8; -34.5); above VVF threshold 161.2 so full hit in fonds; tick678",
    f"bud_vl_traffic_fines_threshold_161_2m,vlaanderen_gov,2026,161200000,,,budgeted,{src},strong,Verkeersveiligheidsfonds fine threshold 161.2m; tick678",
    f"bud_vl_klimaatfonds_begin_58_1m_2026,vlaanderen_gov,2026,58100000,,,budgeted,{src},strong,Klimaatfonds begin saldo 58.1m (IB est eoy 32.6); tick678",
    f"bud_vl_klimaatfonds_rec_264_5m_2026,vlaanderen_gov,2026,264500000,,,budgeted,{src},strong,Klimaatfonds receipts 264.5m 2026 (auctions+); tick678",
    f"bud_vl_klimaatfonds_exp_11_3m_2026,vlaanderen_gov,2026,11300000,,,budgeted,{src},strong,Klimaatfonds direct VEK exp 11.3m; tick678",
    f"bud_vl_klimaatfonds_desaffect_252_8m_2026,vlaanderen_gov,2026,252800000,,,budgeted,{src},strong,Klimaatfonds desaffect/transfer 252.8m 2026; tick678",
    f"bud_vl_klimaatfonds_end_58_5m_2026,vlaanderen_gov,2026,58500000,,,budgeted,{src},strong,Klimaatfonds budget end surplus 58.5m; CoA: not equal to real cumulative position; tick678",
    f"bud_vl_klimaatfonds_cum_deficit_54m_2026,vlaanderen_gov,2026,54000000,,,estimate,{src},strong,Klimaatfonds cumulative deficit end2026 ~54m (IB 56) after historic commitments; CoA transparency gap; tick678",
    f"bud_vl_klimaat_to_energie_31_6m_2026,vlaanderen_gov,2026,31600000,,,budgeted,{src},strong,Klimaatfonds toelage to Energiefonds +31.6m for REG-ODV financing; tick678",
    f"bud_vl_icl_194m_2026,vlaanderen_gov,2026,194000000,,,budgeted,{src},strong,Indirect carbon leakage (ICL) costs 194.0m 2026 (-23.0 vs prior); tick678",
    f"bud_vl_klimaat_auction_up_11_7m_2026,vlaanderen_gov,2026,11700000,,,budgeted,{src},strong,Higher ETS auction revenue +11.7m path in Klimaatfonds; tick678",
    f"bud_vl_energiefonds_begin_290m_2026,vlaanderen_gov,2026,290000000,,,budgeted,{src},strong,Energiefonds begin 290.0m (IB est eoy 309.6); tick678",
    f"bud_vl_energiefonds_rec_218_5m_2026,vlaanderen_gov,2026,218500000,,,budgeted,{src},strong,Energiefonds receipts 218.5m (own 166.9 + internal 51.6); tick678",
    f"bud_vl_energiefonds_own_166_9m_2026,vlaanderen_gov,2026,166900000,,,budgeted,{src},strong,Energiefonds eigen/ESR receipts 166.9m; tick678",
    f"bud_vl_energiefonds_internal_51_6m_2026,vlaanderen_gov,2026,51600000,,,budgeted,{src},strong,Energiefonds internal streams 51.6m (Klimaat transfer class); tick678",
    f"bud_vl_energiefonds_exp_205_1m_2026,vlaanderen_gov,2026,205100000,,,budgeted,{src},strong,Energiefonds exp 205.1m 2026; tick678",
    f"bud_vl_energiefonds_desaffect_46_2m_art32_2026,vlaanderen_gov,2026,46200000,,,budgeted,{src},strong,Energiefonds desaffect art32 max 46.2m to algemene middelen; tick678",
    f"bud_vl_energiefonds_desaffect_56_2m_admin_2026,vlaanderen_gov,2026,56200000,,,budgeted,{src},strong,Admin uitgaventabel Energiefonds desaffect 56.2m (vs art32 46.2 conflict; IB was 27.8 for energy interest); CoA formal remark; tick678",
    f"bud_vl_energiefonds_end_257_2m_2026,vlaanderen_gov,2026,257200000,,,budgeted,{src},strong,Energiefonds end 257.2m (-32.8 / -11.3pct); tick678",
    f"bud_vl_weddenfonds_begin_123_3m_2026,vlaanderen_gov,2026,123300000,,,budgeted,{src},strong,Fonds Wedden/Toelagen Onderwijs begin 123.3m; tick678",
    f"bud_vl_weddenfonds_rec_147m_2026,vlaanderen_gov,2026,147000000,,,budgeted,{src},strong,Weddenrecuperatiefonds receipts 147.0m (wrongly paid wages recoveries); tick678",
    f"bud_vl_weddenfonds_exp_176_7m_2026,vlaanderen_gov,2026,176700000,,,budgeted,{src},strong,Weddenfonds exp 176.7m; tick678",
    f"bud_vl_weddenfonds_end_93_6m_2026,vlaanderen_gov,2026,93600000,,,budgeted,{src},strong,Weddenfonds end 93.6m (-29.7 / -24.1pct); tick678",
    f"bud_vl_fonds_andere_end_267m_2026,vlaanderen_gov,2026,267000000,,,budgeted,{src},strong,Other begrotingsfondsen end 267.0m (begin 277 rec 196.9 exp -178.1 des -28.8); tick678",
    f"bud_vl_volwassenen_inschrijf_40_9m_2026,vlaanderen_gov,2026,40900000,,,budgeted,{src},strong,Inschrijvingsgelden volwassenenonderwijs fonds receipts 40.9m; tick678",
    f"bud_vl_desaffect_oda_0_8m_missing_2026,vlaanderen_gov,2026,800000,,,budgeted,{src},strong,Desaffect Fonds ontwikkelingssamenwerking 0.8m missing from middelendecreet table; CoA formal; tick678",
    f"bud_vl_desaffect_esf_25_9m_missing_2026,vlaanderen_gov,2026,25900000,,,budgeted,{src},strong,Desaffect Vlaams Cofinancieringsfonds ESF 25.9m missing from table; CoA formal; tick678",
    f"bud_vl_ho_recuperatie_desaffect_2m_2026,vlaanderen_gov,2026,2000000,,,budgeted,{src},strong,Recuperatiefonds Hoger Onderwijs desaffect 2.0m art4 middelendecreet; tick678",
    # FB provisies residual
    f"bud_vl_bufferprovisie_up_58_5m_2026,vlaanderen_gov,2026,58500000,,,budgeted,{src},strong,Buffer provisie Monitoring +58.5m VEK without budget specialty; CoA: explain use in outturn; tick678",
    f"bud_vl_index_provisie_under_48_3m_2026,vlaanderen_gov,2026,48300000,,,estimate,{src},strong,Index provisie underestimation 48.3m (spilindex Jun not Jul; FPB Jun vs Mar); tick678",
    f"bud_vl_gezondheidsindex_extra_7m_2026,vlaanderen_gov,2026,7000000,,,estimate,{src},strong,Health-index growth 3.2pct vs BA 2.7 → ~7.0m extra ops/wage; tick678",
    # Ruiter residual
    f"bud_vl_ruiter_vak_carry_1415m_2026,vlaanderen_gov,2026,1415300000,,,budgeted,{src},strong,Overdracht vastleggingskredieten 2025->2026 1415.3m (of which ESR8 126.9); CoA T8; tick678",
    f"bud_vl_consol_beleid_vak_67789m_2026,vlaanderen_gov,2026,67788900000,,,budgeted,{src},strong,ESR-consolidated policy VAK BA2026 67788.9m + carry 1415.3; tick678",
    f"bud_dual_vl_fonds_end_856m_2026,gg_belgium,2026,856500000,,,budgeted,{src_dual},strong,Dual VL begrotingsfondsen end 856.5m vs WAL fonds stocks class; not TE-additive; tick678",
    f"bud_dual_klimaat_cum_deficit_54m_2026,gg_belgium,2026,54000000,,,estimate,{src_dual},strong,Dual Klimaatfonds cum deficit ~54m vs WAL Kyoto stock opacity class; tick678",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

cmt_rows = [
    f'cmt_vl_begrotingsfondsen_856m,VL begrotingsfondsen end 856.5m dual WAL,vlaanderen_gov,MVG funds,CoA 2026_28 T9,2026-06-01,2026,2026,856500000,"{{""begin"":928700000,""end"":856500000,""desaffect"":330400000}}",,active,,Flexible multi-year credits,Publish L5 per fund,{src},strong,VL>fonds>total,tick678',
    f'cmt_vl_klimaatfonds_cum_deficit_54m,Klimaatfonds cum deficit ~54m vs surplus 58.5,vlaanderen_gov,Climate/ETS,CoA 2026_28,2026-06-01,2026,2026,54000000,"{{""surplus_budget"":58500000,""cum_deficit"":54000000}}",,active,,Historic commitments,Transparent eng table,{src},strong,VL>fonds>klimaat,tick678',
    f'cmt_vl_energiefonds_desaffect_conflict,Energiefonds desaffect 46.2 vs admin 56.2,vlaanderen_gov,FB general means,Art32 uitgavendecreet + admin table,2026-06-01,2026,2026,56200000,"{{""art32_max"":46200000,""admin"":56200000}}",,active,,Interest energy related,Align decree/table,{src},strong,VL>fonds>energie,tick678',
    f'cmt_vl_buffer_provisie_58_5m,Buffer provisie +58.5m no specialty,vlaanderen_gov,FB Monitoring,CoA 2026_28 7.1,2026-06-01,2026,2026,58500000,"{{""2026"":58500000}}",,active,,Contingency VEK,Outturn allocation FOI,{src},strong,VL>FB>buffer,tick678',
    f'cmt_vl_index_under_55_3m,Index provisie under 48.3+7.0 health,vlaanderen_gov,Public wages ops,FPB Jun2026 vs BA Mar,2026-06-02,2026,2026,55300000,"{{""spil"":48300000,""gzi"":7000000}}",,active,,Inflation dual fed,Update provisie,{src},strong,VL>FB>index,tick678',
    f'cmt_dual_vl_fonds_tick678,Dual VL fonds 0.86bn vs WAL fonds stocks,gg_belgium,VL+WAL dual,CoA fonds dual,2026-06-01,2026,2026,856500000,"{{""2026"":856500000}}",,active,,Dual residual,Not TE-additive,{src_dual},strong,Belgium>dual>fonds,tick678',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_vl_begrotingsfondsen_856m_2026,VL begrotingsfondsen end 856.5m,Flanders,ops,VL>fonds,856500000,0,Strong CoA T9: begin 928.7 end 856.5 desaffect 330.4; dual WAL,strong,{src},MVG programmes,Flexible funds,Primary,5.5,7.0,3,5.95,L5 per fund FOI,open,,tick678",
    f"lb_vl_klimaat_cum_deficit_54m,Klimaatfonds cum deficit ~54m hidden,Flanders,ops,VL>fonds>klimaat,54000000,0,Strong CoA: budget surplus 58.5 masks historic eng deficit ~54; transparency fail,strong,{src},climate policy,ETS fund,Primary absurd,8.0,5.5,3,6.85,Publish eng table,open,,tick678",
    f"lb_vl_energiefonds_desaffect_conflict,Energiefonds desaffect 46.2 vs 56.2 conflict,Flanders,ops,VL>fonds>energie,56200000,0,Strong CoA formal: art32 max 46.2 admin table 56.2 IB was 27.8 energy interest,strong,{src},FB general means,Desaffect opacity,Primary,7.5,5.0,2,6.45,Align decree,open,,tick678",
    f"lb_vl_buffer_provisie_58_5m,Buffer provisie 58.5m no specialty,Flanders,ops,VL>FB>buffer,58500000,0,Strong CoA: 58.5m VEK budgeted without specialty; outturn allocation unknown,strong,{src},FB monitoring,Contingency,Primary,7.5,5.0,2,6.45,Specialty + report,open,,tick678",
    f"lb_vl_index_under_55m_2026,Index provisie underest ~55m,Flanders,ops,VL>FB>index,55300000,0,Strong CoA: spil 48.3 + GZI 7.0 FPB Jun vs BA Mar,strong,{src},public sector,Inflation dual,Primary,6.5,5.0,2,5.75,Rebase provisie,open,,tick678",
    f"lb_dual_vl_fonds_2026,Dual VL fonds 856m vs WAL stocks,Belgium,ops,Belgium>dual>fonds,856500000,0,Strong dual: VL end 856.5 + Klimaat deficit 54 vs WAL Kyoto/dechets class; not TE-additive,strong,{src_dual},all entities,Fonds dual residual,Primary dual,6.0,7.0,3,6.35,Cross FOI,open,,tick678",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

ent = data / "entities.csv"
et = ent.read_text(encoding="utf-8")
new_ents = []
if "\nvl_begrotingsfondsen," not in et:
    new_ents.append(
        "vl_begrotingsfondsen,Vlaamse begrotingsfondsen,Fonds budgetaires flamands,Flanders budget funds perimeter,agency,vlaanderen_gov,nl,,,CoA BA2026 T9 end 856.5m; tick678"
    )
if "\nvl_verkeersveiligheidsfonds," not in et:
    new_ents.append(
        "vl_verkeersveiligheidsfonds,Verkeersveiligheidsfonds,Fonds securite routiere VL,Flanders road safety budget fund,agency,vlaanderen_gov,nl,,,CoA BA2026 end 180.2m fines threshold 161.2; tick678"
    )
if "\nvl_weddenrecuperatiefonds," not in et:
    new_ents.append(
        "vl_weddenrecuperatiefonds,Fonds Wedden en Toelagen Onderwijs,Fonds salaires enseignement,Flanders education wage recovery fund,agency,vlaanderen_gov,nl,,,CoA BA2026 end 93.6m rec 147; tick678"
    )
if new_ents:
    with ent.open("a", encoding="utf-8", newline="") as f:
        for e in new_ents:
            f.write("\n" + e)

gap_id = "gap_vl_ba2026_begrotingsfondsen_l5"
foi_row = (
    f"{gap_id},Vlaanderen>BA2026>Begrotingsfondsen_L5,vlaanderen_gov,"
    "Per-fund L5 cash 2024-26 Verkeersveiligheid/Klimaat/Energie/Wedden/Andere; Klimaat historic eng table behind cum deficit 54; Energiefonds desaffect 46.2 vs 56.2 reconcile; buffer 58.5 allocation specialties; missing ODA 0.8 ESF 25.9 desaffect lines; ESR bridge 812.9 vs 866.8; VCO art15 personnel-leave fund toelage amount,"
    "CoA VL BA2026 fonds strong tick678; dual WAL fonds stocks,"
    "5,Departement Financiën en Begroting / openbaarheid Vlaanderen,"
    "openbaarheid@vlaanderen.be,https://www.vlaanderen.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_vl_begrotingsfondsen_856m|cmt_vl_klimaatfonds_cum_deficit_54m|cmt_vl_energiefonds_desaffect_conflict,"
    "lb_vl_begrotingsfondsen_856m_2026|lb_vl_klimaat_cum_deficit_54m|lb_vl_energiefonds_desaffect_conflict,"
    f"{utc},{utc},tick678 CoA VL BA2026 fonds primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_669,"):
        out.append(
            "rq_669,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,sec_ss,"
            "Next residual: VL BA fonds residual CoA 2026_28 or fed nonfiscal SFPIM dual or SS other receipts L5.,,"
            f"2026-08-01T11:00:00Z,{utc},"
            "tick678 VL fonds end 856.5m Klimaat deficit 54 Energie desaffect conflict dual; FOI gap_vl_ba2026_begrotingsfondsen_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_670,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,vlaanderen_gov,"
    "Next residual: fed nonfiscal SFPIM dual CoA 2026_22 or SS other receipts L5 or progress@680 synthesis.,,"
    f"{utc},,spawned tick678 after rq_669"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_669,678,no,"
    "tick678 VL fonds 856.5m Klimaat deficit 54 Energie desaffect 46/56 dual; next rq_670; progress@680 in 2; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Onderzoek aanpassing Vlaamse begroting 2026 (2026_28) §2.2.3 Begrotingsfondsen + §7.1 FB

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: Departement Financiën en Begroting
openbaarheid@vlaanderen.be

Betreft: Openbaarheid — BA2026 begrotingsfondsen (eindsaldo 856,5 mEUR) L5

Geachte,

Op grond van het Bestuursdecreet verzoek ik om:

1. **Tabel begrotingsfondsen** met beginsaldo, ontvangsten, uitgaven,
   desaffectaties en eindsaldo 2024–2026 voor minstens:
   Verkeersveiligheidsfonds, Klimaatfonds, Energiefonds, Fonds Wedden
   Onderwijs, en residuale fondsen (Andere).
2. **Klimaatfonds**: overzicht historische engagementen die het
   gecumuleerd tekort van ca. **54 mEUR** eind 2026 verklaren, naast
   het budgettaire overschot **58,5 mEUR**.
3. **Energiefonds desaffectatie**: reconciliatie art. 32 maximum
   **46,2 mEUR** versus administratieve tabel **56,2 mEUR** (IB **27,8**
   voor energiegere lateerde interestlasten).
4. **Ontbrekende desaffectaties** in middelendecreet-overzicht:
   Fonds ontwikkelingssamenwerking **0,8 mEUR** en Cofinancieringsfonds
   ESF **25,9 mEUR**.
5. **Bufferprovisie +58,5 mEUR**: specialiteiten / artikelen waarop
   deze middelen (zullen) worden aangewend.
6. **Brug** tussen toegewezen ontvangsten algemene toelichting
   (**812,9 mEUR**) en middelendecreet (**866,8 mEUR**), incl. ESR vs
   interne stromen.
7. **Afwijking VCO art. 15 §3**: bedrag toelage aan fonds
   Personeelsleden verlof voor opdracht.

Publieke steun: Rekenhof, *Onderzoek van de aanpassing van de Vlaamse
begroting voor het jaar 2026* (2026_28), juni 2026.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Dual: WAL fonds stocks (Kyoto/déchets/env) class.
- Tick 678.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_669** (FOI-adjacent dual residual — **VL BA2026 begrotingsfondsen Table9–10 dual WAL**)
- Found (primary CoA 2026_28 §2.2.3 + §7.1):
  - **Fonds total:** begin **EUR928.7m** → end **856.5** (−72.2); rec **866.8** exp **−608.6** desaffect **−330.4**; ESA impact **+265.8** (ESR rec 791.9 / exp 526.1)
  - **Verkeersveiligheid** end **180.2** (rec 40 / exp −37.4 / des −2.6); fines est **168.3** (was 202.8; threshold 161.2)
  - **Klimaat** end surplus **58.5** but **cum deficit ~54**; rec **264.5** des **−252.8**; →Energie **+31.6** REG; ICL **194** (−23); auction **+11.7**
  - **Energie** end **257.2** (rec 218.5 = own 166.9 + int 51.6; exp −205.1); desaffect **art32 46.2 vs admin 56.2** (IB 27.8) conflict
  - **Wedden onderwijs** end **93.6** (rec 147 / exp −176.7); Andere end **267**
  - Missing desaffect ODA **0.8** + ESF **25.9**; buffer provisie **+58.5** no specialty; index under **48.3+7.0**
  - Dual WAL fonds stocks. Strong CoA; L5 FOI.
- Wrote: budgets (+50); commitments (+6); leaderboard (+6); sources (+2); entities (+3); FOI draft **gap_vl_ba2026_begrotingsfondsen_l5**; rq_669=done; spawn **rq_670**; loop_state ticks=678
- FOI opened: gap_vl_ba2026_begrotingsfondsen_l5 — ready (not sent)
- Next: rq_670; progress@680 in 2 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick678")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows), "ents", len(new_ents))

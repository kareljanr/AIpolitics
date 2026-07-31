from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 679
utc = "2026-08-01T11:30:00Z"
src = "src_ccrek_fed_aju2026_nonfiscal_sfpim"
src_dual = "src_dual_nonfiscal_sfpim_tick679"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

src_rows = [
    f'{src},CoA federal BA2026 nonfiscal receipts + SFPIM dividend residual dual,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick679: cash total rec 167159 (+2725); fiscal 159310 (+1367); nonfiscal cash table 7849 (+1358) / middelen text 7829 (+1358); middelenbegroting 72644 (+738); afdrachten total 94515 (EU 4745 SS 27953 C&R 59936); nonfiscal ESA-impact 6886 (+1036); refunds RSZ evenwicht +548 RIZIV COVID +187 CREG energy +285 (path 412 no ESA); customs retention 1013.8 (+229.3); license plate delay -42.2 + old concession 4.3; SFPIM dividend 78.4 vs budgeted 55.8 under by 22.6; customs reform nonfisc +112.3 of 25pct retention path"',
    f'{src_dual},Dual fed nonfiscal/SFPIM vs VL Finocas investment holdings,{url},DOGE synthesis CoA fed+VL dual,2026-08-01,synthesis,"Strong dual: SFPIM dividend 78.4 underbooked 22.6 vs VL Finocas capital 177.5 unclear; nonfiscal refunds dual SS; not TE-additive; tick679"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # Cash receipts overview p26
    f"bud_fed_cash_rec_total_167159m_2026,sec_federal,2026,167159000000,,,budgeted,{src},strong,Federal cash receipts total BC2026 167159m (+2725 / +1.6pct vs IB); excl municipal opcentiemen; tick679",
    f"bud_fed_cash_rec_fiscal_159310m_2026,sec_federal,2026,159310000000,,,budgeted,{src},strong,Fiscal cash receipts 159310m (+1367 / +0.9pct); tick679",
    f"bud_fed_cash_rec_nonfiscal_7849m_2026,sec_federal,2026,7849000000,,,budgeted,{src},strong,Nonfiscal cash table BC2026 7849m (+1358 vs IB 6491); CoA T p26; tick679",
    f"bud_fed_cash_rec_ib_164434m_2026,sec_federal,2026,164434000000,,,budgeted,{src},strong,IB2026 total cash receipts 164434m for compare; tick679",
    f"bud_fed_afdrachten_total_94515m_2026,sec_federal,2026,94515000000,,,budgeted,{src},strong,Transfers to other governments 94515m (+1987 / +2.1pct); 56.5pct of total cash rec; tick679",
    f"bud_fed_afdracht_eu_4745m_2026,sec_federal,2026,4745000000,,,budgeted,{src},strong,EU transfers 4745m (+595); tick679",
    f"bud_fed_afdracht_cr_59936m_2026,sec_federal,2026,59936000000,,,budgeted,{src},strong,Regions+communities transfers 59936m (+753); tick679",
    f"bud_fed_afdracht_ss_27953m_2026,sec_federal,2026,27953000000,,,budgeted,{src},strong,SS transfers from federal cash 27953m (+628); dual SS alt finance; tick679",
    f"bud_fed_afdracht_divers_1881m_2026,sec_federal,2026,1881000000,,,budgeted,{src},strong,Diverse afdrachten 1881m (+11); tick679",
    f"bud_fed_middelenbegroting_72644m_2026,sec_federal,2026,72644000000,,,budgeted,{src},strong,Middelenbegroting after transfers 72644m (+738 / +1.0pct; 43.5pct of cash); tick679",
    f"bud_fed_afdracht_nonfiscal_20m_2026,sec_federal,2026,20000000,,,budgeted,{src},strong,Nonfiscal share inside intergovernmental transfers ~20m (rest almost all fiscal); tick679",
    # Nonfiscal middelen detail p33-34
    f"bud_fed_nonfiscal_middelen_7829m_2026,sec_federal,2026,7829000000,,,budgeted,{src},strong,Nonfiscal middelenbegroting text 7829m (+1358 vs IB); CoA p33 (cash table 7849 keep both); tick679",
    f"bud_fed_nonfiscal_esa_6886m_2026,sec_federal,2026,6886000000,,,budgeted,{src},strong,Nonfiscal with ESA saldo impact 6886m (+1036 vs IB); tick679",
    f"bud_fed_nonfiscal_refund_rsz_548m_2026,sec_federal,2026,548000000,,,budgeted,{src},strong,RSZ evenwichtsdotatie refund +548m sect24 (prior-year overpayment); no full ESA clean; tick679",
    f"bud_fed_nonfiscal_refund_riziv_covid_187m_2026,sec_federal,2026,187000000,,,budgeted,{src},strong,RIZIV COVID-19 subsidy refund +187m sect24; tick679",
    f"bud_fed_nonfiscal_refund_creg_285m_2026,sec_federal,2026,285000000,,,budgeted,{src},strong,CREG energy-crisis premium refund +285m sect32 (path up to 412 if suppliers repay); no ESA saldo impact; tick679",
    f"bud_fed_nonfiscal_creg_path_412m_2026,sec_federal,2026,412000000,,,estimate,{src},medium,CREG refund path up to 412m if supplier claims repaid; CoA; tick679",
    f"bud_fed_nonfiscal_refunds_pack_1020m_2026,sec_federal,2026,1020000000,,,budgeted,{src},strong,Refund pack RSZ 548 + RIZIV 187 + CREG 285 = 1020m of nonfiscal uplift; tick679",
    f"bud_fed_customs_retention_1013_8m_2026,sec_federal,2026,1013800000,,,budgeted,{src},strong,Customs collection fee retention 25pct = 1013.8m (+229.3 vs IB); e-comm reform; tick679",
    f"bud_fed_customs_retention_uplift_229_3m_2026,sec_federal,2026,229300000,,,budgeted,{src},strong,Customs retention uplift +229.3m vs IB from tariff reform; tick679",
    f"bud_fed_customs_reform_nonfisc_112_3m_2026,sec_federal,2026,112300000,,,budgeted,{src},strong,Customs reform path: 25pct retention nonfiscal +112.3m of +449 customs (offset EU transfer); CoA p31; tick679",
    f"bud_fed_customs_reform_gross_449m_2026,sec_federal,2026,449000000,,,budgeted,{src},strong,Customs reform gross rights +449m (EU own resources transfer -449); tick679",
    f"bud_fed_customs_handling_fee_77_4m_2026,sec_federal,2026,77400000,,,budgeted,{src},medium,EU handling fee est 77.4m undivided correction (from 1 Nov 2026; law pending); tick679",
    f"bud_fed_license_plate_delay_minus_42_2m_2026,sec_federal,2026,42200000,,,budgeted,{src},strong,License plate/kenteken new contract delay to 2027 cancels 42.2m receipt 2026; tick679",
    f"bud_fed_license_plate_old_concession_4_3m_2026,sec_federal,2026,4300000,,,budgeted,{src},strong,Old license-plate concession receipt reinstated +4.3m 2026; tick679",
    f"bud_fed_license_plate_net_path_minus_37_9m_2026,sec_federal,2026,37900000,,,estimate,{src},strong,Net license-plate path -37.9m (cancel 42.2 + old 4.3); tick679",
    # SFPIM
    f"bud_sfpim_dividend_actual_78_4m_2026,sfpim,2026,78400000,,,budgeted,{src},strong,SFPIM dividend to State actual 78.4m 2026 (CoA); tick679",
    f"bud_sfpim_dividend_budgeted_55_8m_2026,sfpim,2026,55800000,,,budgeted,{src},strong,SFPIM dividend inscribed in aju draft 55.8m (under by 22.6); tick679",
    f"bud_sfpim_dividend_underbook_22_6m_2026,sfpim,2026,22600000,,,budgeted,{src},strong,SFPIM dividend under-budgeted 22.6m (78.4-55.8); CoA correction; tick679",
    # Dual
    f"bud_dual_sfpim_finocas_dividends_2026,gg_belgium,2026,78400000,,,budgeted,{src_dual},strong,Dual SFPIM dividend 78.4 vs VL Finocas capital inject 177.5 unclear class; not TE-additive; tick679",
    f"bud_dual_nonfiscal_esa_6886m_2026,gg_belgium,2026,6886000000,,,budgeted,{src_dual},strong,Dual federal nonfiscal ESA 6.89bn residual; tick679",
    f"bud_fed_nonfiscal_ib_6491m_2026,sec_federal,2026,6491000000,,,budgeted,{src},strong,IB2026 nonfiscal cash 6491m baseline for +1358 path; tick679",
    f"bud_fed_fiscal_ib_157943m_2026,sec_federal,2026,157943000000,,,budgeted,{src},strong,IB2026 fiscal cash 157943m; tick679",
    f"bud_fed_creg_refund_no_esa_note_2026,sec_federal,2026,285000000,,,budgeted,{src},strong,CREG refund no ESA saldo impact (crisis premium clawback); residual note tick679",
    f"bud_fed_rsz_refund_sect24_548m_note,sec_federal,2026,548000000,,,budgeted,{src},strong,RSZ evenwicht refund dual with RSZ-GB deficit settle 547.5 (tick677); tick679",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

cmt_rows = [
    f'cmt_fed_nonfiscal_7829m,Federal nonfiscal middelen 7.83bn dual,sec_federal,State receipts,CoA 2026_22 p33,2026-05-21,2026,2026,7829000000,"{{""middelen"":7829,""cash_table"":7849,""esa"":6886}}",,active,,Nonfiscal dual refunds,L5 line FOI,{src},strong,Fed>receipts>nonfiscal,tick679',
    f'cmt_sfpim_dividend_78_4m,SFPIM dividend 78.4m underbooked 22.6,sfpim,Belgian State,SFPIM board / CoA,2026-05-21,2026,2026,78400000,"{{""actual"":78400000,""budgeted"":55800000}}",,active,,State SOE dividend,Correct middelen,{src},strong,Fed>SFPIM>dividend,tick679',
    f'cmt_customs_retention_1014m,Customs 25pct retention 1.01bn,sec_federal,FOD Fin customs,EU customs reform 2026,2026-05-21,2026,2026,1013800000,"{{""2026"":1013800000}}",,active,,Collection fee,Monitor e-comm shift,{src},strong,Fed>customs>retention,tick679',
    f'cmt_nonfiscal_refunds_1020m,Refund pack RSZ+RIZIV+CREG 1.02bn,sec_federal,RSZ RIZIV CREG,CoA 2026_22 p33,2026-05-21,2026,2026,1020000000,"{{""rsz"":548,""riziv"":187,""creg"":285}}",,active,,Prior-year clawbacks,CREG path 412 FOI,{src},strong,Fed>nonfiscal>refunds,tick679',
    f'cmt_license_plate_delay_2026,License plate contract delay -42.2+4.3,sec_federal,Mobility admin,CoA 2026_22 p34,2026-05-21,2026,2027,42200000,"{{""cancel_2026"":42200000,""old_concession"":4300000}}",,active,,Concession timing,Track 2027 award,{src},strong,Fed>nonfiscal>plates,tick679',
    f'cmt_dual_sfpim_finocas_tick679,Dual SFPIM dividend vs VL Finocas capital,gg_belgium,Fed+VL holdings,CoA dual,2026-05-21,2026,2026,78400000,"{{""sfpim_div"":78400000}}",,active,,Investment dual,Not TE-additive,{src_dual},strong,Belgium>dual>sfpim,tick679',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_fed_nonfiscal_7_83bn_2026,Federal nonfiscal receipts 7.83bn,Federal,ops,Fed>receipts>nonfiscal,7829000000,0,Strong CoA middelen 7829 (+1358); ESA-impact 6886; refund pack 1020,strong,{src},taxpayers,Nonfiscal dual,Primary,5.5,7.5,3,6.15,L5 FOI,open,,tick679",
    f"lb_sfpim_dividend_underbook_22_6m,SFPIM dividend underbooked 22.6m,Federal,ops,Fed>SFPIM>dividend,22600000,0,Strong CoA: actual 78.4 vs inscribed 55.8; easy budget fix,strong,{src},State shareholder,SOE dividend,Primary,7.0,4.0,1,5.80,Correct middelen,open,,tick679",
    f"lb_customs_retention_1_01bn_2026,Customs retention 1.01bn e-comm reform,Federal,ops,Fed>customs>retention,1013800000,0,Strong CoA +229.3 uplift from tariff reform; dual EU transfer,strong,{src},importers,Collection fee,Primary,5.0,7.0,3,5.70,Monitor import shift,open,,tick679",
    f"lb_creg_refund_285m_path_412,CREG crisis refund 285 path 412,Federal,ops,Fed>nonfiscal>CREG,285000000,0,Strong CoA: crisis premium clawback no ESA impact; supplier path 412,strong,{src},energy suppliers,Crisis residual,Primary,6.5,5.5,2,5.95,Supplier claim FOI,open,,tick679",
    f"lb_license_plate_delay_42m_2026,License plate receipt delay 42.2m,Federal,ops,Fed>nonfiscal>plates,42200000,0,Strong CoA: new contract to 2027; old concession +4.3 only,strong,{src},drivers,Concession timing,Primary,6.0,4.0,2,5.20,2027 award FOI,open,,tick679",
    f"lb_dual_sfpim_finocas_2026,Dual SFPIM dividend vs Finocas capital,Belgium,ops,Belgium>dual>sfpim,78400000,0,Strong dual: SFPIM 78.4 underbook vs VL Finocas 177.5 unclear; not TE-additive,strong,{src_dual},all entities,Holdings dual,Primary dual,6.0,5.5,3,5.75,Cross FOI,open,,tick679",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

gap_id = "gap_fed_aju2026_nonfiscal_sfpim_l5"
foi_row = (
    f"{gap_id},Federal>Aju2026>Nonfiscal_SFPIM_L5,sec_federal,"
    "Nonfiscal middelen L5 line list reconciling 7829 vs cash table 7849; ESA vs non-ESA split behind 6886; RSZ 548 settle detail dual GB deficit; RIZIV COVID 187 components; CREG 285 supplier claims path to 412; customs retention monthly 1013.8; license-plate tender calendar; SFPIM dividend 78.4 board decision vs 55.8 budget note,"
    "CoA fed nonfiscal SFPIM strong tick679; dual Finocas,"
    "5,FOD Financiën / FOD BOSA / SFPIM,"
    "openbaarheid@minfin.fed.be,https://finance.belgium.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_fed_nonfiscal_7829m|cmt_sfpim_dividend_78_4m|cmt_nonfiscal_refunds_1020m,"
    "lb_fed_nonfiscal_7_83bn_2026|lb_sfpim_dividend_underbook_22_6m|lb_creg_refund_285m_path_412,"
    f"{utc},{utc},tick679 CoA fed nonfiscal primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_670,"):
        out.append(
            "rq_670,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,vlaanderen_gov,"
            "Next residual: fed nonfiscal SFPIM dual CoA 2026_22 or SS other receipts L5 or progress@680 synthesis.,,"
            f"2026-08-01T11:15:00Z,{utc},"
            "tick679 nonfiscal 7.83bn SFPIM div 78.4 under 22.6 customs 1.01bn dual; FOI gap_fed_aju2026_nonfiscal_sfpim_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_671,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,sec_federal,"
    "PROGRESS@680: refresh progress_every_10_ticks.md + doge_waste_top10_current.md; synthesize residual wave ticks671-679 dual fed/VL; spawn next hole-fill.,,"
    f"{utc},,spawned tick679 after rq_670; progress milestone next"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_670,679,no,"
    "tick679 nonfiscal 7.83bn SFPIM 78.4 under 22.6 customs 1.01bn dual; next rq_671 PROGRESS@680; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22) Deel II Ch I §3 Niet-fiscale ontvangsten

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: FOD Financiën / FOD BOSA
Cc: SFPIM
openbaarheid@minfin.fed.be

Betreft: Openbaarheid — aju 2026 niet-fiscale ontvangsten (~7,8 mld) + SFPIM-dividend L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. **Reconciliatie** niet-fiscale ontvangsten kasbasis-tabel (**7.849 mEUR**)
   versus middelenbegrotingstekst (**7.829 mEUR**) en uitsplitsing ESR-
   impact (**6.886 mEUR**) versus niet-ESR.
2. **Terugbetalingen**: RSZ evenwichtsdotatie **+548 mEUR** (sectie 24) —
   methodenota en link met afrekening Globaal Beheer 2025; RIZIV COVID
   **+187 mEUR** componenten; CREG energiepremies **+285 mEUR** en pad
   tot **412 mEUR** (leveranciersvorderingen).
3. **Douane inningsvergoeding 25 %**: cash **1.013,8 mEUR** (+229,3) —
   maandreeks en impact e-commercehervorming.
4. **Nummerplaten**: planning overheidsopdracht (uitstel 2027, −42,2) en
   ontvangsten oude concessie (+4,3).
5. **SFPIM-dividend**: beslissing / akte **78,4 mEUR** versus ingeschreven
   **55,8 mEUR** (−22,6 te laag) en correctie in middelenbegroting.

Publieke steun: Rekenhof, *Commentaar … staatsbegroting 2026* (2026_22),
Deel II, Hoofdstuk I Ontvangsten — Niet-fiscale ontvangsten.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Dual: VL Finocas capital opacity (tick671/678).
- Tick 679.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_670** (FOI-adjacent dual residual — **federal CoA BA2026 nonfiscal + SFPIM dividend dual Finocas**)
- Found (primary CoA 2026_22 Deel II Ch I):
  - **Cash total EUR167.159bn** (+2.725): fiscal **159.310** (+1.367) · nonfiscal table **7.849** (+1.358) · middelen text **7.829**
  - **Afdrachten EUR94.515bn** (EU **4.745** · C&R **59.936** · SS **27.953**); middelenbegroting **72.644**
  - **ESA nonfiscal 6.886** (+1.036); refunds RSZ **+548** · RIZIV COVID **+187** · CREG **+285** (path **412** no ESA)
  - **Customs retention 1.013.8** (+229.3); reform path +112.3 of 25pct; handling fee **77.4** pending
  - **License plates:** delay −**42.2** + old concession **+4.3**
  - **SFPIM dividend 78.4** vs budgeted **55.8** under **22.6**
  - Dual VL Finocas. Strong CoA; L5 FOI.
- Wrote: budgets (+35); commitments (+6); leaderboard (+6); sources (+2); FOI draft **gap_fed_aju2026_nonfiscal_sfpim_l5**; rq_670=done; spawn **rq_671** (PROGRESS@680); loop_state ticks=679
- FOI opened: gap_fed_aju2026_nonfiscal_sfpim_l5 — ready (not sent)
- Next: **rq_671 PROGRESS@680**; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick679")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows))

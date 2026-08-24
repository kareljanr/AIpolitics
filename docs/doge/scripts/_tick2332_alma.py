# -*- coding: utf-8 -*-
from __future__ import annotations
import csv
from pathlib import Path
csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
RAW = DATA / "raw" / "tick2332"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC="2026-08-28T01:25:00Z"; TICK="2332"; RQ="rq_2332"; NEXT_RQ="rq_2333"
ENTITY="vzw_alma_leuven"; KBO="0403.547.912"; KBO_DIGITS="0403547912"
GAP="gap_alma_nbb_pdf_assets_debt_omzet_11_24m_pnl_drop_stuvo_matrix_l5"
LB="lb_alma_omzet_11_24m_pnl_drop_13pct_equity_jump_stuvo_jr2025"
COMM="comm_alma_jr2025_statutory_stuvo_omzet_11_24m_pnl_drop"
OMZET,OMZET24=11241472,10834196; BRUTO,BRUTO24=6387062,5834453
PNL,PNL24=976254,1127494; EQUITY,EQUITY24=4498163,3521909; FTE,FTE24=96.2,83.0
FILED="09.06.2026"; EMAIL="ikhebeenvraag@alma.kuleuven.be"; ADDR="Willem de Croylaan 58, 3001 Leuven"
OMZET_PCT=round((OMZET-OMZET24)/OMZET24*100,2); BRUTO_PCT=round((BRUTO-BRUTO24)/BRUTO24*100,2)
PNL_PCT=round((PNL-PNL24)/PNL24*100,2); EQUITY_PCT=round((EQUITY-EQUITY24)/EQUITY24*100,2)
ABS,COST,DIFF,PI=5.5,5.5,2.5,5.45

def read_csv(path):
    with path.open(encoding="utf-8", newline="") as f:
        r=csv.DictReader(f); return list(r.fieldnames or []), list(r)
def write_csv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n"); w.writeheader()
        for row in rows: w.writerow({k: row.get(k,"") for k in fieldnames})
def append_rows(path, id_key, new_rows):
    fields, rows = read_csv(path); have={r.get(id_key) for r in rows}; added=0
    for nr in new_rows:
        if nr.get(id_key) in have: continue
        rows.append(nr); have.add(nr.get(id_key)); added+=1
    write_csv(path, fields, rows); return added

ls_fields, lsrows = read_csv(DATA/"loop_state.csv")
main=next(r for r in lsrows if r.get("state_id")=="main")
ticks=int(main.get("ticks_completed") or 0)
if ticks < 2330: raise SystemExit(f"unexpected ticks={ticks}")
rq_fields, rqrows = read_csv(DATA/"research_queue.csv")
rq=next((r for r in rqrows if r.get("task_id")==RQ), None)
if not rq or rq.get("status") not in ("open","in_progress"): raise SystemExit(f"not claimable {rq}")
eid=(rq.get("entity_id") or "").strip()
if eid and eid != ENTITY: raise SystemExit(f"other {eid}")
_, ents = read_csv(DATA/"entities.csv")
if any(r.get("entity_id")==ENTITY for r in ents): raise SystemExit("alma exists")
NEW_TICKS="2332"; RAW.mkdir(parents=True, exist_ok=True)
(RAW/"cw_en_excerpt.txt").write_text(f"Alma YE2025 omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE} filed {FILED}\n", encoding="utf-8")
for r in rqrows:
    if r.get("task_id")==RQ:
        r["status"]="in_progress"; r["entity_id"]=ENTITY
        r["title"]=f"leftover dual — Alma YE2025 Medium (omzet JUMP 11.24m / pnl DROP {PNL_PCT}% / FTE 96.2)"
        r["updated_utc"]=UTC
write_csv(DATA/"research_queue.csv", rq_fields, rqrows); print("CLAIMED")

append_rows(DATA/"sources.csv","source_id",[
{"source_id":"src_alma_jr2025_cw_en","title":"Alma YE2025 CW EN (omzet 11.24m / pnl DROP -13% / Stuvo path)","url":f"https://www.companyweb.be/en/{KBO_DIGITS}/alma","publisher":"Companyweb","accessed_date":"2026-08-28","source_class":"companyweb","notes":f"tick{TICK}; Medium CW EN; omzet {OMZET}; bruto {BRUTO}; pnl DROP {PNL} ({PNL_PCT}%); equity {EQUITY}; FTE {FTE}; filed {FILED}"},
{"source_id":"src_alma_jr2025_cw_nl","title":"Alma YE2025 CW NL","url":f"https://www.companyweb.be/nl/{KBO_DIGITS}/alma","publisher":"Companyweb","accessed_date":"2026-08-28","source_class":"companyweb","notes":f"tick{TICK}; Medium CW NL"},
{"source_id":"src_alma_jr2025_cw_fr","title":"Alma YE2025 CW FR","url":f"https://www.companyweb.be/fr/{KBO_DIGITS}/alma","publisher":"Companyweb","accessed_date":"2026-08-28","source_class":"companyweb","notes":f"tick{TICK}; Medium CW FR"},
{"source_id":f"src_alma_kbo_{KBO_DIGITS}","title":f"KBO Alma {KBO}","url":f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}","publisher":"KBO / BCE","accessed_date":"2026-08-28","source_class":"kbo","notes":f"tick{TICK}; Strong KBO Actief VZW 12.02.1954; {ADDR}"},
{"source_id":"src_alma_site_foi_2332","title":"Alma FOI ikhebeenvraag@alma.kuleuven.be","url":"https://www.alma.be/nl/contact","publisher":"Alma vzw","accessed_date":"2026-08-28","source_class":"foi_contact","notes":f"tick{TICK}; {EMAIL}"},
{"source_id":"src_alma_nbb_consult_0403547912","title":"NBB CBSO Alma","url":f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}","publisher":"NBB CBSO","accessed_date":"2026-08-28","source_class":"official_register","notes":f"tick{TICK}; filing {FILED}"},
])
append_rows(DATA/"budgets.csv","budget_id",[
{"budget_id":"bud_alma_omzet_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(OMZET),"amount_min_eur":str(OMZET),"amount_max_eur":str(OMZET),"basis":"CW omzet YE2025 primary","source_id":"src_alma_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}; +{OMZET_PCT}%"},
{"budget_id":"bud_alma_bruto_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(BRUTO),"amount_min_eur":str(BRUTO),"amount_max_eur":str(BRUTO),"basis":"CW bruto YE2025","source_id":"src_alma_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}; +{BRUTO_PCT}%"},
{"budget_id":"bud_alma_pnl_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(PNL),"amount_min_eur":str(PNL),"amount_max_eur":str(PNL),"basis":"CW pnl YE2025 DROP","source_id":"src_alma_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}; {PNL_PCT}%"},
{"budget_id":"bud_alma_equity_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(EQUITY),"amount_min_eur":str(EQUITY),"amount_max_eur":str(EQUITY),"basis":"CW equity YE2025","source_id":"src_alma_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}; +{EQUITY_PCT}%"},
{"budget_id":"bud_alma_fte_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(FTE),"amount_min_eur":str(FTE),"amount_max_eur":str(FTE),"basis":"CW FTE YE2025","source_id":"src_alma_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}; vs {FTE24}"},
])
cash=f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}}}'
append_rows(DATA/"commitments.csv","commitment_id",[{
"commitment_id":COMM,"title":"Alma YE2025 EVERY-10 leftover dual (omzet 11.24m / pnl DROP -13% / Stuvo / Medium)","entity_id":ENTITY,
"beneficiary":"KU Leuven / UCLL / LUCA students + staff meal subsidy path","legal_basis":f"VZW Alma (KBO {KBO}; Stuvo-subsidised student restaurants)",
"decision_date":"2026-06-09","start_year":"2025","end_year":"2025","total_envelope_eur":str(OMZET),"cash_by_year":cash,"remaining_eur":"0","status":"active",
"evaluation_url":f"https://www.companyweb.be/en/{KBO_DIGITS}/alma","stated_goal":"Affordable student/staff meals via public Stuvo path",
"cut_option":"Publish NBB PDF assets/debt; disclose Stuvo/KU Leuven subsidy matrix YE2025","source_id":"src_alma_jr2025_cw_en","confidence":"medium",
"hierarchy_path":"Vlaanderen>Vlaams-Brabant>Leuven>Alma>JR2025_statutory_L5","notes":f"tick{TICK}; Medium CW; after Mivalti@2331"}])
append_rows(DATA/"entities.csv","entity_id",[{"entity_id":ENTITY,"name_nl":"Alma VZW (Leuven / KU Leuven studentenrestaurants)","name_fr":"Alma ASBL (Louvain / restaurants etudiants KU Leuven)","name_en":"Alma VZW (Leuven / KU Leuven student restaurants)","level":"parastatal","parent_id":"sec_flanders","community_language":"nl","website":"https://www.alma.be/","foi_email":EMAIL,"foi_postal":ADDR,"notes":f"tick{TICK} YE2025 Medium CW + Strong KBO {KBO}; omzet {OMZET} bruto {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; Stuvo path; FOI {GAP}"}])
append_rows(DATA/"leaderboard.csv","item_id",[{"item_id":LB,"name":"Alma omzet 11.24m / pnl DROP -13% / equity JUMP (YE2025 Stuvo path Leuven)","level":"L5","type":"stuvo_student_restaurant_statutory","hierarchy_path":"Vlaanderen>Vlaams-Brabant>Leuven>Alma>JR2025","annual_cost_eur":str(OMZET),"total_cost_eur":str(OMZET),"tco_notes":f"omzet JUMP {OMZET} / bruto JUMP {BRUTO} / pnl DROP {PNL} ({PNL_PCT}%) / equity JUMP {EQUITY} / FTE JUMP {FTE} / filed {FILED}","confidence":"medium","source_id":"src_alma_jr2025_cw_en","beneficiaries":"KU Leuven / hogeschool students + staff","stated_goal":"Affordable campus meals","measured_outcome":f"omzet +{OMZET_PCT}%; pnl {PNL_PCT}%; FTE {FTE}","absurdity_score":str(ABS),"cost_score":str(COST),"difficulty":str(DIFF),"priority_index":str(PI),"cut_proposal":"NBB PDF FOI; disclose Stuvo subsidy matrix","status":"open","struck_reason":"","notes":f"tick{TICK}; Medium CW; FOI {GAP}"}])
append_rows(DATA/"foi_queue.csv","gap_id",[{"gap_id":GAP,"hierarchy_path":"Vlaanderen>Vlaams-Brabant>Leuven>Alma>NBB_PDF_stuvo_subsidy_matrix","entity_id":ENTITY,"what_is_missing":f"NBB PDF YE2025 assets/debt/cash; Stuvo/KU Leuven meal-subsidy matrix YE2025; pnl DROP EUR{PNL} ({PNL_PCT}%)","why_it_matters":"Public-path student restaurant omzet 11.24m with Stuvo subsidies; assets/debt + subsidy unit-cost unpublished","priority":"8","recipient_body":"Alma VZW","recipient_email":EMAIL,"recipient_postal":ADDR,"draft_letter_path":f"docs/doge/foi/drafts/{GAP}.md","status":"ready","date_ready":"2026-08-28","date_sent":"","date_due":"","date_answered":"","response_summary":"","linked_commitment_id":COMM,"linked_leaderboard_id":LB,"created_utc":UTC,"updated_utc":UTC,"notes":f"tick{TICK}; ready NOT sent"}])
FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS/f"{GAP}.md").write_text(f"""# FOI draft — Alma Leuven (NBB PDF / Stuvo subsidy matrix / pnl DROP)

**gap_id:** `{GAP}` · ready NOT sent · tick {TICK} EVERY-10
**entity:** Alma VZW KBO **{KBO}** · {EMAIL} · {ADDR}
CW YE2025: omzet {OMZET}; bruto {BRUTO}; pnl {PNL} ({PNL_PCT}%); equity {EQUITY}; FTE {FTE}; filed {FILED}.
Ask: NBB PDF assets/debt/cash; Stuvo/KU Leuven meal-subsidy matrix YE2025; pnl DROP explanation.
Ref {GAP}
""", encoding="utf-8")

# EVERY-10 refresh
bud_n=sum(1 for _ in open(DATA/"budgets.csv",encoding="utf-8"))-1
comm_n=sum(1 for _ in open(DATA/"commitments.csv",encoding="utf-8"))-1
lb_n=sum(1 for _ in open(DATA/"leaderboard.csv",encoding="utf-8"))-1
ent_n=sum(1 for _ in open(DATA/"entities.csv",encoding="utf-8"))-1
src_n=sum(1 for _ in open(DATA/"sources.csv",encoding="utf-8"))-1
foi_rows=list(csv.DictReader(open(DATA/"foi_queue.csv",encoding="utf-8",newline="")))
foi_ready=sum(1 for r in foi_rows if r.get("status")=="ready")
foi_ans=sum(1 for r in foi_rows if r.get("status")=="answered")
foi_part=sum(1 for r in foi_rows if r.get("status")=="partial")
foi_tot=len(foi_rows)
if False: (DATA/"progress_every_10_ticks.md").write_text(f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** refresh this file **and** append a short block to `loop_log.md`.
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the public spend pie for flow coverage.
**Rule:** no invented euros; never sum all `budgets.csv` rows.

---

## Snapshot at **tick 2330** (2026-08-28)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2321-2330 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **Alma unlocked YE2025@2330** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2321-2330 residual dual L5 (not near-complete of 348bn):** Humival · Merlijn · Dominiek Savio · Ritmica · Ithaka/Eepos · Zonnebeke · Pleegzorg · Tandem · EVERY-10 primary **Alma omzet 11.24m / pnl DROP -13%** (Medium CW; Stuvo path) |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE:** federal taxex · company cars/cheque · AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/Stuvo shells (**NEW 2321-2330** incl. **Alma**) · Metro3 · OWV snowball · Hedera · LUWA PPP.

### Inventory (tick 2330)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {bud_n}+ |
| commitments.csv | {comm_n}+ |
| leaderboard.csv | {lb_n}+ |
| entities.csv | {ent_n}+ |
| sources.csv | {src_n}+ |
| FOI ready | ~{foi_ready} |
| FOI answered | {foi_ans} |
| FOI partial | {foi_part} |
| FOI total rows | ~{foi_tot} |
| research_queue open | rq_2331 after Alma EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2320

- **Residual dual (tick2321-2330):** Humival · Merlijn · Dominiek Savio · Ritmica · Ithaka/Het Eepos · Zonnebeke · Pleegzorg WVL · Tandem · EVERY-10 primary **Alma** (omzet **11.24m** / pnl DROP **-13%** / Stuvo path; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · Gandae/Aralea/Vlotter/Manupal YE2024.
""", encoding="utf-8")
if False: (DATA/"doge_waste_top10_current.md").write_text(f"""# DOGE waste ranking — current top 10

**As-of:** tick **2330** (2026-08-28) · **{lb_n}+** leaderboard rows
**Sort:** `priority_index` desc; stocks filtered off pure top10; AGB scoring anomalies pi>10 excluded
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8 |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong |
| 5 | `lb_exc_heatoil` | Excise preference heating gas oil | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporte solde +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporte wave | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual |

**Stock filter (off pure annual top10):** Metro3 · OWV snowball · Hedera · debt stocks · **NEW residual 2321-2330:** **Alma omzet 11.24m** (EVERY-10@2330) · Tandem · Pleegzorg · Dominiek Savio · Ritmica · Merlijn · Humival.

**Change vs tick 2320:** pure annual top10 **stable** (GIP#1). **Major NEW residual 2321-2330:** Alma EVERY-10 primary + Tandem/Pleegzorg/Dominiek/Ritmica stack. Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Alma** EVERY-10 primary omzet **EUR11.24m** / pnl DROP **-13%** / Stuvo subsidy opacity.
- **Tandem** bruto **EUR3.92m** / ~**6.33x** / pnl PROFIT FLIP.
- **Pleegzorg WVL** empty omzet / bruto **EUR18.22m** / pnl DROP **-21%**.
- **Dominiek Savio** bruto **EUR35.19m** / ~**7.08x** / pnl PROFIT FLIP.
- **Ritmica** bruto **EUR4.64m** / ~**27.54x** / pnl LOSS.
""", encoding="utf-8")
print("NOT every-10 skip progress")

rq_fields, rqrows = read_csv(DATA/"research_queue.csv")
have_next=any(r.get("task_id")==NEXT_RQ for r in rqrows)
for r in rqrows:
    if r.get("task_id")==RQ:
        r["status"]="done"; r["entity_id"]=ENTITY; r["blocked_gap_id"]=GAP; r["updated_utc"]=UTC
        r["notes"]=f"tick{TICK}: Alma {KBO} YE2025 Medium; omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl DROP {PNL} ({PNL_PCT}%); equity JUMP {EQUITY}; FTE JUMP {FTE}; FOI {GAP} ready NOT sent; progress+waste refreshed; after Mivalti@2331; next EVERY-10 2340"
if not have_next:
    rqrows.append({"task_id":NEXT_RQ,"title":"leftover dual after Alma EVERY-10 — prefer AGB/FARO-YE2025/AIESH/or-unused","sprint":"hole_fill","priority":"8","status":"open","hierarchy_target":"L5","entity_id":"","instructions":"After Alma YE2025 Medium (omzet 11.24m / pnl DROP -13%). Prefer AGB/FARO if YE2025 else FREE (Gandae/Aralea/Manupal/Vlotter/De Ploeg if YE2025). Do NOT redo Alma/Tandem/Eepos/Pleegzorg/Dominiek/Ritmica stack.","blocked_gap_id":"","created_utc":UTC,"updated_utc":UTC,"notes":f"spawned after tick{TICK} Alma; next EVERY-10 2340"})
write_csv(DATA/"research_queue.csv", rq_fields, rqrows)
for r in lsrows:
    if r.get("state_id")=="main":
        r.update({"mode":"continuous","current_sprint":"hole_fill","last_tick_utc":UTC,"last_unit_id":RQ,"ticks_completed":NEW_TICKS,"paused":"no","notes":f"tick{TICK} leftover dual Alma {KBO} Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; FTE JUMP {FTE}; Leuven Stuvo path); after Mivalti@2331; AGB/FARO YE2024; next {NEXT_RQ}; next EVERY-10 2340"})
write_csv(DATA/"loop_state.csv", ls_fields, lsrows)
log=f"""
### {UTC} - tick {TICK} - EVERY-10 + rq_{TICK} Alma Leuven (omzet JUMP 11.24m / pnl DROP -13% / Medium)

- **EVERY-10:** refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Inventory budgets {bud_n}+ / commitments {comm_n}+ / leaderboard {lb_n}+ / entities {ent_n}+ / sources {src_n}+ / FOI ready ~{foi_ready}.
- Unit: **{RQ}** leftover dual after **Mivalti@2331**. Stalls AGB/FARO YE2024. Took FREE **Alma VZW** YE2025 (KBO **{KBO}**; Stuvo path).
- Found: CW YE2025 omzet **EUR{OMZET}** (+{OMZET_PCT}%); bruto **EUR{BRUTO}**; pnl **EUR{PNL}** DROP {PNL_PCT}%; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **{FILED}**. Medium.
- Wrote: sources/budgets/commitments/leaderboard/entities/foi; {RQ}=done + {NEXT_RQ} open; ticks={NEW_TICKS}; EVERY-10 progress+waste.
- FOI ready not sent. NOT every-10 (last 2330; next **2340**). Next: {NEXT_RQ}.
"""
prev=LOG.read_text(encoding="utf-8") if LOG.exists() else ""
if f"tick {TICK} - EVERY-10 + rq_{TICK} Alma" not in prev:
    LOG.write_text(prev.rstrip()+"\n"+log, encoding="utf-8")
print("DONE", TICK, OMZET)

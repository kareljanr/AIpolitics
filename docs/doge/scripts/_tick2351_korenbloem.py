# -*- coding: utf-8 -*-
from __future__ import annotations
import csv, json, sys, time
from pathlib import Path
csv.field_size_limit(sys.maxsize)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs/doge/data"
FOI = ROOT / "docs/doge/foi/drafts"
LOG = ROOT / "docs/doge/loop_log.md"
TICK="2351"; RQ="rq_2351"; RQ_NEXT="rq_2352"
EID="vzw_de_korenbloem_kortrijk"; KBO="0418.825.412"; KBO_NUM="0418825412"
OMZET=12564145; BRUTO=12311379; PNL=-360537; EQUITY=8688763; FTE=175.9
OMZET24=12291695; BRUTO24=12290405; PNL24=73799; EQUITY24=9136438; FTE24=172.7
RATIO=round(BRUTO/OMZET,2)
FILED="03.06.2026"; ADDR="Pieter de Conincklaan 12, 8500 Kortrijk"
EMAIL="info@dekorenbloem.net"; SITE="https://www.dekorenbloem.net"
GAP="gap_korenbloem_nbb_pdf_assets_debt_omzet_12_56m_pnl_loss_flip_wzc_matrix_l5"
UTC="2026-08-24T20:00:00Z"
COST=5.5; ABS=7.5; DIFF=5
PI=round(0.55*COST+0.35*ABS+0.10*(10-DIFF),2)

def read_csv(path):
    for _ in range(30):
        try:
            with path.open(encoding="utf-8", newline="") as f:
                r=csv.DictReader(f); return list(r.fieldnames or []), list(r)
        except (PermissionError, FileNotFoundError): time.sleep(0.4)
    raise RuntimeError("read")

def atomic_write(path, fields, rows):
    tmp=path.with_name(path.name+".__n2351__"); bak=path.with_name(path.name+".__b2351__")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader()
        for row in rows: w.writerow({k: row.get(k,"") for k in fields})
    for _ in range(50):
        try:
            if bak.exists():
                try: bak.unlink()
                except: pass
            if path.exists(): path.replace(bak)
            tmp.replace(path)
            try:
                if bak.exists(): bak.unlink()
            except: pass
            return
        except (PermissionError, FileNotFoundError, OSError): time.sleep(0.5)
    raise RuntimeError("atomic")

def append_rows(path, new_rows, id_key=None):
    fields, rows = read_csv(path)
    have={r.get(id_key) for r in rows} if id_key else set()
    added=0
    for nr in new_rows:
        if id_key and nr.get(id_key) in have: continue
        rows.append(nr); added+=1
    if added: atomic_write(path, fields, rows)
    return added

fields, rq = read_csv(DATA/"research_queue.csv")
for r in rq:
    if r.get("task_id")==RQ:
        eid=r.get("entity_id") or ""; st=r.get("status")
        if st=="done" and eid and eid!=EID: print("RACE done",eid); sys.exit(2)
        if st=="in_progress" and eid and eid!=EID: print("RACE ip",eid); sys.exit(3)
        if st=="done" and eid==EID: print("ALREADY done same"); sys.exit(0)
        r["status"]="in_progress"; r["entity_id"]=EID; r["updated_utc"]=UTC
        r["notes"]=(r.get("notes") or "")+f"; tick{TICK} CLAIM De Korenbloem"
        atomic_write(DATA/"research_queue.csv", fields, rq)
        print("CLAIMED", EID)
        break
else:
    print("missing", RQ); sys.exit(4)

_, ents = read_csv(DATA/"entities.csv")
if any(e.get("entity_id")==EID for e in ents):
    print("ALREADY mined", EID); sys.exit(5)

src="src_korenbloem_jr2025_cw_en"
append_rows(DATA/"sources.csv", [
 {"source_id":"src_korenbloem_jr2025_cw_nl","title":"Companyweb NL De Korenbloem YE2025","url":f"https://www.companyweb.be/nl/{KBO_NUM}/de-korenbloem","publisher":"Companyweb (NBB-derived)","accessed_date":"2026-08-24","source_class":"secondary_aggregator","notes":f"tick{TICK}; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed {FILED}"},
 {"source_id":src,"title":"Companyweb EN De Korenbloem YE2025","url":f"https://www.companyweb.be/en/{KBO_NUM}/de-korenbloem","publisher":"Companyweb (NBB-derived)","accessed_date":"2026-08-24","source_class":"secondary_aggregator","notes":f"tick{TICK}; EN Medium"},
 {"source_id":"src_korenbloem_jr2025_cw_fr","title":"Companyweb FR De Korenbloem YE2025","url":f"https://www.companyweb.be/fr/{KBO_NUM}/de-korenbloem","publisher":"Companyweb (NBB-derived)","accessed_date":"2026-08-24","source_class":"secondary_aggregator","notes":f"tick{TICK}; FR mirror"},
 {"source_id":f"src_korenbloem_kbo_{TICK}","title":f"KBO De Korenbloem {KBO}","url":f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_NUM}","publisher":"KBO FOD Economie","accessed_date":"2026-08-24","source_class":"official_register","notes":f"tick{TICK}; Strong KBO Actief 1 VE Aanbestedende RSZ 87.101"},
 {"source_id":f"src_korenbloem_site_{TICK}","title":"De Korenbloem FOI info@dekorenbloem.net","url":SITE,"publisher":"De Korenbloem VZW","accessed_date":"2026-08-24","source_class":"foi_contact","notes":f"tick{TICK}; {EMAIL}; {ADDR}"},
], "source_id")
append_rows(DATA/"budgets.csv", [
 {"budget_id":"bud_korenbloem_omzet_jr2025_statutory","entity_id":EID,"year":"2025","amount_eur":str(OMZET),"amount_min_eur":str(OMZET),"amount_max_eur":str(OMZET),"basis":"CW statutory omzet YE2025 JUMP","source_id":src,"confidence":"medium","notes":f"tick{TICK}; +2.22% vs {OMZET24}"},
 {"budget_id":"bud_korenbloem_bruto_jr2025_statutory","entity_id":EID,"year":"2025","amount_eur":str(BRUTO),"amount_min_eur":str(BRUTO),"amount_max_eur":str(BRUTO),"basis":f"CW statutory bruto_marge YE2025 ~{RATIO}x","source_id":src,"confidence":"medium","notes":f"tick{TICK}"},
 {"budget_id":"bud_korenbloem_pnl_jr2025_statutory","entity_id":EID,"year":"2025","amount_eur":str(PNL),"amount_min_eur":str(PNL),"amount_max_eur":str(PNL),"basis":"CW statutory winst/verlies YE2025 LOSS FLIP","source_id":src,"confidence":"medium","notes":f"tick{TICK}; LOSS FLIP vs {PNL24}"},
 {"budget_id":"bud_korenbloem_equity_jr2025_statutory","entity_id":EID,"year":"2025","amount_eur":str(EQUITY),"amount_min_eur":str(EQUITY),"amount_max_eur":str(EQUITY),"basis":"CW statutory eigen_vermogen YE2025 DROP","source_id":src,"confidence":"medium","notes":f"tick{TICK}"},
 {"budget_id":"bud_korenbloem_fte_jr2025_statutory","entity_id":EID,"year":"2025","amount_eur":str(FTE),"amount_min_eur":str(FTE),"amount_max_eur":str(FTE),"basis":f"CW FTE {FTE} JUMP","source_id":src,"confidence":"medium","notes":f"tick{TICK}"},
], "budget_id")
cash={"2025_omzet":OMZET,"2025_bruto":BRUTO,"2025_pnl":PNL,"2025_equity":EQUITY,"2025_fte":FTE,"2024_omzet":OMZET24,"2024_bruto":BRUTO24,"2024_pnl":PNL24,"2024_equity":EQUITY24,"2024_fte":FTE24}
append_rows(DATA/"commitments.csv", [{
 "commitment_id":"comm_korenbloem_jr2025_statutory_omzet_12_56m_pnl_loss_flip_wzc",
 "title":f"De Korenbloem YE2025 leftover dual (omzet JUMP 12.56m / pnl LOSS FLIP / FTE 175.9 / Medium)",
 "entity_id":EID,"beneficiary":"WZC residents Kortrijk / jongdementie + ouderen",
 "legal_basis":f"VZW De Korenbloem (KBO {KBO}; Actief; Aanbestedende; RSZ 87.101; 1 VE)",
 "decision_date":"2026-06-03","start_year":"2025","end_year":"2025","total_envelope_eur":str(OMZET),
 "cash_by_year":json.dumps(cash,separators=(",",":")),"remaining_eur":"0","status":"active",
 "evaluation_url":f"https://www.companyweb.be/en/{KBO_NUM}/de-korenbloem",
 "stated_goal":"Residential nursing home / RVT + jongdementie Kortrijk",
 "cut_option":"Publish NBB PDF assets/debt; explain pnl LOSS FLIP at omzet 12.56m",
 "source_id":src,"confidence":"medium",
 "hierarchy_path":"Vlaanderen>WestVlaanderen>Kortrijk>De_Korenbloem_WZC>JR2025_statutory_L5",
 "notes":f"tick{TICK}; Medium CW; after Leieborg@2350; not TE-additive",
}], "commitment_id")
append_rows(DATA/"leaderboard.csv", [{
 "item_id":"lb_korenbloem_omzet_12_56m_pnl_loss_flip_fte_jump_jr2025",
 "name":f"De Korenbloem omzet JUMP 12.56m / pnl LOSS FLIP / FTE JUMP 175.9 (YE2025 WZC Kortrijk)",
 "level":"L5","type":"wzc_rvt_vzw_statutory",
 "hierarchy_path":"Vlaanderen>WestVlaanderen>Kortrijk>De_Korenbloem>JR2025",
 "annual_cost_eur":str(OMZET),"total_cost_eur":str(OMZET),
 "tco_notes":f"CW omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE JUMP {FTE}; filed {FILED}",
 "confidence":"medium","source_id":src,"beneficiaries":"WZC residents Kortrijk incl. jongdementie",
 "stated_goal":"Residential nursing home RVT","measured_outcome":"Unknown assets/debt",
 "absurdity_score":str(ABS),"cost_score":str(COST),"difficulty":str(DIFF),"priority_index":str(PI),
 "cut_proposal":"FOI NBB PDF + LOSS FLIP path + Zorgkas/public subsidy matrix","status":"active","struck_reason":"",
 "notes":f"tick{TICK}; Medium CW + Strong KBO; AGB/FARO YE2024",
}], "item_id")
append_rows(DATA/"entities.csv", [{
 "entity_id":EID,"name_nl":"De Korenbloem VZW (Kortrijk / WZC RVT)","name_fr":"De Korenbloem ASBL (Courtrai / MRS RVT)",
 "name_en":"De Korenbloem VZW (Kortrijk / nursing home RVT)","level":"parastatal","parent_id":"sec_flanders",
 "community_language":"nl","website":SITE,"foi_email":EMAIL,"foi_postal":ADDR,
 "notes":f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE Aanbestedende RSZ 87.101; omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE JUMP {FTE}; neerlegging {FILED}; FOI {GAP}; after Leieborg@2350; AGB/FARO YE2024",
}], "entity_id")
append_rows(DATA/"foi_queue.csv", [{
 "gap_id":GAP,"hierarchy_path":"Vlaanderen>WestVlaanderen>Kortrijk>De_Korenbloem>NBB_PDF","entity_id":EID,
 "what_is_missing":f"NBB PDF YE2025 assets/debt/cash; why pnl LOSS FLIP EUR{PNL} at omzet EUR{OMZET}; Zorgkas/public subsidy vs omzet; FTE JUMP to {FTE}",
 "why_it_matters":f"Medium CW WZC Kortrijk omzet 12.56m with LOSS FLIP from profit; assets/debt unknown",
 "priority":"8","recipient_body":"De Korenbloem VZW","recipient_email":EMAIL,"recipient_postal":ADDR,
 "draft_letter_path":f"docs/doge/foi/drafts/{GAP}.md","status":"ready","date_ready":"2026-08-24",
 "date_sent":"","date_due":"","date_answered":"","response_summary":"",
 "linked_commitment_id":"comm_korenbloem_jr2025_statutory_omzet_12_56m_pnl_loss_flip_wzc",
 "linked_leaderboard_id":"lb_korenbloem_omzet_12_56m_pnl_loss_flip_fte_jump_jr2025",
 "created_utc":UTC,"updated_utc":UTC,"notes":f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO",
}], "gap_id")
FOI.mkdir(parents=True, exist_ok=True)
(FOI/f"{GAP}.md").write_text(f"""# FOI draft — De Korenbloem Kortrijk (omzet 12.56m / pnl LOSS FLIP)

**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}  
**entity:** De Korenbloem VZW — KBO **{KBO}** (Actief; {ADDR}; FTE {FTE}; RSZ **87.101** RVT; 1 VE Aanbestedende)  
**recipient:** {EMAIL}

## Brief
```text
Aan: De Korenbloem VZW via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 De Korenbloem (KBO {KBO})

1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting pnl LOSS FLIP EUR{PNL} (vs YE2024 winst EUR{PNL24}) bij omzet EUR{OMZET}.
3. Zorgkas / publieke toelagen vs omzet YE2025.
4. FTE JUMP {FTE} vs YE2024 {FTE24}.
5. Schulden LT/KT en liquiditeiten YE2025.

Ref: {GAP}
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
fields, rq = read_csv(DATA/"research_queue.csv")
for r in rq:
    if r.get("task_id")==RQ:
        if (r.get("entity_id") or "") not in ("", EID):
            print("RACE close", r.get("entity_id")); sys.exit(6)
        r["status"]="done"; r["entity_id"]=EID; r["blocked_gap_id"]=GAP
        r["title"]=f"leftover dual — De Korenbloem YE2025 Medium (omzet JUMP 12.56m / pnl LOSS FLIP / FTE {FTE})"
        r["updated_utc"]=UTC
        r["notes"]=f"tick{TICK}: De Korenbloem {KBO} YE2025 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE JUMP {FTE}; 1 VE Aanbestedende RSZ 87.101); FOI {GAP} ready not sent; after Leieborg@2350; next EVERY-10 2360"
if not any(r.get("task_id")==RQ_NEXT for r in rq):
    rq.append({"task_id":RQ_NEXT,"title":"leftover dual after De Korenbloem — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk","sprint":"hole_fill","priority":"8","status":"open","hierarchy_target":"L5","entity_id":"","instructions":"After De Korenbloem YE2025@2351. Prefer AGB/FARO if YE2025 else FREE ETA-VAPH-WZC-maatwerk. Do NOT redo Korenbloem/Leieborg/Helan HH stack.","blocked_gap_id":"","created_utc":UTC,"updated_utc":UTC,"notes":f"spawned after tick{TICK}; next EVERY-10 2360"})
atomic_write(DATA/"research_queue.csv", fields, rq)
lsf, ls = read_csv(DATA/"loop_state.csv")
for r in ls:
    if r.get("state_id")=="main":
        r.update({"last_tick_utc":UTC,"last_unit_id":RQ,"ticks_completed":TICK,"paused":"no","mode":"continuous","current_sprint":"hole_fill",
                  "notes":f"tick{TICK} leftover dual De Korenbloem {KBO} Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE JUMP {FTE}; 1 VE Aanbestedende RSZ 87.101); after Leieborg@2350; AGB/FARO YE2024; next {RQ_NEXT}; next EVERY-10 2360"})
atomic_write(DATA/"loop_state.csv", lsf, ls)
raw=DATA/"raw"/f"tick{TICK}"; raw.mkdir(parents=True, exist_ok=True)
(raw/"summary.json").write_text(json.dumps({"tick":TICK,"unit":RQ,"entity":EID,"kbo":KBO,"omzet":OMZET,"bruto":BRUTO,"pnl":PNL,"equity":EQUITY,"fte":FTE,"confidence":"medium","gap":GAP,"pi":PI}, indent=2), encoding="utf-8")
with LOG.open("a", encoding="utf-8") as f:
    f.write(f"""
### {UTC} — tick {TICK} — {RQ} De Korenbloem Kortrijk (omzet JUMP 12.56m / pnl LOSS FLIP / FTE {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Leieborg@2350**. Prefer NON-stall AGB/FARO YE2024. Took FREE Flemish WZC **De Korenbloem VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief** **1 VE Aanbestedende**; RSZ **87.101**; {EMAIL}).
- Found: CW NL+EN YE2025 — omzet **EUR{OMZET}** JUMP +2.22%; bruto **EUR{BRUTO}**; pnl **EUR{PNL}** LOSS FLIP; equity **EUR{EQUITY}** DROP −4.9%; FTE **{FTE}** JUMP; neerlegging **{FILED}**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw tick{TICK}/.
- FOI: **ready not sent**. NOT every-10 (next **2360**). Next: {RQ_NEXT}.
""")
print(f"SUCCESS {RQ} Korenbloem omzet {OMZET} LOSS FLIP PI {PI}")

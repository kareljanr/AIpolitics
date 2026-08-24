# -*- coding: utf-8 -*-
"""Tick 2302: MLP maakleerplek Leuven YE2025 after Havinet."""
from __future__ import annotations
import csv, os
csv.field_size_limit(10**7)
ROOT = r"C:\Users\karel\dev\AIpolitics"
DATA = os.path.join(ROOT, "docs", "doge", "data")
RAW = os.path.join(DATA, "raw", "tick2302")
FOI_DRAFTS = os.path.join(ROOT, "docs", "doge", "foi", "drafts")
LOG = os.path.join(ROOT, "docs", "doge", "loop_log.md")
UTC, TICK, RQ, NEXT_RQ = "2026-08-27T18:30:00Z", "2302", "rq_2302", "rq_2303"
ENTITY, KBO = "vzw_mlp_maakleerplek_leuven", "0765.569.332"
GAP = "gap_mlp_nbb_pdf_assets_debt_bruto_gt_omzet_2_11x_pnl_loss_flip_equity_drop_51pct_matrix_l5"
LB = "lb_mlp_bruto_0_20m_omzet_0_09m_2_11x_pnl_loss_flip_equity_drop_51pct_jr2025"
COMM = "comm_mlp_jr2025_statutory_bruto_gt_omzet_2_11x_pnl_loss_flip"
OMZET, OMZET24, BRUTO, BRUTO24 = 94059, 62625, 198928, 118208
PNL, PNL24, EQUITY, EQUITY24, FTE = -52677, 70422, 50225, 102902, 5.0
FILED, EMAIL = "03.06.2026", "info@maakleerplek.be"
RATIO = round(BRUTO / OMZET, 2)
ABS, COST, DIFF, PI = 7.5, 1.0, 3.0, 3.90

def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)

def write_csv(path, fieldnames, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})

os.makedirs(RAW, exist_ok=True)
os.makedirs(FOI_DRAFTS, exist_ok=True)
lsfields, lsrows = read_csv(os.path.join(DATA, "loop_state.csv"))
for r in lsrows:
    if r.get("state_id") == "main" and int(r.get("ticks_completed") or 0) >= 2302:
        raise SystemExit("already past 2302")
open(os.path.join(RAW, "cw_en_excerpt.txt"), "w", encoding="utf-8").write(f"MLP YE2025 {OMZET} {BRUTO} {PNL} {EQUITY}\n")

sfields, srows = read_csv(os.path.join(DATA, "sources.csv"))
for ns in [
 {"source_id":"src_mlp_jr2025_cw_en","title":f"MLP YE2025 CW EN (~{RATIO}x LOSS FLIP equity DROP -51%)","url":"https://www.companyweb.be/en/0765569332/maakleerplek","publisher":"Companyweb","accessed_date":"2026-08-27","source_class":"companyweb","notes":f"tick{TICK}; Medium; omzet {OMZET}; bruto {BRUTO}; pnl {PNL}; equity {EQUITY}; FTE {FTE}; filed {FILED}"},
 {"source_id":"src_mlp_jr2025_cw_nl","title":"MLP YE2025 CW NL","url":"https://www.companyweb.be/nl/0765569332/maakleerplek","publisher":"Companyweb","accessed_date":"2026-08-27","source_class":"companyweb","notes":f"tick{TICK}; Medium NL"},
 {"source_id":"src_mlp_jr2025_cw_fr","title":"MLP YE2025 CW FR","url":"https://www.companyweb.be/fr/0765569332/maakleerplek","publisher":"Companyweb","accessed_date":"2026-08-27","source_class":"companyweb","notes":f"tick{TICK}; Medium FR"},
 {"source_id":"src_mlp_kbo_0765569332","title":"KBO MLP 0765.569.332 Actief 1 VE NACE 88.993","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0765569332","publisher":"KBO / BCE","accessed_date":"2026-08-27","source_class":"kbo","notes":f"tick{TICK}; Strong KBO Actief Leuven"},
 {"source_id":"src_mlp_site_contact_2302","title":"maakleerplek FOI info@maakleerplek.be","url":"https://maakleerplek.be/contact/","publisher":"MLP VZW","accessed_date":"2026-08-27","source_class":"foi_contact","notes":f"tick{TICK}; {EMAIL}"},
]:
    if ns["source_id"] not in {r["source_id"] for r in srows}:
        srows.append(ns)
write_csv(os.path.join(DATA, "sources.csv"), sfields, srows)

efields, erows = read_csv(os.path.join(DATA, "entities.csv"))
if not any(r.get("entity_id") == ENTITY for r in erows):
    erows.append({"entity_id":ENTITY,"name_nl":"MLP / maakleerplek VZW (Leuven)","name_fr":"MLP / maakleerplek ASBL (Louvain)","name_en":"MLP / maakleerplek VZW (Leuven makerspace)","level":"parastatal","parent_id":"sec_flanders","community_language":"nl","website":"https://maakleerplek.be/","foi_email":EMAIL,"foi_postal":"Stapelhuisstraat 13/15, 3000 Leuven","notes":f"tick{TICK} YE2025 Medium CW + Strong KBO {KBO}; bruto {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FOI {GAP}"})
write_csv(os.path.join(DATA, "entities.csv"), efields, erows)

bfields, brows = read_csv(os.path.join(DATA, "budgets.csv"))
for nb in [
 {"budget_id":"bud_mlp_bruto_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(BRUTO),"amount_min_eur":str(BRUTO),"amount_max_eur":str(BRUTO),"basis":"CW bruto YE2025","source_id":"src_mlp_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}"},
 {"budget_id":"bud_mlp_omzet_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(OMZET),"amount_min_eur":str(OMZET),"amount_max_eur":str(OMZET),"basis":"CW omzet YE2025","source_id":"src_mlp_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}"},
 {"budget_id":"bud_mlp_pnl_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(PNL),"amount_min_eur":str(PNL),"amount_max_eur":str(PNL),"basis":"CW pnl LOSS FLIP","source_id":"src_mlp_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}"},
 {"budget_id":"bud_mlp_equity_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(EQUITY),"amount_min_eur":str(EQUITY),"amount_max_eur":str(EQUITY),"basis":"CW equity YE2025","source_id":"src_mlp_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}"},
 {"budget_id":"bud_mlp_fte_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":str(FTE),"amount_min_eur":str(FTE),"amount_max_eur":str(FTE),"basis":"CW FTE","source_id":"src_mlp_jr2025_cw_en","confidence":"medium","notes":f"tick{TICK}"},
]:
    if nb["budget_id"] not in {r["budget_id"] for r in brows}:
        brows.append(nb)
write_csv(os.path.join(DATA, "budgets.csv"), bfields, brows)

cfields, crows = read_csv(os.path.join(DATA, "commitments.csv"))
if not any(r.get("commitment_id") == COMM for r in crows):
    crows.append({"commitment_id":COMM,"title":f"MLP YE2025 (bruto 0.20m ~{RATIO}x / pnl LOSS FLIP / equity DROP -51%)","entity_id":ENTITY,"beneficiary":"Leuven makerspace","legal_basis":f"VZW MLP {KBO}","decision_date":"2026-06-03","start_year":"2025","end_year":"2025","total_envelope_eur":str(BRUTO),"cash_by_year":f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE}}}',"remaining_eur":"0","status":"active","evaluation_url":"https://www.companyweb.be/en/0765569332/maakleerplek","stated_goal":"Leuven circular makerspace","cut_option":"NBB PDF FOI","source_id":"src_mlp_jr2025_cw_en","confidence":"medium","hierarchy_path":"Vlaanderen>Vlaams_Brabant>Leuven>MLP>JR2025","notes":f"tick{TICK}"})
write_csv(os.path.join(DATA, "commitments.csv"), cfields, crows)

lfields, lrows = read_csv(os.path.join(DATA, "leaderboard.csv"))
if not any(r.get("item_id") == LB for r in lrows):
    lrows.append({"item_id":LB,"name":f"MLP bruto 0.20m ~{RATIO}x / pnl LOSS FLIP / equity DROP -51%","level":"L5","type":"makerspace_maatwerk_vzw_statutory","hierarchy_path":"Vlaanderen>Vlaams_Brabant>Leuven>MLP>JR2025","annual_cost_eur":str(BRUTO),"total_cost_eur":str(BRUTO),"tco_notes":f"bruto {BRUTO} ~{RATIO}x omzet {OMZET}; pnl {PNL}; equity {EQUITY}","confidence":"medium","source_id":"src_mlp_jr2025_cw_en","beneficiaries":"Leuven makerspace","stated_goal":"circular makerspace","measured_outcome":f"LOSS FLIP; equity DROP -51%; ~{RATIO}x","absurdity_score":str(ABS),"cost_score":str(COST),"difficulty":str(DIFF),"priority_index":str(PI),"cut_proposal":"NBB PDF FOI","status":"open","struck_reason":"","notes":f"tick{TICK}; FOI {GAP}"})
write_csv(os.path.join(DATA, "leaderboard.csv"), lfields, lrows)

ffields, frows = read_csv(os.path.join(DATA, "foi_queue.csv"))
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append({"gap_id":GAP,"hierarchy_path":"Vlaanderen>Vlaams_Brabant>Leuven>MLP>NBB_PDF","entity_id":ENTITY,"what_is_missing":f"NBB PDF; bruto {BRUTO} vs omzet {OMZET}; LOSS FLIP {PNL}; equity DROP {EQUITY}","why_it_matters":"Leuven makerspace public dual opacity","priority":"8","recipient_body":"MLP VZW","recipient_email":EMAIL,"recipient_postal":"Stapelhuisstraat 13/15, 3000 Leuven","draft_letter_path":f"docs/doge/foi/drafts/{GAP}.md","status":"ready","date_ready":"2026-08-27","date_sent":"","date_due":"","date_answered":"","response_summary":"","linked_commitment_id":COMM,"linked_leaderboard_id":LB,"created_utc":UTC,"updated_utc":UTC,"notes":f"tick{TICK}; ready NOT sent"})
write_csv(os.path.join(DATA, "foi_queue.csv"), ffields, frows)

open(os.path.join(FOI_DRAFTS, f"{GAP}.md"), "w", encoding="utf-8").write(f"""# FOI draft — MLP maakleerplek
**gap_id:** `{GAP}` · **status:** ready NOT sent · **tick:** {TICK}
**entity:** MLP VZW KBO {KBO} · **recipient:** {EMAIL}
## Brief
Openbaarmaking NBB PDF YE2025; toelichting bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x); pnl LOSS FLIP EUR{PNL}; equity DROP EUR{EQUITY} (−51.19%).
- [x] ready NOT sent
""")

rqfields, rqrows = read_csv(os.path.join(DATA, "research_queue.csv"))
for r in rqrows:
    if r.get("task_id") == RQ:
        if r.get("status") == "done":
            raise SystemExit("rq_2302 already done")
        r.update({"status":"done","entity_id":ENTITY,"updated_utc":UTC,"blocked_gap_id":GAP,"title":f"leftover dual — MLP YE2025 Medium (bruto 0.20m ~{RATIO}x / pnl LOSS FLIP / equity DROP -51%)","notes":f"tick{TICK} MLP; bruto {BRUTO}; FOI ready NOT sent"})
        break
if not any(r.get("task_id") == NEXT_RQ for r in rqrows):
    rqrows.append({"task_id":NEXT_RQ,"title":"leftover dual after MLP — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk","sprint":"hole_fill","priority":"8","status":"open","hierarchy_target":"L5","entity_id":"","instructions":"After MLP. Prefer AGB/FARO if YE2025 else unused. Do NOT redo MLP/Havinet/De Kiem/MPI/JOMI stack.","blocked_gap_id":"","created_utc":UTC,"updated_utc":UTC,"notes":f"spawned after tick{TICK}; next every-10 2310"})
write_csv(os.path.join(DATA, "research_queue.csv"), rqfields, rqrows)

for r in lsrows:
    if r.get("state_id") == "main":
        r.update({"last_tick_utc":UTC,"last_unit_id":RQ,"ticks_completed":TICK,"paused":"no","notes":f"tick{TICK} MLP {KBO} Medium (bruto {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; equity DROP {EQUITY}); after Havinet@2301; next {NEXT_RQ}; next every-10 2310"})
write_csv(os.path.join(DATA, "loop_state.csv"), lsfields, lsrows)

open(LOG, "a", encoding="utf-8").write(f"""
### {UTC} - tick {TICK} - {RQ} MLP maakleerplek Leuven (bruto 0.20m ~{RATIO}x / pnl LOSS FLIP / equity DROP -51% / Medium)
- Unit: **{RQ}** after Havinet@2301. Stalls YE2024. Took FREE **MLP** YE2025 KBO **{KBO}**.
- Found: omzet EUR{OMZET}; bruto EUR{BRUTO} ~{RATIO}x; pnl EUR{PNL} LOSS FLIP; equity EUR{EQUITY} DROP -51%; FTE {FTE}; filed {FILED}. Medium.
- Wrote: CSVs + FOI {GAP}; {RQ}=done + {NEXT_RQ} open; ticks={TICK}.
- FOI ready not sent. NOT every-10 (last 2300; next 2310).
""")
print(f"OK tick{TICK} bruto={BRUTO} ratio={RATIO}x pnl={PNL} pi={PI} next={NEXT_RQ}")

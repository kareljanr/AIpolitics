# tick 2325 leftover dual Het Eepos Laakdal YE2025 BBC Strong
import csv, json, shutil
from pathlib import Path
csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TICK = "2325"
TS = "2026-08-28T00:20:00Z"
ENTITY = "vzw_het_eepos_laakdal"
GAP = "gap_eepos_nbb_pdf_personnel_split_vaph_pvf_matrix_bbc_l5"
LB = "lb_eepos_opbrengsten_6_97m_subsidies_5_81m_pnl_0_47m_jr2025"
COMM = "comm_eepos_jr2025_bbc_vaph_laakdal_opbrengsten_subsidies"
SRC_BBC = "src_eepos_jr2025_bbc_pdf"
OMZET = 6967405  # opbrengsten / exploitatie ontvangsten
SUBSIDIES = 5812130
PNL = 471677  # overschot boekjaar J5
EQUITY = 3060522  # nettoactief
ASSETS = 4890405
DEBT = 895167  # LT financial debt
CASH = 2749412
EXPLOIT_SALDO = 530919
PERSONNEL = 5310275
FTE = 50.0
OMZET24 = 6396294
PNL24 = 440987
EQUITY24 = 2588845
PI = 6.25

def append_csv(path, fieldnames, rows):
    path = Path(path)
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        path.write_bytes(data + b"\n")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in rows:
            w.writerow(r)

rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []
ok = False
for r in rq_rows:
    if r.get("task_id") == "rq_2325":
        st = r.get("status")
        eid = (r.get("entity_id") or "").strip()
        if st == "done":
            raise SystemExit("rq_2325 already done")
        if st == "in_progress" and eid == ENTITY:
            ok = True
        elif st == "open" or (st == "in_progress" and not eid):
            r["status"] = "in_progress"
            r["entity_id"] = ENTITY
            r["updated_utc"] = TS
            ok = True
        else:
            raise SystemExit(f"blocked {st} {eid}")
        break
if not ok:
    raise SystemExit("not found")
with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)
with (ROOT / "entities.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row.get("entity_id") == ENTITY:
            raise SystemExit("entity exists")
print("OK claim", ENTITY)

# copy PDF into raw
raw = ROOT / "raw" / f"tick{TICK}"
raw.mkdir(parents=True, exist_ok=True)
src_pdf = Path(r"C:\Users\karel\.grok\sessions\C%3A%5CUsers%5Ckarel%5Cdev%5CAIpolitics\01a033ee-4a6a-73a3-b8af-8d68484e94f9\downloads\1.pdf")
if src_pdf.exists():
    shutil.copy2(src_pdf, raw / "Jaarrekening-2025-Finaal.pdf")

append_csv(ROOT / "sources.csv", ["source_id","title","url","publisher","accessed_date","source_class","notes"], [
{"source_id":SRC_BBC,"title":"Het Eepos Jaarrekening BBC 2025 (official PDF)","url":"https://www.laakdal.be/sites/default/files/2026-06/Jaarrekening-2025-Finaal.pdf","publisher":"Welzijnsvereniging Het Eepos / Gemeente Laakdal","accessed_date":"2026-08-28","source_class":"primary_bbc_pdf","notes":f"tick{TICK}; Strong BBC JR2025 74p; AV 03.06.2026; opbrengsten {OMZET} subsidies {SUBSIDIES} overschot {PNL} assets {ASSETS} debt LT {DEBT} equity {EQUITY} cash {CASH}"},
{"source_id":"src_eepos_kbo_0886198829","title":"KBO Het Eepos 0886.198.829","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0886198829","publisher":"FOD Economie KBO","accessed_date":"2026-08-28","source_class":"official_register","notes":f"tick{TICK}; Strong KBO Actief Welzijnsvereniging Ass.CPAS; Markt 19 2430 Laakdal"},
{"source_id":"src_eepos_portal_2325","title":"Laakdal IGS portal Het Eepos JR2025 listing","url":"https://www.laakdal.be/gemeente-en-bestuur/intergemeentelijke-samenwerkingsverbanden","publisher":"Gemeente Laakdal","accessed_date":"2026-08-28","source_class":"primary_portal","notes":f"tick{TICK}; JR2025 PDF listed after AV 03.06.2026"},
{"source_id":"src_eepos_foi_2325","title":"Het Eepos FOI welkom@het-eepos.be","url":"https://www.laakdal.be/sites/default/files/2025-10/2025-09-30-Besluitenlijst-Algemene-vergadering-Het-Eepos.pdf","publisher":"Het Eepos","accessed_date":"2026-08-28","source_class":"foi_contact","notes":f"tick{TICK}; welkom@het-eepos.be; T 013 66 34 16; Vogelzang 48 / Markt 19 Laakdal"},
{"source_id":"src_eepos_cw_0886198829","title":"Het Eepos Companyweb listing","url":"https://www.companyweb.be/en/0886198829/het-eepos","publisher":"Companyweb","accessed_date":"2026-08-28","source_class":"company_register_aggregator","notes":f"tick{TICK}; CW no statutory euros (BBC entity); FTE ~50; corroborates KBO"},
])
append_csv(ROOT / "budgets.csv", ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"], [
{"budget_id":"bud_eepos_opbrengsten_jr2025_bbc","entity_id":ENTITY,"year":"2025","amount_eur":OMZET,"amount_min_eur":OMZET,"amount_max_eur":OMZET,"basis":"BBC J5 opbrengsten YE2025","source_id":SRC_BBC,"confidence":"strong","notes":f"tick{TICK}; Strong BBC; +{round((OMZET-OMZET24)/OMZET24*100,2)}% vs YE2024 {OMZET24}"},
{"budget_id":"bud_eepos_subsidies_jr2025_bbc","entity_id":ENTITY,"year":"2025","amount_eur":SUBSIDIES,"amount_min_eur":SUBSIDIES,"amount_max_eur":SUBSIDIES,"basis":"BBC J5 werkingssubsidies YE2025","source_id":SRC_BBC,"confidence":"strong","notes":f"tick{TICK}; Strong; specifieke 5715375 + algemene 96755"},
{"budget_id":"bud_eepos_pnl_jr2025_bbc","entity_id":ENTITY,"year":"2025","amount_eur":PNL,"amount_min_eur":PNL,"amount_max_eur":PNL,"basis":"BBC J5 overschot YE2025","source_id":SRC_BBC,"confidence":"strong","notes":f"tick{TICK}; Strong; vs YE2024 {PNL24}; exploitatiesaldo J2 {EXPLOIT_SALDO}"},
{"budget_id":"bud_eepos_equity_jr2025_bbc","entity_id":ENTITY,"year":"2025","amount_eur":EQUITY,"amount_min_eur":EQUITY,"amount_max_eur":EQUITY,"basis":"BBC J4 nettoactief YE2025","source_id":SRC_BBC,"confidence":"strong","notes":f"tick{TICK}; Strong; vs YE2024 {EQUITY24}"},
{"budget_id":"bud_eepos_assets_jr2025_bbc","entity_id":ENTITY,"year":"2025","amount_eur":ASSETS,"amount_min_eur":ASSETS,"amount_max_eur":ASSETS,"basis":"BBC J4 activa YE2025","source_id":SRC_BBC,"confidence":"strong","notes":f"tick{TICK}; Strong; cash {CASH}; debt LT fin {DEBT}"},
{"budget_id":"bud_eepos_personnel_jr2025_bbc","entity_id":ENTITY,"year":"2025","amount_eur":PERSONNEL,"amount_min_eur":PERSONNEL,"amount_max_eur":PERSONNEL,"basis":"BBC J5 bezoldigingen YE2025","source_id":SRC_BBC,"confidence":"strong","notes":f"tick{TICK}; Strong; personnel {PERSONNEL}"},
])
cash = {"2025_opbrengsten":OMZET,"2025_subsidies":SUBSIDIES,"2025_pnl":PNL,"2025_equity":EQUITY,"2025_assets":ASSETS,"2025_debt_lt":DEBT,"2025_cash":CASH,"2025_exploit_saldo":EXPLOIT_SALDO,"2024_opbrengsten":OMZET24,"2024_pnl":PNL24,"2024_equity":EQUITY24}
append_csv(ROOT / "commitments.csv", ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"], [{
"commitment_id":COMM,"title":f"Het Eepos YE2025 BBC opbrengsten 6.97m / subsidies 5.81m / pnl 0.47m Strong","entity_id":ENTITY,"beneficiary":"VAPH users Laakdal-Meerhout adults disability","legal_basis":"Welzijnsvereniging Het Eepos KBO 0886.198.829 Decreet Lokaal Bestuur / VAPH-recognised","decision_date":"2026-06-03","start_year":"2025","end_year":"2025","total_envelope_eur":OMZET,"cash_by_year":json.dumps(cash,separators=(",",":")),"remaining_eur":0,"status":"active","evaluation_url":"https://www.laakdal.be/sites/default/files/2026-06/Jaarrekening-2025-Finaal.pdf","stated_goal":"VAPH residential/day support Laakdal-Meerhout welzijnsvereniging","cut_option":"Publish personnel FTE split; VAPH/PVF vs client fees matrix; reconcile BBC vs any NBB deposit","source_id":SRC_BBC,"confidence":"strong","hierarchy_path":"Vlaanderen>Antwerpen>Laakdal>Het_Eepos>JR2025_BBC","notes":f"tick{TICK}; Strong BBC primary; after Ritmica@2324; AGB/FARO YE2024"
}])
append_csv(ROOT / "leaderboard.csv", ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"], [{
"item_id":LB,"name":f"Het Eepos opbrengsten 6.97m / VAPH subsidies 5.81m / pnl 0.47m (YE2025 BBC Laakdal)","level":"L5","type":"vaph_welzijnsvereniging_bbc","hierarchy_path":"Vlaanderen>Antwerpen>Laakdal>Het_Eepos>JR2025","annual_cost_eur":OMZET,"total_cost_eur":OMZET,"tco_notes":f"BBC opbrengsten {OMZET} / subsidies {SUBSIDIES} (~83%) / overschot {PNL} / assets {ASSETS} / debt LT {DEBT} / equity {EQUITY} / cash {CASH} / personnel {PERSONNEL}","confidence":"strong","source_id":SRC_BBC,"beneficiaries":"VAPH users Laakdal-Meerhout","stated_goal":"VAPH disability care welzijnsvereniging","measured_outcome":"subsidies dominate ~83% of revenue; exploitatiesaldo +0.53m; equity JUMP","absurdity_score":6.5,"cost_score":5.5,"difficulty":2.5,"priority_index":PI,"cut_proposal":"FOI FTE/personnel split + VAPH/PVF vs client-fee matrix; monitor invest vs exploitatie pressure","status":"open","struck_reason":"","notes":f"tick{TICK}; Strong BBC; FOI {GAP}"
}])
append_csv(ROOT / "entities.csv", ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"], [{
"entity_id":ENTITY,"name_nl":"Welzijnsvereniging Het Eepos (Laakdal / VAPH)","name_fr":"Association CPAS Het Eepos (Laakdal / VAPH)","name_en":"Het Eepos welfare association (Laakdal / VAPH)","level":"parastatal","parent_id":"sec_flanders","community_language":"nl","website":"https://www.laakdal.be/gemeente-en-bestuur/intergemeentelijke-samenwerkingsverbanden","foi_email":"welkom@het-eepos.be","foi_postal":"Markt 19, 2430 Laakdal","notes":f"tick{TICK} YE2025 Strong BBC JR2025 + Strong KBO 0886.198.829 Actief Welzijnsvereniging; opbrengsten {OMZET}; subsidies {SUBSIDIES}; pnl {PNL}; equity {EQUITY}; assets {ASSETS}; debt LT {DEBT}; FOI {GAP}"
}])
append_csv(ROOT / "foi_queue.csv", ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"], [{
"gap_id":GAP,"hierarchy_path":"Vlaanderen>Antwerpen>Laakdal>Het_Eepos>personnel_vaph_matrix","entity_id":ENTITY,"what_is_missing":f"FTE social-balance split; VAPH/PVF vs client woon-leefkosten matrix behind subsidies {SUBSIDIES}; any NBB deposit id","why_it_matters":"Strong BBC shows subsidy-heavy 6.97m VAPH welzijnsvereniging; personnel {PERSONNEL} opaque by grade","priority":7,"recipient_body":"Welzijnsvereniging Het Eepos","recipient_email":"welkom@het-eepos.be","recipient_postal":"Markt 19 / Vogelzang 48, 2430 Laakdal","draft_letter_path":f"docs/doge/foi/drafts/{GAP}.md","status":"ready","date_ready":"2026-08-28","date_sent":"","date_due":"","date_answered":"","response_summary":"","linked_commitment_id":COMM,"linked_leaderboard_id":LB,"created_utc":TS,"updated_utc":TS,"notes":f"tick{TICK}; ready NOT sent; Strong BBC primary already public"
}])

with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []
for r in rq_rows:
    if r.get("task_id") == "rq_2325":
        eid = (r.get("entity_id") or "").strip()
        if r.get("status") == "done":
            raise SystemExit("stolen done")
        if eid not in ("", ENTITY):
            raise SystemExit(f"stolen {eid}")
        r["title"] = f"leftover dual — Het Eepos YE2025 Strong (opbrengsten 6.97m / subsidies 5.81m / pnl 0.47m / equity 3.06m)"
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = f"tick{TICK}; Het Eepos 0886.198.829 YE2025 Strong BBC; opbrengsten {OMZET}; subsidies {SUBSIDIES}; pnl {PNL}; equity {EQUITY}; assets {ASSETS}; debt LT {DEBT}; FOI {GAP} ready NOT sent; after Ritmica@2324; next EVERY-10 2330"
        break
if not any(x.get("task_id") == "rq_2326" for x in rq_rows):
    rq_rows.append({"task_id":"rq_2326","title":"leftover dual after Het Eepos — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk","sprint":"hole_fill","priority":"8","status":"open","hierarchy_target":"L5","entity_id":"","instructions":"After Het Eepos YE2025 Strong BBC (opbrengsten 6.97m). Prefer AGB/FARO YE2025 else unused Tandem/Gandae/Aralea/Manupal/Vlotter/Wonen-Werken-Autisme if YE2025. Do NOT redo Het Eepos/Ritmica/Dominiek Savio/Merlijn/Humival stack.","blocked_gap_id":"","created_utc":TS,"updated_utc":TS,"notes":"spawned after tick2325 Het Eepos; next EVERY-10 2330"})
with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"], lineterminator="\n")
    w.writeheader()
    w.writerow({"state_id":"main","mode":"continuous","current_sprint":"hole_fill","last_tick_utc":TS,"last_unit_id":"rq_2325","ticks_completed":"2325","paused":"no","notes":f"tick{TICK} leftover dual Het Eepos 0886.198.829 Strong BBC (opbrengsten JUMP {OMZET}; subsidies {SUBSIDIES}; pnl {PNL}; equity JUMP {EQUITY}; assets {ASSETS}; debt LT {DEBT}; Laakdal VAPH welzijnsvereniging); after Ritmica@2324; AGB/FARO YE2024; next rq_2326; next EVERY-10 2330"})
Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(f"# FOI draft — Het Eepos Laakdal\n\n**gap_id:** `{GAP}` · ready NOT sent · tick {TICK}\n**KBO:** 0886.198.829 · FOI welkom@het-eepos.be · Markt 19 / Vogelzang 48, 2430 Laakdal · T 013 66 34 16\nBBC JR2025 primary: opbrengsten {OMZET}; subsidies {SUBSIDIES}; overschot {PNL}; assets {ASSETS}; debt LT {DEBT}; equity {EQUITY}.\nAsk: FTE/personnel grade split; VAPH/PVF vs client woon-leefkosten matrix; NBB deposit id if any. Ref {GAP}\n", encoding="utf-8")
(raw / "summary.json").write_text(json.dumps({"tick":TICK,"entity_id":ENTITY,"opbrengsten":OMZET,"subsidies":SUBSIDIES,"pnl":PNL,"equity":EQUITY,"assets":ASSETS,"debt_lt":DEBT,"confidence":"strong","gap_id":GAP}, indent=2), encoding="utf-8")
log = Path("docs/doge/loop_log.md")
log.write_text(log.read_text(encoding="utf-8") + f"\n### 2026-08-28T00:20:00Z - tick 2325 - rq_2325 Het Eepos Laakdal (opbrengsten 6.97m / subsidies 5.81m / pnl 0.47m / Strong)\n\n- Unit: **rq_2325** finish in_progress **Het Eepos** after **Ritmica@2324**. Stalls AGB/FARO YE2024. Took claimed FREE VAPH welzijnsvereniging **Het Eepos** YE2025 BBC (KBO **0886.198.829**; Laakdal; welkom@het-eepos.be).\n- Found: official BBC JR2025 PDF — opbrengsten **EUR{OMZET}**; werkingssubsidies **EUR{SUBSIDIES}** (~83%); overschot **EUR{PNL}**; assets **EUR{ASSETS}**; debt LT **EUR{DEBT}**; equity **EUR{EQUITY}**; cash **EUR{CASH}**; personnel **EUR{PERSONNEL}**; AV **03.06.2026**. Strong.\n- Wrote: sources(+5) budgets(+6) commitments(+1) leaderboard(+1) entities(+1) foi; rq_2325=done + rq_2326 open; ticks=2325; raw PDF.\n- FOI ready not sent. NOT every-10 (next **2330**). Next: rq_2326.\n", encoding="utf-8")
print("SUCCESS", OMZET, SUBSIDIES, PNL, "Strong", PI)

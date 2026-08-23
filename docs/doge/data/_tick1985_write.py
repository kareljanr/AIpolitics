# ephemeral tick1985 — Epicura YE2025
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)

UTC = "2026-08-23T23:55:00Z"
ENTITY = "vzw_epicura"
GAP = "gap_epicura_nbb_pdf_assets_debt_pnl_loss_matrix_l5"
SRC = "src_epicura_jr2025_cw"
SRC_EN = "src_epicura_jr2025_cw_en"
SRC_KBO = "src_epicura_kbo_1985"
SRC_SITE = "src_epicura_site_1985"

def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []

def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_1985")
if (r.get("status") or "").lower() not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {**{k:"" for k in sfields},"source_id":SRC,"title":"Companyweb NL Epicura YE2025 statutory","url":"https://www.companyweb.be/nl/0842335231/centre-hospitalier-epicura","publisher":"Companyweb (NBB-derived)","accessed_date":"2026-08-23","source_class":"secondary_aggregator","notes":"tick1985; YE2025 omzet JUMP 370875883 pnl LOSS -2318017 equity DROP 66288513 bruto JUMP 193877413 FTE 2511; neerlegging 10.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1985/epicura_cw_nl.html"},
    {**{k:"" for k in sfields},"source_id":SRC_EN,"title":"Companyweb EN Epicura YE2025 statutory","url":"https://www.companyweb.be/en/0842335231/centre-hospitalier-epicura","publisher":"Companyweb (NBB-derived)","accessed_date":"2026-08-23","source_class":"secondary_aggregator","notes":"tick1985; EN mirror YE2025 Medium; YoY vs YE2024 omzet 362353096 pnl 1110530 equity 68602099 bruto 193520369 FTE 2511.6; raw docs/doge/data/raw/tick1985/epicura_cw_en.html"},
    {**{k:"" for k in sfields},"source_id":SRC_KBO,"title":"KBO Epicura 0842.335.231 Actief ASBL Saint-Ghislain","url":"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0842335231","publisher":"KBO FOD Economie","accessed_date":"2026-08-23","source_class":"official_register","notes":"tick1985; Actief ASBL; Rue Louis Caty 136 7331 Saint-Ghislain; 15 VE; no KBO email/web; NACE hospital"},
    {**{k:"" for k in sfields},"source_id":SRC_SITE,"title":"epicura.be Centre Hospitalier Epicura","url":"https://www.epicura.be/","publisher":"Epicura","accessed_date":"2026-08-23","source_class":"official_org","notes":"tick1985; Hainaut hospital ASBL network; FOI via site contact"},
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {"budget_id":"bud_epicura_omzet_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":"370875883","amount_min_eur":"","amount_max_eur":"","basis":"CW YE2025 omzet / Turnover","source_id":SRC,"confidence":"medium","notes":"tick1985; omzet JUMP 370875883 +2.35pct vs YE2024 362353096"},
    {"budget_id":"bud_epicura_pnl_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":"-2318017","amount_min_eur":"","amount_max_eur":"","basis":"CW YE2025 Profit/Loss","source_id":SRC,"confidence":"medium","notes":"tick1985; pnl LOSS -2318017 turnaround -308.73pct vs YE2024 profit 1110530"},
    {"budget_id":"bud_epicura_equity_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":"66288513","amount_min_eur":"","amount_max_eur":"","basis":"CW YE2025 Eigen vermogen","source_id":SRC,"confidence":"medium","notes":"tick1985; equity DROP 66288513 -3.37pct vs YE2024 68602099"},
    {"budget_id":"bud_epicura_bruto_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":"193877413","amount_min_eur":"","amount_max_eur":"","basis":"CW YE2025 Brutomarge","source_id":SRC,"confidence":"medium","notes":"tick1985; bruto JUMP 193877413 +0.18pct vs YE2024 193520369"},
    {"budget_id":"bud_epicura_fte_jr2025_statutory","entity_id":ENTITY,"year":"2025","amount_eur":"2511","amount_min_eur":"","amount_max_eur":"","basis":"CW social-balance FTE","source_id":SRC,"confidence":"medium","notes":"tick1985; YE2025 FTE 2511 vs YE2024 2511.6"},
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k:"" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {**{k:"" for k in cfields},"commitment_id":"comm_epicura_jr2025_statutory_hospital","title":"Epicura YE2025 leftover Hainaut hospital ASBL dual (omzet JUMP 370.88m / pnl LOSS 2.32m)","entity_id":ENTITY,"beneficiary":"Hainaut patients / Epicura hospital network","legal_basis":"ASBL hospitaliere / decret wallon sante","decision_date":"2026-07-10","start_year":"2025","end_year":"2025","total_envelope_eur":"370875883","cash_by_year":'{"2025_omzet":370875883,"2025_pnl":-2318017,"2025_equity":66288513,"2025_bruto":193877413,"2025_fte":2511}',"remaining_eur":"0","status":"active","evaluation_url":"https://www.companyweb.be/nl/0842335231/centre-hospitalier-epicura","stated_goal":"Hospital care Hainaut / Saint-Ghislain network","cut_option":"Publish NBB PDF assets/debt + pnl LOSS recon FOI","source_id":SRC,"confidence":"medium","hierarchy_path":"Wallonie>Hainaut>Epicura>JR2025_statutory_L5","notes":"tick1985; Medium CW; assets/debt Unknown; pnl LOSS turnaround; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024"}
if not any(x.get("commitment_id")==nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nlb = {**{k:"" for k in lfields},"item_id":"lb_epicura_omzet_jump_370_88m_pnl_loss_2_32m_jr2025","name":"Epicura omzet JUMP 370.88m / pnl LOSS 2.32m / equity DROP 66.29m (Hainaut hospital YE2025)","level":"L5","type":"walloon_hospital_asbl_dual","hierarchy_path":"Wallonie>Hainaut>Epicura>JR2025_statutory_L5","annual_cost_eur":"370875883","total_cost_eur":"66288513","tco_notes":"statutory omzet JUMP 370875883 pnl LOSS -2318017 equity DROP 66288513 bruto JUMP 193877413 FTE 2511; assets/debt Unknown; LOSS turnaround vs YE2024 profit","confidence":"medium","source_id":SRC,"beneficiaries":"Hainaut patients via Epicura hospital ASBL","stated_goal":"Integrated hospital care Hainaut","measured_outcome":"Medium CW YE2025; 370.9m omzet JUMP; pnl LOSS turnaround; NBB PDF residual","absurdity_score":"5.0","cost_score":"7.5","difficulty":"4.0","priority_index":"6.125","cut_proposal":"Publish NBB PDF assets/debt + pnl LOSS recon FOI; dual vs CHwapi/Vivalia/HELORA hospital opacity","status":"active","struck_reason":"","notes":"tick1985 leftover dual; Medium CW; large hospital TE-adjacent; not pure-waste top10; next every-10 1990"}
if not any(x.get("item_id")==nlb["item_id"] for x in lrows):
    lrows.append(nlb)
save("docs/doge/data/leaderboard.csv", lrows, lfields)

erows, efields = load("docs/doge/data/entities.csv")
ne = {**{k:"" for k in efields},"entity_id":ENTITY,"name_nl":"Epicura (Centre Hospitalier Epicura)","name_fr":"Epicura (Centre Hospitalier Epicura)","name_en":"Epicura (Hainaut hospital ASBL)","level":"hospital","parent_id":"wallonie_gov","community_language":"fr","website":"https://www.epicura.be/","foi_email":"","foi_postal":"Rue Louis Caty 136, 7331 Saint-Ghislain","notes":"tick1985 YE2025 Medium CW NL+EN + Strong KBO 0842.335.231 Actief ASBL; omzet JUMP 370.88m pnl LOSS 2.32m equity DROP 66.29m bruto JUMP 193.88m FTE 2511; assets/debt Unknown; neerlegging 10.07.2026; 15 VE; FOI gap_epicura_nbb_pdf_assets_debt_pnl_loss_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo CHwapi/IDETA/SPI/Vivalia/HELORA/CISCH/LOGIPOLE/IDELUX*/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH"}
if not any(x.get("entity_id")==ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {**{k:"" for k in ffields},"gap_id":GAP,"hierarchy_path":"Wallonie>Hainaut>Epicura>NBB_PDF_assets_debt_pnl_loss","entity_id":ENTITY,"what_is_missing":"NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS turnaround recon vs YE2024 profit 1.11m; campus/network matrix","why_it_matters":"Medium CW shows 370.9m omzet hospital ASBL flipping to LOSS without balance sheet","priority":"7","recipient_body":"Epicura","recipient_email":"","recipient_postal":"https://www.epicura.be/","draft_letter_path":f"docs/doge/foi/drafts/{GAP}.md","status":"ready","date_ready":"2026-08-23","linked_commitment_id":"comm_epicura_jr2025_statutory_hospital","linked_leaderboard_id":"lb_epicura_omzet_jump_370_88m_pnl_loss_2_32m_jr2025","created_utc":UTC,"updated_utc":UTC,"notes":"tick1985; human-send only; Medium CW; KBO no email — route via epicura.be contact; next every-10 1990"}
if not any(x.get("gap_id")==GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(f"""# FOI draft — Epicura (NBB PDF / assets-debt / pnl LOSS)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Epicura ASBL — KBO **0842.335.231**  
**recipient:** Epicura (KBO has no email; route via https://www.epicura.be/ contact)  
**sources:** [CW NL](https://www.companyweb.be/nl/0842335231/centre-hospitalier-epicura) · [CW EN](https://www.companyweb.be/en/0842335231/centre-hospitalier-epicura) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0842335231) · [site](https://www.epicura.be/)  
**tick:** 1985  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.07.2026**): omzet **EUR370,875,883** JUMP +2.35%; pnl **NEG EUR-2,318,017** (LOSS turnaround); equity **EUR66,288,513** DROP -3.37%; bruto **EUR193,877,413** JUMP +0.18%; FTE **2511**; assets/debt **Unknown**.
- Hainaut hospital ASBL (Rue Louis Caty 136, Saint-Ghislain). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. CHwapi mined tick1984.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Epicura — Rue Louis Caty 136, 7331 Saint-Ghislain
cc: SPW sante / Hainaut transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 Epicura + balans + pnl-LOSS recon (KBO 0842.335.231)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl LOSS turnaround (vs YE2024 profit EUR1,110,530).
4. Campus / network matrix indien relevant.
5. Dual vs CHwapi / Vivalia / HELORA indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")

for x in qrows:
    if x.get("task_id")=="rq_1985":
        x["status"]="done"; x["updated_utc"]=UTC; x["entity_id"]=ENTITY; x["blocked_gap_id"]=GAP
        x["title"]="leftover dual hole-fill after CHwapi — Epicura YE2025 Medium"
        x["notes"]="tick1985 Epicura Medium omzet JUMP 370.88m pnl LOSS 2.32m; FOI ready; next rq_1986; next every-10 1990"
        x["instructions"]=f"Completed leftover Epicura Hainaut hospital ASBL YE2025 Medium CW; KBO 0842.335.231; omzet JUMP 370875883 pnl LOSS -2318017 equity DROP 66288513 bruto JUMP 193877413 FTE 2511; FOI {GAP}"
if not any(x.get("task_id")=="rq_1986" for x in qrows):
    qrows.append({**{k:"" for k in qfields},"task_id":"rq_1986","title":"leftover dual hole-fill after Epicura","sprint":"hole_fill","priority":"8","status":"open","hierarchy_target":"L5","entity_id":"","instructions":"Tick 1985 after Epicura YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/ADT (ISoSL if YE2025 / other). Do NOT redo Epicura, CHwapi, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Env.","blocked_gap_id":"","created_utc":UTC,"updated_utc":UTC,"notes":"spawned after tick1985 Epicura; next every-10 1990"})
save("docs/doge/data/research_queue.csv", qrows, qfields)

srows2, sfields2 = load("docs/doge/data/loop_state.csv")
for s in srows2:
    s["last_tick_utc"]=UTC; s["last_unit_id"]="rq_1985"; s["ticks_completed"]="1985"; s["paused"]="no"; s["mode"]="continuous"; s["current_sprint"]="hole_fill"
    s["notes"]="tick1985 leftover Epicura 0842.335.231 Medium CW (omzet JUMP 370.88m pnl LOSS 2.32m equity DROP 66.29m bruto JUMP 193.88m FTE 2511; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; ISoSL YE2025 deferred; next rq_1986; next every-10 1990; continuous hole_fill"
save("docs/doge/data/loop_state.csv", srows2, sfields2)

log_path = Path("docs/doge/loop_log.md")
log_path.write_text(log_path.read_text(encoding="utf-8") + f"""

## Tick 1985 — 2026-08-23T23:55:00Z — rq_1985 Epicura YE2025 (omzet JUMP 370.88m / pnl LOSS 2.32m / Medium)

- Unit: **rq_1985** leftover dual after **rq_1984 CHwapi**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Epicura** YE2025 (KBO **0842.335.231**; Rue Louis Caty 136 Saint-Ghislain; Hainaut **hospital ASBL**). **ISoSL** YE2025 also live deferred. Do not redo CHwapi/IDETA/SPI/Vivalia/HELORA/CISCH/LOGIPOLE/IDELUX*/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/SWDE.
- Found: Companyweb NL+EN YE2025 — omzet **EUR370,875,883** JUMP +2.35%; pnl **NEG EUR-2,318,017** LOSS turnaround; equity **EUR66,288,513** DROP -3.37%; bruto **EUR193,877,413** JUMP +0.18%; FTE **2511**; neerlegging **10.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief ASBL 15 VE; no KBO email.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_epicura); foi + draft {GAP}; rq_1985=done + rq_1986 open; loop_state ticks=1985.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1986 (AGB/FARO-if-YE2025 / AIESH-REW / ISoSL / unused DSO-IGS-HVZ).

""", encoding="utf-8")
print("DONE tick1985 Epicura")

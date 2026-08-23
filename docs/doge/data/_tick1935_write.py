# tick 1935 — Elia Transmission Belgium YE2025 Medium CW+Upswitch
# (tick 1934 already taken by concurrent Fluxys; this is next open rq_1935)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).resolve().parent
TS = "2026-08-27T14:45:00Z"
csv.field_size_limit(10**7)

sources_new = [
    {
        "source_id": "src_etb_jr2025_cw",
        "title": "Companyweb Elia Transmission Belgium YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/en/0731852231/elia-transmission-belgium",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": "tick1935; neerlegging 09.06.2026; omzet 1524550649 flat +0.14pct; bruto 242276439 JUMP +23.04pct; pnl 228371596 DROP -3.64pct; equity 3860494516 JUMP +39.79pct; FTE 611.6",
    },
    {
        "source_id": "src_etb_jr2025_upswitch",
        "title": "Upswitch Elia Transmission Belgium YE2025 NBB/CBSO assets EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/elia-transmission-belgium-0731852231",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": "tick1935; YE2025 assets 10452686219 JUMP vs 8592763692 YE2024; equity 3860494516; omzet 1524550649; EBITDA 152687864; operating result 125587333",
    },
    {
        "source_id": "src_etb_kbo",
        "title": "KBO Elia Transmission Belgium 0731.852.231 Belgian TSO NV",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0731852231",
        "publisher": "KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": "tick1935; Actief NV; Keizerslaan 20 Brussel; kapitaal 2824448580; NACE 35.130; Interfin 0222.944.897 bestuurder; RSZ employer; parent path Elia Group/Publi-T",
    },
]


def append_csv(path, rows):
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        for r in rows:
            w.writerow(r)


append_csv(DATA / "sources.csv", sources_new)

budgets_new = [
    {"budget_id": "bud_etb_omzet_jr2025", "entity_id": "elia", "year": "2025", "amount_eur": "1524550649", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived omzet", "source_id": "src_etb_jr2025_cw", "confidence": "medium", "notes": "tick1935; YE2025 omzet 1524550649 flat +0.14pct"},
    {"budget_id": "bud_etb_bruto_jr2025", "entity_id": "elia", "year": "2025", "amount_eur": "242276439", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived 9900", "source_id": "src_etb_jr2025_cw", "confidence": "medium", "notes": "tick1935; YE2025 bruto 242276439 JUMP +23.04pct"},
    {"budget_id": "bud_etb_pnl_jr2025", "entity_id": "elia", "year": "2025", "amount_eur": "228371596", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived 9904", "source_id": "src_etb_jr2025_cw", "confidence": "medium", "notes": "tick1935; YE2025 pnl 228371596 DROP -3.64pct"},
    {"budget_id": "bud_etb_equity_jr2025", "entity_id": "elia", "year": "2025", "amount_eur": "3860494516", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW/Upswitch NBB-derived 10/15", "source_id": "src_etb_jr2025_cw", "confidence": "medium", "notes": "tick1935; YE2025 equity 3860494516 JUMP +39.79pct"},
    {"budget_id": "bud_etb_assets_jr2025", "entity_id": "elia", "year": "2025", "amount_eur": "10452686219", "amount_min_eur": "", "amount_max_eur": "", "basis": "Upswitch NBB/CBSO assets", "source_id": "src_etb_jr2025_upswitch", "confidence": "medium", "notes": "tick1935; YE2025 assets 10452686219 JUMP vs 8.59bn YE2024"},
    {"budget_id": "bud_etb_ebitda_jr2025", "entity_id": "elia", "year": "2025", "amount_eur": "152687864", "amount_min_eur": "", "amount_max_eur": "", "basis": "Upswitch NBB/CBSO EBITDA", "source_id": "src_etb_jr2025_upswitch", "confidence": "medium", "notes": "tick1935; YE2025 EBITDA 152687864"},
    {"budget_id": "bud_etb_fte_jr2025", "entity_id": "elia", "year": "2025", "amount_eur": "612", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived FTE 611.6", "source_id": "src_etb_jr2025_cw", "confidence": "medium", "notes": "tick1935; YE2025 FTE 611.6 (stored 612)"},
]
append_csv(DATA / "budgets.csv", budgets_new)

comm = {
    "commitment_id": "comm_etb_jr2025_omzet",
    "title": "Elia Transmission Belgium YE2025 leftover Belgian TSO dual (omzet 1.52bn / equity JUMP 3.86bn / assets 10.45bn)",
    "entity_id": "elia",
    "beneficiary": "Elia Group / Publi-T / Interfin / municipalities / grid users / MOG-CAPEX path",
    "legal_basis": "WVV NV; NBB neerlegging; Elektriciteitswet TSO; Bestuursdecreet / aanbestedende overheid path",
    "decision_date": "2026-06-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1524550649",
    "cash_by_year": "2025:omzet=1524550649;bruto=242276439;pnl=228371596;equity=3860494516;assets=10452686219;ebitda=152687864;fte=611.6;kapitaal=2824448580",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0731852231/elia-transmission-belgium",
    "stated_goal": "Belgian electricity TSO (ETB) regulated transmission after Elia Group capital-raise dual",
    "cut_option": "FOI NBB PDF + debt/cash/tariff path explaining equity JUMP +39.79pct with flat omzet + parent/Publi-T/Interfin share",
    "source_id": "src_etb_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Belgie>Brussel>ETB>JR2025_L5",
    "notes": "tick1935; Medium CW+Upswitch; preferred AGB Bornem JR2024 / Dijk92 CDN 403 / FARO YE2024; Fluxys done 1934; BNO done 1933; NON-Eneco; double-count vs Elia Group/Publi-T/Interfin/MOG/Fluxys path possible",
}
append_csv(DATA / "commitments.csv", [comm])

lb = {
    "item_id": "lb_etb_omzet_1_52bn_equity_jump_3_86bn_assets_10_45bn_jr2025",
    "name": "ETB omzet 1.52bn / equity JUMP 3.86bn / assets 10.45bn (Belgian TSO after Elia Group raise)",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Belgie>Brussel>ETB>JR2025_L5",
    "annual_cost_eur": "1524550649",
    "total_cost_eur": "10452686219",
    "tco_notes": "omzet 1524550649 flat bruto 242276439 JUMP pnl 228371596 DROP equity 3860494516 JUMP +40pct assets 10452686219 JUMP ebitda 152687864 FTE 611.6; NBB PDF unresolved",
    "confidence": "medium",
    "source_id": "src_etb_jr2025_cw",
    "beneficiaries": "Elia Group / Publi-T / Interfin / municipalities / grid users",
    "stated_goal": "Regulated Belgian electricity TSO (ETB)",
    "measured_outcome": "Equity JUMP +40pct to 3.86bn and assets JUMP to 10.45bn with flat 1.52bn omzet after parent capital raise; NBB PDF unresolved",
    "absurdity_score": "6.5",
    "cost_score": "9.8",
    "difficulty": "4.0",
    "priority_index": "7.6",
    "cut_proposal": "Publish NBB PDF + debt/cash/tariff matrix + equity JUMP recon vs Publi-T/Elia Group raise",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1935; Medium CW+Upswitch; leftover after Fluxys; not TE-additive; NON-Eneco; double-count vs Elia Group/Publi-T/Interfin/MOG possible",
}
append_csv(DATA / "leaderboard.csv", [lb])

ent_path = DATA / "entities.csv"
with ent_path.open(encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    ent_fields = er.fieldnames
    ents = list(er)
for e in ents:
    if e["entity_id"] == "elia":
        e["parent_id"] = "nv_elia_group"
        e["foi_email"] = "info@elia.be"
        e["foi_postal"] = "Keizerslaan 20 1000 Brussel"
        e["notes"] = (
            "Federal electricity TSO; hosts CRM auctions and federal GC OSP cash; tick169; "
            "tick1935 YE2025 Medium CW+Upswitch KBO 0731.852.231 Actief NV; omzet 1.52bn equity JUMP 3.86bn "
            "assets 10.45bn pnl 228.4m bruto 242.3m FTE 611.6 kapitaal 2.82bn; Interfin bestuurder; "
            "NBB PDF FOI; distinct from nv_elia_group holding"
        )
        break
with ent_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ent_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(ents)

foi = {
    "gap_id": "gap_etb_nbb_pdf_debt_tariff_equity_jump_l5",
    "hierarchy_path": "Belgie>Brussel>ETB>nbb_debt_tariff_equity_L5",
    "entity_id": "elia",
    "what_is_missing": "NBB deposit id + full JR2025 PDF (debt/cash/CAPEX exact); tariff/RAB path explaining equity JUMP +39.79% to 3.86bn and assets JUMP to 10.45bn with flat omzet 1.52bn; Elia Group / Publi-T / Interfin ownership % and related-party flows",
    "why_it_matters": "Belgian TSO — 1.52bn omzet / 3.86bn equity JUMP / 10.45bn assets hides regulated CAPEX+parent capital-raise money after Elia Group/Publi-T/Interfin/Fluxys mined",
    "priority": "8",
    "recipient_body": "Elia Transmission Belgium NV",
    "recipient_email": "info@elia.be",
    "recipient_postal": "Keizerslaan 20 1000 Brussel (cc Elia Group / Publi-T / Interfin)",
    "draft_letter_path": "docs/doge/foi/drafts/gap_etb_nbb_pdf_debt_tariff_equity_jump_l5.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_etb_jr2025_omzet",
    "linked_leaderboard_id": "lb_etb_omzet_1_52bn_equity_jump_3_86bn_assets_10_45bn_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1935; human-send only; Medium CW+Upswitch; NBB SPA HTML only this tick; AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; Fluxys done 1934; BNO done 1933",
}
append_csv(DATA / "foi_queue.csv", [foi])

rq_path = DATA / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rq_fields = rr.fieldnames
    rqs = list(rr)
for r in rqs:
    if r["task_id"] == "rq_1935":
        r["status"] = "done"
        r["entity_id"] = "elia"
        r["blocked_gap_id"] = "gap_etb_nbb_pdf_debt_tariff_equity_jump_l5"
        r["updated_utc"] = TS
        r["instructions"] = (
            "Completed: Elia Transmission Belgium (KBO 0731.852.231) YE2025 Medium CW+Upswitch "
            "(omzet 1.52bn equity JUMP 3.86bn assets 10.45bn pnl 228.4m bruto 242.3m FTE 611.6); "
            "AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; Fluxys done 1934; BNO done 1933; FOI ready not sent"
        )
        r["notes"] = (
            "tick1935 ETB Medium CW+Upswitch; preferred leftovers stalled; NON-Eneco; "
            "double-count vs Elia Group/Publi-T/Interfin/MOG possible; next every-10 1940"
        )
        break
rqs.append(
    {
        "task_id": "rq_1936",
        "title": "Leftover dual residual hole-fill after ETB (AGB/Dijk92-if-200 / FARO-if-YE2025 / FluxysLNG-otherHVZ-IGS-if-live)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1936 after 1935 ETB. Prefer leftover AGB/APB if PDF live, else Dijk92 if CDN 200, "
            "else FARO if TRUE NBB YE2025, else Fluxys LNG / other HVZ/IGS if unused live YE2025 euros. "
            "Do NOT redo BNO, Fluxys holding, ETB, or Elia Group."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": "spawned after tick1935; next every-10 1940",
    }
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rqs)

state_path = DATA / "loop_state.csv"
with state_path.open(encoding="utf-8", newline="") as f:
    sr = csv.DictReader(f)
    state_fields = sr.fieldnames
    states = list(sr)
states[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": TS,
        "last_unit_id": "rq_1935",
        "ticks_completed": "1935",
        "paused": "no",
        "notes": (
            "tick1935 leftover ETB 0731.852.231 Medium CW+Upswitch (omzet 1.52bn equity JUMP 3.86bn "
            "assets 10.45bn pnl 228.4m bruto 242.3m FTE 611.6); NBB PDF+debt/tariff FOI; "
            "AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; Fluxys done 1934; BNO done 1933; "
            "next rq_1936; next every-10 1940; continuous hole_fill"
        ),
    }
)
with state_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=state_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(states)

draft = ROOT / "foi" / "drafts" / "gap_etb_nbb_pdf_debt_tariff_equity_jump_l5.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    """# FOI draft — Elia Transmission Belgium (NBB PDF / debt / tariff / equity JUMP)

**gap_id:** `gap_etb_nbb_pdf_debt_tariff_equity_jump_l5`  
**status:** ready (NOT sent)  
**entity:** Elia Transmission Belgium NV — KBO **0731.852.231**  
**recipient:** info@elia.be / Keizerslaan 20 1000 Brussel / cc Elia Group / Publi-T / Interfin  
**sources:** [Companyweb](https://www.companyweb.be/en/0731852231/elia-transmission-belgium) · [Upswitch](https://www.upswitch.app/en/companies/be/elia-transmission-belgium-0731852231) · KBO · NBB consult SPA only  
**tick:** 1935 (NOT every-10; next every-10 is **1940**)  
**confidence on table euros:** Medium (NBB-derived CW+Upswitch; primary deposit PDF unresolved this tick)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **09.06.2026**): omzet **€1.524.550.649** (flat **+0,14%**); bruto **€242.276.439** (**JUMP +23,04%**); PnL **€228.371.596** (**DROP −3,64%**); equity **€3.860.494.516** (**JUMP +39,79%**); assets **€10.452.686.219**; EBITDA **€152.687.864**; FTE **611,6**; kapitaal **€2.824.448.580**.
- **Public dual:** Belgian TSO; Interfin bestuurder; Elia Group / Publi-T municipal capital-raise path; MOG/grid CAPEX.
- Preferred leftover paths stalled: AGB Bornem **JR2024-only**; Dijk92 CDN **403**; FARO YE2024; **Fluxys** done tick **1934**; **BNO** done tick **1933**.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Elia Transmission Belgium NV
t.a.v. openbaarheid / raad van bestuur
Keizerslaan 20
1000 Brussel

cc: Elia Group NV / Publi-T CV / Interfin CV PR

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
schulden, tarieven/RAB en equity-sprong (KBO 0731.852.231)

Geachte,

Op grond van toepasselijke openbaarheid (Bestuursdecreet /
aanbestedende overheid / Elektriciteitswet-transparantie) vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF), neergelegd ~09.06.2026.
2. Balans totaal activa / cash / schuldenrooster (LT/ST) en CAPEX-uitsplitsing.
3. Toelichting tariff/RAB-pad dat equity JUMP +39,79% tot €3.860.494.516
   en activa JUMP tot €10.452.686.219 verklaart bij vlakke omzet €1.524.550.649.
4. Actueel aandeelhoudersregister (Elia Group / Publi-T / Interfin / overige)
   en related-party stromen met de holding.
5. Reconciliatie maatschappelijk kapitaal €2.824.448.580 met
   Publi-T/Elia Group-transacties 2024–2025.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: gap_etb_nbb_pdf_debt_tariff_equity_jump_l5

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Draft complete
- [ ] Human review
- [ ] Human send (agent must NOT send)
- [ ] Track response in foi_queue.csv
""",
    encoding="utf-8",
)

log_path = ROOT / "loop_log.md"
log_block = """
## Tick 1935 - 2026-08-27T14:45:00Z - rq_1935 ETB (omzet 1.52bn / equity JUMP 3.86bn / assets 10.45bn / Medium)

- Unit: **rq_1935** leftover dual after Fluxys (1934 concurrent). Prefer NON-Eneco live. Hunt: AGB Bornem still **JR2024-only**; Dijk92 CDN **2026-00377886 still 403**; FARO NBB still **YE2024**. Took named leftover **Elia Transmission Belgium** (KBO **0731.852.231**; Keizerslaan 20 Brussel; Belgian TSO; Elia Group/Publi-T/Interfin path; NON-Eneco). **BNO done 1933 / Fluxys done 1934 — not redone.**
- Primary hunt: NBB consult SPA HTML only (deposit PDF unresolved). **Medium** euros from [Companyweb](https://www.companyweb.be/en/0731852231/elia-transmission-belgium) + [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/elia-transmission-belgium-0731852231) + KBO (neerlegging **09.06.2026**; YE **31.12.2025**; kapitaal **EUR2,824,448,580**): omzet **EUR1,524,550,649** (flat **+0.14%**); bruto **EUR242,276,439** (**JUMP +23.04%**); PnL **EUR228,371,596** (**DROP -3.64%**); equity **EUR3,860,494,516** (**JUMP +39.79%**); assets **EUR10,452,686,219**; EBITDA **EUR152,687,864**; FTE **611.6**.
- Wrote: sources (+3); budgets (+7); commitments (+1); leaderboard (+1); entities (updated elia); foi + draft gap_etb_nbb_pdf_debt_tariff_equity_jump_l5; rq_1935=done + rq_1936 open; loop_state ticks=1935.
- FOI opened: NBB PDF + debt/tariff/equity JUMP recon (**ready**, human-send only).
- NOT every-10 (**next every-10 is 1940**). Next: rq_1936 (AGB/Dijk92-if-200 / FARO-if-YE2025 / FluxysLNG-otherHVZ-IGS).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1935 write OK")

# tick 2326: leftover dual WZC Sint-Jozef Zonnebeke YE2025
import csv, json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TICK, TS = "2326", "2026-08-28T00:05:00Z"
ENTITY = "vzw_zorgcentrum_sint_jozef_zonnebeke"
GAP = "gap_zonnebeke_sint_jozef_nbb_pdf_assets_debt_omzet_7_25m_pnl_jump_wzc_matrix_l5"
LB = "lb_zonnebeke_sint_jozef_omzet_7_25m_pnl_jump_69pct_fte_101_jr2025"
COMM = "comm_zonnebeke_sint_jozef_jr2025_statutory_wzc_omzet_7_25m"
SRC_EN = "src_zonnebeke_sint_jozef_jr2025_cw_en"
OMZET, BRUTO, PNL, EQUITY, FTE = 7250810, 7157383, 268729, 4943062, 101.0
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 7097174, 6936065, 159351, 4675412, 98.2
RATIO = round(BRUTO / OMZET, 2)
PI = "4.55"  # 0.55*3.5 + 0.35*5.5 + 0.70


def append_csv(path, fields, rows):
    p = Path(path)
    d = p.read_bytes()
    if d and not d.endswith(b"\n"):
        p.write_bytes(d + b"\n")
    with p.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for r in rows:
            w.writerow(r)


rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys())

for r in rq_rows:
    if r.get("task_id") == "rq_2326":
        st, eid = r.get("status"), (r.get("entity_id") or "").strip()
        if st == "done":
            raise SystemExit("rq_2326 already done")
        if st == "in_progress" and eid and eid != ENTITY:
            raise SystemExit(f"rq_2326 race-locked entity={eid}")
        r.update({
            "status": "done",
            "title": f"leftover dual — WZC Sint-Jozef Zonnebeke YE2025 Medium (omzet JUMP {OMZET/1e6:.2f}m / pnl JUMP +69% / FTE {FTE})",
            "entity_id": ENTITY,
            "updated_utc": TS,
            "blocked_gap_id": GAP,
            "notes": (
                f"tick{TICK} Zorgcentrum Sint-Jozef Zonnebeke 0450.265.783 YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl JUMP {PNL} (+68.64%); equity JUMP {EQUITY}; "
                f"FTE {FTE}; 1 VE NACE 87.301 ROB/WZC; neerlegging 04.06.2026; assets/debt Unknown; FOI ready NOT sent"
            ),
        })
        break
else:
    raise SystemExit("rq_2326 not found")

if "rq_2327" not in {x.get("task_id") for x in rq_rows}:
    t = {k: "" for k in rq_fields}
    t.update({
        "task_id": "rq_2327",
        "title": "leftover dual after Zonnebeke Sint-Jozef — prefer AGB/FARO-YE2025/AIESH/Citeco/or-unused ETA-VAPH-WZC",
        "sprint": "hole_fill", "priority": "8", "status": "open",
        "hierarchy_target": "Vlaanderen>dual_structures>leftover_ETA_VAPH_WZC",
        "created_utc": TS, "updated_utc": TS,
        "notes": "spawned after tick2326 Zonnebeke; AGB Bornem JR2024; FARO/AIESH/Citeco YE2024; next EVERY-10 2330",
    })
    rq_rows.append(t)

ent_path = ROOT / "entities.csv"
with ent_path.open(newline="", encoding="utf-8") as f:
    ents = list(csv.DictReader(f))
    ent_fields = list(ents[0].keys())
for e in ents:
    blob = "|".join((e.get(k) or "") for k in e.keys()).lower()
    if e.get("entity_id") == ENTITY or "0450.265.783" in blob:
        raise SystemExit(f"already in entities: {e.get('entity_id')}")

ents.append({
    "entity_id": ENTITY,
    "name_nl": "Zorgcentrum Sint-Jozef VZW (Zonnebeke / WZC ROB)",
    "name_fr": "ASBL Zorgcentrum Sint-Jozef (Zonnebeke / MRS ROB)",
    "name_en": "Zorgcentrum Sint-Jozef VZW (Zonnebeke / nursing home ROB)",
    "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl",
    "website": "https://zorgcentrumsintjozef.be/",
    "foi_email": "info@zorgcentrumsintjozef.be",
    "foi_postal": "Ieperstraat 54, 8980 Zonnebeke",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0450.265.783 Actief VZW RSZ 87.301; "
        f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} (+68.64%) equity JUMP {EQUITY} FTE {FTE}; "
        f"1 VE; neerlegging 04.06.2026; FOI {GAP}; after aPart@2325; AGB/FARO YE2024; not TE-additive"
    ),
})

sources = [
    {"source_id": SRC_EN, "title": "Zonnebeke Sint-Jozef YE2025 Companyweb EN", "url": "https://www.companyweb.be/en/0450265783/zorgcentrum-sint-jozef", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 04-06-2026"},
    {"source_id": "src_zonnebeke_sint_jozef_jr2025_cw_nl", "title": "Zonnebeke Sint-Jozef YE2025 Companyweb NL", "url": "https://www.companyweb.be/nl/0450265783/zorgcentrum-sint-jozef", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL; omzet JUMP {OMZET}; pnl JUMP {PNL}"},
    {"source_id": "src_zonnebeke_sint_jozef_jr2025_cw_fr", "title": "Zonnebeke Sint-Jozef YE2025 Companyweb FR", "url": "https://www.companyweb.be/fr/0450265783/zorgcentrum-sint-jozef", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW FR; CA {OMZET}; bénéfice {PNL}"},
    {"source_id": "src_zonnebeke_sint_jozef_kbo_0450265783", "title": "KBO Zorgcentrum Sint-Jozef 0450.265.783", "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=450265783", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-28", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW sinds 12.05.1993; 1 VE; RSZ NACE 87.301; Ieperstraat 54 8980 Zonnebeke"},
    {"source_id": "src_zonnebeke_sint_jozef_site_foi_2326", "title": "Zonnebeke Sint-Jozef FOI channel info@zorgcentrumsintjozef.be", "url": "https://zorgcentrumsintjozef.be/", "publisher": "Zorgcentrum Sint-Jozef VZW", "accessed_date": "2026-08-28", "source_class": "foi_contact", "notes": f"tick{TICK}; info@zorgcentrumsintjozef.be; 051 46 09 90; WZC/CVK/AV/DVC Zonnebeke"},
]
budgets = [
    {"budget_id": "bud_zonnebeke_sj_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": OMZET, "amount_min_eur": OMZET, "amount_max_eur": OMZET, "basis": "CW statutory omzet YE2025 primary WZC", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; +2.16% vs {OMZET24}"},
    {"budget_id": "bud_zonnebeke_sj_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": BRUTO, "amount_min_eur": BRUTO, "amount_max_eur": BRUTO, "basis": "CW bruto YE2025", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; +3.19% vs {BRUTO24}"},
    {"budget_id": "bud_zonnebeke_sj_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": PNL, "amount_min_eur": PNL, "amount_max_eur": PNL, "basis": "CW pnl YE2025 JUMP", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; +68.64% vs {PNL24}"},
    {"budget_id": "bud_zonnebeke_sj_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": EQUITY, "amount_min_eur": EQUITY, "amount_max_eur": EQUITY, "basis": "CW equity YE2025", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; +5.72% vs {EQUITY24}"},
    {"budget_id": "bud_zonnebeke_sj_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": FTE, "amount_min_eur": FTE, "amount_max_eur": FTE, "basis": f"CW FTE {FTE}", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; vs {FTE24}"},
    {"budget_id": "bud_zonnebeke_sj_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": PNL24, "amount_min_eur": PNL24, "amount_max_eur": PNL24, "basis": "CW pnl YE2024 cmp", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; cmp"},
]
cash = {"2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE, "2024_omzet": OMZET24, "2024_bruto": BRUTO24, "2024_pnl": PNL24, "2024_equity": EQUITY24, "2024_fte": FTE24}
commitments = [{
    "commitment_id": COMM,
    "title": f"Zonnebeke Sint-Jozef YE2025 leftover dual (omzet {OMZET/1e6:.2f}m / pnl JUMP +69% / Medium)",
    "entity_id": ENTITY, "beneficiary": "WZC/ROB residents Zonnebeke",
    "legal_basis": "VZW Zorgcentrum Sint-Jozef (KBO 0450.265.783; Actief; RSZ 87.301)",
    "decision_date": "2026-06-04", "start_year": "2025", "end_year": "2025",
    "total_envelope_eur": OMZET, "cash_by_year": json.dumps(cash, separators=(",", ":")),
    "remaining_eur": "0", "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0450265783/zorgcentrum-sint-jozef",
    "stated_goal": "Flemish WZC/ROB residential elderly care Zonnebeke",
    "cut_option": "Publish NBB PDF; reconcile pnl JUMP +69% + assets/debt vs WZC matrix",
    "source_id": SRC_EN, "confidence": "medium",
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Zonnebeke>Sint_Jozef_WZC>JR2025_statutory_L5",
    "notes": f"tick{TICK}; after aPart@2325",
}]
leaderboard = [{
    "item_id": LB,
    "name": f"Zonnebeke Sint-Jozef omzet {OMZET/1e6:.2f}m / pnl JUMP +69% / FTE {FTE} (YE2025)",
    "level": "L5", "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Zonnebeke>Sint_Jozef_WZC>JR2025",
    "annual_cost_eur": OMZET, "total_cost_eur": OMZET,
    "tco_notes": f"CW omzet JUMP {OMZET} / bruto {BRUTO} / pnl JUMP {PNL} (+68.64% vs {PNL24}) / equity {EQUITY} / FTE {FTE} / filed 04.06.2026",
    "confidence": "medium", "source_id": SRC_EN,
    "beneficiaries": "WZC/ROB elderly Zonnebeke",
    "stated_goal": "Flemish nursing-home residential care",
    "measured_outcome": f"omzet {OMZET/1e6:.2f}m; pnl JUMP +69%; FTE {FTE}",
    "absurdity_score": "5.5", "cost_score": "3.5", "difficulty": "3.0", "priority_index": PI,
    "cut_proposal": "Publish NBB PDF FOI; reconcile pnl JUMP +69% + assets/debt",
    "status": "open", "struck_reason": "",
    "notes": f"tick{TICK}; FOI {GAP}; after aPart@2325",
}]
with (ROOT / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    foi_fields = list(csv.DictReader(f).fieldnames)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>West_Vlaanderen>Zonnebeke>Sint_Jozef_WZC>NBB_PDF_assets_debt_omzet_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025; assets/debt; why pnl JUMP EUR{PNL} (+68.64% vs EUR{PNL24}) on omzet EUR{OMZET}",
    "why_it_matters": f"Medium CW WZC Zonnebeke (omzet {OMZET/1e6:.2f}m / pnl JUMP +69% / FTE {FTE})",
    "priority": "8", "recipient_body": "Zorgcentrum Sint-Jozef VZW",
    "recipient_email": "info@zorgcentrumsintjozef.be",
    "recipient_postal": "Ieperstraat 54, 8980 Zonnebeke",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md", "status": "ready", "date_ready": "2026-08-28",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": COMM, "linked_leaderboard_id": LB,
    "created_utc": TS, "updated_utc": TS,
    "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO",
}

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader(); w.writerows(rq_rows)
with ent_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ent_fields, lineterminator="\n")
    w.writeheader(); w.writerows(ents)
append_csv(ROOT / "sources.csv", ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"], sources)
append_csv(ROOT / "budgets.csv", ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"], budgets)
append_csv(ROOT / "commitments.csv", ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"], commitments)
append_csv(ROOT / "leaderboard.csv", ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"], leaderboard)
append_csv(ROOT / "foi_queue.csv", foi_fields, [foi])

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Zonnebeke Sint-Jozef (NBB PDF / omzet 7.25m / pnl JUMP +69%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Zorgcentrum Sint-Jozef VZW — KBO **0450.265.783** (Actief; Ieperstraat 54, 8980 Zonnebeke; FTE {FTE}; NACE **87.301** ROB/WZC)  
**recipient:** info@zorgcentrumsintjozef.be · Ieperstraat 54, 8980 Zonnebeke  
**sources:** [CW EN](https://www.companyweb.be/en/0450265783/zorgcentrum-sint-jozef) · [CW NL](https://www.companyweb.be/nl/0450265783/zorgcentrum-sint-jozef) · [CW FR](https://www.companyweb.be/fr/0450265783/zorgcentrum-sint-jozef) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=450265783) · [site](https://zorgcentrumsintjozef.be/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0450265783)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN+FR YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Zorgcentrum Sint-Jozef** sinds **12.05.1993**; **1 VE**; zetel Ieperstraat 54, 8980 Zonnebeke; RSZ NACE **87.301**.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +2.16%; bruto **EUR{BRUTO:,}**; pnl **EUR{PNL:,}** JUMP +68.64%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **04.06.2026**.
- After aPart@2325. Stalls: AGB Bornem JR2024; FARO/AIESH/Citeco YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Zorgcentrum Sint-Jozef VZW
via info@zorgcentrumsintjozef.be
Ieperstraat 54, 8980 Zonnebeke
Betreft: Openbaarmaking jaarrekening 2025 Zorgcentrum Sint-Jozef (KBO 0450.265.783)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaanderen / Bestuursdecreet), vraag ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting pnl JUMP EUR{PNL} (+68.64% vs YE2024 EUR{PNL24}) bij omzet EUR{OMZET}.
3. Overzicht publieke toelagen/RVT-financiering YE2025.
4. Schulden LT/KT en liquide middelen YE2025.
5. Toelichting FTE {FTE} vs YE2024 {FTE24}.

Periode YE2025 (+ YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

ls_path = ROOT / "loop_state.csv"
with ls_path.open(newline="", encoding="utf-8") as f:
    ls = list(csv.DictReader(f)); lf = list(ls[0].keys())
for row in ls:
    if row.get("state_id") == "main":
        row.update({
            "mode": "continuous", "current_sprint": "hole_fill", "last_tick_utc": TS,
            "last_unit_id": "rq_2326", "ticks_completed": TICK, "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Zorgcentrum Sint-Jozef Zonnebeke 0450.265.783 Medium "
                f"(omzet JUMP {OMZET}; bruto JUMP {BRUTO}; pnl JUMP {PNL} +68.64%; equity JUMP {EQUITY}; "
                f"FTE {FTE}; 1 VE WZC Zonnebeke); after aPart@2325; AGB Bornem JR2024; "
                f"FARO/AIESH/Citeco YE2024; next rq_2327; next EVERY-10 2330"
            ),
        })
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lf, lineterminator="\n")
    w.writeheader(); w.writerows(ls)

with Path("docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(f"""
## tick {TICK} — {TS} — rq_2326 Zonnebeke Sint-Jozef YE2025

- **Unit:** leftover dual WZC VZW Zorgcentrum Sint-Jozef (KBO 0450.265.783) Zonnebeke after aPart@2325.
- **Primary €:** omzet **EUR{OMZET}**; Medium CW; PI **{PI}**.
- **Also:** pnl JUMP EUR{PNL} (+68.64%); bruto EUR{BRUTO}; equity EUR{EQUITY}; FTE {FTE}; filed 04.06.2026.
- **Writes:** entities/sources/budgets/commitments/leaderboard + FOI `{GAP}` ready NOT sent.
- **Stalls:** AGB Bornem JR2024; FARO/AIESH/Citeco YE2024.
- **Next:** rq_2327 open; next EVERY-10 **2330**.
""")
print(f"DONE {TICK} omzet={OMZET} pnl={PNL} PI={PI}")

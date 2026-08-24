# tick 2325: leftover dual aPart Gent YE2025 (Het Eepos/Pleegzorg stalls or races)
import csv, json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TICK, TS = "2325", "2026-08-28T00:25:00Z"
ENTITY = "vzw_apart_gent"
GAP = "gap_apart_nbb_pdf_assets_debt_bruto_gt_omzet_419_67x_pnl_drop_99pct_jeugdhulp_matrix_l5"
LB = "lb_apart_bruto_8_79m_gt_omzet_419_67x_pnl_drop_99pct_jr2025"
COMM = "comm_apart_jr2025_statutory_bruto_8_79m_gt_omzet_419_67x"
SRC_EN = "src_apart_jr2025_cw_en"
OMZET, BRUTO, PNL, EQUITY, FTE = 20940, 8787800, 3607, 4025991, 115.7
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 26679, 8354144, 856164, 4037002, 110.8
RATIO = round(BRUTO / OMZET, 2)
PI = "6.55"  # 0.55*5.0 + 0.35*8.5 + 0.1*7


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
    if r.get("task_id") == "rq_2325":
        st, eid = r.get("status"), (r.get("entity_id") or "").strip()
        if st == "done":
            raise SystemExit("rq_2325 already done")
        if st == "in_progress" and eid and eid != ENTITY and "apart" not in eid:
            # allow override of known stalls/races only if same tick reclaim
            if eid not in (
                "vzw_het_eepos_laakdal",
                "vzw_pleegzorg_west_vlaanderen",
            ):
                raise SystemExit(f"rq_2325 race-locked entity={eid}")
        r.update({
            "status": "done",
            "title": (
                f"leftover dual — aPart Gent YE2025 Medium "
                f"(bruto JUMP 8.79m / ~{RATIO}x omzet / pnl DROP -99.58% / FTE JUMP {FTE})"
            ),
            "entity_id": ENTITY,
            "hierarchy_target": "L5",
            "updated_utc": TS,
            "blocked_gap_id": GAP,
            "notes": (
                f"tick{TICK}; aPart 0567.657.460 Medium CW NL+EN + Strong KBO; "
                f"omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL}; equity {EQUITY}; "
                f"FTE JUMP {FTE}; 12 VE NACE 87.991 jeugdhulp; neerlegging 24.06.2026; "
                f"assets/debt Unknown; FOI ready NOT sent; Het Eepos CW N/A stall"
            ),
        })
        break
else:
    raise SystemExit("rq_2325 not found")

if "rq_2326" not in {x.get("task_id") for x in rq_rows}:
    t = {k: "" for k in rq_fields}
    t.update({
        "task_id": "rq_2326",
        "title": "leftover dual after aPart — prefer AGB/FARO-YE2025/AIESH/Citeco/or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill", "priority": "8", "status": "open",
        "hierarchy_target": "Vlaanderen>dual_structures>leftover_ETA_VAPH_WZC",
        "created_utc": TS, "updated_utc": TS,
        "notes": "spawned after tick2325 aPart; AGB Bornem JR2024; FARO/AIESH/Citeco/Het Eepos YE2024-or-N/A; next EVERY-10 2330",
    })
    rq_rows.append(t)

ent_path = ROOT / "entities.csv"
with ent_path.open(newline="", encoding="utf-8") as f:
    ents = list(csv.DictReader(f))
    ent_fields = list(ents[0].keys())
for e in ents:
    blob = "|".join((e.get(k) or "") for k in e.keys()).lower()
    if e.get("entity_id") == ENTITY or "0567.657.460" in blob:
        raise SystemExit(f"already in entities: {e.get('entity_id')}")

ents.append({
    "entity_id": ENTITY,
    "name_nl": "aPart VZW (Gent / integrale jeugdhulp met huisvesting)",
    "name_fr": "aPart ASBL (Gand / aide à la jeunesse avec hébergement)",
    "name_en": "aPart VZW (Ghent / youth care with accommodation)",
    "level": "parastatal", "parent_id": "sec_flanders", "community_language": "nl",
    "website": "https://vzwapart.be",
    "foi_email": "raf.demulder@vzwapart.be",
    "foi_postal": "Brandstraat 3, 9000 Gent",
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN + Strong KBO 0567.657.460 Actief VZW RSZ 87.991; "
        f"omzet DROP {OMZET} bruto JUMP {BRUTO} ~{RATIO}x pnl DROP {PNL} equity {EQUITY} FTE JUMP {FTE}; "
        f"12 VE; neerlegging 24.06.2026; FOI {GAP}; after Ritmica@2324; Het Eepos CW N/A; not TE-additive"
    ),
})

sources = [
    {"source_id": SRC_EN, "title": "aPart YE2025 Companyweb EN", "url": "https://www.companyweb.be/en/0567657460/apart", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} ~{RATIO}x pnl {PNL} equity {EQUITY} FTE {FTE}; filed 24-06-2026"},
    {"source_id": "src_apart_jr2025_cw_nl", "title": "aPart YE2025 Companyweb NL", "url": "https://www.companyweb.be/nl/0567657460/apart", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL; bruto JUMP {BRUTO} (~{RATIO}x omzet); pnl DROP -99.58%"},
    {"source_id": "src_apart_kbo_0567657460", "title": "KBO aPart 0567.657.460", "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=567657460", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-28", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW sinds 14.10.2014; 12 VE; RSZ NACE 87.991; Brandstraat 3 9000 Gent"},
    {"source_id": "src_apart_foi_2325", "title": "aPart FOI channel raf.demulder@vzwapart.be", "url": "https://vzwapart.be", "publisher": "vzw aPart", "accessed_date": "2026-08-28", "source_class": "foi_contact", "notes": f"tick{TICK}; raf.demulder@vzwapart.be; 09/225.01.59; Brandstraat 3 Gent"},
    {"source_id": "src_het_eepos_stall_cw_2325", "title": "Het Eepos CW balansjaar N/A stall (preferred unused)", "url": "https://www.companyweb.be/nl/0886198829/het-eepos", "publisher": "Companyweb", "accessed_date": "2026-08-28", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; preferred Het Eepos 0886.198.829 CW balansjaar N/A / BBC JR2024-only; took FREE aPart YE2025"},
]
budgets = [
    {"budget_id": "bud_apart_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": OMZET, "amount_min_eur": OMZET, "amount_max_eur": OMZET, "basis": "CW statutory omzet YE2025", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; DROP -21.51% vs {OMZET24}"},
    {"budget_id": "bud_apart_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": BRUTO, "amount_min_eur": BRUTO, "amount_max_eur": BRUTO, "basis": f"CW bruto YE2025 ~{RATIO}x omzet primary", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; JUMP +5.19% vs {BRUTO24}; opacity ~{RATIO}x"},
    {"budget_id": "bud_apart_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": PNL, "amount_min_eur": PNL, "amount_max_eur": PNL, "basis": "CW pnl YE2025 DROP -99.58%", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; DROP vs {PNL24}"},
    {"budget_id": "bud_apart_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": EQUITY, "amount_min_eur": EQUITY, "amount_max_eur": EQUITY, "basis": "CW equity YE2025", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; FLAT -0.27% vs {EQUITY24}"},
    {"budget_id": "bud_apart_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": FTE, "amount_min_eur": FTE, "amount_max_eur": FTE, "basis": f"CW FTE {FTE}", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; JUMP vs {FTE24}"},
]
cash = {
    "2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE,
    "2024_omzet": OMZET24, "2024_bruto": BRUTO24, "2024_pnl": PNL24, "2024_equity": EQUITY24, "2024_fte": FTE24,
    "bruto_omzet_ratio": RATIO,
}
commitments = [{
    "commitment_id": COMM,
    "title": f"aPart Gent YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m ~{RATIO}x omzet / Medium)",
    "entity_id": ENTITY, "beneficiary": "vulnerable youth / youth care East Flanders",
    "legal_basis": "VZW aPart (KBO 0567.657.460; Actief; RSZ 87.991)",
    "decision_date": "2026-06-24", "start_year": "2025", "end_year": "2025",
    "total_envelope_eur": BRUTO, "cash_by_year": json.dumps(cash, separators=(",", ":")),
    "remaining_eur": "0", "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0567657460/apart",
    "stated_goal": "Flemish integrale jeugdhulp with accommodation (CANO etc.)",
    "cut_option": f"Publish NBB PDF; reconcile bruto~{RATIO}x omzet + Opgroeien subsidy matrix",
    "source_id": SRC_EN, "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>aPart>JR2025_statutory_L5",
    "notes": f"tick{TICK}; after Ritmica@2324; Het Eepos stall",
}]
leaderboard = [{
    "item_id": LB,
    "name": f"aPart bruto {BRUTO/1e6:.2f}m ~{RATIO}x omzet / pnl DROP -99.58% (YE2025)",
    "level": "L5", "type": "jeugdhulp_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>aPart>JR2025",
    "annual_cost_eur": BRUTO, "total_cost_eur": BRUTO,
    "tco_notes": f"CW omzet DROP {OMZET} / bruto JUMP {BRUTO} ~{RATIO}x / pnl DROP {PNL} / equity {EQUITY} / FTE JUMP {FTE} / filed 24.06.2026",
    "confidence": "medium", "source_id": SRC_EN,
    "beneficiaries": "vulnerable children/youth East Flanders",
    "stated_goal": "Opgroeien-adjacent integrale jeugdhulp with housing",
    "measured_outcome": f"bruto~{RATIO}x omzet opacity; pnl crater -99.58%; FTE JUMP {FTE}",
    "absurdity_score": "8.5", "cost_score": "5.0", "difficulty": "3.0", "priority_index": PI,
    "cut_proposal": f"Publish NBB PDF FOI; reconcile ~{RATIO}x bruto/omzet + subsidy flows",
    "status": "open", "struck_reason": "",
    "notes": f"tick{TICK}; FOI {GAP}; after Ritmica@2324",
}]
with (ROOT / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    foi_fields = list(csv.DictReader(f).fieldnames)
foi = {
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>aPart>NBB_PDF_assets_debt_bruto_gt_omzet",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025; assets/debt; why bruto EUR{BRUTO} ~{RATIO}x omzet EUR{OMZET}; Opgroeien subsidy matrix; pnl crater",
    "why_it_matters": f"Medium CW jeugdhulp (bruto {BRUTO/1e6:.2f}m ~{RATIO}x omzet / pnl DROP -99.58% / FTE JUMP {FTE})",
    "priority": "8", "recipient_body": "aPart VZW",
    "recipient_email": "raf.demulder@vzwapart.be",
    "recipient_postal": "Brandstraat 3, 9000 Gent",
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
    f"""# FOI draft — aPart Gent (NBB PDF / bruto ~{RATIO}x omzet / pnl DROP -99.58%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** aPart VZW — KBO **0567.657.460** (Actief; Brandstraat 3, 9000 Gent; FTE {FTE}; NACE **87.991**)  
**recipient:** raf.demulder@vzwapart.be · Brandstraat 3, 9000 Gent  
**sources:** [CW EN](https://www.companyweb.be/en/0567657460/apart) · [CW NL](https://www.companyweb.be/nl/0567657460/apart) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=567657460) · [site](https://vzwapart.be) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0567657460)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **aPart** sinds **14.10.2014**; **12 VE**; RSZ NACE **87.991** Integrale jeugdhulp met huisvesting; zetel Brandstraat 3, 9000 Gent.
- CW YE2025: omzet **EUR{OMZET:,}** DROP −21.51%; bruto **EUR{BRUTO:,}** JUMP +5.19% (~**{RATIO}x**); pnl **EUR{PNL:,}** DROP −99.58%; equity **EUR{EQUITY:,}**; FTE **{FTE}** JUMP; filed **24.06.2026**.
- After Ritmica@2324. Preferred Het Eepos CW balansjaar N/A / BBC JR2024-only — stall; took FREE aPart.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: aPart VZW
via raf.demulder@vzwapart.be
Brandstraat 3, 9000 Gent
Betreft: Openbaarheid jaarrekening 2025 aPart (KBO 0567.657.460)

Geachte,

Op grond van het Bestuursdecreet (openbaarheid van bestuur) vraag ik:

1. PDF NBB/CBCSO jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting waarom brutomarge EUR{BRUTO} ~{RATIO}x omzet EUR{OMZET} bedraagt.
3. Overzicht Opgroeien / andere publieke subsidies YE2025 (en YE2024).
4. LT/KT schulden en liquiditeiten YE2025.
5. Verklaring pnl DROP EUR{PNL} (−99.58% vs YE2024 EUR{PNL24}).

Periode YE2025 (+ YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

raw = Path(f"docs/doge/data/raw/tick{TICK}")
raw.mkdir(parents=True, exist_ok=True)
(raw / "cw_summary.json").write_text(json.dumps({
    "kbo": "0567.657.460", "entity": ENTITY, "year": 2025,
    "omzet": OMZET, "bruto": BRUTO, "ratio": RATIO, "pnl": PNL, "equity": EQUITY, "fte": FTE,
    "filed": "2026-06-24", "confidence": "medium",
}, indent=2), encoding="utf-8")

ls_path = ROOT / "loop_state.csv"
with ls_path.open(newline="", encoding="utf-8") as f:
    ls = list(csv.DictReader(f)); lf = list(ls[0].keys())
for row in ls:
    if row.get("state_id") == "main":
        row.update({
            "mode": "continuous", "current_sprint": "hole_fill", "last_tick_utc": TS,
            "last_unit_id": "rq_2325", "ticks_completed": TICK, "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual aPart Gent 0567.657.460 Medium "
                f"(omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL}; equity {EQUITY}; "
                f"FTE JUMP {FTE}; 12 VE jeugdhulp Gent); after Ritmica@2324; "
                f"Het Eepos CW N/A stall; AGB/FARO YE2024; next rq_2326; next EVERY-10 2330"
            ),
        })
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lf, lineterminator="\n")
    w.writeheader(); w.writerows(ls)

with Path("docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(f"""
## tick {TICK} — {TS} — rq_2325 aPart Gent YE2025

- **Unit:** leftover dual Flemish jeugdhulp VZW aPart (KBO 0567.657.460) Gent after Ritmica@2324.
- **Primary €:** bruto **EUR{BRUTO}** (~**{RATIO}x** omzet EUR{OMZET}); Medium CW; PI **{PI}**.
- **Also:** pnl DROP EUR{PNL} (−99.58%); equity EUR{EQUITY}; FTE JUMP {FTE}; filed 24.06.2026; 12 VE RSZ 87.991.
- **Writes:** entities/sources/budgets/commitments/leaderboard + FOI `{GAP}` ready NOT sent.
- **Stalls:** Het Eepos CW balansjaar N/A / BBC JR2024; AGB Bornem JR2024; FARO/AIESH/Citeco YE2024.
- **Next:** rq_2326 open; next EVERY-10 **2330**.
""")
print(f"DONE {TICK} bruto={BRUTO} ratio={RATIO}x pnl={PNL} PI={PI}")

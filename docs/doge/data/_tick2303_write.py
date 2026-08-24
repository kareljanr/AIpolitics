# tick2303: Voluit YE2025 leftover dual Medium (after MLP@2302)
from pathlib import Path
import csv, json
csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2303"
raw.mkdir(parents=True, exist_ok=True)

TICK, UTC = "2303", "2026-08-27T18:45:00Z"
ENTITY, KBO, KBO_DIGITS = "vzw_voluit_evergem", "0420.982.473", "0420982473"
OMZET, BRUTO, PNL, EQUITY, FTE = 2268150, 16778853, 320032, 7512588, 206.2
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 2309634, 15730843, 546023, 7286565, 198.7
RATIO = round(BRUTO / OMZET, 2)  # 7.40
GAP = "gap_voluit_nbb_pdf_assets_debt_bruto_gt_omzet_7_4x_pnl_drop_41pct_fte_jump_vaph_matrix_l5"
LB = "lb_voluit_bruto_16_78m_omzet_2_27m_7_4x_pnl_drop_41pct_fte_jump_jr2025"
COMM = "comm_voluit_jr2025_statutory_vaph_bruto_16_78m_7_4x_pnl_drop"
RQ, RQ_NEXT = "rq_2303", "rq_2304"
SRC_EN, SRC_NL, SRC_FR = "src_voluit_jr2025_cw_en", "src_voluit_jr2025_cw_nl", "src_voluit_jr2025_cw_fr"
SRC_KBO, SRC_SITE = "src_voluit_kbo_0420982473", "src_voluit_site_contact_2303"
ABS, COST, DIFF = 7.6, 6.0, 3.0
PI = round((ABS + COST) / 2, 2)  # 6.80
EMAIL = "info@voluit.be"
ADDR = "Kramershoek 39, 9940 Evergem"
FILED = "16.06.2026"


def append_csv(path, rows, id_key):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, existing = reader.fieldnames, list(reader)
    have = {r.get(id_key) for r in existing}
    new = [r for r in rows if r.get(id_key) not in have]
    if not new:
        print(path.name, "already")
        return
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(path.name, "+", len(new))


def upsert_rq():
    path = data / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, rows = reader.fieldnames, list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            r.update({
                "status": "done",
                "entity_id": ENTITY,
                "updated_utc": UTC,
                "blocked_gap_id": GAP,
                "title": f"leftover dual — Voluit YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl DROP -41% / FTE JUMP {FTE})",
                "notes": (
                    f"tick{TICK}: Voluit YE2025 Medium (omzet DROP {OMZET} -1.8%; bruto JUMP {BRUTO} ~{RATIO}x; "
                    f"pnl DROP {PNL} -41.39%; equity JUMP {EQUITY}; FTE JUMP {FTE}; 7 VE VAPH Evergem NACE 87.202 "
                    f"aanbestedende overheid); FOI {GAP} ready not sent; after MLP@2302; stalls AGB/FARO/AIESH YE2024"
                ),
            })
            found = True
            break
    if not found:
        raise SystemExit("missing " + RQ)
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": "leftover dual after Voluit — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Voluit YE2025 Medium (omzet DROP {OMZET/1e6:.2f}m / bruto~{RATIO}x / pnl DROP -41%). "
                "Prefer AGB/FARO if YE2025 else unused ETA-VAPH-WZC-maatwerk (Gandae YE2024). "
                "Do NOT redo Voluit/MLP/Havinet/De Kiem/MPI Oosterlo/JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove/"
                "Entiris/Mirto/Blankedale/Werkmmaat/Lidwina/Zonnelied stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK} Voluit; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; next EVERY-10 2310",
        })
        print("rq_next spawned", RQ_NEXT)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print("research_queue updated")


ls_path = data / "loop_state.csv"
with ls_path.open(encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
ticks = int(ls[0].get("ticks_completed") or 0)
if ticks >= 2303:
    raise SystemExit(f"already past 2303 (ticks={ticks})")
if ticks != 2302:
    print(f"WARN ticks={ticks} expected 2302; continuing if rq_2303 open")

append_csv(data / "sources.csv", [
    {"source_id": SRC_EN, "title": "Voluit YE2025 Companyweb EN", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/voluit", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed {FILED}; assets/debt Unknown"},
    {"source_id": SRC_NL, "title": "Voluit YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/voluit", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging {FILED}; Groot {FTE} FTE"},
    {"source_id": SRC_FR, "title": "Voluit YE2025 Companyweb FR", "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/voluit", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Evergem; CA {OMZET}; marge brute {BRUTO}; benefice {PNL}"},
    {"source_id": SRC_KBO, "title": f"KBO Voluit {KBO}", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW sinds 13.10.1980; 7 VE; {ADDR}; RSZ 87.202; aanbestedende overheid sinds 18.01.2003; naam VOLUIT sinds 01.01.2023"},
    {"source_id": SRC_SITE, "title": f"Voluit FOI channel {EMAIL}", "url": "https://voluit.be/over-voluit/", "publisher": "Voluit VZW", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; {EMAIL}; +32 9 253 63 52; {ADDR}; also Groot Begijnhof 10 9040 Gent"},
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_voluit_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; omzet DROP -1.8% vs YE2024 {OMZET24}"},
    {"budget_id": "bud_voluit_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; bruto JUMP +6.66% vs YE2024 {BRUTO24}; bruto/omzet ~{RATIO}x"},
    {"budget_id": "bud_voluit_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; pnl DROP -41.39% vs YE2024 {PNL24}"},
    {"budget_id": "bud_voluit_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; equity JUMP +3.1% vs YE2024 {EQUITY24}"},
    {"budget_id": "bud_voluit_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE24}; assets/debt Unknown"},
    {"budget_id": "bud_voluit_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL24), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative"},
], "budget_id")

cash = json.dumps({
    "2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE,
    "2024_omzet": OMZET24, "2024_bruto": BRUTO24, "2024_pnl": PNL24, "2024_equity": EQUITY24, "2024_fte": FTE24,
}, separators=(",", ":"))
append_csv(data / "commitments.csv", [{
    "commitment_id": COMM,
    "title": f"Voluit YE2025 leftover dual (bruto {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl DROP -41% / FTE JUMP {FTE} / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "VAPH adults with mental disability / begeleid wonen Evergem-Gent path",
    "legal_basis": f"VZW VOLUIT (KBO {KBO}; Actief; 7 VE; RSZ 87.202; aanbestedende overheid)",
    "decision_date": "2026-06-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/voluit",
    "stated_goal": "Flemish VAPH residential care for adults with mental disability (Evergem)",
    "cut_option": f"Publish NBB PDF assets/debt; disclose VAPH matrix behind bruto~{RATIO}x omzet + pnl DROP -41%",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Evergem>Voluit>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; omzet {OMZET} ~{RATIO}x; FOI {GAP}; not TE-additive",
}], "commitment_id")

append_csv(data / "leaderboard.csv", [{
    "item_id": LB,
    "name": f"Voluit bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / pnl DROP -41% / FTE JUMP {FTE} (YE2025 VAPH Evergem)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Evergem>Voluit>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": (
        f"CW omzet DROP {OMZET} (-1.8%) / bruto JUMP {BRUTO} (+6.66%; ~{RATIO}x) / pnl DROP {PNL} (-41.39%) / "
        f"equity JUMP {EQUITY} (+3.1%) / FTE JUMP {FTE} (vs {FTE24}) / 7 VE VAPH NACE 87.202"
    ),
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "VAPH adults with mental disability Evergem / Gent belt",
    "stated_goal": "Residential + mobile support disability",
    "measured_outcome": f"omzet DROP -1.8%; bruto JUMP +6.66% (~{RATIO}x); pnl DROP -41.39%; equity JUMP +3.1%; FTE JUMP {FTE}; filed {FILED}",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose VAPH matrix behind bruto>~{RATIO}x omzet despite pnl DROP -41%",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK}; Medium CW NL+EN+FR; FOI {GAP}; after MLP@2302; AGB/FARO/AIESH YE2024",
}], "item_id")

append_csv(data / "entities.csv", [{
    "entity_id": ENTITY,
    "name_nl": "Voluit VZW (Evergem / VAPH volwassenen mentale handicap)",
    "name_fr": "Voluit ASBL (Evergem / VAPH adultes handicap mental)",
    "name_en": "Voluit ASBL (Evergem VAPH residential care mental disability)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://voluit.be/",
    "foi_email": EMAIL,
    "foi_postal": ADDR,
    "notes": (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 7 VE VZW RSZ 87.202 aanbestedende overheid; "
        f"omzet DROP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; "
        f"neerlegging {FILED}; FOI {GAP}; after MLP@2302; not TE-additive"
    ),
}], "entity_id")

append_csv(data / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Evergem>Voluit>NBB_PDF_assets_debt_bruto_gt_omzet_7_4x_pnl_drop_vaph",
    "entity_id": ENTITY,
    "what_is_missing": (
        f"NBB PDF YE2025 full (assets/debt/cash); omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); "
        f"pnl DROP EUR{PNL} (-41.39%); FTE JUMP {FTE}; VAPH/persoonsvolgende financing matrix"
    ),
    "why_it_matters": (
        f"Medium CW shows VAPH Evergem residential VZW (bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet / pnl DROP -41% / "
        f"FTE JUMP {FTE} / 7 VE); assets/debt unpublished; public care subsidy opacity"
    ),
    "priority": "8",
    "recipient_body": "Voluit VZW",
    "recipient_email": EMAIL,
    "recipient_postal": ADDR,
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK}; ready NOT sent; Medium CW NL+EN+FR + Strong KBO; after MLP@2302",
}], "gap_id")

upsert_rq()
ls_path.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    + (
        f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,"
        f"tick{TICK} leftover dual Voluit {KBO} Medium (omzet DROP {OMZET} -1.8%; bruto JUMP {BRUTO} ~{RATIO}x; "
        f"pnl DROP {PNL} -41.39%; equity JUMP {EQUITY} +3.1%; FTE JUMP {FTE}; 7 VE VAPH Evergem); "
        f"after MLP@2302; AGB Bornem JR2024; FARO/AIESH YE2024; next {RQ_NEXT}; next EVERY-10 2310; continuous hole_fill\n"
    ),
    encoding="utf-8",
)
(raw / "summary.json").write_text(json.dumps({
    "tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO,
    "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE,
    "ratio_bruto_omzet": RATIO, "confidence": "medium", "gap": GAP,
}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(
    f"Voluit YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE} filed {FILED} {EMAIL}\n",
    encoding="utf-8",
)

log = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - {RQ} Voluit Evergem (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl DROP -41% / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **MLP@2302**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH/Citeco/Groupe Foes/Gandae still **YE2024**. Took FREE Flemish VAPH **Voluit VZW** YE2025 (KBO **{KBO}**; {ADDR}; **Actief** **7 VE**; RSZ **87.202**; aanbestedende overheid; {EMAIL}). Do not redo MLP/Havinet/De Kiem/MPI Oosterlo/JOMI/De Stobbe/De Okkernoot/SOBO/Lidwina/Zonnelied stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP -1.8% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +6.66% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -41.39% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +3.1%; FTE **{FTE}** JUMP (vs {FTE24}); neerlegging **{FILED}**. Strong KBO Actief 7 VE. Assets/debt Unknown. Medium. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2300**; next **2310**). Next: {RQ_NEXT} (AGB/FARO-if-YE2025 / AIESH / unused ETA-VAPH-WZC-maatwerk).
"""
text = log.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print("loop_log ok")

(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — Voluit (NBB PDF / bruto~{RATIO}x omzet / pnl DROP -41% / VAPH)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Voluit VZW — KBO **{KBO}** (Actief; {ADDR}; **7 VE**; FTE {FTE}; RSZ **87.202**; VAPH adults mental disability; aanbestedende overheid)  
**recipient:** {EMAIL} · {ADDR} (+32 9 253 63 52)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}/voluit) · [CW NL](https://www.companyweb.be/nl/{KBO_DIGITS}/voluit) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [site](https://voluit.be/over-voluit/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW NL+EN+FR YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds **13.10.1980**; naam **VOLUIT** sinds **01.01.2023**; **7 VE**; zetel {ADDR}; RSZ **87.202**; aanbestedende overheid sinds **18.01.2003**.
- CW YE2025: omzet **EUR{OMZET:,}** DROP -1.8%; bruto **EUR{BRUTO:,}** JUMP +6.66% (~{RATIO}x); pnl **EUR{PNL:,}** DROP -41.39%; equity **EUR{EQUITY:,}**; FTE **{FTE}**; filed **{FILED}**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH YE2024. After MLP@2302. DISTINCT Lidwina Mol / Zonnelied Roosdaal / Havinet Grimbergen.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Voluit VZW
via {EMAIL}
{ADDR}
Betreft: Openbaarmaking jaarrekening 2025 Voluit (KBO {KBO})

Geachte,

Op grond van openbaarheid van bestuur (Vlaams Bestuursdecreet), vraag ik:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten; activa/schulden/cash).
2. Toelichting omzet DROP EUR{OMZET} naast bruto EUR{BRUTO} (~{RATIO}x),
   pnl DROP EUR{PNL} (-41.39%) en FTE JUMP {FTE} (vs {FTE24}).
3. Overzicht VAPH-/persoonsvolgende vergoedingen achter bruto~{RATIO}x omzet.
4. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("DONE", TICK, "pi", PI, "bruto", BRUTO, "ratio", RATIO)

import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-28T01:30:00Z"
ROOT = Path("docs/doge/data")
Path("docs/doge/data/raw/tick2332").mkdir(parents=True, exist_ok=True)
Path("docs/doge/foi/drafts").mkdir(parents=True, exist_ok=True)

GAP = "gap_gielsbos_nbb_pdf_assets_debt_bruto_gt_omzet_7_80x_pnl_jump_vaph_matrix_l5"
LB = "lb_gielsbos_bruto_41_72m_gt_omzet_7_80x_pnl_jump_fte_509_jr2025"
COMM = "comm_gielsbos_jr2025_statutory_vaph_bruto_41_72m_7_80x"
ENTITY = "vzw_het_gielsbos_lille"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


path_rq = ROOT / "research_queue.csv"
with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
rq = next((row for row in rq_rows if row["task_id"] == "rq_2332"), None)
if not rq or rq.get("status") not in ("open", "in_progress"):
    raise SystemExit("rq_2332 not claimable: " + repr(rq and rq.get("status")))
if has_id(ROOT / "entities.csv", "entity_id", ENTITY):
    raise SystemExit("Het GielsBos already present")
# claim immediately to reduce race window
for row in rq_rows:
    if row["task_id"] == "rq_2332":
        row["status"] = "in_progress"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)

if not has_id(ROOT / "sources.csv", "source_id", "src_gielsbos_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_gielsbos_jr2025_cw_nl",
            "Companyweb NL Het GielsBos YE2025 statutory",
            "https://www.companyweb.be/nl/0408318233/het-giels-bos",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2332; YE2025 omzet 5351872 bruto 41720205 ~7.80x pnl JUMP 1613061 equity 38121725 FTE 509.3",
        ),
        (
            "src_gielsbos_jr2025_cw_en",
            "Companyweb EN Het GielsBos YE2025 statutory",
            "https://www.companyweb.be/en/0408318233/het-giels-bos",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2332; EN Medium; filed 13-06-2026; Turnover 5351872 Gross 41720205 P/L 1613061 Equity 38121725 FTE 509.3",
        ),
        (
            "src_gielsbos_kbo_2332",
            "KBO Het GielsBos 0408.318.233",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408318233",
            "KBO FOD Economie",
            "official_register",
            "tick2332; Actief VZW 7 VE Lille Aanbestedende; RSZ 87.202; BTW 87.201+87.202",
        ),
        (
            "src_gielsbos_site_contact_2332",
            "Het GielsBos FOI info@hetgielsbos.be",
            "https://www.hetgielsbos.be/",
            "Het GielsBos VZW",
            "foi_contact",
            "tick2332; info@hetgielsbos.be; Vosselaarseweg 1, 2275 Lille; T +32 14 60 12 11",
        ),
    ]:
        append_csv(
            ROOT / "sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-28",
                source_class=klass,
                notes=notes,
            ),
        )

append_csv(
    ROOT / "entities.csv",
    dict(
        entity_id=ENTITY,
        name_nl="Het GielsBos VZW (Lille / VAPH woonondersteuning)",
        name_fr="Het GielsBos ASBL (Lille / hébergement VAPH)",
        name_en="Het GielsBos VZW (Lille / VAPH residential care)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://www.hetgielsbos.be/",
        foi_email="info@hetgielsbos.be",
        foi_postal="Vosselaarseweg 1, 2275 Lille",
        notes="tick2332 YE2025 Medium CW NL+EN + Strong KBO 0408.318.233 Actief VZW 7 VE Aanbestedende RSZ 87.202; omzet JUMP 5351872 (+3.71%); bruto JUMP 41720205 (~7.80x / +2.13%); pnl JUMP 1613061 (+14.35%); equity JUMP 38121725 (+4.04%); FTE 509.3; neerlegging 13.06.2026; assets/debt Unknown; FOI gap_gielsbos_*; after Den Brand EVERY-10@2330; AGB Bornem JR2024; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter YE2024; not TE-additive of 348bn",
    ),
)

for bid, amt, basis, notes in [
    ("bud_gielsbos_omzet_jr2025_statutory", 5351872, "CW statutory omzet YE2025 JUMP", "tick2332; Medium CW; omzet +3.71% vs 5160465"),
    ("bud_gielsbos_bruto_jr2025_statutory", 41720205, "CW statutory bruto_marge YE2025 ~7.80x omzet", "tick2332; Medium CW; bruto +2.13% vs 40850817"),
    ("bud_gielsbos_pnl_jr2025_statutory", 1613061, "CW statutory winst/verlies YE2025 JUMP", "tick2332; Medium CW; pnl +14.35% vs 1410671"),
    ("bud_gielsbos_equity_jr2025_statutory", 38121725, "CW statutory eigen_vermogen YE2025 JUMP", "tick2332; Medium CW; equity +4.04% vs 36640735"),
    ("bud_gielsbos_fte_jr2025_statutory", 509.3, "CW social-balance FTE 509.3", "tick2332; Medium CW; FTE 509.3 vs 510.7"),
]:
    append_csv(
        ROOT / "budgets.csv",
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year="2025",
            amount_eur=str(amt),
            amount_min_eur=str(amt),
            amount_max_eur=str(amt),
            basis=basis,
            source_id="src_gielsbos_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    ROOT / "commitments.csv",
    dict(
        commitment_id=COMM,
        title="Het GielsBos YE2025 leftover dual (omzet 5.35m / bruto 41.72m ~7.80x / pnl JUMP / FTE 509.3 / Medium)",
        entity_id=ENTITY,
        beneficiary="kinderen/volwassenen met mentale handicap Kempen Lille-Beerse-Gierle / VAPH",
        legal_basis="VZW Het GielsBos (KBO 0408.318.233; Actief; 7 VE; Aanbestedende; RSZ NACE 87.202)",
        decision_date="2026-06-13",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="41720205",
        cash_by_year='{"2025_omzet":5351872,"2025_bruto":41720205,"2025_pnl":1613061,"2025_equity":38121725,"2025_fte":509.3,"2024_omzet":5160465,"2024_bruto":40850817,"2024_pnl":1410671,"2024_equity":36640735,"2024_fte":510.7}',
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0408318233/het-giels-bos",
        stated_goal="VAPH woonondersteuning Het GielsBos Lille",
        cut_option="Publish NBB PDF assets/debt FOI; explain bruto~7.80x omzet",
        source_id="src_gielsbos_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>Antwerpen>Lille>HetGielsBos_VAPH>JR2025_statutory_L5",
        notes="tick2332; Medium CW; after Den Brand EVERY-10@2330; not TE-additive",
    ),
)

append_csv(
    ROOT / "leaderboard.csv",
    dict(
        item_id=LB,
        name="Het GielsBos bruto 41.72m / ~7.80x omzet 5.35m / pnl JUMP / FTE 509.3 (YE2025 VAPH Lille)",
        level="L5",
        type="vaph_vzw_statutory",
        hierarchy_path="Vlaanderen>Antwerpen>Lille>HetGielsBos_VAPH>JR2025",
        annual_cost_eur="41720205",
        total_cost_eur="41720205",
        tco_notes="CW omzet 5351872 / bruto 41720205 ~7.80x / pnl JUMP 1613061 / equity JUMP 38121725 / FTE 509.3",
        confidence="medium",
        source_id="src_gielsbos_jr2025_cw_en",
        beneficiaries="personen met handicap Kempen",
        stated_goal="VAPH woonondersteuning",
        measured_outcome="bruto~7.80x omzet; pnl JUMP +14.35%; FTE 509.3; filed 13.06.2026",
        absurdity_score="6.5",
        cost_score="5.5",
        difficulty="3.0",
        priority_index="6.00",
        cut_proposal="Publish NBB PDF assets/debt FOI; VAPH subsidy matrix",
        status="open",
        struck_reason="",
        notes="tick2332; Medium CW; FOI gap_gielsbos_*; after Den Brand EVERY-10@2330",
    ),
)

append_csv(
    ROOT / "foi_queue.csv",
    dict(
        gap_id=GAP,
        hierarchy_path="Vlaanderen>Antwerpen>Lille>HetGielsBos_VAPH>NBB_PDF",
        entity_id=ENTITY,
        what_is_missing="NBB PDF YE2025 assets/debt; bruto 41720205 ~7.80x omzet 5351872; pnl JUMP 1613061; VAPH subsidy matrix; FTE 509.3",
        why_it_matters="Medium CW VAPH Lille bruto~7.80x omzet; large public-care shell; assets/debt unknown",
        priority="8",
        recipient_body="Het GielsBos VZW",
        recipient_email="info@hetgielsbos.be",
        recipient_postal="Vosselaarseweg 1, 2275 Lille",
        draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
        status="ready",
        date_ready="2026-08-28",
        date_sent="",
        date_due="",
        date_answered="",
        response_summary="",
        linked_commitment_id=COMM,
        linked_leaderboard_id=LB,
        created_utc=UTC,
        updated_utc=UTC,
        notes="tick2332; ready NOT sent; Medium CW + Strong KBO; after Den Brand EVERY-10@2330",
    ),
)

foi_path = Path(f"docs/doge/foi/drafts/{GAP}.md")
foi_path.write_text(
    f"""# FOI draft — Het GielsBos Lille (NBB PDF / bruto≫omzet ~7.80x)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Het GielsBos VZW — KBO **0408.318.233** (Actief; Vosselaarseweg 1, 2275 Lille; FTE 509.3; 7 VE; Aanbestedende; RSZ **87.202**; VAPH woon)  
**recipient:** info@hetgielsbos.be · Vosselaarseweg 1, 2275 Lille (T +32 14 60 12 11)  
**sources:** [CW EN](https://www.companyweb.be/en/0408318233/het-giels-bos) · [CW NL](https://www.companyweb.be/nl/0408318233/het-giels-bos) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408318233) · [site](https://www.hetgielsbos.be/)  
**tick:** 2332  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR5,351,872** JUMP +3.71%; bruto **EUR41,720,205** JUMP +2.13% (~**7.80x**); pnl **EUR1,613,061** JUMP +14.35%; equity **EUR38,121,725** JUMP +4.04%; FTE **509.3**; filed **13.06.2026**.
- After Den Brand EVERY-10@2330. Stalls: AGB Bornem JR2024; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Het GielsBos VZW
via info@hetgielsbos.be
Vosselaarseweg 1, 2275 Lille
Betreft: Openbaarmaking jaarrekening 2025 Het GielsBos (KBO 0408.318.233)

Geachte,
Op grond van openbaarheid van bestuur / Bestuursdecreet vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR41720205 ≫ omzet EUR5351872 (~7.80x) — VAPH/PVF-matrix.
3. Toelichting pnl JUMP EUR1613061 (+14.35% vs YE2024) bij equity JUMP.
4. Overzicht publieke toelagen YE2025 (+ YE2024).
5. Schulden LT/KT en liquide middelen YE2025.
Ref: {GAP}
Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == "rq_2332":
        row["status"] = "done"
        row["title"] = "leftover dual — Het GielsBos YE2025 Medium (bruto JUMP 41.72m / ~7.80x omzet / pnl JUMP / FTE 509.3)"
        row["entity_id"] = ENTITY
        row["hierarchy_target"] = "L5"
        row["priority"] = "8"
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick2332 Het GielsBos 0408.318.233 YE2025 Medium; omzet 5351872; bruto 41720205 ~7.80x; "
            "pnl JUMP 1613061; equity 38121725; FTE 509.3; FOI ready NOT sent; after Den Brand EVERY-10@2330; next EVERY-10 2340"
        )
        row["instructions"] = (
            "After Den Brand EVERY-10@2330. Prefer AGB/FARO YE2025 else unused. Do NOT redo Het GielsBos/Mivalti/Den Brand/Tandem stack."
        )

if not any(row["task_id"] == "rq_2333" for row in rows):
    rows.append(
        {
            "task_id": "rq_2333",
            "title": "leftover dual after Het GielsBos — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "After Het GielsBos YE2025 Medium@2332. Prefer AGB/FARO YE2025 else FREE "
                "(Gandae/Aralea/Manupal/Vlotter if YE2025 / unused ETA-VAPH-WZC). "
                "Do NOT redo Het GielsBos/Mivalti/Den Brand/Tandem/Pleegzorg/Het Eepos/Zonnebeke stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2332 Het GielsBos; next EVERY-10 2340",
        }
    )

with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(ROOT / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        dict(
            state_id="main",
            mode="continuous",
            current_sprint="hole_fill",
            last_tick_utc=UTC,
            last_unit_id="rq_2332",
            ticks_completed="2332",
            paused="no",
            notes=(
                "tick2332 leftover dual Het GielsBos 0408.318.233 Medium "
                "(omzet JUMP 5351872; bruto JUMP 41720205 ~7.80x; pnl JUMP 1613061; equity JUMP 38121725; FTE 509.3; "
                "7 VE Lille VAPH Aanbestedende); after Den Brand EVERY-10@2330; AGB/FARO YE2024; next rq_2333; next EVERY-10 2340"
            ),
        )
    )

with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick 2332 - rq_2332 Het GielsBos Lille (bruto JUMP 41.72m / ~7.80x omzet / pnl JUMP / FTE 509.3 / Medium)

- Unit: **rq_2332** leftover dual after Den Brand EVERY-10@2330. Stalls AGB Bornem / FARO / AIESH / Gandae / Aralea / Manupal / Vlotter still **YE2024**. Took FREE Flemish VAPH **Het GielsBos VZW** YE2025 (KBO **0408.318.233**; Vosselaarseweg 1, 2275 Lille; **Actief** **7 VE**; Aanbestedende; RSZ **87.202**; info@hetgielsbos.be).
- Found (CW NL+EN YE2025): omzet **EUR5351872** JUMP +3.71%; bruto **EUR41720205** JUMP +2.13% (~**7.80x**); pnl **EUR1613061** JUMP +14.35%; equity **EUR38121725** JUMP +4.04%; FTE **509.3**; neerlegging **13.06.2026**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1 pi 6.00); entities (+1 {ENTITY}); foi + draft `{GAP}`; rq_2332=done + rq_2333 open; loop_state ticks=2332.
- FOI: **ready not sent**. NOT every-10 (next **2340**). Next: rq_2333.
"""
    )

print("OK tick2332 Het GielsBos")
print("ratio", round(41720205 / 5351872, 2), "pi 6.00")

import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-28T02:20:00Z"
ROOT = Path("docs/doge/data")
Path("docs/doge/data/raw/tick2341").mkdir(parents=True, exist_ok=True)
Path("docs/doge/foi/drafts").mkdir(parents=True, exist_ok=True)

GAP = "gap_eyckerheyde_nbb_pdf_assets_debt_bruto_gt_omzet_7_89x_pnl_jump_vaph_matrix_l5"
LB = "lb_eyckerheyde_bruto_9_74m_gt_omzet_7_89x_pnl_jump_fte_jump_jr2025"
COMM = "comm_eyckerheyde_jr2025_statutory_vaph_bruto_9_74m_7_89x"
ENTITY = "vzw_huize_eyckerheyde_bornem"
RQ, RQ_NEXT, TICK = "rq_2341", "rq_2342", "2341"


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
rq = next((row for row in rq_rows if row["task_id"] == RQ), None)
if not rq or rq.get("status") not in ("open", "in_progress"):
    raise SystemExit(f"{RQ} not claimable: " + repr(rq and (rq.get("status"), (rq.get("title") or "")[:80])))
if has_id(ROOT / "entities.csv", "entity_id", ENTITY):
    raise SystemExit("Eyckerheyde already present")
for row in rq_rows:
    if row["task_id"] == RQ:
        row["status"] = "in_progress"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)

if not has_id(ROOT / "sources.csv", "source_id", "src_eyckerheyde_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_eyckerheyde_jr2025_cw_nl",
            "Companyweb NL Huize Eyckerheyde YE2025 statutory",
            "https://www.companyweb.be/nl/0424829019/huize-eyckerheyde",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2341; YE2025 omzet 1234247 bruto 9742289 ~7.89x pnl JUMP 408164 equity 6020250 FTE 121.9",
        ),
        (
            "src_eyckerheyde_jr2025_cw_en",
            "Companyweb EN Huize Eyckerheyde YE2025 statutory",
            "https://www.companyweb.be/en/0424829019/huize-eyckerheyde",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2341; EN Medium; filed 22-06-2026; Turnover 1234247 Gross 9742289 P/L 408164 Equity 6020250 FTE 121.9",
        ),
        (
            "src_eyckerheyde_kbo_2341",
            "KBO Huize Eyckerheyde 0424.829.019",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424829019",
            "KBO FOD Economie",
            "official_register",
            "tick2341; Actief VZW Bornem RSZ 87.202; secretariaat@eyckerheyde.be",
        ),
        (
            "src_eyckerheyde_site_contact_2341",
            "Huize Eyckerheyde FOI secretariaat@eyckerheyde.be",
            "https://www.eyckerheyde.be/",
            "Huize Eyckerheyde VZW",
            "foi_contact",
            "tick2341; secretariaat@eyckerheyde.be; Koningin Astridlaan 3, 2880 Bornem; T +32 3 889 20 00",
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
        name_nl="Huize Eyckerheyde VZW (Bornem / VAPH woonondersteuning)",
        name_fr="Huize Eyckerheyde ASBL (Bornem / hébergement VAPH)",
        name_en="Huize Eyckerheyde VZW (Bornem / VAPH residential care)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://www.eyckerheyde.be/",
        foi_email="secretariaat@eyckerheyde.be",
        foi_postal="Koningin Astridlaan 3, 2880 Bornem",
        notes="tick2341 YE2025 Medium CW NL+EN + Strong KBO 0424.829.019 Actief VZW RSZ 87.202; omzet DROP 1234247 (-3.08%); bruto JUMP 9742289 (~7.89x / +7.02%); pnl JUMP 408164 (+9.48%); equity JUMP 6020250 (+4.45%); FTE JUMP 121.9; neerlegging 22.06.2026; assets/debt Unknown; FOI gap_eyckerheyde_*; after Konekt EVERY-10@2340; AGB Bornem JR2024; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter YE2024; not TE-additive of 348bn",
    ),
)

for bid, amt, basis, notes in [
    ("bud_eyckerheyde_omzet_jr2025_statutory", 1234247, "CW statutory omzet YE2025 DROP", "tick2341; Medium CW; omzet -3.08% vs 1273435"),
    ("bud_eyckerheyde_bruto_jr2025_statutory", 9742289, "CW statutory bruto_marge YE2025 ~7.89x omzet", "tick2341; Medium CW; bruto +7.02% vs 9103102"),
    ("bud_eyckerheyde_pnl_jr2025_statutory", 408164, "CW statutory winst/verlies YE2025 JUMP", "tick2341; Medium CW; pnl +9.48% vs 372826"),
    ("bud_eyckerheyde_equity_jr2025_statutory", 6020250, "CW statutory eigen_vermogen YE2025 JUMP", "tick2341; Medium CW; equity +4.45% vs 5763939"),
    ("bud_eyckerheyde_fte_jr2025_statutory", 121.9, "CW social-balance FTE 121.9", "tick2341; Medium CW; FTE 121.9 vs 115.9"),
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
            source_id="src_eyckerheyde_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        ),
    )

append_csv(
    ROOT / "commitments.csv",
    dict(
        commitment_id=COMM,
        title="Huize Eyckerheyde YE2025 leftover dual (omzet 1.23m / bruto 9.74m ~7.89x / pnl JUMP / FTE 121.9 / Medium)",
        entity_id=ENTITY,
        beneficiary="volwassenen/jongeren met ernstige mentale handicap Bornem / VAPH",
        legal_basis="VZW Huize Eyckerheyde (KBO 0424.829.019; Actief; RSZ NACE 87.202)",
        decision_date="2026-06-22",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="9742289",
        cash_by_year='{"2025_omzet":1234247,"2025_bruto":9742289,"2025_pnl":408164,"2025_equity":6020250,"2025_fte":121.9,"2024_omzet":1273435,"2024_bruto":9103102,"2024_pnl":372826,"2024_equity":5763939,"2024_fte":115.9}',
        remaining_eur="0",
        status="active",
        evaluation_url="https://www.companyweb.be/en/0424829019/huize-eyckerheyde",
        stated_goal="VAPH woonondersteuning Huize Eyckerheyde Bornem",
        cut_option="Publish NBB PDF assets/debt FOI; explain bruto~7.89x omzet",
        source_id="src_eyckerheyde_jr2025_cw_en",
        confidence="medium",
        hierarchy_path="Vlaanderen>Antwerpen>Bornem>HuizeEyckerheyde_VAPH>JR2025_statutory_L5",
        notes="tick2341; Medium CW; after Konekt EVERY-10@2340; not TE-additive",
    ),
)

append_csv(
    ROOT / "leaderboard.csv",
    dict(
        item_id=LB,
        name="Huize Eyckerheyde bruto 9.74m / ~7.89x omzet 1.23m / pnl JUMP / FTE JUMP (YE2025 VAPH Bornem)",
        level="L5",
        type="vaph_vzw_statutory",
        hierarchy_path="Vlaanderen>Antwerpen>Bornem>HuizeEyckerheyde_VAPH>JR2025",
        annual_cost_eur="9742289",
        total_cost_eur="9742289",
        tco_notes="CW omzet 1234247 / bruto 9742289 ~7.89x / pnl JUMP 408164 / equity JUMP 6020250 / FTE JUMP 121.9",
        confidence="medium",
        source_id="src_eyckerheyde_jr2025_cw_en",
        beneficiaries="personen met ernstige mentale handicap Bornem",
        stated_goal="VAPH woonondersteuning",
        measured_outcome="bruto~7.89x omzet; pnl JUMP +9.48%; FTE JUMP 121.9; filed 22.06.2026",
        absurdity_score="6.6",
        cost_score="3.5",
        difficulty="3.0",
        priority_index="4.94",
        cut_proposal="Publish NBB PDF assets/debt FOI; VAPH subsidy matrix",
        status="open",
        struck_reason="",
        notes="tick2341; Medium CW; FOI gap_eyckerheyde_*; after Konekt EVERY-10@2340",
    ),
)

append_csv(
    ROOT / "foi_queue.csv",
    dict(
        gap_id=GAP,
        hierarchy_path="Vlaanderen>Antwerpen>Bornem>HuizeEyckerheyde_VAPH>NBB_PDF",
        entity_id=ENTITY,
        what_is_missing="NBB PDF YE2025 assets/debt; bruto 9742289 ~7.89x omzet 1234247; pnl JUMP 408164; VAPH subsidy matrix; FTE JUMP 121.9",
        why_it_matters="Medium CW VAPH Bornem bruto~7.89x omzet; assets/debt unknown",
        priority="8",
        recipient_body="Huize Eyckerheyde VZW",
        recipient_email="secretariaat@eyckerheyde.be",
        recipient_postal="Koningin Astridlaan 3, 2880 Bornem",
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
        notes="tick2341; ready NOT sent; Medium CW + Strong KBO; after Konekt EVERY-10@2340",
    ),
)

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Huize Eyckerheyde Bornem (NBB PDF / bruto≫omzet ~7.89x)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Huize Eyckerheyde VZW — KBO **0424.829.019** (Actief; Koningin Astridlaan 3, 2880 Bornem; FTE 121.9; RSZ **87.202**; VAPH woon)  
**recipient:** secretariaat@eyckerheyde.be · Koningin Astridlaan 3, 2880 Bornem (T +32 3 889 20 00)  
**sources:** [CW EN](https://www.companyweb.be/en/0424829019/huize-eyckerheyde) · [CW NL](https://www.companyweb.be/nl/0424829019/huize-eyckerheyde) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424829019) · [site](https://www.eyckerheyde.be/)  
**tick:** 2341  
**confidence:** Medium

## Context
- CW YE2025: omzet **EUR1,234,247** DROP −3.08%; bruto **EUR9,742,289** JUMP +7.02% (~**7.89x**); pnl **EUR408,164** JUMP +9.48%; equity **EUR6,020,250** JUMP +4.45%; FTE **121.9** JUMP; filed **22.06.2026**.
- After Konekt EVERY-10@2340. Stalls: AGB Bornem JR2024; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Huize Eyckerheyde VZW
via secretariaat@eyckerheyde.be
Koningin Astridlaan 3, 2880 Bornem
Betreft: Openbaarmaking jaarrekening 2025 Huize Eyckerheyde (KBO 0424.829.019)

Geachte,
Op grond van openbaarheid van bestuur / Bestuursdecreet vraag ik:
1. NBB/CBSO PDF YE2025 (activa/schulden/cash).
2. Toelichting bruto EUR9742289 ≫ omzet EUR1234247 (~7.89x) — VAPH/PVF-matrix.
3. Toelichting pnl JUMP EUR408164 (+9.48%) bij omzet DROP.
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
    if row["task_id"] == RQ:
        row["status"] = "done"
        row["title"] = "leftover dual — Huize Eyckerheyde YE2025 Medium (bruto JUMP 9.74m / ~7.89x omzet / pnl JUMP / FTE JUMP 121.9)"
        row["entity_id"] = ENTITY
        row["hierarchy_target"] = "L5"
        row["priority"] = "8"
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick2341 Huize Eyckerheyde 0424.829.019 YE2025 Medium; omzet 1234247; bruto 9742289 ~7.89x; "
            "pnl JUMP 408164; equity 6020250; FTE 121.9; FOI ready NOT sent; after Konekt EVERY-10@2340; next EVERY-10 2350"
        )
        row["instructions"] = (
            "After Konekt EVERY-10@2340. Prefer AGB/FARO YE2025 else unused. Do NOT redo Eyckerheyde/Konekt/OZC/De Cirkel stack."
        )

if not any(row["task_id"] == RQ_NEXT for row in rows):
    rows.append(
        {
            "task_id": RQ_NEXT,
            "title": "leftover dual after Huize Eyckerheyde — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "After Huize Eyckerheyde YE2025 Medium@2341. Prefer AGB/FARO YE2025 else FREE unused ETA-VAPH-WZC-maatwerk. "
                "Do NOT redo Eyckerheyde/Konekt/OZC SV/De Cirkel/Wieltjesgracht/Apojo/GielsBos stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2341 Huize Eyckerheyde; next EVERY-10 2350",
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
            last_unit_id=RQ,
            ticks_completed=TICK,
            paused="no",
            notes=(
                "tick2341 leftover dual Huize Eyckerheyde 0424.829.019 Medium "
                "(omzet DROP 1234247; bruto JUMP 9742289 ~7.89x; pnl JUMP 408164; equity JUMP 6020250; FTE JUMP 121.9; "
                "Bornem VAPH); after Konekt EVERY-10@2340; AGB/FARO YE2024; next rq_2342; next EVERY-10 2350"
            ),
        )
    )

with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} - tick 2341 - rq_2341 Huize Eyckerheyde Bornem (bruto JUMP 9.74m / ~7.89x omzet / pnl JUMP / FTE JUMP 121.9 / Medium)

- Unit: **rq_2341** leftover dual after Konekt EVERY-10@2340. Stalls AGB Bornem / FARO / AIESH / Gandae / Aralea / Manupal / Vlotter still **YE2024**. Took FREE Flemish VAPH **Huize Eyckerheyde VZW** YE2025 (KBO **0424.829.019**; Koningin Astridlaan 3, 2880 Bornem; RSZ **87.202**; secretariaat@eyckerheyde.be).
- Found (CW NL+EN YE2025): omzet **EUR1234247** DROP -3.08%; bruto **EUR9742289** JUMP +7.02% (~**7.89x**); pnl **EUR408164** JUMP +9.48%; equity **EUR6020250** JUMP +4.45%; FTE **121.9** JUMP; neerlegging **22.06.2026**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1 pi 4.94); entities (+1 {ENTITY}); foi + draft `{GAP}`; rq_2341=done + rq_2342 open; loop_state ticks=2341.
- FOI: **ready not sent**. NOT every-10 (next **2350**). Next: rq_2342.
"""
    )

print("OK tick2341 Huize Eyckerheyde")
print("ratio", round(9742289 / 1234247, 2), "pi 4.94")

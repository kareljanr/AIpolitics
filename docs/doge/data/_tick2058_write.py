# ephemeral tick2058 — 't Pandje Izegem YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T19:35:00Z"
ENTITY = "vzw_tpandje_izegem"
GAP = "gap_tpandje_nbb_pdf_assets_debt_pnl_flip_matrix_l5"
SRC = "src_tpandje_jr2025_cw"
SRC_EN = "src_tpandje_jr2025_cw_en"
SRC_FR = "src_tpandje_jr2025_cw_fr"
SRC_KBO = "src_tpandje_kbo_2058"
SRC_SITE = "src_tpandje_site_2058"

OMZET = "7362472"
PNL = "54453"
EQUITY = "5679276"
BRUTO = "6967215"
FTE = "89.6"
OMZET24 = "6985680"
PNL24 = "-54704"
EQUITY24 = "5642052"
BRUTO24 = "6678824"
# pi = 0.55*4.7 + 0.35*5.2 + 0.10*(10-4) = 2.585 + 1.82 + 0.6 = 5.005 → 5.0
PI = "5.0"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
        fields = [f.lstrip("\ufeff") for f in fields]
        for row in rows:
            if any(k.startswith("\ufeff") for k in row):
                for k in list(row):
                    if k.startswith("\ufeff"):
                        row[k.lstrip("\ufeff")] = row.pop(k)
        return rows, fields


def save(path, rows, fields):
    fields = [f.lstrip("\ufeff") for f in fields]
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2058")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL 't Pandje Izegem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0424249987/-t-pandje",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2058; YE2025 omzet JUMP {OMZET} pnl FLIP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 24.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2058/tpandje_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN 't Pandje Izegem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0424249987/-t-pandje",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2058; EN mirror YE2025 Medium; filed 24-06-2026; Last balance sheet year 2025; FTE 89.6; raw docs/doge/data/raw/tick2058/tpandje_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR 't Pandje Izegem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0424249987/-t-pandje",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2058; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2058/tpandje_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO 't Pandje 0424.249.987 Actief VZW Izegem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424249987",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2058; Actief VZW; Mentenhoekstraat 4 8870 Izegem; 1 VE; NACE 87.101; KBO email empty; aanbestedende overheid flag not present in KBO extract",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "'t Pandje site info@tpandje.be",
        "url": "https://www.tpandje.be/",
        "publisher": "'t Pandje vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2058; site+contact list info@tpandje.be; raw docs/doge/data/raw/tick2058/tpandje_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_tpandje_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2058; omzet JUMP {OMZET} +5.39pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_tpandje_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2058; pnl FLIP {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_tpandje_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2058; equity JUMP {EQUITY} +0.66pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_tpandje_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2058; bruto JUMP {BRUTO} +4.32pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_tpandje_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2058; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_tpandje_jr2025_statutory_wzc",
    "title": "'t Pandje Izegem YE2025 leftover dual (omzet JUMP 7.36m / pnl FLIP 54k)",
    "entity_id": ENTITY,
    "beneficiary": "West-Vlaanderen elderly-care residents (WZC 't Pandje Izegem)",
    "legal_basis": "VZW WZC operator (KBO 0424.249.987)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0424249987/-t-pandje",
    "stated_goal": "WZC 't Pandje Izegem",
    "cut_option": "Publish NBB PDF assets/debt + explain FLIP to profit FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Izegem>TPandje>JR2025_statutory_L5",
    "notes": "tick2058; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_tpandje_omzet_jump_7_36m_pnl_flip_jr2025",
    "name": "'t Pandje Izegem omzet JUMP 7.36m / pnl FLIP 54k (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Izegem>TPandje>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl FLIP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; VZW WZC dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "West-Vlaanderen elderly-care residents via 't Pandje Izegem",
    "stated_goal": "WZC 't Pandje",
    "measured_outcome": "Medium CW YE2025; 7.36m omzet JUMP +5.39pct with pnl FLIP to profit EUR54k (was LOSS EUR-55k); NBB PDF residual",
    "absurdity_score": "5.2",
    "cost_score": "4.7",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map subsidy vs dagprijs stack",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2058 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "'t Pandje (VZW WZC Izegem)",
    "name_fr": "'t Pandje (ASBL MRS Izegem)",
    "name_en": "'t Pandje (VZW nursing home Izegem)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.tpandje.be/",
    "foi_email": "info@tpandje.be",
    "foi_postal": "Mentenhoekstraat 4, 8870 Izegem",
    "notes": (
        "tick2058 YE2025 Medium CW NL+EN+FR + Strong KBO 0424.249.987 Actief VZW 1 VE; omzet JUMP 7.36m pnl FLIP 54k equity JUMP 5.68m bruto JUMP 6.97m FTE 89.6; "
        "assets/debt Unknown; neerlegging 24.06.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have"
    ),
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Izegem>TPandje>NBB_PDF_assets_debt_pnl_flip",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of FLIP to profit (EUR54k vs YE2024 LOSS EUR-55k)",
    "why_it_matters": "Medium CW shows 7.36m omzet VL WZC VZW with pnl FLIP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "'t Pandje vzw",
    "recipient_email": "info@tpandje.be",
    "recipient_postal": "Mentenhoekstraat 4, 8870 Izegem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_tpandje_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_tpandje_omzet_jump_7_36m_pnl_flip_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2058; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — 't Pandje Izegem (NBB PDF / assets-debt / pnl-flip)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** 't Pandje VZW — KBO **0424.249.987**  
**recipient:** info@tpandje.be · Mentenhoekstraat 4, 8870 Izegem  
**sources:** [CW NL](https://www.companyweb.be/nl/0424249987/-t-pandje) · [CW EN](https://www.companyweb.be/en/0424249987/-t-pandje) · [CW FR](https://www.companyweb.be/fr/0424249987/-t-pandje) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424249987) · [site](https://www.tpandje.be/)  
**tick:** 2058  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **24.06.2026**): omzet **EUR7,362,472** JUMP +5.39%; pnl **EUR54,453** FLIP vs YE2024 LOSS EUR-54,704; equity **EUR5,679,276** JUMP +0.66%; bruto **EUR6,967,215** JUMP +4.32%; FTE **89.6**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Mentenhoekstraat 4 Izegem; NACE 87.101.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: 't Pandje vzw — Mentenhoekstraat 4, 8870 Izegem
info@tpandje.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 't Pandje + subsidiematrix (KBO 0424.249.987)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 24.06.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting omslag van verlies (EUR-54.704 YE2024) naar winst (EUR54.453 YE2025).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, "
    "AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2058":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Groep Zorg H. Familie — 't Pandje Izegem YE2025 Medium"
        x["notes"] = (
            "tick2058 't Pandje Medium omzet JUMP 7.36m pnl FLIP 54k equity JUMP 5.68m bruto JUMP 6.97m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2059; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover 't Pandje Izegem YE2025 Medium CW; KBO 0424.249.987; "
            f"omzet JUMP {OMZET} pnl FLIP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2059" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2059",
            "title": "leftover dual hole-fill after 't Pandje Izegem",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2058 after 't Pandje Izegem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2058 't Pandje; next every-10 2060",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2058",
        "ticks_completed": "2058",
        "paused": "no",
        "notes": (
            "tick2058 leftover 't Pandje Izegem 0424.249.987 Medium CW (omzet JUMP 7.36m pnl FLIP 54k equity JUMP 5.68m bruto JUMP 6.97m FTE 89.6; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2059; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2058 - {UTC} - rq_2058 't Pandje Izegem (omzet JUMP 7.36m / pnl FLIP 54k / Medium)

- Unit: **rq_2058** leftover dual after **rq_2057 Groep Zorg H. Familie**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **'t Pandje** YE2025 (KBO **0424.249.987**; Mentenhoekstraat 4 Izegem; West-Vlaanderen **VZW** WZC / **1 VE**). Do not redo H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR7,362,472** JUMP +5.39%; pnl **EUR54,453** FLIP vs YE2024 LOSS EUR-54,704; equity **EUR5,679,276** JUMP +0.66%; bruto **EUR6,967,215** JUMP +4.32%; FTE **89.6**; neerlegging **24.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@tpandje.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2058=done + rq_2059 open; loop_state ticks=2058; raw under docs/doge/data/raw/tick2058/.
- FOI: **ready not sent** (human-gated; info@tpandje.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2059 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2058 't Pandje", OMZET, "pi", PI)

# ephemeral tick2052 — Ter Berk / Seniorenzorg Sint-Vincentius Anzegem YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T18:10:00Z"
ENTITY = "vzw_seniorenzorg_sint_vincentius_anzegem"
GAP = "gap_ter_berk_anzegem_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_ter_berk_jr2025_cw"
SRC_EN = "src_ter_berk_jr2025_cw_en"
SRC_FR = "src_ter_berk_jr2025_cw_fr"
SRC_KBO = "src_ter_berk_kbo_2052"
SRC_SITE = "src_ter_berk_site_2052"

OMZET = "12323749"
PNL = "95151"
EQUITY = "14792035"
BRUTO = "12916037"
FTE = "163.4"
OMZET24 = "11339235"
PNL24 = "266596"
EQUITY24 = "14407855"
BRUTO24 = "11921914"
# pi = 0.55*5.0 + 0.35*5.5 + 0.10*(10-4) = 2.75 + 1.925 + 0.6 = 5.275 → 5.3
PI = "5.3"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2052")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Seniorenzorg Sint-Vincentius Anzegem (Ter Berk) YE2025",
        "url": "https://www.companyweb.be/nl/0473267354/seniorenzorg-sint-vincentius-anzegem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2052; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 26.05.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2052/ter_berk_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Seniorenzorg Sint-Vincentius Anzegem YE2025",
        "url": "https://www.companyweb.be/en/0473267354/seniorenzorg-sint-vincentius-anzegem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2052; EN mirror YE2025 Medium; filed 26-05-2026; Last balance sheet year 2025; FTE 163.4; raw docs/doge/data/raw/tick2052/ter_berk_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Seniorenzorg Sint-Vincentius Anzegem YE2025",
        "url": "https://www.companyweb.be/fr/0473267354/seniorenzorg-sint-vincentius-anzegem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2052; FR mirror YE2025 Medium; depose le 26-05-2026; raw docs/doge/data/raw/tick2052/ter_berk_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Seniorenzorg Sint-Vincentius Anzegem 0473.267.354 Actief VZW aanbestedende overheid",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0473267354",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2052; Actief VZW; Berkenlaan 2 8570 Anzegem; 2 VE (Ter Berk + Sint-Vincentiusrustoord Izegem); aanbestedende overheid sinds 05.10.2000; NACE 87.301; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Ter Berk site info@terberk.be",
        "url": "https://terberk.be/",
        "publisher": "Seniorenzorg Sint-Vincentius Anzegem / Ter Berk",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2052; site+contact list info@terberk.be; raw docs/doge/data/raw/tick2052/ter_berk_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_ter_berk_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2052; omzet JUMP {OMZET} +8.68pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_ter_berk_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2052; pnl DROP {PNL} -64.31pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_ter_berk_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2052; equity JUMP {EQUITY} +2.67pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_ter_berk_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2052; bruto JUMP {BRUTO} +8.34pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_ter_berk_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2052; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_ter_berk_jr2025_statutory_wzc",
    "title": "Ter Berk / Seniorenzorg Sint-Vincentius Anzegem YE2025 leftover dual (omzet JUMP 12.32m / pnl DROP 95k)",
    "entity_id": ENTITY,
    "beneficiary": "West-Vlaanderen elderly-care residents (Ter Berk Anzegem + Sint-Vincentiusrustoord Izegem)",
    "legal_basis": "VZW WZC operator / aanbestedende overheid (KBO 0473.267.354)",
    "decision_date": "2026-05-26",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0473267354/seniorenzorg-sint-vincentius-anzegem",
    "stated_goal": "Multi-site WZC Ter Berk Anzegem / Sint-Vincentiusrustoord Izegem",
    "cut_option": "Publish NBB PDF assets/debt + explain pnl DROP -64pct vs omzet JUMP FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Anzegem>TerBerk>JR2025_statutory_L5",
    "notes": "tick2052; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe/Lendelede YE2025 deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_ter_berk_omzet_jump_12_32m_pnl_drop_jr2025",
    "name": "Ter Berk Anzegem omzet JUMP 12.32m / pnl DROP 95k (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Anzegem>TerBerk>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "West-Vlaanderen elderly-care residents via Ter Berk / Sint-Vincentius Anzegem",
    "stated_goal": "Multi-site WZC Ter Berk / Sint-Vincentiusrustoord",
    "measured_outcome": "Medium CW YE2025; 12.32m omzet JUMP +8.68pct with pnl DROP -64.31pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP vs omzet JUMP; map subsidy stack",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2052 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Seniorenzorg Sint-Vincentius Anzegem / Ter Berk (VZW)",
    "name_fr": "Soins aux seniors Sint-Vincentius Anzegem / Ter Berk (ASBL)",
    "name_en": "Seniorenzorg Sint-Vincentius Anzegem / Ter Berk (VZW nursing homes)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://terberk.be/",
    "foi_email": "info@terberk.be",
    "foi_postal": "Berkenlaan 2, 8570 Anzegem",
    "notes": (
        "tick2052 YE2025 Medium CW NL+EN+FR + Strong KBO 0473.267.354 Actief VZW aanbestedende overheid 2 VE; omzet JUMP 12.32m pnl DROP 95k equity JUMP 14.79m bruto JUMP 12.92m FTE 163.4; "
        "assets/debt Unknown; neerlegging 26.05.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe/Lendelede YE2025 deferred; do not redo Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have"
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
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Anzegem>TerBerk>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl DROP -64pct despite omzet JUMP +8.7pct; campus split Ter Berk vs Izegem",
    "why_it_matters": "Medium CW shows 12.32m omzet VL aanbestedende-overheid WZC VZW with sharp pnl DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Seniorenzorg Sint-Vincentius Anzegem vzw (Ter Berk)",
    "recipient_email": "info@terberk.be",
    "recipient_postal": "Berkenlaan 2, 8570 Anzegem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ter_berk_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_ter_berk_omzet_jump_12_32m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2052; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Ter Berk / Seniorenzorg Sint-Vincentius Anzegem (NBB PDF / assets-debt / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Seniorenzorg Sint-Vincentius Anzegem VZW — KBO **0473.267.354**  
**recipient:** info@terberk.be · Berkenlaan 2, 8570 Anzegem  
**sources:** [CW NL](https://www.companyweb.be/nl/0473267354/seniorenzorg-sint-vincentius-anzegem) · [CW EN](https://www.companyweb.be/en/0473267354/seniorenzorg-sint-vincentius-anzegem) · [CW FR](https://www.companyweb.be/fr/0473267354/seniorenzorg-sint-vincentius-anzegem) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0473267354) · [site](https://terberk.be/)  
**tick:** 2052  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **26.05.2026**): omzet **EUR12,323,749** JUMP +8.68%; pnl **EUR95,151** DROP −64.31% vs YE2024 EUR266,596; equity **EUR14,792,035** JUMP +2.67%; bruto **EUR12,916,037** JUMP +8.34%; FTE **163.4**; assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **2 VE** (Ter Berk Anzegem + Sint-Vincentiusrustoord Izegem).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Huize Westerhauwe / Seniorenzorg Lendelede YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Seniorenzorg Sint-Vincentius Anzegem vzw — Berkenlaan 2, 8570 Anzegem
info@terberk.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Ter Berk + subsidiematrix (KBO 0473.267.354)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 26.05.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting pnl DROP (van EUR266.596 YE2024 naar EUR95.151 YE2025) bij omzet JUMP.
5. Niet-confidentieel overzicht omzet/resultaat per campus (Ter Berk Anzegem vs Sint-Vincentiusrustoord Izegem).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, "
    "AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2052":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Van Lierde — Ter Berk Anzegem YE2025 Medium"
        x["notes"] = (
            "tick2052 Ter Berk Medium omzet JUMP 12.32m pnl DROP 95k equity JUMP 14.79m bruto JUMP 12.92m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe/Lendelede deferred; next rq_2053; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover Ter Berk / Seniorenzorg Sint-Vincentius Anzegem YE2025 Medium CW; KBO 0473.267.354; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2053" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2053",
            "title": "leftover dual hole-fill after Ter Berk Anzegem",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2052 after Ter Berk Anzegem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Huize Westerhauwe YE2025 live deferred / Seniorenzorg Lendelede YE2025 / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2052 Ter Berk; next every-10 2060; Westerhauwe/Lendelede YE2025 deferred",
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
        "last_unit_id": "rq_2052",
        "ticks_completed": "2052",
        "paused": "no",
        "notes": (
            "tick2052 leftover Ter Berk Anzegem 0473.267.354 Medium CW (omzet JUMP 12.32m pnl DROP 95k equity JUMP 14.79m bruto JUMP 12.92m FTE 163.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe/Lendelede deferred; next rq_2053; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2052 - {UTC} - rq_2052 Ter Berk Anzegem (omzet JUMP 12.32m / pnl DROP 95k / Medium)

- Unit: **rq_2052** leftover dual after **rq_2051 Van Lierde**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Seniorenzorg Sint-Vincentius Anzegem / Ter Berk** YE2025 (KBO **0473.267.354**; Berkenlaan 2 Anzegem; West-Vlaanderen **aanbestedende-overheid VZW** WZC / **2 VE**). Huize Westerhauwe / Seniorenzorg Lendelede YE2025 also live — deferred. Do not redo Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR12,323,749** JUMP +8.68%; pnl **EUR95,151** DROP −64.31%; equity **EUR14,792,035** JUMP +2.67%; bruto **EUR12,916,037** JUMP +8.34%; FTE **163.4**; neerlegging **26.05.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 2 VE; email info@terberk.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2052=done + rq_2053 open; loop_state ticks=2052; raw under docs/doge/data/raw/tick2052/.
- FOI: **ready not sent** (human-gated; info@terberk.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2053 (AGB/FARO-if-YE2025 / AIESH-REW / Westerhauwe-Lendelede deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2052 Ter Berk", OMZET, "pi", PI)

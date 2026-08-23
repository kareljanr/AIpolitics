# ephemeral tick2055 — Centrum Ganspoel YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T18:50:00Z"
ENTITY = "vzw_centrum_ganspoel"
GAP = "gap_ganspoel_nbb_pdf_assets_debt_pnl_drop_subsidy_matrix_l5"
SRC = "src_ganspoel_jr2025_cw"
SRC_EN = "src_ganspoel_jr2025_cw_en"
SRC_FR = "src_ganspoel_jr2025_cw_fr"
SRC_KBO = "src_ganspoel_kbo_2055"
SRC_SITE = "src_ganspoel_site_2055"

OMZET = "1714365"
PNL = "133240"
EQUITY = "19098814"
BRUTO = "20569172"
FTE = "244.7"
OMZET24 = "1692759"
PNL24 = "667800"
EQUITY24 = "18381270"
BRUTO24 = "20114712"
# cost on bruto ~20.6m; absurdity pnl DROP -80%; pi = 0.55*5.5 + 0.35*5.8 + 0.10*(10-4) = 3.025 + 2.03 + 0.6 = 5.655 → 5.7
PI = "5.7"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2055")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Centrum Ganspoel YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0410917437/centrum-ganspoel",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2055; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 24.06.2026; assets/debt Unknown; code70 omzet understates vs bruto; raw docs/doge/data/raw/tick2055/ganspoel_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Centrum Ganspoel YE2025 statutory",
        "url": "https://www.companyweb.be/en/0410917437/centrum-ganspoel",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2055; EN mirror YE2025 Medium; filed 24-06-2026; Last balance sheet year 2025; FTE 244.7; raw docs/doge/data/raw/tick2055/ganspoel_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Centrum Ganspoel YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0410917437/centrum-ganspoel",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2055; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2055/ganspoel_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Centrum Ganspoel 0410.917.437 Actief VZW aanbestedende overheid Huldenberg",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410917437",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2055; Actief VZW; Ganspoel 2 3040 Huldenberg; 5 VE; aanbestedende overheid sinds 30.03.1961; NACE 87.303; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Centrum Ganspoel site info@ganspoel.be",
        "url": "https://www.ganspoel.be/",
        "publisher": "Centrum Ganspoel vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2055; VAPH disability care (visual/multiple impairment); site+contact list info@ganspoel.be; raw docs/doge/data/raw/tick2055/ganspoel_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_ganspoel_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover (code70; understates vs bruto)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2055; omzet JUMP {OMZET} +1.28pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_ganspoel_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2055; pnl DROP {PNL} -80.05pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_ganspoel_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2055; equity JUMP {EQUITY} +3.90pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_ganspoel_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin (material VZW/VAPH flow)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2055; bruto JUMP {BRUTO} +2.26pct vs YE2024 {BRUTO24}; preferred envelope vs code70 omzet",
    },
    {
        "budget_id": "bud_ganspoel_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2055; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_ganspoel_jr2025_statutory_vaph",
    "title": "Centrum Ganspoel YE2025 leftover dual (bruto JUMP 20.57m / pnl DROP 0.13m)",
    "entity_id": ENTITY,
    "beneficiary": "VL persons with visual/multiple disability (VAPH Ganspoel Huldenberg)",
    "legal_basis": "VZW disability care / aanbestedende overheid (KBO 0410.917.437)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": BRUTO,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0410917437/centrum-ganspoel",
    "stated_goal": "VAPH care/education for visual and multiple disability (Centrum Ganspoel)",
    "cut_option": "Publish NBB PDF assets/debt + VAPH subsidy matrix FOI; explain pnl DROP -80pct",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Huldenberg>CentrumGanspoel>JR2025_statutory_L5",
    "notes": "tick2055; Medium CW; assets/debt Unknown; envelope=bruto (code70 omzet understates); preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe YE2025 deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_ganspoel_bruto_jump_20_57m_pnl_drop_jr2025",
    "name": "Centrum Ganspoel bruto JUMP 20.57m / pnl DROP 0.13m (YE2025)",
    "level": "L5",
    "type": "vzw_vaph_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Huldenberg>CentrumGanspoel>JR2025_statutory_L5",
    "annual_cost_eur": BRUTO,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory bruto JUMP {BRUTO} omzet {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; assets/debt Unknown; code70 omzet understates VZW/VAPH; aanbestedende overheid",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "VL persons with visual/multiple disability via Centrum Ganspoel / VAPH",
    "stated_goal": "VAPH disability care and education campus Huldenberg",
    "measured_outcome": "Medium CW YE2025; bruto 20.57m JUMP +2.26pct with pnl DROP -80.05pct (EUR133k vs EUR668k); NBB PDF residual",
    "absurdity_score": "5.8",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map VAPH subsidy vs other income; explain pnl DROP -80pct",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2055 leftover dual; Medium CW; TE-adjacent VAPH care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Centrum Ganspoel (VZW, VAPH Huldenberg)",
    "name_fr": "Centre Ganspoel (ASBL, handicap visuel/multiple Huldenberg)",
    "name_en": "Centrum Ganspoel (VZW disability care Huldenberg)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.ganspoel.be/",
    "foi_email": "info@ganspoel.be",
    "foi_postal": "Ganspoel 2, 3040 Huldenberg",
    "notes": (
        "tick2055 YE2025 Medium CW NL+EN+FR + Strong KBO 0410.917.437 Actief VZW aanbestedende overheid 5 VE; bruto JUMP 20.57m omzet 1.71m pnl DROP 0.13m equity JUMP 19.10m FTE 244.7; "
        "assets/debt Unknown; neerlegging 24.06.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe YE2025 deferred; do not redo Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have"
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
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Huldenberg>CentrumGanspoel>NBB_PDF_assets_debt_pnl_drop_subsidy",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); VAPH/other public subsidy vs omzet/bruto recon; explanation of pnl DROP -80pct (EUR133k vs EUR668k YE2024)",
    "why_it_matters": "Medium CW shows ~20.6m bruto VL aanbestedende-overheid VAPH VZW with sharp pnl DROP and code70 omzet only 1.7m; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Centrum Ganspoel vzw",
    "recipient_email": "info@ganspoel.be",
    "recipient_postal": "Ganspoel 2, 3040 Huldenberg",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ganspoel_jr2025_statutory_vaph",
    "linked_leaderboard_id": "lb_ganspoel_bruto_jump_20_57m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2055; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Centrum Ganspoel (NBB PDF / assets-debt / pnl-drop / VAPH subsidy)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Centrum Ganspoel VZW — KBO **0410.917.437**  
**recipient:** info@ganspoel.be · Ganspoel 2, 3040 Huldenberg  
**sources:** [CW NL](https://www.companyweb.be/nl/0410917437/centrum-ganspoel) · [CW EN](https://www.companyweb.be/en/0410917437/centrum-ganspoel) · [CW FR](https://www.companyweb.be/fr/0410917437/centrum-ganspoel) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410917437) · [site](https://www.ganspoel.be/)  
**tick:** 2055  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **24.06.2026**): bruto **EUR20,569,172** JUMP +2.26%; omzet code70 **EUR1,714,365** JUMP +1.28%; pnl **EUR133,240** DROP −80.05% vs YE2024 EUR667,800; equity **EUR19,098,814** JUMP +3.90%; FTE **244.7**; assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **5 VE**; zetel Ganspoel 2 Huldenberg; NACE 87.303 (VAPH disability).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Huize Westerhauwe YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Centrum Ganspoel vzw — Ganspoel 2, 3040 Huldenberg
info@ganspoel.be
cc: VAPH / Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Centrum Ganspoel + VAPH-subsidiematrix (KBO 0410.917.437)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 24.06.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split VAPH/andere publieke subsidies vs eigen bijdragen/omzet 2025 (recon code70 omzet EUR1.714.365 vs brutomarge EUR20.569.172).
4. Toelichting pnl DROP (van EUR667.800 YE2024 naar EUR133.240 YE2025).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, "
    "Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "Sint-Jozef Rumst, Veilige Have, Witte Meren, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, "
    "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
    "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2055":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Seniorenzorg Lendelede — Centrum Ganspoel YE2025 Medium"
        x["notes"] = (
            "tick2055 Ganspoel Medium bruto JUMP 20.57m omzet 1.71m pnl DROP 0.13m equity JUMP 19.10m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe deferred; next rq_2056; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover Centrum Ganspoel YE2025 Medium CW; KBO 0410.917.437; "
            f"bruto JUMP {BRUTO} omzet {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2056" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2056",
            "title": "leftover dual hole-fill after Centrum Ganspoel",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2055 after Centrum Ganspoel YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Huize Westerhauwe YE2025 live deferred / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2055 Centrum Ganspoel; next every-10 2060; Westerhauwe YE2025 deferred",
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
        "last_unit_id": "rq_2055",
        "ticks_completed": "2055",
        "paused": "no",
        "notes": (
            "tick2055 leftover Centrum Ganspoel 0410.917.437 Medium CW (bruto JUMP 20.57m omzet 1.71m pnl DROP 0.13m equity JUMP 19.10m FTE 244.7; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Westerhauwe deferred; next rq_2056; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2055 - {UTC} - rq_2055 Centrum Ganspoel (bruto JUMP 20.57m / pnl DROP 0.13m / Medium)

- Unit: **rq_2055** leftover dual after **rq_2054 Seniorenzorg Lendelede**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Centrum Ganspoel** YE2025 (KBO **0410.917.437**; Ganspoel 2 Huldenberg; Vlaams-Brabant **aanbestedende-overheid VZW** VAPH disability / **5 VE**). Huize Westerhauwe YE2025 also live — deferred. Do not redo Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — bruto **EUR20,569,172** JUMP +2.26%; omzet code70 **EUR1,714,365** JUMP +1.28%; pnl **EUR133,240** DROP −80.05%; equity **EUR19,098,814** JUMP +3.90%; FTE **244.7**; neerlegging **24.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 5 VE; email info@ganspoel.be. Envelope uses **bruto** (code70 omzet understates VZW/VAPH flow).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2055=done + rq_2056 open; loop_state ticks=2055; raw under docs/doge/data/raw/tick2055/.
- FOI: **ready not sent** (human-gated; info@ganspoel.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2056 (AGB/FARO-if-YE2025 / AIESH-REW / Westerhauwe deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2055 Centrum Ganspoel", BRUTO, "pi", PI)

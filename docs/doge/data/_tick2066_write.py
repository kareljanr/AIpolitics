# ephemeral tick2066 — Bejaardenzorg Zusters Sint-Vincentius Deinze YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T21:35:00Z"
ENTITY = "vzw_bejaardenzorg_zusters_sv_deinze"
GAP = "gap_deinze_zusters_nbb_pdf_assets_debt_pnl_deeper_loss_matrix_l5"
SRC = "src_deinze_zusters_jr2025_cw"
SRC_EN = "src_deinze_zusters_jr2025_cw_en"
SRC_FR = "src_deinze_zusters_jr2025_cw_fr"
SRC_KBO = "src_deinze_zusters_kbo_2066"
SRC_SITE = "src_deinze_zusters_site_2066"

OMZET = "10951934"
PNL = "-661300"
EQUITY = "4780639"
BRUTO = "11057428"
FTE = "147.8"
OMZET24 = "11117960"
PNL24 = "-541401"
EQUITY24 = "5483612"
BRUTO24 = "11415649"
# pi = 0.55*5.0 + 0.35*5.4 + 0.10*(10-4) = 2.75 + 1.89 + 0.6 = 5.24 → 5.2
PI = "5.2"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2066")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Bejaardenzorg Zusters SV Deinze YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0454090355/bejaardenzorg-zusters-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2066; YE2025 omzet DROP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 06.08.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2066/deinze_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Bejaardenzorg Zusters SV Deinze YE2025 statutory",
        "url": "https://www.companyweb.be/en/0454090355/bejaardenzorg-zusters-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2066; EN mirror YE2025 Medium; filed 06-08-2026; Last balance sheet year 2025; FTE 147.8; raw docs/doge/data/raw/tick2066/deinze_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Bejaardenzorg Zusters SV Deinze YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0454090355/bejaardenzorg-zusters-sint-vincentius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2066; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2066/deinze_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Bejaardenzorg Zusters SV 0454.090.355 Actief VZW Deinze",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0454090355",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2066; Actief VZW; Ten Bosse 150 9800 Deinze; 2 VE; NACE 87.301; aanbestedende overheid sinds 26.11.1988; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "SV Bejaardenzorg site info@svbejaardenzorg.be",
        "url": "https://www.svbejaardenzorg.be/",
        "publisher": "Bejaardenzorg Zusters Sint-Vincentius vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2066; site+contact info@svbejaardenzorg.be; tel 09 381 08 08; raw docs/doge/data/raw/tick2066/deinze_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_deinze_zusters_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2066; omzet DROP {OMZET} -1.49pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_deinze_zusters_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2066; pnl DEEPER LOSS {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_deinze_zusters_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2066; equity DROP {EQUITY} -12.82pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_deinze_zusters_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2066; bruto DROP {BRUTO} -3.14pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_deinze_zusters_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2066; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_deinze_zusters_jr2025_statutory_wzc",
    "title": "Zusters SV Deinze YE2025 leftover dual (omzet DROP 10.95m / pnl DEEPER LOSS 0.66m)",
    "entity_id": ENTITY,
    "beneficiary": "Deinze elderly residents (Bejaardenzorg Zusters Sint-Vincentius)",
    "legal_basis": "VZW WZC / aanbestedende overheid / publiek gesubsidieerde zorg (KBO 0454.090.355)",
    "decision_date": "2026-08-06",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0454090355/bejaardenzorg-zusters-sint-vincentius",
    "stated_goal": "WZC residential elderly care Deinze Ten Bosse",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain DEEPER LOSS + equity DROP -12.82pct",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>ZustersSV>JR2025_statutory_L5",
    "notes": "tick2066; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_deinze_zusters_omzet_drop_10_95m_pnl_deeper_loss_jr2025",
    "name": "Zusters SV Deinze omzet DROP 10.95m / pnl DEEPER LOSS 0.66m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>ZustersSV>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet DROP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual aanbestedende overheid",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Deinze elderly residents via Bejaardenzorg Zusters Sint-Vincentius",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 10.95m omzet DROP -1.49pct with DEEPER LOSS -661k (from -541k) and equity DROP -12.82pct; NBB PDF residual",
    "absurdity_score": "5.4",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain DEEPER LOSS + equity DROP; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2066 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Bejaardenzorg Zusters Sint-Vincentius (VZW, Deinze)",
    "name_fr": "Bejaardenzorg Zusters Sint-Vincentius (ASBL MRS, Deinze)",
    "name_en": "Bejaardenzorg Zusters Sint-Vincentius (VZW nursing home Deinze)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.svbejaardenzorg.be/",
    "foi_email": "info@svbejaardenzorg.be",
    "foi_postal": "Ten Bosse 150, 9800 Deinze",
    "notes": (
        "tick2066 YE2025 Medium CW NL+EN+FR + Strong KBO 0454.090.355 Actief VZW aanbestedende overheid 2 VE; omzet DROP 10.95m pnl DEEPER LOSS 0.66m equity DROP 4.78m bruto DROP 11.06m FTE 147.8; "
        "assets/debt Unknown; neerlegging 06.08.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Leiehome/Compostela/Always Home/Vulpia YE2025 deferred; do not redo Seniorencentrum OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Home Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof"
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
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Deinze>ZustersSV>NBB_PDF_assets_debt_pnl_deeper_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of DEEPER LOSS (-661k vs -541k) and equity DROP -12.82pct",
    "why_it_matters": "Medium CW shows 10.95m omzet WZC VZW aanbestedende overheid with DEEPER LOSS + equity DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Bejaardenzorg Zusters Sint-Vincentius vzw",
    "recipient_email": "info@svbejaardenzorg.be",
    "recipient_postal": "Ten Bosse 150, 9800 Deinze",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_deinze_zusters_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_deinze_zusters_omzet_drop_10_95m_pnl_deeper_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2066; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Bejaardenzorg Zusters SV Deinze (NBB PDF / assets-debt / pnl-deeper-loss)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Bejaardenzorg Zusters Sint-Vincentius VZW — KBO **0454.090.355**  
**recipient:** info@svbejaardenzorg.be · Ten Bosse 150, 9800 Deinze  
**sources:** [CW NL](https://www.companyweb.be/nl/0454090355/bejaardenzorg-zusters-sint-vincentius) · [CW EN](https://www.companyweb.be/en/0454090355/bejaardenzorg-zusters-sint-vincentius) · [CW FR](https://www.companyweb.be/fr/0454090355/bejaardenzorg-zusters-sint-vincentius) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0454090355) · [site](https://www.svbejaardenzorg.be/)  
**tick:** 2066  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **06.08.2026**): omzet **EUR10,951,934** DROP -1.49%; pnl **LOSS EUR-661,300** DEEPER vs YE2024 LOSS EUR-541,401; equity **EUR4,780,639** DROP -12.82%; bruto **EUR11,057,428** DROP -3.14%; FTE **147.8**; assets/debt **Unknown**.
- KBO: Actief VZW; **2 VE**; aanbestedende overheid; zetel Ten Bosse 150 Deinze; NACE 87.301.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live YE2025: Leiehome / Compostela / Always Home / Vulpia.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Bejaardenzorg Zusters Sint-Vincentius vzw — Ten Bosse 150, 9800 Deinze
info@svbejaardenzorg.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Bejaardenzorg Zusters SV Deinze + subsidiematrix (KBO 0454.090.355)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (aanbestedende overheid / publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 06.08.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting verdieping verlies van EUR-541.401 (YE2024) naar EUR-661.300 (YE2025) en equity DROP -12,82%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
    "OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, "
    "Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, "
    "WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2066":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after OLV Bornem — Zusters SV Deinze YE2025 Medium"
        x["notes"] = (
            "tick2066 Zusters SV Deinze Medium omzet DROP 10.95m pnl DEEPER LOSS 0.66m equity DROP 4.78m bruto DROP 11.06m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2067; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover Zusters SV Deinze YE2025 Medium CW; KBO 0454.090.355; "
            f"omzet DROP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2067" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2067",
            "title": "leftover dual hole-fill after Zusters SV Deinze",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2066 after Zusters SV Deinze YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Leiehome / Compostela / Always Home / Vulpia YE2025 deferred if still live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2066 Zusters SV Deinze; next every-10 2070",
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
        "last_unit_id": "rq_2066",
        "ticks_completed": "2066",
        "paused": "no",
        "notes": (
            "tick2066 leftover Zusters SV Deinze 0454.090.355 Medium CW (omzet DROP 10.95m pnl DEEPER LOSS 0.66m equity DROP 4.78m bruto DROP 11.06m FTE 147.8; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2067; next every-10 2070; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2066 - 2026-08-24T21:35:00Z - rq_2066 Zusters SV Deinze (omzet DROP 10.95m / pnl DEEPER LOSS 0.66m / Medium)

- Unit: **rq_2066** leftover dual after **rq_2065 Seniorencentrum OLV Bornem**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred leftover **Bejaardenzorg Zusters Sint-Vincentius Deinze** YE2025 (KBO **0454.090.355**; Ten Bosse 150 Deinze; Oost-Vlaanderen **aanbestedende-overheid VZW** WZC / **2 VE**). Leiehome / Compostela / Always Home / Vulpia YE2025 also live - deferred. Do not redo OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR10,951,934** DROP -1.49%; pnl **LOSS EUR-661,300** DEEPER vs YE2024 LOSS EUR-541,401; equity **EUR4,780,639** DROP -12.82%; bruto **EUR11,057,428** DROP -3.14%; FTE **147.8**; neerlegging **06.08.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 2 VE; email info@svbejaardenzorg.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.2); entities (+1 vzw_bejaardenzorg_zusters_sv_deinze); foi + draft {GAP}; rq_2066=done + rq_2067 open; loop_state ticks=2066; raw under docs/doge/data/raw/tick2066/.
- FOI: **ready not sent** (human-gated; info@svbejaardenzorg.be).
- NOT every-10 (**next every-10 is 2070**). Next: rq_2067 (AGB/FARO-if-YE2025 / AIESH-REW / Leiehome-Compostela-AlwaysHome-Vulpia deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2066")

# ephemeral tick2072 — WZC Maria's Rustoord Moorslede YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T23:05:00Z"
ENTITY = "vzw_wzc_maria_rustoord_moorslede"
GAP = "gap_maria_moorslede_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_maria_moorslede_jr2025_cw"
SRC_EN = "src_maria_moorslede_jr2025_cw_en"
SRC_FR = "src_maria_moorslede_jr2025_cw_fr"
SRC_KBO = "src_maria_moorslede_kbo_2072"
SRC_SITE = "src_maria_moorslede_site_2072"

OMZET = "6022436"
PNL = "573226"
EQUITY = "5409227"
BRUTO = "6333433"
FTE = "76.8"
OMZET24 = "5878939"
PNL24 = "338717"
EQUITY24 = "4991342"
BRUTO24 = "6019016"
PI = "4.8"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2072")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Maria's Rustoord Moorslede YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0411600692/wzc-maria-s-rustoord",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2072; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 01.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2072/maria_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Maria's Rustoord Moorslede YE2025 statutory",
        "url": "https://www.companyweb.be/en/0411600692/wzc-maria-s-rustoord",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2072; EN mirror YE2025 Medium; filed 01-07-2026; FTE 76.8; raw docs/doge/data/raw/tick2072/maria_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Maria's Rustoord Moorslede YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0411600692/wzc-maria-s-rustoord",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2072; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2072/maria_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC Maria's Rustoord 0411.600.692 Actief VZW Moorslede",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411600692",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2072; Actief VZW; Beselarestraat 15 8890 Moorslede; 1 VE; NACE 87.301; KBO email/tel empty; aanbestedende flag not present; raw docs/doge/data/raw/tick2072/maria_kbo.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "WZC Maria's Rustoord Dadizele site info@mariasrustoord.be",
        "url": "http://mariasrustoord.be/",
        "publisher": "WZC Maria's Rustoord vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2072; Dadizele/Moorslede WZC; FOI email info@mariasrustoord.be; raw docs/doge/data/raw/tick2072/maria_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_maria_moorslede_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2072; omzet JUMP {OMZET} +2.44pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_maria_moorslede_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2072; pnl JUMP {PNL} +69.23pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_maria_moorslede_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2072; equity JUMP {EQUITY} +8.37pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_maria_moorslede_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2072; bruto JUMP {BRUTO} +5.22pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_maria_moorslede_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2072; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_maria_moorslede_jr2025_statutory_wzc",
    "title": "WZC Maria's Rustoord Moorslede YE2025 leftover dual (omzet JUMP 6.02m / pnl JUMP 0.57m)",
    "entity_id": ENTITY,
    "beneficiary": "Moorslede-Dadizele elderly residents (WZC Maria's Rustoord)",
    "legal_basis": "VZW WZC / publiek gesubsidieerde zorg (KBO 0411.600.692)",
    "decision_date": "2026-07-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0411600692/wzc-maria-s-rustoord",
    "stated_goal": "WZC residential elderly care Moorslede Dadizele Beselarestraat",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl JUMP +69pct vs omzet +2.4pct",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Moorslede>Maria_Rustoord>JR2025_statutory_L5",
    "notes": "tick2072; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT from Maria Rustoord Ingelmunster 0458.458.325; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_maria_moorslede_omzet_jump_6_02m_pnl_jump_jr2025",
    "name": "WZC Maria's Rustoord Moorslede omzet JUMP 6.02m / pnl JUMP 0.57m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Moorslede>Maria_Rustoord>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual Dadizele",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Moorslede-Dadizele elderly residents via WZC Maria's Rustoord",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 6.02m omzet JUMP +2.44pct with pnl JUMP +69.23pct and equity JUMP +8.37pct; NBB PDF residual",
    "absurdity_score": "4.6",
    "cost_score": "4.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl JUMP +69pct vs modest omzet growth; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2072 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2080",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "WZC Maria's Rustoord (VZW, Moorslede-Dadizele)",
    "name_fr": "WZC Maria's Rustoord (ASBL MRS, Moorslede-Dadizele)",
    "name_en": "WZC Maria's Rustoord (VZW nursing home Moorslede-Dadizele)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "http://mariasrustoord.be/",
    "foi_email": "info@mariasrustoord.be",
    "foi_postal": "Beselarestraat 15, 8890 Moorslede",
    "notes": "tick2072 YE2025 Medium CW NL+EN+FR + Strong KBO 0411.600.692 Actief VZW 1 VE; omzet JUMP 6.02m pnl JUMP 0.57m equity JUMP 5.41m bruto JUMP 6.33m FTE 76.8; assets/debt Unknown; neerlegging 01.07.2026; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT from Maria Rustoord Ingelmunster; do not redo MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie",
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
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Moorslede>Maria_Rustoord>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl JUMP +69.23pct with omzet only +2.44pct",
    "why_it_matters": "Medium CW shows 6.02m omzet WZC VZW with sharp pnl JUMP without balanstotaal/assets/debt; material L5 residual for FOI; distinct from already-mined Maria Rustoord Ingelmunster",
    "priority": "8",
    "recipient_body": "WZC Maria's Rustoord vzw",
    "recipient_email": "info@mariasrustoord.be",
    "recipient_postal": "Beselarestraat 15, 8890 Moorslede",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_maria_moorslede_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_maria_moorslede_omzet_jump_6_02m_pnl_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2072; human-send only; Medium CW; next every-10 2080",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Maria's Rustoord Moorslede (NBB PDF / assets-debt / pnl-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** WZC Maria's Rustoord VZW — KBO **0411.600.692**  
**recipient:** info@mariasrustoord.be · Beselarestraat 15, 8890 Moorslede  
**sources:** [CW NL](https://www.companyweb.be/nl/0411600692/wzc-maria-s-rustoord) · [CW EN](https://www.companyweb.be/en/0411600692/wzc-maria-s-rustoord) · [CW FR](https://www.companyweb.be/fr/0411600692/wzc-maria-s-rustoord) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411600692) · [site](http://mariasrustoord.be/)  
**tick:** 2072  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **01.07.2026**): omzet **EUR6,022,436** JUMP +2.44%; pnl **EUR573,226** JUMP +69.23% vs YE2024 EUR338,717; equity **EUR5,409,227** JUMP +8.37%; bruto **EUR6,333,433** JUMP +5.22%; FTE **76.8**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Beselarestraat 15 Moorslede (Dadizele); NACE 87.301; KBO email empty; site info@mariasrustoord.be.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. DISTINCT from Maria Rustoord Ingelmunster (0458.458.325).

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: WZC Maria's Rustoord vzw — Beselarestraat 15, 8890 Moorslede
info@mariasrustoord.be
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Maria's Rustoord Moorslede + subsidiematrix (KBO 0411.600.692)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 01.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting stijging winst van EUR338.717 (YE2024) naar EUR573.226 (YE2025; +69,23%) bij omzetgroei van slechts +2,44%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, "
    "Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, "
    "Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, "
    "WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, "
    "Maria Rustoord Ingelmunster, Always Home, Armonea, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
    "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear. "
    "Leftover Mater Amabilis Wervik 0417.430.293 YE2025 live unused; Heilig Hart Grimbergen 0409.724.238 YE2025 live unused."
)

for x in qrows:
    if x.get("task_id") == "rq_2072":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual — WZC Maria's Rustoord Moorslede YE2025 Medium"
        x["notes"] = (
            "tick2072 Maria Moorslede Medium omzet JUMP 6.02m pnl JUMP 0.57m equity JUMP 5.41m bruto JUMP 6.33m; "
            "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2073; next every-10 2080"
        )
        x["instructions"] = (
            f"Completed leftover Maria's Rustoord Moorslede YE2025 Medium CW; KBO 0411.600.692; omzet JUMP {OMZET} pnl JUMP {PNL} "
            f"equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}; DISTINCT Ingelmunster"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2073" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2073",
            "title": "leftover dual hole-fill after Maria Moorslede — prefer AGB/FARO-YE2025/AIESH-REW/Mater-Amabilis/HH-Grimbergen",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2072 after Maria's Rustoord Moorslede YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else Mater Amabilis Wervik 0417.430.293 YE2025 live unused / Heilig Hart Grimbergen 0409.724.238 YE2025 live unused / "
                "unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. " + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2072 Maria Moorslede; next every-10 2080",
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
        "last_unit_id": "rq_2072",
        "ticks_completed": "2072",
        "paused": "no",
        "notes": (
            "tick2072 leftover Maria Moorslede 0411.600.692 Medium CW (omzet JUMP 6.02m pnl JUMP 0.57m equity JUMP 5.41m "
            "bruto JUMP 6.33m FTE 76.8; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2073; "
            "next every-10 2080; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_path.write_text(
    log_path.read_text(encoding="utf-8")
    + f"""

## Tick 2072 - 2026-08-24T23:05:00Z - rq_2072 Maria Moorslede (omzet JUMP 6.02m / pnl JUMP 0.57m / Medium)

- Unit: **rq_2072** leftover dual after **rq_2071 MSW NZVL**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **WZC Maria's Rustoord Moorslede** YE2025 (KBO **0411.600.692**; Beselarestraat 15 Moorslede-Dadizele; West-Vlaanderen **VZW** WZC / **1 VE**). DISTINCT from Maria Rustoord Ingelmunster. Mater Amabilis Wervik / Heilig Hart Grimbergen YE2025 also live - deferred. Do not redo MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Zusters SV Deinze/OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR6,022,436** JUMP +2.44%; pnl **EUR573,226** JUMP +69.23% vs YE2024 EUR338,717; equity **EUR5,409,227** JUMP +8.37%; bruto **EUR6,333,433** JUMP +5.22%; FTE **76.8**; neerlegging **01.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@mariasrustoord.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2072=done + rq_2073 open; loop_state ticks=2072; raw under docs/doge/data/raw/tick2072/.
- FOI: **ready not sent** (human-gated; info@mariasrustoord.be).
- NOT every-10 (**next every-10 is 2080**). Next: rq_2073 (AGB/FARO-if-YE2025 / AIESH-REW / Mater-Amabilis-HH-Grimbergen deferred / unused DSO-IGS-HVZ-WZC-psych).
""",
    encoding="utf-8",
)
print("log ok")
print("DONE tick2072")

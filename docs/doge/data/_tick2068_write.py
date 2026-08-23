# ephemeral tick2068 — Compostela YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T22:05:00Z"
ENTITY = "vzw_compostela"
GAP = "gap_compostela_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_compostela_jr2025_cw"
SRC_EN = "src_compostela_jr2025_cw_en"
SRC_FR = "src_compostela_jr2025_cw_fr"
SRC_KBO = "src_compostela_kbo_2068"
SRC_SITE = "src_compostela_site_2068"
SRC_ZORG = "src_compostela_zorg_repertorium_2068"

OMZET = "37795157"
PNL = "1228006"
EQUITY = "60201736"
BRUTO = "39900746"
FTE = "497.1"
OMZET24 = "36698802"
PNL24 = "1608382"
EQUITY24 = "59348989"
BRUTO24 = "38849670"
# pi = 0.55*5.5 + 0.35*5.2 + 0.10*(10-4) = 3.025 + 1.82 + 0.6 = 5.445 → 5.4
PI = "5.4"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2068")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Compostela YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0432401155/compostela",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2068; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 27.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2068/compostela_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Compostela YE2025 statutory",
        "url": "https://www.companyweb.be/en/0432401155/compostela",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2068; EN mirror YE2025 Medium; filed 27-06-2026; Last balance sheet year 2025; FTE 497.1; raw docs/doge/data/raw/tick2068/compostela_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Compostela YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0432401155/compostela",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2068; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2068/compostela_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Compostela 0432.401.155 Actief VZW Antwerpen-Borsbeek",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0432401155",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2068; Actief VZW; Doolweg 6 2150 Antwerpen; 7 VE; NACE 87.301; aanbestedende overheid; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Compostela / WoonZorgCollectief site",
        "url": "https://www.compostela.be/",
        "publisher": "VZW Compostela / WoonZorgCollectief",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2068; multi-site WZC group Borsbeek+; FOI email compostela@compostela.be from Departement Zorg repertorium; raw docs/doge/data/raw/tick2068/compostela_site.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_ZORG,
        "title": "Departement Zorg repertorium Compostela compostela@compostela.be",
        "url": "https://www.zorg-en-gezondheid.be/sites/default/files/external/Repertorium_burst_def_-_ADRESSEN_WZC-_PROVINCIE_Antwerpen.pdf",
        "publisher": "Departement Zorg Vlaanderen",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2068; PE1313 Compostela Doolweg 6; tel 03 366 50 90; email compostela@compostela.be; capacity 98; sister sites cocoon@ / cleo@",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_compostela_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2068; omzet JUMP {OMZET} +2.99pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_compostela_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2068; pnl DROP {PNL} -23.65pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_compostela_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2068; equity JUMP {EQUITY} +1.44pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_compostela_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2068; bruto JUMP {BRUTO} +2.71pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_compostela_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2068; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_compostela_jr2025_statutory_wzc",
    "title": "Compostela YE2025 leftover dual (omzet JUMP 37.80m / pnl DROP 1.23m)",
    "entity_id": ENTITY,
    "beneficiary": "Antwerpen-Borsbeek belt elderly residents (WZC Compostela group)",
    "legal_basis": "VZW WZC / aanbestedende overheid / publiek gesubsidieerde zorg (KBO 0432.401.155)",
    "decision_date": "2026-06-27",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0432401155/compostela",
    "stated_goal": "Multi-site WZC / assistentiewoningen / kortverblijf / dagverzorging (WoonZorgCollectief)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl DROP -23.65pct",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Borsbeek>Compostela>JR2025_statutory_L5",
    "notes": "tick2068; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_compostela_omzet_jump_37_80m_pnl_drop_jr2025",
    "name": "Compostela omzet JUMP 37.80m / pnl DROP 1.23m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>Antwerpen>Borsbeek>Compostela>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; multi-site WZC VZW dual aanbestedende overheid",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Antwerpen-Borsbeek belt elderly residents via Compostela / WoonZorgCollectief",
    "stated_goal": "Multi-site WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 37.80m omzet JUMP +2.99pct with pnl DROP -23.65pct; NBB PDF residual",
    "absurdity_score": "5.2",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP; map IFIC/Alivia vs dagprijs split across 7 VE",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2068 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Compostela (VZW WZC-groep, Borsbeek/Antwerpen)",
    "name_fr": "Compostela (ASBL groupe MRS, Borsbeek/Anvers)",
    "name_en": "Compostela (VZW nursing-home group Borsbeek/Antwerp)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.compostela.be/",
    "foi_email": "compostela@compostela.be",
    "foi_postal": "Doolweg 6, 2150 Antwerpen",
    "notes": (
        "tick2068 YE2025 Medium CW NL+EN+FR + Strong KBO 0432.401.155 Actief VZW aanbestedende overheid 7 VE; omzet JUMP 37.80m pnl DROP 1.23m equity JUMP 60.20m bruto JUMP 39.90m FTE 497.1; "
        "assets/debt Unknown; neerlegging 27.06.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Always Home/Vulpia YE2025 deferred; do not redo Leiehome/Zusters SV Deinze/OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Home Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof"
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
    "hierarchy_path": "Vlaanderen>Antwerpen>Borsbeek>Compostela>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split across 7 VE; explanation of pnl DROP -23.65pct YE2025",
    "why_it_matters": "Medium CW shows 37.80m omzet multi-site WZC VZW aanbestedende overheid with pnl DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "VZW Compostela",
    "recipient_email": "compostela@compostela.be",
    "recipient_postal": "Doolweg 6, 2150 Antwerpen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_compostela_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_compostela_omzet_jump_37_80m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2068; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Compostela (NBB PDF / assets-debt / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** VZW Compostela — KBO **0432.401.155**  
**recipient:** compostela@compostela.be · Doolweg 6, 2150 Antwerpen (Borsbeek)  
**sources:** [CW NL](https://www.companyweb.be/nl/0432401155/compostela) · [CW EN](https://www.companyweb.be/en/0432401155/compostela) · [CW FR](https://www.companyweb.be/fr/0432401155/compostela) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0432401155) · [site](https://www.compostela.be/)  
**tick:** 2068  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **27.06.2026**): omzet **EUR37,795,157** JUMP +2.99%; pnl **EUR1,228,006** DROP -23.65% vs YE2024 EUR1,608,382; equity **EUR60,201,736** JUMP +1.44%; bruto **EUR39,900,746** JUMP +2.71%; FTE **497.1**; assets/debt **Unknown**.
- KBO: Actief VZW; **7 VE**; aanbestedende overheid; zetel Doolweg 6 Antwerpen-Borsbeek; NACE 87.301; WoonZorgCollectief multi-site.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live YE2025: Always Home / Vulpia.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: VZW Compostela — Doolweg 6, 2150 Antwerpen
compostela@compostela.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Compostela + subsidiematrix (KBO 0432.401.155)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (aanbestedende overheid / publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 27.06.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025, bij voorkeur per vestigingseenheid (7 VE).
4. Toelichting daling winst van EUR1.608.382 (YE2024) naar EUR1.228.006 (YE2025; -23,65%).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, "
    "WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, "
    "Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, "
    "WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2068":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Leiehome — Compostela YE2025 Medium"
        x["notes"] = (
            "tick2068 Compostela Medium omzet JUMP 37.80m pnl DROP 1.23m equity JUMP 60.20m bruto JUMP 39.90m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2069; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover Compostela YE2025 Medium CW; KBO 0432.401.155; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2069" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2069",
            "title": "leftover dual hole-fill after Compostela",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2068 after Compostela YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Always Home / Vulpia YE2025 deferred if still live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2068 Compostela; next every-10 2070",
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
        "last_unit_id": "rq_2068",
        "ticks_completed": "2068",
        "paused": "no",
        "notes": (
            "tick2068 leftover Compostela 0432.401.155 Medium CW (omzet JUMP 37.80m pnl DROP 1.23m equity JUMP 60.20m bruto JUMP 39.90m FTE 497.1; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2069; next every-10 2070; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2068 - 2026-08-24T22:05:00Z - rq_2068 Compostela (omzet JUMP 37.80m / pnl DROP 1.23m / Medium)

- Unit: **rq_2068** leftover dual after **rq_2067 Leiehome**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Compostela** YE2025 (KBO **0432.401.155**; Doolweg 6 Antwerpen-Borsbeek; Antwerpen **aanbestedende-overheid VZW** multi-site WZC / **7 VE** / WoonZorgCollectief). Always Home / Vulpia YE2025 also live - deferred. Do not redo Leiehome/Zusters SV Deinze/OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR37,795,157** JUMP +2.99%; pnl **EUR1,228,006** DROP -23.65%; equity **EUR60,201,736** JUMP +1.44%; bruto **EUR39,900,746** JUMP +2.71%; FTE **497.1**; neerlegging **27.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 7 VE; email compostela@compostela.be.
- Wrote: sources (+6); budgets (+5); commitments (+1); leaderboard (+1 pi 5.4); entities (+1 vzw_compostela); foi + draft {GAP}; rq_2068=done + rq_2069 open; loop_state ticks=2068; raw under docs/doge/data/raw/tick2068/.
- FOI: **ready not sent** (human-gated; compostela@compostela.be).
- NOT every-10 (**next every-10 is 2070**). Next: rq_2069 (AGB/FARO-if-YE2025 / AIESH-REW / AlwaysHome-Vulpia deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2068")

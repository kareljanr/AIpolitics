# ephemeral tick2062 — WZC OLV Wezembeek-Oppem YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T20:35:00Z"
ENTITY = "vzw_wzc_olv_wezembeek"
GAP = "gap_olv_wezembeek_nbb_pdf_assets_debt_pnl_flip_loss_matrix_l5"
SRC = "src_olv_wezembeek_jr2025_cw"
SRC_EN = "src_olv_wezembeek_jr2025_cw_en"
SRC_FR = "src_olv_wezembeek_jr2025_cw_fr"
SRC_KBO = "src_olv_wezembeek_kbo_2062"
SRC_SITE = "src_olv_wezembeek_site_2062"

OMZET = "4436070"
PNL = "-8367"
EQUITY = "3164859"
BRUTO = "3763636"
FTE = "46.2"
OMZET24 = "4665578"
PNL24 = "86441"
EQUITY24 = "3202887"
BRUTO24 = "4079699"
# pi = 0.55*4.2 + 0.35*5.3 + 0.10*(10-4) = 2.31 + 1.855 + 0.6 = 4.765 → 4.8
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
r = next(x for x in qrows if x.get("task_id") == "rq_2062")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC OLV Wezembeek-Oppem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2062; YE2025 omzet DROP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 13.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2062/wezembeek_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC OLV Wezembeek-Oppem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2062; EN mirror YE2025 Medium; filed 13-07-2026; Last balance sheet year 2025; FTE 46.2; raw docs/doge/data/raw/tick2062/wezembeek_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC OLV Wezembeek-Oppem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2062; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2062/wezembeek_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC OLV Wezembeek-Oppem 0433.419.259 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0433419259",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2062; Actief VZW; Jan Baptist De Keyzerstraat 35 1970 Wezembeek-Oppem (since 22.04.1999); 1 VE; NACE 87.301; KBO email empty; not marked aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "WZC OLV Wezembeek site wzc-olvrouw.be (info@wzc-olvrouw.be)",
        "url": "https://wzc-olvrouw.be/",
        "publisher": "Woon- en Zorgcentrum Onze-Lieve-Vrouw vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2062; JB De Keyzerstraat 35 1970 Wezembeek-Oppem; Tel 02/731.27.39; email via Sociale Kaart/gemeente info@wzc-olvrouw.be; raw docs/doge/data/raw/tick2062/wezembeek_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_olv_wezembeek_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2062; omzet DROP {OMZET} -4.92pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_olv_wezembeek_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2062; pnl FLIP LOSS {PNL} vs YE2024 profit {PNL24} (-109.68pct)",
    },
    {
        "budget_id": "bud_olv_wezembeek_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2062; equity DROP {EQUITY} -1.19pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_olv_wezembeek_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2062; bruto DROP {BRUTO} -7.75pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_olv_wezembeek_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2062; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_olv_wezembeek_jr2025_statutory_wzc",
    "title": "WZC OLV Wezembeek YE2025 leftover dual (omzet DROP 4.44m / pnl FLIP LOSS 8k)",
    "entity_id": ENTITY,
    "beneficiary": "Wezembeek-Oppem elderly residents (WZC OLV)",
    "legal_basis": "VZW WZC / publiek gesubsidieerde zorg (KBO 0433.419.259)",
    "decision_date": "2026-07-13",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem",
    "stated_goal": "WZC residential elderly care Wezembeek-Oppem JB De Keyzerstraat",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl FLIP LOSS despite modest omzet DROP",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>WezembeekOppem>WZCOLV>JR2025_statutory_L5",
    "notes": "tick2062; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nlb = {
    **{k: "" for k in lfields},
    "item_id": "lb_olv_wezembeek_omzet_drop_4_44m_pnl_flip_loss_jr2025",
    "name": "WZC OLV Wezembeek omzet DROP 4.44m / pnl FLIP LOSS 8k (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>WezembeekOppem>WZCOLV>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet DROP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Wezembeek-Oppem elderly residents via WZC OLV",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 4.44m omzet DROP -4.92pct with pnl FLIP LOSS vs YE2024 profit 86k; NBB PDF residual",
    "absurdity_score": "5.3",
    "cost_score": "4.2",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2062 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nlb["item_id"] for x in lrows):
    lrows.append(nlb)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "WZC Onze-Lieve-Vrouw Wezembeek-Oppem (VZW)",
    "name_fr": "MRS Notre-Dame Wezembeek-Oppem (ASBL)",
    "name_en": "WZC Onze-Lieve-Vrouw Wezembeek-Oppem (VZW nursing home)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://wzc-olvrouw.be/",
    "foi_email": "info@wzc-olvrouw.be",
    "foi_postal": "Jan Baptist De Keyzerstraat 35, 1970 Wezembeek-Oppem",
    "notes": (
        "tick2062 YE2025 Medium CW NL+EN+FR + Strong KBO 0433.419.259 Actief VZW 1 VE; omzet DROP 4.44m pnl FLIP LOSS 8k equity DROP 3.16m bruto DROP 3.76m FTE 46.2; "
        "assets/debt Unknown; neerlegging 13.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Ter Burg/Christine/Home Vrijzicht/'t Pandje/Groep Zorg H. Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem"
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
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>WezembeekOppem>WZCOLV>NBB_PDF_assets_debt_pnl_flip_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl FLIP LOSS YE2025 vs YE2024 profit",
    "why_it_matters": "Medium CW shows 4.44m omzet WZC VZW with pnl FLIP LOSS without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Woon- en Zorgcentrum Onze-Lieve-Vrouw te Wezembeek-Oppem vzw",
    "recipient_email": "info@wzc-olvrouw.be",
    "recipient_postal": "Jan Baptist De Keyzerstraat 35, 1970 Wezembeek-Oppem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_olv_wezembeek_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_olv_wezembeek_omzet_drop_4_44m_pnl_flip_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2062; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC OLV Wezembeek (NBB PDF / assets-debt / pnl-flip-loss)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon en zorgcentrum Onze-Lieve-Vrouw te Wezembeek-Oppem VZW — KBO **0433.419.259**  
**recipient:** info@wzc-olvrouw.be · Jan Baptist De Keyzerstraat 35, 1970 Wezembeek-Oppem  
**sources:** [CW NL](https://www.companyweb.be/nl/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem) · [CW EN](https://www.companyweb.be/en/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem) · [CW FR](https://www.companyweb.be/fr/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0433419259) · [site](https://wzc-olvrouw.be/)  
**tick:** 2062  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **13.07.2026**): omzet **EUR4,436,070** DROP −4.92%; pnl **LOSS EUR-8,367** FLIP vs YE2024 profit EUR86,441; equity **EUR3,164,859** DROP −1.19%; bruto **EUR3,763,636** DROP −7.75%; FTE **46.2**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Jan Baptist De Keyzerstraat 35 Wezembeek-Oppem; NACE 87.301; niet gemarkeerd als aanbestedende overheid.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live YE2025: Sint-Antonius.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en Zorgcentrum Onze-Lieve-Vrouw te Wezembeek-Oppem vzw — Jan Baptist De Keyzerstraat 35, 1970 Wezembeek-Oppem
info@wzc-olvrouw.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC OLV Wezembeek + subsidiematrix (KBO 0433.419.259)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 13.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting omslag van winst EUR86.441 (YE2024) naar verlies EUR-8.367 (YE2025) bij omzet DROP −4,92%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo WZC OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, "
    "Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, "
    "WZC De Foyer Gent, Zusterhof, Veilige Have, Witte Meren, Sint-Jozef Rumst, Werken Glorieux, IPFBW, IGRETEC, "
    "Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
    "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2062":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Ter Burg — OLV Wezembeek YE2025 Medium"
        x["notes"] = (
            "tick2062 OLV Wezembeek Medium omzet DROP 4.44m pnl FLIP LOSS 8k equity DROP 3.16m bruto DROP 3.76m; "
            "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2063; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover WZC OLV Wezembeek YE2025 Medium CW; KBO 0433.419.259; "
            f"omzet DROP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2063" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2063",
            "title": "leftover dual hole-fill after WZC OLV Wezembeek",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2062 after OLV Wezembeek YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Sint-Antonius YE2025 deferred if still live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2062 OLV Wezembeek; next every-10 2070",
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
        "last_unit_id": "rq_2062",
        "ticks_completed": "2062",
        "paused": "no",
        "notes": (
            "tick2062 leftover OLV Wezembeek 0433.419.259 Medium CW (omzet DROP 4.44m pnl FLIP LOSS 8k equity DROP 3.16m bruto DROP 3.76m FTE 46.2; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2063; next every-10 2070; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("loop_state ok")

log = Path("docs/doge/loop_log.md")
block = f"""


## Tick 2062 - 2026-08-24T20:35:00Z - rq_2062 OLV Wezembeek (omzet DROP 4.44m / pnl FLIP LOSS 8k / Medium)

- Unit: **rq_2062** leftover dual after **rq_2061 WZC Ter Burg**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **WZC OLV Wezembeek-Oppem** YE2025 (KBO **0433.419.259**; Jan Baptist De Keyzerstraat 35 Wezembeek-Oppem; Vlaams-Brabant **VZW** WZC / **1 VE**). Sint-Antonius YE2025 also live — deferred. Do not redo Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR4,436,070** DROP −4.92%; pnl **LOSS EUR-8,367** FLIP vs YE2024 profit EUR86,441; equity **EUR3,164,859** DROP −1.19%; bruto **EUR3,763,636** DROP −7.75%; FTE **46.2**; neerlegging **13.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@wzc-olvrouw.be (Sociale Kaart / gemeente).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 4.8); entities (+1 vzw_wzc_olv_wezembeek); foi + draft {GAP}; rq_2062=done + rq_2063 open; loop_state ticks=2062; raw under docs/doge/data/raw/tick2062/.
- FOI: **ready not sent** (human-gated; info@wzc-olvrouw.be).
- NOT every-10 (**next every-10 is 2070**). Next: rq_2063 (AGB/FARO-if-YE2025 / AIESH-REW / Sint-Antonius / unused DSO-IGS-HVZ-WZC-psych).
"""
log.write_text(log.read_text(encoding="utf-8") + block, encoding="utf-8")
print("log ok")
print("DONE tick2062")

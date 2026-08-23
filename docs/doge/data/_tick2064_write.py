# ephemeral tick2064 — Huize Sint-Jozef Ieper YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T21:05:00Z"
ENTITY = "vzw_huize_sint_jozef_ieper"
GAP = "gap_huize_sj_ieper_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_huize_sj_ieper_jr2025_cw"
SRC_EN = "src_huize_sj_ieper_jr2025_cw_en"
SRC_FR = "src_huize_sj_ieper_jr2025_cw_fr"
SRC_KBO = "src_huize_sj_ieper_kbo_2064"
SRC_SITE = "src_huize_sj_ieper_site_2064"

OMZET = "8360491"
PNL = "1129712"
EQUITY = "10622287"
BRUTO = "8398601"
FTE = "95.2"
OMZET24 = "8118741"
PNL24 = "1240962"
EQUITY24 = "9492976"
BRUTO24 = "8424207"
# pi = 0.55*4.8 + 0.35*4.9 + 0.10*(10-4) = 2.64 + 1.715 + 0.6 = 4.955 → 5.0
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
r = next(x for x in qrows if x.get("task_id") == "rq_2064")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Huize Sint-Jozef Ieper YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0409942289/huize-sint-jozef",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2064; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 05.05.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2064/huize_sj_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Huize Sint-Jozef Ieper YE2025 statutory",
        "url": "https://www.companyweb.be/en/0409942289/huize-sint-jozef",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2064; EN mirror YE2025 Medium; filed 05-05-2026; Last balance sheet year 2025; FTE 95.2; raw docs/doge/data/raw/tick2064/huize_sj_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Huize Sint-Jozef Ieper YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0409942289/huize-sint-jozef",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2064; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2064/huize_sj_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Huize Sint-Jozef 0409.942.289 Actief VZW Ieper",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409942289",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2064; Actief VZW; Meenseweg 31 8900 Ieper; 1 VE; NACE 87.301; aanbestedende overheid; replaces 0409.955.652 closed 07.08.2013; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Huize Sint-Jozef Ieper site onthaal@huizesintjozef.be",
        "url": "https://www.huizesintjozef.be/",
        "publisher": "Huize Sint-Jozef vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2064; site+contact onthaal@huizesintjozef.be; tel +32 57 22 73 71; raw docs/doge/data/raw/tick2064/huize_sj_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_huize_sj_ieper_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2064; omzet JUMP {OMZET} +2.98pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_huize_sj_ieper_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2064; pnl DROP {PNL} -8.97pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_huize_sj_ieper_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2064; equity JUMP {EQUITY} +11.90pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_huize_sj_ieper_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2064; bruto DROP {BRUTO} -0.30pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_huize_sj_ieper_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2064; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_huize_sj_ieper_jr2025_statutory_wzc",
    "title": "Huize Sint-Jozef Ieper YE2025 leftover dual (omzet JUMP 8.36m / pnl DROP 1.13m)",
    "entity_id": ENTITY,
    "beneficiary": "Ieper elderly residents (Huize Sint-Jozef)",
    "legal_basis": "VZW WZC / aanbestedende overheid / publiek gesubsidieerde zorg (KBO 0409.942.289)",
    "decision_date": "2026-05-05",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0409942289/huize-sint-jozef",
    "stated_goal": "WZC residential elderly care Ieper Meenseweg (NOT Rumst/Rillaar Sint-Jozef)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl DROP with equity JUMP",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>HuizeSintJozef>JR2025_statutory_L5",
    "notes": "tick2064; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; distinct from Sint-Jozef Rumst/Rillaar; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_huize_sj_ieper_omzet_jump_8_36m_pnl_drop_jr2025",
    "name": "Huize Sint-Jozef Ieper omzet JUMP 8.36m / pnl DROP 1.13m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>HuizeSintJozef>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual aanbestedende overheid",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Ieper elderly residents via Huize Sint-Jozef",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 8.36m omzet JUMP +2.98pct with pnl DROP -8.97pct and equity JUMP +11.90pct; NBB PDF residual",
    "absurdity_score": "4.9",
    "cost_score": "4.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP vs equity JUMP; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2064 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Huize Sint-Jozef (VZW WZC, Ieper)",
    "name_fr": "Huize Sint-Jozef (ASBL MRS, Ieper)",
    "name_en": "Huize Sint-Jozef (VZW nursing home Ieper)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.huizesintjozef.be/",
    "foi_email": "onthaal@huizesintjozef.be",
    "foi_postal": "Meenseweg 31, 8900 Ieper",
    "notes": (
        "tick2064 YE2025 Medium CW NL+EN+FR + Strong KBO 0409.942.289 Actief VZW aanbestedende overheid 1 VE; omzet JUMP 8.36m pnl DROP 1.13m equity JUMP 10.62m bruto DROP 8.40m FTE 95.2; "
        "assets/debt Unknown; neerlegging 05.05.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT from Sint-Jozef Rumst/Rillaar; do not redo Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Home Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof"
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
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>HuizeSintJozef>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl DROP -8.97pct with equity JUMP +11.90pct YE2025",
    "why_it_matters": "Medium CW shows 8.36m omzet WZC VZW aanbestedende overheid with pnl DROP + equity JUMP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Huize Sint-Jozef vzw",
    "recipient_email": "onthaal@huizesintjozef.be",
    "recipient_postal": "Meenseweg 31, 8900 Ieper",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_huize_sj_ieper_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_huize_sj_ieper_omzet_jump_8_36m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2064; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Huize Sint-Jozef Ieper (NBB PDF / assets-debt / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Huize Sint-Jozef VZW — KBO **0409.942.289**  
**recipient:** onthaal@huizesintjozef.be · Meenseweg 31, 8900 Ieper  
**sources:** [CW NL](https://www.companyweb.be/nl/0409942289/huize-sint-jozef) · [CW EN](https://www.companyweb.be/en/0409942289/huize-sint-jozef) · [CW FR](https://www.companyweb.be/fr/0409942289/huize-sint-jozef) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409942289) · [site](https://www.huizesintjozef.be/)  
**tick:** 2064  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **05.05.2026**): omzet **EUR8,360,491** JUMP +2.98%; pnl **EUR1,129,712** DROP -8.97% vs YE2024 EUR1,240,962; equity **EUR10,622,287** JUMP +11.90%; bruto **EUR8,398,601** DROP -0.30%; FTE **95.2**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; aanbestedende overheid; zetel Meenseweg 31 Ieper; NACE 87.301; DISTINCT from Sint-Jozef Rumst/Rillaar.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live YE2025 candidates: Leiehome / Compostela / Always Home / Vulpia.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Huize Sint-Jozef vzw — Meenseweg 31, 8900 Ieper
onthaal@huizesintjozef.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Huize Sint-Jozef Ieper + subsidiematrix (KBO 0409.942.289)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (aanbestedende overheid / publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 05.05.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting daling winst van EUR1.240.962 (YE2024) naar EUR1.129.712 (YE2025; -8,97%) bij equity JUMP +11,90%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, "
    "'t Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, "
    "Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, "
    "Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, "
    "FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, "
    "Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2064":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Sint-Antonius — Huize Sint-Jozef Ieper YE2025 Medium"
        x["notes"] = (
            "tick2064 Huize Sint-Jozef Ieper Medium omzet JUMP 8.36m pnl DROP 1.13m equity JUMP 10.62m bruto DROP 8.40m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2065; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover Huize Sint-Jozef Ieper YE2025 Medium CW; KBO 0409.942.289; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2065" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2065",
            "title": "leftover dual hole-fill after Huize Sint-Jozef Ieper",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2064 after Huize Sint-Jozef Ieper YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Leiehome / Compostela / Always Home / Vulpia YE2025 deferred if still live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2064 Huize Sint-Jozef Ieper; next every-10 2070",
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
        "last_unit_id": "rq_2064",
        "ticks_completed": "2064",
        "paused": "no",
        "notes": (
            "tick2064 leftover Huize Sint-Jozef Ieper 0409.942.289 Medium CW (omzet JUMP 8.36m pnl DROP 1.13m equity JUMP 10.62m bruto DROP 8.40m FTE 95.2; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2065; next every-10 2070; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2064 - 2026-08-24T21:05:00Z - rq_2064 Huize Sint-Jozef Ieper (omzet JUMP 8.36m / pnl DROP 1.13m / Medium)

- Unit: **rq_2064** leftover dual after **rq_2063 Sint-Antonius**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Huize Sint-Jozef Ieper** YE2025 (KBO **0409.942.289**; Meenseweg 31 Ieper; West-Vlaanderen **aanbestedende-overheid VZW** WZC / **1 VE**). DISTINCT from Sint-Jozef Rumst/Rillaar. Leiehome / Compostela / Always Home / Vulpia YE2025 also live - deferred. Do not redo Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof/Woonhaven.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR8,360,491** JUMP +2.98%; pnl **EUR1,129,712** DROP -8.97%; equity **EUR10,622,287** JUMP +11.90%; bruto **EUR8,398,601** DROP -0.30%; FTE **95.2**; neerlegging **05.05.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email onthaal@huizesintjozef.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.0); entities (+1 vzw_huize_sint_jozef_ieper); foi + draft {GAP}; rq_2064=done + rq_2065 open; loop_state ticks=2064; raw under docs/doge/data/raw/tick2064/.
- FOI: **ready not sent** (human-gated; onthaal@huizesintjozef.be).
- NOT every-10 (**next every-10 is 2070**). Next: rq_2065 (AGB/FARO-if-YE2025 / AIESH-REW / Leiehome-Compostela-AlwaysHome-Vulpia deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2064")

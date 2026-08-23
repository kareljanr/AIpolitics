# ephemeral tick2069 — Vulpia Vlaanderen YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T22:20:00Z"
ENTITY = "vzw_vulpia_vlaanderen"
GAP = "gap_vulpia_vl_nbb_pdf_assets_debt_pnl_drop_thin_equity_matrix_l5"
SRC = "src_vulpia_vl_jr2025_cw"
SRC_EN = "src_vulpia_vl_jr2025_cw_en"
SRC_FR = "src_vulpia_vl_jr2025_cw_fr"
SRC_KBO = "src_vulpia_vl_kbo_2069"
SRC_SITE = "src_vulpia_vl_site_2069"

OMZET = "198151222"
PNL = "596759"
EQUITY = "617922"
BRUTO = "137168547"
FTE = "1902.1"
OMZET24 = "189377878"
PNL24 = "6852825"
EQUITY24 = "27363"
BRUTO24 = "132394925"
# cost~6.8 absurdity~5.8 difficulty 4 → 0.55*6.8+0.35*5.8+0.6 = 6.37 → 6.4
PI = "6.4"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2069")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Vulpia Vlaanderen YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0521970559/vulpia-vlaanderen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2069; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 23.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2069/vulpia_vl_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Vulpia Vlaanderen YE2025 statutory",
        "url": "https://www.companyweb.be/en/0521970559/vulpia-vlaanderen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2069; EN mirror YE2025 Medium; filed 23-07-2026; Last balance sheet year 2025; FTE 1902.1; raw docs/doge/data/raw/tick2069/vulpia_vl_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Vulpia Vlaanderen YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0521970559/vulpia-vlaanderen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2069; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2069/vulpia_vl_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Vulpia Vlaanderen 0521.970.559 Actief VZW Brasschaat",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0521970559",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2069; Actief VZW; Ruiterijschool 6 2930 Brasschaat; 34 VE; NACE 87.301/87.101; inschrijvingsplichtige onderneming; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Vulpia site info@vulpia.be",
        "url": "https://vulpia.be/contact",
        "publisher": "Vulpia",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2069; contact info@vulpia.be; tel 03 680 29 90; HQ Ruiterijschool 6 Brasschaat",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_vulpia_vl_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2069; omzet JUMP {OMZET} +4.63pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_vulpia_vl_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2069; pnl DROP {PNL} -91.29pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_vulpia_vl_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2069; equity JUMP {EQUITY} from thin YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_vulpia_vl_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2069; bruto JUMP {BRUTO} +3.61pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_vulpia_vl_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2069; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_vulpia_vl_jr2025_statutory_wzc",
    "title": "Vulpia Vlaanderen YE2025 leftover dual (omzet JUMP 198.15m / pnl DROP 0.60m)",
    "entity_id": ENTITY,
    "beneficiary": "Flanders elderly residents (Vulpia multi-site WZC network)",
    "legal_basis": "VZW WZC / publiek gesubsidieerde zorg (KBO 0521.970.559)",
    "decision_date": "2026-07-23",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0521970559/vulpia-vlaanderen",
    "stated_goal": "Multi-site WZC / RVT residential elderly care Flanders (34 VE)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl DROP -91.29pct and thin equity vs 198m omzet",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Brasschaat>VulpiaVlaanderen>JR2025_statutory_L5",
    "notes": "tick2069; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Always Home=Armonea skipped; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_vulpia_vl_omzet_jump_198_15m_pnl_drop_jr2025",
    "name": "Vulpia Vlaanderen omzet JUMP 198.15m / pnl DROP 0.60m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>Antwerpen>Brasschaat>VulpiaVlaanderen>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; multi-site WZC VZW dual 34 VE",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Flanders elderly residents via Vulpia WZC network",
    "stated_goal": "Multi-site WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 198.15m omzet JUMP +4.63pct with pnl DROP -91.29pct to 0.60m and thin equity 0.62m; NBB PDF residual",
    "absurdity_score": "5.8",
    "cost_score": "6.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP -91pct + thin equity vs 198m flow; map IFIC/Alivia vs dagprijs across 34 VE",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2069 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Vulpia Vlaanderen (VZW WZC-groep, Brasschaat)",
    "name_fr": "Vulpia Vlaanderen (ASBL groupe MRS, Brasschaat)",
    "name_en": "Vulpia Vlaanderen (VZW nursing-home group Brasschaat)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://vulpia.be/",
    "foi_email": "info@vulpia.be",
    "foi_postal": "Ruiterijschool 6, 2930 Brasschaat",
    "notes": (
        "tick2069 YE2025 Medium CW NL+EN+FR + Strong KBO 0521.970.559 Actief VZW 34 VE; omzet JUMP 198.15m pnl DROP 0.60m equity JUMP 0.62m bruto JUMP 137.17m FTE 1902.1; "
        "assets/debt Unknown; neerlegging 23.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Always Home skipped (Armonea); do not redo Compostela/Leiehome/Zusters SV Deinze/OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Home Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea"
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
    "hierarchy_path": "Vlaanderen>Antwerpen>Brasschaat>VulpiaVlaanderen>NBB_PDF_assets_debt_pnl_drop_thin_equity",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split across 34 VE; explanation of pnl DROP -91.29pct and thin equity 0.62m vs 198.15m omzet",
    "why_it_matters": "Medium CW shows 198.15m omzet multi-site WZC VZW with pnl collapse + thin equity without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Vulpia Vlaanderen vzw",
    "recipient_email": "info@vulpia.be",
    "recipient_postal": "Ruiterijschool 6, 2930 Brasschaat",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_vulpia_vl_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_vulpia_vl_omzet_jump_198_15m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2069; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Vulpia Vlaanderen (NBB PDF / assets-debt / pnl-drop / thin equity)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Vulpia Vlaanderen VZW — KBO **0521.970.559**  
**recipient:** info@vulpia.be · Ruiterijschool 6, 2930 Brasschaat  
**sources:** [CW NL](https://www.companyweb.be/nl/0521970559/vulpia-vlaanderen) · [CW EN](https://www.companyweb.be/en/0521970559/vulpia-vlaanderen) · [CW FR](https://www.companyweb.be/fr/0521970559/vulpia-vlaanderen) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0521970559) · [site](https://vulpia.be/contact)  
**tick:** 2069  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **23.07.2026**): omzet **EUR198,151,222** JUMP +4.63%; pnl **EUR596,759** DROP -91.29% vs YE2024 EUR6,852,825; equity **EUR617,922** JUMP from thin YE2024 EUR27,363; bruto **EUR137,168,547** JUMP +3.61%; FTE **1902.1**; assets/debt **Unknown**.
- KBO: Actief VZW; **34 VE**; zetel Ruiterijschool 6 Brasschaat; NACE 87.301/87.101; inschrijvingsplichtige onderneming.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Always Home skipped (Armonea on do-not-redo). Compostela already taken tick2068.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Vulpia Vlaanderen vzw — Ruiterijschool 6, 2930 Brasschaat
info@vulpia.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Vulpia Vlaanderen + subsidiematrix (KBO 0521.970.559)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 23.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025 across 34 VE.
4. Toelichting pnl DROP van EUR6.852.825 (YE2024) naar EUR596.759 (YE2025) (-91,29%) bij omzet JUMP +4,63%, en dun eigen vermogen EUR617.922 vs omzet ~EUR198m.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, "
    "Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, "
    "Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, "
    "Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, "
    "Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, "
    "Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, "
    "FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, "
    "Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea, Always Home. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2069":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Compostela — Vulpia Vlaanderen YE2025 Medium"
        x["notes"] = (
            "tick2069 Vulpia Vlaanderen Medium omzet JUMP 198.15m pnl DROP 0.60m equity JUMP 0.62m bruto JUMP 137.17m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Always Home=Armonea skipped; next rq_2070 EVERY-10; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover Vulpia Vlaanderen YE2025 Medium CW; KBO 0521.970.559; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2070" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2070",
            "title": "EVERY-10 progress + leftover dual hole-fill after Vulpia Vlaanderen",
            "sprint": "hole_fill",
            "priority": "9",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2069 after Vulpia Vlaanderen YE2025 Medium. MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                "Then prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2069 Vulpia Vlaanderen; EVERY-10 mandatory at 2070",
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
        "last_unit_id": "rq_2069",
        "ticks_completed": "2069",
        "paused": "no",
        "notes": (
            "tick2069 leftover Vulpia Vlaanderen 0521.970.559 Medium CW (omzet JUMP 198.15m pnl DROP 0.60m equity JUMP 0.62m bruto JUMP 137.17m FTE 1902.1; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Always Home=Armonea skipped; next rq_2070 EVERY-10; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2069 - 2026-08-24T22:20:00Z - rq_2069 Vulpia Vlaanderen (omzet JUMP 198.15m / pnl DROP 0.60m / Medium)

- Unit: **rq_2069** leftover dual after **rq_2068 Compostela** (already on main). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Always Home YE2025 live but **Armonea** (info@armonea.be) — skipped per do-not-redo. Took deferred leftover **Vulpia Vlaanderen** YE2025 (KBO **0521.970.559**; Ruiterijschool 6 Brasschaat; Antwerpen **VZW** multi-site WZC/RVT / **34 VE**). Do not redo Compostela/Leiehome/Zusters SV Deinze/OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR198,151,222** JUMP +4.63%; pnl **EUR596,759** DROP -91.29% vs YE2024 EUR6,852,825; equity **EUR617,922** JUMP from thin YE2024 EUR27,363; bruto **EUR137,168,547** JUMP +3.61%; FTE **1902.1**; neerlegging **23.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 34 VE; email info@vulpia.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.4); entities (+1 vzw_vulpia_vlaanderen); foi + draft {GAP}; rq_2069=done + rq_2070 open (EVERY-10); loop_state ticks=2069; raw under docs/doge/data/raw/tick2069/.
- FOI: **ready not sent** (human-gated; info@vulpia.be).
- NOT every-10 (**next every-10 is 2070 THIS next tick**). Next: rq_2070 (EVERY-10 mandatory + AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2069")

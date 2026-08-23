# ephemeral tick2009 — OLVT / AZ Sint-Blasius YE2025 Medium (leftover dual after AZ Oostende)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T06:40:00Z"
ENTITY = "vzw_olvt_sint_blasius"
GAP = "gap_olvt_sint_blasius_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_olvt_sint_blasius_jr2025_cw"
SRC_EN = "src_olvt_sint_blasius_jr2025_cw_en"
SRC_FR = "src_olvt_sint_blasius_jr2025_cw_fr"
SRC_KBO = "src_olvt_sint_blasius_kbo_2009"
SRC_SITE = "src_olvt_sint_blasius_site_2009"

OMZET = "235942746"
PNL = "1990218"
EQUITY = "82628815"
BRUTO = "102389176"
FTE = "1120"
OMZET24 = "224562867"
PNL24 = "4604650"
EQUITY24 = "81476583"
BRUTO24 = "96522404"
SITE_OPBRENSTEN = "246957758"
SITE_NETTO = "2242668"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2009")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL OLVT / AZ Sint-Blasius YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0411975133",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2009; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 16.06.2026; assets/debt Unknown; site kerncijfers bedrijfsopbrengsten {SITE_OPBRENSTEN} netto {SITE_NETTO} differ from CW; raw docs/doge/data/raw/tick2009/blasius_olv_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN OLVT / AZ Sint-Blasius YE2025 statutory",
        "url": "https://www.companyweb.be/en/0411975133",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2009; EN mirror YE2025 Medium; filed 16-06-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2009/blasius_olv.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR OLVT / AZ Sint-Blasius YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0411975133",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2009; FR mirror YE2025 Medium; deposés le 16-06-2026; raw docs/doge/data/raw/tick2009/blasius_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO OLVT O.L.Vrouw van Troost 0411.975.133 Actief VZW Dendermonde",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411975133",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2009; Actief VZW since 20.01.1972; OLVT / O.L.Vrouw van Troost (AZ Sint-Blasius); Kroonveldlaan 50 9200 Dendermonde; web azsintblasius.be; no KBO email; 3 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azsintblasius.be kerncijfers + rechtspersoon OLVT",
        "url": "https://www.azsintblasius.be/over-ons/beleid/kerncijfers",
        "publisher": "AZ Sint-Blasius / OLVT",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": f"tick2009; site YE2025 bedrijfsopbrengsten {SITE_OPBRENSTEN} netto {SITE_NETTO}; rechtspersoon BE0411.975.133; info@azsintblasius.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_olvt_sint_blasius_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2009; omzet JUMP {OMZET} +5.07pct vs YE2024 {OMZET24}; site bedrijfsopbrengsten {SITE_OPBRENSTEN} differ",
    },
    {
        "budget_id": "bud_olvt_sint_blasius_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2009; pnl DROP {PNL} -56.78pct vs YE2024 {PNL24}; site netto {SITE_NETTO} differ",
    },
    {
        "budget_id": "bud_olvt_sint_blasius_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2009; equity JUMP {EQUITY} +1.41pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_olvt_sint_blasius_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2009; bruto JUMP {BRUTO} +6.08pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_olvt_sint_blasius_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2009; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_olvt_sint_blasius_jr2025_statutory_hospital",
    "title": "OLVT/AZ Sint-Blasius YE2025 leftover hospital dual (omzet JUMP 235.94m / pnl DROP 1.99m / equity JUMP 82.63m)",
    "entity_id": ENTITY,
    "beneficiary": "Dendermonde-region hospital patients / AZ Sint-Blasius",
    "legal_basis": "VZW/ASBL hospital OLVT (KBO 0411.975.133)",
    "decision_date": "2026-06-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0411975133",
    "stated_goal": "Regional hospital care (Dendermonde / Zele)",
    "cut_option": "Publish NBB PDF assets/debt + recon CW omzet vs site bedrijfsopbrengsten FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>OLVT_Sint_Blasius>JR2025_statutory_L5",
    "notes": "tick2009; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Zottegem/Turnhout/Waregem/Yperman CW N/A omzet; AZ Oostende already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_olvt_sint_blasius_omzet_jump_235_94m_pnl_drop_1_99m_equity_jump_jr2025",
    "name": "OLVT/AZ Sint-Blasius omzet JUMP 235.94m / pnl DROP 1.99m / equity JUMP 82.63m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "OostVlaanderen>OLVT_Sint_Blasius>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; site opbrengsten {SITE_OPBRENSTEN}",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Dendermonde patients via OLVT / AZ Sint-Blasius VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 235.94m omzet JUMP +5.07pct with pnl DROP -56.78pct; site kerncijfers differ; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon CW vs site bedrijfsopbrengsten; pnl DROP path vs Oostende/Glorieux",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2009 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "OLVT / O.L.Vrouw van Troost (AZ Sint-Blasius)",
    "name_fr": "OLVT / O.L.Vrouw van Troost (AZ Sint-Blasius)",
    "name_en": "OLVT / AZ Sint-Blasius Dendermonde",
    "level": "asbl",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://www.azsintblasius.be/",
    "foi_email": "info@azsintblasius.be",
    "foi_postal": "Kroonveldlaan 50, 9200 Dendermonde",
    "notes": "tick2009 YE2025 Medium CW NL+EN+FR + Strong KBO 0411.975.133 Actief VZW; omzet JUMP 235.94m pnl DROP 1.99m equity JUMP 82.63m bruto JUMP 102.39m FTE 1120; assets/debt Unknown; neerlegging 16.06.2026; 3 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Zottegem/Turnhout/Waregem/Yperman CW N/A; do not redo AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "OostVlaanderen>OLVT_Sint_Blasius>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); recon CW omzet vs site bedrijfsopbrengsten; pnl DROP recon",
    "why_it_matters": "Medium CW shows 235.94m omzet Dendermonde hospital VZW with pnl DROP -57pct; site kerncijfers differ (opbrengsten 246.96m)",
    "priority": "7",
    "recipient_body": "OLVT / O.L.Vrouw van Troost VZW (AZ Sint-Blasius)",
    "recipient_email": "info@azsintblasius.be",
    "recipient_postal": "Kroonveldlaan 50, 9200 Dendermonde",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_olvt_sint_blasius_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_olvt_sint_blasius_omzet_jump_235_94m_pnl_drop_1_99m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2009; human-send only; Medium CW; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — OLVT / AZ Sint-Blasius (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** OLVT / O.L.Vrouw van Troost VZW (AZ Sint-Blasius) — KBO **0411.975.133**  
**recipient:** info@azsintblasius.be · Kroonveldlaan 50, 9200 Dendermonde  
**sources:** [CW NL](https://www.companyweb.be/nl/0411975133) · [CW EN](https://www.companyweb.be/en/0411975133) · [CW FR](https://www.companyweb.be/fr/0411975133) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411975133) · [kerncijfers](https://www.azsintblasius.be/over-ons/beleid/kerncijfers)  
**tick:** 2009  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; site figures differ)

## Context
- YE **2025** (neerlegging **16.06.2026**): CW omzet **EUR235,942,746** JUMP +5.07%; pnl **EUR1,990,218** DROP −56.78%; equity **EUR82,628,815** JUMP +1.41%; bruto **EUR102,389,176** JUMP +6.08%; FTE **1120**; assets/debt **Unknown**.
- Site kerncijfers: bedrijfsopbrengsten **EUR246,957,758**; netto **EUR2,242,668** (differ from CW).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Zottegem/Turnhout/Waregem/Yperman CW N/A omzet. AZ Oostende already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: OLVT / O.L.Vrouw van Troost VZW (AZ Sint-Blasius) — Kroonveldlaan 50, 9200 Dendermonde
info@azsintblasius.be
cc: Agentschap Zorg en Gezondheid / Provincie Oost-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 OLVT + balans (KBO 0411.975.133)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 16.06.2026).
2. Assets / schulden LT-ST / cash.
3. Recon CW omzet EUR235.942.746 vs site bedrijfsopbrengsten EUR246.957.758.
4. Recon pnl DROP (EUR1.990.218 vs YE2024 EUR4.604.650; −56,78pct) vs site netto EUR2.242.668.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2009":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AZ Oostende — OLVT/AZ Sint-Blasius YE2025 Medium"
        x["notes"] = (
            "tick2009 OLVT/AZ Sint-Blasius Medium omzet JUMP 235.94m pnl DROP 1.99m equity JUMP 82.63m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Zottegem/Turnhout/Waregem/Yperman CW N/A; next rq_2010 EVERY-10; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover OLVT/AZ Sint-Blasius YE2025 Medium CW; KBO 0411.975.133; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2010" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2010",
            "title": "EVERY-10 + leftover dual hole-fill after OLVT/AZ Sint-Blasius",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2009 after OLVT/AZ Sint-Blasius YE2025 Medium. MANDATORY EVERY-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Vlaamse Zorgkas YE2025 live / Jan Yperman if omzet appears / Vesalius / Heilig Hart Lier / Sint-Jan Brugge / other unused YE2025 if live). "
                "Do NOT redo OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2009 OLVT; EVERY-10 due at 2010; AGB/FARO/AIESH/REW still YE2024; Vlaamse Zorgkas YE2025 live deferred",
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
        "last_unit_id": "rq_2009",
        "ticks_completed": "2009",
        "paused": "no",
        "notes": (
            "tick2009 leftover OLVT/AZ Sint-Blasius 0411.975.133 Medium CW (omzet JUMP 235.94m pnl DROP 1.99m equity JUMP 82.63m bruto JUMP 102.39m FTE 1120; "
            "assets/debt Unknown; site opbrengsten differ); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2010 EVERY-10; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2009 - {UTC} - rq_2009 OLVT/AZ Sint-Blasius (omzet JUMP 235.94m / pnl DROP 1.99m / Medium)

- Unit: **rq_2009** leftover dual after **rq_2008 AZ Oostende**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Zottegem/Turnhout/Waregem/Yperman CW **N/A omzet**. Took preferred leftover **OLVT / AZ Sint-Blasius** YE2025 (KBO **0411.975.133**; Kroonveldlaan 50 Dendermonde; Oost-Vlaanderen **hospital VZW**). Vlaamse Zorgkas YE2025 also live deferred. Do not redo AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR235,942,746** JUMP +5.07%; pnl **EUR1,990,218** DROP −56.78%; equity **EUR82,628,815** JUMP +1.41%; bruto **EUR102,389,176** JUMP +6.08%; FTE **1120**; neerlegging **16.06.2026**. Site kerncijfers bedrijfsopbrengsten **EUR246,957,758** / netto **EUR2,242,668** (differ). Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 3 VE; email info@azsintblasius.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_olvt_sint_blasius); foi + draft {GAP}; rq_2009=done + rq_2010 open (EVERY-10); loop_state ticks=2009; raw under docs/doge/data/raw/tick2009/.
- FOI: **ready not sent** (human-gated; info@azsintblasius.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2010 (EVERY-10 + AGB/FARO-if-YE2025 / AIESH-REW / Vlaamse Zorgkas / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")

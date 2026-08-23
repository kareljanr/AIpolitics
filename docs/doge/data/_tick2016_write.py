# ephemeral tick2016 — AZ Zeno YE2025 Medium (leftover dual after Heilig Hart Tienen)
# CW year-label shows anomalous 2008; neerlegging 02.07.2026 + 2-year matrix treated as YE2025/YE2024
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T08:25:00Z"
ENTITY = "vzw_az_zeno"
GAP = "gap_az_zeno_nbb_pdf_assets_debt_year_label_matrix_l5"
SRC = "src_az_zeno_jr2025_cw"
SRC_EN = "src_az_zeno_jr2025_cw_en"
SRC_FR = "src_az_zeno_jr2025_cw_fr"
SRC_KBO = "src_az_zeno_kbo_2016"
SRC_SITE = "src_az_zeno_site_2016"

OMZET = "64650772"
PNL = "6176929"
EQUITY = "51316660"
BRUTO = "37489915"
FTE = "579.5"
OMZET24 = "59430716"
PNL24 = "1248572"
EQUITY24 = "44990551"
BRUTO24 = "33803854"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2016")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZ Zeno YE2025 statutory (year-label anomaly)",
        "url": "https://www.companyweb.be/nl/0410123819/az-zeno",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2016; CW Laatste balansjaar shows anomalous 2008 but neerlegging 02.07.2026; treat latest as YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; raw docs/doge/data/raw/tick2016/azzeno_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZ Zeno YE2025 statutory (year-label anomaly)",
        "url": "https://www.companyweb.be/en/0410123819/az-zeno",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2016; EN mirror; Last balance sheet year shows anomalous 2008; filed 02-07-2026; treated YE2025 Medium; raw docs/doge/data/raw/tick2016/azzeno_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZ Zeno YE2025 statutory (year-label anomaly)",
        "url": "https://www.companyweb.be/fr/0410123819/az-zeno",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2016; FR mirror; deposés le 02-07-2026; treated YE2025 Medium; raw docs/doge/data/raw/tick2016/azzeno_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZ ZENO 0410.123.819 Actief VZW Knokke-Heist",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410123819",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2016; Actief VZW since 28.06.1967; Kalvekeetdijk 260 8300 Knokke-Heist; no KBO email; 3 VE",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azzeno.be AZ Zeno",
        "url": "https://www.azzeno.be/",
        "publisher": "AZ Zeno",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2016; info@azzeno.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_az_zeno_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW latest column treated YE2025 omzet (year-label anomaly)",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2016; omzet JUMP {OMZET} +8.78pct vs prior {OMZET24}; CW year-label 2008 anomalous",
    },
    {
        "budget_id": "bud_az_zeno_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW latest Profit/Loss treated YE2025",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2016; pnl JUMP {PNL} +394.72pct vs prior {PNL24}",
    },
    {
        "budget_id": "bud_az_zeno_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW latest Eigen vermogen treated YE2025",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2016; equity JUMP {EQUITY} +14.06pct vs prior {EQUITY24}",
    },
    {
        "budget_id": "bud_az_zeno_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW latest Brutomarge treated YE2025",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2016; bruto JUMP {BRUTO} +10.90pct vs prior {BRUTO24}",
    },
    {
        "budget_id": "bud_az_zeno_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2016; FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_az_zeno_jr2025_statutory_hospital",
    "title": "AZ Zeno YE2025 leftover hospital dual (omzet JUMP 64.65m / pnl JUMP 6.18m / equity JUMP 51.32m; year-label anomaly)",
    "entity_id": ENTITY,
    "beneficiary": "Knokke-Heist-region hospital patients / AZ Zeno",
    "legal_basis": "VZW/ASBL hospital (KBO 0410.123.819)",
    "decision_date": "2026-07-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0410123819/az-zeno",
    "stated_goal": "Regional hospital care (Knokke-Heist)",
    "cut_option": "Publish NBB PDF + confirm fiscal year FOI (CW year-label anomaly)",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>AZ_Zeno>JR2025_statutory_L5",
    "notes": "tick2016; Medium CW; CW year-label shows 2008 anomalous; treated YE2025 via neerlegging 02.07.2026; preferred AGB/FARO/AIESH/REW YE2024; Klina N/A omzet; HH Tienen already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_az_zeno_omzet_jump_64_65m_pnl_jump_6_18m_equity_jump_jr2025",
    "name": "AZ Zeno omzet JUMP 64.65m / pnl JUMP 6.18m / equity JUMP 51.32m (YE2025; CW year-label anomaly)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "WestVlaanderen>AZ_Zeno>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; CW year-label 2008 anomalous; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Knokke-Heist patients via AZ Zeno VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW treated YE2025; 64.65m omzet JUMP +8.78pct with pnl JUMP +395pct; CW year-label anomaly FOI residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF + confirm boekjaar FOI; recon pnl JUMP path",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2016 leftover dual; Medium CW year-label anomaly; TE-adjacent hospital flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZ Zeno",
    "name_fr": "AZ Zeno",
    "name_en": "AZ Zeno (Knokke-Heist hospital)",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.azzeno.be/",
    "foi_email": "info@azzeno.be",
    "foi_postal": "Kalvekeetdijk 260, 8300 Knokke-Heist",
    "notes": (
        "tick2016 YE2025 Medium CW NL+EN+FR (year-label anomaly 2008) + Strong KBO 0410.123.819 Actief VZW; "
        "omzet JUMP 64.65m pnl JUMP 6.18m equity JUMP 51.32m bruto JUMP 37.49m FTE 579.5; assets/debt Unknown; "
        "neerlegging 02.07.2026; 3 VE; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Klina CW N/A omzet; do not redo Heilig Hart Tienen/"
        "Heilig Hart Leuven/Sint-Trudo/Sint-Andries Tielt/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/"
        "Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/"
        "CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC"
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
    "hierarchy_path": "WestVlaanderen>AZ_Zeno>NBB_PDF_assets_debt_year_label",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening (confirm boekjaar YE2025 vs CW year-label 2008); assets/debt LT-ST/cash",
    "why_it_matters": "Medium CW shows 64.65m omzet Knokke hospital with pnl JUMP +395pct but Laatste balansjaar label stuck at 2008 despite filing 02.07.2026",
    "priority": "7",
    "recipient_body": "AZ Zeno vzw",
    "recipient_email": "info@azzeno.be",
    "recipient_postal": "Kalvekeetdijk 260, 8300 Knokke-Heist",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_az_zeno_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_az_zeno_omzet_jump_64_65m_pnl_jump_6_18m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2016; human-send only; Medium CW year-label anomaly; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZ Zeno (NBB PDF / assets-debt / year-label)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** AZ Zeno vzw — KBO **0410.123.819**  
**recipient:** info@azzeno.be · Kalvekeetdijk 260, 8300 Knokke-Heist  
**sources:** [CW NL](https://www.companyweb.be/nl/0410123819/az-zeno) · [CW EN](https://www.companyweb.be/en/0410123819/az-zeno) · [CW FR](https://www.companyweb.be/fr/0410123819/az-zeno) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410123819) · [site](https://www.azzeno.be/)  
**tick:** 2016  
**confidence:** Medium (CW NL+EN+FR; CW year-label anomaly; assets/debt Unknown)

## Context
- CW shows **Laatste balansjaar / Last balance sheet year = 2008** (anomalous) but **neerlegging 02.07.2026**.
- Treated as YE **2025** (latest column): omzet **EUR64,650,772** JUMP +8.78%; pnl **EUR6,176,929** JUMP +394.72%; equity **EUR51,316,660** JUMP +14.06%; bruto **EUR37,489,915** JUMP +10.90%; FTE **579.5**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. Klina filed but CW N/A omzet. Heilig Hart Tienen already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: AZ Zeno vzw — Kalvekeetdijk 260, 8300 Knokke-Heist
info@azzeno.be
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening + bevestiging boekjaar (KBO 0410.123.819)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF van de meest recente jaarrekening (neerlegging 02.07.2026) met expliciete boekjaar-einddatum.
2. Bevestiging of dit YE2025 betreft (Companyweb toont anomalisch '2008' als laatste balansjaar).
3. Assets / schulden LT-ST / cash.
4. Toelichting PnL-stijging van EUR1.248.572 (prior) naar EUR6.176.929 (latest).
Periode van de neergelegde jaarrekening. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2016":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Heilig Hart Tienen — AZ Zeno YE2025 Medium (year-label anomaly)"
        x["notes"] = (
            "tick2016 AZ Zeno Medium omzet JUMP 64.65m pnl JUMP 6.18m equity JUMP 51.32m; CW year-label 2008 anomalous; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Klina N/A omzet; next rq_2017; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover AZ Zeno treated YE2025 Medium CW (year-label anomaly); KBO 0410.123.819; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2017" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2017",
            "title": "leftover dual hole-fill after AZ Zeno",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2016 after AZ Zeno YE2025 Medium (CW year-label anomaly). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Jessa / ZOL / Vesalius if omzet / other unused YE2025 if live with omzet). "
                "Do NOT redo AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2016 AZ Zeno; next every-10 2020; Klina N/A omzet",
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
        "last_unit_id": "rq_2016",
        "ticks_completed": "2016",
        "paused": "no",
        "notes": (
            "tick2016 leftover AZ Zeno 0410.123.819 Medium CW (omzet JUMP 64.65m pnl JUMP 6.18m equity JUMP 51.32m bruto JUMP 37.49m FTE 579.5; "
            "CW year-label 2008 anomalous; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Klina N/A omzet; next rq_2017; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2016 - {UTC} - rq_2016 AZ Zeno (omzet JUMP 64.65m / pnl JUMP 6.18m / Medium; year-label anomaly)

- Unit: **rq_2016** leftover dual after **rq_2015 Heilig Hart Tienen**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Klina filed **30.06.2026** but CW **N/A omzet**. Took deferred leftover **AZ Zeno** (KBO **0410.123.819**; Kalvekeetdijk 260 Knokke-Heist) — CW year-label anomalously shows **2008**, but neerlegging **02.07.2026**; treated latest column as **YE2025** Medium. Do not redo Heilig Hart Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR - omzet **EUR64,650,772** JUMP +8.78%; pnl **EUR6,176,929** JUMP +394.72%; equity **EUR51,316,660** JUMP +14.06%; bruto **EUR37,489,915** JUMP +10.90%; FTE **579.5**; neerlegging **02.07.2026**. Assets/debt Unknown. Medium confidence (year-label anomaly). Strong KBO Actief VZW 3 VE; email info@azzeno.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_az_zeno); foi + draft {GAP}; rq_2016=done + rq_2017 open; loop_state ticks=2016; raw under docs/doge/data/raw/tick2016/.
- FOI: **ready not sent** (human-gated; info@azzeno.be) — also asks boekjaar confirmation.
- NOT every-10 (**next every-10 is 2020**). Next: rq_2017 (AGB/FARO-if-YE2025 / AIESH-REW / Jessa-ZOL / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")

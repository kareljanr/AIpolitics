# ephemeral tick1982 — SPI Liège YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-23T23:15:00Z"
ENTITY = "igs_spi"
GAP = "gap_spi_nbb_pdf_assets_debt_bruto_collapse_sowafinal_matrix_l5"
SRC = "src_spi_jr2025_cw"
SRC_EN = "src_spi_jr2025_cw_en"
SRC_KBO = "src_spi_kbo_1982"
SRC_SITE = "src_spi_site_1982"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1982")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL SPI YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0204259135/spi",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1982; YE2025 omzet DROP 20760649 pnl LOSS -289708 equity JUMP 221420326 bruto DROP 177083 FTE 105.2; neerlegging 07.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1982/spi_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN SPI YE2025 statutory",
        "url": "https://www.companyweb.be/en/0204259135/spi",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1982; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1982/spi_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO SPI 0204.259.135 Actief CV Liege",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0204259135",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": "tick1982; Actief CV; Rue du Vertbois 11 4000 Liege Atrium Vertbois; email officiel.ic-spi@spi.be; Aanbestedende overheid; ADT Liege",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "spi.be Liege territorial development ADT",
        "url": "https://www.spi.be/",
        "publisher": "SPI",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": "tick1982; Liege ADT / ZAE / SOWAFINAL dual residual",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_spi_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "20760649",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1982; omzet DROP 20760649 -23.22pct vs YE2024 27040503",
    },
    {
        "budget_id": "bud_spi_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "-289708",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss NEG",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1982; pnl LOSS -289708 deepening -278.61pct vs YE2024 -76518",
    },
    {
        "budget_id": "bud_spi_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "221420326",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1982; equity JUMP 221420326 +7.25pct vs YE2024 206449517",
    },
    {
        "budget_id": "bud_spi_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "177083",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1982; bruto DROP 177083 -97.14pct vs YE2024 6183042",
    },
    {
        "budget_id": "bud_spi_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "105.2",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1982; YE2025 FTE 105.2 vs YE2024 105",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_spi_jr2025_statutory_adt",
    "title": "SPI YE2025 leftover Liege ADT dual (omzet DROP 20.76m / bruto DROP 0.177m / pnl LOSS 0.290m)",
    "entity_id": ENTITY,
    "beneficiary": "Liege province communes + ZAE / SOWAFINAL dual",
    "legal_basis": "Code democratie locale intercommunale developpement economique CV",
    "decision_date": "2026-07-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "20760649",
    "cash_by_year": '{"2025_omzet":20760649,"2025_pnl":-289708,"2025_equity":221420326,"2025_bruto":177083,"2025_fte":105.2}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0204259135/spi",
    "stated_goal": "Liege territorial economic development ADT / ZAE parks",
    "cut_option": "Publish NBB PDF assets/debt + bruto collapse recon + SOWAFINAL dual FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Liege>SPI>JR2025_statutory_L5",
    "notes": "tick1982; Medium CW; assets/debt Unknown; bruto -97pct collapse; preferred AGB Bornem JR2024; FARO/AIESH/REW/IDETA YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_spi_omzet_drop_20_76m_bruto_collapse_0_177m_pnl_loss_jr2025",
    "name": "SPI omzet DROP 20.76m / bruto collapse 0.177m / pnl LOSS 0.290m / equity JUMP 221.42m (Liege ADT YE2025)",
    "level": "L5",
    "type": "walloon_igs_adt_dual",
    "hierarchy_path": "Wallonie>Liege>SPI>JR2025_statutory_L5",
    "annual_cost_eur": "20760649",
    "total_cost_eur": "221420326",
    "tco_notes": "statutory omzet DROP 20760649 pnl LOSS -289708 equity JUMP 221420326 bruto DROP 177083 FTE 105.2; assets/debt Unknown; bruto -97pct",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Liege communes via ADT / ZAE financing shell",
    "stated_goal": "Territorial economic development and industrial parks",
    "measured_outcome": "Medium CW YE2025; 221m equity with deepening LOSS and bruto collapse; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "3.5",
    "priority_index": "5.2",
    "cut_proposal": "Publish NBB PDF + bruto collapse / SOWAFINAL dual FOI; scrutinise equity JUMP with LOSS deepening",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1982 leftover dual; Medium CW; not TE-additive pure-waste top10; next every-10 1990",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "SPI (Liege ADT / developpement economique)",
    "name_fr": "SPI (ADT Liege / developpement economique)",
    "name_en": "SPI (Liege territorial development ADT IGS)",
    "level": "intercommunale",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.spi.be/",
    "foi_email": "officiel.ic-spi@spi.be",
    "foi_postal": "Rue du Vertbois 11, 4000 Liege (Atrium Vertbois)",
    "notes": "tick1982 YE2025 Medium CW NL+EN + Strong KBO 0204.259.135 Actief CV; omzet DROP 20.76m pnl LOSS 0.290m equity JUMP 221.42m bruto DROP 0.177m (-97pct) FTE 105.2; assets/debt Unknown; neerlegging 07.07.2026; FOI gap_spi_nbb_pdf_assets_debt_bruto_collapse_sowafinal_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW/IDETA YE2024; do not redo Vivalia/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IGRETEC/HELORA",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Liege>SPI>NBB_PDF_assets_debt_bruto_sowafinal",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); bruto collapse -97pct recon; SOWAFINAL dual debt attribution; ZAE sales matrix",
    "why_it_matters": "Medium CW shows 221m equity ADT with deepening LOSS and bruto collapse without balance sheet; SOWAFINAL dual opacity",
    "priority": "6",
    "recipient_body": "SPI",
    "recipient_email": "officiel.ic-spi@spi.be",
    "recipient_postal": "https://www.spi.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "linked_commitment_id": "comm_spi_jr2025_statutory_adt",
    "linked_leaderboard_id": "lb_spi_omzet_drop_20_76m_bruto_collapse_0_177m_pnl_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1982; human-send only; Medium CW; next every-10 1990",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — SPI (NBB PDF / assets-debt / bruto collapse / SOWAFINAL)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** SPI CV — KBO **0204.259.135**  
**recipient:** officiel.ic-spi@spi.be  
**sources:** [CW NL](https://www.companyweb.be/nl/0204259135/spi) · [CW EN](https://www.companyweb.be/en/0204259135/spi) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0204259135) · [site](https://www.spi.be/)  
**tick:** 1982  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **07.07.2026**): omzet **EUR20,760,649** DROP -23.22%; pnl **NEG EUR-289,708** (deepening); equity **EUR221,420,326** JUMP +7.25%; bruto **EUR177,083** DROP -97.14%; FTE **105.2**; assets/debt **Unknown**.
- Liege ADT / ZAE intercommunale. Preferred stall: AGB Bornem / FARO / AIESH / REW / IDETA still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: SPI — officiel.ic-spi@spi.be
Rue du Vertbois 11, 4000 Liege
cc: SPW economie / Province Liege transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 SPI + balans + bruto/SOWAFINAL recon (KBO 0204.259.135)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 07.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon bruto DROP (-97pct vs YE2024 6.18m).
4. SOWAFINAL dual debt attribution 2025.
5. ZAE sales / terrain matrix indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1982":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Vivalia — SPI YE2025 Medium"
        x["notes"] = "tick1982 SPI Medium omzet DROP 20.76m bruto collapse 0.177m pnl LOSS 0.290m; FOI ready; next rq_1983; next every-10 1990"
        x["instructions"] = (
            "Completed leftover SPI Liege ADT YE2025 Medium CW; KBO 0204.259.135; "
            "omzet DROP 20760649 pnl LOSS -289708 equity JUMP 221420326 bruto DROP 177083 FTE 105.2; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1983" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1983",
            "title": "leftover dual hole-fill after SPI",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1982 after SPI YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/ADT (IDETA if YE2025 / other). Do NOT redo SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1982 SPI; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1982",
        "ticks_completed": "1982",
        "paused": "no",
        "notes": "tick1982 leftover SPI 0204.259.135 Medium CW (omzet DROP 20.76m pnl LOSS 0.290m equity JUMP 221.42m bruto DROP 0.177m -97pct FTE 105.2; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW/IDETA YE2024; next rq_1983; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1982 - 2026-08-23T23:15:00Z - rq_1982 SPI (omzet DROP 20.76m / bruto collapse 0.177m / pnl LOSS / Medium)

- Unit: **rq_1982** leftover dual after **rq_1981 Vivalia**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW/IDETA still **YE2024**. Took unused leftover **SPI** YE2025 (KBO **0204.259.135**; Rue du Vertbois 11 Liege; Liege **ADT**). Do not redo Vivalia/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/HELORA/BEP*/IBH/IGRETEC/IPFBW.
- Found: Companyweb NL+EN YE2025 - omzet **EUR20,760,649** DROP -23.22%; pnl **NEG EUR-289,708** (deepening); equity **EUR221,420,326** JUMP +7.25%; bruto **EUR177,083** DROP -97.14%; FTE **105.2**; neerlegging **07.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV; email officiel.ic-spi@spi.be.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igs_spi); foi + draft gap_spi_nbb_pdf_assets_debt_bruto_collapse_sowafinal_matrix_l5; rq_1982=done + rq_1983 open; loop_state ticks=1982.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1983 (AGB/FARO-if-YE2025 / AIESH-REW / IDETA / unused DSO-IGS-HVZ).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1982" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1982")

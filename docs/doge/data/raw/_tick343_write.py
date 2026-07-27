# tick 343 — Federal Tax Shelter AV TE dual culture (FPS inventory)
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T10:15:00Z"

with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_fps_taxex_inventory_2026,FPS Finance Inventory of Federal Tax Expenditures 2024 edition tax shelter AV,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/Inventory_federal_tax_expenditures_2026.pdf,"
        "FPS Finance,2026-07-31,official_inventory,"
        "Strong: Tax shelter audiovisual Art.194ter CIT EUR m 2004-2023 series end 204.38/212.15 2022-23; "
        "scenic 41.82 2023; games 1.33 2023; dual VAF CCA culture; tick343\n"
    )

with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "tax_shelter_av,Tax Shelter audiovisual federal CIT exemption,"
        "Tax Shelter audiovisuel federal,"
        "Federal corporate tax shelter for audiovisual performing arts and video games Art.194ter,"
        "taxex,fod_finance,bi,https://finance.belgium.be/en/enterprises/corporation-tax/tax-benefits/tax-shelter-audiovisuel-production,,,,"
        "FPS TE AV 212.15m 2023; dual VAF CCA Wallimage Screen Flanders; tick343\n"
    )

# years 2004-2023 series for AV tax shelter (mEUR)
av_series = {
    2004: 5.62, 2005: 10.0, 2006: 13.29, 2007: 33.2, 2008: 31.41,
    2009: 31.59, 2010: 20.11, 2011: 38.1, 2012: 55.78, 2013: 5.39,
    2014: 7.44, 2015: 191.41, 2016: 154.35, 2017: 170.23, 2018: 166.9,
    2019: 174.12, 2020: 173.36, 2021: 183.73, 2022: 204.38, 2023: 212.15,
}
# scenic 2016-2023 (8 values)
scenic = {2016: 3.16, 2017: 10.87, 2018: 16.67, 2019: 24.45, 2020: 23.05, 2021: 22.31, 2022: 21.88, 2023: 41.82}
# games 2022-2023
games = {2022: 0.2, 2023: 1.33}

bud = []
for y, m in av_series.items():
    eur = int(round(m * 1_000_000))
    conf = "strong"
    bud.append(
        f"bud_taxshelter_av_{y},tax_shelter_av,{y},{eur},,,taxex,src_fps_taxex_inventory_2026,{conf},"
        f"FPS inventory CIT Tax shelter audiovisual work Art.194ter {m}m EUR"
    )
for y, m in scenic.items():
    eur = int(round(m * 1_000_000))
    bud.append(
        f"bud_taxshelter_scenic_{y},tax_shelter_av,{y},{eur},,,taxex,src_fps_taxex_inventory_2026,strong,"
        f"FPS inventory Tax shelter scenic/performing arts Art.194ter {m}m EUR"
    )
for y, m in games.items():
    eur = int(round(m * 1_000_000))
    bud.append(
        f"bud_taxshelter_games_{y},tax_shelter_av,{y},{eur},,,taxex,src_fps_taxex_inventory_2026,strong,"
        f"FPS inventory Tax shelter video games Art.194ter {m}m EUR"
    )
# package 2023
pack_2023 = int(round((212.15 + 41.82 + 1.33) * 1_000_000))
bud.append(
    f"bud_taxshelter_pack_2023,tax_shelter_av,2023,{pack_2023},,,taxex,src_fps_taxex_inventory_2026,strong,"
    "FPS inventory Tax shelter package AV+scenic+games 212.15+41.82+1.33=255.3m EUR 2023"
)
with open(root / "budgets.csv", "a", encoding="utf-8") as f:
    f.write("\n".join(bud) + "\n")

# tax_expenditures.csv
tx_path = root / "tax_expenditures.csv"
with open(tx_path, "a", encoding="utf-8") as f:
    f.write(
        "tx_taxshelter_av_2023,Tax shelter audiovisual work CIT Art.194ter,federal,2023,212150000,CIT,"
        "src_fps_taxex_inventory_2026,strong,5,"
        "\"FPS inventory 212.15m 2023; dual culture VAF/CCA; reform jump 2015; not pure waste industrial policy\"\n"
    )
    f.write(
        "tx_taxshelter_scenic_2023,Tax shelter scenic performing arts CIT Art.194ter,federal,2023,41820000,CIT,"
        "src_fps_taxex_inventory_2026,strong,4,"
        "\"FPS inventory 41.82m 2023; extension performing arts\"\n"
    )
    f.write(
        "tx_taxshelter_games_2023,Tax shelter video games CIT Art.194ter,federal,2023,1330000,CIT,"
        "src_fps_taxex_inventory_2026,strong,4,"
        "\"FPS inventory 1.33m 2023; gaming extension from 2023\"\n"
    )
    f.write(
        "tx_taxshelter_pack_2023,Tax shelter package AV scenic games CIT,federal,2023,255300000,CIT,"
        "src_fps_taxex_inventory_2026,strong,5,"
        "\"Sum AV 212.15 + scenic 41.82 + games 1.33 = 255.3m 2023 FPS inventory\"\n"
    )


def cmt(cid, title, eid, ben, legal, ddate, sy, ey, tot, cash, rem, url, goal, cut, src, conf, path, notes):
    cf = json.dumps(cash, separators=(",", ":")).replace('"', '""')
    rem_s = "" if rem is None else str(rem)
    return (
        f'{cid},{title},{eid},{ben},{legal},{ddate},{sy},{ey},{tot},'
        f'"{cf}",{rem_s},active,{url},{goal},{cut},{src},{conf},{path},{notes}\n'
    )


cash_by_year = {str(y): int(round(m * 1_000_000)) for y, m in av_series.items()}
cash_by_year["note"] = (
    "FPS inventory EUR million converted; 2015 reform spike; dual VAF/CCA culture grants; "
    "CCA 2024 raised 84.73m investor cash differs from TE revenue forgone metric"
)
with open(root / "commitments.csv", "a", encoding="utf-8") as f:
    f.write(
        cmt(
            "cmt_taxshelter_av_path_2004_23",
            "Federal Tax Shelter audiovisual CIT multi-year TE dual culture",
            "tax_shelter_av",
            "Belgian producers investors audiovisual sector",
            "ITC Art.194ter tax shelter audiovisual + scenic + games extensions",
            "2004-01-01",
            2004,
            2023,
            212150000,
            {
                "series_m": av_series,
                "scenic_2023_m": 41.82,
                "games_2023_m": 1.33,
                "pack_2023_m": 255.3,
                "cca_raised_2024_m": 84.73,
                "vaf_vl_dots_2024_m": 30.7,
                "cca_envelope_2024_m": 44.0,
                "note": "TE revenue forgone != investment raised; dual community cultural funds + regional economic funds",
            },
            None,
            "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/Inventory_federal_tax_expenditures_2026.pdf",
            "Stimulate Belgian audiovisual production via corporate tax incentive",
            "Audit additionality; dual VAF CCA transparency; FOI L5 beneficiaries concentration",
            "src_fps_taxex_inventory_2026",
            "strong",
            "Federal>taxex>TaxShelter_AV",
            "tick343: 212m AV TE 2023 dual culture AV stack",
        )
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_taxshelter_av_212m,Federal Tax Shelter audiovisual CIT TE 212m 2023 dual culture,federal,tax_expenditure,"
        "Federal>taxex>TaxShelter_AV,212150000,212150000,"
        "Strong FPS inventory: AV shelter 212.15m 2023 (204.38 2022); package+scenic+games 255.3m; dual VAF CCA,"
        "strong,src_fps_taxex_inventory_2026,AV producers corporate investors,"
        "Stimulate Belgian film TV production industrial culture,"
        "Off pure TE waste if additionality real; dual community grants separate; large fiscal cost,"
        "5,8.0,6,6.65,Publish concentration top producers; audit deadweight; dual VAF CCA map,seed,,tick343 dual culture TE\n"
    )
    f.write(
        "lb_taxshelter_pack_255m,Tax Shelter package AV scenic games 255m 2023,federal,tax_expenditure,"
        "Federal>taxex>TaxShelter_pack,255300000,255300000,"
        "Strong FPS: AV 212.15 + scenic 41.82 + games 1.33 = 255.3m 2023,"
        "strong,src_fps_taxex_inventory_2026,Creative industries investors,"
        "Federal creative industries tax incentive package,"
        "Culture industrial policy; dual regional funds; games extension small,"
        "4,8.0,6,6.3,Track multi-year path post-2023 inventory update,seed,,tick343\n"
    )

with open(root / "foi_queue.csv", "a", encoding="utf-8") as f:
    f.write(
        "gap_taxshelter_l5_beneficiaries,Federal>taxex>TaxShelter>L5_producers,tax_shelter_av,"
        "Top50 Tax Shelter framework contracts certificates by producer intermediary EUR 2022-2025; "
        "reconcile FPS TE 212m with CCA raised 84.73m and Flanders raised totals; games and scenic L5,"
        "Aggregates strong FPS inventory; end-receiver concentration opacity,6,"
        "FOD Financien Tax Shelter cel / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_taxshelter_l5_beneficiaries.md,ready,2026-07-31,,,,,"
        f"cmt_taxshelter_av_path_2004_23,lb_taxshelter_av_212m,{now},{now},"
        "tick343 draft ready human send; dual VAF CCA culture stack\n"
    )

draft = root.parent / "foi" / "drafts" / "gap_taxshelter_l5_beneficiaries.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    """# FOI draft — gap_taxshelter_l5_beneficiaries

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: FOD Financiën — Tax Shelter cel
via https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — Tax Shelter L5 begunstigden

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik:

1. Top-50 (of volledige geaggregeerde) lijst van Tax Shelter-raamovereenkomsten /
   certificaten 2022-2025 met: productiemaatschappij, intermediair, bedrag, werktype
   (AV / podium / games), regio indien bekend.
2. Jaarreeksen die de FPS-inventaris TE (AV **€212,15 m** 2023) verbinden met de
   door CCA/FWB gerapporteerde **opgehaalde** investeringen (**€84,73 m** 2024).
3. Aandeel games en podiumkunsten in de recente certificaten.

Publiek: Inventaris federale fiscale uitgaven 2024 (editie 2026) Art. 194ter;
CCA Bilan 2024 tax shelter raised; VAF/CCA culture dual.

Dossierreferentie intern: gap_taxshelter_l5_beneficiaries

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] FOD Financiën Tax Shelter
- [x] Concrete L5 + recon metrics
- [x] foi_queue ready
- [ ] Human send
""",
    encoding="utf-8",
)

# research queue seed rq_334
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
if "rq_334" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_334,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_taxshelter_l5_beneficiaries,"
        f"2026-07-31T09:45:00Z,{now},"
        "tick343: Tax Shelter AV TE 212m 2023 FPS dual VAF/CCA culture; FOI L5; spawn rq_335\n"
    )
else:
    rq = re.sub(
        r"rq_334,[^\n]+",
        "rq_334,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_taxshelter_l5_beneficiaries,"
        f"2026-07-31T09:45:00Z,{now},"
        "tick343: Tax Shelter AV TE 212m 2023 FPS dual VAF/CCA culture; FOI L5; spawn rq_335",
        rq,
        count=1,
    )
if "rq_335" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_335,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        f"{now},,Spawned tick343 after Tax Shelter TE dual culture; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_334,343,no,"
    "Scheduler 60s. Next prio5 rq_335; rq_116 SWA deferred. FOI ready. tick343 TaxShelter AV 212m.\n",
    encoding="utf-8",
)

print("OK tick343 pack", pack_2023)

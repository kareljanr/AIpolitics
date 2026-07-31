# -*- coding: utf-8 -*-
"""Tick 146: rq_136 VRT BHO full cash-by-year + side envelopes."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T22:10:00Z"
TICK = 146
UNIT = "rq_136"


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1"), "latin-1"


def write_text(path: Path, text: str, enc: str) -> None:
    path.write_bytes(text.encode(enc, errors="replace"))


def append_lines(path: Path, lines: list[str]) -> None:
    text, enc = read_text(path)
    if not text.endswith("\n"):
        text += "\n"
    write_text(path, text + "\n".join(lines) + "\n", enc)


append_lines(DATA / "sources.csv", [
    'src_vl_vrt_basistoelage_pq130,VP schriftelijke vraag 130 Van Achter VRT basistoelage 2025-2026 rebuild,https://docs.vlaamsparlement.be/pfile?id=2215524,Vlaams Parlement,2026-07-27,parliament,"Basistoelage 2025 258393k; 2026 296400k; components wage index +36340 partial ops +1489 MAX rights +104 energy -276 digital training +200 NL-BE coop +150"',
    'src_vrt_jv2023_pillars,VRT Jaarverslag 2023 financieringspijlers + overheidsfinanciering split,https://www.mediaspecs.be/wp-content/uploads/2024/06/vrt-jaarverslag-2023.pdf,VRT,2026-07-27,annual_report,"2023 gov 297.9m (basisdot 287.2 inflation 7.1 transform 1.1 other 2.5); eigen 199.7; total 497.6; BAN+comm 81.0; deferred sport -4.3 nieuwbouw -8.6; net PSO cost 291.7 subsidies 285.0"',
    'src_vrt_jv2024_summary,VRT Jaarverslag 2024 overheidsfinanciering + eigen inkomsten,https://www.vrt.be/nl/assets/files/2025-06/Jaarverslag-2024.pdf,VRT,2026-07-27,annual_report,"2024 overheidsfinanciering 304.4m (59.9pct); eigen inkomsten 203.7m (40.1pct); cost per Fleming 3.72 euro/month"',
    'src_vrt_jv2025_fin_html,VRT Jaarverslag 2025 financiele resultaten web,https://jaarverslag.vrt.be/interne-keuken/financiele-resultaten,VRT,2026-07-27,annual_report,"2025 total opbrengsten 528.4m; overheidsfinanciering 306m; eigen 222.3m; commercial+BAN 83m (plafond 90.8); costs 533.1m; external production invest 122.3m; mgmt result -1.6m"',
    'src_radiovisie_vrt_comm_2024,Radiovisie VRT commercial communication + BAN 2024,https://radiovisie.eu/doorgelicht-de-centen-van-vrt-radio-in-2024/,Radiovisie,2026-07-27,secondary,"Commercial communication 74.5m 2024 (+2.7 vs 2023); BAN 10.4m (9.2 in 2023); sum ~84.9m class"',
])

append_lines(DATA / "budgets.csv", [
    # 2022-2023 from JV2023
    "bud_vrt_gov_2022,vrt,2022,290600000,,,outturn,src_vrt_jv2023_pillars,strong,Overheidsfinanciering total 2022",
    "bud_vrt_basisdot_2022,vrt,2022,277500000,,,outturn,src_vrt_jv2023_pillars,strong,Basisdotatie 2022",
    "bud_vrt_eigen_2022,vrt,2022,198900000,,,outturn,src_vrt_jv2023_pillars,strong,Eigen inkomsten 2022",
    "bud_vrt_total_rev_2022,vrt,2022,489500000,,,outturn,src_vrt_jv2023_pillars,strong,Total financing pillars 2022",
    "bud_vrt_gov_2023,vrt,2023,297900000,,,outturn,src_vrt_jv2023_pillars,strong,Overheidsfinanciering total 2023",
    "bud_vrt_basisdot_2023,vrt,2023,287200000,,,outturn,src_vrt_jv2023_pillars,strong,Basisdotatie 2023 (non-indexed base 260.8 + wage index 25.9 + MAX 0.104)",
    "bud_vrt_inflation_dot_2023,vrt,2023,7100000,,,outturn,src_vrt_jv2023_pillars,strong,Eenmalige inflatiekosten dotatie 2023",
    "bud_vrt_transform_dot_2023,vrt,2023,1100000,,,outturn,src_vrt_jv2023_pillars,strong,Herstructurering/transformatieplan 2023 (of 16m 2021-25 package)",
    "bud_vrt_other_subs_2023,vrt,2023,2500000,,,outturn,src_vrt_jv2023_pillars,strong,Overige subsidies 2023",
    "bud_vrt_eigen_2023,vrt,2023,199700000,,,outturn,src_vrt_jv2023_pillars,strong,Eigen inkomsten 2023",
    "bud_vrt_ban_comm_2023,vrt,2023,81000000,,,outturn,src_vrt_jv2023_pillars,strong,BAN + commercial communication 2023",
    "bud_vrt_total_rev_2023,vrt,2023,497600000,,,outturn,src_vrt_jv2023_pillars,strong,Total financing pillars 2023",
    "bud_vrt_net_pso_cost_2023,vrt,2023,291700000,,,outturn,src_vrt_jv2023_pillars,strong,Nettokosten publieke opdracht 2023",
    "bud_vrt_gov_subs_net_2023,vrt,2023,285000000,,,outturn,src_vrt_jv2023_pillars,strong,Overheidssubsidies after deferred for PSO net cost 2023",
    # 2024
    "bud_vrt_gov_2024,vrt,2024,304400000,,,outturn,src_vrt_jv2024_summary,strong,Overheidsfinanciering total 2024 (59.9pct)",
    "bud_vrt_eigen_2024,vrt,2024,203700000,,,outturn,src_vrt_jv2024_summary,strong,Eigen inkomsten 2024 (40.1pct)",
    "bud_vrt_total_rev_2024,vrt,2024,508100000,,,outturn,src_vrt_jv2024_summary,strong,Sum gov+eigen 304.4+203.7",
    "bud_vrt_comm_2024,vrt,2024,74500000,,,outturn,src_radiovisie_vrt_comm_2024,medium,Commercial communication only 2024 secondary Radiovisie citing VRT",
    "bud_vrt_ban_2024,vrt,2024,10400000,,,outturn,src_radiovisie_vrt_comm_2024,medium,BAN 2024 secondary",
    # 2025
    "bud_vrt_total_rev_2025,vrt,2025,528400000,,,outturn,src_vrt_jv2025_fin_html,strong,Totale opbrengsten 2025",
    "bud_vrt_gov_2025,vrt,2025,306000000,,,outturn,src_vrt_jv2025_fin_html,strong,Overheidsfinanciering 2025 (main VL toelage + limited EU/VLAIO etc)",
    "bud_vrt_eigen_2025,vrt,2025,222300000,,,outturn,src_vrt_jv2025_fin_html,strong,Eigen inkomsten 2025",
    "bud_vrt_ban_comm_2025,vrt,2025,83000000,,,outturn,src_vrt_jv2025_fin_html,strong,Commercial+BAN realized 2025 (plafond 90.8m)",
    "bud_vrt_costs_2025,vrt,2025,533100000,,,outturn,src_vrt_jv2025_fin_html,strong,Totale kosten 2025",
    "bud_vrt_ext_prod_2025,vrt,2025,122300000,,,outturn,src_vrt_jv2025_fin_html,strong,External production+facilities invest 2025 (~25pct of income)",
    # basistoelage path
    "bud_vrt_basistoelage_2025,vrt,2025,258393000,,,budgeted,src_vl_vrt_basistoelage_pq130,strong,Basistoelage 2025 component only (not full gov package)",
    "bud_vrt_basistoelage_2026,vrt,2026,296400000,,,budgeted,src_vl_vrt_basistoelage_pq130,strong,Basistoelage 2026 BHO 2026-2030",
])

append_lines(DATA / "commitments.csv", [
    'cmt_vrt_public_package_2022_30,VRT multi-year public financing + basistoelage path dual RTBF,vrt,VRT,Beheersovereenkomst 2021-2025 + BHO 2026-2030 Mediadecreet art.16,2021-01-01,2022,2030,296400000,"{""2022_gov"":290600000,""2022_eigen"":198900000,""2022_total"":489500000,""2023_gov"":297900000,""2023_basisdot"":287200000,""2023_inflation"":7100000,""2023_transform"":1100000,""2023_other_subs"":2500000,""2023_eigen"":199700000,""2023_ban_comm"":81000000,""2023_total"":497600000,""2023_net_pso"":291700000,""2024_gov"":304400000,""2024_eigen"":203700000,""2024_total"":508100000,""2025_gov"":306000000,""2025_eigen"":222300000,""2025_total"":528400000,""2025_ban_comm"":83000000,""2025_plafond_comm"":90800000,""2025_costs"":533100000,""2025_ext_prod"":122300000,""2025_basistoelage"":258393000,""2026_basistoelage"":296400000,""2026_rebuild"":{""wage_index"":36340000,""ops_partial"":1489000,""max_rights"":104000,""energy_eff"":-276000,""digital_training"":200000,""nl_coop"":150000},""bho_2026_30_base_flat_illustrative"":296400000}",0,active,https://jaarverslag.vrt.be/interne-keuken/financiele-resultaten,Public media NL community dual with RTBF,Publish annual side-envelope split; track basistoelage indexation; dual RTBF package ~378m,src_vrt_jv2025_fin_html,strong,Vlaanderen>CJSM>Media>VRT,tick146; supersedes flat-only cmt_vrt_dotatie for full package; dual PSB VRT gov 306 + RTBF 378 ~684m 2025',
])

append_lines(DATA / "leaderboard.csv", [
    "lb_vrt_public_package,VRT public overheidsfinanciering ~306m 2025 (basistoelage path to 296.4 2026),multi,ops,Vlaanderen>Media>VRT,306000000,528400000,JV2025 strong: gov 306m of total rev 528.4m; eigen 222.3; dual RTBF package 378; basistoelage jumps 258.4 to 296.4 in 2026 via wage index consolidation,strong,src_vrt_jv2025_fin_html,Flemish households media consumers,Public service broadcasting Flanders,Core remit not pure waste; dual NL/FR PSB; commercial cap 90.8m,5,8.0,7,6.3,Benchmark vs RTBF unit cost; open annual side-envelope L5; no automatic merge,seed,,tick146",
])

# entity
etext, _ = read_text(DATA / "entities.csv")
if not any(line.startswith("vrt,") for line in etext.splitlines()):
    append_lines(DATA / "entities.csv", [
        "vrt,VRT,VRT,Vlaamse Radio- en Televisieomroeporganisatie,agency,vlaanderen_gov,nl,https://www.vrt.be,,,PSB Flanders; 2025 gov 306m total rev 528.4m; basistoelage 2026 296.4m; dual RTBF",
    ])

# research_queue
rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_136,VRT BHO full cash-by-year + side envelopes,continuous,6,open,L2,vrt,'
    '"Beyond basistoelage: all public VRT lines.",'
    ",2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,"
)
new = (
    'rq_136,VRT BHO full cash-by-year + side envelopes,continuous,6,done,L2,vrt,'
    '"Beyond basistoelage: all public VRT lines.",'
    "gap_vrt_side_envelopes,2026-07-27T14:00:00Z,2026-07-27T22:10:00Z,"
    '"tick146: gov 2023-25 297.9/304.4/306m; basistoelage 258.4->296.4; FOI residual 2024-25 L5 split"'
)
if old not in rtext:
    raise SystemExit("rq_136 OLD NOT FOUND:\n" + "\n".join(l for l in rtext.splitlines() if "rq_136" in l))
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_vrt_side_envelopes.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_vrt_side_envelopes`  
**Status:** ready (human send only)  
**Linked:** rq_136 · cmt_vrt_public_package_2022_30 · lb_vrt_public_package

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: VRT — transparantie / financieel
     en/of Vlaamse overheid Team Openbaarheid / Departement CJSM Media
     openbaarheid@vlaanderen.be
     Havenlaan 88 bus 20 1000 Brussel

Betreft: Verzoek om openbaarmaking — VRT overheidsfinanciering split 2023-2026

Geachte,

Op grond van het Bestuursdecreet dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Cash-by-year 2023-2026 van alle openbare middelen aan VRT, gesplitst in minstens:
   - basistoelage / basisdotatie;
   - loonindexatie / indexprovisie;
   - eenmalige of structurele aanvullingen (inflatie, energie, transformatieplan);
   - specifieke toelagen (VRT MAX/BVN, samenwerking NL, opleiding digitaal, O&I, sport evenementen);
   - uitgestelde/in opbrengst genomen dotaties (nieuwbouw, sport);
   - overige subsidies (EU, VLAIO, federale of lokale).
2. Begrotingsartikels / BBT-codes Vlaamse begroting per lijn 2024-2026.
3. Aansluitingstabel basistoelage 258,393k (2025) / 296,400k (2026) naar totale
   overheidsfinanciering in de jaarrekening (2024: 304,4m; 2025: 306m class).
4. Commercieel plafond en realisatie BAN+commerciele communicatie 2023-2026.

Periode: 2023-01-01 tot meest recente stand.

### 2. Context

Jaarverslagen en parlementaire antwoorden geven sterke totalen; L5 side-envelope
matrix en budgetcodes ontbreken voor volledige multi-year compare met RTBF.

Hierarchie: Vlaanderen > CJSM > Media > VRT.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: gap_vrt_side_envelopes

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
""",
    encoding="utf-8",
    newline="\n",
)

append_lines(DATA / "foi_queue.csv", [
    "gap_vrt_side_envelopes,Vlaanderen>Media>VRT>side_envelopes,vrt,L5 split all public lines beyond basistoelage 2023-2026 with BBT codes; reconcile basistoelage 258.4/296.4 to gov totals 304.4/306; commercial plafond series,Totals strong; side-envelope matrix incomplete,5,VRT / Team Openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vrt_side_envelopes.md,ready,2026-07-27,,,,,cmt_vrt_public_package_2022_30,lb_vrt_public_package,2026-07-27T22:10:00Z,2026-07-27T22:10:00Z,tick146 partial; human send",
])

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 Actiris Myria hospitals; FOI ready human send. rq_136 VRT package done."\n',
    "utf-8",
)

log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (VRT BHO full public financing + side envelopes)
- Found (strong JV2023 + JV2024 + JV2025 web + PQ130):
  - **Overheidsfinanciering:** 2022 **EUR 290.6m** · 2023 **297.9m** · 2024 **304.4m** · 2025 **306m**.
  - **2023 L5 split:** basisdot **287.2** + inflatie **7.1** + transform **1.1** + overige **2.5**.
  - **Basistoelage path:** 2025 **258.393m** → 2026 **296.400m** (wage index +36.34; partial ops +1.49; MAX +0.10; energy −0.28; digital +0.20; NL coop +0.15).
  - **Eigen inkomsten:** 2023 **199.7** · 2024 **203.7** · 2025 **222.3**; total rev 2025 **528.4m**.
  - **BAN+comm 2025: EUR 83m** (plafond 90.8); external production invest **122.3m**.
  - Dual PSB 2025 class: VRT gov **306** + RTBF package **378** ≈ **~684m**.
- Wrote: sources 5; budgets 27; cmt_vrt_public_package; lb_vrt; rq_136=done; FOI residual ready.
- FOI: gap_vrt_side_envelopes (2024-26 L5 matrix + BBT codes) human send.
- Next: prio6 **rq_134 Actiris** / **rq_140 hospitals** / **rq_120 Myria**.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick146 write OK")

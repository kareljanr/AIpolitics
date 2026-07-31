# -*- coding: utf-8 -*-
"""Tick 148: rq_140 Hospital federal/regional investment subsidies L5 sample."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T22:50:00Z"
TICK = 148
UNIT = "rq_140"


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
    'src_nbb_subsidies_ent_2025_vipa,NBB Economic Review 2025 No9 Flanders D.92 Hospitals via VIPA tables A3-A4,https://www.nbb.be/doc/ts/publications/economicreview/2025/ecorevi2025_h09.pdf,NBB/NAI,2026-07-27,official,"Flanders D.92 hospitals VIPA: public 72m 2023; non-public 208m 2023 / 192m 2024; FL D.92 total 1204/1362m 2023-24; FWB CHU Liege 9m + other UZ 7m 2023"',
    'src_vrt_jessa_vipa_500m,VRT NWS Jessa Ziekenhuis Hasselt VIPA 500m over 40 years May 2026,https://www.vrt.be/vrtnws/nl/2026/05/16/jessa-ziekenhuis-subsidies-vipa-bouw-nieuw-ziekenhuis-hasselt/,VRT NWS,2026-07-27,news,"Flanders awards VIPA ~500m total (annual forfait 40y after opening); project cost ~1bn own+loans; doctors invest 125m; ready ~2036"',
    'src_jessa_vipa_groen_licht,Jessa ZH VIPA groen licht zorgpark,https://www.jessazh.be/w/vipa-geeft-groen-licht-voor-nieuw-zorgpark-van-jessa,Jessa Ziekenhuis,2026-07-27,agency,"VIPA annual forfait 40 years estimated total ~500m from use date"',
    'src_gezondbelgie_bfm_2025,GezondBelgie hospital financing BFM general hospitals Jan 2025,https://www.gezondbelgie.be/nl/blikvanger-gezondheidszorg/algemene-ziekenhuizen/financiering,FPS Health / GezondBelgie,2026-07-27,agency,"General hospitals BFM max 9.62bn Jan 2025"',
    'src_despecialist_bfm_2025,De Specialist hospital BFM total 2025 11.778bn,https://www.despecialist.eu/nl/nieuws/bijna-11-8-miljard-euro-toegewezen-aan-ziekenhuizen-voor-2025.html,De Specialist,2026-07-27,news,"Total hospital BFM 2025 11778368068 EUR class; secondary citing official allocation"',
    'src_artsenkrant_vipa_2024,Artsenkrant VIPA strategic forfaits paid 2024,https://lejournaldumedecin.pmg.be/nl/dossier/EAHbe2505W14_00,Artsenkrant,2026-07-27,press,"VIPA paid strategic forfaits hospitals 4476693.98 EUR in 2024; cash-year only medium"',
])

append_lines(DATA / "budgets.csv", [
    # Flanders VIPA D.92 hospitals NBB strong
    "bud_vipa_hosp_public_2023,vipa,2023,72000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,Flanders D.92 investment grants hospitals via VIPA to public enterprises 72m 2023",
    "bud_vipa_hosp_nonpublic_2023,vipa,2023,208000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,Flanders D.92 hospitals VIPA non-public enterprises 208m 2023",
    "bud_vipa_hosp_nonpublic_2024,vipa,2024,192000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,Flanders D.92 hospitals VIPA non-public 192m 2024",
    "bud_vipa_hosp_total_2023,vipa,2023,280000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,Sum public+non-public VIPA hospitals D.92 2023 72+208",
    "bud_fl_d92_total_2023,vlaanderen_gov,2023,1204000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,Flanders total D.92 investment grants to enterprises 1.204bn 2023",
    "bud_fl_d92_total_2024,vlaanderen_gov,2024,1362000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,Flanders total D.92 1.362bn 2024",
    # Federal BFM operating envelope
    "bud_bfm_general_hosp_2025,fod_volksgezondheid,2025,9620000000,,,budgeted,src_gezondbelgie_bfm_2025,strong,BFM general hospitals max 9.62bn Jan 2025 (operating not pure investment)",
    "bud_bfm_all_hosp_2025,fod_volksgezondheid,2025,11778368068,,,budgeted,src_despecialist_bfm_2025,medium,All hospitals BFM total 11.778bn 2025 secondary citing official",
    # FWB university hospitals current subsidies (not investment)
    "bud_fwb_chu_liege_2023,fwb_gov,2023,9000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,FWB D.31 subsidy CHU Liege 9m 2023",
    "bud_fwb_other_uz_2023,fwb_gov,2023,7000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,FWB D.31 other university hospitals 7m 2023",
    # VIPA cash strategic forfaits small line 2024
    "bud_vipa_strategic_cash_2024,vipa,2024,4476693.98,,,outturn,src_artsenkrant_vipa_2024,medium,VIPA strategic forfaits cash paid 2024 only 4.48m (multi-year commitments larger)",
    # Jessa multi-year
    "bud_jessa_vipa_envelope,vipa,2026,500000000,,,commitment,src_vrt_jessa_vipa_500m,strong,Jessa Hasselt VIPA strategic forfait package ~500m over 40y after opening (not single-year cash)",
])

append_lines(DATA / "commitments.csv", [
    'cmt_vipa_hospitals_d92,Flanders VIPA hospital investment grants multi-year D.92,vipa,Flemish hospitals (public+non-public),VIPA / Departement Zorg infrastructure subsidies,2015-01-01,2023,2024,280000000,"{""2023_public"":72000000,""2023_nonpublic"":208000000,""2023_total"":280000000,""2024_nonpublic"":192000000,""2015_public"":5000000,""note"":""NBB ESA D.92 cash-year; strategic forfait multi-year commitments exceed annual cash""}",0,active,https://www.nbb.be/doc/ts/publications/economicreview/2025/ecorevi2025_h09.pdf,High-quality healthcare infrastructure Flanders,Publish named L5 beneficiaries annual; open VIPA payment calendar,src_nbb_subsidies_ent_2025_vipa,strong,Vlaanderen>VIPA>ziekenhuizen,tick148',
    'cmt_jessa_vipa_500m,Jessa Ziekenhuis Hasselt VIPA strategic forfait ~500m/40y,vipa,Jessa Ziekenhuis Hasselt,VIPA strategisch forfait besluit 2026,2026-05-16,2026,2066,500000000,"{""total_envelope_class"":500000000,""years"":40,""project_total_cost"":1000000000,""doctors_invest_claim"":125000000,""opening_class"":2036,""cash_start"":""after_opening_annual_forfait""}",0,active,https://www.jessazh.be/w/vipa-geeft-groen-licht-voor-nieuw-zorgpark-van-jessa,Replace ageing hospital infrastructure Hasselt,Track annual forfait cash once open; KPI beds/network,src_vrt_jessa_vipa_500m,strong,Vlaanderen>VIPA>Jessa,tick148 named L5 largest single hospital package found',
    'cmt_bfm_hospitals_2025,Federal BFM hospital operating budget 2025,fod_volksgezondheid,All Belgian hospitals,Budget van Financiele Middelen FOD Volksgezondheid,2025-01-01,2025,2025,11778368068,"{""all_hospitals_2025"":11778368068,""general_hospitals_jan2025"":9620000000,""note"":""operating BFM not investment grants; dual with regional VIPA infra""}",0,active,https://www.gezondbelgie.be/nl/blikvanger-gezondheidszorg/algemene-ziekenhuizen/financiering,Hospital operating financing federal,Separate investment (VIPA) from BFM ops; publish hospital-level BFM,src_gezondbelgie_bfm_2025,strong,Federal>Volksgezondheid>BFM,tick148; do not double-count with VIPA D.92',
])

append_lines(DATA / "leaderboard.csv", [
    "lb_vipa_hosp_invest,Flanders VIPA hospital investment grants ~192-280m/yr,Flanders,subsidy,Vlaanderen>VIPA>ziekenhuizen,192000000,280000000,NBB strong: D.92 non-public 192m 2024 / total public+non-public 280m 2023; multi-year forfaits exceed cash year,strong,src_nbb_subsidies_ent_2025_vipa,Flemish hospital patients,Healthcare infrastructure quality,Core infrastructure not pure waste; L5 names thin except Jessa 500m,4,7.5,5,5.8,Publish annual named top-20 VIPA; FOI residual list,seed,,tick148",
    "lb_jessa_vipa_500m,Jessa Hasselt VIPA package ~500m over 40y,Flanders,subsidy,Vlaanderen>VIPA>Jessa,12500000,500000000,VRT+Jessa strong May2026: ~500m total annual forfait 40y; project ~1bn; annual_avg illustrative 12.5m,strong,src_vrt_jessa_vipa_500m,Limburg patients,New hospital campus,Large multi-decade commitment; cash starts after opening ~2036,5,7.0,4,5.8,Track forfait indexation; publish open cash schedule,seed,,tick148",
    "lb_bfm_hospitals_ops,Federal BFM hospital operating envelope ~11.8bn 2025,federal,ops,Federal>Volksgezondheid>BFM,11778368068,11778368068,GezondBelgie general 9.62bn + De Specialist total 11.78bn 2025; operating not investment,strong,src_gezondbelgie_bfm_2025,Hospital patients BE,Hospital operating financing,Core health spending; dual with regional infra VIPA,2,9.5,8,5.5,Publish hospital-level BFM open data; efficiency benchmarks,seed,,tick148",
])

# entity vipa if missing
etext, _ = read_text(DATA / "entities.csv")
if not any(line.startswith("vipa,") for line in etext.splitlines()):
    append_lines(DATA / "entities.csv", [
        "vipa,Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden,Fonds flamand d infrastructure pour les matieres personnalisables,Flemish Infrastructure Fund for Person-related Matters,agency,vlaanderen_gov,nl,https://www.departementzorg.be/nl/vipa-0,,,Hospital and care infrastructure subsidies; D.92 ~192-280m/yr hospitals",
    ])
if not any(line.startswith("fod_volksgezondheid,") for line in etext.splitlines()):
    append_lines(DATA / "entities.csv", [
        "fod_volksgezondheid,FOD Volksgezondheid,SPF Sante publique,FPS Health Food Chain Safety and Environment,ministry,sec_federal,bi,https://www.health.belgium.be,,,BFM hospital operating budget ~11.8bn 2025",
    ])

rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_140,Hospital federal/regional investment subsidies L5 sample,continuous,6,open,L5,gg_belgium,'
    '"Named hospital infra subsidies top 10.",'
    ",2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,"
)
new = (
    'rq_140,Hospital federal/regional investment subsidies L5 sample,continuous,6,done,L5,gg_belgium,'
    '"Named hospital infra subsidies top 10.",'
    "gap_vipa_named_l5,2026-07-27T14:00:00Z,2026-07-27T22:50:00Z,"
    '"tick148: VIPA D.92 280m 2023/192m 2024; Jessa 500m/40y; BFM 11.8bn ops; FOI named top list"'
)
if old not in rtext:
    raise SystemExit("rq_140 OLD NOT FOUND:\n" + "\n".join(l for l in rtext.splitlines() if "rq_140" in l))
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_vipa_named_l5.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_vipa_named_l5`  
**Status:** ready (human send only)  
**Linked:** rq_140 · cmt_vipa_hospitals_d92 · lb_vipa_hosp_invest

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Departement Zorg / VIPA
     Team Openbaarheid Vlaanderen
     openbaarheid@vlaanderen.be
     Havenlaan 88 bus 20 1000 Brussel

Betreft: Verzoek om openbaarmaking — VIPA ziekenhuissubsidies L5 2023-2026

Geachte,

Op grond van het Bestuursdecreet dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Lijst van alle goedgekeurde VIPA-toekenningen aan ziekenhuizen 2023-2026 met:
   - naam instelling / KBO;
   - type (strategisch forfait / instandhouding / toestelfinanciering);
   - totaal toegekend envelope en looptijd (jaren);
   - cash-by-year betaald 2023-2026.
2. Jaarlijkse kredieten VIPA ziekenhuizen (begrotingscodes BBT) 2023-2026.
3. Aansluitingstabel naar NBB/ESA D.92 totalen (2023: ~280m class public+non-public).
4. Volledige beslissing Jessa Hasselt strategisch forfait (~500m / 40 jaar) met betaalkalender.

Periode: 2023-01-01 tot meest recente stand.

### 2. Context

NBB publiceert aggregaten VIPA-ziekenhuizen; open data goedgekeurde aanvragen
op departementzorg.be mist systematische EUR-bedragen. Jessa is een bekend
L5-dossier; top-10 ontbreekt.

Hierarchie: Vlaanderen > VIPA > ziekenhuizen.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: gap_vipa_named_l5

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
    "gap_vipa_named_l5,Vlaanderen>VIPA>ziekenhuizen>named_L5,vipa,Named VIPA hospital awards 2023-2026 with envelopes cash-by-year and BBT codes; reconcile NBB D.92 192-280m; Jessa 500m payment calendar,NBB aggregates + Jessa package strong; bulk named top-10 thin,7,Departement Zorg VIPA / Team Openbaarheid,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vipa_named_l5.md,ready,2026-07-27,,,,,cmt_vipa_hospitals_d92,lb_vipa_hosp_invest,2026-07-27T22:50:00Z,2026-07-27T22:50:00Z,tick148 partial; human send",
])

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 universities intercommunales Myria; FOI ready human send. rq_140 hospital infra done."\n',
    "utf-8",
)

log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Hospital federal/regional investment subsidies L5 sample)
- Found (strong NBB + BFM + named Jessa):
  - **Flanders VIPA hospitals D.92:** public **EUR 72m 2023** + non-public **208m 2023 / 192m 2024** (total class **~280m 2023**).
  - **Named L5:** **Jessa Hasselt VIPA ~EUR 500m over 40 years** (approved May 2026; project ~1bn; cash after opening ~2036).
  - **Federal BFM ops:** general hospitals **EUR 9.62bn** Jan 2025; all hospitals **EUR 11.778bn 2025** (operating — not investment).
  - **FWB current:** CHU Liege **EUR 9m** + other UZ **EUR 7m** 2023 (NBB D.31).
  - Strategic forfaits cash 2024 only **EUR 4.48m** medium (commitments multi-year larger).
  - Prior stock: Flanders non-Maastricht hospital infra claim **EUR 2.184bn**.
- Wrote: sources 6; budgets 12; cmt 3; lb 3; entities vipa+fod_volksgezondheid; rq_140=done; FOI residual ready.
- FOI: gap_vipa_named_l5 (top named list + cash calendar) human send.
- Next: prio6 **rq_141 universities** / **rq_142 intercommunales** / **rq_120 Myria**.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick148 write OK")

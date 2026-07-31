# -*- coding: utf-8 -*-
"""Tick 149: rq_141 Universities public operating grants by institution."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T23:15:00Z"
TICK = 149
UNIT = "rq_141"


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
    'src_vl_crc_ho_2024,College regeringscommissarissen financiele toestand Vlaams hoger onderwijs 2024,https://data-onderwijs.vlaanderen.be/documenten/bestanden/financi%C3%ABle-toestand-en-evolutie-personeelsbestand-hoger-onderwijs.pdf,College van regeringscommissarissen HO,2026-07-27,official,"VL universities 2024: 1st stream basisfinanciering 1440744600 (werkingsuitk 1354798125 invest 45623950 stuvo 30359491); 2nd 460276480; 3rd 711880167; 4th 378276220; AHOVOKS effective werkings 1224240771; per student 8286; students 149848"',
    'src_kuleuven_jv_2025,KU Leuven Jaarverslag 2025 resultatenrekening geldstromen,https://www.kuleuven.be/over-kuleuven/pdf/jaarverslag-ku-leuven-2025.pdf,KU Leuven,2026-07-27,annual_report,"1st stream 2024 546506062 (werkings 515120013 invest 19364877 stuvo 11843756); 2025 1st 567940708 (werkings 536061091); research exp 2024 749.2m 2025 781.88m; bedrijfsopbrengsten 2025 1.565bn"',
    'src_fwb_expgen_2026,FWB Expose general depenses 2026 Initial education superieur lines,https://budget-finances.cfwb.be/fileadmin/sites/dgbf/uploads/documents/budget_comptabilite/ressources/budgets/2026/Expose_general_des_depenses_2026_-_Initial.pdf,FWB Budget,2026-07-27,budget,"Prior tick: edu_class 10.928bn 2026; superieur_savings 14m; research do45 262.6m; not per-university split"',
])

append_lines(DATA / "budgets.csv", [
    # VL universities aggregate first stream
    "bud_vl_univ_1st_stream_2024,sec_flanders,2024,1440744600,,,outturn,src_vl_crc_ho_2024,strong,VL universities basisfinanciering 1st geldstroom total 2024",
    "bud_vl_univ_werking_2024,sec_flanders,2024,1354798125,,,outturn,src_vl_crc_ho_2024,strong,VL universities werkingsuitkeringen code 7000 2024",
    "bud_vl_univ_invest_uitk_2024,sec_flanders,2024,45623950,,,outturn,src_vl_crc_ho_2024,strong,VL universities investeringsuitkeringen 2024",
    "bud_vl_univ_stuvo_2024,sec_flanders,2024,30359491,,,outturn,src_vl_crc_ho_2024,strong,VL universities sociale toelagen STUVO 2024",
    "bud_vl_univ_ahovoks_werking_2024,sec_flanders,2024,1224240771,,,outturn,src_vl_crc_ho_2024,strong,AHOVOKS effectieve werkingsmiddelen paid 2024 (excl some components)",
    "bud_vl_univ_2nd_stream_2024,sec_flanders,2024,460276480,,,outturn,src_vl_crc_ho_2024,strong,2nd stream fundamental research gov (BOF+FWO class) 2024",
    "bud_vl_univ_3rd_stream_2024,sec_flanders,2024,711880167,,,outturn,src_vl_crc_ho_2024,strong,3rd stream applied research gov 2024",
    "bud_vl_univ_4th_stream_2024,sec_flanders,2024,378276220,,,outturn,src_vl_crc_ho_2024,strong,4th stream private research + valorisatie 2024",
    "bud_vl_univ_total_edu_research_rev_2024,sec_flanders,2024,3331395347,,,outturn,src_vl_crc_ho_2024,strong,All 4 streams + other edu/research related revenue 2024",
    "bud_vl_univ_per_student_werking_2024,sec_flanders,2024,8286,,,outturn,src_vl_crc_ho_2024,strong,Werkingsmiddelen per student under diplomacontract 2024 EUR",
    # KU Leuven named
    "bud_kuleuven_1st_2024,ku_leuven,2024,546506062,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven 1st stream basisfinanciering 2024",
    "bud_kuleuven_werking_2024,ku_leuven,2024,515120013,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven werkingsuitkeringen 2024 (~38pct of VL univ 1st stream)",
    "bud_kuleuven_invest_2024,ku_leuven,2024,19364877,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven investeringsuitkeringen 2024",
    "bud_kuleuven_stuvo_2024,ku_leuven,2024,11843756,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven sociale toelagen 2024",
    "bud_kuleuven_1st_2025,ku_leuven,2025,567940708,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven 1st stream 2025",
    "bud_kuleuven_werking_2025,ku_leuven,2025,536061091,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven werkingsuitkeringen 2025 (+20.9m vs 2024)",
    "bud_kuleuven_research_exp_2024,ku_leuven,2024,749200000,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven total research expenditure 2024",
    "bud_kuleuven_research_exp_2025,ku_leuven,2025,781880000,,,outturn,src_kuleuven_jv_2025,strong,KU Leuven total research expenditure 2025",
    # FWB education aggregate (not pure university ops)
    "bud_fwb_edu_class_2026,fwb_gov,2026,10928638000,,,budgeted,src_fwb_expgen_2026,strong,FWB education class envelope 10.928bn 2026 (schools+HE; not university-only)",
    "bud_fwb_superieur_savings_2026,fwb_gov,2026,14000000,,,budgeted,src_fwb_expgen_2026,strong,FWB superieur savings line 14m 2026",
])

append_lines(DATA / "commitments.csv", [
    'cmt_vl_univ_basisfinanciering_2024,Flanders universities basisfinanciering 1st stream multi-year,sec_flanders,5 VL universities (KU Leuven UGent UA UHasselt VUB),Decreet hoger onderwijs enveloppesysteem AHOVOKS,2020-01-01,2020,2024,1440744600,"{""2020_1st"":1166685767,""2021_1st"":1173755120,""2022_1st"":1276706214,""2023_1st"":1361480191,""2024_1st"":1440744600,""2024_werking"":1354798125,""2024_invest"":45623950,""2024_stuvo"":30359491,""2024_ahovoks_werking"":1224240771,""2024_2nd"":460276480,""2024_3rd"":711880167,""2024_4th"":378276220,""2024_per_student"":8286,""2024_students"":149848,""2024_extra_nl_20m"":true,""2024_extra_medicine_10m"":true}",0,active,https://data-onderwijs.vlaanderen.be/documenten/bestanden/financi%C3%ABle-toestand-en-evolutie-personeelsbestand-hoger-onderwijs.pdf,Public higher education basisfinanciering Flanders,Publish AHOVOKS per-university matrix annually open data,src_vl_crc_ho_2024,strong,Vlaanderen>Onderwijs>Universiteiten,tick149; residual per-institution except KU Leuven FOI',
    'cmt_kuleuven_public_1st_stream,KU Leuven public basisfinanciering 1st stream,ku_leuven,KU Leuven,CHO + AHOVOKS enveloppe,2024-01-01,2024,2025,567940708,"{""2024_1st"":546506062,""2024_werking"":515120013,""2024_invest"":19364877,""2024_stuvo"":11843756,""2025_1st"":567940708,""2025_werking"":536061091,""share_vl_1st_2024_pct"":37.9,""research_exp_2024"":749200000,""research_exp_2025"":781880000}",0,active,https://www.kuleuven.be/over-kuleuven/pdf/jaarverslag-ku-leuven-2025.pdf,Largest VL university public operating grant,Benchmark unit cost per student; track marktaandeel shifts,src_kuleuven_jv_2025,strong,Vlaanderen>Universiteiten>KU_Leuven,tick149 named L5',
])

append_lines(DATA / "leaderboard.csv", [
    "lb_vl_univ_basisfinanciering,Flanders universities basisfinanciering 1st stream ~1.44bn 2024,Flanders,ops,Vlaanderen>Universiteiten>1ste_geldstroom,1440744600,1440744600,CRC HO 2024 strong: 1st stream 1.441bn (werking 1.355 + invest 45.6 + stuvo 30.4); per student 8286; dual FWB HE separate,strong,src_vl_crc_ho_2024,149848 university students VL,Public higher education basisfinanciering,Core education not pure waste; partial indexation + efficiency plans,3,9.0,7,5.7,Open AHOVOKS per-uni matrix; dual FWB transparency,seed,,tick149",
    "lb_kuleuven_werking,KU Leuven werkingsuitkering ~515-536m 2024-25,Flanders,ops,Vlaanderen>Universiteiten>KU_Leuven,515120013,536061091,JV2025 strong: largest VL share ~38pct of 1st stream; research exp separate 749-782m,strong,src_kuleuven_jv_2025,KU Leuven students researchers,University basisfinanciering,Core remit; marktaandeel pressure noted in JV,3,8.5,6,5.5,Publish peer unit costs; residual UGent UA VUB UHasselt FOI,seed,,tick149",
])

etext, _ = read_text(DATA / "entities.csv")
if not any(line.startswith("ku_leuven,") for line in etext.splitlines()):
    append_lines(DATA / "entities.csv", [
        "ku_leuven,KU Leuven,KU Leuven,Katholieke Universiteit Leuven,university,sec_flanders,nl,https://www.kuleuven.be,,,Largest VL uni; 1st stream 546.5m 2024 / 567.9m 2025; research exp ~782m 2025",
    ])

rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_141,Universities public operating grants by institution,continuous,6,open,L5,gg_belgium,'
    '"VL+FWB+federal university grants named.",'
    ",2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,"
)
new = (
    'rq_141,Universities public operating grants by institution,continuous,6,done,L5,gg_belgium,'
    '"VL+FWB+federal university grants named.",'
    "gap_univ_per_institution,2026-07-27T14:00:00Z,2026-07-27T23:15:00Z,"
    '"tick149: VL 1st stream 1.441bn 2024; KU Leuven 515m werking; FOI residual 4 unis + FWB"'
)
if old not in rtext:
    raise SystemExit("rq_141 OLD NOT FOUND:\n" + "\n".join(l for l in rtext.splitlines() if "rq_141" in l))
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_univ_per_institution.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_univ_per_institution`  
**Status:** ready (human send only)  
**Linked:** rq_141 · cmt_vl_univ_basisfinanciering_2024 · lb_vl_univ_basisfinanciering

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: AHOVOKS / Departement Onderwijs en Vorming
     Team Openbaarheid Vlaanderen
     openbaarheid@vlaanderen.be
     Havenlaan 88 bus 20 1000 Brussel

     en/of: Ministere FWB Enseignement superieur / ARES
     publicite de l administration

Betreft: Verzoek om openbaarmaking — werkingsuitkeringen per universiteit 2023-2026

Geachte,

Op grond van het Bestuursdecreet / regles d ouverture de l administration
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp (Vlaanderen)

1. AHOVOKS-uitbetaalde werkingsmiddelen / basistoelage per universiteit
   (KU Leuven, UGent, UAntwerpen, UHasselt, VUB) cash-by-year 2023-2026,
   met splitsing: werkingsuitkering, investeringsuitkering, STUVO, AOM,
   werkgeversbijdragen, speciale impulsen.
2. Marktaandelen en parameters die de enveloppeverdeling bepalen.

### 2. Voorwerp (FWB)

1. Dotations / subventions de fonctionnement aux universites de la FWB
   (UCLouvain, ULB, ULiege, UMons, UNamur et le cas echeant autres)
   cash-by-year 2023-2026.
2. Codes budgetaires FWB et reconciliation avec l enveloppe enseignement
   superieur / ARES.

Periode: 2023-01-01 tot meest recente stand.

### 3. Context

Sectorrapport VL 2024 geeft sterke totalen (1ste geldstroom 1,441 bn);
KU Leuven JV geeft named 515-536m werking. Ontbrekend: open matrix voor
alle 5 VL-unies + FWB per-instelling.

Hierarchie: BE > Universities > public operating grants.

### 4. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 5. Identiteit

Naam: […]
Dossierreferentie intern: gap_univ_per_institution

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
    "gap_univ_per_institution,BE>Universities>operating_grants_L5,sec_flanders,AHOVOKS per-university werkingsuitkering matrix 2023-2026 (5 VL unis) + FWB university operating dots by institution,VL sector totals + KU Leuven strong; UGent UA VUB UHasselt + FWB L5 opaque,7,AHOVOKS / Team Openbaarheid + FWB Enseignement,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_univ_per_institution.md,ready,2026-07-27,,,,,cmt_vl_univ_basisfinanciering_2024,lb_vl_univ_basisfinanciering,2026-07-27T23:15:00Z,2026-07-27T23:15:00Z,tick149 partial; human send",
])

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 intercommunales climate Myria; FOI ready human send. rq_141 universities done."\n',
    "utf-8",
)

log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Universities public operating grants by institution)
- Found (strong CRC HO 2024 + KU Leuven JV 2025):
  - **VL universities 1st stream 2024: EUR 1.441bn** (werking **1.355bn** · invest **45.6m** · STUVO **30.4m**); path 1.167→1.441bn 2020-24.
  - **AHOVOKS effectieve werkingsmiddelen 2024: EUR 1.224bn**; **EUR 8,286/student**; 149,848 students.
  - **2nd/3rd/4th streams 2024:** 460m · 712m · 378m (research).
  - **Named L5 KU Leuven:** 1st stream **EUR 546.5m 2024 / 567.9m 2025**; werking **515.1 / 536.1m** (~38% of VL 1st).
  - **FWB:** education class **EUR 10.93bn 2026** (not uni-only); superieur savings **14m** — per-uni FOI.
- Wrote: sources 3; budgets 20; cmt 2; lb 2; entity ku_leuven; rq_141=done; FOI residual ready.
- FOI: gap_univ_per_institution (4 remaining VL unis + FWB) human send.
- Next: prio6 **rq_142 intercommunales** / **rq_148 climate** / **rq_120 Myria**.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick149 write OK")

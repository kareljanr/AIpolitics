#!/usr/bin/env python3
"""Surgical tick 2367 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_sig"
SRC_PDF = "src_sig_jr2025_nbb_pdf_2367"
SRC_KBO = "src_sig_kbo_2367"
SRC_SBM = "src_sig_sbm_2367"
SRC_SITE = "src_sig_site_2367"
COMM = "comm_sig_jr2025_statutory_bruto_0_86m_pnl_jump_109k_bestemde_fondsen_cash_0_72m"
LB = "lb_sig_bruto_0_86m_pnl_jump_109k_bestemde_fondsen_jr2025"
GAP = "gap_sig_vl_matrix_bruto_0_86m_omzet_empty_109k_bestemde_fondsen_cash_0_72m_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

# --- FOI draft ---
foi = f"""# FOI draft — Sig vzw (bruto 0.86m / omzet+73 empty / 109k bestemde fondsen / cash 0.72m / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Sig vzw — KBO **0431.736.211** (Actief; 1 VE **2.156.389.875** naam vzw Sig; zetel Kloosterstraat 6, 9031 Gent/Drongen; operationeel Pachthofstraat 1, 9308 Aalst; RSZ2025 **94.993** ziektepreventie/gezondheidsbevordering; NACE VE **85.599** overige vormen van onderwijs; voorzitter Nick Van Hamme)  
**recipient:** Sig vzw / Nick Van Hamme (voorzitter RvB) — info@sig-net.be — Pachthofstraat 1, 9308 Aalst  
**sources:** official NBB WVV VKT-VZW PDF deposit **2026-00072461** (header **02.04.2026**; CDN Last-Modified **11.04.2026**; AV **02.03.2026**; **49763** bytes / **13p**; model **VKT-VZW** 25.0.10 m04-f); [official CDN](http://cdn.staatsbladmonitor.be/2026pdf/2026-00072461.pdf); [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0431736211); [KBO 0431.736.211](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431736211); [site](https://www.sig-net.be/)  
**tick:** 2367 (NOT every-10; next every-10 is **2370**)

## Context (primary official NBB VKT-VZW JR2025)

- Leftover dual public **inclusie-/vormings-VZW** (mensen met een beperking / psychische kwetsbaarheid) of mined **CAR Wegwijs@2366** + **TKDV Het Veer@2365** + **Kapelhof@2364** + **De Steijger@2363** + **De Steijgertjes@2362** + **De Elfjes@2361** + **Noordhoek@2360** + **Oostakker@2359** + **Stappie@2358** + **'t Vlot@2357** + **CAR Het Veer@2356** + **Ter Kouter@2355** — same statutory seat Kloosterstraat 6 Drongen + shared board (Singelée bestuurder; Van Hamme voorzitter). Operational Pachthofstraat 1 Aalst. Prefix `vzw_sig` unused. Parent `sec_flanders`. Confirmed leftover public (inclusie/gezondheidsbevordering + onderwijs-vorming; same-zetel public CAR cluster) not private clinic.
- Stalls this tick: AGB Bornem still **JR2024**; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). First unused leftover same-zetel with live 2026pdf after Wegwijs: SIG (deposit HEAD 200 / 49763 B).
- EUR **strong** from official PDF (not Companyweb / not SBM table): omzet 70 **empty**; code 73 **empty**; bruto **864311** JUMP +8.45% (VKT envelope); pnl **13584** JUMP from loss −33266; equity **680079** JUMP +2.04%; assets **891158** JUMP +0.59%; debt **211080** DROP −3.79%; FTE **7.7** DROP; kapitaalsubsidies **empty**; destin 691 **empty**; bestemde fondsen 13 **109390** unchanged; cash **722466** JUMP +0.88% (~84% of bruto). Strong KBO + Strong PDF.
- Next leftover same-zetel / cluster if live 2026pdf: DIGOR **0870.833.435** deposit **2026-00205516** (HEAD 200 / 48559 B); Mozaiek **0415.272.935** deposit **2026-00206415** (HEAD 200 / 71192 B). DCGZ 0411.917.131 empty shell. Steunfonds Martens-Sotteau **0476.428.861** absorbed into empty DCGZ (2022).

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Sig vzw
t.a.v. de dienst openbaarheid van bestuur / Nick Van Hamme
(voorzitter Raad van Bestuur)
Pachthofstraat 1
9308 Aalst
info@sig-net.be
https://www.sig-net.be/

Betreft: Verzoek om openbaarmaking van bestuursdocumenten —
JR2025 Sig vzw (KBO 0431.736.211)
brutomarge 864.311 (omzet 70 leeg / code 73 leeg)
/ winst 13.584 (JUMP vanuit verlies)
/ bestemde fondsen 109.390
/ liquide middelen 722.466
/ FTE 7,7

Geachte,

Op grond van het Bestuursdecreet (openbaarheid van bestuur)
dien ik hierbij een verzoek in tot openbaarmaking / inzage /
afschrift van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. De volledige jaarrekening 2025 (NBB VKT-VZW deposit
   2026-00072461) plus het activiteitenverslag 2025 en
   het verslag van het bestuursorgaan aan de AV van
   2 maart 2026.
2. De uitsplitsing van brutomarge code 9900 EUR 864.311
   (was 796.982; JUMP +8,45%) — waarom omzet code 70
   én lidgeld/schenkingen/subsidies code 73 leeg zijn
   terwijl de brutomarge 0,86 miljoen bedraagt.
   Uitsplitsing vormingen / publicaties / subsidies
   (Vlaanderen / gemeente Aalst / andere) / overige.
3. De toelichting bij bestemde fondsen code 13
   EUR 109.390 (ongewijzigd; geen toevoeging 691) —
   doel / geoormerkte publieke middelen / bestemming;
   overgedragen winst code 14 EUR 567.814.
4. De toelichting bij liquide middelen code 54/58
   EUR 722.466 (was 716.179; JUMP +0,88% — circa 84%
   van de brutomarge) — treasurybeleid / geoormerkte
   publieke middelen.
5. De toelichting bij schulden code 17/49
   EUR 211.080 (was 219.396; DROP −3,79%) — aard
   (handelsschulden 59.294 / sociale lasten 69.179 /
   overlopende rekeningen 76.661).
6. De relatie duale rechtspersonen op dezelfde
   statutaire zetel Drongen (Kloosterstraat 6, zelfde
   adres als CAR Ter Kouter, CAR Het Veer, CAR 't Vlot,
   CAR Stappie, CAR Oostakker, CAR Noordhoek, CAR De
   Steijger, CAR Kapelhof, CAR Wegwijs, KDV De Elfjes,
   KDV De Steijgertjes, TKDV Het Veer) versus
   operationele site Aalst Pachthofstraat 1. Interne
   rekeningen, subsidies, gedeelde raad,
   DIGOR-aansluiting.
7. Het personeelsbestand 2025: 7,7 VTE gemiddeld
   (was 8) versus bezoldigingen code 62
   EUR 645.226 — uitsplitsing per functie / site.
8. De notulen van de algemene vergadering van
   2 maart 2026 (niet-persoonsgebonden delen).
9. Eventuele Vlaamse of lokale subsidies 2025
   (Departement Zorg / Onderwijs / Cultuur / gemeente
   Aalst) — bedrag / looptijd / KPI's. Toelichting
   waarom die niet onder code 73 verschijnen.

Periode: boekjaar 01.01.2025–31.12.2025 en lopende
meerjarige verbintenissen.

### 2. Context (waarom)

Dit verzoek kadert in onderzoek naar overheidsuitgaven
en subsidies (transparantie van publieke middelen).
Hiërarchisch pad (intern):
Vlaanderen > Oost-Vlaanderen > Aalst >
Sig vzw > JR2025 statutory L5.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail.
Indien weigering of gedeeltelijke openbaarmaking:
gemotiveerde beslissing met rechtsgrond en beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern:
{GAP}

Met vriendelijke groet,
[Naam]
```

## Checklist vóór `ready`

- [x] Juiste instelling (Sig vzw / voorzitter RvB)
- [x] Concrete documenten (VL-matrix, omzet+73 empty, 109k bestemde fondsen, 0.72m cash)
- [x] Periode en bedragen gevraagd (PDF-sourced)
- [x] Meerjarigheid expliciet gevraagd
- [ ] Contactgegevens verzoeker ingevuld (human)
- [x] `foi_queue.csv` bijgewerkt
- [x] ready NOT sent (human-gated)
"""
draft_path = ROOT / DRAFT
draft_path.write_text(foi, encoding="utf-8")
print("wrote", draft_path, draft_path.stat().st_size)

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

# sources (+4)
append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB WVV VKT-VZW jaarrekening 2025 Sig vzw deposit 2026-00072461,http://cdn.staatsbladmonitor.be/2026pdf/2026-00072461.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2367; official PDF 49763 bytes 13p VKT-VZW 25.0.10 m04-f; header 02.04.2026; AV 02.03.2026; YE 01.01.2025-31.12.2025; euros extracted from PDF text not SBM table",
    f"{SRC_KBO},KBO Sig vzw 0431.736.211,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431736211,KBO Public Search FOD Economie,{DAY},official_register,tick2367; Actief; 1 VE 2.156.389.875 naam vzw Sig; zetel Kloosterstraat 6 9031 Gent/Drongen; VE Pachthofstraat 1 9308 Aalst; RSZ2025 94.993; NACE VE 85.599; voorzitter Van Hamme Nick; bestuurder Singelee Stefaan",
    f"{SRC_SBM},Staatsbladmonitor fiche Sig vzw 0431736211 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0431736211,Staatsbladmonitor,{DAY},official_register,tick2367; deposit-id 2026-00072461 and CDN Last-Modified 2026-04-11; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Sig vzw FOI contact / inclusie-vorming Aalst,https://www.sig-net.be/,Sig vzw,{DAY},foi_contact,tick2367; operational Pachthofstraat 1 9308 Aalst; FOI info@sig-net.be; zetel Kloosterstraat 6 9031 Drongen; leftover same-zetel Ter Kouter/CAR cluster",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},Sig VZW (Aalst / inclusie-vorming),Sig ASBL (Alost / inclusion-formation),Sig VZW (Aalst / inclusion training),parastatal,sec_flanders,nl,https://www.sig-net.be/,info@sig-net.be,"Pachthofstraat 1, 9308 Aalst / Kloosterstraat 6, 9031 Drongen",tick2367 YE2025 Strong official NBB PDF deposit 2026-00072461 + Strong KBO 0431.736.211 Actief 1 VE 2.156.389.875 RSZ2025 94.993 NACE 85.599; omzet empty; code73 empty; bruto JUMP 864311; pnl JUMP 13584 from loss; equity JUMP 680079; assets JUMP 891158; debt DROP 211080; FTE DROP 7.7; destin691 empty; kapitaalsubsidies empty; bestemde fondsen 109390; cash JUMP 722466; leftover Wegwijs@2366 same zetel; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+9) — envelope = bruto 9900 (VKT + omzet empty)
append_lines(DATA / "budgets.csv", [
    f"bud_sig_bruto_jr2025_statutory,{EID},2025,864311,864311,864311,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +8.45% (primary L5 envelope; omzet 70 empty),{SRC_PDF},strong,tick2367; PDF p6; YE2024 796982; VKT envelope because omzet empty; inclusie-VZW not commercial-only",
    f"bud_sig_pnl_jr2025_statutory,{EID},2025,13584,13584,13584,NBB VKT-VZW code 9904 winst YE2025 JUMP from loss,{SRC_PDF},strong,tick2367; PDF p6; YE2024 -33266; bedrijfswinst 9901 8667",
    f"bud_sig_equity_jr2025_statutory,{EID},2025,680079,680079,680079,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.04%,{SRC_PDF},strong,tick2367; PDF p5; YE2024 666495; kapitaalsubsidies empty; bestemde fondsen 109390",
    f"bud_sig_assets_jr2025_statutory,{EID},2025,891158,891158,891158,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +0.59%,{SRC_PDF},strong,tick2367; PDF p4; YE2024 885891",
    f"bud_sig_debt_jr2025_statutory,{EID},2025,211080,211080,211080,NBB VKT-VZW code 17/49 schulden YE2025 DROP -3.79%,{SRC_PDF},strong,tick2367; PDF p5; YE2024 219396",
    f"bud_sig_cash_jr2025_statutory,{EID},2025,722466,722466,722466,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +0.88% ~84pct bruto,{SRC_PDF},strong,tick2367; PDF p4; YE2024 716179",
    f"bud_sig_bestemde_fondsen_jr2025_statutory,{EID},2025,109390,109390,109390,NBB VKT-VZW code 13 bestemde fondsen YE2025 unchanged; destin 691 empty,{SRC_PDF},strong,tick2367; PDF p5/p7; YE2024 109390",
    f"bud_sig_personnel_jr2025_statutory,{EID},2025,645226,645226,645226,NBB VKT-VZW code 62 bezoldigingen YE2025 DROP -1.28%,{SRC_PDF},strong,tick2367; PDF p6; YE2024 653616; sociale balans 102 606260",
    f"bud_sig_fte_jr2025_statutory,{EID},2025,7.7,7.7,7.7,NBB VKT-VZW code 9087 FTE YE2025 DROP,{SRC_PDF},strong,tick2367; PDF p9; YE2024 8",
])

# commitments (+1) — JSON doubled quotes like prior ticks
cash_json = (
    '"{""2025_omzet"":null,""2025_bruto"":864311,""2025_pnl"":13584,""2025_equity"":680079,'
    '""2025_assets"":891158,""2025_debt"":211080,""2025_fte"":7.7,""2025_code73"":null,'
    '""2025_kapitaalsubsidies"":null,""2025_destin691"":null,""2025_cash"":722466,'
    '""2025_bestemde_fondsen"":109390,""2025_personnel62"":645226,'
    '""2024_omzet"":null,""2024_bruto"":796982,""2024_pnl"":-33266,""2024_equity"":666495,'
    '""2024_assets"":885891,""2024_debt"":219396,""2024_fte"":8,""2024_cash"":716179,'
    '""2024_bestemde_fondsen"":109390}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Sig vzw YE2025 (bruto 0.86m / pnl JUMP from loss / 109k bestemde fondsen / cash 0.72m / Strong PDF),{EID},inclusie-vorming Aalst / dual Drongen zetel,VZW Sig (KBO 0431.736.211; Actief; 1 VE; RSZ2025 94.993),2026-04-02,2025,2025,864311,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00072461.pdf,Inclusie mensen met beperking/psychische kwetsbaarheid + vorming professionelen Aalst + dual Drongen Ter Kouter cluster,Publish VL vs other matrix inside bruto 864k (omzet+73 empty); explain 109k bestemde fondsen + cash 0.72m ~84pct bruto,{SRC_PDF},strong,Vlaanderen>Oost_Vlaanderen>Aalst>Sig>JR2025_statutory_L5,tick2367; Strong official PDF; leftover Wegwijs@2366 same Drongen zetel; not TE-additive",
])

# leaderboard (+1) pi = 0.4*5.5 + 0.4*4.0 + 0.2*5 = 4.80
append_lines(DATA / "leaderboard.csv", [
    f"{LB},Sig vzw bruto 0.86m / pnl JUMP from loss / 109k bestemde fondsen (YE2025 inclusie Aalst),L5,inclusie_vorming_vzw_statutory,Vlaanderen>Oost_Vlaanderen>Aalst>Sig>JR2025,864311,864311,PDF omzet empty; code73 empty; bruto JUMP 864311; pnl JUMP 13584 from loss; equity JUMP 680079; assets JUMP 891158; debt DROP 211080; FTE DROP 7.7; destin691 empty; kapitaalsubsidies empty; cash JUMP 722466; bestemde fondsen 109390,strong,{SRC_PDF},people with disability / psychological vulnerability (inclusie-vorming Aalst + dual Drongen Ter Kouter cluster),Inclusie- en vormingscentrum mensen met beperking,omzet+73 empty while bruto 0.86m; 109k destin unchanged; cash 0.72m ~84% bruto; dual Aalst/Drongen leftover same-zetel of Wegwijs/Ter Kouter cluster; VL/other split unpublished,5.5,4.0,5,4.80,FOI VL matrix inside bruto 864k (omzet+73 empty) + 109k bestemde fondsen + cash 0.72m + dual Aalst/Drongen + Ter Kouter cluster,active,,tick2367; Strong official NBB PDF + Strong KBO; leftover Wegwijs@2366 same zetel; next leftover DIGOR / Mozaiek",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost_Vlaanderen>Aalst>Sig>VL_bruto_omzet_empty,vzw_sig,VL vs other split inside bruto 864311 given omzet 70 empty + code 73 empty; nature of bestemde fondsen 109390 residual public; toelichting cash 722466 ~84pct bruto; dual Aalst/Drongen zetel,Strong official PDF leftover inclusie-VZW of Wegwijs@2366 same zetel; omzet+73 empty while 0.86m bruto; 109k destin; cash 0.72m; public inclusie not private clinic,8,Sig VZW / Nick Van Hamme voorzitter RvB,info@sig-net.be,"Pachthofstraat 1, 9308 Aalst / Kloosterstraat 6, 9031 Drongen",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2367; ready NOT sent; Strong official NBB PDF; after Wegwijs@2366; leftover same-zetel inclusie-VZW; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2367 + append rq_2368 only
rq_path = DATA / "research_queue.csv"
rq_text = rq_path.read_text(encoding="utf-8")
old_2367 = None
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2367,"):
        old_2367 = line
        break
if not old_2367:
    raise SystemExit("rq_2367 line not found")
if rq_text.count("\nrq_2367,") + (1 if rq_text.startswith("rq_2367,") else 0) != 1 and rq_text.count("rq_2367,") != 1:
    # safer: exactly one startswith line
    n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2367,"))
    if n != 1:
        raise SystemExit(f"expected 1 rq_2367 line, found {n}")

new_2367 = (
    "rq_2367,leftover dual — Sig vzw YE2025 Strong (bruto JUMP 0.86m / pnl JUMP from loss / 109k bestemde fondsen),hole_fill,8,done,L5,vzw_sig,"
    "After CAR Wegwijs YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel SIG 0431.736.211 deposit 2026-00072461 if live 2026pdf. "
    "Do NOT redo Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.,"
    f"{GAP},{STAMP.replace(STAMP, '2026-08-24T21:53:43Z')},{STAMP},"
    "tick2367 Sig 0431.736.211 YE2025 Strong official PDF 2026-00072461; omzet empty; code73 empty; bruto JUMP 864311; pnl JUMP 13584 from loss; equity JUMP 680079; assets JUMP 891158; debt DROP 211080; FTE DROP 7.7; destin691 empty; kapitaalsubsidies empty; bestemde fondsen 109390; cash JUMP 722466; FOI ready NOT sent; leftover Wegwijs@2366 same zetel; next leftover DIGOR / Mozaiek\n"
)
# created_utc should stay the spawn time of rq_2367
new_2367 = (
    "rq_2367,leftover dual — Sig vzw YE2025 Strong (bruto JUMP 0.86m / pnl JUMP from loss / 109k bestemde fondsen),hole_fill,8,done,L5,vzw_sig,"
    "After CAR Wegwijs YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel SIG 0431.736.211 deposit 2026-00072461 if live 2026pdf. "
    "Do NOT redo Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.,"
    f"{GAP},2026-08-24T21:53:43Z,{STAMP},"
    "tick2367 Sig 0431.736.211 YE2025 Strong official PDF 2026-00072461; omzet empty; code73 empty; bruto JUMP 864311; pnl JUMP 13584 from loss; equity JUMP 680079; assets JUMP 891158; debt DROP 211080; FTE DROP 7.7; destin691 empty; kapitaalsubsidies empty; bestemde fondsen 109390; cash JUMP 722466; FOI ready NOT sent; leftover Wegwijs@2366 same zetel; next leftover DIGOR / Mozaiek\n"
)
if not rq_text.endswith("\n"):
    raise SystemExit("research_queue missing trailing LF")
# replace only that one line
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2367,"):
        parts.append(new_2367)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2367 replace count {replaced}")
new_rq = "".join(parts)
# append rq_2368
new_2368 = (
    "rq_2368,leftover dual after Sig — prefer AGB/FARO-YE2025/or leftover DIGOR / Mozaiek,hole_fill,8,open,L5,,"
    "After Sig YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel DIGOR 0870.833.435 deposit 2026-00205516 / Mozaiek 0415.272.935 deposit 2026-00206415 if live 2026pdf. "
    "Do NOT redo SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2367; leftover DIGOR / Mozaiek still unused; DCGZ 0411.917.131 empty-shell skip; next EVERY-10 2370\n"
)
new_rq = new_rq + new_2368
# write back only if prefix+suffix of file otherwise identical except target
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2367 + rq_2368; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2367,2367,no,"
    "tick2367 leftover dual Sig 0431.736.211 Strong PDF (omzet empty; code73 empty; bruto JUMP 864311 VKT envelope; pnl JUMP 13584 from loss; equity JUMP 680079; assets JUMP 891158; debt DROP 211080; FTE DROP 7.7; destin691 empty; kapitaalsubsidies empty; bestemde fondsen 109390; cash JUMP 722466; 1 VE RSZ2025 94.993); after Wegwijs@2366 same zetel; leftover DIGOR / Mozaiek; AGB/FARO/Gandae YE2024; next rq_2368; next EVERY-10 2370\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2367 - rq_2367 Sig vzw Aalst (bruto JUMP 0.86m / pnl JUMP from loss / 109k bestemde fondsen / Strong PDF)

- Unit: **rq_2367** leftover dual after **Wegwijs@2366**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Took FREE leftover Flemish **Sig VZW** YE2025 (KBO **0431.736.211**; zetel Kloosterstraat 6, 9031 Drongen — same seat as Ter Kouter + CAR Het Veer + 't Vlot + Stappie + Oostakker + Noordhoek + De Elfjes + De Steijgertjes + De Steijger + Kapelhof + TKDV Het Veer + Wegwijs; operational Pachthofstraat 1, 9308 Aalst VE **2.156.389.875**; **Actief** **1 VE**; RSZ2025 **94.993** / NACE **85.599**; leftover same-zetel dual of mined **Wegwijs@2366** / **TKDV Het Veer@2365** / **Kapelhof@2364** / **De Steijger@2363** / **De Steijgertjes@2362** / **De Elfjes@2361** / **Noordhoek@2360** / **Oostakker@2359** / **Stappie@2358** / **'t Vlot@2357** / **CAR Het Veer@2356** / **Ter Kouter@2355**; info@sig-net.be). Confirmed leftover public (inclusie-/vormings-VZW mensen met beperking + same-zetel public CAR cluster) not private clinic. Do not redo Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.
- Found: official NBB VKT-VZW PDF deposit **2026-00072461** (49763 B / 13p; AV **02.03.2026**; header **02.04.2026**) — omzet 70 **empty**; code 73 **empty**; bruto **EUR864311** JUMP +8.45% (VKT envelope); pnl **EUR13584** JUMP from loss −33266; equity **EUR680079** JUMP +2.04%; assets **EUR891158** JUMP +0.59%; debt **EUR211080** DROP −3.79%; FTE **7.7** DROP; kapitaalsubsidies **empty**; destin 691 **empty**; bestemde fondsen 13 **EUR109390**; cash **EUR722466** JUMP +0.88% (~84% bruto). Strong KBO + Strong PDF.
- Wrote: sources (+4); budgets (+9); commitments (+1); leaderboard (+1 pi 4.80); entities (+1 vzw_sig); foi + draft `{GAP}`; rq_2367=done + rq_2368 open; loop_state ticks=2367; raw tick2367/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2370**). Next: rq_2368 leftover same-zetel DIGOR 0870.833.435 deposit 2026-00205516 / Mozaiek 0415.272.935 deposit 2026-00206415 if live 2026pdf.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")

# persist stamp for commit message / verify
(DATA / "_tick2367_stamp.txt").write_text(STAMP + "\n", encoding="utf-8")
print("done")

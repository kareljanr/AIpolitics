# FOI draft — Stad+OCMW Lievegem JR2025 TLS / no downloadable PDF (GE residual)

**gap_id:** `gap_lvgm_jr2025_tls_nodownload_l5`  
**status:** ready (NOT sent)  
**entity:** Gemeente Lievegem + OCMW Lievegem — KBO 0697.609.152 / 0697.663.986  
**recipient:** College van burgemeester en schepenen Lievegem — financien@lievegem.be — Kasteeldreef 72 9920 Lievegem  
**sources:** [jaarrekeningen page](https://www.lievegem.be/bestuur/beleid/jaarrekening); [KBO GE 0697.609.152](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0697609152); [KBO OCMW 0697.663.986](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0697663986); [openbaarheid](https://www.lievegem.be/toegang-tot-bestuursdocumenten)  
**tick:** 1315

## Context (official page lists JR2025; PDF does not download)

- Leftover unmapped city GE after residual dual hunt. Official lievegem.be jaarrekeningen page (fetched 2026-08-17 via isolated fetch) **lists** `JR2025_beleidsrapport_Lievegem_GR 25.06.2026, gepubliceerd 26.06.2026` and `JR2025_documentatie_Lievegem_GR 25.06.2026, gepubliceerd 26.06.2026`. Direct HTTPS download from this environment fails with **TLS unexpected EOF** (HTTP 301 http→https then OpenSSL `UNEXPECTED_EOF_WHILE_READING`; same class as zorgbedrijfsinttruiden.be / vlaamsbrabant.be TLS). Guessed Drupal file URL also TLS-fails. Echo portal `lievegem-echo.cipalschaubroeck.be` HTTP 403. No primary euros extracted.
- KBO **0697.609.152** Gemeente Lievegem (actief; stad/gemeente sinds 01.06.2018; zetel Centrumstraat 42 9920 sinds 26.03.2026; 40 VE; algemeen directeur Kenneth Pauwels sinds 01.06.2024; NACE 84.114/84.120; aanbestedende overheid; slorpte Lovendegem 0207.452.712 / Waarschoot 0207.455.977 / Zomergem 0207.456.769 op 01.01.2019; geen KBO-financiën). KBO **0697.663.986** OCMW Lievegem (actief; zelfde zetel; 18 VE; zelfde AD; NACE 84.115; geen KBO-financiën). Financieel directeur Bart Kerkhof — financien@lievegem.be / 09 396 23 00. FOI-post: College CBS, Kasteeldreef 72, 9920 Lievegem.
- Hunt this tick (leftover cities): Londerzeel `/jaarrekeningen` HTTP 200 only JR2022 PDF (GR 2024/2025 mentioned, no JR2025 file); Holsbeek meeting.burger JR2024-only; Zwalm HLN 23.06.2026 approval, no official PDF, echo 403; Wortegem-Petegem no JR2025; Maarkedal official page JR2020–2024 only (press euros not used); Ranst official JR2024-only; Linkebeek JR2024-only; Kapellen beleidsdocumenten no JR PDF; Drogenbos/Boutersem bestuur 404; Stad+OCMW Maaseik still JR2024-only; Bierbeek JR2024-only; Moerbeke site redirects to Lokeren (already mined); Wachtebeke site redirects to Lochristi. AGB Bornem still JR2024-only; AGB De Kluize still unpublished. Already-mined skip: Ternat 1073/1124, Oostkamp 909/1131, Wetteren 1011/1231, Poperinge 864/1188, Haacht 933/934, Bilzen-Hoeselt 1149/1216, Geel 848/1175/1252, Zwevegem 972/973, AGB Sport Hulshout 1314, AGB Merchtem 1313, AGBIM/AGB Maaseik 1311–1312. NBB consult skipped (403/SPA). Belscope/Companyweb euros **niet** gebruikt.
- **EUR:** none sourced. Do not invent euros. Do not send without human OK.

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: College van burgemeester en schepenen
Gemeente Lievegem
t.a.v. de dienst openbaarheid van bestuur / dienst Financiën
Kasteeldreef 72
9920 Lievegem
financien@lievegem.be
cc: info@lievegem.be

Betreft: Verzoek om openbaarmaking van bestuursdocumenten —
jaarrekening 2025 Gemeente + OCMW Lievegem (KBO 0697.609.152 / 0697.663.986)

Geachte,

Op grond van het Bestuursdecreet (openbaarheid van bestuur) dien ik hierbij een verzoek in tot
openbaarmaking / inzage / afschrift van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. De volledige BBC-jaarrekening 2025 van het lokaal bestuur Lievegem
   (beleidsrapport / beleidsevaluatie, financiële nota J1–J5 of J1–J7,
   toelichting, documentatie), inclusief balans, staat van opbrengsten
   en kosten, budgettair resultaat, autofinancieringsmarge, financiële
   schulden, nieuwe leningen, tussenkomst gemeente–OCMW, toelagen,
   personeel/VTE, en de geconsolideerde GE+OCMW-cijfers.
2. De documentatiebundel bij de jaarrekening 2025
   (JR2025_documentatie_Lievegem zoals vermeld op de website).
3. Het besluit van de gemeenteraad van 25 juni 2026 tot vaststelling
   van de jaarrekening 2025 en het besluit van de raad voor
   maatschappelijk welzijn tot vaststelling van het OCMW-deel,
   met datum van bekendmaking.
4. Een werkende, publieke download-URL (of een digitale kopie per e-mail)
   van de PDF's die op https://www.lievegem.be/bestuur/beleid/jaarrekening
   als "JR2025_beleidsrapport_Lievegem_GR 25.06.2026, gepubliceerd 26.06.2026"
   en "JR2025_documentatie_Lievegem_GR 25.06.2026, gepubliceerd 26.06.2026"
   worden vermeld. Rechtstreekse HTTPS-download faalt hier met TLS unexpected EOF.
5. Een machineleesbare export (PDF + indien beschikbaar CSV/XLSX) van de
   J-schema's en T-tabellen 2025.

Periode: boekjaar 2025 en nog lopende verbintenissen 2026–2031.

### 2. Context (waarom)

Onderzoek naar overheidsuitgaven (transparantie van publieke middelen).
Hiërarchisch pad: Vlaanderen>Gemeenten>Lievegem>jr2025_L5.
Op 17 augustus 2026 vermeldt https://www.lievegem.be/bestuur/beleid/jaarrekening
de jaarrekening 2025 (GR 25.06.2026 / publicatie 26.06.2026), maar de PDF
is van deze omgeving niet downloadbaar (TLS unexpected EOF).

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail.
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: gap_lvgm_jr2025_tls_nodownload_l5

Met vriendelijke groet,

[Naam]
```

---

## Checklist vóór `ready`

- [x] Juiste instelling (Gemeente + OCMW Lievegem)  
- [x] Concrete documenten (BBC JR2025 beleidsrapport + documentatie + GR/RMW)  
- [x] Geen verzonnen eurobedragen  
- [x] Meerjarigheid expliciet gevraagd  
- [ ] Contactgegevens verzoeker (human)  
- [x] `foi_queue.csv` status=ready, NOT sent  

**Do not send without human OK.**

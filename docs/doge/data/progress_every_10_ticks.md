# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2750** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2740; 2741-2749 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2741-2749 residual dual L5 (not near-complete of 348bn):** Wit-Gele Kruis Oost-Vlaanderen (Gent) · Ferm Thuiszorg (Leuven) · Federatie Wit-Gele Kruis (Brussel) · Gezinszorg De Regenboog (Kruibeke) · Kribbe Bethlehem (Antwerpen) · Kribbe Sint-Jacob (Leuven) · Het Toverhuis (Kessel-Lo) · Hebe Kenniscentrum Kinderopvang (Wilrijk) · Dagcentrum Kasteel (Turnhout) (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2416** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2468** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2741-2749** Wit-Gele Kruis Oost-Vlaanderen (Gent) · Ferm Thuiszorg (Leuven) · Federatie Wit-Gele Kruis (Brussel) · Gezinszorg De Regenboog (Kruibeke) · Kribbe Bethlehem (Antwerpen) · Kribbe Sint-Jacob (Leuven) · Het Toverhuis (Kessel-Lo) · Hebe Kenniscentrum Kinderopvang (Wilrijk) · Dagcentrum Kasteel (Turnhout).

### Inventory (tick 2750)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57823 |
| commitments.csv | 6468 |
| leaderboard.csv | 8588 |
| entities.csv | 2487 |
| sources.csv | 8335 |
| FOI ready | 2416 |
| FOI total rows | 2468 |
| research_queue open | rq_2750 (carried; next: more NACE 88.911 childcare and 88.101 home-care VZWs outside the main cities; Perspectief Oostende needs projectvereniging handling) |

### What improved since tick 2740

- **New source (tick2741-2749):** Wit-Gele Kruis Oost-Vlaanderen (Gent) · Ferm Thuiszorg (Leuven) · Federatie Wit-Gele Kruis (Brussel) · Gezinszorg De Regenboog (Kruibeke) · Kribbe Bethlehem (Antwerpen) · Kribbe Sint-Jacob (Leuven) · Het Toverhuis (Kessel-Lo) · Hebe Kenniscentrum Kinderopvang (Wilrijk) · Dagcentrum Kasteel (Turnhout). Source: Wit-Gele Kruis list (witgelekruis.be), KBO name search (gezinszorg) and KBO NACE-BEL 88.101/88.911/88.993 activity searches. WGK Oost-Vlaanderen: scanned NBB PDF, OCR unreliable, so all used figures were read from the rendered PDF pages (write.py now accepts the m05-f-p model).
- **FOI addresses:** verified on opened official pages except **Ferm Thuiszorg** (thuiszorg@samenferm.be seen only on a third-party listing; samenferm.be is script-rendered; FOI row marked NEEDS VERIFICATION). Dagcentrum Kasteel uses its unit mailbox on theaterstap.be.
- **Runner note:** 2576-2750 ran on the local fallback runner (Actions last ticked 2575), from the fresh clone /workspace/AIpolitics-loop since 2681; toolkit persistent at /workspace/AIpolitics-loop-tk. Do not run both at once.
- **Rejected 2741-2749 (fast):** Perspectief Oostende (projectvereniging, not a VZW); Gezinszorg Ronse (only a named person's mailbox); Kinderdagverblijf De Ketjes (mailbox on site misspelt); Maan en Wolf (no own mailbox); Familiezorg, Familiezorg West-Vlaanderen (already in repo); Solidariteit voor het Gezin (no NBB deposits).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2740** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2730; 2731-2739 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2731-2739 residual dual L5 (not near-complete of 348bn):** Wit-Gele Kruis West-Vlaanderen (Brugge) · Wit-Gele Kruis Limburg (Genk) · Wit-Gele Kruis Antwerpen (Herentals) · Wit-Gele Kruis Vlaams-Brabant (Lubbeek) · Thuiszorg Vleminckveld (Antwerpen) · Liers Centrum voor Gezinszorg (Lier) · MSOC Vlaams-Brabant (Leuven) · Mariahof (Leuven) · Salvator Gezinszorg (Hasselt) (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2407** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2459** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2731-2739** Wit-Gele Kruis West-Vlaanderen (Brugge) · Wit-Gele Kruis Limburg (Genk) · Wit-Gele Kruis Antwerpen (Herentals) · Wit-Gele Kruis Vlaams-Brabant (Lubbeek) · Thuiszorg Vleminckveld (Antwerpen) · Liers Centrum voor Gezinszorg (Lier) · MSOC Vlaams-Brabant (Leuven) · Mariahof (Leuven) · Salvator Gezinszorg (Hasselt).

### Inventory (tick 2740)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57749 |
| commitments.csv | 6459 |
| leaderboard.csv | 8579 |
| entities.csv | 2478 |
| sources.csv | 8308 |
| FOI ready | 2407 |
| FOI total rows | 2459 |
| research_queue open | rq_2740 (carried; next: Wit-Gele Kruis Oost-Vlaanderen (scanned filing), WGK federation, Dagcentrum Kasteel, Perspectief Oostende) |

### What improved since tick 2730

- **New source (tick2731-2739):** Wit-Gele Kruis West-Vlaanderen (Brugge) · Wit-Gele Kruis Limburg (Genk) · Wit-Gele Kruis Antwerpen (Herentals) · Wit-Gele Kruis Vlaams-Brabant (Lubbeek) · Thuiszorg Vleminckveld (Antwerpen) · Liers Centrum voor Gezinszorg (Lier) · MSOC Vlaams-Brabant (Leuven) · Mariahof (Leuven) · Salvator Gezinszorg (Hasselt). Source: KBO NACE-BEL 88.101 (home care for the elderly), 88.991 (ambulant addiction care) and 87.302 (assistance flats) activity search by postcode, plus the provincial Wit-Gele Kruis associations listed with KBO numbers on witgelekruis.be/contacteer-ons.
- **FOI addresses:** each verified on an opened official page; general mailboxes except MSOC Vlaams-Brabant (Leuven seat mailbox; no organisation-wide box published). **Data fix tick 2731:** Ter Engelen FOI row and draft now info@hofterengelen.be (completes the tick-2721 entity fix).
- **Runner note:** 2576-2740 ran on the local fallback runner (Actions last ticked 2575), from the fresh clone /workspace/AIpolitics-loop since 2681; toolkit persistent at /workspace/AIpolitics-loop-tk. Do not run both at once.
- **Rejected 2731-2739 (fast):** Huis Vandecruys (BV); Participo CM, Thuiszorg Arbeid en Gezondheid, Thuiszorg H.Hart (no verified mailbox); Zusterkens der Armen Brussel (official contact page could not be opened; its 2025 profit EUR5.14m comes from EUR7.66m non-recurring operating income per the filing); Sociaal Centrum Lier (733 empty); Gandae, In-Z (already in repo); De Lochting (financial year ends 31-03-2026); Wit-Gele Kruis Oost-Vlaanderen (scanned -p filing, deferred).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2730** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2720; 2721-2729 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2721-2729 residual dual L5 (not near-complete of 348bn):** Tele-Onthaal (Brussel) · Centrum ter Preventie van Zelfdoding (Schaarbeek) · HOBO (Brussel) · PSC Open Huis (Antwerpen) · Partner in Assistentie zorg (Hasselt) · de Refuge (Gent) · Huis Sint-Jozef (Berchem) · Home Claire / Eau de Gand (Gent) · Westerlinde (Kortrijk/Roeselare) (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2398** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2450** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2721-2729** Tele-Onthaal (Brussel) · Centrum ter Preventie van Zelfdoding (Schaarbeek) · HOBO (Brussel) · PSC Open Huis (Antwerpen) · Partner in Assistentie zorg (Hasselt) · de Refuge (Gent) · Huis Sint-Jozef (Berchem) · Home Claire / Eau de Gand (Gent) · Westerlinde (Kortrijk/Roeselare).

### Inventory (tick 2730)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57672 |
| commitments.csv | 6450 |
| leaderboard.csv | 8570 |
| entities.csv | 2469 |
| sources.csv | 8281 |
| FOI ready | 2398 |
| FOI total rows | 2450 |
| research_queue open | rq_2730 (carried; next: Huis Vandecruys model check, Zusterkens der Armen Brussel, NACE 88.991/88.993 scan) |

### What improved since tick 2720

- **New source (tick2721-2729):** Tele-Onthaal (Brussel) · Centrum ter Preventie van Zelfdoding (Schaarbeek) · HOBO (Brussel) · PSC Open Huis (Antwerpen) · Partner in Assistentie zorg (Hasselt) · de Refuge (Gent) · Huis Sint-Jozef (Berchem) · Home Claire / Eau de Gand (Gent) · Westerlinde (Kortrijk/Roeselare). Source: KBO NACE-BEL 88.994 (general welfare work without accommodation) and 87.301 (rest homes) activity search by postcode. New write.py text options so welfare/WZC FOI drafts no longer use youth-care wording.
- **FOI addresses:** each verified on an opened official page; general mailboxes except Westerlinde (only a social-service mailbox published, flagged in its FOI note) and Eau de Gand (location mailbox). **Data fix tick 2721:** vzw_ter_engelen (Lokeren, KBO 0430.882.809) FOI address info@covida.be was wrong; now info@hofterengelen.be (verified on hofterengelen.be/contact).
- **Runner note:** 2576-2730 ran on the local fallback runner (Actions last ticked 2575), from the fresh clone /workspace/AIpolitics-loop since 2681; toolkit persistent at /workspace/AIpolitics-loop-tk. Do not run both at once.
- **Rejected 2721-2729 (fast):** Philippus Neri 0410.505.582 (property VZW, 0 FTE; the 2024 operating loss EUR20.99m is real per both the YE2024 and YE2025 filings: non-recurring operating costs EUR22.49m, nature not disclosed; no general mailbox); GPN Seniorenzorg Waasland (no general mailbox); BRAVVO (VOL, 733 empty); GSD-V (already gsd_vlaanderen); Huis Vandecruys (m81 model); De Lage Drempel (no YE2025 filing); Nottebohm Home (733 empty).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2720** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2710; 2711-2719 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2711-2719 residual dual L5 (not near-complete of 348bn):** Covida/Ter Engelen Tevona (Genk) · Ubuntu Achtkanter (Kortrijk) · KIDS (Hasselt) · Begeleidingscentrum autisme (Mechelen) · Ondo (Borgerhout) · PVT Valckeburg (Roeselare) · De Maanwandelaars (Hoboken) · Leef (Ranst) · Albe (Kapellen) (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2389** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2441** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2711-2719** Covida/Ter Engelen Tevona (Genk) · Ubuntu Achtkanter (Kortrijk) · KIDS (Hasselt) · Begeleidingscentrum autisme (Mechelen) · Ondo (Borgerhout) · PVT Valckeburg (Roeselare) · De Maanwandelaars (Hoboken) · Leef (Ranst) · Albe (Kapellen).

### Inventory (tick 2720)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57597 |
| commitments.csv | 6441 |
| leaderboard.csv | 8561 |
| entities.csv | 2460 |
| sources.csv | 8254 |
| FOI ready | 2389 |
| FOI total rows | 2441 |
| research_queue open | rq_2720 (carried; next: Philippus Neri 0410.505.582, then NACE 88.994 welzijnswerk and 87.301) |

### What improved since tick 2710

- **New source (tick2711-2719):** Covida/Ter Engelen Tevona (Genk) · Ubuntu Achtkanter (Kortrijk) · KIDS (Hasselt) · Begeleidingscentrum autisme (Mechelen) · Ondo (Borgerhout) · PVT Valckeburg (Roeselare) · De Maanwandelaars (Hoboken) · Leef (Ranst) · Albe (Kapellen). Source: KBO NACE-BEL 87.201/87.202/87.203 (residential care for persons with a disability / psychiatric problems) activity search by postcode.
- **FOI addresses:** all nine general organisation mailboxes, each verified on an opened official page (Ubuntu Achtkanter uses the Groep Ubuntu group mailbox; Covida's info@covida.be on terengelen.be is also used by existing entity vzw_ter_engelen, KBO 0430.882.809, a different Lokeren organisation; that row should be checked).
- **Runner note:** 2576-2720 ran on the local fallback runner (Actions last ticked 2575), from the fresh clone /workspace/AIpolitics-loop since 2681; toolkit persistent at /workspace/AIpolitics-loop-tk. Do not run both at once.
- **Rejected 2711-2719 (fast):** Ons Huis, Sint Oda, Escalante (no NBB filing); CJM Antwerpen (no YE2025 filing); Delacroix (precedent skip); De Kever (BV); VillaVip entities. Spare: Philippus Neri Sint-Niklaas (2024 operating loss 20.99m looks odd, verify first).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2710** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2700; 2701-2709 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2701-2709 residual dual L5 (not near-complete of 348bn):** Pleegzorg Provincie Antwerpen (Mechelen) · Pleegzorg Vlaams-Brabant en Brussel (Leuven) · Pleegzorg Limburg (Genk) · Pleegzorg Vlaanderen (Leuven) · Habbekrats Gent · Jongerenatelier Kortrijk · J@M Mechelen · Parcours Gent · Erat Leuven (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2380** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2432** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2701-2709** Pleegzorg Provincie Antwerpen (Mechelen) · Pleegzorg Vlaams-Brabant en Brussel (Leuven) · Pleegzorg Limburg (Genk) · Pleegzorg Vlaanderen (Leuven) · Habbekrats Gent · Jongerenatelier Kortrijk · J@M Mechelen · Parcours Gent · Erat Leuven.

### Inventory (tick 2710)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57519 |
| commitments.csv | 6432 |
| leaderboard.csv | 8552 |
| entities.csv | 2451 |
| sources.csv | 8227 |
| FOI ready | 2380 |
| FOI total rows | 2432 |
| research_queue open | rq_2710 (carried; next: other NACE 87/88 codes 87.202/87.203, 88.994; Pleegzorg West/Oost re-check) |

### What improved since tick 2700

- **New source (tick2701-2709):** Pleegzorg Provincie Antwerpen (Mechelen) · Pleegzorg Vlaams-Brabant en Brussel (Leuven) · Pleegzorg Limburg (Genk) · Pleegzorg Vlaanderen (Leuven) · Habbekrats Gent · Jongerenatelier Kortrijk · J@M Mechelen · Parcours Gent · Erat Leuven. Source: KBO NACE-BEL 88.992 (integrale jeugdhulp zonder huisvesting) activity search by postcode (pre-2025 code 87.901 no longer valid in KBO).
- **FOI addresses:** all nine general organisation mailboxes, each verified on an opened official page (J@M: info@jamvzw.be from its annual accounts published on mechelen.be; jamvzw.be shows no mailbox).
- **Runner note:** 2576-2710 ran on the local fallback runner (Actions last ticked 2575), from the fresh clone /workspace/AIpolitics-loop since 2681; toolkit persistent at /workspace/AIpolitics-loop-tk. Do not run both at once.
- **Rejected 2701-2709 (fast):** de mobil Leuven (tiny micro, shares Arktos address; contact mailbox is a live.be address); 't Pakhuus, Young Fenix, Yadelim Plus, Routes2Grow, Resett, Zwerfgoed (no NBB filing); Kwaito, RESET (micro BVs); De Kleine Vos (precedent skip); Brussels French-community AMO/ASBL hits out of scope.
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2700** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2690; 2691-2699 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2691-2699 residual dual L5 (not near-complete of 348bn):** Koninklijk Werk IBIS Bredene · Arcade Gistel · Begeleidingscentrum Bethanie Kortrijk · De Patio Brugge · De Cocon Gent · Jeugdzorg Nazareth-De Pinte · Lionshulp Gent · Martens-Sotteau Gent · Alba Herent (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2371** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2423** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2691-2699** Koninklijk Werk IBIS Bredene · Arcade Gistel · Begeleidingscentrum Bethanie Kortrijk · De Patio Brugge · De Cocon Gent · Jeugdzorg Nazareth-De Pinte · Lionshulp Gent · Martens-Sotteau Gent · Alba Herent.

### Inventory (tick 2700)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57444 |
| commitments.csv | 6423 |
| leaderboard.csv | 8543 |
| entities.csv | 2442 |
| sources.csv | 8200 |
| FOI ready | 2371 |
| FOI total rows | 2423 |
| research_queue open | rq_2700 (carried; OVBJ lists exhausted; next: KBO NACE 87/88 lists) |

### What improved since tick 2690

- **New source (tick2691-2699):** Koninklijk Werk IBIS Bredene · Arcade Gistel · Begeleidingscentrum Bethanie Kortrijk · De Patio Brugge · De Cocon Gent · Jeugdzorg Nazareth-De Pinte · Lionshulp Gent · Martens-Sotteau Gent · Alba Herent. Source: KBO-number re-check of all five Opgroeien OVBJ provincial lists. It found organisations that earlier name-matching had missed (IBIS was the queued lead).
- **FOI addresses:** all nine are general organisation mailboxes verified on an opened official page (Lionshulp: lions@lionshulp.be, the only general address on its homepage).
- **Runner note:** 2576-2700 ran on the local fallback runner (Actions last ticked 2575), from the fresh clone /workspace/AIpolitics-loop since 2681; toolkit now persistent at /workspace/AIpolitics-loop-tk. Do not run both at once.
- **Rejected 2691-2699 (fast):** Kompani Koksijde (VOL 733 empty, skip rule); NOVA Kortrijk (KBO 2025, no filing yet); GO! scholengroepen Inspira/Xplora/Impact (school groups, out of scope); Evara (already in repo).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2690** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2680; 2681-2689 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2681-2689 residual dual L5 (not near-complete of 348bn):** 't Spiegeltje Asse · Arktos Leuven · Cocon Vilvoorde · Eigen Kracht Centrale Kortenaken · Minor-Ndako & Juna Anderlecht · Radar Ternat · Sporen Leuven · Tonuso Anderlecht · Amber Bierbeek (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2362** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2414** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2681-2689** 't Spiegeltje Asse · Arktos Leuven · Cocon Vilvoorde · Eigen Kracht Centrale Kortenaken · Minor-Ndako & Juna Anderlecht · Radar Ternat · Sporen Leuven · Tonuso Anderlecht · Amber Bierbeek.

### Inventory (tick 2690)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57370 |
| commitments.csv | 6414 |
| leaderboard.csv | 8534 |
| entities.csv | 2433 |
| sources.csv | 8173 |
| FOI ready | 2362 |
| FOI total rows | 2414 |
| research_queue open | rq_2690 (carried; OVBJ Vlaams-Brabant/Brussel list finished; next: IBIS (verify mailbox), then KBO NACE 87/88 lists) |

### What improved since tick 2680

- **New source (tick2681-2689):** 't Spiegeltje Asse · Arktos Leuven · Cocon Vilvoorde · Eigen Kracht Centrale Kortenaken · Minor-Ndako & Juna Anderlecht · Radar Ternat · Sporen Leuven · Tonuso Anderlecht · Amber Bierbeek. Source: Opgroeien OVBJ Vlaams-Brabant/Brussel list (april 2026; re-fetched as a valid PDF at contactgegevens-ovbj-vlaams-brabant-brussel.pdf). All OVBJ provincial lists now used.
- **FOI addresses:** only addresses verified on an official page that could be opened. General mailboxes for Arktos, Eigen Kracht Centrale, Radar, Sporen, Tonuso, Amber. Named contacts (no general mailbox verifiable) for 't Spiegeltje (own site), Cocon (Opgroeien list; own site down) and Minor-Ndako (Opgroeien list; site has form only). Dageraad (tick2678) address now verified on dageraadvzw.be.
- **Runner note:** 2576-2690 ran on the local fallback runner (Actions last ticked 2575). From 2681 the runner uses a fresh clone (/workspace/AIpolitics-loop) after the old checkout was found reset. Do not run both at once.
- **Rejected 2681-2689 (fast):** CAW Brussel (already in repo); De Loper Anderlecht (no YE2025 deposit yet; latest YE2024); De Vogelzang Sint-Pieters-Woluwe (YE2025 near-dormant, 9900 negative; activity moved to Convento, already in repo); Adem, Alba, Cidar, MFC Combo, Monte Rosa, De Wissel, Huize Levenslust, Huize Levensruimte, Convento (already in repo).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2680** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2670; 2671-2679 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2671-2679 residual dual L5 (not near-complete of 348bn):** CAS Genk · YAR Vlaanderen Hasselt · Jongerenwerking Pieter Simenon Lommel · Huize Sint-Vincentius Halen · Jeugdzorgcentrum Maaseik · Daidalos Houthalen-Helchteren · Cirkant Turnhout · Dageraad Schilde · De Touter Antwerpen (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2353** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2405** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2671-2679** CAS Genk · YAR Vlaanderen Hasselt · Jongerenwerking Pieter Simenon Lommel · Huize Sint-Vincentius Halen · Jeugdzorgcentrum Maaseik · Daidalos Houthalen-Helchteren · Cirkant Turnhout · Dageraad Schilde · De Touter Antwerpen.

### Inventory (tick 2680)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57294 |
| commitments.csv | 6405 |
| leaderboard.csv | 8525 |
| entities.csv | 2424 |
| sources.csv | 8146 |
| FOI ready | 2353 |
| FOI total rows | 2405 |
| research_queue open | rq_2680 (carried; source = Opgroeien OVBJ provincial lists; next: OVBJ leftovers) |

### What improved since tick 2670

- **New source (tick2671-2679):** CAS Genk · YAR Vlaanderen Hasselt · Jongerenwerking Pieter Simenon Lommel · Huize Sint-Vincentius Halen · Jeugdzorgcentrum Maaseik · Daidalos Houthalen-Helchteren · Cirkant Turnhout · Dageraad Schilde · De Touter Antwerpen. Source: Opgroeien OVBJ Limburg list (finished) then OVBJ Antwerpen list (finished).
- **Runner note:** 2576-2680 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2671-2679 (fast):** none new; OVBJ Vlaams-Brabant/Brussel PDF could not be parsed (not a valid PDF on download).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2670** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2660; 2661-2669 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2661-2669 residual dual L5 (not near-complete of 348bn):** Binnenstad Brugge · Hof ter Welle Beveren · Nieuwland Brugge · De Loods Poperinge · Oranjehuis Kortrijk · Jongerenzorg Zuid-West-Vlaanderen Zwevegem · Mariahuis Alken · Ons Geluk Oostende · Golfbreker Veurne (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2344** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2396** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2661-2669** Binnenstad Brugge · Hof ter Welle Beveren · Nieuwland Brugge · De Loods Poperinge · Oranjehuis Kortrijk · Jongerenzorg Zuid-West-Vlaanderen Zwevegem · Mariahuis Alken · Ons Geluk Oostende · Golfbreker Veurne.

### Inventory (tick 2670)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57217 |
| commitments.csv | 6396 |
| leaderboard.csv | 8516 |
| entities.csv | 2415 |
| sources.csv | 8119 |
| FOI ready | 2344 |
| FOI total rows | 2396 |
| research_queue open | rq_2670 (carried; source = Opgroeien OVBJ provincial lists; next: OVBJ leftovers) |

### What improved since tick 2660

- **New source (tick2661-2669):** Binnenstad Brugge · Hof ter Welle Beveren · Nieuwland Brugge · De Loods Poperinge · Oranjehuis Kortrijk · Jongerenzorg Zuid-West-Vlaanderen Zwevegem · Mariahuis Alken · Ons Geluk Oostende · Golfbreker Veurne. Source: Opgroeien OVBJ provincial lists (mei 2026; W-Vl / O-Vl / Limburg), continued.
- **Runner note:** 2576-2670 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2661-2669 (fast):** Koninklijk Werk IBIS (mixed school + youth care; general mailbox unverified) · Daidalos (Opgroeien contact address truncated; parked) · OCMW / GO! entries (public).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2660** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2650; 2651-2659 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2651-2659 residual dual L5 (not near-complete of 348bn):** Jeugdzorg Ter Elst Duffel · DVC De Triangel Lievegem · De Kantel Brugge · Blij Leven Lievegem · De Wiekslag Alken · Steevliet Merelbeke-Melle · Spoor 56 Hamme · De Walhoeve Vleteren · Grienta Eeklo (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2335** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2387** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2651-2659** Jeugdzorg Ter Elst Duffel · DVC De Triangel Lievegem · De Kantel Brugge · Blij Leven Lievegem · De Wiekslag Alken · Steevliet Merelbeke-Melle · Spoor 56 Hamme · De Walhoeve Vleteren · Grienta Eeklo.

### Inventory (tick 2660)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57143 |
| commitments.csv | 6387 |
| leaderboard.csv | 8507 |
| entities.csv | 2406 |
| sources.csv | 8092 |
| FOI ready | 2335 |
| FOI total rows | 2387 |
| research_queue open | rq_2660 (carried; source = Opgroeien OVBJ provincial lists; next: OVBJ leftovers) |

### What improved since tick 2650

- **New source (tick2651-2659):** Jeugdzorg Ter Elst Duffel · DVC De Triangel Lievegem · De Kantel Brugge · Blij Leven Lievegem · De Wiekslag Alken · Steevliet Merelbeke-Melle · Spoor 56 Hamme · De Walhoeve Vleteren · Grienta Eeklo. Sources: Opgroeien OBC + GES+ lists (finished), then Opgroeien OVBJ provincial lists (mei 2026; started with O-Vl / W-Vl / Limburg).
- **Runner note:** 2576-2660 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2651-2659 (fast):** 16 OBC/GES+ providers already in repo · Stichting Delacroix (733 empty) · OVBJ entries run by OCMW / GO! scholengroepen (public, out of scope).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2650** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2640; 2641-2649 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2641-2649 residual dual L5 (not near-complete of 348bn):** OOOC Luein Lochristi · OOOC Elkeen Lommel · LIA Waasmunster · Kruislink Beerse · Kiosk Wommelgem · Elegast Antwerpen · XPLO Roeselare · Amon Zwalm · OOOC t Pasrel Schaarbeek (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2326** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2378** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2641-2649** OOOC Luein Lochristi · OOOC Elkeen Lommel · LIA Waasmunster · Kruislink Beerse · Kiosk Wommelgem · Elegast Antwerpen · XPLO Roeselare · Amon Zwalm · OOOC t Pasrel Schaarbeek.

### Inventory (tick 2650)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 57064 |
| commitments.csv | 6378 |
| leaderboard.csv | 8498 |
| entities.csv | 2397 |
| sources.csv | 8065 |
| FOI ready | 2326 |
| FOI total rows | 2378 |
| research_queue open | rq_2650 (carried; Opgroeien OOOC list finished; next: other Opgroeien jeugdhulp lists, then KBO NACE 87/88) |

### What improved since tick 2640

- **New source (tick2641-2649):** OOOC Luein Lochristi · OOOC Elkeen Lommel · LIA Waasmunster · Kruislink Beerse · Kiosk Wommelgem · Elegast Antwerpen · XPLO Roeselare · Amon Zwalm · OOOC t Pasrel Schaarbeek. Source: Opgroeien OOOC list (april 2026), now finished.
- **Runner note:** 2576-2650 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2641-2649 (fast):** Organisatie Broeders van Liefde (OOOC De Luwte; national umbrella, out of scope) · Emmaus / KiJoCo / De Patio units (already in repo).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2640** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2630; 2631-2639 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2631-2639 residual dual L5 (not near-complete of 348bn):** CKG Sint-Clara Brugge · Koraal Antwerpen · i-mens Gent · CIG De Zeshoek Lommel · CIG De Kiekenstraat Gent · CIG Convento Kraainem · CIG Nestel Kortrijk · OOOC Ter Heide Bonheiden · OOOC De Zandberg Jabbeke (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2317** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2369** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2631-2639** CKG Sint-Clara Brugge · Koraal Antwerpen · i-mens Gent · CIG De Zeshoek Lommel · CIG De Kiekenstraat Gent · CIG Convento Kraainem · CIG Nestel Kortrijk · OOOC Ter Heide Bonheiden · OOOC De Zandberg Jabbeke.

### Inventory (tick 2640)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56986 |
| commitments.csv | 6369 |
| leaderboard.csv | 8489 |
| entities.csv | 2388 |
| sources.csv | 8038 |
| FOI ready | 2317 |
| FOI total rows | 2369 |
| research_queue open | rq_2640 (carried; source = Opgroeien OOOC list; next: Luein, Elkeen, LIA, Kruislink, Kiosk, t Pasrel, Elegast, XPLO, Amon) |

### What improved since tick 2630

- **New source (tick2631-2639):** CKG Sint-Clara Brugge · Koraal Antwerpen · i-mens Gent · CIG De Zeshoek Lommel · CIG De Kiekenstraat Gent · CIG Convento Kraainem · CIG Nestel Kortrijk · OOOC Ter Heide Bonheiden · OOOC De Zandberg Jabbeke. Sources: Opgroeien CKG list (finished), Opgroeien CIG list (finished), then Opgroeien OOOC list (17 orgs).
- **Runner note:** 2576-2640 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2631-2639 (fast):** CKG Glorieux / OOOC Glorieux (hospital group vzw) · CKG Zorgbedrijf Antwerpen (public) · CKG Den Boomgaard (733 empty) · Het Open Poortje (subsidies booked as 732 legaten; parked) · CIG De Stobbe / Ter Loke / De Shelter / Ten Anker (already in repo).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2630** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2620; 2621-2629 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2621-2629 residual dual L5 (not near-complete of 348bn):** CLB Het Kompas Mechelen · CLB Noordwest-Brabant Asse · Vrije CLB Archipel Deinze · Vrij CLB Brabant Oost Aarschot · CKG Kapoentje Oostende · CKG De Stap Genk · CKG Molenberg Bilzen-Hoeselt · CKG Lentekind · CKG Kinderland (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2308** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2360** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2621-2629** CLB Het Kompas Mechelen · CLB Noordwest-Brabant Asse · Vrije CLB Archipel Deinze · Vrij CLB Brabant Oost Aarschot · CKG Kapoentje Oostende · CKG De Stap Genk · CKG Molenberg Bilzen-Hoeselt · CKG Lentekind · CKG Kinderland.

### Inventory (tick 2630)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56912 |
| commitments.csv | 6360 |
| leaderboard.csv | 8480 |
| entities.csv | 2379 |
| sources.csv | 8011 |
| FOI ready | 2308 |
| FOI total rows | 2360 |
| research_queue open | rq_2630 (carried; source = Opgroeien CKG list; next: remaining CKGs Sint-Clara, Den Boomgaard, Het Open Poortje, Koraal, i-mens) |

### What improved since tick 2620

- **New source (tick2621-2629):** CLB Het Kompas Mechelen · CLB Noordwest-Brabant Asse · Vrije CLB Archipel Deinze · Vrij CLB Brabant Oost Aarschot · CKG Kapoentje Oostende · CKG De Stap Genk · CKG Molenberg Bilzen-Hoeselt · CKG Lentekind · CKG Kinderland. Sources: Vrij CLB-netwerk (finished) then the Opgroeien list of centres for child care and family support (CKG, 18 orgs).
- **Runner note:** 2576-2630 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2621-2629 (fast):** Vrij CLB Kempen (run by school board, no separate KBO) · Vrij CLB Netwerk koepel (Schaarbeek) · VCLB West-Vlaanderen koepel (0 deposits) · CKG Betlehem (Emmaus) · CKG Don Bosco / Hummeltjes / De Schommel (already in repo) · De Kleine Vos (no subsidy line in filing).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2620** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2610; 2611-2619 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2611-2619 residual dual L5 (not near-complete of 348bn):** Cidar Kortenberg · Ter Wende-Espero Leuven · De Markgrave Antwerpen · Vrij CLB Limburg · Vrij CLB Regio Gent · Vrije CLB Westhoek-Houtland · CLB aan de Leie · Vrij CLB Anker · Vrij CLB De Havens (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2299** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2351** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2611-2619** Cidar Kortenberg · Ter Wende-Espero Leuven · De Markgrave Antwerpen · Vrij CLB Limburg · Vrij CLB Regio Gent · Vrije CLB Westhoek-Houtland · CLB aan de Leie · Vrij CLB Anker · Vrij CLB De Havens.

### Inventory (tick 2620)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56836 |
| commitments.csv | 6351 |
| leaderboard.csv | 8471 |
| entities.csv | 2370 |
| sources.csv | 7984 |
| FOI ready | 2299 |
| FOI total rows | 2351 |
| research_queue open | rq_2620 (carried; source = VAPH MDT list tid:1393 + Vrij CLB-netwerk; next: remaining Vrij CLBs (Kempen, Halle, Mechelen…), then KBO NACE 87/88) |

### What improved since tick 2610

- **New source (tick2611-2619):** Cidar Kortenberg · Ter Wende-Espero Leuven · De Markgrave Antwerpen · Vrij CLB Limburg · Vrij CLB Regio Gent · Vrije CLB Westhoek-Houtland · CLB aan de Leie · Vrij CLB Anker · Vrij CLB De Havens. Source = VAPH MDT list (tid:1393) non-hospital VZWs + Vrij CLB-netwerk (CLBs are VAPH-recognised MDTs).
- **Runner note:** 2576-2620 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2611-2619 (fast):** MDT-list hospitals/UZ/mutualities · IGL Ter Heide, Het Veer, Don Bosco De Waai, Overleie, De Kade, Bethanie, Oranje, Kompas, Integra (already in repo) · Sint-Oda (Stijn) · De Poolster (VGC public) · Sint-Gerardus (no NBB deposit) · Klief (hospital S-model) · Ludentia (OLO-Rotonde, in repo) · Vrij CLB Leuven / Antwerpen-Middengebied (tiny) · Vrij CLB Halle (unparseable).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2610** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2600; 2601-2609 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2601-2609 residual dual L5 (not near-complete of 348bn):** Huis in de Stad (Strong upgrade) · DOP Oost-Vlaanderen · DOP West-Vlaanderen · DOP Limburg · DOP Vlaams-Brabant en Brussel · KanNet · Bijstandsorganisatie Absoluut · Onafhankelijk Leven · WVA-Metgezel (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2290** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2342** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2601-2609** Huis in de Stad (Strong upgrade) · DOP Oost-Vlaanderen · DOP West-Vlaanderen · DOP Limburg · DOP Vlaams-Brabant en Brussel · KanNet · Bijstandsorganisatie Absoluut · Onafhankelijk Leven · WVA-Metgezel.

### Inventory (tick 2610)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56761 |
| commitments.csv | 6342 |
| leaderboard.csv | 8462 |
| entities.csv | 2361 |
| sources.csv | 7957 |
| FOI ready | 2290 |
| FOI total rows | 2342 |
| research_queue open | rq_2610 (carried; source = VAPH non-VZA type lists tid:1397/1400/1406/1399/1398; next Ludentia, Oranje Vrije Tijd, VOC Opstap (micro), Alin/Zoom need Brussels parent) |

### What improved since tick 2600

- **New source (tick2601-2609):** Huis in de Stad (Strong upgrade) · DOP Oost-Vlaanderen · DOP West-Vlaanderen · DOP Limburg · DOP Vlaams-Brabant en Brussel · KanNet · Bijstandsorganisatie Absoluut · Onafhankelijk Leven · WVA-Metgezel. Source switch recorded in loop_log tick 2601: VAPH adreslijst type 1389 exhausted → Huis in de Stad Strong upgrade → VAPH non-VZA type lists (DOP tid:1397, bijstand tid:1400, gebruikersvereniging tid:1406, vrijetijdszorg tid:1399).
- **Runner note:** 2576-2610 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2601-2609 (fast):** DOP Provincie Antwerpen (already in repo) · Fovig / Gezin en Handicap / Hersenletsel Liga (0 NBB deposits) · Dito (already in repo) · Alin (Sint-Joost) / Zoom (Schaarbeek) (no mined Brussels-commune parent) · Kompas Wondelgem / Integra Hasselt (already in repo, Strong) · VOC Opstap Roeselare (micro model) · Ampel (CGG-linked).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2600** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2590; 2591-2599 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2591-2599 residual dual L5 (not near-complete of 348bn):** Start West-Vlaanderen · t Prieeltje · MPC Terbank · Tikvatenoe · Unie-K · Widar · Tanderuis · Zonnehoeve / Living+ · Ritmica Thuishaven (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2281** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2333** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2591-2599** Start West-Vlaanderen · t Prieeltje · MPC Terbank · Tikvatenoe · Unie-K · Widar · Tanderuis · Zonnehoeve / Living+ · Ritmica Thuishaven.

### Inventory (tick 2600)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56688 |
| commitments.csv | 6333 |
| leaderboard.csv | 8453 |
| entities.csv | 2353 |
| sources.csv | 7930 |
| FOI ready | 2281 |
| FOI total rows | 2333 |
| research_queue open | rq_2600 (carried; VAPH adreslijst scanned to last page 62 — next: new candidate source) |

### What improved since tick 2590

- **Residual dual (tick2591-2599):** Start West-Vlaanderen · t Prieeltje · MPC Terbank · Tikvatenoe · Unie-K · Widar · Tanderuis · Zonnehoeve / Living+ · Ritmica Thuishaven. Largest: Unie-K Brugge 733 **EUR38.33m**; MPC Terbank Leuven 733 **EUR12.05m**; Zonnehoeve / Living+ Nazareth 733 **EUR11.99m**.
- **Runner note:** 2576-2600 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2591-2599 (fast):** Voluntas Merksem (0 NBB deposits) · Komoo Leopoldsburg (founded 2025) · Woonondersteuning Vlaanderen Gavere (YE2024 latest; serviceflats) · Woon- en Zorgresidentie PURA Maarkedal (no mined parent city; VKT without subsidy split) · Vereniging Ons Huis Brugge (no KBO found; possibly Mintus-linked) · 't Weyerke (Stijn) · VillaVip sites · Bindkracht (already in repo). Note: Tanderuis parent set to city_merelbeke_melle (Melle merged 2025).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2590** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2580; 2581-2589 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2581-2589 residual dual L5 (not near-complete of 348bn):** Het Raster · Levedale · KOCA · Mariënstede · Mobilant · Raakzaam · Samenpunt · Primavera · Ter Muiden en t Veldzicht (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2272** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2324** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2581-2589** Het Raster · Levedale · KOCA · Mariënstede · Mobilant · Raakzaam · Samenpunt · Primavera · Ter Muiden en t Veldzicht.

### Inventory (tick 2590)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56609 |
| commitments.csv | 6324 |
| leaderboard.csv | 8444 |
| entities.csv | 2344 |
| sources.csv | 7903 |
| FOI ready | 2272 |
| FOI total rows | 2324 |
| research_queue open | rq_2590 (carried; VAPH list pages 52+ / Start West-Vlaanderen / 't Prieeltje) |

### What improved since tick 2580

- **Residual dual (tick2581-2589):** Het Raster · Levedale · KOCA · Mariënstede · Mobilant · Raakzaam · Samenpunt · Primavera · Ter Muiden en t Veldzicht. Largest: KOCA Antwerpen 733 **EUR20.94m**; Raakzaam Sint-Niklaas 733 **EUR14.48m**; Het Raster Antwerpen 733 **EUR9.96m**.
- **Runner note:** 2576-2590 ran on the local fallback runner (Actions last ticked 2575). Do not run both at once.
- **Rejected 2581-2589 (fast):** Resonans Zaventem (YE2024 latest) · Leefboerderij De Kanteling Herzele (YE2018) · MFC Odisam Deinze (0 deposits) · Madee / MFC Zonnebos (GO! public) · Huize Terloo / Clara Fey / De Beweging / Ebergiste / Sint-Ferdinand / Styrka / Sint-Gregorius / KI Woluwe (Evara/BvL VE) · 't Weyerke (Stijn) · already in repo: Huis in de Stad (Strong-PDF upgrade candidate 2026-00217681), IZW, OLO-Rotonde, MPC Sint-Franciscus, Woon en Zorg H. Hart.
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2580** (2026-10-12; local fallback runner while GitHub Actions cron is unreliable)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2570; 2571-2579 residual dual is L5 depth, not new L2 mass |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2571-2579 residual dual L5 (not near-complete of 348bn):** Nethedal · Levenslust · De Ark Moerkerke-Brugge · Klim · Mekanders · De Klaproos · De Vijver · De Kerselaar · De Karrekol (all Strong official NBB YE2025 PDFs) |
| **E. FOI-ready gaps** | **2263** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2315** (~14 legacy malformed status rows still untouched) |

**Off-TE (do not mix into 348 bn):** VAPH/maatwerk/CAR dual shells incl. **NEW 2571-2579** Nethedal · Levenslust · De Ark Moerkerke-Brugge · Klim · Mekanders · De Klaproos · De Vijver · De Kerselaar · De Karrekol.

### Inventory (tick 2580)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56532 |
| commitments.csv | 6315 |
| leaderboard.csv | 8435 |
| entities.csv | 2335 |
| sources.csv | 7876 |
| FOI ready | 2263 |
| FOI total rows | 2315 |
| research_queue open | rq_2580 (carried; CJMIB Antwerpen 0415.343.805 stalled YE2024-only) |

### What improved since tick 2570

- **Residual dual (tick2571-2579):** Nethedal · Levenslust · De Ark Moerkerke-Brugge · Klim · Mekanders · De Klaproos · De Vijver · De Kerselaar · De Karrekol. Largest: De Vijver Deurne 733 **EUR22.98m**; Mekanders Turnhout 70/76A **EUR13.90m**; Levenslust Lennik 733 **EUR13.20m**.
- **Runner note:** tick 2575 ran on GitHub Actions; 2576-2580 ran on the local fallback runner (Actions cron not firing reliably). Do not run both at once.
- **Rejected this tick (fast):** CJMIB Antwerpen (YE2024 latest deposit) · De Beerbos / De Beukheuvel / De Ark van Pollare (groenezorg) · Sint-Oda Pelt / De Klimroos Pelt (Stijn VE) · DVC Zevenbergen (Emmaüs VE).
- **Top10:** stable; #1 GIP ~EUR2.5bn pi 8.7.

---

## Snapshot at **tick 2570** (2026-10-12; loop resumed after human pause 2026-08-29 → 2026-10-12)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2560; residual dual 2561-2570 is L5 depth, not new L2 mass; AGB Bornem / FARO / AIESH still YE2024 stalls (not rechecked this tick) |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2561-2570 residual dual L5 (not near-complete of 348bn):** Berkenhof · Licht en Liefde Heem · Kerckstede · De Berken · Duinhelm · Vondels · Oikonde · Emiliani · Hoito · EVERY-10 primary **Het Balanske Tielt-Winge 73 JUMP 1.61m / debt JUMP 2.31m / 9901 DROP 12k** (Strong official NBB PDF 2026-00206974) |
| **E. FOI-ready gaps** | **2254** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2306** (status column has ~14 legacy malformed rows — data-quality debt, not touched) |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie/CIK shells** (**NEW 2561-2570** Berkenhof · Licht en Liefde Heem · Kerckstede · De Berken · Duinhelm · Vondels · Oikonde · Emiliani · Hoito · **Het Balanske**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2570)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56440 |
| commitments.csv | 6306 |
| leaderboard.csv | 8426 |
| entities.csv | 2326 |
| sources.csv | 7848 |
| FOI ready | 2254 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | 2306 |
| research_queue open | rq_2571 after Het Balanske Tielt-Winge EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2560 / last file refresh 2560

- **Residual dual (tick2561-2570):** leftover public VAPH **Berkenhof Leopoldsburg / Licht en Liefde Heem Jabbeke / Kerckstede Staden / De Berken Overijse / Duinhelm Oostende / Vondels Ieper / Oikonde Mechelen / Emiliani Lokeren (70/76A 22.02m) / Hoito Tienen** · EVERY-10 primary **Het Balanske Tielt-Winge** (KBO 0448.595.801; VKT-VZW YE2025: 73 **1.61m** JUMP +11.4% / bruto 9900 **1.27m** / 62 **1.15m** JUMP +18.1% / 9901 DROP to **12k** / debt 17/49 JUMP **2.31m** (+193%; overige leningen 174/0 **1.64m** new) / aanbouw **1.36m** + capex **1.24m** = new Villa84 woonproject Diest (2nd VE since 23.01.2026) / cash **1.28m** / FTE 17,9; Strong official NBB PDF; FOI ready on subsidy split + lender terms).
- **Pause note:** 2026-08-29 → 2026-10-12 human pause; no ticks in between. New YE2025 deposits may now exist for earlier 0-deposit / YE2024-only skips (VillaVip, Aalternatief, De Beukheuvel, OpWeg, Nethedal, Levenslust …) — recheck queued in rq_2571.
- **Rejected this tick (fast):** Eyckenborgh Gooik 0434.019.372 (WZC / Gravenkasteel inrichtende macht, not VAPH) · Zwart Goor Merksplas (Klavier = Emmaüs 0411.515.075, zetel Mechelen, leftover-via-VE) · CDN staatsbladmonitor timeouts → official NBB broker PDF endpoint used.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · Bethanië Genk SCAN/OCR · leftover groenezorg deferred · leftover-via-VE parents · city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING.

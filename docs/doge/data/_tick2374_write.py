#!/usr/bin/env python3
"""Surgical tick 2374 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_inkendaal"
SRC_PDF = "src_inkendaal_jr2025_nbb_pdf_2374"
SRC_KBO = "src_inkendaal_kbo_2374"
SRC_SBM = "src_inkendaal_sbm_2374"
SRC_SITE = "src_inkendaal_site_2374"
COMM = "comm_inkendaal_jr2025_statutory_omzet_43_55m_bfm_29_44m"
LB = "lb_inkendaal_omzet_43_55m_pnl_drop_jr2025"
GAP = "gap_inkendaal_bfm_riziv_school_matrix_omzet_43_55m_pnl_drop_6_11m_kapitaalsubsidies_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"
if not (ROOT / DRAFT).is_file():
    raise SystemExit("FOI draft missing")


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
    f"{SRC_PDF},NBB hospital-schema VOL-VZW jaarrekening 2025 Inkendaal vzw deposit 2026-00277815,http://cdn.staatsbladmonitor.be/2026pdf/2026-00277815.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2374; official scanned PDF 27804988 bytes 34p S-vzw 26.0.15 m140-f-p hospital KB 19 juni 2007; header 09.07.2026; AV 29.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-29; CreationDate 2026-07-09 13:36:21 UTC Foxit + OpenPDF 1.3.26; euros OCR from official PDF pages not SBM table",
    f"{SRC_KBO},KBO Revalidatieziekenhuis Inkendaal-Koninklijke Instelling vzw 0410.392.647,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410392647,KBO Public Search FOD Economie,{DAY},official_register,tick2374; Actief; 3 VE; zetel Inkendaalstraat 1 1602 Sint-Pieters-Leeuw since 01.10.1990; Aanbestedende overheid since 01.01.1924; RSZ2025 86.103; voorzitter Poullet Yves since 27.06.2022; dagelijks bestuur Blancquaert Sofie since 09.01.2015; replaces 0410.499.149 closed 26.09.2013",
    f"{SRC_SBM},Staatsbladmonitor fiche Inkendaal vzw 0410392647 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410392647,Staatsbladmonitor,{DAY},official_register,tick2374; deposit-id 2026-00277815 and CDN Last-Modified 2026-07-29; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Inkendaal vzw FOI contact / revalidatieziekenhuis + school,https://www.inkendaal.be/,Revalidatieziekenhuis Inkendaal vzw,{DAY},foi_contact,tick2374; FOI info@inkendaal.be; zetel Inkendaalstraat 1 1602 Vlezenbeek (Sint-Pieters-Leeuw); leftover city_sint_pieters_leeuw@1066; NOT Kloosterstraat 6; NOT Sint-Lievenspoort",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},Revalidatieziekenhuis Inkendaal-Koninklijke Instelling VZW (Vlezenbeek / specialized rehab hospital + school),Inkendaal ASBL (Vlezenbeek / hopital de reeducation + ecole),Inkendaal VZW (Vlezenbeek / specialized rehab hospital + school),parastatal,city_sint_pieters_leeuw,nl,https://www.inkendaal.be/,info@inkendaal.be,"Inkendaalstraat 1, 1602 Vlezenbeek (Sint-Pieters-Leeuw)",tick2374 YE2025 Strong official scanned NBB PDF deposit 2026-00277815 + Strong KBO 0410.392.647 Actief 3 VE Aanbestedende RSZ2025 86.103; omzet JUMP 43545639 BFM-inclusive hospital envelope; BFM 29444046; RIZIV 3652381; opbr 70/74 JUMP 46965368; pnl DROP 26399; equity DROP 31830373; assets DROP 47957505; debt JUMP 15827132; FTE 348.20; kapitaalsubsidies DROP 6112555; destin691 112377; cash DROP 6725035; leftover city_sint_pieters_leeuw@1066; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+10) — envelope = omzet 70 (BFM-inclusive hospital, not commercial-only)
append_lines(DATA / "budgets.csv", [
    f"bud_inkendaal_omzet_jr2025_statutory,{EID},2025,43545639,43545639,43545639,NBB hospital VOL-VZW code 70 omzet YE2025 JUMP +1.50% (primary L5 envelope; BFM-inclusive not commercial-only),{SRC_PDF},strong,tick2374; PDF p5 OCR; YE2024 42902910; BFM 700 29444046; RIZIV 703 3652381",
    f"bud_inkendaal_opbr_jr2025_statutory,{EID},2025,46965368,46965368,46965368,NBB hospital VOL-VZW code 70/74 bedrijfsopbrengsten YE2025 JUMP +2.03%,{SRC_PDF},strong,tick2374; PDF p5 OCR; YE2024 46030711; andere 74 3419729",
    f"bud_inkendaal_bfm_jr2025_statutory,{EID},2025,29444046,29444046,29444046,NBB hospital VOL-VZW code 700 Budget van Financiele Middelen YE2025 JUMP +1.06%,{SRC_PDF},strong,tick2374; PDF p5 OCR; YE2024 29135546; RIZIV 703 3652381 vs YE2024 3607506",
    f"bud_inkendaal_pnl_jr2025_statutory,{EID},2025,26399,26399,26399,NBB hospital VOL-VZW code 70/66 winst van het boekjaar YE2025 DROP -97.86%,{SRC_PDF},strong,tick2374; PDF p6 OCR; YE2024 1232231; bedrijfsverlies 445174; destin691/2 112377",
    f"bud_inkendaal_equity_jr2025_statutory,{EID},2025,31830373,31830373,31830373,NBB hospital VOL-VZW code 10/15 eigen vermogen YE2025 DROP -1.63%,{SRC_PDF},strong,tick2374; PDF p4 OCR; YE2024 32356255; kapitaalsubsidies 6112555; reserves 23495082",
    f"bud_inkendaal_assets_jr2025_statutory,{EID},2025,47957505,47957505,47957505,NBB hospital VOL-VZW code 20/58 totaal activa YE2025 DROP -0.28%,{SRC_PDF},strong,tick2374; PDF p3 OCR; YE2024 48094244",
    f"bud_inkendaal_debt_jr2025_statutory,{EID},2025,15827132,15827132,15827132,NBB hospital VOL-VZW code 17/49 schulden incl accruals YE2025 JUMP +2.52%,{SRC_PDF},strong,tick2374; PDF p4 OCR; YE2024 15437989; LT 2397366; ST 12783351; overlopende 646415",
    f"bud_inkendaal_cash_jr2025_statutory,{EID},2025,6725035,6725035,6725035,NBB hospital VOL-VZW code 54/58 liquide middelen YE2025 DROP -0.62%,{SRC_PDF},strong,tick2374; PDF p3 OCR; YE2024 6766911; geldbeleggingen 51/53 13067599",
    f"bud_inkendaal_kapitaalsubsidies_jr2025_statutory,{EID},2025,6112555,6112555,6112555,NBB hospital VOL-VZW code 15 investeringssubsidies YE2025 DROP -8.29%,{SRC_PDF},strong,tick2374; PDF p4 OCR; YE2024 6664836",
    f"bud_inkendaal_fte_jr2025_statutory,{EID},2025,348.20,348.20,348.20,NBB hospital VOL-VZW gemiddeld personeelsbestand VTE YE2025 348.20,{SRC_PDF},strong,tick2374; PDF p10 OCR; personnel 62 28463175 JUMP +5.31% vs YE2024 27028341; destin691/2 112377",
])

# commitments (+1)
cash_json = (
    '"{""2025_omzet"":43545639,""2025_opbr"":46965368,""2025_bfm700"":29444046,""2025_riziv703"":3652381,'
    '""2025_pnl"":26399,""2025_equity"":31830373,""2025_assets"":47957505,""2025_debt"":15827132,'
    '""2025_fte"":348.20,""2025_kapitaalsubsidies"":6112555,""2025_destin691"":112377,'
    '""2025_cash"":6725035,""2025_geldbeleggingen"":13067599,""2025_personnel62"":28463175,'
    '""2025_gebouwen22"":15162839,""2025_bedrijfsverlies"":445174,""2025_fin75"":962172,'
    '""2024_omzet"":42902910,""2024_opbr"":46030711,""2024_bfm700"":29135546,""2024_riziv703"":3607506,'
    '""2024_pnl"":1232231,""2024_equity"":32356255,""2024_assets"":48094244,""2024_debt"":15437989,'
    '""2024_kapitaalsubsidies"":6664836,""2024_destin691"":1197559,""2024_cash"":6766911,'
    '""2024_personnel62"":27028341}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Inkendaal vzw YE2025 (omzet 43.55m / BFM 29.44m / pnl DROP 26k / 6.11m kapitaalsubsidies / Strong PDF),{EID},FOD Volksgezondheid BFM + RIZIV rehab + leftover city_sint_pieters_leeuw,VZW Revalidatieziekenhuis Inkendaal-Koninklijke Instelling (KBO 0410.392.647; Actief; 3 VE; Aanbestedende; RSZ2025 86.103),2026-07-09,2025,2025,43545639,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00277815.pdf,Public specialized rehab hospital + school dual of mined city_sint_pieters_leeuw,Publish BFM/RIZIV/school matrix inside omzet 43.55m + 6.11m kapitaalsubsidies vs pnl DROP 26k,{SRC_PDF},strong,Vlaanderen>Vlaams_Brabant>Sint_Pieters_Leeuw>Inkendaal>JR2025_statutory_L5,tick2374; Strong official scanned PDF OCR; leftover city_sint_pieters_leeuw@1066; NOT Kloosterstraat 6; NOT Sint-Lievenspoort; not TE-additive",
])

# leaderboard (+1) pi = 0.4*6.4 + 0.4*7.4 + 0.2*5.0 = 6.52
append_lines(DATA / "leaderboard.csv", [
    f"{LB},Inkendaal omzet 43.55m / BFM 29.44m / pnl DROP 26k (YE2025 rehab hospital + school SPL),L5,rehab_hospital_school_vzw_statutory,Vlaanderen>Vlaams_Brabant>Sint_Pieters_Leeuw>Inkendaal>JR2025,43545639,43545639,PDF omzet JUMP 43545639 BFM-inclusive; BFM 29444046; RIZIV 3652381; opbr JUMP 46965368; pnl DROP 26399; equity DROP 31830373; assets DROP 47957505; debt JUMP 15827132; FTE 348.20; kapitaalsubsidies DROP 6112555; destin691 112377; cash DROP 6725035; geldbeleggingen 13067599; gebouwen 15162839; personnel JUMP 28463175,strong,{SRC_PDF},children + adults in specialized rehab Vlezenbeek (hospital + school),FOD Volksgezondheid BFM + RIZIV + leftover city_sint_pieters_leeuw,43.55m hospital omzet incl 29.44m BFM; pnl collapse 1.23m to 26k; 6.11m kapitaalsubsidies; 13.07m investments + 6.73m cash; leftover city_sint_pieters_leeuw,6.4,7.4,5,6.52,FOI BFM/RIZIV/school matrix + 6.11m kapitaalsubsidies + pnl DROP 26k + dual hospital/school,active,,tick2374; Strong official NBB scanned PDF OCR + Strong KBO; leftover city_sint_pieters_leeuw@1066; OFF Drongen",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Vlaams_Brabant>Sint_Pieters_Leeuw>Inkendaal>BFM_RIZIV_school,vzw_inkendaal,BFM/RIZIV/school split inside omzet 43545639 + BFM 29444046 + RIZIV 3652381; nature of kapitaalsubsidies 6112555 DROP and pnl DROP 26399; destin 691/2 112377; dual hospital+school,Strong official PDF leftover public rehab hospital of city_sint_pieters_leeuw@1066; 43.55m omzet; 29.44m BFM; pnl collapse; public not private clinic,8,Revalidatieziekenhuis Inkendaal-Koninklijke Instelling VZW / Yves Poullet voorzitter RvB,info@inkendaal.be,"Inkendaalstraat 1, 1602 Vlezenbeek (Sint-Pieters-Leeuw)",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2374; ready NOT sent; Strong official scanned NBB PDF OCR; after Sint-Lievenspoort@2373; leftover city_sint_pieters_leeuw hospital off Drongen; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2374 + append rq_2375 only
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2374,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2374 line, found {n}")
if "rq_2375," in rq_text:
    raise SystemExit("rq_2375 already exists")

new_2374 = (
    "rq_2374,leftover dual — Inkendaal YE2025 Strong (omzet JUMP 43.55m / BFM 29.44m / pnl DROP 26k),"
    "hole_fill,8,done,L5,vzw_inkendaal,"
    "Tick 2374 leftover after Sint-Lievenspoort. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort). "
    "Took Inkendaal 0410.392.647 deposit 2026-00277815 leftover city_sint_pieters_leeuw@1066. "
    "Do NOT redo Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T22:30:13Z,{STAMP},"
    "tick2374 Inkendaal 0410.392.647 YE2025 Strong official scanned PDF 2026-00277815; omzet JUMP 43545639 BFM-inclusive; BFM 29444046; RIZIV 3652381; opbr JUMP 46965368; pnl DROP 26399; equity DROP 31830373; assets DROP 47957505; debt JUMP 15827132; FTE 348.20; kapitaalsubsidies DROP 6112555; cash DROP 6725035; FOI ready NOT sent; leftover city_sint_pieters_leeuw@1066; OFF Drongen\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2374,"):
        parts.append(new_2374)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2374 replace count {replaced}")
new_rq = "".join(parts)
new_2375 = (
    "rq_2375,leftover dual after Inkendaal — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Inkendaal YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal). "
    "Do NOT redo Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2374; Inkendaal taken leftover city_sint_pieters_leeuw; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2375
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2374 + rq_2375; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2374,2374,no,"
    "tick2374 leftover dual Inkendaal 0410.392.647 Strong scanned PDF (omzet JUMP 43545639 BFM-inclusive; BFM 29444046; RIZIV 3652381; opbr JUMP 46965368; pnl DROP 26399; equity DROP 31830373; assets DROP 47957505; debt JUMP 15827132; FTE 348.20; kapitaalsubsidies DROP 6112555; destin691 112377; cash DROP 6725035; 3 VE Aanbestedende RSZ2025 86.103); leftover city_sint_pieters_leeuw@1066; OFF Drongen; AGB/FARO/Gandae YE2024; next rq_2375; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append (NOT every-10)
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2374 - rq_2374 Inkendaal Vlezenbeek (omzet JUMP 43.55m / BFM 29.44m / pnl DROP 26k / Strong PDF)

- Unit: **rq_2374** leftover dual after **Sint-Lievenspoort@2373**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Revalidatieziekenhuis Inkendaal-Koninklijke Instelling VZW** YE2025 (KBO **0410.392.647**; zetel Inkendaalstraat 1, 1602 Sint-Pieters-Leeuw / Vlezenbeek; **Actief** **3 VE**; **Aanbestedende overheid**; RSZ2025 **86.103**; leftover of mined **city_sint_pieters_leeuw@1066**; info@inkendaal.be). Confirmed leftover public (RIZIV/FOD BFM specialized rehab hospital + school under hospital schema KB 19 juni 2007) not private clinic. Do not redo Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB hospital-schema VOL-VZW scanned PDF deposit **2026-00277815** (27804988 B / 34p; AV **29.06.2026**; header **09.07.2026**; CDN Last-Modified **29.07.2026**) — omzet 70 **EUR43545639** JUMP +1.50% (BFM-inclusive hospital envelope); BFM 700 **EUR29444046**; RIZIV 703 **EUR3652381**; bedrijfsopbrengsten 70/74 **EUR46965368** JUMP +2.03%; pnl **EUR26399** DROP −97.86%; equity **EUR31830373** DROP −1.63%; assets **EUR47957505** DROP −0.28%; debt **EUR15827132** JUMP +2.52%; FTE **348.20**; kapitaalsubsidies **EUR6112555** DROP −8.29%; destin 691/2 **EUR112377**; cash **EUR6725035** DROP −0.62%; geldbeleggingen **EUR13067599**; gebouwen **EUR15162839**; personeel 62 **EUR28463175** JUMP +5.31%. Strong KBO + Strong PDF (OCR of official scan; not SBM table).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 6.52); entities (+1 vzw_inkendaal); foi + draft `{GAP}`; rq_2374=done + rq_2375 open; loop_state ticks=2374; raw tick2374/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380**). Next: rq_2375 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6).

"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")

#!/usr/bin/env python3
"""Surgical tick 2372 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_car_buggenhout"
SRC_PDF = "src_car_buggenhout_jr2025_nbb_pdf_2372"
SRC_KBO = "src_car_buggenhout_kbo_2372"
SRC_SBM = "src_car_buggenhout_sbm_2372"
SRC_SITE = "src_car_buggenhout_site_2372"
COMM = "comm_car_buggenhout_jr2025_statutory_omzet_2_65m_640k_destin_jump"
LB = "lb_car_buggenhout_omzet_2_65m_640k_destin_jump_jr2025"
GAP = "gap_car_buggenhout_riziv_vl_matrix_2_65m_omzet_640k_destin_655k_kapitaalsubsidies_car_l5"
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
    f"{SRC_PDF},NBB WVV VKT-VZW jaarrekening 2025 Revalidatiecentrum Buggenhout vzw deposit 2026-00205237,http://cdn.staatsbladmonitor.be/2026pdf/2026-00205237.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2372; official PDF 48084 bytes 12p VKT-VZW 26.0.15 m04-f; header 24.06.2026; AV 22.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-10; CreationDate 2026-06-26 23:30:55 UTC OpenPDF 1.3.26; euros extracted from PDF text not SBM table",
    f"{SRC_KBO},KBO Revalidatiecentrum Buggenhout vzw 0412.404.903,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412404903,KBO Public Search FOD Economie,{DAY},official_register,tick2372; Actief; 1 VE 2.153.792.057 Kloosterstraat 6 9031 Gent since 31.05.2006; zetel Kloosterstraat 6 9031 Gent/Drongen since 06.05.1996; RSZ2025 86.959; voorzitter Singelee Stefaan; dagelijks bestuur Vanvolsem Pieter",
    f"{SRC_SBM},Staatsbladmonitor fiche Revalidatiecentrum Buggenhout vzw 0412404903 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0412404903,Staatsbladmonitor,{DAY},official_register,tick2372; deposit-id 2026-00205237 and CDN Last-Modified 2026-07-10; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Buggenhout vzw FOI contact / RIZIV CAR Buggenhout,https://www.car-buggenhout.be/,Revalidatiecentrum Buggenhout vzw,{DAY},foi_contact,tick2372; FOI info@car-buggenhout.be; operational Klaverveld 3 9255 Buggenhout; zetel Kloosterstraat 6 9031 Drongen; RIZIV 96529252 HCO 29580; leftover same-zetel Impuls/Bolt/Mozaiek/DIGOR/Ter Kouter cluster + leftover city_buggenhout@1018",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},CAR Buggenhout VZW (Buggenhout / ambulante revalidatie),CAR Buggenhout ASBL (Buggenhout / revalidation ambulatoire),CAR Buggenhout VZW (Buggenhout / outpatient rehabilitation),parastatal,sec_flanders,nl,https://www.car-buggenhout.be/,info@car-buggenhout.be,"Klaverveld 3, 9255 Buggenhout",tick2372 YE2025 Strong official NBB PDF deposit 2026-00205237 + Strong KBO 0412.404.903 Actief 1 VE 2.153.792.057 RSZ2025 86.959 RIZIV 96529252 HCO 29580; omzet JUMP 2650604; bruto JUMP 3077569 ~1.16x; pnl JUMP 212752; equity JUMP 2434396; assets JUMP 2789093; debt JUMP 354697; FTE DROP 34.2; code73 606146; kapitaalsubsidies DROP 655340; destin691 JUMP 640000; cash JUMP 1314856; leftover Impuls@2371 same zetel; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+10) — envelope = omzet 70 (present and not commercial-only vs 73)
append_lines(DATA / "budgets.csv", [
    f"bud_car_buggenhout_omzet_jr2025_statutory,{EID},2025,2650604,2650604,2650604,NBB VKT-VZW code 70 omzet YE2025 JUMP +4.52% (primary L5 envelope),{SRC_PDF},strong,tick2372; PDF p5; YE2024 2535883; omzet present and not commercial-only vs 73 606146",
    f"bud_car_buggenhout_bruto_jr2025_statutory,{EID},2025,3077569,3077569,3077569,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +3.08% (~1.16x omzet),{SRC_PDF},strong,tick2372; PDF p5; YE2024 2985522",
    f"bud_car_buggenhout_code73_jr2025_statutory,{EID},2025,606146,606146,606146,NBB VKT-VZW code 73 lidgeld/schenkingen/subsidies YE2025 DROP -0.62%,{SRC_PDF},strong,tick2372; PDF p5; YE2024 609928",
    f"bud_car_buggenhout_pnl_jr2025_statutory,{EID},2025,212752,212752,212752,NBB VKT-VZW code 9905 te bestemmen winst YE2025 JUMP +0.95%,{SRC_PDF},strong,tick2372; PDF p5; YE2024 210760; bedrijfswinst 9901 204073 JUMP +1.20%",
    f"bud_car_buggenhout_equity_jr2025_statutory,{EID},2025,2434396,2434396,2434396,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +8.27%,{SRC_PDF},strong,tick2372; PDF p4; YE2024 2248403; kapitaalsubsidies 655340; bestemde fondsen 640000",
    f"bud_car_buggenhout_assets_jr2025_statutory,{EID},2025,2789093,2789093,2789093,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +7.79%,{SRC_PDF},strong,tick2372; PDF p3; YE2024 2587604",
    f"bud_car_buggenhout_debt_jr2025_statutory,{EID},2025,354697,354697,354697,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +4.57%,{SRC_PDF},strong,tick2372; PDF p4; YE2024 339201",
    f"bud_car_buggenhout_cash_jr2025_statutory,{EID},2025,1314856,1314856,1314856,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +16.78%,{SRC_PDF},strong,tick2372; PDF p3; YE2024 1125932",
    f"bud_car_buggenhout_destin691_jr2025_statutory,{EID},2025,640000,640000,640000,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was empty),{SRC_PDF},strong,tick2372; PDF p6; YE2024 empty; bestemde fondsen 13 JUMP 640000",
    f"bud_car_buggenhout_fte_jr2025_statutory,{EID},2025,34.2,34.2,34.2,NBB VKT-VZW code 9087 FTE YE2025 DROP -0.58%,{SRC_PDF},strong,tick2372; PDF p8; YE2024 34.4; kapitaalsubsidies 15 DROP 655340; capex 8169 18805",
])

# commitments (+1)
cash_json = (
    '"{""2025_omzet"":2650604,""2025_code73"":606146,""2025_bruto"":3077569,""2025_pnl"":212752,'
    '""2025_equity"":2434396,""2025_assets"":2789093,""2025_debt"":354697,""2025_fte"":34.2,'
    '""2025_kapitaalsubsidies"":655340,""2025_destin691"":640000,""2025_destin13"":640000,'
    '""2025_cash"":1314856,""2025_personnel62"":2759313,""2025_capex8169"":18805,'
    '""2025_gebouwen22"":1114906,""2025_vorderingen40"":263562,""2024_omzet"":2535883,'
    '""2024_code73"":609928,""2024_bruto"":2985522,""2024_pnl"":210760,""2024_equity"":2248403,'
    '""2024_assets"":2587604,""2024_debt"":339201,""2024_fte"":34.4,""2024_kapitaalsubsidies"":682099,'
    '""2024_destin13"":0,""2024_cash"":1125932}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Buggenhout vzw YE2025 (omzet 2.65m / 640k destin JUMP / 655k kapitaalsubsidies / Strong PDF),{EID},RIZIV CAR Buggenhout / dual same zetel,VZW Revalidatiecentrum Buggenhout (KBO 0412.404.903; Actief; 1 VE; RSZ2025 86.959; RIZIV 96529252),2026-06-24,2025,2025,2650604,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00205237.pdf,RIZIV-conventioned ambulante revalidatie children + NAH + dual Drongen Ter Kouter cluster,Publish RIZIV/VL matrix inside omzet 2.65m + 73 0.61m; explain 640k destin JUMP from empty and 655k kapitaalsubsidies vs cash JUMP,{SRC_PDF},strong,Vlaanderen>Oost_Vlaanderen>Buggenhout>CAR_Buggenhout>JR2025_statutory_L5,tick2372; Strong official PDF; leftover Impuls@2371 same Drongen zetel; leftover city_buggenhout@1018; not TE-additive",
])

# leaderboard (+1) pi = 0.4*6.0 + 0.4*4.9 + 0.2*5.0 = 5.36
append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Buggenhout omzet 2.65m / 640k destin JUMP / 655k kapitaalsubsidies (YE2025 CAR Buggenhout),L5,car_revalidatie_vzw_statutory,Vlaanderen>Oost_Vlaanderen>Buggenhout>CAR_Buggenhout>JR2025,2650604,2650604,PDF omzet JUMP 2650604; bruto JUMP 3077569 (~1.16x); pnl JUMP 212752; equity JUMP 2434396; assets JUMP 2789093; debt JUMP 354697; FTE DROP 34.2; destin691 JUMP 640000; kapitaalsubsidies DROP 655340; cash JUMP 1314856; code73 606146; gebouwen 1114906; capex 18805,strong,{SRC_PDF},outpatient rehab children + NAH Buggenhout (RIZIV 96529252 + dual Ter Kouter cluster),RIZIV-conventioned ambulante revalidatie Buggenhout,640k destin JUMP (empty to 640000) while omzet JUMP and cash JUMP +16.78%; kapitaalsubsidies 655340 DROP; RIZIV/VL split unpublished; leftover same-zetel of Impuls/Bolt/Mozaiek/DIGOR/Ter Kouter cluster,6.0,4.9,5,5.36,FOI RIZIV/VL matrix + 640k destin JUMP + 655k kapitaalsubsidies + cash JUMP + dual Drongen cluster,active,,tick2372; Strong official NBB PDF + Strong KBO; leftover Impuls@2371 same zetel; Drongen named+unnamed CARs now exhausted",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost_Vlaanderen>Buggenhout>CAR_Buggenhout>RIZIV_VL_destin,vzw_car_buggenhout,RIZIV vs VL split inside omzet 2650604 + code 73 606146; nature of destin 691 640000 JUMP from empty and bestemde fondsen 13 640000; kapitaalsubsidies 655340 DROP; cash JUMP 1314856; dual Drongen zetel,Strong official PDF leftover RIZIV CAR of Impuls@2371 same zetel; 640k destin JUMP; 655k capital subsidies; public CAR not private clinic,8,Revalidatiecentrum Buggenhout VZW / Stefaan Singelee voorzitter RvB,info@car-buggenhout.be,"Klaverveld 3, 9255 Buggenhout",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2372; ready NOT sent; Strong official NBB PDF; after Impuls@2371; leftover same-zetel CAR; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2372 + append rq_2373 only
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2372,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2372 line, found {n}")
if "rq_2373," in rq_text:
    raise SystemExit("rq_2373 already exists")

new_2372 = (
    "rq_2372,leftover dual — CAR Buggenhout YE2025 Strong (omzet JUMP 2.65m / 640k destin JUMP / 655k kapitaalsubsidies),"
    "hole_fill,8,done,L5,vzw_car_buggenhout,"
    "Tick 2372 leftover after CAR Impuls. Prefer AGB/FARO if YE2025 else leftover same-zetel Revalidatiecentrum Buggenhout 0412.404.903 deposit 2026-00205237 if live 2026pdf. "
    "Do NOT redo CAR Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T22:20:00Z,{STAMP},"
    "tick2372 CAR Buggenhout 0412.404.903 YE2025 Strong official PDF 2026-00205237; omzet JUMP 2650604; bruto JUMP 3077569; pnl JUMP 212752; equity JUMP 2434396; assets JUMP 2789093; debt JUMP 354697; FTE DROP 34.2; destin691 JUMP 640000; kapitaalsubsidies DROP 655340; cash JUMP 1314856; FOI ready NOT sent; leftover Impuls@2371 same zetel CAR; Drongen named+unnamed CARs exhausted\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2372,"):
        parts.append(new_2372)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2372 replace count {replaced}")
new_rq = "".join(parts)
new_2373 = (
    "rq_2373,leftover dual after CAR Buggenhout — Drongen CARs exhausted hunt elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR Buggenhout YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (NOT Kloosterstraat 6). "
    "Do NOT redo CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2372; Drongen named+unnamed CARs exhausted after Buggenhout; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2373
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2372 + rq_2373; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2372,2372,no,"
    "tick2372 leftover dual CAR Buggenhout 0412.404.903 Strong PDF (omzet JUMP 2650604; bruto JUMP 3077569 ~1.16x; pnl JUMP 212752; equity JUMP 2434396; assets JUMP 2789093; debt JUMP 354697; FTE DROP 34.2; destin691 JUMP 640000; kapitaalsubsidies DROP 655340; cash JUMP 1314856; 1 VE RSZ2025 86.959 RIZIV 96529252); after Impuls@2371 same zetel; Drongen named+unnamed CARs exhausted; AGB/FARO/Gandae YE2024; next rq_2373; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append (NOT every-10)
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2372 - rq_2372 CAR Buggenhout (omzet JUMP 2.65m / 640k destin JUMP / 655k kapitaalsubsidies / Strong PDF)

- Unit: **rq_2372** leftover dual after **CAR Impuls@2371**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Took FREE leftover same-zetel Flemish **Revalidatiecentrum Buggenhout VZW** YE2025 (KBO **0412.404.903**; zetel Kloosterstraat 6, 9031 Drongen — same seat as Ter Kouter + CAR Het Veer + 't Vlot + Stappie + Oostakker + Noordhoek + De Elfjes + De Steijgertjes + De Steijger + Kapelhof + TKDV Het Veer + Wegwijs + Sig + DiGOR + Mozaiek + Bolt + Impuls; VE **2.153.792.057** same address since 31.05.2006; operational Klaverveld 3, 9255 Buggenhout; **Actief** **1 VE**; RSZ2025 **86.959**; RIZIV **96529252** / HCO **29580** overeenkomst 953/965; leftover same-zetel CAR of mined **Impuls@2371** / **Bolt@2370** / **Mozaiek@2369** / **DiGOR@2368** / **Sig@2367** / **Wegwijs@2366** / **TKDV Het Veer@2365** / **Kapelhof@2364** / **De Steijger@2363** / **De Steijgertjes@2362** / **De Elfjes@2361** / **Noordhoek@2360** / **Oostakker@2359** / **Stappie@2358** / **'t Vlot@2357** / **CAR Het Veer@2356** / **Ter Kouter@2355** + leftover of mined **city_buggenhout@1018**; info@car-buggenhout.be). Confirmed leftover public (RIZIV-conventioned CAR + Departement Zorg) not private clinic. Do not redo Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VKT-VZW PDF deposit **2026-00205237** (48084 B / 12p; AV **22.05.2026**; header **24.06.2026**; CDN Last-Modified **10.07.2026**) — omzet 70 **EUR2650604** JUMP +4.52%; bruto **EUR3077569** JUMP +3.08% (~**1.16x**); code 73 **EUR606146** DROP −0.62%; pnl **EUR212752** JUMP +0.95%; equity **EUR2434396** JUMP +8.27%; assets **EUR2789093** JUMP +7.79%; debt **EUR354697** JUMP +4.57%; FTE **34.2** DROP −0.58%; kapitaalsubsidies **EUR655340** DROP −3.92%; destin 691 **EUR640000** JUMP (was empty); cash **EUR1314856** JUMP +16.78%; gebouwen **EUR1114906**; capex **EUR18805**. Strong KBO + Strong PDF.
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.36); entities (+1 vzw_car_buggenhout); foi + draft `{GAP}`; rq_2372=done + rq_2373 open; loop_state ticks=2372; raw tick2372/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380**). Named + unnamed Drongen same-zetel CARs now **exhausted**. Next: rq_2373 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf **elsewhere** (not Kloosterstraat 6).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")

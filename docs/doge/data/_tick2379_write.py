#!/usr/bin/env python3
"""Surgical tick 2379 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_floordam"
SRC_PDF = "src_floordam_jr2025_nbb_pdf_2379"
SRC_KBO = "src_floordam_kbo_2379"
SRC_SBM = "src_floordam_sbm_2379"
SRC_SITE = "src_floordam_site_2379"
COMM = "comm_floordam_jr2025_statutory_omzet_9_63m_pnl_drop"
LB = "lb_floordam_omzet_9_63m_pnl_drop_jr2025"
GAP = "gap_floordam_zorgkas_riziv_wzc_matrix_omzet_9_63m_73_2_10m_3_89m_kapitaalsubsidies_l5"
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


append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Goddelijke Voorzienigheid Floordam deposit 2026-00303832,http://cdn.staatsbladmonitor.be/2026pdf/2026-00303832.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2379; official native PDF 372908 bytes 46p VOL-VZW 26.0.15 m05-f; header 17.07.2026; AV 26.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-02; CreationDate 2026-07-17 11:16:47 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table",
    f"{SRC_KBO},KBO Goddelijke Voorzienigheid vzw 0428.792.557,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0428792557,KBO Public Search FOD Economie,{DAY},official_register,tick2379; Actief; 1 VE 2.150.766.944 Goddelijke Voorzienigheid VZW Vanheylenstraat 71 since 03.01.2006; zetel Vanheylenstraat 71 1820 Steenokkerzeel since 22.06.2007; RSZ2025 87.101 RVT; voorzitter Clemens Peeters; dagelijks bestuur Patrick Meers; commissaris L&S / Saskia Luteijn tot 26.06.2026",
    f"{SRC_SBM},Staatsbladmonitor fiche Goddelijke Voorzienigheid vzw 0428792557 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0428792557,Staatsbladmonitor,{DAY},official_register,tick2379; deposit-id 2026-00303832 and CDN Last-Modified 2026-08-02; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC Floordam FOI contact / WZC Steenokkerzeel,https://www.floordam.be/,Goddelijke Voorzienigheid vzw WZC Floordam,{DAY},foi_contact,tick2379; FOI info@floordam.be; zetel Vanheylenstraat 71 1820 Steenokkerzeel; leftover city_steenokkerzeel@1298 after NMSC@2377; NOT Kloosterstraat 6; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},Goddelijke Voorzienigheid VZW (WZC Floordam / Steenokkerzeel / ouderenzorg),Goddelijke Voorzienigheid ASBL (MRS Floordam / Steenokkerzeel),Goddelijke Voorzienigheid VZW (WZC Floordam / Steenokkerzeel),parastatal,city_steenokkerzeel,nl,https://www.floordam.be/,info@floordam.be,"Vanheylenstraat 71, 1820 Steenokkerzeel",tick2379 YE2025 Strong official native NBB PDF deposit 2026-00303832 + Strong KBO 0428.792.557 Actief 1 VE RSZ2025 87.101; omzet JUMP 9631828 WZC ouderenzorg envelope; 73 DROP 2104477 (733 2102277); opbr JUMP 12042966; pnl DROP 58161; equity DROP 7064273; assets DROP 11071966; debt DROP 4007692; FTE 131.9; kapitaalsubsidies DROP 3886611; destin691 empty; cash DROP 428213; leftover city_steenokkerzeel@1298 after NMSC@2377; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_floordam_omzet_jr2025_statutory,{EID},2025,9631828,9631828,9631828,NBB VOL-VZW code 70 omzet YE2025 JUMP +3.89% (primary L5 envelope; WZC ouderenzorg not commercial-only),{SRC_PDF},strong,tick2379; PDF p7 native; YE2024 9271200; 100pct categorie Ouderenzorg; 73 2104477; 733 2102277",
    f"bud_floordam_opbr_jr2025_statutory,{EID},2025,12042966,12042966,12042966,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.40%,{SRC_PDF},strong,tick2379; PDF p7 native; YE2024 11761018; 74 300298; 76A 6363",
    f"bud_floordam_subs73_jr2025_statutory,{EID},2025,2104477,2104477,2104477,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -3.99%,{SRC_PDF},strong,tick2379; PDF p7+p23 native; YE2024 2191993; 731 2200; 733 2102277; 730 empty; 732 empty",
    f"bud_floordam_pnl_jr2025_statutory,{EID},2025,58161,58161,58161,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -71.15%,{SRC_PDF},strong,tick2379; PDF p8 native; YE2024 201627; bedrijfswinst 9901 144793 vs YE2024 440331; destin691 empty",
    f"bud_floordam_equity_jr2025_statutory,{EID},2025,7064273,7064273,7064273,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -2.55%,{SRC_PDF},strong,tick2379; PDF p6 native; YE2024 7249332; kapitaalsubsidies 3886611; overgedragen 14 735995; bestemde fondsen 13 1500000",
    f"bud_floordam_assets_jr2025_statutory,{EID},2025,11071966,11071966,11071966,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -5.38%,{SRC_PDF},strong,tick2379; PDF p5 native; YE2024 11701496",
    f"bud_floordam_debt_jr2025_statutory,{EID},2025,4007692,4007692,4007692,NBB VOL-VZW code 17/49 schulden incl accruals YE2025 DROP -9.98%,{SRC_PDF},strong,tick2379; PDF p6 native; YE2024 4452164; LT 2170129; ST 1821372",
    f"bud_floordam_cash_jr2025_statutory,{EID},2025,428213,428213,428213,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -26.02%,{SRC_PDF},strong,tick2379; PDF p5 native; YE2024 578819; geldbeleggingen 50/53 empty",
    f"bud_floordam_kapitaalsubsidies_jr2025_statutory,{EID},2025,3886611,3886611,3886611,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -5.89%,{SRC_PDF},strong,tick2379; PDF p6 native; YE2024 4129831",
    f"bud_floordam_fte_jr2025_statutory,{EID},2025,131.9,131.9,131.9,NBB VOL-VZW gemiddeld personeelseffectief VTE YE2025 131.9 JUMP +2.49%,{SRC_PDF},strong,tick2379; PDF p23 native; YE2024 128.7; koppen 9086 167 vs 171; personnel 62 9031594; uitzend 617 222964; uitzend FTE 1.8",
])

cash_json = (
    '"{""2025_omzet"":9631828,""2025_opbr"":12042966,""2025_73"":2104477,'
    '""2025_731"":2200,""2025_733"":2102277,""2025_74"":300298,""2025_76A"":6363,'
    '""2025_pnl"":58161,""2025_bedrijfswinst"":144793,""2025_equity"":7064273,'
    '""2025_assets"":11071966,""2025_debt"":4007692,""2025_fte"":131.9,'
    '""2025_kapitaalsubsidies"":3886611,""2025_destin691"":0,""2025_cash"":428213,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":9031594,'
    '""2025_uitzend617"":222964,""2025_gebouwen22"":8241668,'
    '""2025_fondsen13"":1500000,""2024_omzet"":9271200,""2024_opbr"":11761018,'
    '""2024_73"":2191993,""2024_pnl"":201627,""2024_bedrijfswinst"":440331,'
    '""2024_equity"":7249332,""2024_assets"":11701496,""2024_debt"":4452164,'
    '""2024_kapitaalsubsidies"":4129831,""2024_cash"":578819,""2024_fte"":128.7}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Goddelijke Voorzienigheid vzw WZC Floordam YE2025 (omzet 9.63m / 73 2.10m / 3.89m kapitaalsubsidies / pnl DROP 71% / Strong PDF),{EID},Vlaamse zorgkas + Departement Zorg + leftover city_steenokkerzeel,VZW Goddelijke Voorzienigheid Floordam (KBO 0428.792.557; Actief; 1 VE; RSZ2025 87.101),2026-07-17,2025,2025,9631828,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00303832.pdf,Public WZC dual of mined city_steenokkerzeel,Publish zorgkas/RIZIV/resident-fee matrix inside omzet 9.63m + explain 73 2.10m DROP + 3.89m kapitaalsubsidies DROP + pnl DROP 71% + cash DROP 26%,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Steenokkerzeel>Floordam_WZC>JR2025_statutory_L5,tick2379; Strong official native PDF; leftover city_steenokkerzeel@1298 after NMSC@2377; NOT Kloosterstraat 6; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Floordam WZC omzet 9.63m / 73 2.10m / 3.89m kapitaalsubsidies / pnl DROP 71% (YE2025 Steenokkerzeel),L5,wzc_vzw_statutory,Vlaanderen>Vlaams-Brabant>Steenokkerzeel>Floordam_WZC>JR2025,9631828,9631828,PDF omzet JUMP 9631828 WZC ouderenzorg envelope; 73 DROP 2104477 (731 2200; 733 2102277); opbr JUMP 12042966; 74 300298; bedrijfswinst DROP 144793; pnl DROP 58161; equity DROP 7064273; assets DROP 11071966; debt DROP 4007692; FTE 131.9 JUMP; kapitaalsubsidies DROP 3886611; destin691 empty; cash DROP 428213; gebouwen 8241668; personnel 9031594; uitzend 222964 JUMP,strong,{SRC_PDF},WZC + dagverzorging + LDC Omikron residents Steenokkerzeel,Vlaamse zorgkas + Departement Zorg + leftover city_steenokkerzeel,9.63m WZC omzet; 2.10m 73 subsidies DROP; pnl DROP 71%; 3.89m kapitaalsubsidies DROP; cash DROP 26%; leftover city_steenokkerzeel,5.9,5.8,5.4,5.70,FOI zorgkas/RIZIV/resident-fee matrix + 73 2.10m DROP + 3.89m kapitaalsubsidies DROP + pnl DROP 71% + cash DROP 26%,active,,tick2379; Strong official NBB native PDF + Strong KBO; leftover city_steenokkerzeel@1298 after NMSC@2377; OFF Drongen OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Vlaams-Brabant>Steenokkerzeel>Floordam_WZC>zorgkas_RIZIV_WZC,vzw_floordam,zorgkas/RIZIV/resident-fee split inside omzet 9631828; why 73 2104477 DROP (733 2102277); nature of kapitaalsubsidies 3886611 DROP and destin 691 empty; pnl DROP 58161; cash DROP 428213; uitzend JUMP 222964,Strong official PDF leftover public WZC of city_steenokkerzeel@1298; 9.63m omzet; public not private clinic,8,Goddelijke Voorzienigheid VZW / Clemens Peeters voorzitter RvB,info@floordam.be,"Vanheylenstraat 71, 1820 Steenokkerzeel",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2379; ready NOT sent; Strong official native NBB PDF; after Heropbeuring@2378; leftover city_steenokkerzeel WZC off Drongen off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2379,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2379 line, found {n}")
if "rq_2380," in rq_text:
    raise SystemExit("rq_2380 already exists")

new_2379 = (
    "rq_2379,leftover dual — Goddelijke Voorzienigheid Floordam YE2025 Strong (omzet JUMP 9.63m / 73 2.10m / 3.89m kapitaalsubsidies / pnl DROP 71%),"
    "hole_fill,8,done,L5,vzw_floordam,"
    "Tick 2379 leftover after Heropbeuring. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring). "
    "Took Goddelijke Voorzienigheid Floordam 0428.792.557 deposit 2026-00303832 leftover city_steenokkerzeel@1298 after NMSC@2377. "
    "Do NOT redo Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:10:32Z,{STAMP},"
    "tick2379 Floordam 0428.792.557 YE2025 Strong official native PDF 2026-00303832; omzet JUMP 9631828 WZC ouderenzorg envelope; 73 DROP 2104477 (733 2102277); opbr JUMP 12042966; pnl DROP 58161; equity DROP 7064273; assets DROP 11071966; debt DROP 4007692; FTE 131.9; kapitaalsubsidies DROP 3886611; destin691 empty; cash DROP 428213; FOI ready NOT sent; leftover city_steenokkerzeel@1298 after NMSC@2377; OFF Drongen OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2379,"):
        parts.append(new_2379)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2379 replace count {replaced}")
new_rq = "".join(parts)
new_2380 = (
    "rq_2380,EVERY-10 + leftover dual after Floordam — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Goddelijke Voorzienigheid Floordam YE2025. THIS IS EVERY-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557). "
    "Do NOT redo Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2379; Floordam WZC taken leftover city_steenokkerzeel after NMSC; AGB/FARO/Gandae still YE2024; THIS IS EVERY-10\n"
)
new_rq = new_rq + new_2380
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2379 + rq_2380; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2379,2379,no,"
    "tick2379 leftover dual Goddelijke Voorzienigheid Floordam 0428.792.557 Strong native PDF (omzet JUMP 9631828 WZC ouderenzorg envelope; 73 DROP 2104477 733 2102277; opbr JUMP 12042966; pnl DROP 58161; equity DROP 7064273; assets DROP 11071966; debt DROP 4007692; FTE 131.9; kapitaalsubsidies DROP 3886611; destin691 empty; cash DROP 428213; 1 VE RSZ2025 87.101); leftover city_steenokkerzeel@1298 after NMSC@2377; OFF Drongen OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2380 EVERY-10\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2379 - rq_2379 Goddelijke Voorzienigheid Floordam Steenokkerzeel (omzet JUMP 9.63m / 73 2.10m / 3.89m kapitaalsubsidies / pnl DROP 71% / Strong PDF)

- Unit: **rq_2379** leftover dual after **Heropbeuring@2378**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Goddelijke Voorzienigheid VZW (WZC Floordam)** YE2025 (KBO **0428.792.557**; zetel Vanheylenstraat 71, 1820 Steenokkerzeel; **Actief** **1 VE** **2.150.766.944** Goddelijke Voorzienigheid VZW; RSZ2025 **87.101** RVT; leftover of mined **city_steenokkerzeel@1298** / leftover after **agb_steenokkerzeel@1167** / leftover after **NMSC@2377**; info@floordam.be). Confirmed leftover public (Departement Zorg WZC Floordam HCO 3368 + dagverzorging + LDC Omikron) not private clinic / not NMSC 0410.338.110 Vanheylenstraat 16. Do not redo Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VOL-VZW native PDF deposit **2026-00303832** (372908 B / 46p; AV **26.06.2026**; header **17.07.2026**; CDN Last-Modified **02.08.2026**) — omzet 70 **EUR9631828** JUMP +3.89% (WZC ouderenzorg envelope; not commercial-only; 100% categorie Ouderenzorg); 73 **EUR2104477** DROP −3.99% (731 **2200** + 733 **2102277**); bedrijfsopbrengsten 70/76A **EUR12042966** JUMP +2.40%; 74 **300298**; 76A **6363**; bedrijfswinst 9901 **EUR144793** DROP −67.12%; pnl 9904 **EUR58161** DROP −71.15%; equity **EUR7064273** DROP −2.55%; assets **EUR11071966** DROP −5.38%; debt **EUR4007692** DROP −9.98%; FTE **131.9** JUMP +2.49%; kapitaalsubsidies **EUR3886611** DROP −5.89%; destin 691 **empty**; cash **EUR428213** DROP −26.02%; geldbeleggingen empty; gebouwen **EUR8241668**; personeel 62 **EUR9031594**; uitzend 617 **EUR222964** JUMP. Strong KBO + Strong PDF (native text; not SBM table; smaller than Heropbeuring 9MB / NMSC 17MB / Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.70); entities (+1 vzw_floordam); foi + draft `{GAP}`; rq_2379=done + rq_2380 open; loop_state ticks=2379; raw tick2379/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380 IS every-10**). Next: rq_2380 EVERY-10 + unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Floordam / NOT Heropbeuring / NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). Zeepreventorium still YE2024.

"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")

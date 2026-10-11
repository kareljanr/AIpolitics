#!/usr/bin/env python3
"""Surgical tick 2375 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_pulderbos"
SRC_PDF = "src_pulderbos_jr2025_nbb_pdf_2375"
SRC_KBO = "src_pulderbos_kbo_2375"
SRC_SBM = "src_pulderbos_sbm_2375"
SRC_SITE = "src_pulderbos_site_2375"
COMM = "comm_pulderbos_jr2025_statutory_omzet_16_89m_pnl_loss"
LB = "lb_pulderbos_omzet_16_89m_pnl_loss_jr2025"
GAP = "gap_pulderbos_bfm_riziv_limmerik_matrix_omzet_16_89m_pnl_loss_370k_kapitaalsubsidies_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Pulderbos vzw deposit 2026-00189394,http://cdn.staatsbladmonitor.be/2026pdf/2026-00189394.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2375; official native PDF 2465298 bytes 44p VOL-VZW 25.0.13 m05-f; header 22.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-24 01:09:41 UTC OpenPDF 1.3.26; euros from official PDF text not SBM table",
    f"{SRC_KBO},KBO Pulderbos Revalidatiecentrum voor Kinderen en Jongeren vzw 0833.859.015,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0833859015,KBO Public Search FOD Economie,{DAY},official_register,tick2375; Actief; 2 VE; zetel Reebergenlaan 4 2242 Zandhoven since 15.12.2010; RSZ2025 86.103; voorzitter Steeman Tony since 12.06.2024; gedelegeerd bestuurder hazenbosch Steven since 20.02.2019",
    f"{SRC_SBM},Staatsbladmonitor fiche Pulderbos vzw 0833859015 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0833859015,Staatsbladmonitor,{DAY},official_register,tick2375; deposit-id 2026-00189394 and CDN Last-Modified 2026-07-07; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Pulderbos vzw FOI contact / kinderrevalidatie + Limmerik,https://www.revapulderbos.be/,Pulderbos Revalidatiecentrum vzw,{DAY},foi_contact,tick2375; FOI info@revapulderbos.be; zetel Reebergenlaan 4 2242 Zandhoven (Pulderbos); leftover city_zandhoven@1029; NOT Kloosterstraat 6; NOT Inkendaal; NOT Sint-Lievenspoort",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},Pulderbos Revalidatiecentrum voor Kinderen en Jongeren VZW (Zandhoven / children rehab hospital + Limmerik),Pulderbos ASBL (Zandhoven / hopital de reeducation enfants + Limmerik),Pulderbos VZW (Zandhoven / children rehab hospital + Limmerik),parastatal,city_zandhoven,nl,https://www.revapulderbos.be/,info@revapulderbos.be,"Reebergenlaan 4, 2242 Zandhoven (Pulderbos)",tick2375 YE2025 Strong official native NBB PDF deposit 2026-00189394 + Strong KBO 0833.859.015 Actief 2 VE RSZ2025 86.103; omzet JUMP 16889028 hospital envelope 73 empty; Limmerik 960644; opbr JUMP 19557498; pnl JUMP loss 18791; equity DROP 3658537; assets DROP 8582511; debt DROP 4843974; FTE 196.9; kapitaalsubsidies DROP 370012; destin691 empty; cash DROP 406605; leftover city_zandhoven@1029; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+10) — envelope = omzet 70 (hospital/rehab; 73 empty so public flows inside 70; not commercial-only)
append_lines(DATA / "budgets.csv", [
    f"bud_pulderbos_omzet_jr2025_statutory,{EID},2025,16889028,16889028,16889028,NBB VOL-VZW code 70 omzet YE2025 JUMP +7.33% (primary L5 envelope; hospital/rehab not commercial-only; 73 empty),{SRC_PDF},strong,tick2375; PDF p7 VOL-VZW 4; YE2024 15734928; Revalidatiecentrum 15928384; Limmerik 960644",
    f"bud_pulderbos_opbr_jr2025_statutory,{EID},2025,19557498,19557498,19557498,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +5.70%,{SRC_PDF},strong,tick2375; PDF p7; YE2024 18503062; andere 74 2668470; 76A empty YE2025 (YE2024 422668)",
    f"bud_pulderbos_limmerik_jr2025_statutory,{EID},2025,960644,960644,960644,NBB VOL-VZW 6.9 omzet Limmerik YE2025 JUMP +1.83% (school/dual stream inside omzet 70),{SRC_PDF},strong,tick2375; PDF p21 VOL-VZW 6.9; YE2024 943381; Revalidatiecentrum 15928384",
    f"bud_pulderbos_pnl_jr2025_statutory,{EID},2025,-18791,-18791,-18791,NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 JUMP from larger loss -464551,{SRC_PDF},strong,tick2375; PDF p8; YE2024 -464551; 9901 -132369; destin691 empty",
    f"bud_pulderbos_equity_jr2025_statutory,{EID},2025,3658537,3658537,3658537,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -2.22%,{SRC_PDF},strong,tick2375; PDF p6; YE2024 3741592; kapitaalsubsidies 370012; bestemde fondsen 13 450000 Revapolis",
    f"bud_pulderbos_assets_jr2025_statutory,{EID},2025,8582511,8582511,8582511,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -6.63%,{SRC_PDF},strong,tick2375; PDF p5; YE2024 9192354",
    f"bud_pulderbos_debt_jr2025_statutory,{EID},2025,4843974,4843974,4843974,NBB VOL-VZW code 17/49 schulden incl accruals YE2025 DROP -7.82%,{SRC_PDF},strong,tick2375; PDF p6; YE2024 5255142; LT 789588; ST 3966077; overlopende 88309",
    f"bud_pulderbos_cash_jr2025_statutory,{EID},2025,406605,406605,406605,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -21.90%,{SRC_PDF},strong,tick2375; PDF p5; YE2024 520648; geldbeleggingen 50/53 2501014",
    f"bud_pulderbos_kapitaalsubsidies_jr2025_statutory,{EID},2025,370012,370012,370012,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -14.80%,{SRC_PDF},strong,tick2375; PDF p6; YE2024 434276",
    f"bud_pulderbos_fte_jr2025_statutory,{EID},2025,196.9,196.9,196.9,NBB VOL-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 196.9 DROP,{SRC_PDF},strong,tick2375; PDF p21 VOL-VZW 6.9; YE2024 198.1; koppen 9086 257; personnel 62 16199395 JUMP +4.37% vs YE2024 15521236",
])

# commitments (+1)
cash_json = (
    '"{""2025_omzet"":16889028,""2025_opbr"":19557498,""2025_limmerik"":960644,'
    '""2025_reva"":15928384,""2025_74"":2668470,""2025_pnl"":-18791,'
    '""2025_equity"":3658537,""2025_assets"":8582511,""2025_debt"":4843974,'
    '""2025_fte"":196.9,""2025_kapitaalsubsidies"":370012,""2025_destin691"":0,'
    '""2025_cash"":406605,""2025_geldbeleggingen"":2501014,""2025_personnel62"":16199395,'
    '""2025_gebouwen22"":1186607,""2025_aanbouw27"":1545900,""2025_fondsen13"":450000,'
    '""2025_voorziening_revapolis"":80000,""2025_9901"":-132369,'
    '""2024_omzet"":15734928,""2024_opbr"":18503062,""2024_limmerik"":943381,'
    '""2024_pnl"":-464551,""2024_equity"":3741592,""2024_assets"":9192354,'
    '""2024_debt"":5255142,""2024_kapitaalsubsidies"":434276,""2024_cash"":520648,'
    '""2024_personnel62"":15521236,""2024_fte"":198.1}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Pulderbos vzw YE2025 (omzet 16.89m / Limmerik 0.96m / pnl LOSS 19k / 370k kapitaalsubsidies / Strong PDF),{EID},FOD Volksgezondheid BFM + RIZIV child rehab + leftover city_zandhoven,VZW Pulderbos Revalidatiecentrum voor Kinderen en Jongeren (KBO 0833.859.015; Actief; 2 VE; RSZ2025 86.103),2026-06-22,2025,2025,16889028,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00189394.pdf,Public specialized children rehab hospital + Limmerik dual of mined city_zandhoven,Publish BFM/RIZIV/Limmerik matrix inside omzet 16.89m + 370k kapitaalsubsidies vs pnl LOSS 19k,{SRC_PDF},strong,Vlaanderen>Antwerpen>Zandhoven>Pulderbos>JR2025_statutory_L5,tick2375; Strong official native PDF; leftover city_zandhoven@1029; NOT Kloosterstraat 6; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

# leaderboard (+1) pi = 0.4*6.2 + 0.4*7.2 + 0.2*5.2 = 6.40
append_lines(DATA / "leaderboard.csv", [
    f"{LB},Pulderbos omzet 16.89m / Limmerik 0.96m / pnl LOSS 19k (YE2025 children rehab + Limmerik Zandhoven),L5,child_rehab_hospital_vzw_statutory,Vlaanderen>Antwerpen>Zandhoven>Pulderbos>JR2025,16889028,16889028,PDF omzet JUMP 16889028 hospital envelope 73 empty; Limmerik 960644; opbr JUMP 19557498; 74 2668470; pnl JUMP loss 18791; equity DROP 3658537; assets DROP 8582511; debt DROP 4843974; FTE 196.9; kapitaalsubsidies DROP 370012; destin691 empty; cash DROP 406605; geldbeleggingen 2501014; gebouwen 1186607; aanbouw 1545900; fondsen13 450000 Revapolis; personnel JUMP 16199395,strong,{SRC_PDF},children in specialized rehab Zandhoven (hospital + Limmerik),FOD Volksgezondheid BFM + RIZIV + leftover city_zandhoven,16.89m hospital omzet with 73 empty; Limmerik 0.96m; still-loss 19k after 465k loss; 370k kapitaalsubsidies; 450k Revapolis fund; leftover city_zandhoven,6.2,7.2,5.2,6.40,FOI BFM/RIZIV/Limmerik matrix + 370k kapitaalsubsidies + pnl LOSS + dual hospital/Limmerik,active,,tick2375; Strong official NBB native PDF + Strong KBO; leftover city_zandhoven@1029; OFF Drongen OFF Inkendaal",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Antwerpen>Zandhoven>Pulderbos>BFM_RIZIV_Limmerik,vzw_pulderbos,BFM/RIZIV/Limmerik split inside omzet 16889028 + Limmerik 960644; why code 73 empty; nature of kapitaalsubsidies 370012 DROP and pnl LOSS 18791; destin 691 empty; 450k Revapolis fund,Strong official PDF leftover public children rehab hospital of city_zandhoven@1029; 16.89m omzet; 73 empty; still-loss; public not private clinic,8,Pulderbos Revalidatiecentrum voor Kinderen en Jongeren VZW / Tony Steeman voorzitter RvB,info@revapulderbos.be,"Reebergenlaan 4, 2242 Zandhoven (Pulderbos)",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2375; ready NOT sent; Strong official native NBB PDF; after Inkendaal@2374; leftover city_zandhoven hospital off Drongen off Inkendaal; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2375 + append rq_2376 only
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2375,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2375 line, found {n}")
if "rq_2376," in rq_text:
    raise SystemExit("rq_2376 already exists")

new_2375 = (
    "rq_2375,leftover dual — Pulderbos YE2025 Strong (omzet JUMP 16.89m / Limmerik 0.96m / pnl LOSS 19k),"
    "hole_fill,8,done,L5,vzw_pulderbos,"
    "Tick 2375 leftover after Inkendaal. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal). "
    "Took Pulderbos 0833.859.015 deposit 2026-00189394 leftover city_zandhoven@1029. "
    "Do NOT redo Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T22:35:51Z,{STAMP},"
    "tick2375 Pulderbos 0833.859.015 YE2025 Strong official native PDF 2026-00189394; omzet JUMP 16889028 hospital envelope 73 empty; Limmerik 960644; opbr JUMP 19557498; pnl JUMP loss 18791; equity DROP 3658537; assets DROP 8582511; debt DROP 4843974; FTE 196.9; kapitaalsubsidies DROP 370012; cash DROP 406605; FOI ready NOT sent; leftover city_zandhoven@1029; OFF Drongen OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2375,"):
        parts.append(new_2375)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2375 replace count {replaced}")
new_rq = "".join(parts)
new_2376 = (
    "rq_2376,leftover dual after Pulderbos — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Pulderbos YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos). "
    "Candidate leftover MKL/RevArte 0410.025.037 deposit 2026-00185442 leftover city_edegem (HEAD 200 / 1144102 B this tick). "
    "Do NOT redo Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2375; Pulderbos taken leftover city_zandhoven; AGB/FARO/Gandae still YE2024; next every-10 2380\n"
)
new_rq = new_rq + new_2376
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2375 + rq_2376; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2375,2375,no,"
    "tick2375 leftover dual Pulderbos 0833.859.015 Strong native PDF (omzet JUMP 16889028 hospital envelope 73 empty; Limmerik 960644; opbr JUMP 19557498; pnl JUMP loss 18791; equity DROP 3658537; assets DROP 8582511; debt DROP 4843974; FTE 196.9; kapitaalsubsidies DROP 370012; destin691 empty; cash DROP 406605; 2 VE RSZ2025 86.103); leftover city_zandhoven@1029; OFF Drongen OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2376; next every-10 2380\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append (NOT every-10)
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2375 - rq_2375 Pulderbos Zandhoven (omzet JUMP 16.89m / Limmerik 0.96m / pnl LOSS 19k / Strong PDF)

- Unit: **rq_2375** leftover dual after **Inkendaal@2374**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Pulderbos Revalidatiecentrum voor Kinderen en Jongeren VZW** YE2025 (KBO **0833.859.015**; zetel Reebergenlaan 4, 2242 Zandhoven / Pulderbos; **Actief** **2 VE**; RSZ2025 **86.103**; leftover of mined **city_zandhoven@1029** / leftover after **agb_zandhoven@1222**; info@revapulderbos.be). Confirmed leftover public (RIZIV/FOD specialized children's rehab hospital + Limmerik stream) not private clinic. Do not redo Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VOL-VZW native PDF deposit **2026-00189394** (2465298 B / 44p; AV **17.06.2026**; header **22.06.2026**; CDN Last-Modified **07.07.2026**) — omzet 70 **EUR16889028** JUMP +7.33% (hospital/rehab envelope; code 73 empty); waarvan Revalidatiecentrum **15928384** + Limmerik **960644**; bedrijfsopbrengsten 70/76A **EUR19557498** JUMP +5.70%; pnl 9904 **EUR−18791** JUMP from loss −464551; equity **EUR3658537** DROP −2.22%; assets **EUR8582511** DROP −6.63%; debt **EUR4843974** DROP −7.82%; FTE **196.9**; kapitaalsubsidies **EUR370012** DROP −14.80%; destin 691 **empty**; cash **EUR406605** DROP −21.90%; geldbeleggingen **EUR2501014**; bestemde fondsen 13 **EUR450000** (Revapolis); personeel 62 **EUR16199395** JUMP +4.37%. Strong KBO + Strong PDF (native text; not SBM table; avoided 28MB scan).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 6.40); entities (+1 vzw_pulderbos); foi + draft `{GAP}`; rq_2375=done + rq_2376 open; loop_state ticks=2375; raw tick2375/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2380**). Next: rq_2376 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (candidate MKL/RevArte 0410.025.037 deposit 2026-00185442 leftover city_edegem HEAD 200 / 1144102 B; Zeepreventorium still YE2024). NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6.

"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")

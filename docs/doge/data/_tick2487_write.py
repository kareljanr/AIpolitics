from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2487_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_zonnewende_jr2025_nbb_pdf_2487"
SRC_KBO="src_zonnewende_kbo_2487"
SRC_SBM="src_zonnewende_sbm_2487"
SRC_SITE="src_zonnewende_site_2487"
EID="vzw_zonnewende_tielt"
GAP="gap_zonnewende_tielt_wzc_matrix_omzet_10_71m_73_2_02m_pnl_drop_849k_cash_jump_3_56m_l5"
COMM="comm_zonnewende_jr2025_statutory_omzet_10_71m_73_2_02m_pnl_drop_849k"
LB="lb_zonnewende_omzet_10_71m_73_2_02m_pnl_drop_849k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Zorg Tielt 0711.824.305 remine; NOT Sint Vincentius 0410.266.349 0 VE same address; NOT OCMW Tielt 0212.176.117 bestuurder; NOT Sint-Andriesziekenhuis Tielt 0408.661.691 remine; NOT Mivalti 0416.406.548 remine; NOT Harlekijntjes 0407.700.403 remine tick2452; NOT Huize De Veuster 0476.354.132 remine tick2486; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Blijdorp remine; NOT Den Brand remine; NOT De Schakel remine; NOT WZC Sint-Vincentius Erpe-Mere 0422.620.585 leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Kinderlach YE2024; NOT De Linde Ronse YE2024; NOT Molleke YE2024; NOT t Sas YE2024; NOT OpWeg YE2024")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 De Zonnewende Tielt deposit 2026-00215913,http://cdn.staatsbladmonitor.be/2026pdf/2026-00215913.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2487; official native statutory PDF 1761857 bytes 45p VOL-VZW 25.0.13 m05-f; header 25.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-29 23:16:08 UTC OpenPDF 1.3.26; CDN Last-Modified 12.07.2026; statutory pages native; CDN 2026-00215913 GET 200 1761857 MD5 acdfdae43026c59ac2515e5158285c87; VOL-VZW 6.1 6.2.1-4 6.3.4 6.4.1-3 6.5.1-3 6.13 6.16 niet dienstig; prior-year identical not restated; commissaris Moore Audit BV Van Ryckeghem Geert Vandeputte Jo; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Zonnewende 0735.627.214,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0735627214,KBO Public Search FOD Economie,{DAY},official_register,tick2487; Actief; 1 VE 2.294.938.440 zetel Karel van Manderstraat 68 8760 Tielt since 01.01.2025; VZW since 24.09.2019; begindatum 03.10.2019; RSZ-werkgever RSZ2025 87.301 Rusthuizen voor ouderen ROB; FOI secretariaat@gvo.be; leftover mined city_tielt WZC; VE since 01.11.2019; bestuurders OCMW Tielt 0212.176.117 + Sint Vincentius 0410.266.349; NOT Zorg Tielt remine; NOT Sint Vincentius 0 VE; NOT Huize De Veuster remine",
f"{SRC_SBM},NBB Consult / SBM fiche De Zonnewende 0735627214 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0735627214,NBB Consult / SBM,{DAY},official_register,tick2487; deposit-id 2026-00215913 YE 01.01.2025-31.12.2025 filing VOL-VZW Volledig model vereniging Initial UUID 3449ee4d-55c3-11f1-9044-3df4e799874f; Companyweb last-balansjaar 2025 neergelegd 30.06.2026 deposit-id discovery via SBM/NBB OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},De Zonnewende / GVO FOI contact leftover city_tielt WZC,https://www.gvo.be/,De Zonnewende VZW leftover city_tielt WZC 1 VE GVO,{DAY},foi_contact,tick2487; FOI secretariaat@gvo.be; zetel Karel van Manderstraat 68 8760 Tielt; leftover mined city_tielt WZC after Huize De Veuster lock; NOT Zorg Tielt remine; NOT Sint Vincentius 0 VE; NOT Sint-Andries remine; NOT Mivalti remine; NOT Harlekijntjes remine; NOT Huize De Veuster remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},De Zonnewende VZW,ASBL De Zonnewende,De Zonnewende VZW (leftover city_tielt WZC),parastatal,city_tielt,nl,https://www.gvo.be/,secretariaat@gvo.be,Karel van Manderstraat 68 8760 Tielt,tick2487 YE2025 Strong official native NBB PDF deposit 2026-00215913 + Strong KBO 0735.627.214 Actief 1 VE 2.294.938.440; omzet70 10713499 material not commercial-only; 73 DROP 2015382; 76A DROP 73131; envelope omzet70 JUMP 10713499; 70/76A JUMP 13069784; pnl DROP 848516; 9901 DROP 813452; equity JUMP 3802890; assets JUMP 5621009; debt JUMP 1818119; FTE JUMP 140.6; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 3558410; geldbeleggingen empty; capex 486737; leftover city_tielt WZC 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_zonnewende_omzet_jr2025_statutory,{EID},2025,10713499,10713499,10713499,NBB VOL-VZW code 70 omzet YE2025 JUMP +3.27% (material not commercial-only),{SRC_PDF},strong,tick2487; PDF p6 native; YE2024 10374592; 73 DROP 2015382; 76A DROP 73131; 6.9 WZC 4382230 DVC 73763 Mut-RIZIV 6205227 Andere 52280",
f"bud_zonnewende_73_jr2025_statutory,{EID},2025,2015382,2015382,2015382,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -0.68%,{SRC_PDF},strong,tick2487; PDF p6/p6.9 native; YE2024 2029105; 731 700; 732 empty; 733 2014682; FOI RIZIV/Departement Zorg/OCMW matrix behind 73",
f"bud_zonnewende_opbr_jr2025_statutory,{EID},2025,10713499,10713499,10713499,NBB VOL-VZW envelope omzet 70 YE2025 JUMP +3.27% (VZW envelope because omzet material not commercial-only),{SRC_PDF},strong,tick2487; PDF p6 native; YE2024 10374592; 70 10713499; 73 2015382; 76A 73131; 70/76A 13069784",
f"bud_zonnewende_76A_jr2025_statutory,{EID},2025,73131,73131,73131,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -52.01%,{SRC_PDF},strong,tick2487; PDF p6 native; YE2024 152384",
f"bud_zonnewende_pnl_jr2025_statutory,{EID},2025,848516,848516,848516,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -27.80% (was 1175188),{SRC_PDF},strong,tick2487; PDF p7 native; YE2024 1175188; bedrijfswinst 9901 813452 DROP; destin691 empty",
f"bud_zonnewende_bedrijfswinst_jr2025_statutory,{EID},2025,813452,813452,813452,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -28.60% (was 1139269),{SRC_PDF},strong,tick2487; PDF p6 native; YE2024 1139269; 62 9082553 JUMP; 630 41261 JUMP; 66A empty; 66B empty; 640/8 46768 DROP; 635/9 empty; 631/4 -7081",
f"bud_zonnewende_equity_jr2025_statutory,{EID},2025,3802890,3802890,3802890,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +28.72%,{SRC_PDF},strong,tick2487; PDF p5 native; YE2024 2954374; kapitaalsubsidies empty; overgedragen 14 3652890 JUMP; fondsen 10 150000 FLAT; bestemde fondsen 13 empty",
f"bud_zonnewende_assets_jr2025_statutory,{EID},2025,5621009,5621009,5621009,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +19.43%,{SRC_PDF},strong,tick2487; PDF p4 native; YE2024 4706437; MVA 22/27 642670 JUMP; cash 3558410 JUMP; geldbeleggingen empty; aanbouw 27 206558 JUMP; FVA 28 empty; LT recv 29 empty",
f"bud_zonnewende_debt_jr2025_statutory,{EID},2025,1818119,1818119,1818119,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +3.77%,{SRC_PDF},strong,tick2487; PDF p5 native; YE2024 1752063; 17 empty; 42/48 1811132 JUMP",
f"bud_zonnewende_cash_jr2025_statutory,{EID},2025,3558410,3558410,3558410,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +10.20%,{SRC_PDF},strong,tick2487; PDF p4 native; YE2024 3229138; geldbeleggingen 50/53 empty; capex 486737",
f"bud_zonnewende_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 empty),{SRC_PDF},strong,tick2487; PDF p8 native; YE2024 destin empty; 791 empty; 14 JUMP 3652890 = 14P 2804374 + pnl 848516",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":10713499,\"\"2025_73\"\":2015382,\"\"2025_76A\"\":73131,"
"\"\"2025_opbr70\"\":10713499,\"\"2025_opbr7076A\"\":13069784,"
"\"\"2025_pnl\"\":848516,\"\"2025_bedrijfswinst\"\":813452,"
"\"\"2025_equity\"\":3802890,\"\"2025_assets\"\":5621009,\"\"2025_debt\"\":1818119,"
"\"\"2025_fte\"\":140.6,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":3558410,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":9082553,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":206558,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":150000,\"\"2025_overgedragen14\"\":3652890,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":41261,\"\"2025_capex\"\":486737,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":37890,\"\"2025_74\"\":267772,"
"\"\"2024_omzet\"\":10374592,\"\"2024_73\"\":2029105,"
"\"\"2024_opbr70\"\":10374592,\"\"2024_opbr7076A\"\":12732595,\"\"2024_pnl\"\":1175188,\"\"2024_bedrijfswinst\"\":1139269,"
"\"\"2024_equity\"\":2954374,\"\"2024_assets\"\":4706437,"
"\"\"2024_debt\"\":1752063,\"\"2024_cash\"\":3229138,\"\"2024_fte\"\":128.6,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":152384,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Zonnewende YE2025 (omzet JUMP 10.71m / 73 2.02m / pnl DROP 849k / cash JUMP 3.56m / Strong PDF),{EID},WZC + leftover city_tielt WZC,De Zonnewende VZW (KBO 0735.627.214; Actief; 1 VE; zetel Tielt),2026-06-17,2025,2025,10713499,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00215913.pdf,Public WZC dual of mined city_tielt,Publish RIZIV / Departement Zorg / OCMW / GVO matrix behind omzet 10.71m and 73 2.02m and why pnl DROP 848516 after YE2024 1175188,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Tielt>De-Zonnewende>JR2025_statutory_L5,tick2487; Strong official native PDF; leftover mined city_tielt WZC; 1 VE; prior-year identical; NOT Zorg Tielt remine; NOT Sint Vincentius 0 VE; NOT Huize De Veuster remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"De Zonnewende omzet JUMP 10.71m / 73 2.02m / pnl DROP 849k (YE2025 leftover city_tielt WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Tielt>De-Zonnewende>JR2025",
"10713499",
"10713499",
"PDF envelope 10713499 = omzet 70 VZW because omzet material not commercial-only; 70 10713499; 73 2015382; 76A 73131; 70/76A 13069784; bedrijfswinst DROP 813452; pnl DROP 848516; equity JUMP 3802890; assets JUMP 5621009; debt JUMP 1818119; FTE 140.6; kapitaalsubsidies empty; destin691 empty; cash JUMP 3558410; capex 486737; leftover city_tielt WZC",
"strong",
SRC_PDF,
"WZC + leftover city_tielt WZC",
"WZC leftover city_tielt",
"10.71m envelope; 73 2.02m; pnl DROP 849k; leftover city_tielt WZC",
"5.58",
"5.30",
"5.34",
"5.56",
"FOI RIZIV / Departement Zorg / OCMW / GVO matrix behind envelope omzet 10.71m + 73 2.02m and why pnl DROP 848516 after YE2024 1175188 while FTE JUMP 140.6 and capex 486737",
"active",
"",
"tick2487 leftover mined city_tielt WZC after Huize De Veuster lock; 1 VE; prior-year identical; NOT Zorg Tielt remine; NOT Sint Vincentius 0 VE; NOT Sint-Andries remine; NOT Mivalti remine; NOT Harlekijntjes remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Tielt>De-Zonnewende>WZC",
"entity_id": EID,
"what_is_missing": "RIZIV / Departement Zorg / OCMW Tielt / GVO split behind envelope omzet 10713499 (material not commercial-only vs 73 2015382) and why pnl DROP 848516 after YE2024 1175188 while FTE JUMP 140.6 and capex 486737",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_tielt; VOL envelope 10.71m because omzet material not commercial-only; public ROB 1 VE Karel van Manderstraat 68; pnl DROP 849k / 73 2.02m / cash JUMP 3.56m",
"priority": "8",
"recipient_body": "DE ZONNEWENDE VZW / Raad van Bestuur",
"recipient_email": "secretariaat@gvo.be",
"recipient_postal": "Karel van Manderstraat 68 8760 Tielt",
"draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
"status": "ready",
"date_ready": DAY,
"date_sent": "",
"date_due": "",
"date_answered": "",
"response_summary": "",
"linked_commitment_id": COMM,
"linked_leaderboard_id": LB,
"created_utc": STAMP,
"updated_utc": STAMP,
"notes": "tick2487; ready NOT sent; Strong official native NBB PDF; leftover mined city_tielt WZC after Huize De Veuster lock; 1 VE; prior-year identical; off Zorg Tielt remine; off Sint Vincentius 0 VE; off Sint-Andries remine; off Mivalti remine; off Harlekijntjes remine; off Huize De Veuster remine; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")

print("CORE APPEND DONE")

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2487,")!=1: raise SystemExit(f"bad 2487 count {rq_raw.count(b'rq_2487,')}")
if b"rq_2488," in rq_raw: raise SystemExit("2488 exists")
idx=rq_raw.rfind(b"rq_2487,")
if idx<0: raise SystemExit("rq_2487 not found")
new_2487=(
"rq_2487,leftover dual De Zonnewende YE2025,hole_fill,8,done,L5,vzw_zonnewende_tielt,"
"Took unused leftover public WZC De Zonnewende 0735.627.214 leftover mined city_tielt. Official NBB VOL-VZW YE2025 2026-00215913 native statutory 45p 1.76MB. Envelope omzet 70 JUMP 10713499 (material not commercial-only vs 73 DROP 2015382); pnl DROP 848516; 70/76A JUMP 13069784; FTE 140.6; capex 486737. NOT Zorg Tielt remine. NOT Sint Vincentius 0 VE. NOT Sint-Andries remine. NOT Mivalti remine. NOT Harlekijntjes remine. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2487 leftover mined city_tielt WZC; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2490\n"
)
new_2488=(
"rq_2488,leftover dual hunt after De Zonnewende,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken; leftover VAPH/CAR) / geel (Augustientjes CIK taken; leftover VAPH/CAR) / herentals (Bremdael WZC taken — leftover VAPH/CAR only; OpWeg YE2024) / eeklo (leftover WZC; Kinderlach YE2024) / halle (leftover WZC/VAPH; leftover CIK De Kapoentjes 0821.882.483 unused — take ONLY if unused + official YE2025 native PDF) / kalmthout (leftover WZC/VAPH) / bornem (CAR taken; leftover WZC/VAPH) / puurs (maatwerk taken; leftover WZC/VAPH) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde / mol / zoersel / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken) / lokeren (VAPH taken) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK Harlekijntjes + WZC De Zonnewende taken — leftover VAPH/CAR/maatwerk only). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT De Zonnewende remine. NOT Zorg Tielt remine. NOT Sint Vincentius 0 VE. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2487 leftover city_tielt WZC; De Zonnewende taken leftover mined city_tielt WZC; Huize De Veuster taken leftover mined city_tremelo VAPH; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2487.count("\n")!=1 or new_2488.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2487",new_2487),("2488",new_2488)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2487.encode("utf-8"))
    f.write(new_2488.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2487", chk.count(b"rq_2487,"), "n2488", chk.count(b"rq_2488,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2487,2487,no,tick2487 leftover dual De Zonnewende 0735.627.214 Strong native PDF (omzet70 10713499 material not commercial-only vs 73 DROP 2015382; 76A DROP 73131; envelope omzet70 JUMP 10713499; 70/76A JUMP 13069784; pnl DROP 848516; 9901 DROP 813452; equity JUMP 3802890; assets JUMP 5621009; debt JUMP 1818119; FTE JUMP 140.6; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 3558410; geldbeleggingen empty; capex 486737; 1 VE leftover city_tielt WZC); leftover mined city_tielt WZC; prior-year identical; NOT Zorg Tielt remine; NOT Sint Vincentius 0 VE; NOT Sint-Andries remine; NOT Mivalti remine; NOT Harlekijntjes remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next every-10 is 2490; next rq_2488 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2487 - rq_2487 De Zonnewende Tielt (omzet JUMP 10.71m / 73 2.02m / pnl DROP 849k / cash JUMP 3.56m / Strong PDF)

- Unit: **rq_2487** leftover dual after **Huize De Veuster@2486**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop (prior extraction only skip-list dead-ends Hebe/Sint-Rafaël/VBJK/Vriendenkring/AZ Sint-Maria SCAN/Gezondheidscentrum Waregem). Entity-side official KBO: zetel 8760 Tielt + RSZ2025 **87.301** ROB. Confirmed `city_tielt` exists (mined; leftover CIK Harlekijntjes taken — leftover WZC unused). FIRST leftover unused + live official YE2025 native euros: took FREE leftover Flemish **DE ZONNEWENDE VZW** YE2025 (KBO **0735.627.214**; zetel Karel van Manderstraat 68 8760 Tielt; **Actief** **1 VE** **2.294.938.440** since 01.11.2019; RSZ2025 **87.301**; leftover of mined **city_tielt**; secretariaat@gvo.be; WZC/ROB GVO; bestuurders OCMW Tielt + Sint Vincentius). Identity trap: 0735.627.214 ≠ Zorg Tielt **0711.824.305** remine ≠ Sint Vincentius **0410.266.349** 0 VE ≠ OCMW Tielt **0212.176.117** ≠ Sint-Andriesziekenhuis Tielt remine ≠ Mivalti remine ≠ Harlekijntjes remine ≠ Huize De Veuster remine ≠ WZC Sint-Vincentius Erpe-Mere **0422.620.585**. 1 VE leftover of mined city_tielt (zetel + VE Karel van Manderstraat 68). Confirmed leftover public WZC not convent / not private / not CIK / not VAPH / not commercial NV. VOL-VZW **native text** (not scan) — 1761857 B / 45p all native euros (VOL-VZW 6.1 6.2.1-4 6.3.4 6.4.1-3 6.5.1-3 6.13 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00215913** (1761857 B / 45p; AV **17.06.2026**; header **25.06.2026**; official NBB UUID 3449ee4d-55c3-11f1-9044-3df4e799874f; CDN GET **200** 1761857 official NBB-generated OpenPDF 1.3.26 CreationDate 29.06.2026 Last-Modified 12.07.2026 MD5 acdfdae43026c59ac2515e5158285c87; all 45p native; prior-year identical not restated; commissaris Moore Audit BV / Van Ryckeghem Geert / Vandeputte Jo) — omzet 70 **EUR10713499** JUMP +3.27% (material not commercial-only; was 10374592; 6.9 WZC 4382230 / DVC 73763 / Mut-RIZIV 6205227 / Andere 52280); 73 **EUR2015382** DROP −0.68% (was 2029105; 731 700; 732 empty; 733 2014682); 76A **EUR73131** DROP −52.01% (was 152384); envelope omzet 70 **EUR10713499** JUMP +3.27% (VZW envelope because omzet material not commercial-only; was 10374592); 70/76A **EUR13069784** JUMP +2.65%; 74 **EUR267772** JUMP; 62 **EUR9082553** JUMP +5.15%; 630 **EUR41261** JUMP; 66A **empty**; 66B **empty**; 640/8 **EUR46768** DROP; 635/9 **empty**; 631/4 **EUR-7081**; bedrijfswinst 9901 **EUR813452** DROP −28.60% (was 1139269); pnl 9904 **EUR848516** DROP −27.80% (was 1175188); equity **EUR3802890** JUMP +28.72%; assets **EUR5621009** JUMP +19.43%; debt **EUR1818119** JUMP +3.77%; FTE **140.6** JUMP +9.33% (was 128.6; 1003 140.6; 9087 140.6; 9086 212; 105 149.3); kapitaalsubsidies **empty**; destin 691 **empty**; 791 **empty**; cash **EUR3558410** JUMP +10.20%; geldbeleggingen **empty**; gebouwen **empty**; MVA 22/27 **EUR642670** JUMP; aanbouw **EUR206558** JUMP; capex **EUR486737**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_tielt WZC. NOT Zorg Tielt remine. NOT Sint Vincentius 0 VE. NOT Sint-Andries remine. NOT Mivalti remine. NOT Harlekijntjes remine. NOT Huize De Veuster remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.56); entities (+1 vzw_zonnewende_tielt); foi + draft `gap_zonnewende_tielt_wzc_matrix_omzet_10_71m_73_2_02m_pnl_drop_849k_cash_jump_3_56m_l5`; rq_2487=done + rq_2488 open; loop_state ticks=2487; raw tick2487/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2488 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT De Zonnewende remine / NOT Zorg Tielt remine / NOT Sint Vincentius 0 VE / NOT Huize De Veuster remine / NOT Grijkoort remine / NOT GR.O.O.D. no JR / NOT Nektari remine / NOT Reva Ter Linde remine / NOT De Hagewinde remine / NOT BWP remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_tielt WZC taken (CIK already taken). Leftover CIK De Kapoentjes Halle **0821.882.483** unused — take ONLY if unused + official YE2025 native PDF.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

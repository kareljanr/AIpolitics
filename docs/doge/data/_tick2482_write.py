from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2482_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_ter_linde_jr2025_nbb_pdf_2482"
SRC_KBO="src_ter_linde_kbo_2482"
SRC_SBM="src_ter_linde_sbm_2482"
SRC_SITE="src_ter_linde_site_2482"
EID="vzw_reva_ter_linde_bornem"
GAP="gap_ter_linde_bornem_car_matrix_bruto_1_53m_omzet73_empty_pnl_drop_44k_equity_jump_2_53m_capex_2_88m_l5"
COMM="comm_ter_linde_jr2025_statutory_bruto_153m_pnl_drop_52k_equity_jump_253m"
LB="lb_ter_linde_bruto_153m_omzet73_empty_pnl_drop_52k_equity_jump_253m_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Hagewinde 0861.262.010 remine; NOT Ter Engelen 0430.882.809 remine; NOT CAR Waas 0415.472.279 remine; NOT Sakura 0684.613.726 remine; NOT Kaliber 0407.201.941 remine; NOT Begeleid Wonen Pajottenland 0423.884.258 remine; NOT INFANO 0477.578.411 remine; NOT MWP Pajottenland 0413.313.535 remine; NOT Savio Dilbeek 0472.564.501 remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Dominiek Savio remine; NOT CVDO 0433.927.322 remine; NOT CAR De Klinker Ieper 0430.535.290 remine; NOT Dennenhof 0410.252.590 remine; NOT Ten Anker 0414.679.849 remine; NOT WZC Ten Anker Nieuwpoort 0475.837.260 remine; NOT Bremdael 0435.234.149 remine; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT Vijverbeek 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT 3Wplus remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Huis Perrekes 0444.947.611 remine; NOT Sint-Augustinus Halle 0459.770.496 remine; NOT OLV Bornem 0436.595.020 remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Kaliber YE2024 remine; NOT Philippus Neri 0471.795.132 YE2024 Sint-Niklaas seat leftover-via-VE; NOT De Linde Ronse 0778.279.401 YE2024; NOT De Lindeboom 0435.015.702 remine; NOT De Maretak 0881.890.049 Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW Geel; NOT CAR Glorieux Werken Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT CAR Halle Asse 0425.788.230 remine; NOT Ascendere 0409.470.553 remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea commercial; NOT Orelia commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; NOT Sint Lodewijk remine; NOT De Vier Notelaars remine; NOT Lidwina remine; NOT Homevil remine; NOT Schoonderhage remine; NOT OpWeg Herentals 0443.580.604 YE2024; NOT AZ Herentals 0821.734.213 remine; NOT De Vlietoever BV 0898.596.122 commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; NOT Ter Bake Armonea commercial; NOT Evara 0406.633.304 remine; NOT Zorg-Saam 0470.673.890 remine leftover-via-VE Gent")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Revalidatiecentrum Ter Linde Bornem deposit 2026-00135692,http://cdn.staatsbladmonitor.be/2026pdf/2026-00135692.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2482; official native statutory PDF 49617 bytes 13p VKT-VZW 26.0.11 m04-f; header 02.06.2026; AV 20.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-04 02:32:03 UTC OpenPDF 1.3.26; CDN Last-Modified 11.06.2026; all 13p native; CDN 2026-00135692 GET 200 49617 MD5 4f68756fd85b79c62b971b9e0d55e2eb; VKT-VZW 6.1.3 6.2 6.5 6.6 7 8 niet dienstig; 6.1.1 6.1.2 6.3 6.4 6.7 6.8 present; prior-year RESTATED not identical (73 published YE2024 19920 now empty); euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Revalidatiecentrum Ter Linde 0431.331.383,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431331383,KBO Public Search FOD Economie,{DAY},official_register,tick2482; Actief; 1 VE zetel L. Van Kerckhovenstraat 62 2870 Puurs-Sint-Amands since 17.04.2026; VZW since 11.06.1985; begindatum 11.06.1985; RSZ-werkgever since 01.07.1986; RSZ2025 86.959 Andere ambulante revalidatieactiviteiten; FOI admin@revaterlinde.be; leftover mined city_bornem CAR; VE 2.155.715.726; YE2025 Kapelstraat 12 2880 Bornem; NOT De Linde Ronse remine; NOT OLV Bornem remine; NOT De Vlietoever BV commercial",
f"{SRC_SBM},NBB Consult / SBM fiche Revalidatiecentrum Ter Linde 0431331383 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0431331383,NBB Consult / SBM,{DAY},official_register,tick2482; deposit-id 2026-00135692 YE 01.01.2025-31.12.2025 filing 04.06.2026 published VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Reva Ter Linde FOI contact leftover city_bornem CAR,https://www.revaterlinde.be/,Revalidatiecentrum Ter Linde VZW leftover city_bornem CAR 1 VE,{DAY},foi_contact,tick2482; FOI admin@revaterlinde.be / directie@revaterlinde.be; tel 03 889 72 84; zetel L. Van Kerckhovenstraat 62 2870 Puurs-Sint-Amands; YE2025 Kapelstraat 12 2880 Bornem; 1 VE leftover mined city_bornem after Hagewinde lock; CAR Departement Zorg erkend; NOT De Linde Ronse remine; NOT OLV Bornem remine; NOT De Vlietoever BV commercial; NOT De Hagewinde remine; NOT BWP remine; NOT Kaliber remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},REVALIDATIECENTRUM TER LINDE VZW,ASBL Centre de revalidation Ter Linde,Reva Ter Linde VZW (leftover city_bornem CAR),parastatal,city_bornem,nl,https://www.revaterlinde.be/,admin@revaterlinde.be,L. Van Kerckhovenstraat 62 2870 Puurs-Sint-Amands,tick2482 YE2025 Strong official native NBB PDF deposit 2026-00135692 + Strong KBO 0431.331.383 Actief 1 VE; omzet70 empty VKT; 73 empty VKT restated; 76A empty; envelope bruto 9900 JUMP 1531992; pnl DROP 52313; 9901 DROP 68460; equity JUMP 2531410; assets JUMP 4224348; debt JUMP 1692938; FTE DROP 17.8; kapitaalsubsidies JUMP 1738223; destin691 empty; 791 empty; cash DROP 349806; geldbeleggingen JUMP 86527; capex 2880195; leftover city_bornem CAR 1 VE; zetel moved 17.04.2026 Puurs-Sint-Amands mined; prior-year RESTATED; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_ter_linde_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2482; PDF p5 native; YE2024 empty; 73 empty restated (published YE2024 19920)",
f"bud_ter_linde_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT; prior-year RESTATED vs published 19920),{SRC_PDF},strong,tick2482; PDF p5 native; YE2024 restated empty; published YE2024 deposit 2025-00157245 had 73 19920; FOI CAR/RIZIV/Departement Zorg matrix behind envelope 1531992",
f"bud_ter_linde_opbr_jr2025_statutory,{EID},2025,1531992,1531992,1531992,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +2.06% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2482; PDF p5 native; YE2024 1500999; 70 empty; 73 empty restated; 76A empty",
f"bud_ter_linde_bruto_jr2025_statutory,{EID},2025,1531992,1531992,1531992,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.06% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2482; PDF p5 native; YE2024 1500999; 76A empty; 73 empty restated",
f"bud_ter_linde_pnl_jr2025_statutory,{EID},2025,52313,52313,52313,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -45.94% (was 96767),{SRC_PDF},strong,tick2482; PDF p5 native; YE2024 96767; bedrijfswinst 9901 68460 DROP; destin691 empty",
f"bud_ter_linde_bedrijfswinst_jr2025_statutory,{EID},2025,68460,68460,68460,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -28.37% (was 95573),{SRC_PDF},strong,tick2482; PDF p5 native; YE2024 95573; 62 1389645 JUMP; 630 63065 JUMP; 66A empty; 640/8 10822 DROP; 635/9 empty; 631/4 empty",
f"bud_ter_linde_equity_jr2025_statutory,{EID},2025,2531410,2531410,2531410,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +221.19%,{SRC_PDF},strong,tick2482; PDF p4 native; YE2024 788142; kapitaalsubsidies 1738223 JUMP; overgedragen 14 793187 JUMP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_ter_linde_assets_jr2025_statutory,{EID},2025,4224348,4224348,4224348,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +233.98%,{SRC_PDF},strong,tick2482; PDF p3 native; YE2024 1264840 restated; MVA 22/27 3358544 JUMP; cash 349806 DROP; geldbeleggingen 86527 JUMP; aanbouw 27 empty; FVA 28 empty; LT recv 29 empty",
f"bud_ter_linde_debt_jr2025_statutory,{EID},2025,1692938,1692938,1692938,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +255.14%,{SRC_PDF},strong,tick2482; PDF p4 native; YE2024 476699; 17 447105 JUMP; 42/48 942866 JUMP; 43 300000",
f"bud_ter_linde_cash_jr2025_statutory,{EID},2025,349806,349806,349806,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -45.03%,{SRC_PDF},strong,tick2482; PDF p3 native; YE2024 636317; geldbeleggingen 50/53 86527 JUMP; capex 2880195",
f"bud_ter_linde_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 empty; 14 JUMP 793187),{SRC_PDF},strong,tick2482; PDF p6 native; YE2024 destin empty; 14P 740874 + 9905 52313 = 14 793187",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":1531992,\"\"2025_bruto\"\":1531992,"
"\"\"2025_pnl\"\":52313,\"\"2025_bedrijfswinst\"\":68460,"
"\"\"2025_equity\"\":2531410,\"\"2025_assets\"\":4224348,\"\"2025_debt\"\":1692938,"
"\"\"2025_fte\"\":17.8,\"\"2025_kapitaalsubsidies\"\":1738223,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":349806,\"\"2025_geldbeleggingen\"\":86527,"
"\"\"2025_personnel62\"\":1389645,\"\"2025_gebouwen22\"\":3346726,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":793187,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":63065,\"\"2025_capex\"\":2880195,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":819,\"\"2025_74\"\":0,"
"\"\"2025_731\"\":0,\"\"2025_733\"\":0,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":1500999,\"\"2024_bruto\"\":1500999,\"\"2024_pnl\"\":96767,\"\"2024_bedrijfswinst\"\":95573,"
"\"\"2024_equity\"\":788142,\"\"2024_assets\"\":1264840,"
"\"\"2024_debt\"\":476699,\"\"2024_cash\"\":636317,\"\"2024_fte\"\":18.1,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":47268,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":80501}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Reva Ter Linde YE2025 (bruto JUMP 1.53m / omzet+73 empty VKT / pnl DROP 52k / equity JUMP 2.53m / capex 2.88m / Strong PDF),{EID},Departement Zorg + leftover city_bornem CAR,Revalidatiecentrum Ter Linde VZW (KBO 0431.331.383; Actief; 1 VE; zetel Puurs-Sint-Amands; YE2025 Bornem),2026-05-20,2025,2025,1531992,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00135692.pdf,Public CAR dual of mined city_bornem,Publish CAR / RIZIV / Departement Zorg matrix behind bruto 1.53m and why equity JUMP 2.53m while pnl DROP 52313 and capex 2880195,{SRC_PDF},strong,Vlaanderen>Antwerpen>Bornem>Reva Ter Linde>JR2025_statutory_L5,tick2482; Strong official native PDF; leftover mined city_bornem CAR; 1 VE; prior-year RESTATED; NOT De Linde Ronse remine; NOT OLV Bornem remine; NOT De Vlietoever BV commercial; NOT De Hagewinde remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Reva Ter Linde bruto JUMP 1.53m / omzet+73 empty VKT / pnl DROP 52k / equity JUMP 2.53m / capex 2.88m (YE2025 leftover city_bornem CAR)",
"L5",
"car_vzw_statutory",
"Vlaanderen>Antwerpen>Bornem>Reva Ter Linde>JR2025",
"1531992",
"1531992",
"PDF envelope 1531992 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty restated; 76A empty; bedrijfswinst DROP 68460; pnl DROP 52313; equity JUMP 2531410; assets JUMP 4224348; debt JUMP 1692938; FTE 17.8; kapitaalsubsidies 1738223; destin691 empty; cash DROP 349806; capex 2880195; leftover city_bornem CAR",
"strong",
SRC_PDF,
"Departement Zorg + leftover city_bornem CAR",
"CAR leftover city_bornem",
"1.53m envelope; omzet+73 empty VKT; pnl DROP 52k; equity JUMP 2.53m; capex 2.88m; leftover city_bornem CAR",
"5.48",
"5.35",
"5.20",
"5.34",
"FOI CAR / RIZIV / Departement Zorg matrix behind envelope 1.53m + why 73 RESTATED empty vs published 19920 and why equity JUMP 2.53m while pnl DROP 52313 and capex 2880195",
"active",
"",
"tick2482 leftover mined city_bornem CAR after Hagewinde lock; 1 VE; zetel moved 17.04.2026 Puurs-Sint-Amands mined; prior-year RESTATED; NOT De Linde Ronse remine; NOT OLV Bornem remine; NOT De Vlietoever BV commercial; NOT De Hagewinde remine tick2481; NOT BWP remine tick2480; NOT Kaliber remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Bornem>Reva Ter Linde>CAR",
"entity_id": EID,
"what_is_missing": "CAR / RIZIV / Departement Zorg split behind envelope bruto 9900 1531992 (omzet empty VKT; 73 RESTATED empty vs published YE2024 19920) and why equity JUMP 2531410 while pnl DROP 52313 and capex 2880195 nieuwbouw plus kapitaalsubsidies JUMP 1738223",
"why_it_matters": "Strong official PDF leftover public CAR of mined city_bornem; VKT envelope bruto 1.53m because omzet empty; public CAR 1 VE Kapelstraat 12 Bornem then zetel Puurs-Sint-Amands; equity JUMP 2.53m / capex 2.88m / cash DROP 350k / 73 restated",
"priority": "8",
"recipient_body": "Revalidatiecentrum Ter Linde VZW / Raad van Bestuur",
"recipient_email": "admin@revaterlinde.be",
"recipient_postal": "L. Van Kerckhovenstraat 62 2870 Puurs-Sint-Amands",
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
"notes": "tick2482; ready NOT sent; Strong official native NBB PDF; leftover mined city_bornem CAR after Hagewinde lock; 1 VE; prior-year RESTATED; off De Linde Ronse remine; off OLV Bornem remine; off De Vlietoever BV commercial; off De Hagewinde remine; off BWP remine; off Kaliber remine; off CVDO remine; off Dennenhof remine; off Ten Anker remine; off Bremdael remine; off Armonea commercial; off Vulpia commercial; off Evara remine; off Zorg-Saam remine",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2482,")!=1: raise SystemExit(f"bad 2482 count {rq_raw.count(b'rq_2482,')}")
if b"rq_2483," in rq_raw: raise SystemExit("2483 exists")
idx=rq_raw.rfind(b"rq_2482,")
if idx<0: raise SystemExit("rq_2482 not found")
new_2482=(
"rq_2482,leftover dual Reva Ter Linde YE2025,hole_fill,8,done,L5,vzw_reva_ter_linde_bornem,"
"Took unused leftover public CAR Revalidatiecentrum Ter Linde 0431.331.383 leftover mined city_bornem. Official NBB VKT-VZW YE2025 2026-00135692 native statutory 13p. Envelope bruto 9900 JUMP 1531992 (omzet empty VKT; 73 RESTATED empty); pnl DROP 52313; equity JUMP 2531410; capex 2880195; destin 691 empty; FTE 17.8. NOT De Linde Ronse remine. NOT OLV Bornem remine. NOT De Vlietoever BV commercial. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2482 leftover mined city_bornem CAR; Strong native PDF; 1 VE; prior-year RESTATED; next every-10 is 2490\n"
)
new_2483=(
"rq_2483,leftover dual hunt after Reva Ter Linde,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: vilvoorde / mol / denderleeuw (WZC/VAPH leftover; skip Armonea Ter Bake/Rodenbach) / zoersel / schilde (Sint Lodewijk taken) / kalmthout (Bambi CIK taken; leftover WZC/VAPH; skip Vulpia Beukenhof / De Medemens remine) / dendermonde (Zonneschijn CIK taken; leftover WZC/VAPH/CAR; skip OCMW Aymonshof/De Cocon; skip Zorg-Saam/Broeders leftover-via-VE) / geel (Augustientjes CIK taken; leftover VAPH/CAR; WZC Zusterhof+Perrekes remine; skip Armonea Laarsveld / Vulpia Het Veld / OCMW Wedbos) / herentals (Bremdael WZC taken — leftover VAPH/CAR only; AZ already mined; OpWeg YE2024; Kaliber maatwerk remine) / knokke_heist (De Lindeboom + Duinhuisjes + CVDO taken) / waregem (Kindercentrum + t Zonnetje + Ten Anker taken) / schoten (De Vier Notelaars + Dennenhof taken) / dilbeek (Savio CIK + BWP VAPH taken) / lokeren (CAR Waas + Ter Engelen + Sakura + Hagewinde VAPH taken — different leftover type only) / eeklo (CAR Ascendere + KISME + Don Bosco taken; leftover WZC; skip Zorg-Saam Gent seat; Philippus Neri YE2024 Sint-Niklaas seat) / ronse (De Linde WZC YE2024 0778.279.401) / halle (CAR taken; Sint-Augustinus WZC remine; skip De Maretak Korian; Zonnig Huis city) / bornem (Reva Ter Linde CAR taken; OLV hospital remine; skip De Vlietoever BV; leftover WZC/VAPH only) / puurs_sint_amands (Reva Ter Linde current zetel — leftover CAR taken via Bornem write). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. OpWeg 0443.580.604 leftover city_herentals VAPH YE2024 — take ONLY if unused + official YE2025 native PDF. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. city_kapellen slug missing. WZC Joostens Zoersel = Zorgbedrijf Antwerpen not local VZW. Ter Bake / Rodenbach Denderleeuw Armonea commercial. De Vlietoever Bornem BV commercial. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT Ter Engelen remine. NOT CAR Waas remine. NOT Sakura remine. NOT Kaliber remine. NOT Begeleid Wonen Pajottenland remine. NOT INFANO remine. NOT MWP Lennik remine. NOT Savio remine. NOT EVA Dilbeek remine. NOT CVDO remine. NOT CAR De Klinker Ieper remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT WZC Ten Anker Nieuwpoort remine. NOT Bremdael remine. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Huis Perrekes remine. NOT Sint-Augustinus Halle remine. NOT OLV Bornem remine. NOT AZ Alma remine. NOT AZ Sint-Blasius remine. NOT Philippus Neri YE2024 leftover-via-VE. NOT De Linde Ronse YE2024. NOT De Maretak Korian commercial. NOT Het Veld Vulpia commercial. NOT Laarsveld Armonea commercial. NOT Wedbos OCMW. NOT CAR Glorieux remine. NOT CAR Wegwijs Kloosterstraat 6 Drongen. NOT CAR Halle Asse remine. NOT Ascendere remine. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private. NOT Armonea Vogelzang/Hemelrijck/Ter Bake commercial. NOT Orelia Koningshof commercial. NOT Stijn leftover-via-VE Hasselt remine. NOT Felies leftover-via-VE Brussels. NOT Klein Hemelrijk absorbed. NOT Sint Lodewijk remine. NOT De Lindeboom remine. NOT De Vier Notelaars remine. NOT Lidwina remine. NOT Homevil remine. NOT Schoonderhage remine. NOT AZ Herentals remine. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2482 leftover city_bornem CAR; Reva Ter Linde taken; De Hagewinde taken leftover mined city_lokeren VAPH; Begeleid Wonen Pajottenland taken leftover mined city_dilbeek VAPH; CVDO taken leftover mined city_knokke_heist CAR; Dennenhof taken leftover mined city_schoten VAPH; Ten Anker taken leftover mined city_waregem VAPH; Bremdael taken leftover mined city_herentals WZC; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2482.count("\n")!=1 or new_2483.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2482",new_2482),("2483",new_2483)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2482.encode("utf-8"))
    f.write(new_2483.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2482", chk.count(b"rq_2482,"), "n2483", chk.count(b"rq_2483,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2482,2482,no,tick2482 leftover dual Reva Ter Linde 0431.331.383 Strong native PDF (omzet70 empty VKT; 73 empty RESTATED vs published 19920; 76A empty; envelope bruto 9900 JUMP 1531992; pnl DROP 52313; 9901 DROP 68460; equity JUMP 2531410; assets JUMP 4224348; debt JUMP 1692938; FTE DROP 17.8; kapitaalsubsidies JUMP 1738223; destin691 empty; 791 empty; cash DROP 349806; geldbeleggingen JUMP 86527; capex 2880195; 1 VE leftover city_bornem CAR); leftover mined city_bornem CAR; zetel moved 17.04.2026 Puurs-Sint-Amands mined; prior-year RESTATED; NOT De Linde Ronse remine; NOT OLV Bornem remine; NOT De Vlietoever BV commercial; NOT De Hagewinde remine; NOT BWP remine; NOT Kaliber remine; NOT INFANO remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT Huis Perrekes remine; NOT Sint-Augustinus Halle remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri YE2024 leftover-via-VE; NOT De Maretak Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW; NOT CAR Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; next every-10 is 2490; next rq_2483 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2482 - rq_2482 Revalidatiecentrum Ter Linde Bornem (bruto JUMP 1.53m / omzet+73 empty VKT / pnl DROP 52k / equity JUMP 2.53m / capex 2.88m / Strong PDF)

- Unit: **rq_2482** leftover dual after **Hagewinde@2481**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of less-picked mined Flanders cities (CIK lists herentals/schoten/vilvoorde/mol exhausted at 2476; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde). Confirmed `city_bornem` / `city_puurs_sint_amands` / `city_denderleeuw` / `city_dendermonde` / `city_geel` / `city_herentals` / `city_kalmthout` / `city_eeklo` / `city_ronse` / `city_halle` exist (`city_kapellen` missing). FIRST locked: Revalidatiecentrum Ter Linde **0431.331.383** leftover city_bornem CAR unused YE2025 **2026-00135692** VKT 50kB — unused + leftover mined parent + official CDN GET **200** 49617 native extractable euros — **LOCKED**. Skips this hunt: Kaliber Herentals already mined tick2202; Huis Perrekes Geel remine tick2343; Sint-Augustinus Halle remine tick2085; OLV Bornem remine tick2065; AZ Alma remine tick2006; AZ Sint-Blasius remine tick2009; Philippus Neri / Avondzegen YE2024 Sint-Niklaas seat leftover-via-VE; De Linde Ronse YE2024; De Maretak Halle Korian commercial; Het Veld Geel Vulpia commercial; Laarsveld Geel Armonea commercial; Wedbos Geel OCMW; CAR Glorieux = Werken Glorieux remine; CAR Wegwijs Kloosterstraat 6 Drongen stay OFF; Ter Engelen already mined; Evara / Zorg-Saam leftover-via-VE Gent remine; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde. Identity trap: 0431.331.383 ≠ De Linde Ronse **0778.279.401** ≠ De Lindeboom **0435.015.702** ≠ OLV Bornem **0436.595.020** ≠ De Vlietoever BV **0898.596.122** ≠ De Hagewinde **0861.262.010** ≠ BWP **0423.884.258**. 1 VE leftover of mined city_bornem (YE2025 Kapelstraat 12; zetel moved 17.04.2026 L. Van Kerckhovenstraat 62 Puurs-Sint-Amands mined). Confirmed leftover public CAR not convent / not private / not CIK / not WZC / not VAPH. VKT-VZW native statutory (6.1.3 6.2 6.5 6.6 7 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00135692** (49617 B / 13p; AV **20.05.2026**; header **02.06.2026**; CDN GET **200** 49617 official NBB-generated OpenPDF 1.3.26 CreationDate 04.06.2026 Last-Modified 11.06.2026 MD5 4f68756fd85b79c62b971b9e0d55e2eb; statutory pages native; prior-year RESTATED not identical — 73 published YE2024 **19920** now empty) — omzet 70 **empty** VKT; 73 **empty** VKT restated; 76A **empty**; envelope bruto 9900 **EUR1531992** JUMP +2.06% (VKT because omzet empty; was 1500999); 62 **EUR1389645** JUMP +1.51%; 630 **EUR63065** JUMP +208.39%; 66A **empty**; 640/8 **EUR10822** DROP; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR68460** DROP −28.37% (was 95573); pnl 9904 **EUR52313** DROP −45.94% (was 96767); equity **EUR2531410** JUMP +221.19%; assets **EUR4224348** JUMP +233.98%; debt **EUR1692938** JUMP +255.14%; FTE **17.8** DROP −1.66% (was 18.1; 100 17.8; 105 19.7); kapitaalsubsidies **EUR1738223** JUMP +3577.38%; destin 691 **empty**; 791 **empty**; cash **EUR349806** DROP −45.03%; geldbeleggingen **EUR86527** JUMP +7.49%; gebouwen **EUR3346726** JUMP; MVA 22/27 **EUR3358544** JUMP; aanbouw **empty**; capex **EUR2880195**. Strong KBO + Strong PDF (native statutory; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_bornem CAR. NOT De Linde Ronse remine. NOT OLV Bornem remine. NOT De Vlietoever BV commercial. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT Bremdael remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Evara remine. NOT Zorg-Saam remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.34); entities (+1 vzw_reva_ter_linde_bornem); foi + draft `gap_ter_linde_bornem_car_matrix_bruto_1_53m_omzet73_empty_pnl_drop_44k_equity_jump_2_53m_capex_2_88m_l5`; rq_2482=done + rq_2483 open; loop_state ticks=2482; raw tick2482/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2483 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Reva Ter Linde remine / NOT De Linde Ronse remine / NOT OLV Bornem remine / NOT De Vlietoever BV commercial / NOT De Hagewinde remine / NOT BWP remine / NOT Kaliber remine / NOT CVDO remine / NOT Dennenhof remine / NOT Ten Anker remine / NOT Bremdael remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Evara remine / NOT Zorg-Saam remine / NOT Huis Perrekes remine / NOT Sint-Augustinus Halle remine).

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

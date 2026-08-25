from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2483_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_nektari_jr2025_nbb_pdf_2483"
SRC_KBO="src_nektari_kbo_2483"
SRC_SBM="src_nektari_sbm_2483"
SRC_SITE="src_nektari_site_2483"
EID="vzw_nektari_puurs"
GAP="gap_nektari_puurs_maatwerk_matrix_70_76A_35_76m_omzet_commercial_73_jump_20_15m_pnl_drop_97k_capex_5_34m_l5"
COMM="comm_nektari_jr2025_statutory_70_76A_3576m_73_jump_2015m_pnl_drop_97k_capex_534m"
LB="lb_nektari_70_76A_3576m_omzet_commercial_73_jump_2015m_pnl_drop_97k_capex_534m_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Reva Ter Linde 0431.331.383 remine tick2482; NOT De Hagewinde 0861.262.010 remine; NOT Ter Engelen 0430.882.809 remine; NOT CAR Waas 0415.472.279 remine; NOT Sakura 0684.613.726 remine; NOT Kaliber 0407.201.941 remine; NOT Begeleid Wonen Pajottenland 0423.884.258 remine; NOT INFANO 0477.578.411 remine; NOT MWP Pajottenland 0413.313.535 remine; NOT Savio Dilbeek 0472.564.501 remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Dominiek Savio remine; NOT CVDO 0433.927.322 remine; NOT CAR De Klinker Ieper 0430.535.290 remine; NOT Dennenhof 0410.252.590 remine; NOT Ten Anker 0414.679.849 remine; NOT WZC Ten Anker Nieuwpoort 0475.837.260 remine; NOT Bremdael 0435.234.149 remine; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT Vijverbeek 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT 3Wplus remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Huis Perrekes 0444.947.611 remine; NOT Sint-Augustinus Halle 0459.770.496 remine; NOT OLV Bornem 0436.595.020 remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri 0471.795.132 YE2024 Sint-Niklaas seat leftover-via-VE; NOT De Linde Ronse 0778.279.401 YE2024; NOT De Lindeboom 0435.015.702 remine; NOT De Maretak 0881.890.049 Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW Geel; NOT CAR Glorieux Werken Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT CAR Halle Asse 0425.788.230 remine; NOT Ascendere 0409.470.553 remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea commercial; NOT Orelia commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; NOT Sint Lodewijk remine; NOT De Vier Notelaars remine; NOT Lidwina remine; NOT Homevil remine; NOT Schoonderhage remine; NOT OpWeg Herentals 0443.580.604 YE2024; NOT AZ Herentals 0821.734.213 remine; NOT De Vlietoever BV 0898.596.122 commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; NOT Ter Bake Armonea commercial; NOT Evara 0406.633.304 remine; NOT Zorg-Saam 0470.673.890 remine leftover-via-VE Gent; NOT Aurora Dilbeek 0407.624.484 YE2024; NOT MPI Oosterlo 0414.326.293 remine; NOT Groep Talent remine; NOT Werkplus remine; NOT ARCOR remine; NOT m-accent remine; NOT Anemoon Korian commercial; NOT Gravenkasteel Armonea commercial")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Nektari Puurs-Sint-Amands deposit 2026-00131619,http://cdn.staatsbladmonitor.be/2026pdf/2026-00131619.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2483; official native statutory PDF 838023 bytes 60p VOL-VZW 25.0.12 m05-f; header 02.06.2026; AV 21.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-02 11:16:22 UTC OpenPDF 1.3.26; CDN Last-Modified 10.06.2026; statutory pages native; CDN 2026-00131619 GET 200 838023 MD5 d5b0fddfe4ec387f20b681740b624144; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.5.3 6.16 niet dienstig; prior-year identical not restated; commissaris Baker Tilly / Caluwaerts Christian; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Nektari 0407.231.239,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407231239,KBO Public Search FOD Economie,{DAY},official_register,tick2483; Actief; 12 VE zetel Pullaar 159 2870 Puurs-Sint-Amands since 01.01.2019; VZW since 01.01.1969; replaces 0408.698.711 closed 24.08.2011; RSZ-werkgever RSZ2025 88.993 beschutte/sociale werkplaatsen; FOI info@nektari.be; leftover mined city_puurs_sint_amands maatwerk; VE 2.152.791.373 campus Flexpack; NOT Reva Ter Linde remine; NOT De Vlietoever BV commercial; NOT OLV Bornem remine; NOT Aurora Dilbeek YE2024",
f"{SRC_SBM},NBB Consult / SBM fiche Nektari 0407231239 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0407231239,NBB Consult / SBM,{DAY},official_register,tick2483; deposit-id 2026-00131619 YE 01.01.2025-31.12.2025 filing VOL-VZW Volledig model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Nektari FOI contact leftover city_puurs_sint_amands maatwerk,https://nektari.be/,Nektari VZW leftover city_puurs_sint_amands maatwerk 12 VE,{DAY},foi_contact,tick2483; FOI info@nektari.be / zorg@nektari.be / werk@nektari.be; zetel Pullaar 159 2870 Puurs-Sint-Amands; campuses Flegado / t Onzent / Flexpack / Hof van Coolhem / WinkelAtelier / FietsLoket all Puurs-Sint-Amands; leftover mined city_puurs_sint_amands maatwerk after Ter Linde lock; NOT Reva Ter Linde remine; NOT De Vlietoever BV commercial; NOT OLV Bornem remine; NOT Aurora Dilbeek YE2024; NOT De Hagewinde remine; NOT BWP remine; NOT Kaliber remine; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},NEKTARI VZW,ASBL Nektari,Nektari VZW (leftover city_puurs_sint_amands maatwerk),parastatal,city_puurs_sint_amands,nl,https://nektari.be/,info@nektari.be,Pullaar 159 2870 Puurs-Sint-Amands,tick2483 YE2025 Strong official native NBB PDF deposit 2026-00131619 + Strong KBO 0407.231.239 Actief 12 VE; omzet70 11798237 commercial-only vs large 73; 73 JUMP 20146273; 76A empty; envelope 70/76A JUMP 35757169; pnl DROP 97311; 9901 DROP 207507; equity DROP 25368618; assets JUMP 36837953; debt JUMP 10074829; FTE DROP 602.8; kapitaalsubsidies DROP 1484219; destin691 97311; 791 empty; cash DROP 4085850; geldbeleggingen JUMP 3827873; capex 5339046; aanbouw JUMP 4159253; leftover city_puurs_sint_amands maatwerk 12 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_nektari_omzet_jr2025_statutory,{EID},2025,11798237,11798237,11798237,NBB VOL-VZW code 70 omzet YE2025 DROP -16.12% (commercial-only vs large 73),{SRC_PDF},strong,tick2483; PDF p6 native; YE2024 14064959; 73 JUMP 20146273; 76A empty",
f"bud_nektari_73_jr2025_statutory,{EID},2025,20146273,20146273,20146273,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +11.52%,{SRC_PDF},strong,tick2483; PDF p6 native; YE2024 18064825; 731 15536; 733 20130737; FOI VDAB/maatwerk/VAPH matrix behind 73",
f"bud_nektari_opbr_jr2025_statutory,{EID},2025,35757169,35757169,35757169,NBB VOL-VZW envelope 70/76A YE2025 JUMP +0.57% (VZW envelope because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2483; PDF p6 native; YE2024 35553646; 70 11798237; 73 20146273; 76A empty; 74 2279758",
f"bud_nektari_bruto_jr2025_statutory,{EID},2025,35757169,35757169,35757169,NBB VOL-VZW 70/76A bedrijfsopbrengsten YE2025 JUMP +0.57% (VOL envelope; omzet commercial-only vs large 73),{SRC_PDF},strong,tick2483; PDF p6 native; YE2024 35553646; 76A empty; 73 JUMP 20146273",
f"bud_nektari_pnl_jr2025_statutory,{EID},2025,97311,97311,97311,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -83.74% (was 598608),{SRC_PDF},strong,tick2483; PDF p7 native; YE2024 598608; bedrijfswinst 9901 207507 DROP; destin691 97311",
f"bud_nektari_bedrijfswinst_jr2025_statutory,{EID},2025,207507,207507,207507,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -64.38% (was 582598),{SRC_PDF},strong,tick2483; PDF p6 native; YE2024 582598; 62 25825921 JUMP; 630 1229165 JUMP; 66A empty; 640/8 195867 DROP; 635/9 237125; 631/4 36741",
f"bud_nektari_equity_jr2025_statutory,{EID},2025,25368618,25368618,25368618,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -0.08%,{SRC_PDF},strong,tick2483; PDF p5 native; YE2024 25388341; kapitaalsubsidies 1484219 DROP; overgedragen 14 empty; fondsen 10 833962 FLAT; bestemde fondsen 13 23050437 JUMP",
f"bud_nektari_assets_jr2025_statutory,{EID},2025,36837953,36837953,36837953,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +3.91%,{SRC_PDF},strong,tick2483; PDF p4 native; YE2024 35451311; MVA 22/27 20470597 JUMP; cash 4085850 DROP; geldbeleggingen 3827873 JUMP; aanbouw 27 4159253 JUMP; FVA 28 1874506; LT recv 29 29771",
f"bud_nektari_debt_jr2025_statutory,{EID},2025,10074829,10074829,10074829,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +13.13%,{SRC_PDF},strong,tick2483; PDF p5 native; YE2024 8905589; 17 4756615 JUMP; 42/48 5317400 DROP",
f"bud_nektari_cash_jr2025_statutory,{EID},2025,4085850,4085850,4085850,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -34.61%,{SRC_PDF},strong,tick2483; PDF p4 native; YE2024 6248394; geldbeleggingen 50/53 3827873 JUMP; capex 5339046",
f"bud_nektari_destin_jr2025_statutory,{EID},2025,97311,97311,97311,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 DROP (791 empty; 13 JUMP 23050437),{SRC_PDF},strong,tick2483; PDF p8 native; YE2024 destin 598608; 791 empty; 14 empty",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":11798237,\"\"2025_73\"\":20146273,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":35757169,\"\"2025_bruto\"\":35757169,"
"\"\"2025_pnl\"\":97311,\"\"2025_bedrijfswinst\"\":207507,"
"\"\"2025_equity\"\":25368618,\"\"2025_assets\"\":36837953,\"\"2025_debt\"\":10074829,"
"\"\"2025_fte\"\":602.8,\"\"2025_kapitaalsubsidies\"\":1484219,\"\"2025_destin691\"\":97311,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":4085850,\"\"2025_geldbeleggingen\"\":3827873,"
"\"\"2025_personnel62\"\":25825921,\"\"2025_gebouwen22\"\":14861346,"
"\"\"2025_aanbouw27\"\":4159253,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":833962,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":23050437,"
"\"\"2025_voorzieningen16\"\":1394506,\"\"2025_630\"\":1229165,\"\"2025_capex\"\":5339046,"
"\"\"2025_ltrecv29\"\":29771,\"\"2025_75\"\":82299,\"\"2025_74\"\":2279758,"
"\"\"2025_731\"\":15536,\"\"2025_733\"\":20130737,"
"\"\"2024_omzet\"\":14064959,\"\"2024_73\"\":18064825,"
"\"\"2024_opbr70_76A\"\":35553646,\"\"2024_bruto\"\":35553646,\"\"2024_pnl\"\":598608,\"\"2024_bedrijfswinst\"\":582598,"
"\"\"2024_equity\"\":25388341,\"\"2024_assets\"\":35451311,"
"\"\"2024_debt\"\":8905589,\"\"2024_cash\"\":6248394,\"\"2024_fte\"\":604.8,"
"\"\"2024_destin691\"\":598608,\"\"2024_kapitaalsubsidies\"\":1613961,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":3772023}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Nektari YE2025 (70/76A JUMP 35.76m / omzet commercial vs 73 JUMP 20.15m / pnl DROP 97k / capex 5.34m / Strong PDF),{EID},VDAB + leftover city_puurs_sint_amands maatwerk,Nektari VZW (KBO 0407.231.239; Actief; 12 VE; zetel Puurs-Sint-Amands),2026-05-21,2025,2025,35757169,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00131619.pdf,Public maatwerk dual of mined city_puurs_sint_amands,Publish VDAB / maatwerk / VAPH matrix behind 70/76A 35.76m and why pnl DROP 97311 while capex 5339046 and omzet DROP 11798237,{SRC_PDF},strong,Vlaanderen>Antwerpen>Puurs-Sint-Amands>Nektari>JR2025_statutory_L5,tick2483; Strong official native PDF; leftover mined city_puurs_sint_amands maatwerk; 12 VE; prior-year identical; NOT Reva Ter Linde remine; NOT De Vlietoever BV commercial; NOT OLV Bornem remine; NOT Aurora Dilbeek YE2024; NOT De Hagewinde remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Nektari 70/76A JUMP 35.76m / omzet commercial vs 73 JUMP 20.15m / pnl DROP 97k / capex 5.34m (YE2025 leftover city_puurs_sint_amands maatwerk)",
"L5",
"maatwerk_vzw_statutory",
"Vlaanderen>Antwerpen>Puurs-Sint-Amands>Nektari>JR2025",
"35757169",
"35757169",
"PDF envelope 35757169 = 70/76A VZW because omzet commercial-only vs large 73; 70 11798237; 73 20146273; 76A empty; bedrijfswinst DROP 207507; pnl DROP 97311; equity DROP 25368618; assets JUMP 36837953; debt JUMP 10074829; FTE 602.8; kapitaalsubsidies 1484219; destin691 97311; cash DROP 4085850; capex 5339046; leftover city_puurs_sint_amands maatwerk",
"strong",
SRC_PDF,
"VDAB + leftover city_puurs_sint_amands maatwerk",
"maatwerk leftover city_puurs_sint_amands",
"35.76m envelope; omzet commercial vs 73 20.15m; pnl DROP 97k; capex 5.34m; leftover city_puurs_sint_amands maatwerk",
"5.70",
"5.58",
"5.32",
"5.53",
"FOI VDAB / maatwerk / VAPH matrix behind envelope 35.76m + why omzet commercial-only DROP 11.80m vs 73 JUMP 20.15m and why pnl DROP 97311 while capex 5339046 and cash DROP 4085850",
"active",
"",
"tick2483 leftover mined city_puurs_sint_amands maatwerk after Ter Linde lock; 12 VE; prior-year identical; NOT Reva Ter Linde remine tick2482; NOT De Vlietoever BV commercial; NOT OLV Bornem remine; NOT Aurora Dilbeek YE2024; NOT De Hagewinde remine tick2481; NOT BWP remine tick2480; NOT Kaliber remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Puurs-Sint-Amands>Nektari>maatwerk",
"entity_id": EID,
"what_is_missing": "VDAB / maatwerkdecreet / VAPH split behind envelope 70/76A 35757169 (omzet 70 11798237 commercial-only vs large 73 20146273) and why pnl DROP 97311 while capex 5339046 aanbouw JUMP 4159253 and cash DROP 4085850",
"why_it_matters": "Strong official PDF leftover public maatwerk of mined city_puurs_sint_amands; VOL envelope 35.76m because omzet commercial-only vs large 73; public maatwerk 12 VE Pullaar 159; pnl DROP 97k / capex 5.34m / cash DROP 4.09m / omzet DROP 16pct",
"priority": "8",
"recipient_body": "Nektari VZW / Raad van Bestuur",
"recipient_email": "info@nektari.be",
"recipient_postal": "Pullaar 159 2870 Puurs-Sint-Amands",
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
"notes": "tick2483; ready NOT sent; Strong official native NBB PDF; leftover mined city_puurs_sint_amands maatwerk after Ter Linde lock; 12 VE; prior-year identical; off Reva Ter Linde remine; off De Vlietoever BV commercial; off OLV Bornem remine; off Aurora Dilbeek YE2024; off De Hagewinde remine; off BWP remine; off Kaliber remine; off CVDO remine; off Dennenhof remine; off Ten Anker remine; off Bremdael remine; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
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
if rq_raw.count(b"rq_2483,")!=1: raise SystemExit(f"bad 2483 count {rq_raw.count(b'rq_2483,')}")
if b"rq_2484," in rq_raw: raise SystemExit("2484 exists")
idx=rq_raw.rfind(b"rq_2483,")
if idx<0: raise SystemExit("rq_2483 not found")
new_2483=(
"rq_2483,leftover dual Nektari YE2025,hole_fill,8,done,L5,vzw_nektari_puurs,"
"Took unused leftover public maatwerk Nektari 0407.231.239 leftover mined city_puurs_sint_amands. Official NBB VOL-VZW YE2025 2026-00131619 native statutory 60p. Envelope 70/76A JUMP 35757169 (omzet 11798237 commercial-only vs large 73 JUMP 20146273); pnl DROP 97311; capex 5339046; destin 691 97311; FTE 602.8. NOT Reva Ter Linde remine. NOT De Vlietoever BV commercial. NOT OLV Bornem remine. NOT Aurora Dilbeek YE2024. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2483 leftover mined city_puurs_sint_amands maatwerk; Strong native PDF; 12 VE; prior-year identical; next every-10 is 2490\n"
)
new_2484=(
"rq_2484,leftover dual hunt after Nektari,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: vilvoorde / mol / denderleeuw (WZC/VAPH leftover; skip Armonea Ter Bake/Rodenbach) / zoersel / schilde (Sint Lodewijk taken) / kalmthout (Bambi CIK taken; leftover WZC/VAPH; skip Vulpia Beukenhof / De Medemens remine) / dendermonde (Zonneschijn CIK taken; leftover VAPH/CAR; skip OCMW Aymonshof/De Cocon; skip Zorg-Saam/Broeders leftover-via-VE) / geel (Augustientjes CIK taken; leftover VAPH/CAR; WZC Zusterhof+Perrekes remine; skip Armonea Laarsveld / Vulpia Het Veld / OCMW Wedbos / MPI Oosterlo remine) / herentals (Bremdael WZC taken — leftover VAPH/CAR only; AZ already mined; OpWeg YE2024; Kaliber maatwerk remine) / knokke_heist (De Lindeboom + Duinhuisjes + CVDO taken) / waregem (Kindercentrum + t Zonnetje + Ten Anker taken) / schoten (De Vier Notelaars + Dennenhof taken) / dilbeek (Savio CIK + BWP VAPH taken; Aurora maatwerk YE2024 skip unless YE2025) / lokeren (CAR Waas + Ter Engelen + Sakura + Hagewinde VAPH taken — different leftover type only) / eeklo (CAR Ascendere + KISME + Don Bosco taken; leftover WZC; skip Zorg-Saam Gent seat; Philippus Neri YE2024 Sint-Niklaas seat) / ronse (De Linde WZC YE2024 0778.279.401) / halle (CAR taken; Sint-Augustinus WZC remine; skip De Maretak Korian; Zonnig Huis city) / bornem (Reva Ter Linde CAR taken; OLV hospital remine; skip De Vlietoever BV; leftover WZC/VAPH only) / puurs_sint_amands (Nektari maatwerk taken; Reva Ter Linde current zetel — leftover CAR taken via Bornem write; leftover WZC/VAPH only; skip Anemoon Korian / Gravenkasteel Armonea). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende / Aurora Dilbeek 0407.624.484 still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. OpWeg 0443.580.604 leftover city_herentals VAPH YE2024 — take ONLY if unused + official YE2025 native PDF. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. city_kapellen slug missing. WZC Joostens Zoersel = Zorgbedrijf Antwerpen not local VZW. Ter Bake / Rodenbach Denderleeuw Armonea commercial. De Vlietoever Bornem BV commercial. Anemoon Puurs Korian commercial. Gravenkasteel Puurs Armonea commercial. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT Ter Engelen remine. NOT CAR Waas remine. NOT Sakura remine. NOT Kaliber remine. NOT Begeleid Wonen Pajottenland remine. NOT INFANO remine. NOT MWP Lennik remine. NOT Savio remine. NOT EVA Dilbeek remine. NOT CVDO remine. NOT CAR De Klinker Ieper remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT WZC Ten Anker Nieuwpoort remine. NOT Bremdael remine. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Huis Perrekes remine. NOT Sint-Augustinus Halle remine. NOT OLV Bornem remine. NOT AZ Alma remine. NOT AZ Sint-Blasius remine. NOT Philippus Neri YE2024 leftover-via-VE. NOT De Linde Ronse YE2024. NOT De Maretak Korian commercial. NOT Het Veld Vulpia commercial. NOT Laarsveld Armonea commercial. NOT Wedbos OCMW. NOT CAR Glorieux remine. NOT CAR Wegwijs Kloosterstraat 6 Drongen. NOT CAR Halle Asse remine. NOT Ascendere remine. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private. NOT Armonea Vogelzang/Hemelrijck/Ter Bake/Gravenkasteel commercial. NOT Orelia Koningshof commercial. NOT Korian Anemoon commercial. NOT Stijn leftover-via-VE Hasselt remine. NOT Felies leftover-via-VE Brussels. NOT Klein Hemelrijk absorbed. NOT Sint Lodewijk remine. NOT De Lindeboom remine. NOT De Vier Notelaars remine. NOT Lidwina remine. NOT Homevil remine. NOT Schoonderhage remine. NOT AZ Herentals remine. NOT Evara remine. NOT Zorg-Saam remine. NOT MPI Oosterlo remine. NOT Groep Talent remine. NOT Werkplus remine. NOT ARCOR remine. NOT Aurora Dilbeek YE2024.,"
f",{STAMP},{STAMP},spawned after tick2483 leftover city_puurs_sint_amands maatwerk; Nektari taken; Reva Ter Linde taken leftover mined city_bornem CAR; De Hagewinde taken leftover mined city_lokeren VAPH; Begeleid Wonen Pajottenland taken leftover mined city_dilbeek VAPH; CVDO taken leftover mined city_knokke_heist CAR; Dennenhof taken leftover mined city_schoten VAPH; Ten Anker taken leftover mined city_waregem VAPH; Bremdael taken leftover mined city_herentals WZC; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2483.count("\n")!=1 or new_2484.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2483",new_2483),("2484",new_2484)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2483.encode("utf-8"))
    f.write(new_2484.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2483", chk.count(b"rq_2483,"), "n2484", chk.count(b"rq_2484,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2483,2483,no,tick2483 leftover dual Nektari 0407.231.239 Strong native PDF (omzet70 11798237 commercial-only vs large 73 JUMP 20146273; 76A empty; envelope 70/76A JUMP 35757169; pnl DROP 97311; 9901 DROP 207507; equity DROP 25368618; assets JUMP 36837953; debt JUMP 10074829; FTE DROP 602.8; kapitaalsubsidies DROP 1484219; destin691 97311; 791 empty; cash DROP 4085850; geldbeleggingen JUMP 3827873; capex 5339046; aanbouw JUMP 4159253; 12 VE leftover city_puurs_sint_amands maatwerk); leftover mined city_puurs_sint_amands maatwerk; prior-year identical; NOT Reva Ter Linde remine; NOT De Vlietoever BV commercial; NOT OLV Bornem remine; NOT Aurora Dilbeek YE2024; NOT De Hagewinde remine; NOT BWP remine; NOT Kaliber remine; NOT INFANO remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT Huis Perrekes remine; NOT Sint-Augustinus Halle remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri YE2024 leftover-via-VE; NOT De Maretak Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW; NOT CAR Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT MPI Oosterlo remine; NOT Groep Talent remine; NOT Anemoon Korian commercial; NOT Gravenkasteel Armonea commercial; next every-10 is 2490; next rq_2484 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2483 - rq_2483 Nektari Puurs-Sint-Amands (70/76A JUMP 35.76m / omzet commercial vs 73 JUMP 20.15m / pnl DROP 97k / capex 5.34m / Strong PDF)

- Unit: **rq_2483** leftover dual after **Ter Linde@2482**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of less-picked mined Flanders cities (CIK lists herentals/schoten/vilvoorde/mol exhausted at 2476; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde). Confirmed `city_bornem` / `city_puurs_sint_amands` / `city_denderleeuw` / `city_dendermonde` / `city_geel` / `city_herentals` / `city_kalmthout` / `city_eeklo` / `city_ronse` / `city_halle` exist (`city_kapellen` missing). FIRST locked: Nektari **0407.231.239** leftover city_puurs_sint_amands maatwerk unused YE2025 **2026-00131619** VOL 838kB — unused + leftover mined parent + official CDN GET **200** 838023 native extractable euros — **LOCKED**. Skips this hunt: Reva Ter Linde remine tick2482; OLV Bornem remine; De Vlietoever BV commercial; Anemoon Puurs Korian commercial; Gravenkasteel Puurs Armonea commercial; Sint-Vincentius Kalmthout = De Medemens remine; Beukenhof Kalmthout Vulpia commercial; MPI Oosterlo Geel remine tick2300; Huis Perrekes remine; Het Eepos OCMW JR2024; De Linde Ronse YE2024; Ter Engelen remine; Aurora Dilbeek YE2024; Kaliber remine; Groep Talent / Werkplus / ARCOR / m-accent already mined; Philippus Neri leftover-via-VE; Evara / Zorg-Saam leftover-via-VE Gent remine; Dendermonde WZCs city/OCMW or leftover-via-VE Gent; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde. Identity trap: 0407.231.239 ≠ Reva Ter Linde **0431.331.383** ≠ De Vlietoever BV **0898.596.122** ≠ OLV Bornem **0436.595.020** ≠ Aurora Dilbeek **0407.624.484** ≠ De Hagewinde **0861.262.010** ≠ BWP **0423.884.258**. 12 VE leftover of mined city_puurs_sint_amands (zetel Pullaar 159 + campuses all Puurs-Sint-Amands). Confirmed leftover public maatwerk not convent / not private / not CIK / not WZC / not commercial NV. VOL-VZW native statutory (6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.5.3 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00131619** (838023 B / 60p; AV **21.05.2026**; header **02.06.2026**; CDN GET **200** 838023 official NBB-generated OpenPDF 1.3.26 CreationDate 02.06.2026 Last-Modified 10.06.2026 MD5 d5b0fddfe4ec387f20b681740b624144; statutory pages native; prior-year identical not restated; commissaris Baker Tilly / Caluwaerts Christian) — omzet 70 **EUR11798237** DROP −16.12% (commercial-only vs large 73; was 14064959); 73 **EUR20146273** JUMP +11.52% (was 18064825; 731 15536; 733 20130737); 76A **empty**; envelope 70/76A **EUR35757169** JUMP +0.57% (VZW envelope because omzet commercial-only vs large 73; was 35553646); 74 **EUR2279758** JUMP; 62 **EUR25825921** JUMP +2.22%; 630 **EUR1229165** JUMP +9.79%; 66A **empty**; 640/8 **EUR195867** DROP; 635/9 **EUR237125**; 631/4 **EUR36741**; bedrijfswinst 9901 **EUR207507** DROP −64.38% (was 582598); pnl 9904 **EUR97311** DROP −83.74% (was 598608); equity **EUR25368618** DROP −0.08%; assets **EUR36837953** JUMP +3.91%; debt **EUR10074829** JUMP +13.13%; FTE **602.8** DROP −0.33% (was 604.8; 1003 602.8; 9086 679; 105 601.3); kapitaalsubsidies **EUR1484219** DROP −8.04%; destin 691 **EUR97311**; 791 **empty**; cash **EUR4085850** DROP −34.61%; geldbeleggingen **EUR3827873** JUMP; gebouwen **EUR14861346** DROP; MVA 22/27 **EUR20470597** JUMP; aanbouw **EUR4159253** JUMP; capex **EUR5339046**. Strong KBO + Strong PDF (native statutory; not SBM table; not Companyweb euros). Site: 12 VE leftover mined city_puurs_sint_amands maatwerk. NOT Reva Ter Linde remine. NOT De Vlietoever BV commercial. NOT OLV Bornem remine. NOT Aurora Dilbeek YE2024. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT Bremdael remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.53); entities (+1 vzw_nektari_puurs); foi + draft `gap_nektari_puurs_maatwerk_matrix_70_76A_35_76m_omzet_commercial_73_jump_20_15m_pnl_drop_97k_capex_5_34m_l5`; rq_2483=done + rq_2484 open; loop_state ticks=2483; raw tick2483/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2484 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Nektari remine / NOT Reva Ter Linde remine / NOT De Vlietoever BV commercial / NOT OLV Bornem remine / NOT Aurora Dilbeek YE2024 / NOT De Hagewinde remine / NOT BWP remine / NOT Kaliber remine / NOT CVDO remine / NOT Dennenhof remine / NOT Ten Anker remine / NOT Bremdael remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine / NOT Huis Perrekes remine / NOT Sint-Augustinus Halle remine / NOT MPI Oosterlo remine).

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

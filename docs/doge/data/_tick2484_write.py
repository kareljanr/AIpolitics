from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2484_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_grijkoort_jr2025_nbb_pdf_2484"
SRC_KBO="src_grijkoort_kbo_2484"
SRC_SBM="src_grijkoort_sbm_2484"
SRC_SITE="src_grijkoort_site_2484"
EID="vzw_grijkoort_werkplaats_ronse"
GAP="gap_grijkoort_ronse_maatwerk_matrix_omzet_2_20m_73_jump_2_14m_pnl_improved_loss_63k_cash_jump_291k_l5"
COMM="comm_grijkoort_jr2025_statutory_omzet_220m_73_jump_214m_pnl_improved_loss_63k_cash_jump_291k"
LB="lb_grijkoort_omzet_220m_73_jump_214m_pnl_improved_loss_63k_cash_jump_291k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Nektari 0407.231.239 remine tick2483; NOT Reva Ter Linde 0431.331.383 remine tick2482; NOT De Hagewinde 0861.262.010 remine; NOT Ter Engelen 0430.882.809 remine; NOT CAR Waas 0415.472.279 remine; NOT Sakura 0684.613.726 remine; NOT Kaliber 0407.201.941 remine; NOT Begeleid Wonen Pajottenland 0423.884.258 remine; NOT INFANO 0477.578.411 remine; NOT MWP Pajottenland 0413.313.535 remine; NOT Savio Dilbeek 0472.564.501 remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Dominiek Savio remine; NOT CVDO 0433.927.322 remine; NOT CAR De Klinker Ieper 0430.535.290 remine; NOT Dennenhof 0410.252.590 remine; NOT Ten Anker 0414.679.849 remine; NOT WZC Ten Anker Nieuwpoort 0475.837.260 remine; NOT Bremdael 0435.234.149 remine; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT Vijverbeek 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT 3Wplus remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Huis Perrekes 0444.947.611 remine; NOT Sint-Augustinus Halle 0459.770.496 remine; NOT OLV Bornem 0436.595.020 remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri 0471.795.132 YE2024 Sint-Niklaas seat leftover-via-VE; NOT De Linde Ronse 0778.279.401 YE2024; NOT De Lindeboom 0435.015.702 remine; NOT De Maretak 0881.890.049 Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW Geel; NOT CAR Glorieux Werken Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT CAR Halle Asse 0425.788.230 remine; NOT Ascendere 0409.470.553 remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea commercial; NOT Orelia commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; NOT Sint Lodewijk remine; NOT De Vier Notelaars remine; NOT Lidwina remine; NOT Homevil remine; NOT Schoonderhage remine; NOT OpWeg Herentals 0443.580.604 YE2024; NOT AZ Herentals 0821.734.213 remine; NOT De Vlietoever BV 0898.596.122 commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; NOT Ter Bake Armonea commercial; NOT Evara 0406.633.304 remine; NOT Zorg-Saam 0470.673.890 remine leftover-via-VE Gent; NOT Aurora Dilbeek 0407.624.484 YE2024; NOT MPI Oosterlo 0414.326.293 remine; NOT Groep Talent remine; NOT Werkplus remine; NOT ARCOR 0410.962.274 remine; NOT m-accent remine; NOT Anemoon Korian commercial; NOT Gravenkasteel Armonea commercial; NOT Grijkoort Begeleid Werk 0443.074.521 unused sister; NOT GR.O.O.D. 0885.458.164 unused sister; NOT De Verlosser Dilbeek remine; NOT Het Witte Huis 0443.655.432 YE2024; NOT AZ Sint-Dimpna Geel 0844.179.716 no NBB deposits; NOT Kasteelhof Dendermonde Korian commercial; NOT PARCOER 0683.817.138 GGZ not leftover dual type; NOT De Klokke leftover-via-VE Sint-Niklaas; NOT Vrienden van Thomas leftover-via-VE Antwerpen; NOT Kiemkracht remine; NOT Huize Eyckerheyde remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Grijkoort-Werkplaats Ronse deposit 2026-00312145,http://cdn.staatsbladmonitor.be/2026pdf/2026-00312145.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2484; official native statutory PDF 416958 bytes 25p VKT-VZW 25.0.13 m04-f; header 16.07.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-21 01:05:56 UTC OpenPDF 1.3.26; CDN Last-Modified 03.08.2026; statutory pages native; CDN 2026-00312145 GET 200 416958 MD5 7ae44e2eb0e2da95084f976d3d5c7e96; VKT-VZW 7 niet dienstig; prior-year identical not restated; commissaris A&C Bedrijfsrevisor B00348 / De Clercq Bert; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Grijkoort-Werkplaats 0463.374.146,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0463374146,KBO Public Search FOD Economie,{DAY},official_register,tick2484; Actief; 3 VE zetel Peperstraat 8 9600 Ronse since 18.03.2009; VZW since 12.05.1998; RSZ-werkgever RSZ2025 88.993 beschutte/sociale werkplaatsen; FOI info@grijkoort.be; leftover mined city_ronse maatwerk; VE 2.152.443.955 Peperstraat 8 Ronse + 2.258.507.121 Klein Frankrijk 3 Ronse + 2.152.256.883 Kerkstraat 7 Kluisbergen; NOT Grijkoort Begeleid Werk 0443.074.521 unused sister; NOT GR.O.O.D. 0885.458.164 unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Nektari remine",
f"{SRC_SBM},NBB Consult / SBM fiche Grijkoort 0463374146 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0463374146,NBB Consult / SBM,{DAY},official_register,tick2484; deposit-id 2026-00312145 YE 01.01.2025-31.12.2025 filing VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar still 2024 deposit-id discovery via NBB OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Grijkoort FOI contact leftover city_ronse maatwerk,https://www.grijkoort.be/,Grijkoort-Werkplaats VZW leftover city_ronse maatwerk 3 VE,{DAY},foi_contact,tick2484; FOI info@grijkoort.be; T 055 23 24 56; zetel Peperstraat 8 9600 Ronse; Voorzitter Delbar Georges; Directeur Jan Foulon; leftover mined city_ronse maatwerk after Nektari lock; NOT Grijkoort Begeleid Werk unused sister; NOT GR.O.O.D. unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Nektari remine; NOT Reva Ter Linde remine; NOT Aurora Dilbeek YE2024; NOT De Hagewinde remine; NOT BWP remine; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},GRIJKOORT - WERKPLAATS VZW,ASBL Grijkoort-Werkplaats,Grijkoort-Werkplaats VZW (leftover city_ronse maatwerk),parastatal,city_ronse,nl,https://www.grijkoort.be/,info@grijkoort.be,Peperstraat 8 9600 Ronse,tick2484 YE2025 Strong official native NBB PDF deposit 2026-00312145 + Strong KBO 0463.374.146 Actief 3 VE; omzet70 2196591 material not commercial-only; 73 JUMP 2136864; 76A 2500; envelope omzet 70 JUMP 2196591; bruto JUMP 3690614; pnl IMPROVED LOSS -63323; 9901 IMPROVED -70106; equity DROP 1694909; assets DROP 2405959; debt DROP 711050; FTE DROP 96.7; kapitaalsubsidies DROP 20314; destin691 empty; 791 empty; cash JUMP 291319; geldbeleggingen JUMP 449999; capex 58475; leftover city_ronse maatwerk 3 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_grijkoort_omzet_jr2025_statutory,{EID},2025,2196591,2196591,2196591,NBB VKT-VZW code 70 omzet YE2025 JUMP +10.92% (material not commercial-only),{SRC_PDF},strong,tick2484; PDF p5 native; YE2024 1980362; 73 JUMP 2136864; 76A 2500",
f"bud_grijkoort_73_jr2025_statutory,{EID},2025,2136864,2136864,2136864,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +3.57%,{SRC_PDF},strong,tick2484; PDF p5 native; YE2024 2063256; FOI VDAB/maatwerk matrix behind 73",
f"bud_grijkoort_opbr_jr2025_statutory,{EID},2025,2196591,2196591,2196591,NBB VKT-VZW envelope omzet 70 YE2025 JUMP +10.92% (VZW envelope because omzet material not commercial-only),{SRC_PDF},strong,tick2484; PDF p5 native; YE2024 1980362; 70 2196591; 73 2136864; 76A 2500",
f"bud_grijkoort_bruto_jr2025_statutory,{EID},2025,3690614,3690614,3690614,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +9.93%,{SRC_PDF},strong,tick2484; PDF p5 native; YE2024 3357161; 76A 2500; 73 JUMP 2136864",
f"bud_grijkoort_pnl_jr2025_statutory,{EID},2025,-63323,-63323,-63323,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 IMPROVED LOSS (was -364987),{SRC_PDF},strong,tick2484; PDF p5 native; YE2024 -364987; bedrijfswinst 9901 -70106 IMPROVED; destin691 empty",
f"bud_grijkoort_bedrijfswinst_jr2025_statutory,{EID},2025,-70106,-70106,-70106,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 IMPROVED (was -392400),{SRC_PDF},strong,tick2484; PDF p5 native; YE2024 -392400; 62 3606935 JUMP; 630 158617 DROP; 66A empty; 640/8 21859 JUMP; 635/9 -26691; 631/4 empty",
f"bud_grijkoort_equity_jr2025_statutory,{EID},2025,1694909,1694909,1694909,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -3.88%,{SRC_PDF},strong,tick2484; PDF p4 native; YE2024 1763402; kapitaalsubsidies 20314 DROP; overgedragen 14 745460 DROP; fondsen 10 empty; bestemde fondsen 13 929135 FLAT",
f"bud_grijkoort_assets_jr2025_statutory,{EID},2025,2405959,2405959,2405959,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -4.96%,{SRC_PDF},strong,tick2484; PDF p3 native; YE2024 2531556; MVA 22/27 1013454 DROP; cash 291319 JUMP; geldbeleggingen 449999 JUMP; aanbouw 27 empty; FVA 28 38810; LT recv 29 empty",
f"bud_grijkoort_debt_jr2025_statutory,{EID},2025,711050,711050,711050,NBB VKT-VZW code 17/49 schulden YE2025 DROP -4.10%,{SRC_PDF},strong,tick2484; PDF p4 native; YE2024 741463; 17 empty (was 16666); 42/48 634516 DROP",
f"bud_grijkoort_cash_jr2025_statutory,{EID},2025,291319,291319,291319,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +120.21%,{SRC_PDF},strong,tick2484; PDF p3 native; YE2024 132290; geldbeleggingen 50/53 449999 JUMP; capex 58475",
f"bud_grijkoort_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 FLAT 929135),{SRC_PDF},strong,tick2484; PDF p6 native; YE2024 destin empty; 791 empty; 14 745460 DROP",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":2196591,\"\"2025_73\"\":2136864,\"\"2025_76A\"\":2500,"
"\"\"2025_opbr70\"\":2196591,\"\"2025_bruto\"\":3690614,"
"\"\"2025_pnl\"\":-63323,\"\"2025_bedrijfswinst\"\":-70106,"
"\"\"2025_equity\"\":1694909,\"\"2025_assets\"\":2405959,\"\"2025_debt\"\":711050,"
"\"\"2025_fte\"\":96.7,\"\"2025_kapitaalsubsidies\"\":20314,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":291319,\"\"2025_geldbeleggingen\"\":449999,"
"\"\"2025_personnel62\"\":3606935,\"\"2025_gebouwen22\"\":855593,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":745460,"
"\"\"2025_bestemdefondsen13\"\":929135,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":158617,\"\"2025_capex\"\":58475,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":6029,\"\"2025_60_61\"\":724235,"
"\"\"2024_omzet\"\":1980362,\"\"2024_73\"\":2063256,"
"\"\"2024_opbr70\"\":1980362,\"\"2024_bruto\"\":3357161,\"\"2024_pnl\"\":-364987,\"\"2024_bedrijfswinst\"\":-392400,"
"\"\"2024_equity\"\":1763402,\"\"2024_assets\"\":2531556,"
"\"\"2024_debt\"\":741463,\"\"2024_cash\"\":132290,\"\"2024_fte\"\":99,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":25485,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":445160}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Grijkoort YE2025 (omzet JUMP 2.20m / 73 JUMP 2.14m / pnl IMPROVED LOSS 63k / cash JUMP 291k / Strong PDF),{EID},VDAB + leftover city_ronse maatwerk,Grijkoort-Werkplaats VZW (KBO 0463.374.146; Actief; 3 VE; zetel Ronse),2026-06-25,2025,2025,2196591,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00312145.pdf,Public maatwerk dual of mined city_ronse,Publish VDAB / maatwerk matrix behind omzet 2.20m and 73 2.14m and why pnl IMPROVED LOSS -63323 while cash JUMP 291319,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Ronse>Grijkoort-Werkplaats>JR2025_statutory_L5,tick2484; Strong official native PDF; leftover mined city_ronse maatwerk; 3 VE; prior-year identical; NOT Nektari remine; NOT Grijkoort Begeleid Werk unused sister; NOT GR.O.O.D. unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Reva Ter Linde remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Grijkoort omzet JUMP 2.20m / 73 JUMP 2.14m / pnl IMPROVED LOSS 63k / cash JUMP 291k (YE2025 leftover city_ronse maatwerk)",
"L5",
"maatwerk_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Ronse>Grijkoort-Werkplaats>JR2025",
"2196591",
"2196591",
"PDF envelope 2196591 = omzet 70 VZW because omzet material not commercial-only; 70 2196591; 73 2136864; 76A 2500; bruto 3690614; bedrijfswinst IMPROVED -70106; pnl IMPROVED LOSS -63323; equity DROP 1694909; assets DROP 2405959; debt DROP 711050; FTE 96.7; kapitaalsubsidies 20314; destin691 empty; cash JUMP 291319; capex 58475; leftover city_ronse maatwerk",
"strong",
SRC_PDF,
"VDAB + leftover city_ronse maatwerk",
"maatwerk leftover city_ronse",
"2.20m envelope; 73 2.14m; pnl IMPROVED LOSS 63k; cash JUMP 291k; leftover city_ronse maatwerk",
"5.52",
"5.40",
"5.26",
"5.39",
"FOI VDAB / maatwerk matrix behind envelope omzet 2.20m + 73 JUMP 2.14m and why pnl IMPROVED LOSS -63323 while cash JUMP 291319 and FTE DROP 96.7",
"active",
"",
"tick2484 leftover mined city_ronse maatwerk after Nektari lock; 3 VE; prior-year identical; NOT Nektari remine tick2483; NOT Grijkoort Begeleid Werk 0443.074.521 unused sister; NOT GR.O.O.D. 0885.458.164 unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Reva Ter Linde remine tick2482; NOT De Hagewinde remine tick2481; NOT BWP remine tick2480; NOT Kaliber remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Ronse>Grijkoort-Werkplaats>maatwerk",
"entity_id": EID,
"what_is_missing": "VDAB / maatwerkdecreet split behind envelope omzet 70 2196591 (material not commercial-only vs 73 2136864) and why pnl IMPROVED LOSS -63323 while cash JUMP 291319 and FTE DROP 96.7",
"why_it_matters": "Strong official PDF leftover public maatwerk of mined city_ronse; VKT envelope omzet 2.20m because not commercial-only; public maatwerk 3 VE Peperstraat 8; pnl IMPROVED LOSS 63k / cash JUMP 291k / 73 JUMP 2.14m / omzet JUMP 10.92pct",
"priority": "8",
"recipient_body": "GRIJKOORT - WERKPLAATS VZW / Raad van Bestuur",
"recipient_email": "info@grijkoort.be",
"recipient_postal": "Peperstraat 8 9600 Ronse",
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
"notes": "tick2484; ready NOT sent; Strong official native NBB PDF; leftover mined city_ronse maatwerk after Nektari lock; 3 VE; prior-year identical; off Nektari remine; off Grijkoort Begeleid Werk unused sister; off GR.O.O.D. unused sister; off ARCOR remine; off De Linde Ronse YE2024; off Reva Ter Linde remine; off De Hagewinde remine; off BWP remine; off Kaliber remine; off CVDO remine; off Dennenhof remine; off Ten Anker remine; off Bremdael remine; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
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
if rq_raw.count(b"rq_2484,")!=1: raise SystemExit(f"bad 2484 count {rq_raw.count(b'rq_2484,')}")
if b"rq_2485," in rq_raw: raise SystemExit("2485 exists")
idx=rq_raw.rfind(b"rq_2484,")
if idx<0: raise SystemExit("rq_2484 not found")
new_2484=(
"rq_2484,leftover dual Grijkoort YE2025,hole_fill,8,done,L5,vzw_grijkoort_werkplaats_ronse,"
"Took unused leftover public maatwerk Grijkoort-Werkplaats 0463.374.146 leftover mined city_ronse. Official NBB VKT-VZW YE2025 2026-00312145 native statutory 25p. Envelope omzet 70 JUMP 2196591 (material not commercial-only vs 73 JUMP 2136864); pnl IMPROVED LOSS -63323; cash JUMP 291319; bruto JUMP 3690614; FTE 96.7. NOT Nektari remine. NOT Grijkoort Begeleid Werk unused sister. NOT GR.O.O.D. unused sister. NOT ARCOR remine. NOT De Linde Ronse YE2024. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2484 leftover mined city_ronse maatwerk; Strong native PDF; 3 VE; prior-year identical; next every-10 is 2490\n"
)
new_2485=(
"rq_2485,leftover dual hunt after Grijkoort,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: vilvoorde / mol / denderleeuw (WZC/VAPH leftover; skip Armonea Ter Bake/Rodenbach) / zoersel / schilde (Sint Lodewijk taken) / kalmthout (Bambi CIK taken; leftover WZC/VAPH; skip Vulpia Beukenhof / De Medemens remine) / dendermonde (Zonneschijn CIK taken; leftover VAPH/CAR; skip OCMW Aymonshof/De Cocon; skip Zorg-Saam/Broeders leftover-via-VE; skip Kasteelhof Korian; PARCOER GGZ not leftover dual type) / geel (Augustientjes CIK taken; leftover VAPH/CAR; WZC Zusterhof+Perrekes remine; skip Armonea Laarsveld / Vulpia Het Veld / OCMW Wedbos / MPI Oosterlo remine; AZ Sint-Dimpna 0844.179.716 no NBB deposits) / herentals (Bremdael WZC taken — leftover VAPH/CAR only; AZ already mined; OpWeg YE2024; Kaliber maatwerk remine) / knokke_heist (De Lindeboom + Duinhuisjes + CVDO taken) / waregem (Kindercentrum + t Zonnetje + Ten Anker taken) / schoten (De Vier Notelaars + Dennenhof taken) / dilbeek (Savio CIK + BWP VAPH taken; leftover WZC; Aurora maatwerk YE2024 skip unless YE2025; De Verlosser remine; Het Witte Huis 0443.655.432 YE2024; skip Quietas/Koning Albert Armonea / Maria Assumpta Vulpia / Dilhome Orelia / Breugheldal OCMW) / lokeren (CAR Waas + Ter Engelen + Sakura + Hagewinde VAPH taken — different leftover type only) / eeklo (CAR Ascendere + KISME + Don Bosco taken; leftover WZC; skip Zorg-Saam Gent seat; Philippus Neri YE2024 Sint-Niklaas seat; Kinderlach YE2024) / ronse (Grijkoort-Werkplaats maatwerk taken; De Linde WZC YE2024 0778.279.401; Grijkoort Begeleid Werk 0443.074.521 unused sister — take ONLY if unused + official YE2025 native PDF; GR.O.O.D. 0885.458.164 unused sister) / halle (CAR taken; Sint-Augustinus WZC remine; skip De Maretak Korian; Zonnig Huis city) / bornem (Reva Ter Linde CAR taken; OLV hospital remine; skip De Vlietoever BV / Huize Eyckerheyde remine; leftover WZC/VAPH only) / puurs_sint_amands (Nektari maatwerk taken; Reva Ter Linde current zetel — leftover CAR taken via Bornem write; leftover WZC/VAPH only; skip Anemoon Korian / Gravenkasteel Armonea / Zorgbedrijf Klein-Brabant remine). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende / Aurora Dilbeek 0407.624.484 / Het Witte Huis Dilbeek / OpWeg Herentals still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. city_kapellen slug missing. WZC Joostens Zoersel = Zorgbedrijf Antwerpen not local VZW. Ter Bake / Rodenbach Denderleeuw Armonea commercial. De Vlietoever Bornem BV commercial. Anemoon Puurs Korian commercial. Gravenkasteel Puurs Armonea commercial. NOT Grijkoort-Werkplaats remine. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT Ter Engelen remine. NOT CAR Waas remine. NOT Sakura remine. NOT Kaliber remine. NOT Begeleid Wonen Pajottenland remine. NOT INFANO remine. NOT MWP Lennik remine. NOT Savio remine. NOT EVA Dilbeek remine. NOT CVDO remine. NOT CAR De Klinker Ieper remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT WZC Ten Anker Nieuwpoort remine. NOT Bremdael remine. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Huis Perrekes remine. NOT Sint-Augustinus Halle remine. NOT OLV Bornem remine. NOT AZ Alma remine. NOT AZ Sint-Blasius remine. NOT Philippus Neri YE2024 leftover-via-VE. NOT De Linde Ronse YE2024. NOT De Maretak Korian commercial. NOT Het Veld Vulpia commercial. NOT Laarsveld Armonea commercial. NOT Wedbos OCMW. NOT CAR Glorieux remine. NOT CAR Wegwijs Kloosterstraat 6 Drongen. NOT CAR Halle Asse remine. NOT Ascendere remine. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private. NOT Armonea Vogelzang/Hemelrijck/Ter Bake/Gravenkasteel commercial. NOT Orelia Koningshof commercial. NOT Korian Anemoon commercial. NOT Stijn leftover-via-VE Hasselt remine. NOT Felies leftover-via-VE Brussels. NOT Klein Hemelrijk absorbed. NOT Sint Lodewijk remine. NOT De Lindeboom remine. NOT De Vier Notelaars remine. NOT Lidwina remine. NOT Homevil remine. NOT Schoonderhage remine. NOT AZ Herentals remine. NOT Evara remine. NOT Zorg-Saam remine. NOT MPI Oosterlo remine. NOT Groep Talent remine. NOT Werkplus remine. NOT ARCOR remine. NOT Aurora Dilbeek YE2024. NOT De Verlosser Dilbeek remine. NOT Kiemkracht remine. NOT PARCOER GGZ. NOT AZ Sint-Dimpna no deposits.,"
f",{STAMP},{STAMP},spawned after tick2484 leftover city_ronse maatwerk; Grijkoort-Werkplaats taken; Nektari taken leftover mined city_puurs_sint_amands maatwerk; Reva Ter Linde taken leftover mined city_bornem CAR; De Hagewinde taken leftover mined city_lokeren VAPH; Begeleid Wonen Pajottenland taken leftover mined city_dilbeek VAPH; CVDO taken leftover mined city_knokke_heist CAR; Dennenhof taken leftover mined city_schoten VAPH; Ten Anker taken leftover mined city_waregem VAPH; Bremdael taken leftover mined city_herentals WZC; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2484.count("\n")!=1 or new_2485.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2484",new_2484),("2485",new_2485)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2484.encode("utf-8"))
    f.write(new_2485.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2484", chk.count(b"rq_2484,"), "n2485", chk.count(b"rq_2485,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2484,2484,no,tick2484 leftover dual Grijkoort-Werkplaats 0463.374.146 Strong native PDF (omzet70 2196591 material not commercial-only vs 73 JUMP 2136864; 76A 2500; envelope omzet 70 JUMP 2196591; bruto JUMP 3690614; pnl IMPROVED LOSS -63323; 9901 IMPROVED -70106; equity DROP 1694909; assets DROP 2405959; debt DROP 711050; FTE DROP 96.7; kapitaalsubsidies DROP 20314; destin691 empty; 791 empty; cash JUMP 291319; geldbeleggingen JUMP 449999; capex 58475; 3 VE leftover city_ronse maatwerk); leftover mined city_ronse maatwerk; prior-year identical; NOT Nektari remine; NOT Grijkoort Begeleid Werk unused sister; NOT GR.O.O.D. unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Kaliber remine; NOT INFANO remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT Huis Perrekes remine; NOT Sint-Augustinus Halle remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri YE2024 leftover-via-VE; NOT De Maretak Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW; NOT CAR Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT MPI Oosterlo remine; NOT Groep Talent remine; NOT Anemoon Korian commercial; NOT Gravenkasteel Armonea commercial; NOT De Verlosser Dilbeek remine; NOT Het Witte Huis YE2024; NOT AZ Sint-Dimpna no deposits; NOT PARCOER GGZ; next every-10 is 2490; next rq_2485 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2484 - rq_2484 Grijkoort-Werkplaats Ronse (omzet JUMP 2.20m / 73 JUMP 2.14m / pnl IMPROVED LOSS 63k / cash JUMP 291k / Strong PDF)

- Unit: **rq_2484** leftover dual after **Nektari@2483**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of less-picked mined Flanders cities (CIK lists herentals/schoten/vilvoorde/mol exhausted at 2476; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde). Confirmed `city_ronse` / `city_bornem` / `city_puurs_sint_amands` / `city_denderleeuw` / `city_dendermonde` / `city_geel` / `city_herentals` / `city_kalmthout` / `city_eeklo` / `city_halle` / `city_dilbeek` exist (`city_kapellen` missing). FIRST locked: Grijkoort-Werkplaats **0463.374.146** leftover city_ronse maatwerk unused YE2025 **2026-00312145** VKT 417kB — unused + leftover mined parent + official CDN GET **200** 416958 native extractable euros — **LOCKED**. Skips this hunt: leftover WZC/VAPH of city_puurs_sint_amands (Anemoon Korian / Gravenkasteel Armonea commercial; Zorgbedrijf Klein-Brabant remine; Nektari maatwerk taken). Leftover WZC/VAPH of city_bornem (OLV remine; De Vlietoever BV; Huize Eyckerheyde remine; Ter Linde CAR taken). Dilbeek leftover WZC: De Verlosser remine; Het Witte Huis **0443.655.432** YE2024; Quietas/Koning Albert Armonea; Maria Assumpta Vulpia; Dilhome Orelia; Breugheldal OCMW; Aurora YE2024. OpWeg Herentals still YE2024. De Linde Ronse still YE2024. Kinderlach Eeklo still YE2024. AZ Sint-Dimpna Geel **0844.179.716** no NBB deposits (AVI). Kasteelhof Dendermonde Korian CommV. De Klokke leftover-via-VE Sint-Niklaas. Vrienden van Thomas leftover-via-VE Antwerpen. PARCOER **0683.817.138** YE2025 GGZ not leftover dual type. Kiemkracht remine. leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde. Identity trap: 0463.374.146 ≠ Grijkoort Begeleid Werk **0443.074.521** ≠ GR.O.O.D. **0885.458.164** ≠ ARCOR **0410.962.274** remine ≠ De Linde Ronse **0778.279.401** YE2024 ≠ Nektari **0407.231.239** ≠ Reva Ter Linde **0431.331.383** ≠ De Vlietoever BV **0898.596.122** ≠ OLV Bornem **0436.595.020** ≠ Aurora Dilbeek **0407.624.484** ≠ De Hagewinde **0861.262.010** ≠ BWP **0423.884.258**. 3 VE leftover of mined city_ronse (zetel Peperstraat 8 + Klein Frankrijk 3 Ronse + 1 VE Kerkstraat 7 Kluisbergen). Confirmed leftover public maatwerk not convent / not private / not CIK / not WZC / not commercial NV. VKT-VZW native statutory (7 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00312145** (416958 B / 25p; AV **25.06.2026**; header **16.07.2026**; CDN GET **200** 416958 official NBB-generated OpenPDF 1.3.26 CreationDate 21.07.2026 Last-Modified 03.08.2026 MD5 7ae44e2eb0e2da95084f976d3d5c7e96; statutory pages native; prior-year identical not restated; commissaris A&C Bedrijfsrevisor / De Clercq Bert) — omzet 70 **EUR2196591** JUMP +10.92% (material not commercial-only; was 1980362); 73 **EUR2136864** JUMP +3.57% (was 2063256); 76A **EUR2500** JUMP (was empty); envelope omzet 70 **EUR2196591** JUMP +10.92% (VZW envelope because omzet material not commercial-only); bruto 9900 **EUR3690614** JUMP +9.93% (was 3357161); 62 **EUR3606935** JUMP +2.33%; 630 **EUR158617** DROP −11.66%; 66A **empty**; 640/8 **EUR21859** JUMP; 635/9 **EUR-26691**; 631/4 **empty**; bedrijfswinst 9901 **EUR-70106** IMPROVED (was −392400); pnl 9904 **EUR-63323** IMPROVED LOSS (was −364987); equity **EUR1694909** DROP −3.88%; assets **EUR2405959** DROP −4.96%; debt **EUR711050** DROP −4.10%; FTE **96.7** DROP −2.32% (was 99; 100 96.7; 9087 96.7; 105 95); kapitaalsubsidies **EUR20314** DROP −20.29%; destin 691 **empty**; 791 **empty**; cash **EUR291319** JUMP +120.21%; geldbeleggingen **EUR449999** JUMP; gebouwen **EUR855593** DROP; MVA 22/27 **EUR1013454** DROP; aanbouw **empty**; capex **EUR58475**. Strong KBO + Strong PDF (native statutory; not SBM table; not Companyweb euros). Site: 3 VE leftover mined city_ronse maatwerk. NOT Nektari remine. NOT Grijkoort Begeleid Werk unused sister. NOT GR.O.O.D. unused sister. NOT ARCOR remine. NOT De Linde Ronse YE2024. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT Bremdael remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.39); entities (+1 vzw_grijkoort_werkplaats_ronse); foi + draft `gap_grijkoort_ronse_maatwerk_matrix_omzet_2_20m_73_jump_2_14m_pnl_improved_loss_63k_cash_jump_291k_l5`; rq_2484=done + rq_2485 open; loop_state ticks=2484; raw tick2484/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2485 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Grijkoort-Werkplaats remine / NOT Nektari remine / NOT Grijkoort Begeleid Werk unless unused + official YE2025 native PDF / NOT GR.O.O.D. unless unused + official YE2025 / NOT ARCOR remine / NOT De Linde Ronse YE2024 / NOT Reva Ter Linde remine / NOT De Vlietoever BV commercial / NOT OLV Bornem remine / NOT Aurora Dilbeek YE2024 / NOT De Hagewinde remine / NOT BWP remine / NOT Kaliber remine / NOT CVDO remine / NOT Dennenhof remine / NOT Ten Anker remine / NOT Bremdael remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine / NOT Huis Perrekes remine / NOT Sint-Augustinus Halle remine / NOT MPI Oosterlo remine).

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

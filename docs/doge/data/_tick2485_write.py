from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2485_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_grijkoort_begeleid_jr2025_nbb_pdf_2485"
SRC_KBO="src_grijkoort_begeleid_kbo_2485"
SRC_SBM="src_grijkoort_begeleid_sbm_2485"
SRC_SITE="src_grijkoort_begeleid_site_2485"
EID="vzw_grijkoort_begeleid_werk_ronse"
GAP="gap_grijkoort_begeleid_ronse_vaph_matrix_omzet_574k_73_jump_1_07m_pnl_flip_loss_28k_cash_drop_651k_l5"
COMM="comm_grijkoort_begeleid_jr2025_statutory_omzet_574k_73_jump_107m_pnl_flip_loss_28k_cash_drop_651k"
LB="lb_grijkoort_begeleid_omzet_574k_73_jump_107m_pnl_flip_loss_28k_cash_drop_651k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Grijkoort-Werkplaats 0463.374.146 remine tick2484; NOT Nektari 0407.231.239 remine tick2483; NOT Reva Ter Linde 0431.331.383 remine tick2482; NOT De Hagewinde 0861.262.010 remine; NOT Ter Engelen 0430.882.809 remine; NOT CAR Waas 0415.472.279 remine; NOT Sakura 0684.613.726 remine; NOT Kaliber 0407.201.941 remine; NOT Begeleid Wonen Pajottenland 0423.884.258 remine; NOT INFANO 0477.578.411 remine; NOT MWP Pajottenland 0413.313.535 remine; NOT Savio Dilbeek 0472.564.501 remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Dominiek Savio remine; NOT CVDO 0433.927.322 remine; NOT CAR De Klinker Ieper 0430.535.290 remine; NOT Dennenhof 0410.252.590 remine; NOT Ten Anker 0414.679.849 remine; NOT WZC Ten Anker Nieuwpoort 0475.837.260 remine; NOT Bremdael 0435.234.149 remine; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT Vijverbeek 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT 3Wplus remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO and ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Huis Perrekes 0444.947.611 remine; NOT Sint-Augustinus Halle 0459.770.496 remine; NOT OLV Bornem 0436.595.020 remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri 0471.795.132 YE2024 Sint-Niklaas seat leftover-via-VE; NOT De Linde Ronse 0778.279.401 YE2024; NOT De Lindeboom 0435.015.702 remine; NOT De Maretak 0881.890.049 Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW Geel; NOT CAR Glorieux Werken Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT CAR Halle Asse 0425.788.230 remine; NOT Ascendere 0409.470.553 remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea commercial; NOT Orelia commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; NOT Sint Lodewijk remine; NOT De Vier Notelaars remine; NOT Lidwina remine; NOT Homevil remine; NOT Schoonderhage remine; NOT OpWeg Herentals 0443.580.604 YE2024; NOT AZ Herentals 0821.734.213 remine; NOT De Vlietoever BV 0898.596.122 commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; NOT Ter Bake Armonea commercial; NOT Evara 0406.633.304 remine; NOT Zorg-Saam 0470.673.890 remine leftover-via-VE Gent; NOT Aurora Dilbeek 0407.624.484 YE2024; NOT MPI Oosterlo 0414.326.293 remine; NOT Groep Talent remine; NOT Werkplus remine; NOT ARCOR 0410.962.274 remine; NOT m-accent remine; NOT Anemoon Korian commercial; NOT Gravenkasteel Armonea commercial; NOT GR.O.O.D. 0885.458.164 unused sister; NOT De Verlosser Dilbeek remine; NOT Het Witte Huis 0443.655.432 YE2024; NOT AZ Sint-Dimpna Geel 0844.179.716 no NBB deposits; NOT Kasteelhof Dendermonde Korian commercial; NOT PARCOER 0683.817.138 GGZ not leftover dual type; NOT De Klokke leftover-via-VE Sint-Niklaas; NOT Vrienden van Thomas leftover-via-VE Antwerpen; NOT Kiemkracht remine; NOT Huize Eyckerheyde remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Grijkoort Begeleid Werk Ronse deposit 2026-00311391,http://cdn.staatsbladmonitor.be/2026pdf/2026-00311391.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2485; official native statutory PDF 574322 bytes 20p VKT-VZW 25.0.13 m04-f; header 16.07.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-20 22:15:24 UTC OpenPDF 1.3.26; CDN Last-Modified 03.08.2026; statutory pages native; CDN 2026-00311391 GET 200 574322 MD5 4ab1aa831bee8095d1612680a0842944; VKT-VZW 6.2 6.3 6.5 7 niet dienstig; prior-year identical not restated; commissaris A&C Bedrijfsrevisor B00348 / De Clercq Bert; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Grijkoort Begeleid Werk 0443.074.521,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443074521,KBO Public Search FOD Economie,{DAY},official_register,tick2485; Actief; 6 VE zetel Peperstraat 8 9600 Ronse since 18.03.2009; VZW since 22.02.1990; RSZ-werkgever RSZ2025 85.592 Beroepsopleiding; FOI info@grijkoort.be; leftover mined city_ronse VAPH begeleid werken; VE 2.152.262.823 Peperstraat 8 Ronse; NOT Grijkoort-Werkplaats 0463.374.146 remine tick2484; NOT GR.O.O.D. 0885.458.164 unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Nektari remine",
f"{SRC_SBM},NBB Consult / SBM fiche Grijkoort Begeleid Werk 0443074521 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0443074521,NBB Consult / SBM,{DAY},official_register,tick2485; deposit-id 2026-00311391 YE 01.01.2025-31.12.2025 filing VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar still 2024 deposit-id discovery via NBB OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table not Busibee",
f"{SRC_SITE},Grijkoort Begeleid Werk FOI contact leftover city_ronse VAPH,https://www.grijkoort.be/,Grijkoort Begeleid Werk VZW leftover city_ronse VAPH 6 VE,{DAY},foi_contact,tick2485; FOI info@grijkoort.be; privacy@grijkoort.be; T 055 23 24 51; zetel Peperstraat 8 9600 Ronse; Voorzitter Delbar Georges; leftover mined city_ronse VAPH after Grijkoort-Werkplaats lock; NOT Grijkoort-Werkplaats remine; NOT GR.O.O.D. unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Nektari remine; NOT Reva Ter Linde remine; NOT Aurora Dilbeek YE2024; NOT De Hagewinde remine; NOT BWP remine; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},GRIJKOORT - BEGELEID WERK VZW,ASBL Grijkoort-Begeleid-Werk,Grijkoort Begeleid Werk VZW (leftover city_ronse VAPH),parastatal,city_ronse,nl,https://www.grijkoort.be/,info@grijkoort.be,Peperstraat 8 9600 Ronse,tick2485 YE2025 Strong official native NBB PDF deposit 2026-00311391 + Strong KBO 0443.074.521 Actief 6 VE; omzet70 573569 material not commercial-only; 73 JUMP 1067194; 76A empty; envelope omzet 70 JUMP 573569; bruto JUMP 1226150; pnl FLIP LOSS -27867; 9901 FLIP LOSS -34045; equity DROP 347538; assets DROP 859037; debt DROP 473906; FTE DROP 26.9; kapitaalsubsidies JUMP 25219; destin691 empty; 791 empty; cash DROP 651158; geldbeleggingen empty; capex 36970; leftover city_ronse VAPH 6 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_grijkoort_begeleid_omzet_jr2025_statutory,{EID},2025,573569,573569,573569,NBB VKT-VZW code 70 omzet YE2025 JUMP +1.27% (material not commercial-only),{SRC_PDF},strong,tick2485; PDF p5 native; YE2024 566366; 73 JUMP 1067194; 76A empty",
f"bud_grijkoort_begeleid_73_jr2025_statutory,{EID},2025,1067194,1067194,1067194,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +0.76%,{SRC_PDF},strong,tick2485; PDF p5 native; YE2024 1059110; FOI VAPH/VDAB begeleid-werken matrix behind 73",
f"bud_grijkoort_begeleid_opbr_jr2025_statutory,{EID},2025,573569,573569,573569,NBB VKT-VZW envelope omzet 70 YE2025 JUMP +1.27% (VZW envelope because omzet material not commercial-only),{SRC_PDF},strong,tick2485; PDF p5 native; YE2024 566366; 70 573569; 73 1067194; 76A empty",
f"bud_grijkoort_begeleid_bruto_jr2025_statutory,{EID},2025,1226150,1226150,1226150,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.37%,{SRC_PDF},strong,tick2485; PDF p5 native; YE2024 1197756; 76A empty; 73 JUMP 1067194",
f"bud_grijkoort_begeleid_pnl_jr2025_statutory,{EID},2025,-27867,-27867,-27867,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 FLIP LOSS (was +23425),{SRC_PDF},strong,tick2485; PDF p5 native; YE2024 23425; bedrijfswinst 9901 -34045 FLIP LOSS; destin691 empty",
f"bud_grijkoort_begeleid_bedrijfswinst_jr2025_statutory,{EID},2025,-34045,-34045,-34045,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 FLIP LOSS (was +15277),{SRC_PDF},strong,tick2485; PDF p5 native; YE2024 15277; 62 1219940 JUMP; 630 35323 JUMP; 66A empty; 66B 1103; 640/8 4932 DROP; 635/9 empty; 631/4 empty",
f"bud_grijkoort_begeleid_equity_jr2025_statutory,{EID},2025,347538,347538,347538,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -7.34%,{SRC_PDF},strong,tick2485; PDF p4 native; YE2024 375052; kapitaalsubsidies 25219 JUMP; overgedragen 14 322319 DROP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_grijkoort_begeleid_assets_jr2025_statutory,{EID},2025,859037,859037,859037,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -21.31%,{SRC_PDF},strong,tick2485; PDF p3 native; YE2024 1091674; MVA 22/27 107500 JUMP; cash 651158 DROP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 1250; LT recv 29 empty",
f"bud_grijkoort_begeleid_debt_jr2025_statutory,{EID},2025,473906,473906,473906,NBB VKT-VZW code 17/49 schulden YE2025 DROP -30.21%,{SRC_PDF},strong,tick2485; PDF p4 native; YE2024 679029; 17 empty; 42/48 463283 DROP",
f"bud_grijkoort_begeleid_cash_jr2025_statutory,{EID},2025,651158,651158,651158,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -25.33%,{SRC_PDF},strong,tick2485; PDF p3 native; YE2024 872025; geldbeleggingen 50/53 empty; capex 36970",
f"bud_grijkoort_begeleid_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 empty),{SRC_PDF},strong,tick2485; PDF p6 native; YE2024 destin empty; 791 empty; 14 322319 DROP",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":573569,\"\"2025_73\"\":1067194,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70\"\":573569,\"\"2025_bruto\"\":1226150,"
"\"\"2025_pnl\"\":-27867,\"\"2025_bedrijfswinst\"\":-34045,"
"\"\"2025_equity\"\":347538,\"\"2025_assets\"\":859037,\"\"2025_debt\"\":473906,"
"\"\"2025_fte\"\":26.9,\"\"2025_kapitaalsubsidies\"\":25219,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":651158,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":1219940,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,\"\"2025_66B\"\":1103,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":322319,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":37593,\"\"2025_630\"\":35323,\"\"2025_capex\"\":36970,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":9501,\"\"2025_60_61\"\":441804,"
"\"\"2024_omzet\"\":566366,\"\"2024_73\"\":1059110,"
"\"\"2024_opbr70\"\":566366,\"\"2024_bruto\"\":1197756,\"\"2024_pnl\"\":23425,\"\"2024_bedrijfswinst\"\":15277,"
"\"\"2024_equity\"\":375052,\"\"2024_assets\"\":1091674,"
"\"\"2024_debt\"\":679029,\"\"2024_cash\"\":872025,\"\"2024_fte\"\":27.1,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":24866,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Grijkoort Begeleid Werk YE2025 (omzet JUMP 574k / 73 JUMP 1.07m / pnl FLIP LOSS 28k / cash DROP 651k / Strong PDF),{EID},VAPH + leftover city_ronse VAPH,Grijkoort Begeleid Werk VZW (KBO 0443.074.521; Actief; 6 VE; zetel Ronse),2026-06-25,2025,2025,573569,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00311391.pdf,Public VAPH dual of mined city_ronse,Publish VAPH / VDAB / begeleid-werken matrix behind omzet 574k and 73 1.07m and why pnl FLIP LOSS -27867 while cash DROP 651158,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Ronse>Grijkoort-Begeleid-Werk>JR2025_statutory_L5,tick2485; Strong official native PDF; leftover mined city_ronse VAPH; 6 VE; prior-year identical; NOT Grijkoort-Werkplaats remine; NOT GR.O.O.D. unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Nektari remine; NOT Reva Ter Linde remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Grijkoort Begeleid Werk omzet JUMP 574k / 73 JUMP 1.07m / pnl FLIP LOSS 28k / cash DROP 651k (YE2025 leftover city_ronse VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Ronse>Grijkoort-Begeleid-Werk>JR2025",
"573569",
"573569",
"PDF envelope 573569 = omzet 70 VZW because omzet material not commercial-only; 70 573569; 73 1067194; 76A empty; bruto 1226150; bedrijfswinst FLIP LOSS -34045; pnl FLIP LOSS -27867; equity DROP 347538; assets DROP 859037; debt DROP 473906; FTE 26.9; kapitaalsubsidies 25219; destin691 empty; cash DROP 651158; capex 36970; leftover city_ronse VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_ronse VAPH",
"VAPH leftover city_ronse",
"574k envelope; 73 1.07m; pnl FLIP LOSS 28k; cash DROP 651k; leftover city_ronse VAPH",
"5.50",
"5.22",
"5.26",
"5.33",
"FOI VAPH / VDAB begeleid-werken matrix behind envelope omzet 574k + 73 JUMP 1.07m and why pnl FLIP LOSS -27867 while cash DROP 651158 and FTE DROP 26.9",
"active",
"",
"tick2485 leftover mined city_ronse VAPH after Grijkoort-Werkplaats lock; 6 VE; prior-year identical; NOT Grijkoort-Werkplaats remine tick2484; NOT GR.O.O.D. 0885.458.164 unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Nektari remine tick2483; NOT Reva Ter Linde remine tick2482; NOT De Hagewinde remine tick2481; NOT BWP remine tick2480; NOT Kaliber remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Ronse>Grijkoort-Begeleid-Werk>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / VDAB / begeleid-werken split behind envelope omzet 70 573569 (material not commercial-only vs 73 1067194) and why pnl FLIP LOSS -27867 while cash DROP 651158 and FTE DROP 26.9",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_ronse; VKT envelope omzet 574k because not commercial-only; public VAPH 6 VE Peperstraat 8; pnl FLIP LOSS 28k / cash DROP 651k / 73 JUMP 1.07m / omzet JUMP 1.27pct",
"priority": "8",
"recipient_body": "GRIJKOORT - BEGELEID WERK VZW / Raad van Bestuur",
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
"notes": "tick2485; ready NOT sent; Strong official native NBB PDF; leftover mined city_ronse VAPH after Grijkoort-Werkplaats lock; 6 VE; prior-year identical; off Grijkoort-Werkplaats remine; off GR.O.O.D. unused sister; off ARCOR remine; off De Linde Ronse YE2024; off Nektari remine; off Reva Ter Linde remine; off De Hagewinde remine; off BWP remine; off Kaliber remine; off CVDO remine; off Dennenhof remine; off Ten Anker remine; off Bremdael remine; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
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
if rq_raw.count(b"rq_2485,")!=1: raise SystemExit(f"bad 2485 count {rq_raw.count(b'rq_2485,')}")
if b"rq_2486," in rq_raw: raise SystemExit("2486 exists")
idx=rq_raw.rfind(b"rq_2485,")
if idx<0: raise SystemExit("rq_2485 not found")
new_2485=(
"rq_2485,leftover dual Grijkoort Begeleid Werk YE2025,hole_fill,8,done,L5,vzw_grijkoort_begeleid_werk_ronse,"
"Took unused leftover public VAPH Grijkoort Begeleid Werk 0443.074.521 leftover mined city_ronse. Official NBB VKT-VZW YE2025 2026-00311391 native statutory 20p. Envelope omzet 70 JUMP 573569 (material not commercial-only vs 73 JUMP 1067194); pnl FLIP LOSS -27867; cash DROP 651158; bruto JUMP 1226150; FTE 26.9. NOT Grijkoort-Werkplaats remine. NOT GR.O.O.D. unused sister. NOT ARCOR remine. NOT De Linde Ronse YE2024. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2485 leftover mined city_ronse VAPH; Strong native PDF; 6 VE; prior-year identical; next every-10 is 2490\n"
)

new_2486=(
"rq_2486,leftover dual hunt after Grijkoort Begeleid Werk,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: vilvoorde / mol / denderleeuw (WZC/VAPH leftover; skip Armonea Ter Bake/Rodenbach) / zoersel / schilde (Sint Lodewijk taken) / kalmthout (Bambi CIK taken; leftover WZC/VAPH; skip Vulpia Beukenhof / De Medemens remine) / dendermonde (Zonneschijn CIK taken; leftover VAPH/CAR; skip OCMW Aymonshof/De Cocon; skip Zorg-Saam/Broeders leftover-via-VE; skip Kasteelhof Korian; PARCOER GGZ not leftover dual type) / geel (Augustientjes CIK taken; leftover VAPH/CAR; WZC Zusterhof+Perrekes remine; skip Armonea Laarsveld / Vulpia Het Veld / OCMW Wedbos / MPI Oosterlo remine; AZ Sint-Dimpna 0844.179.716 no NBB deposits) / herentals (Bremdael WZC taken — leftover VAPH/CAR only; AZ already mined; OpWeg YE2024; Kaliber maatwerk remine) / knokke_heist (De Lindeboom + Duinhuisjes + CVDO taken) / waregem (Kindercentrum + t Zonnetje + Ten Anker taken) / schoten (De Vier Notelaars + Dennenhof taken) / dilbeek (Savio CIK + BWP VAPH taken; leftover WZC; Aurora maatwerk YE2024 skip unless YE2025; De Verlosser remine; Het Witte Huis 0443.655.432 YE2024; skip Quietas/Koning Albert Armonea / Maria Assumpta Vulpia / Dilhome Orelia / Breugheldal OCMW) / lokeren (CAR Waas + Ter Engelen + Sakura + Hagewinde VAPH taken — different leftover type only) / eeklo (CAR Ascendere + KISME + Don Bosco taken; leftover WZC; skip Zorg-Saam Gent seat; Philippus Neri YE2024 Sint-Niklaas seat; Kinderlach YE2024) / ronse (Grijkoort-Werkplaats maatwerk taken; Grijkoort Begeleid Werk VAPH taken; De Linde WZC YE2024 0778.279.401; GR.O.O.D. 0885.458.164 unused sister — take ONLY if unused + official YE2025 native PDF) / halle (CAR taken; Sint-Augustinus WZC remine; skip De Maretak Korian; Zonnig Huis city) / bornem (Reva Ter Linde CAR taken; OLV hospital remine; skip De Vlietoever BV / Huize Eyckerheyde remine; leftover WZC/VAPH only) / puurs_sint_amands (Nektari maatwerk taken; Reva Ter Linde current zetel — leftover CAR taken via Bornem write; leftover WZC/VAPH only; skip Anemoon Korian / Gravenkasteel Armonea / Zorgbedrijf Klein-Brabant remine). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende / Aurora Dilbeek 0407.624.484 / Het Witte Huis Dilbeek / OpWeg Herentals still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. city_kapellen slug missing. WZC Joostens Zoersel = Zorgbedrijf Antwerpen not local VZW. Ter Bake / Rodenbach Denderleeuw Armonea commercial. De Vlietoever Bornem BV commercial. Anemoon Puurs Korian commercial. Gravenkasteel Puurs Armonea commercial. FIRST GR.O.O.D. 0885.458.164 unused sister — take ONLY if unused + leftover mined city + official YE2025 native PDF. NOT Grijkoort Begeleid Werk remine. NOT Grijkoort-Werkplaats remine. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT Ter Engelen remine. NOT CAR Waas remine. NOT Sakura remine. NOT Kaliber remine. NOT Begeleid Wonen Pajottenland remine. NOT INFANO remine. NOT MWP Lennik remine. NOT Savio remine. NOT EVA Dilbeek remine. NOT CVDO remine. NOT CAR De Klinker Ieper remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT WZC Ten Anker Nieuwpoort remine. NOT Bremdael remine. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO and ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Huis Perrekes remine. NOT Sint-Augustinus Halle remine. NOT OLV Bornem remine. NOT AZ Alma remine. NOT AZ Sint-Blasius remine. NOT Philippus Neri YE2024 leftover-via-VE. NOT De Linde Ronse YE2024. NOT De Maretak Korian commercial. NOT Het Veld Vulpia commercial. NOT Laarsveld Armonea commercial. NOT Wedbos OCMW. NOT CAR Glorieux remine. NOT CAR Wegwijs Kloosterstraat 6 Drongen. NOT CAR Halle Asse remine. NOT Ascendere remine. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private. NOT Armonea Vogelzang/Hemelrijck/Ter Bake/Gravenkasteel commercial. NOT Orelia Koningshof commercial. NOT Korian Anemoon commercial. NOT Stijn leftover-via-VE Hasselt remine. NOT Felies leftover-via-VE Brussels. NOT Klein Hemelrijk absorbed. NOT Sint Lodewijk remine. NOT De Lindeboom remine. NOT De Vier Notelaars remine. NOT Lidwina remine. NOT Homevil remine. NOT Schoonderhage remine. NOT AZ Herentals remine. NOT Evara remine. NOT Zorg-Saam remine. NOT MPI Oosterlo remine. NOT Groep Talent remine. NOT Werkplus remine. NOT ARCOR remine. NOT Aurora Dilbeek YE2024. NOT De Verlosser Dilbeek remine. NOT Kiemkracht remine. NOT PARCOER GGZ. NOT AZ Sint-Dimpna no deposits.,"
f",{STAMP},{STAMP},spawned after tick2485 leftover city_ronse VAPH; Grijkoort Begeleid Werk taken; Grijkoort-Werkplaats taken leftover mined city_ronse maatwerk; Nektari taken leftover mined city_puurs_sint_amands maatwerk; Reva Ter Linde taken leftover mined city_bornem CAR; De Hagewinde taken leftover mined city_lokeren VAPH; Begeleid Wonen Pajottenland taken leftover mined city_dilbeek VAPH; CVDO taken leftover mined city_knokke_heist CAR; Dennenhof taken leftover mined city_schoten VAPH; Ten Anker taken leftover mined city_waregem VAPH; Bremdael taken leftover mined city_herentals WZC; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2485.count("\n")!=1 or new_2486.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2485",new_2485),("2486",new_2486)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2485.encode("utf-8"))
    f.write(new_2486.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2485", chk.count(b"rq_2485,"), "n2486", chk.count(b"rq_2486,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2485,2485,no,tick2485 leftover dual Grijkoort Begeleid Werk 0443.074.521 Strong native PDF (omzet70 573569 material not commercial-only vs 73 JUMP 1067194; 76A empty; envelope omzet 70 JUMP 573569; bruto JUMP 1226150; pnl FLIP LOSS -27867; 9901 FLIP LOSS -34045; equity DROP 347538; assets DROP 859037; debt DROP 473906; FTE DROP 26.9; kapitaalsubsidies JUMP 25219; destin691 empty; 791 empty; cash DROP 651158; geldbeleggingen empty; capex 36970; 6 VE leftover city_ronse VAPH); leftover mined city_ronse VAPH; prior-year identical; NOT Grijkoort-Werkplaats remine; NOT GR.O.O.D. unused sister; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Kaliber remine; NOT INFANO remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT Huis Perrekes remine; NOT Sint-Augustinus Halle remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri YE2024 leftover-via-VE; NOT De Maretak Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW; NOT CAR Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT MPI Oosterlo remine; NOT Groep Talent remine; NOT Anemoon Korian commercial; NOT Gravenkasteel Armonea commercial; NOT De Verlosser Dilbeek remine; NOT Het Witte Huis YE2024; NOT AZ Sint-Dimpna no deposits; NOT PARCOER GGZ; next every-10 is 2490; next rq_2486 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2485 - rq_2485 Grijkoort Begeleid Werk Ronse (omzet JUMP 574k / 73 JUMP 1.07m / pnl FLIP LOSS 28k / cash DROP 651k / Strong PDF)

- Unit: **rq_2485** leftover dual after **Grijkoort@2484**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of less-picked mined Flanders cities (CIK lists herentals/schoten/vilvoorde/mol exhausted at 2476; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde). Confirmed `city_ronse` / `city_bornem` / `city_puurs_sint_amands` / `city_denderleeuw` / `city_dendermonde` / `city_geel` / `city_herentals` / `city_kalmthout` / `city_eeklo` / `city_halle` / `city_dilbeek` exist (`city_kapellen` missing). FIRST locked: Grijkoort Begeleid Werk **0443.074.521** leftover city_ronse VAPH unused YE2025 **2026-00311391** VKT 574kB — unused + leftover mined parent + official CDN GET **200** 574322 native extractable euros — **LOCKED**. Skips this hunt: leftover WZC/VAPH of city_puurs_sint_amands (Anemoon Korian / Gravenkasteel Armonea commercial; Zorgbedrijf Klein-Brabant remine; Nektari maatwerk taken). Leftover WZC/VAPH of city_bornem (OLV remine; De Vlietoever BV; Huize Eyckerheyde remine; Ter Linde CAR taken). Dilbeek leftover WZC: De Verlosser remine; Het Witte Huis **0443.655.432** YE2024; Quietas/Koning Albert Armonea; Maria Assumpta Vulpia; Dilhome Orelia; Breugheldal OCMW; Aurora YE2024. OpWeg Herentals still YE2024. De Linde Ronse still YE2024. Kinderlach Eeklo still YE2024. AZ Sint-Dimpna Geel **0844.179.716** no NBB deposits (AVI). Kasteelhof Dendermonde Korian CommV. De Klokke leftover-via-VE Sint-Niklaas. Vrienden van Thomas leftover-via-VE Antwerpen. PARCOER **0683.817.138** YE2025 GGZ not leftover dual type. Kiemkracht remine. leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde. Identity trap: 0443.074.521 ≠ Grijkoort-Werkplaats **0463.374.146** remine tick2484 ≠ GR.O.O.D. **0885.458.164** unused sister ≠ ARCOR **0410.962.274** remine ≠ De Linde Ronse **0778.279.401** YE2024 ≠ Nektari **0407.231.239** ≠ Reva Ter Linde **0431.331.383** ≠ De Vlietoever BV **0898.596.122** ≠ OLV Bornem **0436.595.020** ≠ Aurora Dilbeek **0407.624.484** ≠ De Hagewinde **0861.262.010** ≠ BWP **0423.884.258**. 6 VE leftover of mined city_ronse (zetel Peperstraat 8; KBO VE 2.152.262.823 Peperstraat 8 Ronse). Confirmed leftover public VAPH not convent / not private / not CIK / not WZC / not commercial NV / not maatwerk (sister Werkplaats taken). VKT-VZW native statutory (6.2 6.3 6.5 7 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00311391** (574322 B / 20p; AV **25.06.2026**; header **16.07.2026**; CDN GET **200** 574322 official NBB-generated OpenPDF 1.3.26 CreationDate 20.07.2026 Last-Modified 03.08.2026 MD5 4ab1aa831bee8095d1612680a0842944; statutory pages native; prior-year identical not restated; commissaris A&C Bedrijfsrevisor / De Clercq Bert) — omzet 70 **EUR573569** JUMP +1.27% (material not commercial-only; was 566366); 73 **EUR1067194** JUMP +0.76% (was 1059110); 76A **empty**; envelope omzet 70 **EUR573569** JUMP +1.27% (VZW envelope because omzet material not commercial-only); bruto 9900 **EUR1226150** JUMP +2.37% (was 1197756); 62 **EUR1219940** JUMP +6.53%; 630 **EUR35323** JUMP +9.41%; 66A **empty**; 66B **EUR1103**; 640/8 **EUR4932** DROP; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR-34045** FLIP LOSS (was +15277); pnl 9904 **EUR-27867** FLIP LOSS (was +23425); equity **EUR347538** DROP −7.34%; assets **EUR859037** DROP −21.31%; debt **EUR473906** DROP −30.21%; FTE **26.9** DROP −0.74% (was 27.1; 100 26.9; 9087 26.9; 105 26.6); kapitaalsubsidies **EUR25219** JUMP +1.42%; destin 691 **empty**; 791 **empty**; cash **EUR651158** DROP −25.33%; geldbeleggingen **empty**; gebouwen **empty**; MVA 22/27 **EUR107500** JUMP; aanbouw **empty**; capex **EUR36970**. Strong KBO + Strong PDF (native statutory; not SBM table; not Companyweb euros). Site: 6 VE leftover mined city_ronse VAPH. NOT Grijkoort-Werkplaats remine. NOT GR.O.O.D. unused sister. NOT ARCOR remine. NOT De Linde Ronse YE2024. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Kaliber remine. NOT CVDO remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT Bremdael remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.33); entities (+1 vzw_grijkoort_begeleid_werk_ronse); foi + draft `gap_grijkoort_begeleid_ronse_vaph_matrix_omzet_574k_73_jump_1_07m_pnl_flip_loss_28k_cash_drop_651k_l5`; rq_2485=done + rq_2486 open; loop_state ticks=2485; raw tick2485/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2486 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Grijkoort Begeleid Werk remine / NOT Grijkoort-Werkplaats remine / NOT Nektari remine / NOT GR.O.O.D. unless unused + official YE2025 native PDF / NOT ARCOR remine / NOT De Linde Ronse YE2024 / NOT Reva Ter Linde remine / NOT De Vlietoever BV commercial / NOT OLV Bornem remine / NOT Aurora Dilbeek YE2024 / NOT De Hagewinde remine / NOT BWP remine / NOT Kaliber remine / NOT CVDO remine / NOT Dennenhof remine / NOT Ten Anker remine / NOT Bremdael remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine / NOT Huis Perrekes remine / NOT Sint-Augustinus Halle remine / NOT MPI Oosterlo remine).

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2486_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_huize_de_veuster_jr2025_nbb_pdf_2486"
SRC_KBO="src_huize_de_veuster_kbo_2486"
SRC_SBM="src_huize_de_veuster_sbm_2486"
SRC_SITE="src_huize_de_veuster_site_2486"
EID="vzw_huize_de_veuster_tremelo"
GAP="gap_huize_de_veuster_tremelo_vaph_matrix_70_76A_4_16m_omzet_commercial_73_jump_3_33m_pnl_flip_475k_l5"
COMM="comm_huize_de_veuster_jr2025_statutory_70_76A_4_16m_73_jump_333m_pnl_flip_475k"
LB="lb_huize_de_veuster_70_76A_4_16m_73_jump_333m_pnl_flip_475k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Grijkoort Begeleid Werk 0443.074.521 remine tick2485; NOT Grijkoort-Werkplaats 0463.374.146 remine tick2484; NOT GR.O.O.D. 0885.458.164 no JR skip; NOT Nektari 0407.231.239 remine tick2483; NOT Reva Ter Linde 0431.331.383 remine tick2482; NOT De Hagewinde 0861.262.010 remine; NOT BWP 0423.884.258 remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Blijdorp 0409.371.771 remine; NOT Blijdorp II 0418.336.650 no JR; NOT Den Brand 0422.073.526 remine leftover-via-VE Mol; NOT De Schakel 0419.461.652 remine Balen; NOT Huize Zonnelied remine; NOT Huize Eyckerheyde remine; NOT Ter Engelen remine; NOT ARCOR remine; NOT De Linde Ronse YE2024; NOT Aurora Dilbeek YE2024; NOT OpWeg Herentals YE2024; NOT Kinderlach YE2024; NOT Molleke YE2024; NOT t Sas YE2024; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Orelia commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent; NOT MPI Oosterlo remine; NOT PARCOER GGZ; NOT AZ Sint-Dimpna no deposits")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Huize De Veuster Tremelo deposit 2026-00223671,http://cdn.staatsbladmonitor.be/2026pdf/2026-00223671.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2486; official native statutory PDF 84536 bytes 31p VOL-VZW 23.0.10 m05-f; header 30.06.2026; AV 19.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-30 16:17:47 UTC OpenPDF 1.3.26; CDN Last-Modified 12.07.2026; statutory pages native; CDN 2026-00223671 GET 200 84536 MD5 7abcf954d361e97471b65295ee0caf6c; VOL-VZW 6.1 6.2.1-4 6.4.1-2 6.5.1-3 6.6 6.10 6.14 6.15 6.16 7 8 niet dienstig; prior-year identical not restated; commissaris not listed on VOL-VZW 2; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Huize De Veuster 0476.354.132,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0476354132,KBO Public Search FOD Economie,{DAY},official_register,tick2486; Actief; 1 VE 2.155.022.868 zetel Pater Damiaanstraat 33 bus B 3120 Tremelo since 16.10.2008; VZW since 31.10.2001; RSZ-werkgever RSZ2025 87.202 huisvesting volwassenen mentale handicap; FOI ellen.heyligen@huizedeveuster.be; leftover mined city_tremelo VAPH; VE since 11.07.2006; NOT Grijkoort Begeleid Werk remine; NOT GR.O.O.D. no JR; NOT Blijdorp remine; NOT Den Brand remine",
f"{SRC_SBM},NBB Consult / SBM fiche Huize De Veuster 0476354132 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0476354132,NBB Consult / SBM,{DAY},official_register,tick2486; deposit-id 2026-00223671 YE 01.01.2025-31.12.2025 filing VOL-VZW Volledig model vereniging Initial UUID 4365efcc-749c-11f1-9ea1-d5b7adab159f; Companyweb last-balansjaar 2025 deposit-id discovery via NBB OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table not Busibee not Companyweb",
f"{SRC_SITE},Huize De Veuster FOI contact leftover city_tremelo VAPH,https://huizedeveuster.be/,Huize De Veuster VZW leftover city_tremelo VAPH 1 VE,{DAY},foi_contact,tick2486; FOI ellen.heyligen@huizedeveuster.be dagelijks bestuur; T 016 53 65 95; zetel Pater Damiaanstraat 33B 3120 Tremelo; Voorzitter De Vadder Koen; leftover mined city_tremelo VAPH after Grijkoort Begeleid Werk lock; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Blijdorp remine; NOT Den Brand remine; NOT De Schakel remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},HUIZE DE VEUSTER VZW,ASBL Huize De Veuster,Huize De Veuster VZW (leftover city_tremelo VAPH),parastatal,city_tremelo,nl,https://huizedeveuster.be/,ellen.heyligen@huizedeveuster.be,Pater Damiaanstraat 33B 3120 Tremelo,tick2486 YE2025 Strong official native NBB PDF deposit 2026-00223671 + Strong KBO 0476.354.132 Actief 1 VE 2.155.022.868; omzet70 516380 commercial-only vs large 73; 73 JUMP 3327899; 76A JUMP 244497; envelope 70/76A JUMP 4162334; pnl FLIP 474611; 9901 FLIP 519924; equity JUMP 2291678; assets JUMP 4420072; debt DROP 1888395; FTE JUMP 38.5; kapitaalsubsidies DROP 560398; destin691 empty; 791 empty; cash JUMP 1969352; geldbeleggingen empty; capex 482154; leftover city_tremelo VAPH 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_huize_de_veuster_omzet_jr2025_statutory,{EID},2025,516380,516380,516380,NBB VOL-VZW code 70 omzet YE2025 JUMP +4.30% (commercial-only vs large 73),{SRC_PDF},strong,tick2486; PDF p5 native; YE2024 495107; 73 JUMP 3327899; 76A JUMP 244497",
f"bud_huize_de_veuster_73_jr2025_statutory,{EID},2025,3327899,3327899,3327899,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +7.17%,{SRC_PDF},strong,tick2486; PDF p5 native; YE2024 3105238; 730-733 empty VOL 6.9; FOI VAPH/PVB matrix behind 73",
f"bud_huize_de_veuster_opbr_jr2025_statutory,{EID},2025,4162334,4162334,4162334,NBB VOL-VZW envelope 70/76A YE2025 JUMP +11.37% (VZW envelope because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2486; PDF p5 native; YE2024 3737481; 70 516380; 73 3327899; 76A 244497",
f"bud_huize_de_veuster_76A_jr2025_statutory,{EID},2025,244497,244497,244497,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +228.63% (764/8),{SRC_PDF},strong,tick2486; PDF p5/p20 native; YE2024 74400; 66A DROP 25551",
f"bud_huize_de_veuster_pnl_jr2025_statutory,{EID},2025,474611,474611,474611,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 FLIP PROFIT (was -412943),{SRC_PDF},strong,tick2486; PDF p6 native; YE2024 -412943; bedrijfswinst 9901 519924 FLIP; destin691 empty",
f"bud_huize_de_veuster_bedrijfswinst_jr2025_statutory,{EID},2025,519924,519924,519924,NBB VOL-VZW code 9901 bedrijfswinst YE2025 FLIP PROFIT (was -376750),{SRC_PDF},strong,tick2486; PDF p5 native; YE2024 -376750; 62 3063239 JUMP; 630 164039 JUMP; 66A 25551 DROP; 66B empty; 640/8 42713 JUMP; 635/9 empty; 631/4 empty",
f"bud_huize_de_veuster_equity_jr2025_statutory,{EID},2025,2291678,2291678,2291678,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +20.82%,{SRC_PDF},strong,tick2486; PDF p4 native; YE2024 1896733; kapitaalsubsidies 560398 DROP; overgedragen 14 248239 JUMP; fondsen 10 29211 FLAT; bestemde fondsen 13 1453830 FLAT",
f"bud_huize_de_veuster_assets_jr2025_statutory,{EID},2025,4420072,4420072,4420072,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +7.76%,{SRC_PDF},strong,tick2486; PDF p3 native; YE2024 4101891; MVA 22/27 2177006 JUMP; cash 1969352 JUMP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 5082; LT recv 29 83671 DROP",
f"bud_huize_de_veuster_debt_jr2025_statutory,{EID},2025,1888395,1888395,1888395,NBB VOL-VZW code 17/49 schulden YE2025 DROP -3.91%,{SRC_PDF},strong,tick2486; PDF p4 native; YE2024 1965159; 17 1168840 JUMP; 42/48 719554 DROP",
f"bud_huize_de_veuster_cash_jr2025_statutory,{EID},2025,1969352,1969352,1969352,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +0.56%,{SRC_PDF},strong,tick2486; PDF p3 native; YE2024 1958454; geldbeleggingen 50/53 empty; capex 482154",
f"bud_huize_de_veuster_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 FLAT 1453830),{SRC_PDF},strong,tick2486; PDF p7 native; YE2024 destin empty; 791 empty; 14 JUMP 248239 = 14P -226372 + pnl 474611",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":516380,\"\"2025_73\"\":3327899,\"\"2025_76A\"\":244497,"
"\"\"2025_opbr7076A\"\":4162334,"
"\"\"2025_pnl\"\":474611,\"\"2025_bedrijfswinst\"\":519924,"
"\"\"2025_equity\"\":2291678,\"\"2025_assets\"\":4420072,\"\"2025_debt\"\":1888395,"
"\"\"2025_fte\"\":38.5,\"\"2025_kapitaalsubsidies\"\":560398,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1969352,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":3063239,\"\"2025_gebouwen22\"\":1400040,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":25551,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":29211,\"\"2025_overgedragen14\"\":248239,"
"\"\"2025_bestemdefondsen13\"\":1453830,"
"\"\"2025_voorzieningen16\"\":240000,\"\"2025_630\"\":164039,\"\"2025_capex\"\":482154,"
"\"\"2025_ltrecv29\"\":83671,\"\"2025_75\"\":613,\"\"2025_74\"\":73559,"
"\"\"2024_omzet\"\":495107,\"\"2024_73\"\":3105238,"
"\"\"2024_opbr7076A\"\":3737481,\"\"2024_pnl\"\":-412943,\"\"2024_bedrijfswinst\"\":-376750,"
"\"\"2024_equity\"\":1896733,\"\"2024_assets\"\":4101891,"
"\"\"2024_debt\"\":1965159,\"\"2024_cash\"\":1958454,\"\"2024_fte\"\":37.3,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":640064,\"\"2024_76A\"\":74400,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Huize De Veuster YE2025 (70/76A JUMP 4.16m / omzet commercial vs 73 JUMP 3.33m / pnl FLIP 475k / Strong PDF),{EID},VAPH + leftover city_tremelo VAPH,Huize De Veuster VZW (KBO 0476.354.132; Actief; 1 VE; zetel Tremelo),2026-06-19,2025,2025,4162334,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00223671.pdf,Public VAPH dual of mined city_tremelo,Publish VAPH / PVB / woon-dag matrix behind 70/76A 4.16m and 73 3.33m and why pnl FLIP PROFIT 474611 after YE2024 LOSS,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Tremelo>Huize-De-Veuster>JR2025_statutory_L5,tick2486; Strong official native PDF; leftover mined city_tremelo VAPH; 1 VE; prior-year identical; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Blijdorp remine; NOT Den Brand remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Huize De Veuster 70/76A JUMP 4.16m / 73 JUMP 3.33m / pnl FLIP 475k (YE2025 leftover city_tremelo VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Tremelo>Huize-De-Veuster>JR2025",
"4162334",
"4162334",
"PDF envelope 4162334 = 70/76A VZW because omzet commercial-only vs large 73; 70 516380; 73 3327899; 76A 244497; bedrijfswinst FLIP 519924; pnl FLIP 474611; equity JUMP 2291678; assets JUMP 4420072; debt DROP 1888395; FTE 38.5; kapitaalsubsidies 560398; destin691 empty; cash JUMP 1969352; capex 482154; leftover city_tremelo VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_tremelo VAPH",
"VAPH leftover city_tremelo",
"4.16m envelope; 73 3.33m; pnl FLIP 475k; leftover city_tremelo VAPH",
"5.50",
"5.22",
"5.26",
"5.48",
"FOI VAPH / PVB / woon-dag matrix behind envelope 70/76A 4.16m + 73 JUMP 3.33m and why pnl FLIP PROFIT 474611 after YE2024 LOSS 412943 while 66A DROP 25551 and capex 482154 and FTE JUMP 38.5",
"active",
"",
"tick2486 leftover mined city_tremelo VAPH after Grijkoort Begeleid Werk lock; 1 VE; prior-year identical; NOT Grijkoort Begeleid Werk remine tick2485; NOT Grijkoort-Werkplaats remine tick2484; NOT GR.O.O.D. 0885.458.164 no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Blijdorp remine; NOT Den Brand remine; NOT De Schakel remine; NOT Huize Zonnelied remine; NOT Huize Eyckerheyde remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT Kinderlach YE2024; NOT Molleke YE2024; NOT t Sas YE2024",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Tremelo>Huize-De-Veuster>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / PVB / woon-dag split behind envelope 70/76A 4162334 (omzet 516380 commercial-only vs 73 3327899) and why pnl FLIP PROFIT 474611 after YE2024 LOSS 412943 while 66A DROP 25551 and capex 482154 and FTE JUMP 38.5",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_tremelo; VOL envelope 4.16m because omzet commercial-only vs large 73; public VAPH 1 VE Pater Damiaanstraat 33B; pnl FLIP 475k / 73 JUMP 3.33m / 76A JUMP 244k",
"priority": "8",
"recipient_body": "HUIZE DE VEUSTER VZW / Raad van Bestuur",
"recipient_email": "ellen.heyligen@huizedeveuster.be",
"recipient_postal": "Pater Damiaanstraat 33B 3120 Tremelo",
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
"notes": "tick2486; ready NOT sent; Strong official native NBB PDF; leftover mined city_tremelo VAPH after Grijkoort Begeleid Werk lock; 1 VE; prior-year identical; off Grijkoort remine; off GR.O.O.D. no JR; off Blijdorp remine; off Den Brand remine; off De Schakel remine; off Huize Zonnelied remine; off Huize Eyckerheyde remine; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
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
if rq_raw.count(b"rq_2486,")!=1: raise SystemExit(f"bad 2486 count {rq_raw.count(b'rq_2486,')}")
if b"rq_2487," in rq_raw: raise SystemExit("2487 exists")
idx=rq_raw.rfind(b"rq_2486,")
if idx<0: raise SystemExit("rq_2486 not found")
new_2486=(
"rq_2486,leftover dual Huize De Veuster YE2025,hole_fill,8,done,L5,vzw_huize_de_veuster_tremelo,"
"Took unused leftover public VAPH Huize De Veuster 0476.354.132 leftover mined city_tremelo. Official NBB VOL-VZW YE2025 2026-00223671 native statutory 31p 84kB. Envelope 70/76A JUMP 4162334 (omzet 516380 commercial-only vs 73 JUMP 3327899); pnl FLIP PROFIT 474611; 76A JUMP 244497; FTE 38.5; capex 482154. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Blijdorp remine. NOT Den Brand remine. NOT De Schakel remine. NOT Huize Zonnelied remine. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2486 leftover mined city_tremelo VAPH; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2490\n"
)
new_2487=(
"rq_2487,leftover dual hunt after Huize De Veuster,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken; leftover VAPH/CAR; skip OCMW Aymonshof/De Cocon; skip Zorg-Saam/Broeders leftover-via-VE; skip Kasteelhof Korian; skip Blijdorp remine Buggenhout seat; PARCOER GGZ not leftover dual type) / geel (Augustientjes CIK taken; leftover VAPH/CAR; WZC Zusterhof+Perrekes remine; skip Armonea Laarsveld / Vulpia Het Veld / OCMW Wedbos / MPI Oosterlo remine; AZ Sint-Dimpna no deposits) / herentals (Bremdael WZC taken — leftover VAPH/CAR only; AZ remine; OpWeg YE2024; Kaliber maatwerk remine) / eeklo (CAR Ascendere + KISME + Don Bosco taken; leftover WZC; skip Zorg-Saam Gent seat; Kinderlach YE2024) / halle (CAR taken; Sint-Augustinus remine; leftover WZC/VAPH; leftover CIK De Kapoentjes 0821.882.483 unused — take ONLY if unused + official YE2025 native PDF; skip De Maretak Korian) / kalmthout (Bambi CIK taken; leftover WZC/VAPH; skip Vulpia Beukenhof / De Medemens remine) / bornem (CAR taken; leftover WZC/VAPH; skip OLV remine / De Vlietoever BV / Huize Eyckerheyde remine) / puurs (maatwerk taken; leftover WZC/VAPH; skip Anemoon Korian / Gravenkasteel Armonea / Klein-Brabant remine) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. 0885.458.164 no JR skip) / vilvoorde / mol / zoersel / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken) / lokeren (VAPH taken) / dilbeek (CIK+VAPH taken; leftover WZC remine/YE2024/commercial) / tremelo (VAPH Huize De Veuster taken — leftover WZC/CAR/maatwerk/CIK only). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. GR.O.O.D. 0885.458.164 no NBB deposits — skip. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Blijdorp remine. NOT Den Brand remine. NOT De Schakel remine. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2486 leftover city_tremelo VAPH; Huize De Veuster taken leftover mined city_tremelo VAPH; Grijkoort Begeleid Werk taken leftover mined city_ronse VAPH; Grijkoort-Werkplaats taken leftover mined city_ronse maatwerk; Nektari taken leftover mined city_puurs_sint_amands maatwerk; Reva Ter Linde taken leftover mined city_bornem CAR; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2486.count("\n")!=1 or new_2487.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2486",new_2486),("2487",new_2487)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2486.encode("utf-8"))
    f.write(new_2487.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2486", chk.count(b"rq_2486,"), "n2487", chk.count(b"rq_2487,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2486,2486,no,tick2486 leftover dual Huize De Veuster 0476.354.132 Strong native PDF (omzet70 516380 commercial-only vs 73 JUMP 3327899; 76A JUMP 244497; envelope 70/76A JUMP 4162334; pnl FLIP 474611; 9901 FLIP 519924; equity JUMP 2291678; assets JUMP 4420072; debt DROP 1888395; FTE JUMP 38.5; kapitaalsubsidies DROP 560398; destin691 empty; 791 empty; cash JUMP 1969352; geldbeleggingen empty; capex 482154; 1 VE leftover city_tremelo VAPH); leftover mined city_tremelo VAPH; prior-year identical; NOT Grijkoort Begeleid Werk remine; NOT Grijkoort-Werkplaats remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Blijdorp remine; NOT Den Brand remine; NOT De Schakel remine; NOT Huize Zonnelied remine; NOT Huize Eyckerheyde remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT OpWeg Herentals YE2024; NOT Kinderlach YE2024; NOT Molleke YE2024; NOT t Sas YE2024; next every-10 is 2490; next rq_2487 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2486 - rq_2486 Huize De Veuster Tremelo (70/76A JUMP 4.16m / omzet commercial vs 73 JUMP 3.33m / pnl FLIP 475k / Strong PDF)

- Unit: **rq_2486** leftover dual after **Grijkoort Begeleid Werk@2485**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of mined Flanders cities with official YE2025 native PDF. FIRST: GR.O.O.D. **0885.458.164** unused sister Peperstraat 8 Ronse — unused leftover mined city_ronse but 0 VE / NBB ids empty / Companyweb last-balansjaar N/A / geen jaarrekening — **SKIP**. Blijdorp **0409.371.771** already mined parent sec_flanders (zetel Buggenhout). Blijdorp II **0418.336.650** 0 VE no JR. Den Brand **0422.073.526** remine leftover-via-VE Mol. De Schakel remine Balen. WZC Sint-Elisabeth Eeklo = Zorg-Saam leftover-via-VE Gent. Ter Engelen Lokeren remine. Confirmed `city_tremelo` exists (mined). FIRST leftover unused + live official YE2025 native euros: took FREE leftover Flemish **HUIZE DE VEUSTER VZW** YE2025 (KBO **0476.354.132**; zetel Pater Damiaanstraat 33 bus B 3120 Tremelo; **Actief** **1 VE** **2.155.022.868** since 11.07.2006; RSZ2025 **87.202**; leftover of mined **city_tremelo**; ellen.heyligen@huizedeveuster.be; VAPH woon+dag volwassenen verstandelijke beperking / dubbeldiagnose / justitie). Identity trap: 0476.354.132 ≠ Huize Zonnelied ≠ Huize Eyckerheyde remine ≠ Den Brand remine ≠ De Schakel remine ≠ Blijdorp remine ≠ Grijkoort Begeleid Werk remine ≠ Grijkoort-Werkplaats remine ≠ GR.O.O.D. no JR ≠ Nektari remine ≠ Reva Ter Linde remine. 1 VE leftover of mined city_tremelo (zetel + VE Pater Damiaanstraat 33B). Confirmed leftover public VAPH not convent / not private / not CIK / not WZC / not commercial NV. VOL-VZW **native text** (not scan) — 84536 B / 31p all native euros (VOL-VZW 6.1 6.2.1-4 6.4.1-2 6.5.1-3 6.6 6.10 6.14 6.15 6.16 7 8 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00223671** (84536 B / 31p; AV **19.06.2026**; header **30.06.2026**; official NBB UUID 4365efcc-749c-11f1-9ea1-d5b7adab159f; CDN GET **200** 84536 official NBB-generated OpenPDF 1.3.26 CreationDate 30.06.2026 Last-Modified 12.07.2026 MD5 7abcf954d361e97471b65295ee0caf6c; all 31p native; prior-year identical not restated; commissaris not listed on VOL-VZW 2) — omzet 70 **EUR516380** JUMP +4.30% (commercial-only vs large 73; was 495107); 73 **EUR3327899** JUMP +7.17% (was 3105238; 730-733 empty); 76A **EUR244497** JUMP +228.63% (was 74400); envelope 70/76A **EUR4162334** JUMP +11.37% (VZW envelope because omzet commercial-only vs large 73; was 3737481); 74 **EUR73559** JUMP; 62 **EUR3063239** JUMP +11.45%; 630 **EUR164039** JUMP +14.24%; 66A **EUR25551** DROP −95.45% (was 561243); 66B **empty**; 640/8 **EUR42713** JUMP; 635/9 **empty** (was 240000); 631/4 **empty**; bedrijfswinst 9901 **EUR519924** FLIP PROFIT (was −376750); pnl 9904 **EUR474611** FLIP PROFIT (was −412943); equity **EUR2291678** JUMP +20.82%; assets **EUR4420072** JUMP +7.76%; debt **EUR1888395** DROP −3.91%; FTE **38.5** JUMP +3.22% (was 37.3; 1003 38.5; 9087 38.5; 9086 43; 105 37.2); kapitaalsubsidies **EUR560398** DROP −12.45%; destin 691 **empty**; 791 **empty**; cash **EUR1969352** JUMP +0.56%; geldbeleggingen **empty**; gebouwen **EUR1400040** JUMP; MVA 22/27 **EUR2177006** JUMP; aanbouw **empty**; capex **EUR482154**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_tremelo VAPH. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Blijdorp remine. NOT Den Brand remine. NOT De Schakel remine. NOT Huize Zonnelied remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.48); entities (+1 vzw_huize_de_veuster_tremelo); foi + draft `gap_huize_de_veuster_tremelo_vaph_matrix_70_76A_4_16m_omzet_commercial_73_jump_3_33m_pnl_flip_475k_l5`; rq_2486=done + rq_2487 open; loop_state ticks=2486; raw tick2486/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2487 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Huize De Veuster remine / NOT Grijkoort remine / NOT GR.O.O.D. no JR / NOT Blijdorp remine / NOT Den Brand remine / NOT De Schakel remine / NOT Nektari remine / NOT Reva Ter Linde remine / NOT De Hagewinde remine / NOT BWP remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_tremelo VAPH taken. Leftover CIK De Kapoentjes Halle **0821.882.483** unused — take ONLY if unused + official YE2025 native PDF.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

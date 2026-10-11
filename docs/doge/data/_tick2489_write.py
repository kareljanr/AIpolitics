from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2489_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_alderande_jr2025_nbb_pdf_2489"
SRC_KBO="src_alderande_kbo_2489"
SRC_SBM="src_alderande_sbm_2489"
SRC_SITE="src_alderande_site_2489"
EID="vzw_alderande_lokeren"
GAP="gap_alderande_lokeren_vaph_matrix_70_76A_3_74m_omzet_commercial_73_jump_3_18m_pnl_drop_70k_destin_303k_l5"
COMM="comm_alderande_jr2025_statutory_70_76A_3_74m_omzet_commercial_73_jump_3_18m_pnl_drop_70k_destin_303k"
LB="lb_alderande_70_76A_3_74m_omzet_commercial_73_jump_3_18m_pnl_drop_70k_destin_303k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Hagewinde 0861.262.010 remine tick2481; NOT De Kapoentjes 0821.882.483 remine tick2488; NOT De Zonnewende 0735.627.214 remine tick2487; NOT Huize De Veuster 0476.354.132 remine tick2486; NOT Grijkoort Begeleid Werk 0443.074.521 remine; NOT Grijkoort-Werkplaats 0463.374.146 remine; NOT GR.O.O.D. 0885.458.164 no JR; NOT Nektari 0407.231.239 remine; NOT Reva Ter Linde 0431.331.383 remine; NOT CAR Waas 0415.472.279 remine; NOT Ter Engelen 0430.882.809 remine; NOT Sakura 0684.613.726 remine; NOT De Cirkel 0470.413.079 remine; NOT De Poel 0415.693.993 leftover Dilbeek VAPH leftover-via-VE Halle unused YE2025 not taken; NOT ASTOR 0542.836.447 bankrupt; NOT Aralea 0420.809.061 YE2024; NOT CAR Kapelhof 0412.402.032 Drongen OFF; NOT WZC Sint-Vincentius Erpe-Mere 0422.620.585 YE2024; NOT Blijdorp remine; NOT Den Brand remine; NOT De Schakel remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent; NOT Kinderlach YE2024; NOT De Linde Ronse YE2024; NOT Molleke YE2024; NOT t Sas YE2024; NOT OpWeg YE2024")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Alderande Lokeren deposit 2026-00183687,http://cdn.staatsbladmonitor.be/2026pdf/2026-00183687.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2489; official native statutory PDF 498829 bytes 22p VKT-VZW 25.0.13 m04-f; header 22.06.2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-22 23:58:47 UTC OpenPDF 1.3.26; CDN Last-Modified 29.06.2026; statutory pages native; CDN 2026-00183687 GET 200 498829 MD5 ffa112b8eb0fcb77cbbcdf76e3ecf4b1; official NBB UUID 9b1bba84-5db7-11f1-b86a-ef50a6659ad6; VKT-VZW 6.6 8 niet dienstig; 6.1.1 6.1.2 6.1.3 6.2 6.3 6.4 6.5 6.7 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Alderande Lokeren 0431.893.389,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431893389,KBO Public Search FOD Economie,{DAY},official_register,tick2489; Actief; 4 VE leftover city_lokeren all 9160 Lokeren official KBO activity NACE 88106 (Kerkstraat 62; Kerkstraat 9; Molenbergplein 2; Zelestraat 166A); zetel Daknam-dorp 54 9160 Lokeren; VZW; begindatum 10.12.1985; FOI info@alderande.be; leftover mined city_lokeren VAPH after Hagewinde@2481; NOT De Hagewinde remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT De Cirkel remine; NOT CAR Kapelhof Drongen OFF",
f"{SRC_SBM},NBB Consult / SBM fiche Alderande 0431893389 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0431893389,NBB Consult / SBM,{DAY},official_register,tick2489; deposit-id 2026-00183687 YE 01.01.2025-31.12.2025 filing VKT-VZW Verkort model vereniging Initial UUID 9b1bba84-5db7-11f1-b86a-ef50a6659ad6; Companyweb last-balansjaar 2025 deposit-id discovery via NBB OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Alderande Lokeren FOI contact leftover city_lokeren VAPH,https://alderande.be/,Alderande VZW leftover city_lokeren VAPH 4 VE,{DAY},foi_contact,tick2489; FOI info@alderande.be; zetel Daknam-dorp 54 9160 Lokeren; VAPH woon+dag+individuele ondersteuning; PC 31901; leftover mined city_lokeren VAPH after Hagewinde lock; NOT De Hagewinde remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT De Cirkel remine; NOT De Poel leftover-via-VE; NOT CAR Kapelhof Drongen OFF; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Alderande,ASBL Alderande,Alderande VZW (leftover city_lokeren VAPH),parastatal,city_lokeren,nl,https://alderande.be/,info@alderande.be,Daknam-dorp 54 9160 Lokeren,tick2489 YE2025 Strong official native NBB PDF deposit 2026-00183687 + Strong KBO 0431.893.389 Actief 4 VE; omzet70 DROP 560746 commercial-only vs large 73; 73 JUMP 3183043; 76A empty; envelope 70/76A JUMP 3743789; pnl DROP 303348; 9901 DROP 288995; equity JUMP 4235304; assets JUMP 5885663; debt JUMP 1353192; FTE JUMP 36.6; kapitaalsubsidies DROP 265741; destin691 DROP 303348; 791 empty; cash JUMP 650911; geldbeleggingen JUMP 2564849; leftover city_lokeren VAPH 4 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_alderande_omzet_jr2025_statutory,{EID},2025,560746,560746,560746,NBB VKT-VZW code 70 omzet YE2025 DROP -2.05% (commercial-only vs large 73),{SRC_PDF},strong,tick2489; PDF p5 native; YE2024 572476; 73 JUMP 3183043; 76A empty",
f"bud_alderande_73_jr2025_statutory,{EID},2025,3183043,3183043,3183043,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +5.46%,{SRC_PDF},strong,tick2489; PDF p5 native; YE2024 3018391; FOI VAPH/PVB/woon-dag matrix behind 73",
f"bud_alderande_opbr_jr2025_statutory,{EID},2025,3743789,3743789,3743789,NBB VKT-VZW envelope 70/76A YE2025 JUMP +4.26% (VZW envelope because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2489; PDF p5 native; YE2024 3590867; 70 560746; 73 3183043; 76A empty",
f"bud_alderande_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2489; PDF p5 native; YE2024 empty",
f"bud_alderande_pnl_jr2025_statutory,{EID},2025,303348,303348,303348,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -18.84%,{SRC_PDF},strong,tick2489; PDF p5 native; YE2024 373765; bedrijfswinst 9901 288995 DROP; destin691 303348",
f"bud_alderande_bedrijfswinst_jr2025_statutory,{EID},2025,288995,288995,288995,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -17.68% (was 351058),{SRC_PDF},strong,tick2489; PDF p5 native; YE2024 351058; 62 2790554 JUMP; 630 194321 JUMP; 66A 26552 JUMP; 640/8 59394 JUMP; 635/9 19372 DROP; 631/4 empty",
f"bud_alderande_equity_jr2025_statutory,{EID},2025,4235304,4235304,4235304,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +6.88%,{SRC_PDF},strong,tick2489; PDF p4 native; YE2024 3962778; kapitaalsubsidies 15 265741 DROP; overgedragen 14 empty; fondsen 10 1175910 JUMP; bestemde fondsen 13 2793653 DROP",
f"bud_alderande_assets_jr2025_statutory,{EID},2025,5885663,5885663,5885663,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +5.23%,{SRC_PDF},strong,tick2489; PDF p3 native; YE2024 5593240; MVA 22/27 1968816 JUMP; cash 650911 JUMP; geldbeleggingen 2564849 JUMP; aanbouw 27 65960 JUMP; FVA 28 43999; LT recv 29 235419 DROP",
f"bud_alderande_debt_jr2025_statutory,{EID},2025,1353192,1353192,1353192,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +0.04%,{SRC_PDF},strong,tick2489; PDF p4 native; YE2024 1352667; 17 753056 DROP; 42/48 585781 JUMP",
f"bud_alderande_cash_jr2025_statutory,{EID},2025,650911,650911,650911,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +15.22%,{SRC_PDF},strong,tick2489; PDF p3 native; YE2024 564939; geldbeleggingen 50/53 2564849 JUMP; capex 8169 217123",
f"bud_alderande_destin_jr2025_statutory,{EID},2025,303348,303348,303348,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -18.84% (791 empty; 13 DROP 2793653),{SRC_PDF},strong,tick2489; PDF p6 native; YE2024 destin 373765; 791 empty; 14 empty; fondsen 10 JUMP 1175910",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":560746,\"\"2025_73\"\":3183043,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":3743789,\"\"2025_bruto9900\"\":3379188,"
"\"\"2025_pnl\"\":303348,\"\"2025_bedrijfswinst\"\":288995,"
"\"\"2025_equity\"\":4235304,\"\"2025_assets\"\":5885663,\"\"2025_debt\"\":1353192,"
"\"\"2025_fte\"\":36.6,\"\"2025_kapitaalsubsidies\"\":265741,\"\"2025_destin691\"\":303348,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":650911,\"\"2025_geldbeleggingen\"\":2564849,"
"\"\"2025_personnel62\"\":2790554,\"\"2025_gebouwen22\"\":1816942,"
"\"\"2025_aanbouw27\"\":65960,\"\"2025_66A\"\":26552,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":1175910,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":2793653,"
"\"\"2025_voorzieningen16\"\":297167,\"\"2025_630\"\":194321,\"\"2025_capex\"\":217123,"
"\"\"2025_ltrecv29\"\":235419,\"\"2025_75\"\":51249,\"\"2025_9903\"\":303348,"
"\"\"2024_omzet\"\":572476,\"\"2024_73\"\":3018391,"
"\"\"2024_opbr7076A\"\":3590867,\"\"2024_bruto9900\"\":3228837,\"\"2024_pnl\"\":373765,\"\"2024_bedrijfswinst\"\":351058,"
"\"\"2024_equity\"\":3962778,\"\"2024_assets\"\":5593240,"
"\"\"2024_debt\"\":1352667,\"\"2024_cash\"\":564939,\"\"2024_fte\"\":33.9,"
"\"\"2024_destin691\"\":373765,\"\"2024_kapitaalsubsidies\"\":296563,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":2343379}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Alderande YE2025 (70/76A JUMP 3.74m / omzet commercial vs 73 JUMP 3.18m / pnl DROP 70k / destin 303k / Strong PDF),{EID},VAPH + leftover city_lokeren VAPH,Alderande VZW (KBO 0431.893.389; Actief; 4 VE; zetel Lokeren),2026-06-18,2025,2025,3743789,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00183687.pdf,Public VAPH dual of mined city_lokeren,Publish VAPH / PVB / woon-dag matrix behind 70/76A 3.74m and 73 3.18m and why pnl DROP 303348 after YE2024 373765,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Lokeren>Alderande>JR2025_statutory_L5,tick2489; Strong official native PDF; leftover mined city_lokeren VAPH; 4 VE; prior-year identical; NOT De Hagewinde remine; NOT De Kapoentjes remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT De Cirkel remine; NOT CAR Kapelhof Drongen OFF; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Alderande 70/76A JUMP 3.74m / 73 JUMP 3.18m / pnl DROP 70k / destin 303k (YE2025 leftover city_lokeren VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Lokeren>Alderande>JR2025",
"3743789",
"3743789",
"PDF envelope 3743789 = 70/76A VZW because omzet commercial-only vs large 73; 70 560746; 73 3183043; 76A empty; bruto 3379188; bedrijfswinst DROP 288995; pnl DROP 303348; equity JUMP 4235304; assets JUMP 5885663; debt JUMP 1353192; FTE 36.6; kapitaalsubsidies DROP 265741; destin691 303348; cash JUMP 650911; capex 217123; leftover city_lokeren VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_lokeren VAPH",
"VAPH leftover city_lokeren",
"3.74m envelope; 73 3.18m; pnl DROP 70k; destin 303k; leftover city_lokeren VAPH",
"5.48",
"4.98",
"5.25",
"5.40",
"FOI VAPH / PVB / woon-dag matrix behind envelope 70/76A 3.74m + 73 JUMP 3.18m and why pnl DROP 303348 after YE2024 373765 while 62 JUMP 2790554 and FTE JUMP 36.6 and destin 303348 and cash JUMP 650911",
"active",
"",
"tick2489 leftover mined city_lokeren VAPH after Hagewinde lock; 4 VE; prior-year identical; NOT De Hagewinde remine tick2481; NOT De Kapoentjes remine tick2488; NOT De Zonnewende remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT De Cirkel remine; NOT De Poel leftover-via-VE; NOT ASTOR bankrupt; NOT Aralea YE2024; NOT CAR Kapelhof Drongen OFF; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Lokeren>Alderande>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / PVB / woon-dag / stad Lokeren split behind envelope 70/76A 3743789 (omzet 70 560746 commercial-only vs 73 3183043) and why pnl DROP 303348 after YE2024 373765 while destin 691 303348 and cash JUMP 650911",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_lokeren; VZW envelope 3.74m because omzet commercial-only vs large 73; public woon+dag 4 VE Lokeren; pnl DROP 70k / destin 303k / cash JUMP 651k",
"priority": "8",
"recipient_body": "ALDERANDE VZW / Raad van Bestuur",
"recipient_email": "info@alderande.be",
"recipient_postal": "Daknam-dorp 54 9160 Lokeren",
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
"notes": "tick2489; ready NOT sent; Strong official native NBB PDF; leftover mined city_lokeren VAPH after Hagewinde lock; 4 VE; prior-year identical; off De Hagewinde remine; off De Kapoentjes remine; off CAR Waas remine; off Ter Engelen remine; off De Cirkel remine; off De Poel leftover-via-VE; off CAR Kapelhof Drongen OFF; off Armonea commercial; off Vulpia commercial; off Korian commercial",
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
if rq_raw.count(b"rq_2489,")!=1: raise SystemExit(f"bad 2489 count {rq_raw.count(b'rq_2489,')}")
if b"rq_2490," in rq_raw: raise SystemExit("2490 exists")
idx=rq_raw.rfind(b"rq_2489,")
if idx<0: raise SystemExit("rq_2489 not found")
new_2489=(
"rq_2489,leftover dual Alderande YE2025,hole_fill,8,done,L5,vzw_alderande_lokeren,"
"Took unused leftover public VAPH Alderande 0431.893.389 leftover mined city_lokeren. Official NBB VKT-VZW YE2025 2026-00183687 native statutory 22p 498.8kB. Envelope 70/76A JUMP 3743789 (omzet commercial-only vs large 73 JUMP 3183043); pnl DROP 303348; destin 303348; cash JUMP 650911; FTE 36.6. FIRST leftover unused + live official YE2025 after leftover-type hunt (Halle leftover VAPH De Poel 0415.693.993 zetel Dilbeek leftover-via-VE SKIP; ASTOR Geel bankrupt SKIP; Aralea Brasschaat YE2024 SKIP; CAR Kapelhof Drongen OFF). NOT De Hagewinde remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT Huize De Veuster remine. NOT CAR Waas remine. NOT Ter Engelen remine. NOT De Cirkel remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2489 leftover mined city_lokeren VAPH; Strong native PDF; 4 VE; prior-year identical; next rq_2490 IS every-10\n"
)
new_2490=(
"rq_2490,every-10 progress after Alderande — then leftover dual hunt,hole_fill,8,open,L5,,"
"EVERY-10 tick. First refresh progress_every_10_ticks.md layers A-E and doge_waste_top10_current.md. Then unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken; leftover VAPH/CAR) / geel (Augustientjes CIK taken; leftover VAPH/CAR) / herentals (Bremdael WZC taken; leftover VAPH/CAR; OpWeg YE2024) / eeklo (leftover WZC; Kinderlach YE2024) / halle (CAR + CIK De Kapoentjes taken; leftover WZC/VAPH still open — De Poel 0415.693.993 zetel Dilbeek leftover-via-VE SKIP) / kalmthout (leftover WZC/VAPH) / bornem (CAR taken; leftover WZC/VAPH) / puurs (maatwerk taken; leftover WZC/VAPH) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde / mol / zoersel / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken) / lokeren (VAPH Hagewinde + Alderande taken — leftover WZC/CAR/maatwerk still open) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK + WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open — WZC Sint-Vincentius lead is Erpe-Mere YE2024). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT Alderande remine. NOT De Hagewinde remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT BWP remine. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2489 leftover city_lokeren VAPH; Alderande taken leftover mined city_lokeren VAPH; De Hagewinde taken leftover mined city_lokeren VAPH; De Kapoentjes taken leftover mined city_halle CIK; De Zonnewende taken leftover mined city_tielt WZC; THIS TICK IS EVERY-10\n"
)
if new_2489.count("\n")!=1 or new_2490.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2489",new_2489),("2490",new_2490)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2489.encode("utf-8"))
    f.write(new_2490.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2489", chk.count(b"rq_2489,"), "n2490", chk.count(b"rq_2490,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2489,2489,no,tick2489 leftover dual Alderande 0431.893.389 Strong native PDF (omzet70 DROP 560746 commercial-only vs large 73; 73 JUMP 3183043; 76A empty; envelope 70/76A JUMP 3743789; pnl DROP 303348; 9901 DROP 288995; equity JUMP 4235304; assets JUMP 5885663; debt JUMP 1353192; FTE JUMP 36.6; kapitaalsubsidies DROP 265741; destin691 DROP 303348; 791 empty; cash JUMP 650911; geldbeleggingen JUMP 2564849; capex 217123; 4 VE leftover city_lokeren VAPH); leftover mined city_lokeren VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (De Poel leftover-via-VE Dilbeek SKIP; ASTOR bankrupt SKIP; Aralea YE2024 SKIP; CAR Kapelhof Drongen OFF); NOT De Hagewinde remine; NOT De Kapoentjes remine; NOT De Zonnewende remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT De Cirkel remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2490 IS every-10\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2489 - rq_2489 Alderande Lokeren (70/76A JUMP 3.74m / 73 JUMP 3.18m / pnl DROP 70k / destin 303k / Strong PDF)

- Unit: **rq_2489** leftover dual after **De Kapoentjes@2488**. NOT every-10 (next **2490 IS every-10**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop. KBO phonetic GET 404; used official KBO activity + leftover-city name/postcode + NBB YE2025. FIRST leftover unused + live official YE2025 native euros after leftover-type hunt: Halle leftover VAPH **De Poel 0415.693.993** zetel Dilbeek leftover-via-VE SKIP; ASTOR Geel **0542.836.447** bankrupt SKIP; Aralea Brasschaat **0420.809.061** unused leftover maatwerk but last-balansjaar 2024 SKIP; CAR Kapelhof Zele **0412.402.032** zetel Kloosterstraat 6 9031 Drongen OFF; Re-HEAD YE2024 leftovers still YE2024. Confirmed `city_lokeren` exists (mined; leftover VAPH Hagewinde taken tick2481 — leftover unused entity Alderande). Took FREE leftover Flemish **ALDERANDE VZW** YE2025 (KBO **0431.893.389**; zetel Daknam-dorp 54 9160 Lokeren; **Actief** **4 VE** all 9160 Lokeren official KBO activity NACE 88106; leftover of mined **city_lokeren**; info@alderande.be; VAPH woon+dag+individuele ondersteuning; PC 31901). Identity trap: 0431.893.389 ≠ De Hagewinde **0861.262.010** remine ≠ CAR Waas **0415.472.279** remine ≠ Ter Engelen **0430.882.809** remine ≠ Sakura **0684.613.726** remine ≠ De Cirkel **0470.413.079** remine ≠ De Poel **0415.693.993** leftover-via-VE ≠ De Kapoentjes **0821.882.483** remine ≠ CAR Kapelhof **0412.402.032** Drongen OFF. 4 VE leftover of mined city_lokeren (Kerkstraat 62 + Kerkstraat 9 + Molenbergplein 2 + Zelestraat 166A; zetel Daknam-dorp 54). Confirmed leftover public VAPH not convent / not private / not WZC / not CIK / not commercial NV. VKT-VZW **native text** (not scan) — 498829 B / 22p all native euros (VKT-VZW 6.6 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00183687** (498829 B / 22p; AV **18.06.2026**; header **22.06.2026**; official NBB UUID 9b1bba84-5db7-11f1-b86a-ef50a6659ad6; CDN GET **200** 498829 official NBB-generated OpenPDF 1.3.26 CreationDate 22.06.2026 Last-Modified 29.06.2026 MD5 ffa112b8eb0fcb77cbbcdf76e3ecf4b1; all 22p native; prior-year identical not restated) — omzet 70 **EUR560746** DROP −2.05% (commercial-only vs large 73; was 572476); 73 **EUR3183043** JUMP +5.46% (was 3018391); 76A **empty**; envelope 70/76A **EUR3743789** JUMP +4.26% (VZW because omzet commercial-only vs large 73; was 3590867); bruto 9900 **EUR3379188** JUMP +4.66% (was 3228837); 62 **EUR2790554** JUMP +7.70%; 630 **EUR194321** JUMP +37.15%; 66A **EUR26552** JUMP; 640/8 **EUR59394** JUMP; 635/9 **EUR19372** DROP; 631/4 **empty**; bedrijfswinst 9901 **EUR288995** DROP −17.68% (was 351058); pnl 9904 **EUR303348** DROP −18.84% (was 373765); equity **EUR4235304** JUMP +6.88%; assets **EUR5885663** JUMP +5.23%; debt **EUR1353192** JUMP +0.04%; FTE **36.6** JUMP +7.96% (was 33.9; 100 36.6; 9087 36.6; 105 37.2); kapitaalsubsidies **EUR265741** DROP −10.39%; destin 691 **EUR303348** DROP −18.84%; 791 **empty**; cash **EUR650911** JUMP +15.22%; geldbeleggingen **EUR2564849** JUMP +9.45%; gebouwen **EUR1816942** DROP; MVA 22/27 **EUR1968816** JUMP; aanbouw **EUR65960** JUMP; capex **EUR217123**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 4 VE leftover mined city_lokeren VAPH. NOT De Hagewinde remine. NOT De Kapoentjes remine. NOT CAR Waas remine. NOT Ter Engelen remine. NOT De Cirkel remine. NOT De Poel leftover-via-VE. NOT CAR Kapelhof Drongen OFF. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.40); entities (+1 vzw_alderande_lokeren); foi + draft `gap_alderande_lokeren_vaph_matrix_70_76A_3_74m_omzet_commercial_73_jump_3_18m_pnl_drop_70k_destin_303k_l5`; rq_2489=done + rq_2490 open EVERY-10; loop_state ticks=2489; raw tick2489/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490 IS every-10**). Next: rq_2490 EVERY-10 progress then unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Alderande remine / NOT De Hagewinde remine / NOT De Kapoentjes remine / NOT De Zonnewende remine / NOT WZC Sint-Vincentius Erpe-Mere YE2024 / NOT Huize De Veuster remine / NOT Grijkoort remine / NOT GR.O.O.D. no JR / NOT Nektari remine / NOT Reva Ter Linde remine / NOT BWP remine / NOT CAR Waas remine / NOT Ter Engelen remine / NOT De Cirkel remine / NOT De Poel leftover-via-VE / NOT ASTOR bankrupt / NOT Aralea YE2024 / NOT CAR Kapelhof Drongen OFF / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_lokeren VAPH has Hagewinde + Alderande. Leftover WZC/CAR/maatwerk of city_lokeren still open.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

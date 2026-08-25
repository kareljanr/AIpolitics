from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2490_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_sperwer_jr2025_nbb_pdf_2490"
SRC_KBO="src_sperwer_kbo_2490"
SRC_SBM="src_sperwer_sbm_2490"
SRC_SITE="src_sperwer_site_2490"
EID="vzw_sperwer_lokeren"
GAP="gap_sperwer_lokeren_maatwerk_matrix_bruto_3_65m_omzet73_empty_pnl_drop_132k_destin_132k_l5"
COMM="comm_sperwer_jr2025_statutory_bruto_3_65m_omzet73_empty_pnl_drop_132k_destin_132k"
LB="lb_sperwer_bruto_365m_omzet73_empty_pnl_drop_132k_destin_132k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Alderande 0431.893.389 remine tick2489; NOT De Hagewinde 0861.262.010 remine tick2481; NOT De Cirkel 0470.413.079 remine; NOT CAR Waas 0415.472.279 remine; NOT Ter Engelen 0430.882.809 remine; NOT Sakura 0684.613.726 remine; NOT PUUR MAATWERK BV 0844.096.770 commercial; NOT Werkplus 0466.950.179 remine; NOT De Kapoentjes 0821.882.483 remine; NOT De Zonnewende 0735.627.214 remine; NOT Huize De Veuster 0476.354.132 remine; NOT Grijkoort remine; NOT GR.O.O.D. 0885.458.164 no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT BWP remine; NOT De Poel leftover-via-VE; NOT ASTOR bankrupt; NOT Aralea YE2024; NOT CAR Kapelhof Drongen OFF; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 De Sperwer Lokeren deposit 2026-00155231,http://cdn.staatsbladmonitor.be/2026pdf/2026-00155231.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2490; official native statutory PDF 54113 bytes 16p VKT-VZW 26.0.12 m04-f; header 12.06.2026; AV 09.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-12 07:13:56 UTC OpenPDF 1.3.26; CDN Last-Modified 19.06.2026; statutory pages native; CDN 2026-00155231 GET 200 54113 MD5 b3eae39804d808d585d78fc0b4d9981c; official NBB UUID 153e4903-55aa-11f0-96c0-11e19ebfc25a; VKT-VZW 6.1.1 6.1.3 6.5 6.6 7 8 niet dienstig; 6.1.2 6.2 6.3 6.4 6.7 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Sperwer Lokeren 0415.344.892,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415344892,KBO Public Search FOD Economie,{DAY},official_register,tick2490; Actief; 3 VE leftover city_lokeren (Gentsesteenweg 54 Lokeren; Gentsesteenweg 358 Lokeren; Donklaan 119 Berlare); zetel Gentsesteenweg 54 9160 Lokeren; VZW; begindatum 25.07.1975; RSZ2025 88.993; FOI info@desperwer.be; leftover mined city_lokeren maatwerk after Hagewinde+Alderande VAPH locks; NOT De Cirkel remine; NOT Alderande remine; NOT De Hagewinde remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT PUUR MAATWERK BV commercial",
f"{SRC_SBM},NBB Consult / SBM fiche De Sperwer 0415344892 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0415344892,NBB Consult / SBM,{DAY},official_register,tick2490; deposit-id 2026-00155231 YE 01.01.2025-31.12.2025 filing VKT-VZW Verkort model vereniging Initial UUID 153e4903-55aa-11f0-96c0-11e19ebfc25a; Companyweb last-balansjaar used for deposit-id discovery via NBB OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},De Sperwer Lokeren FOI contact leftover city_lokeren maatwerk,https://desperwer.be/,De Sperwer VZW leftover city_lokeren maatwerk 3 VE,{DAY},foi_contact,tick2490; FOI info@desperwer.be; zetel Gentsesteenweg 54 9160 Lokeren; VAPH-vergunde zorgaanbieder werken+wonen+vrije tijd; RSZ2025 88.993; leftover mined city_lokeren maatwerk after VAPH locks; NOT De Cirkel remine; NOT Alderande remine; NOT De Hagewinde remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT PUUR MAATWERK BV commercial; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},De Sperwer,ASBL De Sperwer,De Sperwer VZW (leftover city_lokeren maatwerk),parastatal,city_lokeren,nl,https://desperwer.be/,info@desperwer.be,Gentsesteenweg 54 9160 Lokeren,tick2490 YE2025 Strong official native NBB PDF deposit 2026-00155231 + Strong KBO 0415.344.892 Actief 3 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 3648803; pnl DROP 132424; 9901 DROP 136599; equity JUMP 3469151; assets JUMP 4103906; debt DROP 634755; FTE JUMP 37.5; kapitaalsubsidies DROP 125737; destin691 DROP 132424; 791 empty; cash JUMP 1030218; geldbeleggingen JUMP 300000; leftover city_lokeren maatwerk 3 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_sperwer_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty VKT,{SRC_PDF},strong,tick2490; PDF p6 native; YE2024 empty; 73 empty; 76A empty",
f"bud_sperwer_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty VKT,{SRC_PDF},strong,tick2490; PDF p6 native; YE2024 empty; FOI maatwerk/VAPH matrix behind bruto",
f"bud_sperwer_opbr_jr2025_statutory,{EID},2025,3648803,3648803,3648803,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +8.61% (VKT because omzet empty),{SRC_PDF},strong,tick2490; PDF p6 native; YE2024 3359401; 70 empty; 73 empty; 76A empty",
f"bud_sperwer_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2490; PDF p6 native; YE2024 empty",
f"bud_sperwer_pnl_jr2025_statutory,{EID},2025,132424,132424,132424,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -45.87%,{SRC_PDF},strong,tick2490; PDF p6 native; YE2024 244661; bedrijfswinst 9901 136599 DROP; destin691 132424",
f"bud_sperwer_bedrijfswinst_jr2025_statutory,{EID},2025,136599,136599,136599,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -45.59% (was 251065),{SRC_PDF},strong,tick2490; PDF p6 native; YE2024 251065; 62 3112334 JUMP; 630 203313 DROP; 66A 81914 JUMP; 640/8 114643 JUMP; 635/9 empty; 631/4 empty",
f"bud_sperwer_equity_jr2025_statutory,{EID},2025,3469151,3469151,3469151,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +3.30%,{SRC_PDF},strong,tick2490; PDF p5 native; YE2024 3358400; kapitaalsubsidies 15 125737 DROP; overgedragen 14 990906 FLAT; fondsen 10 379249 FLAT; bestemde fondsen 13 1973260 JUMP",
f"bud_sperwer_assets_jr2025_statutory,{EID},2025,4103906,4103906,4103906,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.60%,{SRC_PDF},strong,tick2490; PDF p4 native; YE2024 4000105; MVA 22/27 2642991 DROP; cash 1030218 JUMP; geldbeleggingen 300000 JUMP; aanbouw 27 empty",
f"bud_sperwer_debt_jr2025_statutory,{EID},2025,634755,634755,634755,NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.08%,{SRC_PDF},strong,tick2490; PDF p5 native; YE2024 641705; 17 74758 DROP; 42/48 559997 JUMP",
f"bud_sperwer_cash_jr2025_statutory,{EID},2025,1030218,1030218,1030218,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +0.67%,{SRC_PDF},strong,tick2490; PDF p4 native; YE2024 1023330; geldbeleggingen 50/53 300000 JUMP; capex 8169 158610",
f"bud_sperwer_destin_jr2025_statutory,{EID},2025,132424,132424,132424,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -45.87% (791 empty; 13 JUMP 1973260),{SRC_PDF},strong,tick2490; PDF p7 native; YE2024 destin 244661; 791 empty; 14 990906 FLAT; fondsen 10 379249 FLAT",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":0,\"\"2025_bruto9900\"\":3648803,"
"\"\"2025_pnl\"\":132424,\"\"2025_bedrijfswinst\"\":136599,"
"\"\"2025_equity\"\":3469151,\"\"2025_assets\"\":4103906,\"\"2025_debt\"\":634755,"
"\"\"2025_fte\"\":37.5,\"\"2025_kapitaalsubsidies\"\":125737,\"\"2025_destin691\"\":132424,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1030218,\"\"2025_geldbeleggingen\"\":300000,"
"\"\"2025_personnel62\"\":3112334,\"\"2025_gebouwen22\"\":2493281,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":81914,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":379249,\"\"2025_overgedragen14\"\":990906,"
"\"\"2025_bestemdefondsen13\"\":1973260,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":203313,\"\"2025_capex\"\":158610,"
"\"\"2025_75\"\":4077,\"\"2025_9903\"\":136342,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr7076A\"\":0,\"\"2024_bruto9900\"\":3359401,\"\"2024_pnl\"\":244661,\"\"2024_bedrijfswinst\"\":251065,"
"\"\"2024_equity\"\":3358400,\"\"2024_assets\"\":4000105,"
"\"\"2024_debt\"\":641705,\"\"2024_cash\"\":1023330,\"\"2024_fte\"\":35.2,"
"\"\"2024_destin691\"\":244661,\"\"2024_kapitaalsubsidies\"\":147410,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":150000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Sperwer YE2025 (bruto JUMP 3.65m / omzet+73 empty VKT / pnl DROP 132k / destin 132k / Strong PDF),{EID},maatwerk + leftover city_lokeren maatwerk,De Sperwer VZW (KBO 0415.344.892; Actief; 3 VE; zetel Lokeren),2026-06-09,2025,2025,3648803,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00155231.pdf,Public maatwerk dual of mined city_lokeren,Publish maatwerk / VAPH woon-werk matrix behind bruto 3.65m and why pnl DROP 132424 after YE2024 244661,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Lokeren>De Sperwer>JR2025_statutory_L5,tick2490; Strong official native PDF; leftover mined city_lokeren maatwerk; 3 VE; prior-year identical; NOT Alderande remine; NOT De Hagewinde remine; NOT De Cirkel remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT PUUR MAATWERK BV commercial; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"De Sperwer bruto JUMP 3.65m / omzet+73 empty VKT / pnl DROP 132k / destin 132k (YE2025 leftover city_lokeren maatwerk)",
"L5",
"maatwerk_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Lokeren>De Sperwer>JR2025",
"3648803",
"3648803",
"PDF envelope 3648803 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A empty; bedrijfswinst DROP 136599; pnl DROP 132424; equity JUMP 3469151; assets JUMP 4103906; debt DROP 634755; FTE 37.5; kapitaalsubsidies DROP 125737; destin691 132424; cash JUMP 1030218; capex 158610; leftover city_lokeren maatwerk",
"strong",
SRC_PDF,
"maatwerk + leftover city_lokeren maatwerk",
"maatwerk leftover city_lokeren",
"3.65m bruto; omzet+73 empty VKT; pnl DROP 132k; destin 132k; leftover city_lokeren maatwerk",
"5.52",
"5.32",
"5.18",
"5.34",
"FOI maatwerk / VAPH woon-werk matrix behind bruto 3.65m and why pnl DROP 132424 after YE2024 244661 while 62 JUMP 3112334 and FTE JUMP 37.5 and destin 132424 and 66A JUMP 81914",
"active",
"",
"tick2490 leftover mined city_lokeren maatwerk after Hagewinde+Alderande VAPH locks; 3 VE; prior-year identical; THIS TICK IS every-10; NOT Alderande remine tick2489; NOT De Hagewinde remine tick2481; NOT De Cirkel remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT PUUR MAATWERK BV commercial; NOT De Kapoentjes remine; NOT De Zonnewende remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT BWP remine; NOT De Poel leftover-via-VE; NOT ASTOR bankrupt; NOT Aralea YE2024; NOT CAR Kapelhof Drongen OFF; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Lokeren>De Sperwer>maatwerk",
"entity_id": EID,
"what_is_missing": "maatwerk / VAPH woon-werk / stad Lokeren split behind bruto 9900 3648803 (omzet 70 empty VKT; 73 empty VKT) and why pnl DROP 132424 after YE2024 244661 while destin 691 132424 and 66A JUMP 81914",
"why_it_matters": "Strong official PDF leftover public maatwerk of mined city_lokeren; VKT envelope 3.65m because omzet empty; public werken+wonen 3 VE; pnl DROP 112k / destin 132k / 66A JUMP 82k",
"priority": "8",
"recipient_body": "DE SPERWER VZW / Raad van Bestuur",
"recipient_email": "info@desperwer.be",
"recipient_postal": "Gentsesteenweg 54 9160 Lokeren",
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
"notes": "tick2490; ready NOT sent; Strong official native NBB PDF; leftover mined city_lokeren maatwerk after Hagewinde+Alderande VAPH locks; 3 VE; prior-year identical; THIS TICK IS every-10; off Alderande remine; off De Hagewinde remine; off De Cirkel remine; off CAR Waas remine; off Ter Engelen remine; off PUUR MAATWERK BV commercial; off Armonea commercial; off Vulpia commercial; off Korian commercial",
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
if rq_raw.count(b"rq_2490,")!=1: raise SystemExit(f"bad 2490 count {rq_raw.count(b'rq_2490,')}")
if b"rq_2491," in rq_raw: raise SystemExit("2491 exists")
idx=rq_raw.rfind(b"rq_2490,")
if idx<0: raise SystemExit("rq_2490 not found")
new_2490=(
"rq_2490,leftover dual De Sperwer YE2025 + every-10,hole_fill,8,done,L5,vzw_sperwer_lokeren,"
"Took unused leftover public maatwerk De Sperwer 0415.344.892 leftover mined city_lokeren. Official NBB VKT-VZW YE2025 2026-00155231 native statutory 16p 54.1kB. Envelope bruto 9900 JUMP 3648803 (omzet+73 empty VKT); pnl DROP 132424; destin 132424; 66A JUMP 81914; FTE 37.5. FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88993 + 9160; PUUR MAATWERK BV commercial SKIP; De Cirkel remine; Werkplus remine; WZC Sint-Pieter OCMW-vereniging remine). EVERY-10 refresh of progress_every_10_ticks.md + doge_waste_top10_current.md. NOT Alderande remine. NOT De Hagewinde remine. NOT CAR Waas remine. NOT Ter Engelen remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT Nektari remine. NOT Reva Ter Linde remine. NOT BWP remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2490 leftover mined city_lokeren maatwerk + every-10; Strong native PDF; 3 VE; prior-year identical; next rq_2491 NOT every-10 (next every-10 is 2500)\n"
)
new_2491=(
"rq_2491,leftover dual hunt after De Sperwer + every-10,hole_fill,8,open,L5,,"
"NOT every-10 (next every-10 is 2500). Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken) / geel (Augustientjes CIK taken; leftover VAPH/CAR/WZC/maatwerk) / herentals (Bremdael WZC taken; leftover VAPH/CAR; OpWeg YE2024) / eeklo (Kinderlach YE2024) / halle (CAR + CIK taken; leftover WZC exhausted; leftover VAPH still open — De Poel leftover-via-VE SKIP) / kalmthout / bornem (CAR taken; leftover WZC/VAPH) / puurs (maatwerk taken; leftover WZC/VAPH) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde / mol / zoersel / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken) / lokeren (VAPH Hagewinde + Alderande taken; maatwerk De Sperwer taken — leftover WZC/CAR still open but Ter Engelen remine / CAR Waas remine) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK + WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg / WZC Sint-Vincentius Erpe-Mere / Aralea still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT De Sperwer remine. NOT Alderande remine. NOT De Hagewinde remine. NOT De Cirkel remine. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT BWP remine. NOT De Poel leftover-via-VE. NOT ASTOR bankrupt. NOT Aralea YE2024. NOT CAR Kapelhof Drongen OFF. NOT PUUR MAATWERK BV commercial. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2490 leftover city_lokeren maatwerk + every-10; De Sperwer taken leftover mined city_lokeren maatwerk; Alderande + Hagewinde taken leftover mined city_lokeren VAPH; NOT every-10 (next 2500)\n"
)
if new_2490.count("\n")!=1 or new_2491.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2490",new_2490),("2491",new_2491)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2490.encode("utf-8"))
    f.write(new_2491.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2490", chk.count(b"rq_2490,"), "n2491", chk.count(b"rq_2491,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2490,2490,no,tick2490 leftover dual De Sperwer 0415.344.892 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 3648803; pnl DROP 132424; 9901 DROP 136599; equity JUMP 3469151; assets JUMP 4103906; debt DROP 634755; FTE JUMP 37.5; kapitaalsubsidies DROP 125737; destin691 DROP 132424; 791 empty; cash JUMP 1030218; geldbeleggingen JUMP 300000; capex 158610; 66A JUMP 81914; 3 VE leftover city_lokeren maatwerk) + EVERY-10; leftover mined city_lokeren maatwerk; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (KBO activity NACE 88993 + 9160; PUUR MAATWERK BV SKIP; De Cirkel remine; Werkplus remine); NOT Alderande remine; NOT De Hagewinde remine; NOT De Cirkel remine; NOT CAR Waas remine; NOT Ter Engelen remine; NOT De Kapoentjes remine; NOT De Zonnewende remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT BWP remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next rq_2491 NOT every-10 (next every-10 is 2500)\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2490 - rq_2490 De Sperwer Lokeren (bruto JUMP 3.65m / omzet+73 empty VKT / pnl DROP 132k / destin 132k / Strong PDF) + EVERY-10

- Unit: **rq_2490** leftover dual after **Alderande@2489**. THIS TICK IS EVERY-10. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop. Official KBO activity NACE **88993** + leftover-city postcode 9160 + NBB YE2025. FIRST leftover unused + live official YE2025 native euros after leftover-type hunt: PUUR MAATWERK **0844.096.770** BV commercial SKIP; WZC Sint-Pieter **0664.681.216** Vereniging van OCMW's remine; Werkplus **0466.950.179** remine tick2204; De Cirkel **0470.413.079** remine; WZG Voorkempen remine; Re-HEAD YE2024 leftovers still YE2024. Confirmed `city_lokeren` exists (mined; leftover VAPH Hagewinde + Alderande taken — leftover unused maatwerk). Took FREE leftover Flemish **DE SPERWER VZW** YE2025 (KBO **0415.344.892**; zetel Gentsesteenweg 54 9160 Lokeren; **Actief** **3 VE**; RSZ2025 **88.993**; leftover of mined **city_lokeren**; info@desperwer.be; VAPH-vergunde zorgaanbieder werken+wonen+vrije tijd). Identity trap: 0415.344.892 ≠ De Cirkel **0470.413.079** remine ≠ Alderande **0431.893.389** remine ≠ De Hagewinde **0861.262.010** remine ≠ CAR Waas **0415.472.279** remine ≠ Ter Engelen **0430.882.809** remine ≠ Sakura **0684.613.726** remine ≠ PUUR MAATWERK BV **0844.096.770** commercial. 3 VE leftover of mined city_lokeren (Gentsesteenweg 54 + Gentsesteenweg 358 Lokeren + Donklaan 119 Berlare; zetel Gentsesteenweg 54). Confirmed leftover public maatwerk not convent / not private / not WZC / not CIK / not commercial NV. VKT-VZW **native text** (not scan) — 54113 B / 16p all native euros (VKT-VZW 6.1.1 6.1.3 6.5 6.6 7 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00155231** (54113 B / 16p; AV **09.06.2026**; header **12.06.2026**; official NBB UUID 153e4903-55aa-11f0-96c0-11e19ebfc25a; CDN GET **200** 54113 official NBB-generated OpenPDF 1.3.26 CreationDate 12.06.2026 Last-Modified 19.06.2026 MD5 b3eae39804d808d585d78fc0b4d9981c; all 16p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR3648803** JUMP +8.61% (VKT because omzet empty; was 3359401); 62 **EUR3112334** JUMP +10.86%; 630 **EUR203313** DROP −0.37%; 66A **EUR81914** JUMP; 640/8 **EUR114643** JUMP; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR136599** DROP −45.59% (was 251065); pnl 9904 **EUR132424** DROP −45.87% (was 244661); equity **EUR3469151** JUMP +3.30%; assets **EUR4103906** JUMP +2.60%; debt **EUR634755** DROP −1.08%; FTE **37.5** JUMP +6.53% (was 35.2; 100 37.5; 9087 37.5; 105 36.6); kapitaalsubsidies **EUR125737** DROP −14.70%; destin 691 **EUR132424** DROP −45.87%; 791 **empty**; cash **EUR1030218** JUMP +0.67%; geldbeleggingen **EUR300000** JUMP +100.00%; gebouwen **EUR2493281** DROP; MVA 22/27 **EUR2642991** DROP; aanbouw **empty**; capex **EUR158610**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 3 VE leftover mined city_lokeren maatwerk. NOT Alderande remine. NOT De Hagewinde remine. NOT De Cirkel remine. NOT CAR Waas remine. NOT Ter Engelen remine. NOT PUUR MAATWERK BV commercial. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.34); entities (+1 vzw_sperwer_lokeren); foi + draft `gap_sperwer_lokeren_maatwerk_matrix_bruto_3_65m_omzet73_empty_pnl_drop_132k_destin_132k_l5`; rq_2490=done + rq_2491 open; loop_state ticks=2490; raw tick2490/ untracked. EVERY-10 refresh of progress_every_10_ticks.md + doge_waste_top10_current.md from live inventory after leftover write.
- FOI: **ready not sent**. Tick **2490 IS every-10**. Next: rq_2491 leftover dual (NOT every-10; next every-10 is **2500**). NOW leftover city_lokeren maatwerk taken (VAPH Hagewinde + Alderande already taken). Leftover WZC/CAR of city_lokeren still open but Ter Engelen remine / CAR Waas remine.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")

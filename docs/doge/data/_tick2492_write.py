from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2492_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_3wplus_werk_jr2025_nbb_pdf_2492"
SRC_KBO="src_3wplus_werk_kbo_2492"
SRC_SBM="src_3wplus_werk_sbm_2492"
SRC_SITE="src_3wplus_werk_site_2492"
EID="vzw_3wplus_werk_asse"
GAP="gap_3wplus_werk_asse_maatwerk_matrix_bruto_2_63m_omzet73_empty_pnl_flip_49k_l5"
COMM="comm_3wplus_werk_jr2025_statutory_bruto_2_63m_omzet73_empty_pnl_flip_49k"
LB="lb_3wplus_werk_bruto_263m_omzet73_empty_pnl_flip_49k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT 3Wplus Kinderopvang 0893.870.539 remine tick2407; NOT AMAB 0411.635.039 remine tick2277; NOT GROEP 3WPLUS 0674.926.988; NOT Hopperank 0434.363.921 remine tick2491; NOT Vijverbeek 0448.164.744 remine tick2469; NOT Hof ter Waarbeek 0478.728.256 remine; NOT Walfergem 0633.687.439 remine; NOT ViTeS 0431.067.802 leftover-via-VE; NOT Groep INTRO 0472.098.703 leftover-via-VE; NOT De Sperwer 0415.344.892 remine; NOT Alderande 0431.893.389 remine; NOT De Hagewinde 0861.262.010 remine; NOT De Kapoentjes remine; NOT De Zonnewende remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT Nektari remine; NOT Reva Ter Linde remine; NOT BWP remine; NOT De Poel leftover-via-VE; NOT ASTOR bankrupt; NOT Aralea YE2024; NOT CAR Kapelhof Drongen OFF; NOT MILLE LUCI CVBA no JR; NOT Huis Coppens commercial; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 3Wplus Werk Asse deposit 2026-00271890,http://cdn.staatsbladmonitor.be/2026pdf/2026-00271890.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2492; official native statutory PDF 309825 bytes 26p VKT-VZW 26.0.15 m04-f; header 09.07.2026; AV 26.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-09 09:41:57 UTC OpenPDF 1.3.26; CDN Last-Modified 29.07.2026; statutory pages native; CDN 2026-00271890 GET 200 309825 MD5 8c29488f1a1fae7afecd118ca9f27390; official NBB UUID 2362fb06-7b77-11f1-886f-e597a8377b24; VKT-VZW 7 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO 3Wplus Werk Asse 0467.004.520,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0467004520,KBO Public Search FOD Economie,{DAY},official_register,tick2492; Actief; 3 VE leftover city_asse (Z. 5 Mollem 250 1730 Asse VE 2.155.000.302 since 10.07.2006; Solheide 16 3090 Overijse VE 2.193.009.058 since 01.09.2005; Marcel Felicestraat 29 1560 Hoeilaart VE 2.342.002.246 since 01.03.2023); zetel Z. 5 Mollem 250 1730 Asse since 01.03.2020; VZW since 11.03.1999; RSZ2025 88.993; FOI maatwerk@3wplus.be; leftover mined city_asse maatwerk after Hopperank VAPH + 3Wplus+Vijverbeek CIK locks; NOT AMAB remine; NOT 3Wplus Kinderopvang remine; NOT GROEP 3WPLUS; NOT Hopperank remine",
f"{SRC_SBM},NBB Consult / SBM fiche 3Wplus Werk 0467004520 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0467004520,NBB Consult / SBM,{DAY},official_register,tick2492; deposit-id 2026-00271890 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial UUID 2362fb06-7b77-11f1-886f-e597a8377b24; NBB published-deposits/ids + broker PDF used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},3Wplus Werk Asse FOI contact leftover city_asse maatwerk,https://3wplus.be/,3Wplus Werk VZW leftover city_asse maatwerk 3 VE,{DAY},foi_contact,tick2492; FOI maatwerk@3wplus.be; zetel Z. 5 Mollem 250 1730 Asse; RSZ2025 88.993 beschutte/sociale werkplaatsen PC 32701; leftover mined city_asse maatwerk after Hopperank VAPH lock; NOT AMAB remine; NOT 3Wplus Kinderopvang remine; NOT GROEP 3WPLUS; NOT Hopperank remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},3Wplus Werk,ASBL 3Wplus Werk,3Wplus Werk VZW (leftover city_asse maatwerk),parastatal,city_asse,nl,https://3wplus.be/,maatwerk@3wplus.be,Z. 5 Mollem 250 1730 Asse,tick2492 YE2025 Strong official native NBB PDF deposit 2026-00271890 + Strong KBO 0467.004.520 Actief 3 VE; omzet70 empty VKT; 73 empty VKT; 76A DROP 1000; envelope bruto9900 JUMP 2631017; pnl FLIP 49057; 9901 JUMP 67042; equity JUMP 1625771; assets DROP 3392304; debt DROP 1766533; FTE JUMP 56.8; kapitaalsubsidies DROP 63475; destin691 empty; 791 empty; cash JUMP 494869; geldbeleggingen empty; leftover city_asse maatwerk 3 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_3wplus_werk_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty VKT,{SRC_PDF},strong,tick2492; PDF p6 native; YE2024 empty; 73 empty; 76A DROP 1000",
f"bud_3wplus_werk_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty VKT,{SRC_PDF},strong,tick2492; PDF p6 native; YE2024 empty; FOI maatwerk/Departement Werk matrix behind bruto",
f"bud_3wplus_werk_opbr_jr2025_statutory,{EID},2025,2631017,2631017,2631017,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +5.66% (VKT because omzet empty),{SRC_PDF},strong,tick2492; PDF p6 native; YE2024 2490048; 70 empty; 73 empty; 76A DROP 1000",
f"bud_3wplus_werk_76A_jr2025_statutory,{EID},2025,1000,1000,1000,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -93.85%,{SRC_PDF},strong,tick2492; PDF p6 native; YE2024 16250",
f"bud_3wplus_werk_pnl_jr2025_statutory,{EID},2025,49057,49057,49057,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP (was LOSS -4970),{SRC_PDF},strong,tick2492; PDF p6 native; YE2024 -4970; bedrijfswinst 9901 67042 JUMP; destin691 empty",
f"bud_3wplus_werk_bedrijfswinst_jr2025_statutory,{EID},2025,67042,67042,67042,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +487.88% (was 11404),{SRC_PDF},strong,tick2492; PDF p6 native; YE2024 11404; 62 2340946 JUMP; 630 147618 JUMP; 66A empty; 640/8 75412 JUMP; 635/9 empty; 631/4 empty",
f"bud_3wplus_werk_equity_jr2025_statutory,{EID},2025,1625771,1625771,1625771,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.12%,{SRC_PDF},strong,tick2492; PDF p5 native; YE2024 1592017; kapitaalsubsidies 15 63475 DROP; overgedragen 14 1072958 JUMP; fondsen 10 empty; bestemde fondsen 13 489338 FLAT",
f"bud_3wplus_werk_assets_jr2025_statutory,{EID},2025,3392304,3392304,3392304,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -0.84%,{SRC_PDF},strong,tick2492; PDF p4 native; YE2024 3420909; MVA 22/27 2320375 JUMP; cash 494869 JUMP; geldbeleggingen empty; aanbouw 27 3236 DROP",
f"bud_3wplus_werk_debt_jr2025_statutory,{EID},2025,1766533,1766533,1766533,NBB VKT-VZW code 17/49 schulden YE2025 DROP -3.39%,{SRC_PDF},strong,tick2492; PDF p5 native; YE2024 1828529; 17 1086704 DROP; 42/48 679829 JUMP",
f"bud_3wplus_werk_cash_jr2025_statutory,{EID},2025,494869,494869,494869,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +1.36%,{SRC_PDF},strong,tick2492; PDF p4 native; YE2024 488222; geldbeleggingen 50/53 empty; capex 8169 226984",
f"bud_3wplus_werk_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 FLAT 489338),{SRC_PDF},strong,tick2492; PDF p7 native; YE2024 destin empty; 791 empty; 14 JUMP 1072958; fondsen 10 empty",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":1000,"
"\"\"2025_opbr7076A\"\":0,\"\"2025_bruto9900\"\":2631017,"
"\"\"2025_pnl\"\":49057,\"\"2025_bedrijfswinst\"\":67042,"
"\"\"2025_equity\"\":1625771,\"\"2025_assets\"\":3392304,\"\"2025_debt\"\":1766533,"
"\"\"2025_fte\"\":56.8,\"\"2025_kapitaalsubsidies\"\":63475,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":494869,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":2340946,\"\"2025_gebouwen22\"\":1802320,"
"\"\"2025_aanbouw27\"\":3236,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":1072958,"
"\"\"2025_bestemdefondsen13\"\":489338,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":147618,\"\"2025_capex\"\":226984,"
"\"\"2025_6408\"\":75412,\"\"2025_75\"\":8469,\"\"2025_9903\"\":49057,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr7076A\"\":0,\"\"2024_bruto9900\"\":2490048,\"\"2024_pnl\"\":-4970,\"\"2024_bedrijfswinst\"\":11404,"
"\"\"2024_equity\"\":1592017,\"\"2024_assets\"\":3420909,"
"\"\"2024_debt\"\":1828529,\"\"2024_cash\"\":488222,\"\"2024_fte\"\":55,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":78777,\"\"2024_76A\"\":16250,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},3Wplus Werk YE2025 (bruto JUMP 2.63m / omzet+73 empty VKT / pnl FLIP 49k / Strong PDF),{EID},maatwerk + leftover city_asse maatwerk,3Wplus Werk VZW (KBO 0467.004.520; Actief; 3 VE; zetel Asse),2026-06-26,2025,2025,2631017,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00271890.pdf,Public maatwerk dual of mined city_asse,Publish maatwerk/Departement Werk matrix behind bruto 2.63m and why pnl FLIP 49057 after YE2024 LOSS -4970,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Asse>3WplusWerk>JR2025_statutory_L5,tick2492; Strong official native PDF; leftover mined city_asse maatwerk; 3 VE; prior-year identical; NOT 3Wplus Kinderopvang remine; NOT AMAB remine; NOT Hopperank remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"3Wplus Werk bruto JUMP 2.63m / omzet+73 empty VKT / pnl FLIP 49k (YE2025 leftover city_asse maatwerk)",
"L5",
"maatwerk_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Asse>3WplusWerk>JR2025",
"2631017",
"2631017",
"PDF envelope 2631017 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A DROP 1000; bedrijfswinst JUMP 67042; pnl FLIP 49057; equity JUMP 1625771; assets DROP 3392304; debt DROP 1766533; FTE 56.8; kapitaalsubsidies DROP 63475; destin691 empty; cash JUMP 494869; capex 226984; leftover city_asse maatwerk",
"strong",
SRC_PDF,
"maatwerk + leftover city_asse maatwerk",
"maatwerk leftover city_asse",
"2.63m bruto; omzet+73 empty VKT; pnl FLIP 49k; leftover city_asse maatwerk",
"5.40",
"5.25",
"5.10",
"5.30",
"FOI maatwerk/Departement Werk matrix behind bruto 2.63m and why pnl FLIP 49057 after YE2024 LOSS -4970 while 640/8 JUMP 75412 and FTE JUMP 56.8",
"active",
"",
"tick2492 leftover mined city_asse maatwerk after Hopperank VAPH + 3Wplus+Vijverbeek CIK locks; 3 VE; prior-year identical; NOT every-10 (next 2500); NOT 3Wplus Kinderopvang remine; NOT AMAB remine; NOT GROEP 3WPLUS; NOT Hopperank remine; NOT Vijverbeek remine; NOT Hof ter Waarbeek remine; NOT Walfergem remine; NOT ViTeS leftover-via-VE; NOT Groep INTRO leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Asse>3WplusWerk>maatwerk",
"entity_id": EID,
"what_is_missing": "maatwerk / Departement Werk / VDAB / stad Asse split behind bruto 9900 2631017 (omzet 70 empty VKT; 73 empty VKT; 76A DROP 1000) and why pnl FLIP 49057 after YE2024 LOSS -4970 while destin 691 empty and 640/8 JUMP 75412",
"why_it_matters": "Strong official PDF leftover public maatwerk of mined city_asse; VKT envelope 2.63m because omzet empty; public beschutte/sociale werkplaats 3 VE; pnl FLIP from LOSS; 640/8 JUMP 5x",
"priority": "8",
"recipient_body": "3WPLUS WERK VZW / Raad van Bestuur",
"recipient_email": "maatwerk@3wplus.be",
"recipient_postal": "Z. 5 Mollem 250 1730 Asse",
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
"notes": "tick2492; ready NOT sent; Strong official native NBB PDF; leftover mined city_asse maatwerk after Hopperank VAPH + 3Wplus+Vijverbeek CIK locks; 3 VE; prior-year identical; NOT every-10 (next 2500); off 3Wplus Kinderopvang remine; off AMAB remine; off GROEP 3WPLUS; off Hopperank remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE APPEND DONE")

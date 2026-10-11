from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2495_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_trento_jr2025_nbb_pdf_2495"
SRC_KBO="src_trento_kbo_2495"
SRC_SBM="src_trento_sbm_2495"
SRC_SITE="src_trento_site_2495"
EID="vzw_zorgnetwerk_trento_hamme"
GAP="gap_trento_hamme_wzc_matrix_omzet_13_43m_73_jump_3_05m_destin_jump_2_30m_cash_drop_1_92m_l5"
COMM="comm_trento_jr2025_statutory_omzet_13_43m_73_jump_3_05m_destin_jump_2_30m"
LB="lb_trento_omzet_1343m_73_jump_305m_destin_jump_230m_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT leftover city_zele (Zele is VE only; zetel Hamme); NOT De Vlietoever BV Bornem 0898.596.122; NOT Woonzorg Samen Ouder 0453.287.037 remine bestuurder; NOT Avondzon remine; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT Doppa remine; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine leftover-via-VE Gent")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Zorgnetwerk Trento deposit 2026-00304248,http://cdn.staatsbladmonitor.be/2026pdf/2026-00304248.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2495; official native statutory PDF 1138780 bytes 45p VOL-VZW 26.0.15 m05-f; header 14.07.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-17 11:35:44 UTC OpenPDF 1.3.26; CDN Last-Modified 02.08.2026; statutory pages native; CDN 2026-00304248 GET 200 1138780 MD5 2ab1e7413417115cf41ab6fd84f4adbc; official NBB UUID c3c61694-7f7b-11f1-8707-69c56c02a08e; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1-2 6.5.1-3 6.16 6.18 niet dienstig; prior-year identical not restated; commissaris Moore Audit BV / Van der Biest Wendy; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Zorgnetwerk Trento 0455.449.048,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455449048,KBO Public Search FOD Economie,{DAY},official_register,tick2495; Actief; 2 VE leftover city_hamme (zetel Molenstraat 11 9220 Hamme since 07.02.1995; VE 2.150.785.453 WZC Sint-Jozef Hamme + VE 2.215.657.667 WZC De Vliet Koevliet 8 Zele); VZW since 07.02.1995; RSZ2025 87.301 ROB; FOI info@zorgnetwerktrento.be; leftover mined city_hamme WZC after leftover-type hunt; NOT leftover city_zele; NOT De Vlietoever BV; NOT Woonzorg Samen Ouder remine",
f"{SRC_SBM},NBB Consult / SBM fiche Trento 0455449048 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0455449048,NBB Consult / SBM,{DAY},official_register,tick2495; deposit-id 2026-00304248 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial UUID c3c61694-7f7b-11f1-8707-69c56c02a08e; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Zorgnetwerk Trento FOI contact leftover city_hamme WZC,https://www.zorgnetwerktrento.be/,Zorgnetwerk Trento VZW leftover city_hamme WZC 2 VE,{DAY},foi_contact,tick2495; FOI info@zorgnetwerktrento.be; bewonersbegeleiding@zorgnetwerktrento.be; zetel Molenstraat 11 9220 Hamme; campus De Vliet Koevliet 8 9240 Zele; RSZ2025 87.301 ROB; leftover mined city_hamme WZC; NOT leftover city_zele; NOT De Vlietoever BV; NOT Woonzorg Samen Ouder remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Zorgnetwerk Trento,ASBL Zorgnetwerk Trento,Zorgnetwerk Trento VZW (leftover city_hamme WZC),parastatal,city_hamme,nl,https://www.zorgnetwerktrento.be/,info@zorgnetwerktrento.be,Molenstraat 11 9220 Hamme,tick2495 YE2025 Strong official native NBB PDF deposit 2026-00304248 + Strong KBO 0455.449.048 Actief 2 VE; omzet70 JUMP 13434174 material not commercial-only; 73 JUMP 3051871; 76A empty; envelope omzet70 JUMP 13434174; pnl JUMP 362341; 9901 JUMP 331288; equity JUMP 13774142; assets DROP 19824343; debt DROP 6050201; FTE DROP 186.5; kapitaalsubsidies DROP 534830; destin691 JUMP 2300000; 791 empty; cash DROP 1921671; geldbeleggingen JUMP 5290614; leftover city_hamme WZC 2 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_trento_omzet_jr2025_statutory,{EID},2025,13434174,13434174,13434174,NBB VOL-VZW code 70 omzet YE2025 JUMP +5.99% (material not commercial-only),{SRC_PDF},strong,tick2495; PDF p7 native; YE2024 12674723",
f"bud_trento_73_jr2025_statutory,{EID},2025,3051871,3051871,3051871,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +8.48%,{SRC_PDF},strong,tick2495; PDF p7 native; YE2024 2813385; 733 3025798; 731 26074; FOI RIZIV/VL matrix behind omzet+73",
f"bud_trento_opbr_jr2025_statutory,{EID},2025,13434174,13434174,13434174,NBB VOL-VZW envelope omzet 70 YE2025 JUMP +5.99% (VZW because omzet material not commercial-only),{SRC_PDF},strong,tick2495; PDF p7 native; YE2024 12674723; 70/76A 17021630 JUMP; 76A empty",
f"bud_trento_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty (was 1000),{SRC_PDF},strong,tick2495; PDF p7 native; YE2024 1000",
f"bud_trento_pnl_jr2025_statutory,{EID},2025,362341,362341,362341,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +431% (was 68230),{SRC_PDF},strong,tick2495; PDF p8 native; YE2024 68230; bedrijfswinst 9901 331288 JUMP; destin691 JUMP 2300000",
f"bud_trento_bedrijfswinst_jr2025_statutory,{EID},2025,331288,331288,331288,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +1910% (was 16482),{SRC_PDF},strong,tick2495; PDF p7 native; YE2024 16482; 62 12989805 JUMP; 630 900836 DROP; 66A 1418 JUMP; 640/8 35371 JUMP; 635/9 empty; 631/4 10923 DROP",
f"bud_trento_equity_jr2025_statutory,{EID},2025,13774142,13774142,13774142,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +1.60%,{SRC_PDF},strong,tick2495; PDF p6 native; YE2024 13556686; kapitaalsubsidies 15 534830 DROP; overgedragen 14 4161237 DROP; fondsen 10 3119608 FLAT; bestemde fondsen 13 5958466 JUMP",
f"bud_trento_assets_jr2025_statutory,{EID},2025,19824343,19824343,19824343,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -1.57%,{SRC_PDF},strong,tick2495; PDF p5 native; YE2024 20140114; MVA 22/27 10414979 DROP; cash 1921671 DROP; geldbeleggingen 5290614 JUMP; aanbouw 27 50499 JUMP",
f"bud_trento_debt_jr2025_statutory,{EID},2025,6050201,6050201,6050201,NBB VOL-VZW code 17/49 schulden YE2025 DROP -8.10%,{SRC_PDF},strong,tick2495; PDF p6 native; YE2024 6583428; 17 2000699 DROP; 42/48 3275888 DROP",
f"bud_trento_cash_jr2025_statutory,{EID},2025,1921671,1921671,1921671,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -31.35%,{SRC_PDF},strong,tick2495; PDF p5 native; YE2024 2799148; geldbeleggingen 50/53 5290614 JUMP; capex 328573",
f"bud_trento_destin_jr2025_statutory,{EID},2025,2300000,2300000,2300000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was 68230; 791 empty; 13 JUMP 5958466),{SRC_PDF},strong,tick2495; PDF p9 native; YE2024 destin 68230; 791 empty; 14 DROP 4161237; fondsen 10 3119608 FLAT",
])
print("entities+budgets ok")
print("CORE1 DONE")

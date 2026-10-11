from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2497_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_pegode_jr2025_nbb_pdf_2497"
SRC_KBO="src_pegode_kbo_2497"
SRC_SBM="src_pegode_sbm_2497"
SRC_SITE="src_pegode_site_2497"
EID="vzw_pegode_kontich"
GAP="gap_pegode_kontich_vaph_matrix_70_76A_18_11m_omzet_commercial_73_jump_15_32m_pnl_jump_630k_cash_jump_1_50m_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT leftover city_niel (Niel is VE only; official KBO zetel Kontich since 06.05.2024); NOT leftover city_schilde (Schilde is VE only); NOT Iris 0419.665.154 remine leftover city_kontich parent sec_flanders; NOT De Dageraad 0412.607.613 remine leftover city_kontich maatwerk; NOT Vierklaver remine; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Pegode deposit 2026-00293740,http://cdn.staatsbladmonitor.be/2026pdf/2026-00293740.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2497; official native statutory PDF 1876188 bytes 47p VOL-VZW 25.0.13 m05-f; header 15.07.2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-15 08:34:54 UTC OpenPDF 1.3.26; CDN Last-Modified 31.07.2026; statutory pages native; CDN 2026-00293740 GET 200 1876188 MD5 714fe54c9910b5bde6f95d413af76e17; official NBB UUID bfc734e3-8023-11f1-9f93-f92d86268d1a; VOL-VZW 6.1 6.2.1-4 6.3.4 6.4.1 6.4.2 6.5.1 6.5.2 6.16 niet dienstig; prior-year identical not restated; commissaris Moore Audit BV / Tindemans Ellen; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Pegode 0420.281.501,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420281501,KBO Public Search FOD Economie,{DAY},official_register,tick2497; Actief; 19 VE leftover city_kontich (official zetel Antwerpsesteenweg 62 2550 Kontich since 06.05.2024; Niel is VE only); VZW since 14.01.1980; RSZ2025 87.202; FOI info@pegode.be; leftover mined city_kontich VAPH after leftover-type hunt; NOT leftover city_niel; NOT leftover city_schilde; NOT Iris remine",
f"{SRC_SBM},NBB Consult / SBM fiche Pegode 0420281501 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0420281501,NBB Consult / SBM,{DAY},official_register,tick2497; deposit-id 2026-00293740 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial UUID bfc734e3-8023-11f1-9f93-f92d86268d1a; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Pegode FOI contact leftover city_kontich VAPH,https://pegode.be/contact/,Pegode VZW leftover city_kontich VAPH 19 VE,{DAY},foi_contact,tick2497; FOI info@pegode.be; official KBO zetel Antwerpsesteenweg 62 2550 Kontich; website still prints old zetel Noeverseweg 34 2845 Niel; RSZ2025 87.202 VAPH; leftover mined city_kontich VAPH; NOT leftover city_niel; NOT leftover city_schilde; NOT Iris remine; NOT De Dageraad remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Pegode,ASBL Pegode,Pegode VZW (leftover city_kontich VAPH),parastatal,city_kontich,nl,https://pegode.be/,info@pegode.be,Antwerpsesteenweg 62 2550 Kontich,tick2497 YE2025 Strong official native NBB PDF deposit 2026-00293740 + Strong KBO 0420.281.501 Actief 19 VE; omzet70 JUMP 1914328 commercial-only vs large 73; 73 JUMP 15317093; 76A JUMP 741511; envelope 70/76A JUMP 18110069; pnl JUMP 629938; 9901 JUMP 610467; equity JUMP 4856573; assets JUMP 8551945; debt DROP 3480999; FTE JUMP 174.6; kapitaalsubsidies JUMP 285334; destin691 JUMP 370649; 791 DROP 92286; cash JUMP 1497839; geldbeleggingen DROP 1240218; leftover city_kontich VAPH 19 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_pegode_omzet_jr2025_statutory,{EID},2025,1914328,1914328,1914328,NBB VOL-VZW code 70 omzet YE2025 JUMP +7.99% (commercial-only vs large 73),{SRC_PDF},strong,tick2497; PDF p7 native; YE2024 1772665; 6.9 no category split",
f"bud_pegode_73_jr2025_statutory,{EID},2025,15317093,15317093,15317093,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +8.10%,{SRC_PDF},strong,tick2497; PDF p7 native; YE2024 14168896; 733 14997731; 731 219048; 732 100314; 730 empty; FOI VAPH/VL/PVB/RTH matrix behind omzet+73",
f"bud_pegode_opbr_jr2025_statutory,{EID},2025,18110069,18110069,18110069,NBB VOL-VZW envelope 70/76A bedrijfsopbrengsten YE2025 JUMP +9.04% (VZW because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2497; PDF p7 native; YE2024 16608499; omzet 1914328 commercial-only; 76A 741511",
f"bud_pegode_76A_jr2025_statutory,{EID},2025,741511,741511,741511,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +114.48%,{SRC_PDF},strong,tick2497; PDF p7 native; YE2024 345722",
f"bud_pegode_pnl_jr2025_statutory,{EID},2025,629938,629938,629938,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +521.19%,{SRC_PDF},strong,tick2497; PDF p8 native; YE2024 101408; bedrijfswinst 9901 610467 JUMP; destin691 JUMP 370649",
f"bud_pegode_bedrijfswinst_jr2025_statutory,{EID},2025,610467,610467,610467,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +1566.76%,{SRC_PDF},strong,tick2497; PDF p7 native; YE2024 36620; 62 14055244 JUMP; 630 441185 JUMP; 66A 10235 JUMP; 640/8 97415 DROP; 635/9 114297 FLIP; 631/4 empty",
f"bud_pegode_equity_jr2025_statutory,{EID},2025,4856573,4856573,4856573,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +15.03%,{SRC_PDF},strong,tick2497; PDF p6 native; YE2024 4221951; kapitaalsubsidies 15 285334 JUMP; overgedragen 14 1880102 JUMP; fondsen 10 1493063 FLAT; bestemde fondsen 13 1198073 JUMP",
f"bud_pegode_assets_jr2025_statutory,{EID},2025,8551945,8551945,8551945,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +2.18%,{SRC_PDF},strong,tick2497; PDF p5 native; YE2024 8369495; MVA 22/27 4436288 JUMP; cash 1497839 JUMP; geldbeleggingen 1240218 DROP; aanbouw 27 124098 JUMP",
f"bud_pegode_debt_jr2025_statutory,{EID},2025,3480999,3480999,3480999,NBB VOL-VZW code 17/49 schulden YE2025 DROP -14.00%,{SRC_PDF},strong,tick2497; PDF p6 native; YE2024 4047469; 17 98384 DROP; 42/48 3348891 JUMP",
f"bud_pegode_cash_jr2025_statutory,{EID},2025,1497839,1497839,1497839,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +92.27%,{SRC_PDF},strong,tick2497; PDF p5 native; YE2024 779025; geldbeleggingen 50/53 1240218 DROP; capex 739991",
f"bud_pegode_destin_jr2025_statutory,{EID},2025,370649,370649,370649,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +16.58% (791 DROP 92286; 13 JUMP 1198073),{SRC_PDF},strong,tick2497; PDF p9 native; YE2024 destin 317923; 791 92286 DROP; 14 JUMP 1880102; fondsen 10 1493063 FLAT",
])
print("entities+budgets ok")
print("CORE1 DONE")

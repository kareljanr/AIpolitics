from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2500_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_luifel_jr2025_nbb_pdf_2500"
SRC_KBO="src_luifel_kbo_2500"
SRC_SBM="src_luifel_sbm_2500"
SRC_SITE="src_luifel_site_2500"
EID="vzw_luifel_tielt"
GAP="gap_luifel_tielt_vaph_matrix_70_76A_1_78m_omzet_commercial_73_jump_1_71m_pnl_drop_20k_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Zonnewende 0735.627.214 remine leftover city_tielt WZC; NOT Mivalti 0416.406.548 remine leftover city_tielt VAPH parent sec_flanders; NOT De Harlekijntjes remine leftover city_tielt CIK; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 De Luifel deposit 2026-00245078,http://cdn.staatsbladmonitor.be/2026pdf/2026-00245078.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2500; official native statutory PDF 47497 bytes 12p VKT-VZW 26.0.15 m04-f; header 02.07.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-03 06:26:29 UTC OpenPDF 1.3.26; CDN Last-Modified 24.07.2026; all 12p native; CDN 2026-00245078 GET 200 47497 MD5 0fe4a9aa4df864a1c001c0439b93aa30; official NBB UUID b721bca2-7618-11f1-9454-415d1325b44c; VKT-VZW 6.1.1 6.1.3 6.2 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Luifel 0434.011.652,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0434011652,KBO Public Search FOD Economie,{DAY},official_register,tick2500; Actief; 2 VE leftover city_tielt (official zetel Tramstraat 42 8700 Tielt since 01.01.2025 technical address code; VE 2.155.776.597 De Luifel Tramstraat 42 since 28.08.2006; VE 2.360.459.762 De Luifel 2 Adolf Loosveldtstraat 9 since 28.03.2022); VZW since 24.09.1987; RSZ2025 88.104; FOI info@deluifel.be; leftover mined city_tielt VAPH after leftover-type hunt; NOT De Zonnewende remine; NOT Mivalti remine",
f"{SRC_SBM},NBB Consult / SBM fiche De Luifel 0434011652 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0434011652,NBB Consult / SBM,{DAY},official_register,tick2500; deposit-id 2026-00245078 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial UUID b721bca2-7618-11f1-9454-415d1325b44c; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},De Luifel FOI contact leftover city_tielt VAPH,https://www.deluifel.be/,De Luifel VZW leftover city_tielt VAPH 2 VE,{DAY},foi_contact,tick2500; FOI info@deluifel.be; official KBO zetel Tramstraat 42 8700 Tielt; VAPH begeleid wonen / RTH / PVB; RSZ2025 88.104; leftover mined city_tielt VAPH; NOT De Zonnewende remine; NOT Mivalti remine; NOT De Harlekijntjes remine; NOT leftover-via-VE",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},De Luifel,ASBL De Luifel,De Luifel VZW (leftover city_tielt VAPH),parastatal,city_tielt,nl,https://www.deluifel.be/,info@deluifel.be,Tramstraat 42 8700 Tielt,tick2500 YE2025 Strong official native NBB PDF deposit 2026-00245078 + Strong KBO 0434.011.652 Actief 2 VE; omzet70 JUMP 71267 commercial-only vs large 73; 73 JUMP 1711321; 76A empty; envelope 70/76A JUMP 1782588; pnl DROP 19557; 9901 DROP 26431; equity JUMP 683911; assets JUMP 1561492; debt DROP 877581; FTE JUMP 21.4; kapitaalsubsidies empty; destin691 empty; cash JUMP 535798; geldbeleggingen empty DROP; leftover city_tielt VAPH 2 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_luifel_omzet_jr2025_statutory,{EID},2025,71267,71267,71267,NBB VKT-VZW code 70 omzet YE2025 JUMP +11.02% (commercial-only vs large 73),{SRC_PDF},strong,tick2500; PDF p native; YE2024 64190",
f"bud_luifel_73_jr2025_statutory,{EID},2025,1711321,1711321,1711321,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +5.41%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 1623463; FOI VAPH/VL/PVB/RTH/gemeente matrix behind omzet+73",
f"bud_luifel_opbr_jr2025_statutory,{EID},2025,1782588,1782588,1782588,NBB VKT-VZW envelope 70/76A YE2025 JUMP +5.62% (VZW because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2500; PDF p native; YE2024 1687653; omzet70 71267 JUMP; 76A empty",
f"bud_luifel_bruto_jr2025_statutory,{EID},2025,1681424,1681424,1681424,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +7.01%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 1571265",
f"bud_luifel_pnl_jr2025_statutory,{EID},2025,19557,19557,19557,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -58.66%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 47313; bedrijfswinst 9901 26431 DROP; destin691 empty",
f"bud_luifel_bedrijfswinst_jr2025_statutory,{EID},2025,26431,26431,26431,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -77.09%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 115382; 62 1591291 JUMP; 630 53797 DROP; 640/8 5686 DROP; 635/9 empty; 631/4 4219 JUMP",
f"bud_luifel_equity_jr2025_statutory,{EID},2025,683911,683911,683911,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.94%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 664354; overgedragen 14 683911 JUMP; 10/13/15 empty",
f"bud_luifel_assets_jr2025_statutory,{EID},2025,1561492,1561492,1561492,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +0.81%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 1548971; MVA 22/27 1016412 DROP; cash 535798 JUMP; geldbeleggingen empty DROP; aanbouw 27 empty",
f"bud_luifel_debt_jr2025_statutory,{EID},2025,877581,877581,877581,NBB VKT-VZW code 17/49 schulden YE2025 DROP -0.80%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 884617",
f"bud_luifel_cash_jr2025_statutory,{EID},2025,535798,535798,535798,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +71.61%,{SRC_PDF},strong,tick2500; PDF p native; YE2024 312225; geldbeleggingen 50/53 empty DROP (was 200000); capex 44199",
f"bud_luifel_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty),{SRC_PDF},strong,tick2500; PDF p native; YE2024 destin empty; 791 empty",
])
print("entities+budgets ok")
print("CORE1 DONE")

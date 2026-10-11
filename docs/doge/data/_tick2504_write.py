from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2504_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hunnegem_jr2025_nbb_pdf_2504"
SRC_KBO="src_hunnegem_kbo_2504"
SRC_SBM="src_hunnegem_sbm_2504"
SRC_SITE="src_hunnegem_site_2504"
EID="vzw_hunnegem_herzele"
GAP="gap_hunnegem_herzele_wzc_matrix_bruto_2_39m_omzet73_empty_pnl_jump_148k_cash_drop_921k_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Heymeulen 0420.669.303 leftover city_buggenhout WZC still YE2024; NOT Avalon 0464.778.666 remine leftover city_buggenhout VAPH; NOT WZC Sint-Vincentius Erpe-Mere 0422.620.585 YE2024; NOT Meredal 0419.333.671 remine leftover city_erpe_mere WZC; NOT Avondzon Erpe 0419.044.057 remine leftover city_erpe_mere WZC; NOT CuraCare 0749.566.807 BV commercial; NOT leftover city_niel unused; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Hunnegem Herzele deposit 2026-00302624,http://cdn.staatsbladmonitor.be/2026pdf/2026-00302624.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2504; official native statutory PDF 291721 bytes 19p VKT-VZW 23.0.10 m04-f; header 16.07.2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-17 06:40:12 UTC OpenPDF 1.3.26; CDN Last-Modified 02.08.2026; statutory pages native; CDN 2026-00302624 GET 200 291721 MD5 b848dbf26d76e71466f3cf80595d73d7; official NBB UUID 3fe891ac-810d-11f1-8707-05421633f30a; VKT-VZW 6.2 6.3 6.5 7 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Hunnegem 0808.756.504,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0808756504,KBO Public Search FOD Economie,{DAY},official_register,tick2504; Actief; 2 VE leftover city_herzele (official zetel Lindestraat 33 9550 Herzele since 10.01.2025; VE 2.270.531.260 HUNNEGEM Lindestraat 33-35 9550 Herzele since 02.01.2018 + VE 2.263.977.525 HUNNEGEM Aaigemdorp 68 9420 Erpe-Mere since 10.05.2017); VZW since 13.12.2008; begindatum 30.12.2008; RSZ2025 87.301 Rusthuizen voor ouderen (ROB); FOI wzc.ocmwterleen@herzele.be municipal Ter Leen campus (NBB PDF email empty); leftover mined city_herzele WZC after Re-HEAD YE2024->YE2025; NOT De Heymeulen still YE2024; NOT Avalon remine; NOT leftover-via-VE",
f"{SRC_SBM},NBB Consult / SBM fiche Hunnegem 0808756504 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0808756504,NBB Consult / SBM,{DAY},official_register,tick2504; deposit-id 2026-00302624 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial UUID 3fe891ac-810d-11f1-8707-05421633f30a; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Hunnegem FOI contact leftover city_herzele WZC,https://publiek.departementzorg.be/Cobrha/Companies/Company/0808756504,CoBRHA / gemeente Herzele Ter Leen campus leftover city_herzele WZC 2 VE,{DAY},foi_contact,tick2504; FOI wzc.ocmwterleen@herzele.be municipal Ter Leen Lindestraat 35 (official NBB PDF email empty; same Lindestraat campus as Hunnegem zetel 33); CoBRHA inrichtende macht Hunnegem Actief 1 zorgvoorziening; official KBO zetel Lindestraat 33 9550 Herzele; RSZ2025 87.301; leftover mined city_herzele WZC; NOT De Heymeulen still YE2024; NOT Avalon remine; NOT leftover-via-VE",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Hunnegem,ASBL Hunnegem,Hunnegem VZW (leftover city_herzele WZC),parastatal,city_herzele,nl,https://publiek.departementzorg.be/Cobrha/Companies/Company/0808756504,wzc.ocmwterleen@herzele.be,Lindestraat 33 9550 Herzele,tick2504 YE2025 Strong official native NBB PDF deposit 2026-00302624 + Strong KBO 0808.756.504 Actief 2 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 2386211; pnl JUMP 147610; 9901 FLIP PROFIT 72121; equity JUMP 1780022; assets JUMP 2368480; debt JUMP 588458; FTE JUMP 35.3; kapitaalsubsidies empty; destin691 empty; cash DROP 491327; geldbeleggingen JUMP 1000000; leftover city_herzele WZC 2 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hunnegem_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT),{SRC_PDF},strong,tick2504; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 2386211 JUMP; FOI RIZIV/zorgkas/gemeente/eigen-bijdrage matrix behind bruto 2386211",
f"bud_hunnegem_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2504; PDF p5 native; YE2024 empty; FOI RIZIV/VL zorgkas matrix behind empty 73 vs material bruto",
f"bud_hunnegem_opbr_jr2025_statutory,{EID},2025,2386211,2386211,2386211,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +12.71% (VKT because 73 empty and bruto ≫ omzet),{SRC_PDF},strong,tick2504; PDF p5 native; YE2024 2117050; omzet70 empty; 73 empty; 76A empty; bruto9900 2386211 JUMP",
f"bud_hunnegem_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2504; PDF p5/p10 native; YE2024 empty; 76B 79454 JUMP non-recurrent financial",
f"bud_hunnegem_pnl_jr2025_statutory,{EID},2025,147610,147610,147610,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +1284.58%,{SRC_PDF},strong,tick2504; PDF p5 native; YE2024 10661; bedrijfswinst 9901 72121 FLIP PROFIT; destin691 empty",
f"bud_hunnegem_bedrijfswinst_jr2025_statutory,{EID},2025,72121,72121,72121,NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP PROFIT,{SRC_PDF},strong,tick2504; PDF p5 native; YE2024 -21551; 62 2268308 JUMP; 630 44463 JUMP; 66A empty; 640/8 1319 JUMP; 635/9 empty; 631/4 empty was 27764",
f"bud_hunnegem_equity_jr2025_statutory,{EID},2025,1780022,1780022,1780022,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +9.04%,{SRC_PDF},strong,tick2504; PDF p4 native; YE2024 1632412; kapitaalsubsidies 15 empty; overgedragen 14 1780022 JUMP; fondsen 10 empty; bestemde 13 empty",
f"bud_hunnegem_assets_jr2025_statutory,{EID},2025,2368480,2368480,2368480,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +16.46%,{SRC_PDF},strong,tick2504; PDF p3 native; YE2024 2033743; MVA 22/27 146421 DROP; cash 491327 DROP; geldbeleggingen 1000000 JUMP from empty; aanbouw 27 empty",
f"bud_hunnegem_debt_jr2025_statutory,{EID},2025,588458,588458,588458,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +46.63%,{SRC_PDF},strong,tick2504; PDF p4 native; YE2024 401331; 17 empty LT; 42/48 588458 JUMP; voorzieningen 16 empty",
f"bud_hunnegem_cash_jr2025_statutory,{EID},2025,491327,491327,491327,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -65.21%,{SRC_PDF},strong,tick2504; PDF p3 native; YE2024 1412310; geldbeleggingen 50/53 1000000 JUMP from empty; combined liquidity 1491327 JUMP; capex 8169 11872",
f"bud_hunnegem_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2504; PDF p6 native; YE2024 destin empty; 791 empty; overgedragen 14 1780022 JUMP; bestemde 13 empty",
])
print("entities+budgets ok")
print("CORE1 DONE")

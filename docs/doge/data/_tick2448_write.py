from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2448_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_peutertuinen_jr2025_nbb_pdf_2448"
SRC_KBO="src_peutertuinen_kbo_2448"
SRC_SBM="src_peutertuinen_sbm_2448"
SRC_SITE="src_peutertuinen_site_2448"
GAP="gap_peutertuinen_opgroeien_matrix_bruto_872k_omzet73_empty_pnl_jump_115k_destin_empty_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Peutertuinen GO Mariakerke deposit 2026-00288310,http://cdn.staatsbladmonitor.be/2026pdf/2026-00288310.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2448; official native PDF 53903 bytes 15p VKT-VZW 26.0.15 m04-f; header 10.07.2026; AV 10.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-31; CreationDate 2026-07-14 06:35:42 UTC OpenPDF 1.3.26; all 15p native; VKT-VZW 6.1.1 6.1.3 6.2 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Peutertuinen Gemeenschapsonderwijs Mariakerke 0410.221.116,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410221116,KBO Public Search FOD Economie,{DAY},official_register,tick2448; Actief; 2 VE; VZW since 26.03.1964; begindatum 26.03.1964; zetel Amand Casier de ter Bekenlaan 26 9030 Gent since 19.12.2005; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI info@peutertuin.be; leftover mined city_gent CIK; NOT Mini-creches GO Next 0896.468.060; NOT Stad Gent peutertuinen; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Peutertuinen GO Mariakerke 0410221116 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0410221116,NBB Consult,{DAY},official_register,tick2448; deposit-id 2026-00288310 YE 30/12/2025 filing 10/07/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Peutertuinen GO Mariakerke FOI contact leftover city_gent CIK,https://peutertuin.be,VZW Peutertuinen GO Mariakerke leftover city_gent CIK,{DAY},foi_contact,tick2448; FOI info@peutertuin.be; zetel Amand Casier de ter Bekenlaan 26 9030 Gent; leftover mined city_gent after Avida / WZC Sint-Coleta / Home Emmaus / Witje Wiebel / Beregoed / Windekind; 2 VE; NOT Kloosterstraat 6 Drongen; NOT Mini-creches GO Next Hasselt; NOT Stad Gent peutertuinen; NOT Villa Boempatat YE2024; NOT COB Annuntiaten remine; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")

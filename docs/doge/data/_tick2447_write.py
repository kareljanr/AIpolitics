from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2447_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_cobah_jr2025_nbb_pdf_2447"
SRC_KBO="src_cobah_kbo_2447"
SRC_SBM="src_cobah_sbm_2447"
SRC_SITE="src_cobah_site_2447"
GAP="gap_cobah_leuven_matrix_bruto_2_46m_omzet73_empty_pnl_drop_199k_destin_empty_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 COB Annuntiaten Heverlee deposit 2026-00216711,http://cdn.staatsbladmonitor.be/2026pdf/2026-00216711.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2447; official native PDF 50510 bytes 13p VKT-VZW 26.0.15 m04-f; header 29.06.2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-12; CreationDate 2026-06-30 00:46:39 UTC OpenPDF 1.3.26; all 13p native; VKT-VZW 6.1.1 6.1.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO COB Annuntiaten Heverlee 0447.017.570,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0447017570,KBO Public Search FOD Economie,{DAY},official_register,tick2447; Actief; 4 VE; VZW since 20.12.1991; begindatum 20.12.1991; zetel Naamsesteenweg 355 3001 Leuven since 20.12.1991; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI veerle.mertens@kdv.annuntiaten.be; leftover mined city_leuven CIK; NOT WZC Annuntiaten 0895.366.220; NOT Kinderkuren 0478.167.834; NOT Kinderdagverblijven Leuven 0413.321.255 absorbed; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche COB Annuntiaten Heverlee 0447017570 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0447017570,NBB Consult,{DAY},official_register,tick2447; deposit-id 2026-00216711 YE 30/12/2025 filing 29/06/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},COBAH FOI contact leftover city_leuven CIK,https://www.kinderopvangleuven.be/nl/opvanglocatie/11,VZW COBAH leftover city_leuven CIK,{DAY},foi_contact,tick2447; FOI veerle.mertens@kdv.annuntiaten.be; zetel Naamsesteenweg 355 3001 Heverlee; leftover mined city_leuven after Kinderkuren / Wigwam / t Anemoontje / IZW / Monte Rosa / De Wissel / De Slabbertjes; 4 VE; NOT Kloosterstraat 6 Drongen; NOT WZC Annuntiaten 0895.366.220; NOT Kinderkuren; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")

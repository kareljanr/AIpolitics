from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2435_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_izw_jr2025_nbb_pdf_2435"
SRC_KBO="src_izw_kbo_2435"
SRC_SBM="src_izw_sbm_2435"
SRC_SITE="src_izw_site_2435"
GAP="gap_izw_vaph_matrix_opbr_1_33m_omzet_530k_73_803k_pnl_drop_10k_destin_35k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 IZW deposit 2026-00262459,http://cdn.staatsbladmonitor.be/2026pdf/2026-00262459.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2435; official native PDF 51221 bytes 15p VKT-VZW 26.0.15 m04-f; header 07.07.2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-27; CreationDate 2026-07-07 18:38:31 UTC OpenPDF 1.3.26; all 15p native text euros; no commissaris; VKT-VZW 7 jaarverslag verkort n.v.t.; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO IZW 0430.278.439,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430278439,KBO Public Search FOD Economie,{DAY},official_register,tick2435; Actief; 3 VE 2.156.408.879 Riddersstraat 60 3000 Leuven since 04.10.2006 + 2.230.343.764 IZW Sint-Maartensdal 3000 Leuven since 01.01.2014 + 2.230.343.467 IZW Strombeek-Bever 1853 Grimbergen since 01.01.2014; naam INTEGRATIE EN ZELFSTANDIG WONEN VAN FYSIEK GEHANDICAPTE PERSONEN since 15.03.1985; afkorting I.Z.W. since 15.03.1985; VZW since 15.03.1985; begindatum 15.03.1985; zetel Riddersstraat 60 bus 02 3000 Leuven since 16.06.2004; RSZ2025 88.999; RSZ-werkgever since 01.12.1988; FOI info@izw.be; NOT Ferm Kinderopvang 0416.117.627; NOT Alvinnenberg 0434.390.150; NOT Hejmen 0426.383.987; NOT Staf 0431.333.660; NOT Grimbergen VAPH Zonnestraal; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche IZW 0430278439 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0430278439,NBB Consult,{DAY},official_register,tick2435; deposit-id 2026-00262459 YE 30/12/2025 filing 07/07/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},IZW FOI contact leftover city_leuven VAPH,https://izw.be/,VZW Integratie en Zelfstandig Wonen,{DAY},foi_contact,tick2435; FOI info@izw.be; tel 016 20 71 50; zetel Riddersstraat 60/02 3000 Leuven; leftover mined city_leuven after Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf / MFC Combo; 3 VE Leuven+Grimbergen same KBO; VAPH ADL; NOT Kloosterstraat 6 Drongen; NOT Ferm Kinderopvang; NOT Alvinnenberg; NOT Hejmen; NOT Staf; NOT Grimbergen VAPH Zonnestraal; NOT Helan; NOT Knuffelboom; NOT De Zeppelin",
])
print("sources ok")

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2391_stamp.txt").read_text().strip().splitlines()
EID = "vzw_de_schans"
SRC_PDF = "src_deschans_jr2025_nbb_pdf_2391"
COMM = "comm_deschans_jr2025_statutory_bruto_76k_73_51k_cash_jump_165k"
LB = "lb_deschans_bruto_76k_73_51k_cash_jump_165k_debt_821k_jr2025"
GAP = "gap_deschans_vl_property_matrix_bruto_76k_73_51k_cash_jump_165k_debt_821k_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

cash_json = (
    '"{""2025_omzet"":0,""2025_bruto9900"":76192,""2025_73"":51177,'
    '""2025_pnl"":12486,""2025_bedrijfswinst"":19901,""2025_equity"":529278,'
    '""2025_assets"":1350530,""2025_debt"":821252,""2025_fte"":0,'
    '""2025_kapitaalsubsidies"":15027,""2025_destin691"":0,""2025_cash"":165386,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":0,'
    '""2025_gebouwen22"":1114602,""2025_aanbouw27"":30559,'
    '""2025_capex"":18346,""2025_fondsen10"":364405,'
    '""2025_bestemde13"":0,""2025_overgedragen14"":149845,'
    '""2025_76A"":0,""2025_791"":0,""2025_vorderingen41"":1423,'
    '""2025_overige_lt_1789"":518960,""2025_reva_borg"":560000,'
    '""2024_omzet"":0,""2024_bruto9900"":82109,'
    '""2024_73"":51177,""2024_pnl"":17456,""2024_bedrijfswinst"":25980,'
    '""2024_equity"":517969,""2024_assets"":1247977,""2024_debt"":730008,'
    '""2024_kapitaalsubsidies"":16204,""2024_cash"":27567,""2024_fte"":0,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},De Schans vzw YE2025 (bruto DROP 76k / 73 51k / cash JUMP 165k / debt 821k / Strong PDF),{EID},Departement Zorg + leftover city_heusden_zolder + leftover city_beringen,VZW De Schans (KBO 0430.473.231; Actief; 0 VE; BTW2025 86.931+68.321),2026-06-29,2025,2025,76192,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00242881.pdf,Public Kohesi-family property dual of mined city_heusden_zolder + city_beringen,Publish VL/property matrix inside bruto 76k + 73 51k + cash JUMP 165k + debt 821k + gebouwen 1.11m + Harmoniestraat onverdeeldheid + REVA borg 560k,{SRC_PDF},strong,Vlaanderen>Limburg>Heusden-Zolder>DeSchans>JR2025_statutory_L5,tick2391; Strong official native PDF; leftover city_heusden_zolder + leftover city_beringen after LDSST@2390; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},De Schans bruto DROP 76k / 73 51k / cash JUMP 165k / debt 821k (YE2025 Heusden-Zolder),L5,property_vzw_statutory,Vlaanderen>Limburg>Heusden-Zolder>DeSchans>JR2025,76192,76192,PDF bruto DROP 76192 MIC envelope; omzet empty; 73 FLAT 51177; bedrijfswinst DROP 19901; pnl DROP 12486; equity JUMP 529278; assets JUMP 1350530; debt JUMP 821252; FTE empty 0 VE; kapitaalsubsidies DROP 15027; destin691 empty; cash JUMP 165386; geldbeleggingen empty; gebouwen 1114602; aanbouw 30559; capex 18346; overige LT 518960; REVA borg 560000,strong,{SRC_PDF},Kohesi family campuses Heusden-Zolder + Beringen,Departement Zorg + leftover city_heusden_zolder + leftover city_beringen,76k MIC bruto DROP 7pct; 73 51k FLAT; cash JUMP 6x to 165k; debt 821k; gebouwen 1.11m; leftover city_heusden_zolder,6.0,4.0,4.8,5.00,FOI VL/property matrix + bruto 76k + 73 51k + cash JUMP 165k + debt 821k + gebouwen 1.11m + Harmoniestraat onverdeeldheid + BTW-eenheid + REVA borg 560k,active,,tick2391; Strong official NBB native PDF + Strong KBO; leftover city_heusden_zolder + leftover city_beringen after LDSST@2390; OFF Drongen OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF LDSST OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Limburg>Heusden-Zolder>DeSchans>VL_property,{EID},VL/Zorg/VAPH/RIZIV split inside bruto 76192; why 73 51177 FLAT and omzet empty; why cash JUMP 165386 (was 27567) while debt JUMP 821252 and overige LT 518960; gebouwen 1114602 + Harmoniestraat 9 onverdeeldheid + REVA borg 560000; 0 VE no sociale balans; BTW-eenheid REVA/CGG/BW/LDSST,Strong official PDF leftover public Kohesi-family property of city_heusden_zolder + city_beringen; 76k bruto; public not private clinic; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not LDSST 0410.121.344,8,De Schans VZW / Erik Ottenbourgs voorzitter / Johan Gommers dagelijks bestuur,info@kohesi.be,"Pastoor Paquaylaan 123 bus 1, 3550 Heusden-Zolder",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2391; ready NOT sent; Strong official native NBB PDF; leftover city_heusden_zolder property after LDSST@2390; off Drongen off REVA Kohesi off CGG Kohesi off BW Kohesi off LDSST off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")

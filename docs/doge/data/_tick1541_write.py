#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1541 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvmw"
SRC = "src_hvmw_jr2025_bbc"
PDF = "https://zonemidwest.be/uploads/files/Zoneraad/Verslagen/2026/Zoneraad-op-vrijdag-27-maart-2026-Overzicht-beslissingen-website.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Hulpverleningszone Midwest official zoneraad JR2025 overzicht beslissingen,{PDF},HVZ Midwest,2026-08-20,budget,tick1541; official zoneraad 27.03.2026 Goedkeuring jaarrekening 2025; PDF 10p / 353741 bytes; pdfinfo created 28.03.2026 16:53:59 UTC Word 2019; legal basis Wet 15.05.2007 civiele veiligheid + KB 19.04.2014 boekhouding hulpverleningszones (as printed); euros PDF only; full rekening verslag + begrotingsrekening presentatie unpublished",
        "src_hvmw_kbo_0500929378,KBO ZONE MIDWEST 0500.929.378,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500929378,FPS Economy KBO,2026-08-20,official_register,tick1541; leftover IGS hulpverleningszone of mined Roeselare + leftover of Ardooie/Dentergem/Hooglede/Ingelmunster/Izegem/Lichtervelde/Moorslede/Oostrozebeke/Pittem/Staden/Tielt/Wingene; zetel Kwadestraat 159 8800 Roeselare; KBO 0500.929.378 Actief; prefix hvmw unused",
        "src_hvmw_site,HVZ Midwest official site (JR2025 zoneraad overzicht published),https://zonemidwest.be/,HVZ Midwest,2026-08-20,official_web,tick1541; leftover IGS of mined Roeselare; official zoneraad 27.03.2026 live on zonemidwest.be; full rekening verslag unpublished (inzage / FOI)",
        "src_hvmw_foi_contact,HVZ Midwest FOI channel (info@zonemidwest.be),https://zonemidwest.be/,HVZ Midwest,2026-08-20,official_web,tick1541; leftover IGS of mined Roeselare; FOI ready not sent; Kwadestraat 159 8800 Roeselare; official contact info@zonemidwest.be; NOT leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Fluvia / leftover DVV Midwest / leftover Thuiswest 1493 / leftover Motena Roeselare / leftover CGG Largo 1518",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvmw," in raw or raw.startswith(b"igs_hvmw,"):
        raise SystemExit("igs_hvmw already present")
    if b"0500.929.378" in raw or b"0500929378" in raw:
        raise SystemExit("HVZ Midwest KBO already present as entity")
    row = (
        "igs_hvmw,Hulpverleningszone Midwest / Brandweerzone Midwest / ZONE MIDWEST (leftover IGS hulpverleningszone of mined Roeselare + leftover of Ardooie/Dentergem/Hooglede/Ingelmunster/Izegem/Lichtervelde/Moorslede/Oostrozebeke/Pittem/Staden/Tielt/Wingene; NOT leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Waasland / leftover HVZ Fluvia / leftover Brandweerzone Centrum / leftover DVV Midwest / leftover Thuiswest 1493 / leftover Motena Roeselare / leftover CGG Largo 1518 / leftover CAW CWVL 1533),"
        "Zone de secours Midwest (IGS residuel / zone de secours),"
        "Hulpverleningszone Midwest leftover fire-rescue IGS of mined Roeselare + remaining Midwest municipalities (not leftover HVZ Meetjesland / leftover HVZ1 / leftover HVZ Fluvia / leftover DVV Midwest / leftover Thuiswest / leftover Motena / leftover CGG Largo / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_roeselare,nl,https://zonemidwest.be/,info@zonemidwest.be,Kwadestraat 159 8800 Roeselare,"
        "tick1541 leftover residual IGS hulpverleningszone of mined Roeselare after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 zoneraad overzicht taken; KBO 0500.929.378 Actief; zetel Roeselare 8800; live JR2025 official zoneraad 27.03.2026; sourced euros assets 20266035 expl 794672 pnl -257322 uitz -1051994 equity 18804221 debt 1461814 vastgelegd_gewone 14801789; FOI ready not sent; parent city_roeselare; prefix hvmw; NOT leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Fluvia / leftover CAW CWVL 1533 / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover DVV Midwest / leftover Thuiswest 1493"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvmw")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")

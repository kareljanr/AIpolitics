#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1538 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzt"
SRC = "src_hvzt_jr2025_bbc"
PDF = "https://www.hvztaxandria.be/storage/files/notulen-open-zitting-zr-25-maart-2026-1777898549.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Hulpverleningszone Taxandria official zoneraad JR2025 notulen,{PDF},HVZ Taxandria,2026-08-20,budget,tick1538; official zoneraad notulen open zitting 25.03.2026 besluit 2026_ZR_00053 Rekening 2025 Vaststelling; PDF 37p / 1268280 bytes; pdfinfo created 26.03.2026 13:26:32 UTC Aspose.PDF; legal basis Wet 15.05.2007 civiele veiligheid + KB 19.04.2017 boekhouding hulpverleningszones (as printed in notulen); euros PDF only; full rekening bijlagen unpublished",
        "src_hvzt_kbo_0500914928,KBO Hulpverleningszone Taxandria 0500.914.928,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500914928,FPS Economy KBO,2026-08-20,official_register,tick1538; leftover IGS hulpverleningszone of mined Turnhout + leftover of 11 other Taxandria municipalities; zetel Noord-Brabantlaan 68 2300 Turnhout; KBO 0500.914.928 Actief; prefix hvzt unused",
        "src_hvzt_site,HVZ Taxandria official site (JR2025 notulen published),https://www.hvztaxandria.be/,HVZ Taxandria,2026-08-20,official_web,tick1538; leftover IGS of mined Turnhout; official notulen open zitting 25.03.2026 live; full rekening bijlagen unpublished (inzage / FOI)",
        "src_hvzt_foi_contact,HVZ Taxandria FOI channel (info@hvztaxandria.be),https://www.hvztaxandria.be/index.php/contact,HVZ Taxandria,2026-08-20,official_web,tick1538; leftover IGS of mined Turnhout; FOI ready not sent; Noord-Brabantlaan 68 2300 Turnhout; official contact info@hvztaxandria.be; BTW BE 0500 914 928; NOT leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Kempen / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvzt," in raw or raw.startswith(b"igs_hvzt,"):
        raise SystemExit("igs_hvzt already present")
    if b"0500.914.928" in raw or b"0500914928" in raw:
        raise SystemExit("HVZ Taxandria KBO already present as entity")
    row = (
        "igs_hvzt,Hulpverleningszone Taxandria / HVZ Taxandria (leftover IGS hulpverleningszone of mined Turnhout + leftover of 11 other Taxandria municipalities Arendonk/Baarle-Hertog/Beerse/Hoogstraten/Kasterlee/Lille/Merksplas/Oud-Turnhout/Ravels/Rijkevorsel/Vosselaar; NOT leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Kempen / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover Welzijnszorg Kempen / leftover Woonboog 1478 / leftover De Noorderkempen / leftover Erfpunt 1536 / leftover IVAREM 1524),"
        "Zone de secours Taxandria (IGS residuel / zone de secours),"
        "Hulpverleningszone Taxandria leftover fire-rescue IGS of mined Turnhout + remaining Taxandria municipalities (not leftover HVZ Oost / leftover Brandweerzone Antwerpen / leftover HVZ Kempen / leftover CAW De Kempen / leftover CGG Kempen / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_turnhout,nl,https://www.hvztaxandria.be/,info@hvztaxandria.be,Noord-Brabantlaan 68 2300 Turnhout,"
        "tick1538 leftover residual IGS hulpverleningszone of mined Turnhout after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 notulen taken; KBO 0500.914.928 Actief; zetel Turnhout 2300; live JR2025 official zoneraad notulen 2026_ZR_00053 25.03.2026; sourced euros assets 15684701 expl 470131 pnl 758780 uitz 288649 equity 14871076 debt 813625 begroting_gewone 622750; FOI ready not sent; parent city_turnhout; prefix hvzt; NOT leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Kempen / leftover CAW De Kempen 1526 / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvzt")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")

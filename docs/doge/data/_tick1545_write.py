#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1545 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvnl"
SRC = "src_hvnl_jr2025_bbc"
PDF = "https://noord-limburg.hulpverleningszone.be/storage/hq2aZiMeCuVVjDBHkPdi4Ej61GUHrlw84ZTwjDeo.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},HVZ Noord-Limburg official jaarverslag 2025,{PDF},HVZ Noord-Limburg,2026-08-20,budget,tick1545; official jaarverslag 2025; PDF 27p / 715240 bytes; pdfinfo created 18.03.2026 11:52:07 UTC Microsoft Word 365; Financieel overzicht pages 25-27; euros PDF only; full zoneraad rekening 2025 unpublished",
        "src_hvnl_kbo_0500906812,KBO Hulpverleningszone Noord-Limburg 0500.906.812,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500906812,FPS Economy KBO,2026-08-20,official_register,tick1545; leftover IGS hulpverleningszone of mined Lommel + leftover of Bree/Peer/Bocholt/Pelt/Leopoldsburg and remaining Noord-Limburg gemeenten; zetel Norbert Neeckxlaan 52 bus Z 3920 Lommel; KBO 0500.906.812 Actief; prefix hvnl unused",
        "src_hvnl_site,HVZ Noord-Limburg official site (jaarverslag 2025 published),https://www.noord-limburg.hulpverleningszone.be/pagina/jaarverslag,HVZ Noord-Limburg,2026-08-20,official_web,tick1545; leftover IGS of mined Lommel; official JV2025 live on noord-limburg.hulpverleningszone.be; full rekening 2025 unpublished (inzage / FOI)",
        "src_hvnl_foi_contact,HVZ Noord-Limburg FOI channel (info@hvznl.be),https://www.noord-limburg.hulpverleningszone.be/pagina/openbaarheid-van-bestuur,HVZ Noord-Limburg,2026-08-20,official_web,tick1545; leftover IGS of mined Lommel; FOI ready not sent; Norbert Neeckxlaan 52 bus Z 3920 Lommel; official e-mail info@hvznl.be; NOT leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvnl," in raw or raw.startswith(b"igs_hvnl,"):
        raise SystemExit("igs_hvnl already present")
    if b"0500.906.812" in raw or b"0500906812" in raw:
        raise SystemExit("HVZ Noord-Limburg KBO already present as entity")
    row = (
        "igs_hvnl,Hulpverleningszone Noord-Limburg / HVZ Noord-Limburg (leftover IGS hulpverleningszone of mined Lommel + leftover of Bree/Peer/Bocholt/Pelt/Leopoldsburg and remaining Noord-Limburg gemeenten Bocholt Bree Hamont-Achel Hechtel-Eksel Leopoldsburg Lommel Pelt Peer; NOT leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Brandweerzone Rand / leftover HVZ Vlaams-Brabant West / leftover HVZ Fluvia),"
        "Zone de secours Noord-Limburg (IGS residuel / zone de secours),"
        "HVZ Noord-Limburg leftover fire-rescue IGS of mined Lommel + remaining Noord-Limburg municipalities (not leftover HVZ Oost-Limburg / leftover CAW Limburg / leftover CGG Integra / leftover CGG Kohesi / leftover Wonen in Limburg / leftover HVZ Westhoek),"
        "other,city_lommel,nl,https://www.noord-limburg.hulpverleningszone.be/,info@hvznl.be,Norbert Neeckxlaan 52 bus Z 3920 Lommel,"
        "tick1545 leftover residual IGS hulpverleningszone of mined Lommel after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JV2025 taken; KBO 0500.906.812 Actief; zetel Lommel 3920; live official jaarverslag 2025 27p 715240 created 18.03.2026; sourced euros uitgaven_gewone 13883486 pers 10572316 werking 2834534 prestaties 834402 werkingstoelagen 14309007 gemeente 8057000 federaal 6252007 invest 3784028; FOI ready not sent; parent city_lommel; prefix hvnl; NOT leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvnl")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")

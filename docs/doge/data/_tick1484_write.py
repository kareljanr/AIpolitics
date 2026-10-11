#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1484 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:50:00Z"
ENT = "wm_mpls"
SRC = "src_mpls_jr2025_nbb"
GAP = "gap_mpls_omzet_13_19m_pers_2_68m_debt_149m_l5"
LB = "lb_mpls_omzet_13_19m_pers_2_68m_debt_149m"
COMM = "comm_mpls_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117115.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},!Mpuls Menen-Wervik official NBB WVV VOL-kap JR2025,{PDF},NBB / !Mpuls Menen-Wervik,2026-08-19,primary_pdf,tick1484; leftover woonmaatschappij of mined Menen + Wervik; official NBB WVV VOL-kap JR2025 PDF 66p / 3536251 bytes; deposit 2026-00117115; AV 12.05.2026; header 13.05.2026; pdfinfo created 20.04.2026 09:16:30 UTC; model VOL-kap 26.0.11 m02-f-p; KBO 0405.501.174; assets 213864560 cash 9225512 debt 149309010 pers 2677490 omzet 13185888 pnl 1225909 equity 62364982",
        "src_mpls_site,!Mpuls Menen-Wervik official pages,https://www.wm-impuls.be,!Mpuls Menen-Wervik,2026-08-19,official_register,tick1484; leftover woonmaatschappij of mined Menen + Wervik; site + werkingsgebied Menen + Wervik; zetel Volkslaan 302 8930 Menen; KBO 0405.501.174",
        "src_kbo_mpls_0405501174,KBO !Mpuls Menen-Wervik 0405.501.174,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405501174,KBO,2026-08-19,official_register,tick1484; Actief since 01.01.1968; naam !MPULS MENEN-WERVIK since 15.11.2022; BV since 15.11.2022; zetel Volkslaan 302 8930 Menen since 29.06.2017; 1 VE; 16 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_mpls_foi_contact,!Mpuls Menen-Wervik FOI channel (info@wm-impuls.be),https://www.wm-impuls.be,!Mpuls Menen-Wervik,2026-08-19,official_register,tick1484; leftover woonmaatschappij of mined Menen + Wervik; FOI ready not sent; NOT leftover WoonST 1483 / leftover SW+ 1472 / leftover AGB Menen / leftover WZBW Wervik / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_mpls," in raw or raw.startswith(b"wm_mpls,"):
        raise SystemExit("wm_mpls already present")
    if b"0405.501.174" in raw or b"0405501174" in raw:
        raise SystemExit("!Mpuls KBO already present as entity")
    row = (
        "wm_mpls,!Mpuls Menen-Wervik (leftover woonmaatschappij / social-housing BV of mined Menen + leftover of mined Wervik; NOT leftover WoonST 1483 / leftover SW+ 1472 / leftover AGB Menen Woonbedrijf / leftover WZBW Wervik / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "!Mpuls Menen-Wervik SRL (logement social residuel Menin + Wervicq),"
        "!Mpuls leftover social-housing company of mined Menen + Wervik (not leftover WoonST / leftover SW+ / leftover AGB Menen / leftover WZBW Wervik / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_menen,nl,https://www.wm-impuls.be,info@wm-impuls.be,Volkslaan 302 bus 0201 8930 Menen,"
        "tick1484 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.501.174 Actief since 01.01.1968; live JR2025 official NBB WVV VOL-kap PDF; sourced euros assets 213864560 omzet 13185888 pers 2677490 33.4 VTE pnl 1225909 equity 62364982 cash 9225512 debt 149309010 capex 22387387 dividend 0; 1 VE; parent city_menen; werkingsgebied Menen + Wervik; prefix mpls"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_mpls")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")

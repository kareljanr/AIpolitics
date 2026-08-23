from pathlib import Path
import re

dst = Path("docs/doge/data/raw/tick2009")
for name in [
    "blasius_olv_nl",
    "blasius_olv",
    "blasius_fr",
    "blasius_kbo",
    "blasius_home",
    "blasius_site",
    "zorgkas_nl",
    "zorgkas_en",
]:
    for ext in [".html", ".pdf"]:
        p = dst / f"{name}{ext}"
        if not p.exists():
            continue
        print("FILE", p.name, p.stat().st_size)
        if ext == ".html":
            t = p.read_text(encoding="utf-8", errors="replace")
            title = re.search(r"<title>([^<]+)</title>", t)
            blocks = re.findall(
                r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
                t,
            )
            print(" title", title.group(1)[:130] if title else None)
            print(" blocks", blocks[:3])
            for lab in [
                "Last balance sheet year",
                "Laatste balansjaar",
                "filed on",
                "neergelegd op",
                "Activity",
                "Hospital",
            ]:
                i = t.find(lab)
                if i >= 0:
                    print(" ", lab, repr(t[i : i + 170]))
            em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
            print(" FTE", em[:2])
        print()

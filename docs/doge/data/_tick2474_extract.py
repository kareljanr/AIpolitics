from pathlib import Path
import subprocess, re
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2474")
pdf=OUT/"hupskadee-nbb-pdf2.pdf"
print(subprocess.check_output(["pdfinfo", str(pdf)], text=True, errors="replace"))
txt=subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True, errors="replace")
(OUT/"hupskadee-2026-00374083.txt").write_text(txt)
print("TEXT LEN", len(txt), "pages hint", txt.count("\f")+1)
print("==== FIRST 3500 ====")
print(txt[:3500])
print("==== PAGE BREAKS / YEAR ====")
for pat in ["01.01.2025","31.12.2025","01/01/2025","31/12/2025","01.01.2024","31.12.2024","boekjaar","HUPSKADEE","0863"]:
    print(pat, txt.find(pat))

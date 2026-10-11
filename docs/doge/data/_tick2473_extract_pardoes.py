from pathlib import Path
import subprocess, re
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")
pdf=OUT/"pardoes-cdn.pdf"
# pdfinfo
print(subprocess.check_output(["pdfinfo", str(pdf)], text=True, errors="replace"))
# extract text
txt=subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True, errors="replace")
(OUT/"pardoes-2026-00295237.txt").write_text(txt)
print("TEXT LEN", len(txt), "pages hint", txt.count("\f")+1)
print("==== FIRST 2500 ====")
print(txt[:2500])
print("==== MID (codes) ====")
# find key codes
for pat in ["9900","9901","9904","70 ","73 ","76A","76/A","691","791","10/15","20/58","17/49","54/58","22/27","9087","9086","FTE","brutomarge","omzet","subsid"]:
    print(pat, txt.lower().find(pat.lower()))

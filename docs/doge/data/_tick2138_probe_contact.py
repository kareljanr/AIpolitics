# -*- coding: utf-8 -*-
from pathlib import Path
import re

html = Path("docs/doge/data/raw/tick2138/prestige_cw_en.html").read_text(
    encoding="utf-8", errors="replace"
)
for pat in [
    r"[\w.+-]+@[\w.-]+\.\w+",
    r"phone[^<]{0,40}",
    r"tel[^<]{0,40}",
    r"Voie de Li[^<\"]{0,40}",
    r"Principal activity[^<]{0,100}",
    r"Company size[^<]{0,80}",
]:
    ms = re.findall(pat, html, re.I)
    if ms:
        print(pat, ms[:5])

# calc
b25, b24 = 3700707.5, 3142656  # FAQ said 3,700,707.50
# use integer from year block without decimals
b25, b24 = 3700707, 3142656
p25, p24 = 57786, -189310
e25, e24 = 277599, 219813
print("bruto yoy", f"{(b25-b24)/b24*100:+.2f}%")
print("pnl improve vs abs prior", f"{(p25-p24)/abs(p24)*100:+.2f}%")
print("equity yoy", f"{(e25-e24)/e24*100:+.2f}%")
print("equity/bruto", f"{e25/b25*100:.2f}%")

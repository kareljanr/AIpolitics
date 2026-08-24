from pathlib import Path

p = Path("docs/doge/data/raw/tick2278/write_tick2278.py")
t = p.read_text(encoding="utf-8")
fixes = [
    (
        "equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%",
        "equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%",
    ),
    (
        "equity **EUR{EQUITY}** DROP {EQUITY_PCT}%",
        "equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%",
    ),
    ("tick2277", "tick2278"),
    ("Vlaanderen>VlaamsBrabant>Eeklo", "Vlaanderen>OostVlaanderen>Eeklo"),
    ("Eeklots/debt Unknown", "Assets/debt Unknown"),
    ("equity DROP {EQUITY_PCT}%", "equity JUMP +{EQUITY_PCT}%"),
    (
        "2. Toelichting bij de overgang naar verlies EUR{PNL} (vs winst EUR{PNL24}, {PNL_PCT}%)\n"
        "   ondanks omzet EUR{OMZET} (+{OMZET_PCT}%) en brutomarge EUR{BRUTO} (~{RATIO}x omzet).",
        "2. Toelichting bij brutomarge EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}) en winstsprong\n"
        "   EUR{PNL} (+{PNL_PCT}% vs EUR{PNL24}) vs publieke maatwerk-loonsubsidies.",
    ),
    (
        "reconcile JUMP + bruto>~1.5x omzet vs maatwerk wage-subsidy matrix",
        "reconcile bruto>~1.6x omzet + pnl JUMP vs maatwerk wage-subsidy matrix",
    ),
    (
        "disclose maatwerk wage-subsidy matrix behind JUMP despite omzet JUMP",
        "disclose maatwerk wage-subsidy matrix behind bruto>~1.6x omzet",
    ),
    (
        "behind bruto>~1.6x omzet + FTE JUMP despite published retail omzet",
        "behind bruto>~1.6x omzet",
    ),
]
for a, b in fixes:
    n = t.count(a)
    t = t.replace(a, b)
    print(n, repr(a[:60]))
p.write_text(t, encoding="utf-8")
print("ok")

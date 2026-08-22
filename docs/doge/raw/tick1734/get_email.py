import urllib.request, ssl, re

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
for path in ["/contact", "/"]:
    u = "https://www.sint-jozef-rumst.be" + path
    req = urllib.request.Request(u, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        html = r.read().decode("utf-8", "replace")
    print("===", path, "len", len(html))
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
    print("emails", emails)
    for m in re.findall(r".{0,40}mailto.{0,80}", html, re.I)[:20]:
        print("mailto", m)
    for m in re.findall(r"cloak|email|@|addy|&#", html, re.I)[:30]:
        pass
    # Joomla email cloak: often &#... patterns or data-... 
    for m in re.findall(r"joomla[^\"']{0,40}mail[^\"']{0,80}", html, re.I)[:10]:
        print("jm", m)
    # look for encoded email components
    for m in re.findall(r"document\.write\([^)]{0,200}\)", html)[:10]:
        print("dw", m[:200])
    for m in re.findall(r"['\"][^'\"]*@[^'\"]*['\"]", html)[:20]:
        print("q", m)
    # numeric html entities near email
    ents = re.findall(r"(?:&#\d+;?){5,}", html)
    print("entity runs", len(ents))
    for e in ents[:10]:
        try:
            decoded = re.sub(r"&#(\d+);?", lambda m: chr(int(m.group(1))), e)
            if "@" in decoded or "sint" in decoded.lower():
                print("dec", decoded)
        except Exception:
            pass

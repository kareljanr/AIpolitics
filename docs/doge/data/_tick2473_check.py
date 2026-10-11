import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
ROOT = Path('/workspace/AIpolitics/docs/doge/data')

needles = ['0448.731.106', '0448731106', '448731106', 't sas', 't_sas', '0448.731']
hits = []
with open(ROOT / 'entities.csv', newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    print('entity cols', r.fieldnames)
    for row in r:
        blob = ' '.join((row.get(k) or '') for k in row).lower()
        for n in needles:
            if n.lower() in blob:
                hits.append({k: (row.get(k) or '')[:140] for k in list(row.keys())[:14]})
                break
print('entity hits', len(hits))
for h in hits:
    print(h)

print('--- denderleeuw ---')
with open(ROOT / 'entities.csv', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        eid = row.get('entity_id') or ''
        name = row.get('name') or row.get('legal_name') or ''
        blob = ' '.join((row.get(k) or '') for k in row).lower()
        if 'denderleeuw' in blob:
            print(eid, '|', name[:90])
            print('  ', {k: (row.get(k) or '')[:100] for k in list(row.keys())[:12]})

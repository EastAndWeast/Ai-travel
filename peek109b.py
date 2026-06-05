import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
# Find Day 109 section
m = re.search(r'<!--\s*第?109天?\s*-->.*?<!--\s*第?108天?\s*-->', content, re.DOTALL)
if m:
    text = m.group(0)
    print('=== Day 109 (raw, first 4000 chars) ===')
    print(text[:4000])
    print()
    print('=== Total length of Day 109 entry ===')
    print(len(text))
else:
    print('not found')

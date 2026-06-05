import re
content = open('index.html', 'r', encoding='utf-8').read()
# Try various date patterns
patterns = [
    r'journey-date">([^<]+)<',
    r'journey-title">第(\d+)天',
    r'第(\d+)天[^<]*2026-(\d\d)-(\d\d)',
]
for p in patterns:
    matches = re.findall(p, content)
    print(f'Pattern: {p[:50]}')
    print(f'  Found: {len(matches)} matches')
    if matches:
        print(f'  First 3: {matches[:3]}')
        print(f'  Last 3: {matches[-3:]}')
    print()

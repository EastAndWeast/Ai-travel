# -*- coding: utf-8 -*-
import re
content = open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8').read()

# Find all day markers with their positions
markers = [(int(m.group(1)), m.start()) for m in re.finditer(r'第(\d+)天-->', content)]
markers.sort(key=lambda x: x[0])
print('Top 5 days by position:')
for d, p in markers[-5:]:
    # Get the date from the journey-date div
    date_match = re.search(r'<div class="journey-date">([^<]+)</div>', content[p:p+500])
    date = date_match.group(1) if date_match else '???'
    print(f'  Day {d} @ pos {p}: {date}')

# Check ordering - is the list ordered ascending or descending by day?
# If newest is at top, ascending
print('\nDays in order of appearance:')
for d, p in sorted(markers, key=lambda x: x[1])[-5:]:
    print(f'  Day {d} @ pos {p}')

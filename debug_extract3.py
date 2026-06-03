import re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

day_pattern = re.compile(r'<!--\s*第(\d+)天\s*-->')
day_comments = list(day_pattern.finditer(html_content))

by_day = {}
for m in day_comments:
    n = int(m.group(1))
    if n not in by_day:
        by_day[n] = []
    by_day[n].append(m)

max_day_num = max(by_day.keys())
last_day = by_day[max_day_num][0]
last_day_num = str(max_day_num)
print(f'Max day: {last_day_num}, at pos: {last_day.start()}')

after_last_day = html_content[last_day.start():]
end_pattern = re.compile(r'<!--\s*第\d+天\s*-->|<footer>')
end_m = end_pattern.search(after_last_day)
if end_m:
    item_text = after_last_day[:end_m.start()]
else:
    item_text = after_last_day

print(f'Item text length: {len(item_text)}')
print('First 500:', item_text[:500])
print('---')
print('Last 300:', item_text[-300:])

# Find title
title_m = re.search(r'<div class="journey-title">([^<]+)</div>', item_text)
print(f'\nTitle match: {title_m}')
if title_m:
    print(f'Title: {title_m.group(1)}')

# Find date
date_m = re.search(r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>', item_text)
print(f'Date match: {date_m}')
if date_m:
    print(f'Date: {date_m.group(1)}')

# Find content
content_start = item_text.find('<div class="journey-content">')
print(f'\nContent start: {content_start}')

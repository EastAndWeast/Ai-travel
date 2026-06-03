# -*- coding: utf-8 -*-
import re

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

days = re.findall(r'第(\d+)天', content)
print(f'Total days found: {len(days)}')
print(f'Day range: {min(days)} - {max(days)}')
print(f'Last 5 days: {days[-5:]}')

day106 = re.search(r'第106天', content)
if day106:
    print('\n✅ Day 106 found!')
    start = day106.start() - 100
    end = min(len(content), day106.end() + 300)
    snippet = content[start:end]
    print(snippet[:500])
else:
    print('\n❌ Day 106 NOT FOUND!')
    print('Last days:', re.findall(r'第(\d+)天', content)[-5:])
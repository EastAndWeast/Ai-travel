# -*- coding: utf-8 -*-
import re
with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
dates = re.findall(r'journey-date">(\d{4}-\d{2}-\d{2})', content)
print('Latest 3 dates:', dates[:3])
days = re.findall(r'第(\d+)天', content)
unique_days = sorted(set(int(d) for d in days))
print('All days count:', len(unique_days))
print('Last 5 days:', unique_days[-5:])
if '第103天' in content:
    print('Day 103 entry: FOUND')
else:
    print('Day 103 entry: NOT FOUND')
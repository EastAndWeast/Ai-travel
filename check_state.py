# -*- coding: utf-8 -*-
import re

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

days = re.findall(r'第(\d+)天', content)
unique_days = sorted(set(int(d) for d in days))
print('Days found (last 10):', unique_days[-10:])

matches = re.findall(r'journey-date">(\d{4}-\d{2}-\d{2})', content)
print('Dates:', matches[:5] if matches else 'none')
print('Total entries:', len(matches))
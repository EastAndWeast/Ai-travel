# -*- coding: utf-8 -*-
import re

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Get the latest entry
dates = re.findall(r'journey-date">(\d{4}-\d{2}-\d{2})', content)
print('Latest dates:', dates[:3])

# Check Day 102 entry
if '第102天' in content:
    print('Day 102 entry: FOUND')
    idx = content.find('第102天')
    print(content[idx:idx+200])
else:
    print('Day 102 entry: NOT FOUND')

days = re.findall(r'第(\d+)天', content)
unique_days = sorted(set(int(d) for d in days))
print('All days (last 5):', unique_days[-5:])
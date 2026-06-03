# -*- coding: utf-8 -*-
import re

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Day 77 content
match = re.search(r'第77天内容.*?(?=<!-- |\Z)', content, re.DOTALL)
if match:
    text = match.group()
    news_count = text.count('news-title')
    print(f'Day 77 has {news_count} news items')
    dates = re.findall(r'<div class="journey-date">(.*?)</div>', text)
    print(f'Date: {dates}')
    
    # Show first 300 chars
    print('\nFirst 300 chars:')
    print(text[:300].encode('utf-8'))
else:
    print('Day 77 not found')
    
# Check subtitle
sub_match = re.search(r'<p class="subtitle">(.*?)</p>', content)
if sub_match:
    print(f'\nSubtitle: {sub_match.group(1)}')
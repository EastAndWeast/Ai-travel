# -*- coding: utf-8 -*-
import re, codecs, sys, os, urllib.request, urllib.parse, json, datetime

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'
NEWS_JSON_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/news_day99.json'

# Check current state
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 97
print(f'Current max AI day: {current_day}')

with open(NEWS_JSON_PATH, 'r', encoding='utf-8') as f:
    news_data = json.load(f)

print(f'News items in day99: {len(news_data)}')

for item in news_data:
    query = item.get('query', 'unknown')
    titles = item.get('titles', [])
    print(f'Query: {query}')
    print(f'Titles count: {len(titles)}')
    for t in titles[:3]:
        print(f'  - {t}')

# Today's date
today = datetime.date.today()
print(f'Today: {today}')
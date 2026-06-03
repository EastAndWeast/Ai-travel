# -*- coding: utf-8 -*-
import re, codecs, sys, urllib.request, urllib.parse, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('AI人工智能最新进展 2026年5月30日', 'AI新闻'),
    ('OpenAI Google GPT Claude Qwen 最新 2026', '大模型更新'),
    ('AI terminal research benchmark 2026', '研究进展'),
]

news_items = []
for query, name in queries:
    try:
        encoded_query = urllib.parse.quote(query)
        url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        snippets = re.findall(r'<a class="result__snippet"[^>]*>([^<]*)</a>', html)
        print(f'=== {name} ({len(titles)} results) ===')
        for i, t in enumerate(titles[:8]):
            print(f'  {i+1}. {t.strip()}')
        if snippets:
            for i, s in enumerate(snippets[:5]):
                print(f'     > {s.strip()[:120]}')
        news_items.append({
            'query': query,
            'titles': [t.strip() for t in titles[:8]],
            'snippets': [s.strip() for s in snippets[:8]]
        })
    except Exception as e:
        print(f'Error fetching {name}: {e}')

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/news_day105.json', 'w', encoding='utf-8') as f:
    json.dump(news_items, f, ensure_ascii=False, indent=2)
print('\nNews saved.')
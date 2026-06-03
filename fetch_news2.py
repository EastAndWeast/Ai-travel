# -*- coding: utf-8 -*-
import re, codecs, sys, urllib.request, urllib.parse, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Try different search approaches
urls = [
    ('https://html.duckduckgo.com/html/?q=AI+news+May+2026', 'DuckDuckGo EN'),
    ('https://html.duckduckgo.com/html/?q=人工智能+2026+最新', 'DuckDuckGo CN'),
]

for url, name in urls:
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        snippets = re.findall(r'<a class="result__snippet"[^>]*>([^<]*)</a>', html)
        print(f'\n=== {name} ({len(titles)} results) ===')
        for i, t in enumerate(titles[:10]):
            print(f'  {i+1}. {t.strip()}')
    except Exception as e:
        print(f'Error with {name}: {e}')

# Try Brave search API style URL
try:
    url = 'https://search.brave.com/search?q=AI+news+May+2026&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=15)
    content = response.read().decode('utf-8')
    print(f'\n=== Brave ({len(content)} chars) ===')
    print(content[:500])
except Exception as e:
    print(f'Brave error: {e}')
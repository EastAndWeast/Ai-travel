# -*- coding: utf-8 -*-
import re

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find day 105
match = re.search(r'(<!-- 第105天 -->.*?</div>\s*</div>\s*<!-- 第106天)', content, re.DOTALL)
if not match:
    # Try another pattern - check if day 105 exists
    day105 = re.search(r'第105天', content)
    if day105:
        start = max(0, day105.start() - 200)
        end = min(len(content), day105.end() + 800)
        snippet = content[start:end]
        # Find the closing </div> for journey-item
        item_end = snippet.find('</div>\n\n\n            <!--')
        if item_end > 0:
            print(repr(snippet[:item_end+20]))
        else:
            print('Found day 105, but structure different')
            print(repr(snippet[:500]))
    else:
        print('Day 105 NOT FOUND!')
        print('Last 10 days found:', re.findall(r'第(\d+)天', content)[-10:])
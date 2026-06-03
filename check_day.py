# -*- coding: utf-8 -*-
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
# Find Day 108 block
idx = content.find('<!-- 第108天')
if idx >= 0:
    end_search = content.find('<footer>', idx)
    if end_search < 0:
        end_search = len(content)
    # Walk back to find closing </div> at right depth
    print(content[idx:end_search][:5000])

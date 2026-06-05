# -*- coding: utf-8 -*-
import sys
content = open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8').read()
idx = content.find('第109天')
print('Pos:', idx)
if idx > 0:
    sys.stdout.reconfigure(encoding='utf-8')
    sample = content[idx:idx+600]
    print(sample)

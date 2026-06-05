# -*- coding: utf-8 -*-
content = open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8').read()
# Find first 109 entry
idx = content.find('第109天-->')
end_idx = content.find('第108天', idx)  # Next previous day marker (109 inserted before 108)
print('109 pos:', idx, '108 pos:', end_idx)
print('Length of 109 block:', end_idx - idx if end_idx > 0 else 'NA')
print('---')
print(content[idx-50:end_idx][:100])

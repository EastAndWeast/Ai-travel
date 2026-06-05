# -*- coding: utf-8 -*-
content = open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8').read()
# Get the surrounding context for inserting before Day 109
idx = content.find('<!-- 第109天-->')
print(content[max(0, idx-300):idx+50])

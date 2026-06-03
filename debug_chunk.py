with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
import sys
sys.stdout.reconfigure(encoding='utf-8')
# Look at content around Day 109
print('=== Around 419600-420400 ===')
print(html[419600:420400])

# -*- coding: utf-8 -*-
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
# Find Day 109 block
m = re.search(r'<!--\s*第109天\s*-->', content)
if m:
    print(f"Day 109 comment found at position: {m.start()}")
    # Find Day 108 (should come after Day 109)
    m108 = re.search(r'<!--\s*第108天\s*-->', content)
    if m108:
        print(f"Day 108 comment at position: {m108.start()}")
        if m.start() < m108.start():
            print("✅ Day 109 comes BEFORE Day 108 (correct order)")
        else:
            print("❌ Day 109 comes AFTER Day 108 (wrong order)")
    # Show Day 109 content (first 1500 chars)
    end = content.find('<!--', m.start() + 1)
    if end < 0:
        end = m.start() + 3000
    print("\n=== Day 109 preview ===")
    print(content[m.start():m.start()+1500])
else:
    print("❌ Day 109 not found!")

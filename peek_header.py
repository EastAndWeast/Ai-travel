import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find header section
# Look for the stats display
m = re.search(r'<div class="stats">.*?</div>', content, re.DOTALL)
if m:
    print('=== Stats section ===')
    print(m.group(0)[:2000])

# Find "第X天" anywhere in header
print('\n=== Day counters in header ===')
for m in re.finditer(r'(总.{0,3}天数|统计|已完成|记录|第.{0,2}天)[^<>]{0,30}', content[:10000]):
    print(f'  {m.group(0)[:80]}')

import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all comment markers
markers = re.findall(r'<!--[^>]*第\d+天[^>]*-->', content[:5000])
print('前5000字符里的所有 day 注释:')
for m in markers:
    print(f'  {m}')

# Check raw bytes around Day 111
pos = content.find('第111天')
print(f'\n第111天 in content: pos={pos}')

# Check Day 109 raw text
pos109 = content.find('第109天')
print(f'第109天 in content: pos={pos109}')

# Check if Day 111 is BEFORE Day 109
pos111 = content.find('第111天')
pos109 = content.find('第109天')
print(f'第111天位置: {pos111}')
print(f'第109天位置: {pos109}')
if pos111 != -1 and pos109 != -1:
    print(f'111 在 109 之前: {pos111 < pos109}')

# Print snippet around insert point
print('\n=== Day 111 段前 200 字符 ===')
print(content[pos111-50:pos111+200])

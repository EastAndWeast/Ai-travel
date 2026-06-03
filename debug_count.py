import re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Use a simpler pattern - match 第N天 (with various unicode)
# The chars in encoded form: 绗 (U+7B2C) = 第; 澶 (U+5929) = 天
# Let me try ASCII only
pattern = re.compile(r'<!--\s*第(\d+)天\s*-->')
matches = list(pattern.finditer(html))
print(f'Pattern 1 total: {len(matches)}')

# Another pattern with encoded form
pattern2 = re.compile(r'<!--\s*绗€(\d+)澶╘?-->')
matches2 = list(pattern2.finditer(html))
print(f'Pattern 2 total: {len(matches2)}')

# Print all matched days
all_days = set()
for m in matches:
    all_days.add(int(m.group(1)))
for m in matches2:
    all_days.add(int(m.group(1)))
print(f'Unique days: {sorted(all_days)}')

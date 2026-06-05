import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find hero/header section
m = re.search(r'<section class="hero">.*?</section>', content, re.DOTALL)
if m:
    print('=== Hero section ===')
    print(m.group(0)[:3000])
else:
    print('Hero section not found, trying other patterns')
    # Try header
    m = re.search(r'<header>.*?</header>', content, re.DOTALL)
    if m:
        print('=== Header section ===')
        print(m.group(0)[:3000])
    # Look for stat numbers like 109 / 105 / 15200
    print('\n=== Search for stat numbers ===')
    for m in re.finditer(r'(109|110|111|108|107|dayCount|kmCount|locationCount|15200|101|100|99|98)', content[:15000]):
        print(f'  pos={m.start()}: {m.group(0)}')

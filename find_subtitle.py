import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find subtitle
m = re.search(r'<p class="subtitle">([^<]+)</p>', content)
if m:
    print(f'Subtitle: {m.group(1)}')
    # Replace with Day 111
    new_subtitle = m.group(1).replace('第7天', '第111天')
    # But better - find the number and replace it
    new_subtitle = re.sub(r'第(\d+)天', '第111天', m.group(1))
    print(f'New subtitle: {new_subtitle}')
else:
    print('Subtitle not found')

# Look for any "第X天" in the header (before main content)
header_end = content.find('</header>')
if header_end > 0:
    print(f'\n=== Header (first {header_end} chars) ===')
    print(content[:header_end+20])

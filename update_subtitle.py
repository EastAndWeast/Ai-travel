import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find subtitle
old_subtitle = re.search(r'<p class="subtitle">第(\d+)天[^<]*</p>', content)
if old_subtitle:
    print(f'Old subtitle: {old_subtitle.group(0)}')
    new_subtitle_str = old_subtitle.group(0).replace(f'第{old_subtitle.group(1)}天', '第111天')
    print(f'New subtitle: {new_subtitle_str}')
    # Apply
    new_content = content.replace(old_subtitle.group(0), new_subtitle_str)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('✅ Subtitle updated to Day 111')
    
    # Verify
    with open('index.html', 'r', encoding='utf-8') as f:
        verify = f.read()
    m2 = re.search(r'<p class="subtitle">([^<]+)</p>', verify)
    if m2:
        print(f'Confirmed: {m2.group(1)}')
else:
    print('Subtitle not found, no update')

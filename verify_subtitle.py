import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<p class="subtitle">([^<]+)</p>', content)
if m:
    print('Current subtitle:', m.group(1))
else:
    print('No subtitle found')

# Check file length
print('File length:', len(content))

import re
with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
pattern = re.compile(r'<!--\s*第(\d+)天\s*-->')
matches = list(pattern.finditer(html))
print(f'Total day comments matched: {len(matches)}')
for m in matches:
    print(f'  Day {m.group(1)} at pos {m.start()}')
if matches:
    last = matches[-1]
    print(f'Last day: {last.group(1)}')
    after = html[last.start():]
    close_m = re.search(r'</div>\n+\s*<footer>', after)
    if close_m:
        item = after[:close_m.end()]
        print(f'Item length: {len(item)}')
        content_m = re.search(r'<div class="journey-content">(.*?)</div>\s*$', item, re.DOTALL)
        if content_m:
            print(f'Content found, length: {len(content_m.group(1))}')
        else:
            print('No content match')
            print('Item end:', repr(item[-300:]))
    else:
        print('No close pattern')

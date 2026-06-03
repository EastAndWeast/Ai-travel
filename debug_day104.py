import re
content = open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8').read()

day_comments = list(re.finditer(r'<!-- 第(\d+)天 -->', content))
last_pos = day_comments[-1].start()

after = content[last_pos:]

# Find the closing </div> that closes journey-item (followed by newlines and <footer>)
# Pattern: </div>\n\n\n            <footer>
close_pat = re.compile(r'</div>(\n\s*)+<footer>')
m = close_pat.search(after)
if m:
    end_pos = m.start()
    item_text = after[:end_pos + 6]  # include the </div>
    with open('C:/Users/admin/.openclaw/workspace/Ai-travel/item_text.txt', 'w', encoding='utf-8') as f:
        f.write(f"Item length: {len(item_text)}\n\n")
        f.write(item_text)
    print(f"Success! Item text length: {len(item_text)}")
else:
    # Try simpler: just find the second </div> after journey-content start
    start_m = re.search(r'<div class="journey-content">', after)
    if start_m:
        search = after[start_m.end():]
        divs = [d.start() for d in re.finditer(r'</div>', search)]
        print(f"First 10 </div> positions after journey-content: {divs[:10]}")
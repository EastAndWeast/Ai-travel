import re
with open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Better approach: find the highest day number
pattern = re.compile(r'<!--\s*第(\d+)天\s*-->')
matches = list(pattern.finditer(html))
print(f'Total matched: {len(matches)}')

# Group by day number (in case of duplicates)
day_to_last = {}
for m in matches:
    day_num = int(m.group(1))
    if day_num not in day_to_last:
        day_to_last[day_num] = []
    day_to_last[day_num].append(m.start())

# Find max day
max_day = max(day_to_last.keys())
positions = day_to_last[max_day]
print(f'Max day: {max_day}, positions: {positions}')

# Use the FIRST occurrence of max day (since newer days are inserted before older)
target_pos = positions[0]
# Find the END of this day block (until next day comment or footer)
after = html[target_pos:]

# Find the next day comment or footer
end_m = re.search(r'<!--\s*第\d+天\s*-->|<footer>', after)
if end_m:
    item = after[:end_m.start()]
else:
    item = after

print(f'Item length: {len(item)}')
print(f'Item first 300: {item[:300]}')
print(f'Item last 200: {item[-200:]}')

# Extract content with proper regex - find the inner content div
# Use lazy matching with nested div counting
content_start = item.find('<div class="journey-content">')
if content_start >= 0:
    print('Content start found')
    # Find the matching close - count divs
    # The journey-content is nested inside journey-item
    # We want everything from content_start until the journey-content's matching </div>
    # Since it's nested, find the LAST </div> in the journey-item structure
    # But journey-content contains many </div> too. 
    # Strategy: find the journey-content div, then find the closing </div> for it
    # The content goes until just before </div>\n            </div>\n\n    which closes journey-content then journey-item
    
    # Look for the closing pattern of the item: ends with </div> closing journey-content, then </div> closing journey-item
    # Pattern: at the end, journey-content close is just before "\n            </div>" (the journey-item close)
    # Let me search backwards from the end of item
    end_content = item.rfind('</div>')
    # Walk back to find the matching opening <div class="journey-content">
    if end_content > content_start:
        raw_content = item[content_start + len('<div class="journey-content">'):end_content]
        print(f'Raw content length: {len(raw_content)}')
        print(f'Raw content first 200: {raw_content[:200]}')

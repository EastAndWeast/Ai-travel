import re
content = open('C:/Users/admin/.openclaw/workspace/Ai-travel/index.html', 'r', encoding='utf-8').read()
dates = re.findall(r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>', content)
days = re.findall(r'第(\d+)天', content)
print(f"Total dates: {len(dates)}, Total day mentions: {len(days)}")
print(f"Last 5 dates: {dates[-5:]}")
print(f"Last 5 days: {days[-5:]}")
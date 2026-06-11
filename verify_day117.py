# -*- coding: utf-8 -*-
"""验证 Day117 添加结果"""
import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 验证 Day 注释 markers
days = re.findall(r'<!--\s*第(\d+)天\s*-->', content)
print('=== Day markers ===')
day_ints = sorted(set([int(d) for d in days]))
print(f'All day markers: {day_ints}')
print(f'Max day: {max(day_ints)}')
print()

# 2. 验证 Day 117 标题
m = re.search(r'<div class="journey-title">第117天[^<]+</div>', content)
if m:
    print('=== [OK] Day117 标题 ===')
    print(f'  {m.group(0)[:200]}...')
else:
    print('=== [FAIL] 未找到 Day117 标题')
print()

# 3. 验证 Day 117 日期
dm = re.search(r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div><div class="journey-title">第117天', content)
if dm:
    print(f'=== [OK] Day117 日期: {dm.group(1)} ===')
else:
    print('=== [FAIL] Day117 日期未找到')
print()

# 4. 验证 subtitle
sm = re.search(r'<p class="subtitle">第(\d+)天[^<]+</p>', content)
if sm:
    print(f'=== [OK] Subtitle: {sm.group(0)} ===')
else:
    print('=== [FAIL] 未找到 Subtitle')
print()

# 5. 验证 Day 116 仍然存在
m116 = re.search(r'<!--\s*第116天\s*-->', content)
print(f'=== [{"OK" if m116 else "FAIL"}] Day116 注释仍存在 ===')
print()

# 6. 验证位置 (Day117 应该在 Day116 之前)
m117 = re.search(r'<!--\s*第117天\s*-->', content)
if m117 and m116:
    print(f'=== Position check ===')
    print(f'Day117 at {m117.start()}, Day116 at {m116.start()}')
    print(f'Day117 - Day116 = {m117.start() - m116.start()} (should be negative)')
    if m117.start() < m116.start():
        print('[OK] Day117 is BEFORE Day116 (correct, Day117 is newer)')
    else:
        print('[FAIL] Day117 is AFTER Day116 (wrong!)')
print()

# 7. Day117 卡片内的 news-item 数
day117_section_match = re.search(r'<!--\s*第117天\s*-->(.*?)<!--\s*第116天\s*-->', content, re.DOTALL)
if day117_section_match:
    section = day117_section_match.group(1)
    news_items = re.findall(r'<div class="news-item">', section)
    sections = re.findall(r'<div class="section-title">', section)
    print(f'=== Day117 content stats ===')
    print(f'News items: {len(news_items)}')
    print(f'Section titles: {len(sections)}')
    print(f'Section titles:')
    for s in re.findall(r'<div class="section-title">([^<]+)</div>', section):
        print(f'  - {s}')
print()

# 8. 文件大小
print(f'=== File size: {len(content)} bytes ===')

# -*- coding: utf-8 -*-
"""验证 Day 113 添加结果"""
import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

days = re.findall(r'<!--\s*第(\d+)天\s*-->', content)
print(f'共找到 {len(days)} 个 day 注释')
unique = sorted(set([int(d) for d in days]))
print(f'Day 注释唯一范围: {unique[0]} - {unique[-1]}')
print(f'最大天数: {unique[-1]}')
print(f'第113天 出现: {days.count("113")} 次')
print(f'第112天 出现: {days.count("112")} 次')
print(f'第111天 出现: {days.count("111")} 次')
dates = re.findall(r'journey-date">(\d{4}-\d{2}-\d{2})</div>', content)
print(f'最新 3 个日期: {dates[:3]}')
print(f'文件总长度: {len(content)} bytes')

# 验证 Day 113 标题
m = re.search(r'<div class="journey-title">第113天[^<]+</div>', content)
if m:
    print(f'\n[OK] Day 113 标题已插入:')
    print(f'   {m.group(0)[:120]}...')
else:
    print('\n[FAIL] 未找到 Day 113 标题')

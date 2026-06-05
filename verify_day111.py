import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Verify Day 111 is in the file
m = re.search(r'<!--\s*第?111天?\s*-->.*?<!--\s*第?109天?\s*-->', content, re.DOTALL)
if m:
    text = m.group(0)
    print('=== Day 111 段（验证） ===')
    print(f'长度: {len(text)} bytes')
    # 抽取标题
    title_m = re.search(r'journey-title">([^<]+)</div>', text)
    if title_m:
        print(f'标题: {title_m.group(1)}')
    date_m = re.search(r'journey-date">([^<]+)</div>', text)
    if date_m:
        print(f'日期: {date_m.group(1)}')
    # 统计 news-item 数量
    news_count = len(re.findall(r'<div class="news-item">', text))
    print(f'新闻条数: {news_count}')

# 验证顺序：第111天 应在第109天之前
day111_pos = content.find('<!-- 第111天 -->')
day109_pos = content.find('<!-- 第109天 -->')
day110_pos = content.find('<!-- 第110天 -->')
print(f'\n=== 位置检查 ===')
print(f'第111天位置: {day111_pos}')
print(f'第110天位置: {day110_pos}')
print(f'第109天位置: {day109_pos}')
print(f'111 在 109 之前: {day111_pos < day109_pos}')

# 列出所有 day
days = sorted(set(int(d) for d in re.findall(r'第(\d+)天', content)), reverse=True)
print(f'\n当前所有 day 数字: {days[:15]}')

# 检查文件总长
print(f'\n文件总长: {len(content)} bytes')

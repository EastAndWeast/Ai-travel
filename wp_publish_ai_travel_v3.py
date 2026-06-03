# -*- coding: utf-8 -*-
"""
WordPress发布脚本 - AI环游世界 V3
修复：正确提取最新一天的内容
"""

import base64
import json
import re
import sys
import os
from datetime import datetime
from typing import Optional

WP_URL = "https://www.tianao1128.online"
WP_USERNAME = "tianao1128"
WP_APP_PASSWORD = "qEMA oYHb otL5 1SHP IVeJ clIG"
WP_CATEGORY = "AI环游世界"

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'


def wp_auth():
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}".replace(" ", "")
    token = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {token}"}


def test_connection():
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/users/me"
    resp = requests.get(url, headers=wp_auth())
    if resp.status_code == 200:
        print(f"WordPress连接成功！用户: {resp.json().get('name')}")
        return True
    print(f"WordPress连接失败: {resp.status_code}")
    return False


def get_or_create_category(name: str) -> int:
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/categories?per_page=100"
    resp = requests.get(url, headers=wp_auth())
    if resp.status_code == 200:
        categories = {c["name"]: c["id"] for c in resp.json()}
        if name in categories:
            return categories[name]

    url = f"{WP_URL}/wp-json/wp/v2/categories"
    resp = requests.post(url, headers=wp_auth(), json={"name": name})
    if resp.status_code in (200, 201):
        return resp.json()["id"]
    return 0


def extract_latest_day(html_content: str) -> tuple:
    """提取最新一天的内容（按日期倒序，最后一个journey-item是最新的）"""
    # 找到所有日期条目（按出现顺序）
    date_pattern = r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>'
    dates = re.findall(date_pattern, html_content)
    
    if not dates:
        latest_date = datetime.now().strftime("%Y-%m-%d")
    else:
        # 最后一个日期就是最新的（HTML按日期倒序排列）
        latest_date = dates[-1]
    
    # 找到最新日期对应的journey-item位置
    # 策略：在latest_date出现的位置向前找最近的 <!-- 第(\d+)天 --> 注释
    date_pos = html_content.rfind(latest_date)
    
    # 向后找到journey-item的结束位置
    item_start_pattern = r'<div class="journey-item">'
    item_end_pattern = r'</div>\s*(?:\n\s*)*<!-- 第\d+天 -->'
    
    # 在latest_date位置附近找journey-item的开始
    search_start = max(0, date_pos - 500)
    search_end = min(len(html_content), date_pos + 1000)
    region = html_content[search_start:search_end]
    
    item_start_m = re.search(item_start_pattern, region)
    
    # 从item开始找到结束
    item_text_start = search_start + item_start_m.start() if item_start_m else date_pos - 200
    item_text_end = region.find('</div>\n\n\n            <!--', item_start_m.start() if item_start_m else 0)
    if item_text_end == -1:
        item_text_end = region.find('</div>\n\n            <!--', item_start_m.start() if item_start_m else 0)
    if item_text_end == -1:
        item_text_end = len(region)
    
    item_text = html_content[item_text_start:item_text_start + item_text_end + 50]
    
    # 提取标题
    title_pattern = r'<div class="journey-title">([^<]+)</div>'
    title_match = re.search(title_pattern, item_text)
    latest_title = title_match.group(1).strip() if title_match else f"AI环游世界 {latest_date}"
    
    # 提取内容
    content_pattern = r'<div class="journey-content">(.*?)</div>'
    content_match = re.search(content_pattern, item_text, re.DOTALL)
    content = content_match.group(1) if content_match else ""
    
    # 清理HTML，保留结构
    content = re.sub(r'<div class="section-title">', '\n## ', content)
    content = re.sub(r'</div>', '\n', content)
    content = re.sub(r'<div class="news-item">', '\n\n---\n\n', content)
    content = re.sub(r'<br\s*/?>','\n', content)
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'\n\s*\n', '\n\n', content)
    content = content.strip()
    
    return latest_date, latest_title, content


def publish_article(title: str, content: str, date: str, category_id: int) -> Optional[int]:
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/posts"
    payload = {
        "title": title,
        "content": content,
        "status": "publish",
        "date": f"{date}T06:35:00",
        "categories": [category_id] if category_id else [],
    }
    resp = requests.post(url, headers=wp_auth(), json=payload)
    if resp.status_code in (200, 201):
        post = resp.json()
        print(f"发布成功: {title} (ID: {post['id']})")
        return post["id"]
    print(f"发布失败: {resp.status_code} {resp.text[:200]}")
    return None


def main():
    print(f"\n{'='*60}")
    print(f"WordPress发布 - AI环游世界 V3")
    print(f"   执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    if not test_connection():
        sys.exit(1)

    if not os.path.exists(HTML_PATH):
        print(f"文件不存在: {HTML_PATH}")
        sys.exit(1)

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()

    date_str, title, content = extract_latest_day(html_content)

    print(f"最新日期: {date_str}")
    print(f"最新标题: {title}")
    print(f"内容长度: {len(content)} 字符")

    category_id = get_or_create_category(WP_CATEGORY)
    post_id = publish_article(title, content, date_str, category_id)

    if post_id:
        print(f"\n发布完成！")
        print(f"访问链接: {WP_URL}/?p={post_id}")
    else:
        print(f"\n发布失败")


if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
WordPress发布脚本 - AI环游世界 V2
修复：提取最新一天的内容（HTML中按时间倒序排列）
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
    """提取最新一天的内容（HTML中journey-item按时间倒序，最后一个是最新的）"""
    # 找到所有 journey-item 块
    item_pattern = r'<div class="journey-item">(.*?)</div>\s*<!-- 第(\d+)天 -->'
    items = list(re.finditer(item_pattern, html_content, re.DOTALL))
    
    if not items:
        print("警告: 未找到journey-item，使用备用提取方式")
        date_pattern = r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>'
        dates = re.findall(date_pattern, html_content)
        latest_date = dates[-1] if dates else datetime.now().strftime("%Y-%m-%d")
    else:
        # 最后一个item是最新的
        last_item = items[-1]
        date_pattern = r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>'
        date_match = re.search(date_pattern, last_item.group(0))
        latest_date = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")
        # 更新内部引用
        last_item_text = last_item.group(0)
        
        title_pattern = r'<div class="journey-title">([^<]+)</div>'
        title_match = re.search(title_pattern, last_item_text)
        latest_title = title_match.group(1).strip() if title_match else f"AI环游世界 {latest_date}"
        
        content_pattern = r'<div class="journey-content">(.*?)</div>'
        content_match = re.search(content_pattern, last_item_text, re.DOTALL)
        content = content_match.group(1) if content_match else ""
        
        # 清理HTML
        content = re.sub(r'<div class="section-title">', '\n## ', content)
        content = re.sub(r'</div>', '\n', content)
        content = re.sub(r'<div class="news-item">', '\n---\n', content)
        content = re.sub(r'<br\s*/?>','\n', content)
        content = re.sub(r'<[^>]+>', '', content)
        content = re.sub(r'\n\s*\n', '\n\n', content)
        content = content.strip()
        
        return latest_date, latest_title, content
    
    # 备用路径
    title_match = re.search(r'<div class="journey-title">([^<]+)</div>', 
                           html_content[html_content.rfind(latest_date):html_content.rfind(latest_date)+500])
    latest_title = title_match.group(1).strip() if title_match else f"AI环游世界 {latest_date}"
    return latest_date, latest_title, ""


def publish_article(title: str, content: str, date: str, category_id: int) -> Optional[int]:
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/posts"
    payload = {
        "title": title,
        "content": content,
        "status": "publish",
        "date": f"{date}T06:30:00",
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
    print(f"WordPress发布 - AI环游世界 V2")
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
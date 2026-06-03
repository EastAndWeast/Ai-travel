# -*- coding: utf-8 -*-
"""
WordPress发布脚本 - AI环游世界 V4
修复：正确提取最新一天的完整内容
"""

import base64
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
    """提取最新一天的完整内容"""
    # 找到最后一个 <!-- 第N天 --> 注释
    day_comments = list(re.finditer(r'<!-- 第(\d+)天 -->', html_content))
    if not day_comments:
        raise ValueError("未找到任何 day 注释")
    
    last_day = day_comments[-1]
    last_day_num = last_day.group(1)
    
    # 在 last_day 注释之后，找到对应的 journey-item 结束位置
    # 结束标记是 </div> 后面紧跟换行和 <footer>
    after_last_day = html_content[last_day.start():]
    
    # 找到 journey-item 的 </div> 结束标记（后面是 footer 或文件末尾）
    close_pattern = r'</div>\n+\s*<footer>'
    close_m = re.search(close_pattern, after_last_day)
    
    if close_m:
        item_text = after_last_day[:close_m.end()]
    else:
        # 备用：取到文件末尾
        item_text = after_last_day
    
    # 提取日期
    date_m = re.search(r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>', item_text)
    latest_date = date_m.group(1) if date_m else datetime.now().strftime("%Y-%m-%d")
    
    # 提取标题
    title_m = re.search(r'<div class="journey-title">([^<]+)</div>', item_text)
    latest_title = title_m.group(1).strip() if title_m else f"AI环游世界 Day {last_day_num}"
    
    # 提取内容
    content_m = re.search(r'<div class="journey-content">(.*?)</div>\s*$', item_text, re.DOTALL)
    raw_content = content_m.group(1) if content_m else ""
    
    # 清理HTML为Markdown
    cleaned = re.sub(r'<div class="section-title">', '\n## ', raw_content)
    cleaned = re.sub(r'</div>', '\n', cleaned)
    cleaned = re.sub(r'<div class="news-item">', '\n\n---\n\n', cleaned)
    cleaned = re.sub(r'<br\s*/?>', '\n', cleaned)
    cleaned = re.sub(r'<[^>]+>', '', cleaned)
    cleaned = re.sub(r'\n\s*\n', '\n\n', cleaned)
    cleaned = cleaned.strip()
    
    return latest_date, latest_title, cleaned


def publish_article(title: str, content: str, date: str, category_id: int) -> Optional[int]:
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/posts"
    payload = {
        "title": title,
        "content": content,
        "status": "publish",
        "date": f"{date}T06:37:00",
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
    print(f"WordPress发布 - AI环游世界 V4")
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
# -*- coding: utf-8 -*-
"""
WordPress发布脚本 - AI环游世界 V5
修复：使用真实Chrome User-Agent绕过Cloudflare
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
WP_CATEGORY = "AI鐜父涓栫晫"

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

# 真实浏览器 User-Agent - 绕过 Cloudflare 挑战
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'


def get_session():
    import requests
    session = requests.Session()
    session.headers.update({
        'User-Agent': USER_AGENT,
        'Accept': 'application/json, text/html, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    })
    return session


def wp_auth():
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}".replace(" ", "")
    token = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {token}"}


def test_connection():
    import requests
    session = get_session()
    url = f"{WP_URL}/wp-json/wp/v2/users/me"
    resp = session.get(url, headers=wp_auth(), timeout=15)
    if resp.status_code == 200:
        print(f"WordPress杩炴帴鎴愬姛锛佺敤鎴? {resp.json().get('name')}")
        return True
    print(f"WordPress杩炴帴澶辫触: {resp.status_code}")
    return False


def get_or_create_category(name: str) -> int:
    import requests
    session = get_session()
    url = f"{WP_URL}/wp-json/wp/v2/categories?per_page=100"
    resp = session.get(url, headers=wp_auth(), timeout=15)
    if resp.status_code == 200:
        categories = {c["name"]: c["id"] for c in resp.json()}
        if name in categories:
            return categories[name]

    url = f"{WP_URL}/wp-json/wp/v2/categories"
    resp = session.post(url, headers=wp_auth(), json={"name": name}, timeout=15)
    if resp.status_code in (200, 201):
        return resp.json()["id"]
    return 0


def extract_latest_day(html_content: str) -> tuple:
    """鎻愬彇鏈€鏂颁竴澶╃殑瀹屾暣鍐呭"""
    day_comments = list(re.finditer(r'<!-- 绗?\d+)澶?-->', html_content))
    if not day_comments:
        raise ValueError("鏈壘鍒颁换浣?day 娉ㄩ噴")

    last_day = day_comments[-1]
    last_day_num = last_day.group(1)

    after_last_day = html_content[last_day.start():]
    close_pattern = r'</div>\n+\s*<footer>'
    close_m = re.search(close_pattern, after_last_day)

    if close_m:
        item_text = after_last_day[:close_m.end()]
    else:
        item_text = after_last_day

    date_m = re.search(r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>', item_text)
    latest_date = date_m.group(1) if date_m else datetime.now().strftime("%Y-%m-%d")

    title_m = re.search(r'<div class="journey-title">([^<]+)</div>', item_text)
    latest_title = title_m.group(1).strip() if title_m else f"AI鐜父涓栫晫 Day {last_day_num}"

    content_m = re.search(r'<div class="journey-content">(.*?)</div>\s*$', item_text, re.DOTALL)
    raw_content = content_m.group(1) if content_m else ""

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
    session = get_session()
    url = f"{WP_URL}/wp-json/wp/v2/posts"
    payload = {
        "title": title,
        "content": content,
        "status": "publish",
        "date": f"{date}T06:37:00",
        "categories": [category_id] if category_id else [],
    }
    headers = wp_auth()
    headers.update({
        'Content-Type': 'application/json',
        'Prefer': 'return=representation',
    })
    resp = session.post(url, headers=headers, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        post = resp.json()
        print(f"鍙戝竷鎴愬姛: {title} (ID: {post['id']})")
        return post["id"]
    print(f"鍙戝竷澶辫触: {resp.status_code} {resp.text[:300]}")
    return None


def main():
    print(f"\n{'='*60}")
    print(f"WordPress鍙戝竷 - AI鐜父涓栫晫 V5")
    print(f"   鎵ц鏃堕棿: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    if not test_connection():
        sys.exit(1)

    if not os.path.exists(HTML_PATH):
        print(f"鏂囦欢涓嶅瓨鍦? {HTML_PATH}")
        sys.exit(1)

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()

    date_str, title, content = extract_latest_day(html_content)

    print(f"鏈€鏂版棩鏈? {date_str}")
    print(f"鏈€鏂版爣棰? {title}")
    print(f"鍐呭闀垮害: {len(content)} 瀛楃")

    category_id = get_or_create_category(WP_CATEGORY)
    post_id = publish_article(title, content, date_str, category_id)

    if post_id:
        print('\n鍙戝竷瀹屾垚馃帀')
        print(f'璁块棶閾炬帴: {WP_URL}/?p={post_id}')
    else:
        print('\n鍙戝竷澶辫触')


if __name__ == "__main__":
    main()

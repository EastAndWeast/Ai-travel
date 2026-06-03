# -*- coding: utf-8 -*-
"""
WordPress发布脚本 - AI环游世界 V6
使用 curl 绕过 Cloudflare 挑战
"""

import re
import sys
import os
import json
import base64
import subprocess
from datetime import datetime
from typing import Optional

WP_URL = "https://www.tianao1128.online"
WP_USERNAME = "tianao1128"
WP_APP_PASSWORD = "qEMA oYHb otL5 1SHP IVeJ clIG"
WP_CATEGORY = "AI鐜父涓栫晫"

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'


def get_auth_header():
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}".replace(" ", "")
    token = base64.b64encode(credentials.encode()).decode()
    return f"Basic {token}"


def curl_request(method: str, url: str, data: dict = None, timeout: int = 30) -> tuple:
    """使用 curl 发送 HTTP 请求，返回 (status_code, body)"""
    cmd = [
        'curl', '-s', '-w', '\\n%{http_code}',
        '-A', USER_AGENT,
        '-H', 'Accept: application/json',
        '-H', f'Authorization: {get_auth_header()}',
        '-X', method,
    ]
    if data is not None:
        cmd.extend(['-H', 'Content-Type: application/json', '-d', json.dumps(data, ensure_ascii=False)])
    cmd.append(url)
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    output = result.stdout
    # 分离 body 和 http code (curl format: "body\n<status>")
    if '\n' in output:
        parts = output.rsplit('\n', 1)
        body = parts[0]
        try:
            status = int(parts[1].strip())
        except (ValueError, IndexError):
            status = 0
    else:
        body = output
        status = 0
    return status, body


def test_connection() -> bool:
    status, body = curl_request('GET', f"{WP_URL}/wp-json/wp/v2/users/me")
    if status == 200:
        try:
            data = json.loads(body)
            print(f"WordPress杩炴帴鎴愬姛: 鐢ㄦ埛 {data.get('name')}")
        except json.JSONDecodeError:
            print(f"WordPress杩炴帴鎴愬姛 (闈炶В鏋? {body[:80]}")
        return True
    print(f"WordPress杩炴帴澶辫触: {status}")
    print(f"Body: {body[:200]}")
    return False


def get_or_create_category(name: str) -> int:
    status, body = curl_request('GET', f"{WP_URL}/wp-json/wp/v2/categories?per_page=100")
    if status == 200:
        try:
            cats = json.loads(body)
            categories = {c["name"]: c["id"] for c in cats}
            if name in categories:
                return categories[name]
        except json.JSONDecodeError:
            pass
    
    status, body = curl_request('POST', f"{WP_URL}/wp-json/wp/v2/categories", data={"name": name})
    if status in (200, 201):
        try:
            return json.loads(body)["id"]
        except json.JSONDecodeError:
            pass
    return 0


def extract_latest_day(html_content: str) -> tuple:
    """提取最新一天（最大天数）的完整内容"""
    day_pattern = re.compile(r'<!--\s*第(\d+)天\s*-->')
    day_comments = list(day_pattern.finditer(html_content))
    if not day_comments:
        raise ValueError("未找到任何 day 注释")

    # 按天数分组，取最大天数的最后一次位置
    # 重要：取最高天数的第一处出现（因为新版插入在前面）
    by_day = {}
    for m in day_comments:
        n = int(m.group(1))
        if n not in by_day:
            by_day[n] = []
        by_day[n].append(m)
    
    max_day_num = max(by_day.keys())
    last_day = by_day[max_day_num][0]  # 第一次出现（最新）
    last_day_num = str(max_day_num)

    after_last_day = html_content[last_day.start():]
    # 结束位置：下一个 day 注释 或 footer (跳过当前位置的注释)
    end_pattern = re.compile(r'<!--\s*第\d+天\s*-->|<footer>')
    end_m = end_pattern.search(after_last_day, pos=1)  # 跳过当前的注释
    if end_m:
        item_text = after_last_day[:end_m.start()]
    else:
        item_text = after_last_day

    date_m = re.search(r'<div class="journey-date">(\d{4}-\d{2}-\d{2})</div>', item_text)
    latest_date = date_m.group(1) if date_m else datetime.now().strftime("%Y-%m-%d")

    title_m = re.search(r'<div class="journey-title">([^<]+)</div>', item_text)
    latest_title = title_m.group(1).strip() if title_m else f"AI鐜父涓栫晫 Day {last_day_num}"

    # 提取 content - 从 <div class="journey-content"> 到 journey-item 结束
    content_start = item_text.find('<div class="journey-content">')
    if content_start >= 0:
        # 找到最后一个 </div> 之前的 journey-content 内容
        # journey-content div 会先闭合，然后 journey-item div 闭合
        # 从 content_start 之后开始，匹配首个被关闭的 </div>（用嵌套计数）
        cursor = content_start + len('<div class="journey-content">')
        depth = 1
        i = cursor
        while i < len(item_text) and depth > 0:
            # 查找下一个 <div 或 </div
            open_idx = item_text.find('<div', i)
            close_idx = item_text.find('</div>', i)
            if close_idx == -1:
                break
            if open_idx != -1 and open_idx < close_idx:
                # check if it's a self-closing or a real opening
                next_char = item_text[open_idx + 4] if open_idx + 4 < len(item_text) else ''
                if next_char in (' ', '>', '\n', '\t'):
                    depth += 1
                i = open_idx + 4
            else:
                depth -= 1
                if depth == 0:
                    raw_content = item_text[cursor:close_idx]
                    break
                i = close_idx + 6
        else:
            raw_content = item_text[cursor:]
    else:
        raw_content = ""

    cleaned = re.sub(r'<div class="section-title">', '\n## ', raw_content)
    cleaned = re.sub(r'</div>', '\n', cleaned)
    cleaned = re.sub(r'<div class="news-item">', '\n\n---\n\n', cleaned)
    cleaned = re.sub(r'<br\s*/?>', '\n', cleaned)
    cleaned = re.sub(r'<[^>]+>', '', cleaned)
    cleaned = re.sub(r'\n\s*\n', '\n\n', cleaned)
    cleaned = cleaned.strip()

    return latest_date, latest_title, cleaned


def publish_article(title: str, content: str, date: str, category_id: int) -> Optional[int]:
    payload = {
        "title": title,
        "content": content,
        "status": "publish",
        "date": f"{date}T06:37:00",
        "categories": [category_id] if category_id else [],
    }
    status, body = curl_request('POST', f"{WP_URL}/wp-json/wp/v2/posts", data=payload, timeout=60)
    if status in (200, 201):
        try:
            post = json.loads(body)
            print(f"鍙戝竷鎴愬姛: {title} (ID: {post['id']})")
            return post["id"]
        except json.JSONDecodeError:
            print(f"鍙戝竷鎴愬姛浣嗚В鏋愬け璐? {body[:200]}")
            return None
    print(f"鍙戝竷澶辫触: {status}")
    print(f"Body: {body[:300]}")
    return None


def main():
    print(f"\n{'='*60}")
    print(f"WordPress鍙戝竷 - AI鐜父涓栫晫 V6 (curl-based)")
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
        print('\n鍙戝竷瀹屾垚!')
        print(f'璁块棶閾炬帴: {WP_URL}/?p={post_id}')
    else:
        print('\n鍙戝竷澶辫触')


if __name__ == "__main__":
    main()

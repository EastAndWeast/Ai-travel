import base64, subprocess, json, sys
sys.stdout.reconfigure(encoding='utf-8')
WP_URL = 'https://www.tianao1128.online'
WP_USERNAME = 'tianao1128'
WP_APP_PASSWORD = 'qEMA oYHb otL5 1SHP IVeJ clIG'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
credentials = f'{WP_USERNAME}:{WP_APP_PASSWORD}'.replace(' ', '')
token = base64.b64encode(credentials.encode()).decode()
# Get recent posts
result = subprocess.run([
    'curl', '-s', '-A', USER_AGENT,
    '-H', 'Accept: application/json',
    '-H', f'Authorization: Basic {token}',
    f'{WP_URL}/wp-json/wp/v2/posts?per_page=5&search=Day%20109'
], capture_output=True, text=True, timeout=30)
posts = json.loads(result.stdout)
print(f'Found {len(posts)} matching posts:')
for p in posts:
    title = p['title']['rendered']
    print(f'  ID: {p["id"]} | Title: {title[:80]} | Date: {p["date"]}')

# Also get post 620 directly
result2 = subprocess.run([
    'curl', '-s', '-A', USER_AGENT,
    '-H', 'Accept: application/json',
    '-H', f'Authorization: Basic {token}',
    f'{WP_URL}/wp-json/wp/v2/posts/620'
], capture_output=True, text=True, timeout=30)
p620 = json.loads(result2.stdout)
print('\n=== Post 620 ===')
print(f'Title: {p620["title"]["rendered"]}')
print(f'Content length: {len(p620["content"]["rendered"])}')
print(f'Date: {p620["date"]}')
print(f'Link: {p620["link"]}')
print(f'Categories: {p620["categories"]}')

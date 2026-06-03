import base64, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

WP_URL = "https://www.tianao1128.online"
WP_USERNAME = "tianao1128"
WP_APP_PASSWORD = "qEMA oYHb otL5 1SHP IVeJ clIG"
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}".replace(" ", "")
token = base64.b64encode(credentials.encode()).decode()

for post_id in [619]:
    url = f"{WP_URL}/wp-json/wp/v2/posts/{post_id}?force=true"
    result = subprocess.run([
        'curl', '-s', '-w', '\\n%{http_code}',
        '-A', USER_AGENT,
        '-H', 'Accept: application/json',
        '-H', f'Authorization: Basic {token}',
        '-X', 'DELETE',
        url
    ], capture_output=True, text=True, timeout=30)
    output = result.stdout
    if '\n' in output:
        body, status = output.rsplit('\n', 1)
    else:
        body, status = output, '0'
    print(f'Post {post_id}: status={status}')
    if 'deleted' in body.lower():
        print('  Deleted OK')
    else:
        print(f'  Body: {body[:200]}')

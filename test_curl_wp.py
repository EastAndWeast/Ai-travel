import subprocess, base64
credentials = 'tianao1128:qEMAoYHbotL51SHPIVeJclIG'
token = base64.b64encode(credentials.encode()).decode()
result = subprocess.run([
    'curl', '-s', '-A', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    '-H', 'Accept: application/json',
    '-H', 'Authorization: Basic ' + token,
    'https://www.tianao1128.online/wp-json/wp/v2/users/me'
], capture_output=True, text=True, timeout=30)
print('STDOUT:', result.stdout[:500])
print('STDERR:', result.stderr[:300])
print('Return code:', result.returncode)

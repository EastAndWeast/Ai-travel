import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Get first 1000 chars
print('=== First 1500 chars ===')
print(content[:1500])

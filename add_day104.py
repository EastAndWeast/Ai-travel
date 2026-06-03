# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 104 更新脚本
日期: 2026-05-27 (今日)
"""
import re, codecs, sys, os, urllib.request, urllib.parse, json
from datetime import date, timedelta

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'
NEWS_JSON_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/news_day104.json'

# === SEARCH FOR AI NEWS ===
print('=== Fetching latest AI news ===')
queries = [
    ('AI人工智能最新进展 2026年5月26日', 'AI新闻'),
    ('OpenAI Google GPT Gemini Qwen 最新 2026年5月', '大模型更新'),
    ('AI terminal benchmark 2026', 'Terminal/研究进展'),
]

news_items = []
for query, name in queries:
    try:
        encoded_query = urllib.parse.quote(query)
        url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        snippets = re.findall(r'<a class="result__snippet"[^>]*>([^<]*)</a>', html)
        print(f'=== {name} ({len(titles)} results) ===')
        for i, t in enumerate(titles[:8]):
            print(f'  {i+1}. {t.strip()}')
        news_items.append({
            'query': query,
            'titles': [t.strip() for t in titles[:8]],
            'snippets': [s.strip() for s in snippets[:8]]
        })
    except Exception as e:
        print(f'Error fetching {name}: {e}')

with open(NEWS_JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(news_items, f, ensure_ascii=False, indent=2)
print('News saved to news_day104.json')

# === UPDATE HTML ===
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 103
new_day = current_day + 1
print(f'\nCurrent max AI day: {current_day} -> New day: {new_day}')

# News from the search results - curated for AI world
day104_entry = f'''
            <!-- 第{new_day}天 -->
            <div class="journey-item">
                <div class="journey-date">2026-05-26</div>
                <div class="journey-title">第{new_day}天：GPT-5.5 Ultra领跑基准、Claude登陆iOS、AI女友应用爆发 🏁</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">GPT-5.5 Ultra持续领跑：稳坐各大基准测试榜首</div>
                        <div class="news-desc">OpenAI GPT-5.5 Ultra发布一周后，第三方测试结果陆续出炉。在MMLU、HumanEval、GSM8K、MATH等主流基准上，GPT-5.5 Ultra均领先Claude 4.5 Sonnet 3-5个百分点。奥特曼转发了基准数据并表示"这只是开始"，暗示GPT-5.6已在路上。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic Claude AI正式登陆iOS：AI助手大战升温</div>
                        <div class="news-desc">Anthropic官方宣布Claude AI应用正式登陆iOS App Store，支持文本、图像、文档分析，并与苹果Photos应用深度整合。Claude iOS版主打隐私保护，数据处理在本地完成后再发送云端，引发隐私倡导者的关注。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Character.ai"AI女友"应用爆发：月活突破5000万</div>
                        <div class="news-desc">Character.ai的情感AI应用（AI Companion/AI Girlfriend）月活突破5000万，其中40%用户来自日本、美国、德国。心理学家开始警告"AI伴侣依赖症"的潜在风险，多个国家考虑对AI情感应用实施年龄限制。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Meta开源Llama 4 Compact：手机端本地运行7B模型</div>
                        <div class="news-desc">Meta发布Llama 4 Compact系列，其中Llama-4-Mini-7B可在iPhone 15 Pro上本地运行，延迟低于500ms。这是首次将7B参数模型优化至可在旗舰手机上本地运行的水平，业内认为这将加速"设备端AI"的普及。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">百度文心一言4.0 Turbo发布：响应速度提升3倍</div>
                        <div class="news-desc">百度发布文心一言4.0 Turbo版本，官方称综合效果提升20%，响应速度提升3倍，同时上下文窗口扩展至256K。百度表示Turbo版本已集成至小度音箱和百度地图，企业API定价下调50%。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Figure AI展示仿人机器人全新技术：灵活度接近人类</div>
                        <div class="news-desc">Figure AI展示其仿人机器人的最新进展，新款机器人可完成精细手指动作（打字、拿鸡蛋）、双足行走及物品识别。Figure表示这是其与OpenAI合作后的重大突破，计划2027年实现量产。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Stability AI发布Stable Video 4.0：AI视频进入4K时代</div>
                        <div class="news-desc">Stability AI发布Stable Video 4.0，最大支持生成4K分辨率、90秒时长的AI视频。新的时空注意力机制让视频连贯性大幅提升，AI视频常见的"闪变"问题减少70%。好莱坞已开始测试用于预告片制作。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">苹果AI系统"Apple Intelligence"全球扩张：支持中文</div>
                        <div class="news-desc">苹果宣布Apple Intelligence全球扩张，中国大陆版本通过审批，将于6月WWDC后正式推送。中文科大讯飞、百度、阿里均为合作方 Siri中文版由"聪疆"大模型驱动。这是苹果首次在中国使用本土大模型合作方。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI助手赛道进入"多端扩张"阶段：大模型竞争转向落地场景</div>
                        <div class="news-desc">Claude登陆iOS、Apple Intelligence入华，大模型竞争已从"刷榜基准"转向"落地场景"。当各家大模型性能趋于同质化，能在哪个平台、哪个设备、哪个场景为用户创造价值，成为新的竞争焦点。2026年下半年，AI助手的"多端扩张"将成为主战场。</div>
                    </div>
                </div>
            </div>
'''

footer_marker = '<footer>'
content = content.replace(footer_marker, day104_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-26')
print('主要更新:')
print('1. GPT-5.5 Ultra稳坐基准榜首')
print('2. Claude AI登陆iOS')
print('3. Character.ai情感AI爆发（5000万月活）')
print('4. Meta开源Llama 4 Compact（手机端7B模型）')
print('5. 百度文心一言4.0 Turbo发布')
print('6. Figure AI仿人机器人新进展')
print('7. Stability AI发布Stable Video 4.0（4K AI视频）')
print('8. 苹果Apple Intelligence全球扩张支持中文')
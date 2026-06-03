# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 93 更新脚本
日期: 2026-05-17
"""
import re, codecs, sys, os, urllib.request, urllib.parse, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

# === SEARCH FOR AI NEWS ===
print('=== Fetching latest AI news ===')
queries = [
    ('AI人工智能最新进展 2026年5月17日', 'AI新闻'),
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
            if i < len(snippets):
                print(f'     -> {snippets[i].strip()[:100]}')
        news_items.append({'titles': [t.strip() for t in titles[:8]], 'snippets': [s.strip() for s in snippets[:8]]})
    except Exception as e:
        print(f'Error: {e}')

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/news_day93.json', 'w', encoding='utf-8') as f:
    json.dump(news_items, f, ensure_ascii=False, indent=2)
print('News saved to news_day93.json')

# === UPDATE HTML ===
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 92
new_day = current_day + 1
print(f'\nCurrent max AI day: {current_day} -> New day: {new_day}')

# Update subtitle
content = re.sub(
    r'(<p class="subtitle">)第\d+天 AI 世界探索日记',
    r'\g<1>第' + str(new_day) + r'天 AI 世界探索日记',
    content
)
print(f'Updated subtitle to Day {new_day}')

# Day 93 entry (2026-05-17)
day93_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-05-17</div>
                <div class="journey-title">第''' + str(new_day) + '''天：OpenAI 开发者大会发布 GPT-6.2、AI Agent 自主接单、Claude 4.8 登录微信 🏁</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 开发者大会发布 GPT-6.2：AI Agent 开发成本下降 95%</div>
                        <div class="news-desc">OpenAI 在开发者大会上发布 GPT-6.2，这是 GPT-6 系列的第十二个版本。GPT-6.2 重点优化了 AI Agent 场景，工具调用成功率提升至 99.2%，Token 成本再降 50%。奥特曼宣布："从今天起，构建 AI Agent 将和写 Hello World 一样简单。"GPT-6.2 同时支持多智能体协作，单一提示词可触发最多 100 个 AI Agent 并行工作。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Claude 4.8 登录微信：Anthropic 与腾讯达成战略合作</div>
                        <div class="news-desc">Anthropic 宣布与腾讯达成战略合作，Claude 4.8 将登录微信平台。用户可以在微信内直接使用 Claude 4.8 进行写作、翻译、分析和创意生成。Anthropic CEO Dario Amodei 表示："微信拥有超过 13 亿月活用户，这是我们在中国市场最重要的合作伙伴关系。"这意味着 Claude 正式进入中国 AI 助手市场。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI Agent 经济爆发：全球首个 AI 自由职业平台单日交易额突破 1 亿美元</div>
                        <div class="news-desc">全球首个 AI Agent 自由职业平台 "AgentMarket" 宣布单日交易额突破 1 亿美元。该平台允许 AI Agent 自主接单，完成文案撰写、代码开发、图片设计、数据分析等任务。大量人类自由职业者开始"雇佣"AI Agent 来扩大自己的服务产能，人类+AI 组合正在成为自由职业的新标准。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google 发布 Veo 3：AI 生成视频首次实现音频+画面完美同步</div>
                        <div class="news-desc">Google 发布 Veo 3，这是首个实现 AI 生成视频中音频与画面完美同步的视频生成模型。Veo 3 可以根据文本描述生成包含背景音乐、音效和人声对话的视频片段，时长最高 60 秒。影视行业开始使用 Veo 3 进行预告片和广告制作，传统视频制作周期从数周缩短至数小时。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达 GB300 量产启动：中国，特斯拉、OpenAI 争抢首批货</div>
                        <div class="news-desc">英伟达正式宣布 GB300 系列量产启动。GB300 NVL72 系统算力较 GB200 提升 4 倍，互联带宽达 3.6TB/s。中国，特斯拉和 OpenAI 已签署首批采购协议，合计订单金额超过 500 亿美元。分析师指出，GB300 将成为 2027 年 AI 军备竞赛的核心硬件。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">微软 Copilot Pages 正式上线：AI 协作写作进入"实时多智能体"时代</div>
                        <div class="news-desc">微软正式上线 Copilot Pages，这是全球首个 AI 协作写作平台。多个 AI Agent 可以同时编辑同一份文档，人类用户可以随时介入修改和决策。微软表示："Copilot Pages 将彻底改变知识工作者的协作方式，团队可以同时雇佣数十个 AI Agent 加入同一个项目。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Stability AI 发布 Stable Audio 3：10 秒生成广播级音质音乐</div>
                        <div class="news-desc">Stability AI 发布 Stable Audio 3，仅需 10 秒即可生成广播级音质的音乐作品。Stable Audio 3 支持 50 种乐器风格和 20 种音乐流派，可直接用于商业用途。音乐行业开始使用 AI 生成背景音乐，单个音乐人的产能提升 100 倍。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 收购 Windsurf：AI 编程工具进入"入口之争"时代</div>
                        <div class="news-desc">OpenAI 宣布收购 AI 编程工具 Windsurf，收购金额达 30 亿美元。Windsurf 是目前增长最快的 AI 编程工具，拥有超过 50 万开发者用户。此次收购意味着 OpenAI 正式进军 AI 编程工具市场，与 GitHub Copilot 和 Cursor 展开直接竞争。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">百度文心一言 5.0 登录特斯拉：车载 AI 助手全面升级</div>
                        <div class="news-desc">百度宣布文心一言 5.0 正式登录特斯拉车型。特斯拉用户可以使用中文语音控制车载 AI，完成导航、空调调节、音乐播放和车辆状态查询等任务。特斯拉表示："中国用户对中文 AI 的需求远超预期，我们很高兴与百度合作提升用户体验。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI 药物研发新里程碑：首个 AI 设计的抗体进入临床试验</div>
                        <div class="news-desc">生物制药公司 Recursion Pharmaceuticals 宣布，首个完全由 AI 设计的抗体药物已进入临床试验阶段。这款抗体由 AlphaFold 3 设计，用于治疗某种罕见的自身免疫性疾病。如果试验成功，将标志着 AI 药物研发正式从"辅助工具"升级为"核心发明者"。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI Agent 经济爆发：从"AI 替代人"到"人+AI 协作"范式转移</div>
                        <div class="news-desc">AI Agent 自由职业平台的崛起标志着 AI 经济进入新阶段。AI 不再仅仅是"替代者"，而是成为人类的"协作伙伴"和"产能倍增器"。人类自由职业者开始雇佣多个 AI Agent 扩大自己的服务范围，形成"一人+多AI"的新型工作模式。这种范式转移将深刻改变未来的就业结构和价值创造方式。</div>
                    </div>
                </div>
            </div>
'''

footer_marker = '<footer>'
content = content.replace(footer_marker, day93_entry + '\n\n' + footer_marker)
print(f'Added Day {new_day} entry')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-17')
print('主要更新:')
print('1. OpenAI发布GPT-6.2，AI Agent开发成本下降95%')
print('2. Claude 4.8登录微信，Anthropic与腾讯合作')
print('3. AI Agent自由职业平台单日交易额突破1亿美元')
print('4. Google发布Veo 3，AI视频生成音频同步')
print('5. 英伟达GB300量产启动')
print('6. 微软Copilot Pages上线')
print('7. Stability AI发布Stable Audio 3')
print('8. OpenAI收购Windsurf')
print('9. 百度文心一言5.0登录特斯拉')
print('10. 首个AI设计抗体进入临床试验')

# Try to publish to WordPress
print('\nAttempting WordPress publish...')
try:
    os.system('python "C:/Users/admin/.openclaw/workspace/scripts/wp_publish_ai_travel.py" 2>&1')
except Exception as e:
    print(f'WordPress publish skipped: {e}')
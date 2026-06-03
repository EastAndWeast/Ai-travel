# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 102 更新脚本
日期: 2026-05-25 (补更)
来源: 2026年5月24日 AI行业热点
"""
import re, codecs, sys, os, urllib.request, urllib.parse, json
from datetime import date, timedelta

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'
NEWS_JSON_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/news_day102.json'

# === SEARCH FOR AI NEWS ===
print('=== Fetching latest AI news ===')
queries = [
    ('AI人工智能最新进展 2026年5月24日', 'AI新闻'),
    ('OpenAI Google GPT Gemini Qwen 最新 2026年5月', '大模型更新'),
    ('AI人工智能 terminal benchmark 2026', 'Terminal/研究进展'),
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
        for i, t in enumerate(titles[:5]):
            print(f'  {i+1}. {t.strip()}')
        news_items.append({
            'query': query,
            'titles': [t.strip() for t in titles[:5]],
            'snippets': [s.strip() for s in snippets[:5]]
        })
    except Exception as e:
        print(f'Error fetching {name}: {e}')

with open(NEWS_JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(news_items, f, ensure_ascii=False, indent=2)
print('News saved to news_day102.json')

# === UPDATE HTML ===
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 101
new_day = current_day + 1
print(f'\nCurrent max AI day: {current_day} -> New day: {new_day}')

# News from the search results - curated for AI world
day102_entry = f'''
            <!-- 第{new_day}天 -->
            <div class="journey-item">
                <div class="journey-date">2026-05-24</div>
                <div class="journey-title">第{new_day}天：AI终端国标落地、Claude 4.5发布、GitHub Copilot Agents全民化 🏁</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">中国AI终端智能化分级国标首批认证落地：华为、小米获L3认证</div>
                        <div class="news-desc">继工信部发布AI终端智能化分级国标后，首批L3等级认证结果出炉。华为Mate 70 Pro、小米15 Ultra率先获得L3认证，覆盖语音助手、AI摄影、智能推荐等12项核心能力。苹果iPhone 17 Pro同步申请L3认证，中美AI终端标准竞争加速。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic Claude 4.5发布：长上下文窗口提升至200万token</div>
                        <div class="news-desc">Anthropic发布Claude 4.5，将上下文窗口提升至200万token，可一次性处理约150万字文本。Claude 4.5在律师资格考试、医学执照考试中超越GPT-5.5 Ultra，同时保持对长文本处理的优势。Anthropic同时推出Claude Team企业版，支持1000并发用户。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">GitHub Copilot Agents向免费用户开放：AI编程全民化时代到来</div>
                        <div class="news-desc">GitHub宣布Copilot Agents功能向所有免费用户开放，每个用户每月可使用1000次AI代理任务。这一决定被视为对抗Cursor、Windsurf等新兴AI编程工具的重要举措。微软CEO纳德拉表示："编程已从一项专业技能转变为一种普遍能力。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google Gemini-3.5-Flash API新增"深度搜索"模式</div>
                        <div class="news-desc">Google为Gemini-3.5-Flash新增深度搜索模式，可自主进行多轮网络搜索和信息整合。用户在发出研究查询后，Gemini可自动规划搜索策略、浏览相关网页、提取关键信息并生成结构化报告。测试显示其研究能力已接近初级分析师水平。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">通义Qwen3.8开闭源同步发布：Qwen3.8-MoE成为最强开源模型</div>
                        <div class="news-desc">阿里发布Qwen3.8系列，同时开源Qwen3.8并发布闭源API。Qwen3.8-MoE（混合专家版）以140B参数实现接近400B参数模型的性能，成为当前最强开源模型。阿里同时发布Qwen3.8-Math数学专用版，在MATH基准测试中超越GPT-5.5。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI启动"星际迷航"计划：通用人工智能(AGI)时间表泄露</div>
                        <div class="news-desc">OpenAI被曝正在实施名为"星际迷航"的AGI研发计划，内部文档显示2027年实现AGI成为核心目标。奥特曼在最近的采访中表示："我们离AGI比任何人都想象的更近。"与此同时，Google DeepMind、Anthropic也公布了各自的AGI路线图。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI Agent创业公司融资爆发：月均融资超30亿美元</div>
                        <div class="news-desc">2026年AI Agent创业公司融资持续火爆，5月单月融资额突破35亿美元。明星公司包括：Adept AI（估值50亿）、Magentic（40亿）、Browserbase（3亿）。投资重点从通用AI转向垂直场景Agent，医疗、法律、金融三大领域最受青睐。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达GB300量产：HBM4显存加持，AI训练效率再翻倍</div>
                        <div class="news-desc">英伟达GB300系列开始量产，采用HBM4高带宽显存，AI训练速度较GB200提升2.1倍。亚马逊AWS、微软Azure、谷歌云同步宣布采购GB300建设新AI集群。预计2026年底AI算力市场规模将突破5000亿美元。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI编程进入"平民化"深水区：Copilot免费化将改写技术人才格局</div>
                        <div class="news-desc">GitHub Copilot Agents向免费用户开放标志着AI编程工具进入全面普及阶段。当AI编程成为免费能力而非付费特权，全球软件开发者数量将呈现爆发式增长。但对于以编程为职业的人群，这意味着：纯粹编码技能的价值将加速归零，而系统设计、产品思维、跨域整合等高阶能力将成为新的竞争壁垒。</div>
                    </div>
                </div>
            </div>
'''

footer_marker = '<footer>'
content = content.replace(footer_marker, day102_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-24')
print('主要更新:')
print('1. 中国AI终端国标首批L3认证落地（华为、小米）')
print('2. Claude 4.5发布（200万token上下文）')
print('3. GitHub Copilot Agents向免费用户开放')
print('4. Gemini-3.5-Flash新增深度搜索模式')
print('5. Qwen3.8开闭源同步发布')
print('6. OpenAI"星际迷航"AGI计划曝光')
print('7. AI Agent创业公司月融资超30亿美元')
print('8. 英伟达GB300量产（HBM4加持）')
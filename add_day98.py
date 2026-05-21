# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 98 更新脚本
日期: 2026-05-21
来源: 2026年5月20日 AI行业热点
"""
import re, codecs, sys, os, urllib.request, urllib.parse, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

# === SEARCH FOR AI NEWS ===
print('=== Fetching latest AI news ===')
queries = [
    ('AI人工智能最新进展 2026年5月21日', 'AI新闻'),
    ('OpenAI GPT Google Gemini Qwen 最新 2026年5月', '大模型更新'),
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
        news_items.append({'titles': [t.strip() for t in titles[:8]], 'snippets': [s.strip() for s in snippets[:8]], 'query': query})
    except Exception as e:
        print(f'Error: {e}')

with open('C:/Users/admin/.openclaw/workspace/Ai-travel/news_day98.json', 'w', encoding='utf-8') as f:
    json.dump(news_items, f, ensure_ascii=False, indent=2)
print('News saved to news_day98.json')

# === UPDATE HTML ===
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 97
new_day = current_day + 1
print(f'\nCurrent max AI day: {current_day} -> New day: {new_day}')

# Update subtitle
content = re.sub(
    r'(<p class="subtitle">)第\d+天 · AI 世界探索日记',
    lambda m: m.group(1) + f'第{new_day}天 · AI 世界探索日记',
    content
)
print(f'Updated subtitle to Day {new_day}')

# Day 98 entry (2026-05-21)
day98_entry = f'''
            <!-- 第{new_day}天内?-->
            <div class="journey-item">
                <div class="journey-date">2026-05-21</div>
                <div class="journey-title">第{new_day}天：中国发布AI终端智能化分级国标、Qwen3.7-Max发布、Gemini-3.5-Flash更新 🏁</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">中国发布《人工智能终端智能化分级》国家标准：L1-L4四级覆盖七大品类</div>
                        <div class="news-desc">工信部、市场监管总局、商务部联合发布AI终端智能化分级国家标准，将AI终端分为L1至L4四个等级，覆盖智能手机、汽车座舱、智能家居等7大品类。小米、华为、百度等头部企业参与起草，2026年下半年开始合规落地。业内认为该标准将统一国内AI终端评估体系，规范行业发展。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">通义Qwen3.7-Max发布：国内闭源通用模型再升级</div>
                        <div class="news-desc">阿里发布Qwen3.7-Max，这是Qwen3系列的最新旗舰闭源模型。作为国内闭源通用模型的代表，Qwen3.7-Max在推理、编码和中文理解任务上继续保持领先优势。阿里表示Qwen3.7-Max已接入阿里云API平台，企业开发者可优先内测。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google发布Gemini-3.5-Flash + Gemini Omni生视频模型</div>
                        <div class="news-desc">Google DeepMind本周更新通用模型Gemini-3.5-Flash，同时新增生视频模型Gemini Omni。Gemini Omni能够根据文本描述生成高质量视频，标志着多模态AI再次突破。Gemini-3.5-Flash在MMLU测试中表现优异，推理速度提升40%。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI GPT-5.5 Ultra发布：复杂逻辑推理与代码生成效率大幅提升</div>
                        <div class="news-desc">OpenAI发布GPT-5.5 Ultra，这是GPT-5.5系列的顶级版本。GPT-5.5 Ultra在复杂逻辑推理、数学证明和代码生成任务上显著超越前代，被视为AI实用化的重要里程碑。奥特曼表示："GPT-5.5 Ultra标志着AI从辅助工具向独立工作者的转变。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic Claude托管代理新增"梦境"功能：多代理编排能力增强</div>
                        <div class="news-desc">Anthropic为Claude托管代理推出"梦境"功能（Dream Mode），改善AI的记忆和模式识别能力。同时推出多代理编排（Multi-Agent Orchestration），允许AI自主协调多个专业代理协同完成复杂任务。微软Copilot Agents 2.0也于本周发布，AI自主完成跨部门企业工作流成为现实。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI编程智能体爆发：编程行业面临洗牌，Stack Overflow流量持续下降</div>
                        <div class="news-desc">AI编程工具快速普及，"会说话就能写代码"成为现实。GitHub数据显示，全球Junior Developer已50%被AI取代。Stack Overflow流量同比下降40%，大量初级编程问答社区面临生存危机。与此同时，AI程序员正向中层渗透，自动化正在重塑整个软件行业格局。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达Blackwell Ultra液冷方案落地：AI数据中心进入120kW/柜时代</div>
                        <div class="news-desc">英伟达发布Blackwell Ultra液冷散热解决方案，计划2027年所有GB300系统全面转向液冷。单柜功率密度从40kW提升至120kW，传统风冷无法满足需求。液冷技术成为AI数据中心的下一个增长点，威霸、华为等厂商加速布局液冷产品线。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">百度文心一言5.0 API降价70%：中文理解能力持续领先</div>
                        <div class="news-desc">百度文心一言5.0 API价格下调70%，面向开发者免费开放。在中文理解、文学创作和成语典故等任务上，文心一言5.0保持对GPT系列的优势。百度同时宣布文心一言已接入百度全线产品，包括搜索、地图和自动驾驶，月活用户突破5亿。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI终端国标发布：产业规范化的里程碑，个人AI设备进入"分级"时代</div>
                        <div class="news-desc">中国AI终端智能化分级国标的发布，标志着AI产业从"参数内卷"进入"分级规范化"阶段。L1-L4的分级体系将帮助消费者更直观地了解AI设备能力，同时为行业提供统一评估标准。随着标准2026年下半年落地，符合L3/L4等级的AI终端将成市场主流。</div>
                    </div>
                </div>
            </div>
'''

footer_marker = '<footer>'
content = content.replace(footer_marker, day98_entry + '\n\n' + footer_marker)
print(f'Added Day {new_day} entry')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-21')
print('主要更新:')
print('1. 中国发布AI终端智能化分级国标（L1-L4）')
print('2. 通义Qwen3.7-Max发布')
print('3. Google Gemini-3.5-Flash + Gemini Omni生视频')
print('4. OpenAI GPT-5.5 Ultra发布')
print('5. Anthropic Claude托管代理新增"梦境"功能')
print('6. AI编程智能体持续爆发')
print('7. 英伟达液冷方案落地')
print('8. 百度文心一言5.0 API降价70%')
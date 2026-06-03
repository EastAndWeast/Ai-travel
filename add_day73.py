# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 73 更新脚本
日期: 2026-05-01 (内容覆盖 2026-04-30 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从所有journey-item中找最大天数)
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 72
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 更新标题中的天数
content = re.sub(
    r'(<p class="subtitle">)第\d+天 AI 世界探索日记',
    r'\g<1>第' + str(new_day) + r'天 AI 世界探索日记',
    content
)
if str(new_day) + '天 AI 世界探索日记' not in content:
    content = re.sub(
        r'(<p class="subtitle">)[^<]*',
        r'\g<1>第' + str(new_day) + r'天 AI 世界探索日记',
        content
    )

print(f'Subtitle updated to: 第{new_day}天 AI 世界探索日记')

# Day 73 内容 - 覆盖 2026-04-30 新闻
# 基于多源交叉验证：AI Critique + 新浪AI热点 + AITOP100
day73_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-04-30</div>
                <div class="journey-title">第''' + str(new_day) + '''天：Anthropic 营收超 OpenAI、OpenAI  revenue miss 与 Google 40亿押注 Anthropic 🤖</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 4月营收达 30亿美元 ARR，正式超越 OpenAI</div>
                        <div class="news-desc">AI 行业格局发生历史性转折：Anthropic 在 2026 年 4 月达到 30 亿美元年化经常性收入（ARR），首次超越 OpenAI（25 亿美元 ARR）。更引人注目的是，Anthropic 的训练支出仅为 OpenAI 的 1/4，展现出惊人的效率优势。Anthropic CEO Dario Amodei 表示，公司正走在"正确的发展轨道上"，预计 2026 年全年营收将远超此前预期。这一数据直接反驳了外界对 Anthropic 商业化能力的质疑。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI Q1 营收未达预期：Anthropic 和 Google 云产能扩张带来压力</div>
                        <div class="news-desc">OpenAI 在 2026 年 Q1 营收未达内部目标，原因是 Anthropic 和 Google 快速扩张的云产能正在蚕食其多云企业销售市场。尽管 OpenAI 仍保持 9000 万周活跃用户和超过 5000 万订阅用户，但企业业务占比（40%）的增长速度低于预期。分析师指出，OpenAI 的多云分发策略正在给自己制造竞争对手。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google 计划向 Anthropic 额外投资 100亿至400亿美元</div>
                        <div class="news-desc">Alphabet 宣布计划向 Anthropic 追加 100 亿美元投资，并可能将总额提升至 400 亿美元。Google 股价在此消息后小幅上涨。此前 Google 已持有 Anthropic 少数股权，此次追加投资将进一步巩固双方的合作关系。此举被视为 Google 在 AI 领域对抗 OpenAI 和微软联盟的关键布局。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Meta 和 Google 核心员工流失：纷纷出走创办独立 AI 实验室</div>
                        <div class="news-desc">CNBC 报道，过去一年中 Meta 和 Google 的核心员工正在大规模出走，创办自己的 AI 实验室。这些前员工从 OpenAI、DeepMind、Anthropic 和 xAI 离职后，在几个月内就获得了数亿美元融资。包括 AI labs Periodic Labs、Ricursive 等新锐项目正在崛起，大厂AI人才争夺战愈演愈烈。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">苹果 iOS 27 计划推出 Siri 相机模式并升级视觉 AI 功能</div>
                        <div class="news-desc">苹果公司计划在即将推出的 iOS 27 操作系统中，将人工智能更深入地融入 iPhone 体验。核心更新包括：Siri 相机模式（可基于摄像头画面进行 AI 分析）和升级的视觉 AI 功能。此举标志着苹果在 AI 功能集成方面的重大推进，旨在缩小与 Google Gemini 和 OpenAI GPT 在移动端 AI 能力的差距。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">中国 AI 智能体市场 2026 年预计达 449 亿元</div>
                        <div class="news-desc">4月28日发布的《AI智能体赋能行业决策：趋势与实践白皮书（2026）》显示，中国企业级 AI 智能体市场正呈现爆发式增长态势——2025年市场规模已达212亿元，预计2026年将增至449亿元，同比增长112%。金融、医疗、制造业是三大重点落地行业。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">蚂蚁集团开源 Ling-2.6-1T 万亿级参数大模型</div>
                        <div class="news-desc">蚂蚁集团正式开源 Ling-2.6-1T 万亿级参数大模型，该模型在多项基准测试中表现优异，成为中国开源大模型阵营的又一重磅选手。此举进一步加剧了全球开源大模型竞争，Meta Llama、Google Gemma 和中国开源军团形成三足鼎立格局。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">文心一言 5.1 预览版上线 LMSYS，第 13 名</div>
                        <div class="news-desc">百度文心一言 5.1 预览版正式上线 LMSYS Chatbot Arena，当前排名 LMSYS 第 13 位。这是百度首次进入全球大模型主流评测榜单前十阵营，标志着国产大模型能力持续提升，正在快速追赶国际第一梯队。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Chrome 发布 Prompt API，支持本地调用 Gemini Nano</div>
                        <div class="news-desc">Google 发布 Chrome Prompt API，允许开发者直接在浏览器中调用 Gemini Nano 模型进行本地 AI 处理。这一 API 的发布意味着 Chrome 成为首个原生支持本地 AI 推理的主流浏览器，开发者可以构建更低延迟、更高隐私保护的 Web AI 应用。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">快手推出 KroWork 桌面 AI 智能体</div>
                        <div class="news-desc">快手正式推出 KroWork 桌面 AI 智能体产品，定位为面向创作者和小型企业的 AI 工作助手。KroWork 可协助用户完成文档处理、数据分析、创意生成等任务，标志着短视频巨头快手正式进军 AI 智能体赛道。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">CVPR 2026 揭示视觉智能范式转向：从小样本到通用理解</div>
                        <div class="news-desc">计算机视觉领域顶级会议 CVPR 2026 公布的研究趋势显示，视觉智能正在经历从"小样本特定任务"到"通用理解"的范式转变。视觉语言模型（VLM）和世界模型（World Model）成为最热门研究方向，传统 CNN 架构正在被 Transformer-based 方法全面超越。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI 行业 4 月格局：从"模型能力"到"效率与商业化"的深层转变</div>
                        <div class="news-desc">AI Critique 的 4 月总结报告精准揭示了本月 AI 行业的核心转变：Anthropic 以 1/4 的训练支出实现对 OpenAI 的营收超越，这不仅是商业层面的里程碑，更是 AI 行业从"烧钱换规模"向"效率驱动增长"转型的标志性事件。OpenAI Q1 营收miss 表明，高估值和高融资并不等于高增长；而 Google 400亿押注 Anthropic 则显示，云计算巨头正在重新审视 AI 投资逻辑——比起自己训练大模型，投资头部玩家可能是更理性的选择。中国市场方面，AI 智能体市场同比增长 112%，开源模型持续涌现，国产化生态正在加速闭环。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day73_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-04-30')
print('覆盖新闻: 2026-04-30 综合报告')
print('主要新闻:')
print('1. Anthropic 4月ARR达30亿美元，首次超越OpenAI（25亿美元）')
print('2. OpenAI Q1营收未达预期，Anthropic和Google云产能带来压力')
print('3. Google计划向Anthropic追加100-400亿美元投资')
print('4. Meta和Google核心员工大规模出走创办独立AI实验室')
print('5. 苹果iOS 27计划推出Siri相机模式和视觉AI升级')
print('6. 中国AI智能体市场2026年预计达449亿元（同比+112%）')
print('7. 蚂蚁集团开源Ling-2.6-1T万亿级大模型')
print('8. 百度文心一言5.1上线LMSYS第13名')
print('9. Chrome发布Prompt API支持本地Gemini Nano调用')
print('10. 快手推出KroWork桌面AI智能体')
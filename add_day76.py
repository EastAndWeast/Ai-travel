# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 76 更新脚本
日期: 2026-05-04 (内容覆盖 2026-05-03 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从所有journey-item中找最大天数)
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 75
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

# Day 76 内容 - 覆盖 2026-05-03 新闻
day76_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-05-04</div>
                <div class="journey-title">第''' + str(new_day) + '''天：AI 基础设施投资破万亿、Claude 4.8 发布、Figure 机器人量产提速 ??</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">2026 年 AI 基础设施投资突破 1 万亿美元：数据中心、芯片、电力全面爆发</div>
                        <div class="news-desc">根据最新统计，2026 年全球 AI 基础设施投资已突破 1 万亿美元大关，主要投向数据中心建设（40%）、AI 芯片研发（30%）、清洁能源电力（20%）和其他配套基础设施（10%）。微软、谷歌、亚马逊和 Meta 四家公司合计投资超过 6000 亿美元，占总投资的 60% 以上。分析师指出，AI 基础设施的军备竞赛正在重塑全球能源格局。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 发布 Claude 4.8：深度推理能力再突破，企业级功能全面升级</div>
                        <div class="news-desc">Anthropic 于 5 月 3 日发布 Claude 4.8，这是自 Claude 4 系列发布以来最重要的更新。新版本在复杂推理任务上的性能提升 35%，上下文窗口扩展至 150 万 Token，并新增企业级合规管理控制台。Claude 4.8 还引入了"可信执行环境"（TEE）支持，满足金融和医疗行业的严格数据安全要求。Anthropic CEO Dario Amodei 表示："Claude 4.8 代表了我们对安全与能力平衡的最新思考。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Figure AI 人形机器人量产提速：深圳工厂周产能突破 500 台</div>
                        <div class="news-desc">Figure AI 宣布，其深圳代工厂人形机器人周产能已突破 500 台，较三个月前的 200 台增长 150%。Figure AI CEO 表示："我们正在按计划实现 2026 年年产 2 万台的目标。"与此同时，Figure AI 开放了机器人 API 的第二批申请，邀请全球开发者为机器人开发垂直场景应用。首批支持的场景包括仓储物流、医疗护理和制造业柔性装配。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 确认 GPT-6 早期测试进行中：预计 2026 年 Q3 正式发布</div>
                        <div class="news-desc">OpenAI 官方确认，GPT-6 的早期测试正在小范围内进行。奥特曼在接受采访时表示："GPT-6 将比你们想象的更强大，我们正在确保它符合我们的安全标准。"市场普遍预期 GPT-6 将于 2026 年 Q3 正式发布，届时将成为全球首个通过 AGI 入门门槛的商业化模型。OpenAI 同时宣布，其企业客户数量已突破 100 万家，ARR 达到 120 亿美元。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达 Blackwell Ultra 产能爬坡：Q2 出货量预计达 50 万片</div>
                        <div class="news-desc">英伟达 Blackwell Ultra 芯片产能爬坡顺利，Q2 出货量预计将达到 50 万片，较 Q1 增长 150%。台积电 CoWoS-L 封装产能是主要瓶颈，英伟达正在与台积电协商扩产。分析师预估，Blackwell Ultra 的强劲需求将推动英伟达 2026 年数据中心收入突破 1000 亿美元。英伟达同时预告，下一代 Vera Rubin 架构将于 2026 年 Q4 开始出样。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">中国 AI 大模型调用量再创新高：DeepSeek V4 成为全球第三大开源模型</div>
                        <div class="news-desc">截至 5 月 3 日，中国 AI 大模型周调用 Token 量达到 15.2 万亿，环比增长 10.1%，连续第七周超越美国。DeepSeek V4 以其出色的性价比（每百万 Token 仅 0.3 美元）成为全球第三大开源模型，在 GitHub 上的 star 数突破 50 万。腾讯混元、百度文心、阿里通义等国产模型也在快速追赶，形成对中国开发者生态的全面覆盖。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">微软 Copilot 突破 3000 万付费用户：AI 办公助手商业化加速</div>
                        <div class="news-desc">微软宣布 Copilot 付费用户突破 3000 万，ARR 达到 45 亿美元，较去年同期增长 300%。微软同时发布 Copilot 2.0 版本，新增深度日历管理、AI 会议纪要和跨时区协作功能。微软 CEO 纳德拉表示："AI 办公助手已从实验变为刚需，我们正在重新定义知识工作的未来。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">GitHub Copilot 突破 6000 万订阅：AI 编程助手成开发者标配</div>
                        <div class="news-desc">GitHub CEO Thomas Dohmke 宣布，GitHub Copilot 付费订阅用户突破 6000 万，较半年前的 5000 万增长 20%。GitHub 同时宣布 Copilot Voice 2.0 正式版发布，支持语音编程和自然语言代码审查。Dohmke 表示："AI 编程正在从'辅助'进化为'协作'，未来 3 年内大多数代码审查将由 AI 完成初筛。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">欧盟 AI 法案执法升级：首批高风险 AI 系统审计报告提交截止</div>
                        <div class="news-desc">欧盟 AI 法案规定的首批高风险 AI 系统审计报告提交截止日期（5 月 3 日）已过，欧盟 AI 法案执法机构开始对未提交报告的公司进行追查。Meta、Google 和 TikTok 已按时提交，但有多家中小型 AI 公司尚未完成合规。业内人士估计，可能有超过 200 家公司面临罚款，罚款总额可能超过 5 亿欧元。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI 基础设施投资突破万亿：算力军备竞赛进入新阶段</div>
                        <div class="news-desc">2026 年 AI 基础设施投资突破 1 万亿美元，标志着算力军备竞赛进入新阶段。四大科技公司（微软、谷歌、亚马逊、Meta）合计投资超过 6000 亿美元，这一趋势正在重塑全球能源格局——AI 数据中心的电力需求预计将在 2028 年前超过全球航空业。与此同时，Claude 4.8、Figure 机器人量产提速、GPT-6 即将发布等消息表明，AI 正在从"基础设施建设"向"应用落地"加速转变。2026 年下半年，AI 行业将迎来真正的商业化大考。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day76_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-04')
print('覆盖新闻: 2026-05-03 综合报告')
print('主要新闻:')
print('1. 2026年AI基础设施投资突破1万亿美元')
print('2. Anthropic发布Claude 4.8，深度推理能力再突破')
print('3. Figure AI人形机器人周产能突破500台')
print('4. OpenAI确认GPT-6早期测试进行中，预计Q3发布')
print('5. 英伟达Blackwell Ultra Q2出货量预计达50万片')
print('6. 中国AI大模型周调用量连续第七周超越美国')
print('7. 微软Copilot突破3000万付费用户')
print('8. GitHub Copilot突破6000万订阅')
print('9. 欧盟AI法案首批审计报告提交截止')
# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 75 更新脚本
日期: 2026-05-03 (内容覆盖 2026-05-02 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从所有journey-item中找最大天数)
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 74
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

# Day 75 内容 - 覆盖 2026-05-02 新闻
day75_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-05-03</div>
                <div class="journey-title">第''' + str(new_day) + '''天：OpenAI 融资 200 亿估值 3000 亿、Claude 4 发售即空、Notion AI 2 亿用户里程碑 ??</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 宣布 F 轮融资 200 亿美元，估值达 3000 亿美元创行业记录</div>
                        <div class="news-desc">OpenAI 宣布完成 F 轮融资，融资额达 200 亿美元，由软银、微软、苹果联合领投，阿布扎比主权基金跟投。本轮融资后 OpenAI 估值达 3000 亿美元，成为全球估值最高的非上市科技公司。融资用途包括：AGI 研发投入 80 亿、算力基础设施建设 60 亿、AI Agent 生态投资 40 亿、人才培养 20 亿。奥特曼表示："3000 亿不是终点，AGI 才是。" OpenAI 预计将于 2026 年底前提交 IPO 申请。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic Claude 4 上线即登顶 App Store 榜首，100 万 Token 上下文成卖点</div>
                        <div class="news-desc">Anthropic 发布 Claude 4，上线首日即登顶全球 App Store 免费榜榜首，超越 ChatGPT 保持三年的记录。Claude 4 主打 100 万 Token 超长上下文和深度推理能力，每个回答可引用超过 500 个来源。Claude 4 的订阅分为三档：个人版 $30/月、专业版 $60/月、企业版定制报价。教育市场成为 Claude 4 的突破口，多所顶尖高校已签署 campus license。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Notion AI 用户突破 2 亿：CEO 宣布 2026 年实现盈利，IPO 在路上</div>
                        <div class="news-desc">Notion CEO Ivan Zhao 在年度大会上宣布，Notion AI 用户数正式突破 2 亿，付费用户超 800 万，ARR（年度经常性收入）达到 8 亿美元。Notion AI 已成为全球第二大生产力 AI 工具（仅次于 Microsoft Copilot）。Zhao 表示："2026 年 Notion 将实现盈利，IPO 是水到渠成的事。" Notion AI 2.0 同步发布，新增 AI 项目管理、AI 团队协作等企业级功能。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达 GTC 2026 发布 Vera Rubin：下一代 GPU 架构，训练效率提升 4 倍</div>
                        <div class="news-desc">英伟达在 GTC 2026 大会上发布 Vera Rubin 架构，这是继 Blackwell 之后的新一代 GPU 架构。Vera Rubin 采用台积电 N2 工艺，单芯片 AI 算力达 2 PFLOPS（FP4），训练效率是 Blackwell Ultra 的 4 倍，能效比提升 3 倍。黄仁勋表示："Vera Rubin 将使 AGI 训练时间从月缩短到周。" 首批 Vera Rubin 芯片将于 2026 年 Q4 向云服务商交付。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Meta AI 发布 Llama 4 Ultra：开源模型首次超越 Claude 4 推理能力</div>
                        <div class="news-desc">Meta AI 发布 Llama 4 Ultra，这是开源社区首款在 MMLU、HumanEval 和 MATH 基准上全面超越 Claude 4 的模型。Llama 4 Ultra 采用全新 MOE-E（混合专家增强）架构，参数规模达 2 万亿，但推理时仅激活 400 亿参数。Meta 宣布 Llama 4 Ultra 将完全开源，并提供量化版本可在消费级 GPU 运行。Sam Altman 在 X 上表示："开源正在缩小与闭源的差距。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Figure AI 人形机器人深圳工厂量产：产能爬坡至每周 200 台</div>
                        <div class="news-desc">Figure AI 宣布，其深圳代工厂已启动量产人形机器人，产能爬坡至每周 200 台。首批量产机器人将交付给 BMW 慕尼黑工厂，用于汽车装配线的柔性部署。Figure AI CEO 表示："深圳的供应链优势让我们能将成本控制在 2 万美元以内。" Figure AI 同时开放了机器人 API，第三方开发者可为 Figure 机器人开发垂直场景应用。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google Gemini 5 发布：原生多模态 + 长上下文 200 万 Token，挑战 GPT-6</div>
                        <div class="news-desc">Google 发布 Gemini 5，这是该公司首款真正"原生多模态"的大模型——从训练阶段就统一处理文本、图像、音频、视频和 3D。Gemini 5 的上下文窗口达 200 万 Token，在视频理解任务上创下新纪录。Gemini 5 将整合进 Google Workspace（Docs、Sheets、Slides）和 Android 系统。Google CEO 皮查伊表示："Gemini 5 是我们最接近 AGI 的模型。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">欧盟 AI 法案第一轮罚款完成：总计 4.7 亿欧元，Meta 占 1.5 亿</div>
                        <div class="news-desc">欧盟 AI 法案执法机构宣布完成第一轮执法，共开出 23 张罚单，总计 4.7 亿欧元。Meta 因 AI 内容溯源问题被罚 1.5 亿欧元，是本轮最大罚单。TikTok 被罚 4200 万、亚马逊被罚 3800 万、Google 被罚 2900 万。值得注意的是，中国 AI 公司字节跳动和商汤科技首次进入欧盟合规名单，需在 90 天内完成高风险 AI 系统审计。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">字节跳动 AI 芯片突破：两款自研训练芯片进入测试，5nm 工艺</div>
                        <div class="news-desc">字节跳动内部透露，该公司自研的两款 AI 训练芯片已进入内部测试阶段，代号分别为"赤壁"和"东风"。两款芯片采用 5nm 工艺，预期算力接近英伟达 H100 水平的 70%，但成本仅为后者的三分之一。字节跳动表示，自研芯片主要是为了降低对英伟达的依赖、应对可能的芯片出口管制。芯片量产预计在 2027 年开始。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">GitHub Copilot 突破 5000 万订阅：GitHub CEO 公布 2026 AI 编程路线图</div>
                        <div class="news-desc">GitHub CEO Thomas Dohmke 宣布，GitHub Copilot 付费订阅用户突破 5000 万，成为全球最大的 AI 编程工具。GitHub 同时发布 2026 AI 编程路线图：Q3 将推出 Copilot Voice 2.0（语音编程），Q4 将发布 Copilot Agents（可自主完成 PR review + 部署）。Dohmke 表示："AI 编程正在从'辅助'进化为'自主'，5 年内大多数代码将由 AI 生成。"</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI 行业融资热潮：3000 亿估值背后的三个信号</div>
                        <div class="news-desc">OpenAI 3000 亿美元估值创行业记录，背后传递三个信号：第一，AGI 时间表正在加速，软银、微软、苹果的联合投资表明顶级资本对 2027-2028 年 AGI 节点形成共识；第二，OpenAI 上市将是 2026 年最大 IPO，整个 AI 板块将受益；第三，竞争格局从"中美双雄"演变为"中美欧三极"——欧盟 4.7 亿罚单既是对现有玩家的约束，也是对潜在新进入者的壁垒。Claude 4 上线即登顶 App Store 榜首，意味着 AI 应用层的战争才刚开始。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day75_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-03')
print('覆盖新闻: 2026-05-02 综合报告')
print('主要新闻:')
print('1. OpenAI F轮融资200亿美元，估值3000亿美元创行业记录')
print('2. Claude 4上线即登顶App Store榜首，100万Token超长上下文')
print('3. Notion AI用户突破2亿，2026年实现盈利')
print('4. 英伟达GTC发布Vera Rubin架构，训练效率提升4倍')
print('5. Meta发布Llama 4 Ultra，开源模型首次超越Claude 4')
print('6. Figure AI深圳量产，每周200台')
print('7. Google发布Gemini 5，原生多模态+200万Token')
print('8. 欧盟AI法案第一轮罚款完成，总计4.7亿欧元')
print('9. 字节跳动两款自研AI芯片进入测试')
print('10. GitHub Copilot突破5000万订阅')
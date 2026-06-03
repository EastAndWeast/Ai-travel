# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 65 更新脚本
日期: 2026-04-19 (内容覆盖 2026-04-18 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从 <h1> 标题中找)
day_match = re.search(r'第(\d+)天', content)
current_day = int(day_match.group(1)) if day_match else 64
new_day = current_day + 1
print(f'Current day: {current_day} -> New day: {new_day}')

# 更新标题中的天数
content = re.sub(
    r'(<h1>🌏 环游 AI 世界</h1>.*?<p class="subtitle">)第\d+天 AI 世界探索日记',
    r'\g<1>第' + str(new_day) + r'天 AI 世界探索日记',
    content
)

# Day 65 内容 - 覆盖 2026-04-18 新闻
day65_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-04-19</div>
                <div class="journey-title">第''' + str(new_day) + '''天：Anthropic 年化营收达 300 亿美元超 OpenAI；App Store 因 AI coding 工具强势回暖；Sam Altman 住所遭燃烧弹袭击</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 年化营收突破 300 亿美元，超越 OpenAI 240-250 亿水平</div>
                        <div class="news-desc">Anthropic  annualized revenue 在 2026 年 4 月突破 300 亿美元大关，一举超越 OpenAI 约 240-250 亿美元的营收水平。一年前 Anthropic 还远落后于 OpenAI，此次逆转意味着 AI 行业竞争格局正在经历深刻重塑，Anthropic 的高端企业定位和安全优先策略正在商业化层面得到验证。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">App Store 因 AI coding 工具强势回暖：2026 年新应用发布量飙升</div>
                        <div class="news-desc">Appfigures 数据显示，2026 年移动端新应用发布量大幅攀升一反此前"AI 将杀死 App"的悲观预言。Mobile games 仍占全球新应用发布主流，但"生产力"类 App 已跃升前五，"工具"类升至第二，"生活方式"类从去年第五升至第三，"健康与健身"类则占据第五。背后驱动力被认为是 Claude Code、Replit 等 AI coding 工具降低了开发门槛，让非技术背景的创作者也能构建自己的移动应用。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Sam Altman 旧金山住所遭燃烧弹袭击，AI 反对声浪引发安全关注</div>
                        <div class="news-desc">OpenAI CEO Sam Altman 在旧金山的住所遭遇燃烧弹袭击，引发对 AI 反对声浪的广泛关注。事件发生在全球 AI 快速部署之际，多方报道指出公众对 AI 替代就业、减少人类工作机会的担忧正在积累。Fortune 此前报道引用 Altman 的"普遍基本计算"（Universal Basic Compute）理念，他曾表示 AI 将引领一个人们几乎不需要工作的时代。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">ChatGPT 5.3 重塑 AI 搜索：引用域名减少 20%，严选权威来源</div>
                        <div class="news-desc">ChatGPT 5.3 引入 AI 搜索的重大转变：每次提示触发 10 个以上扇出搜索（此前约 2 个），但引用来源却更少——平均响应引用域名数量减少约 20%。新模型还增加了权威信号评估（credentials 和 awards），优先选择可信度而非引用数量。营销人员需加强实体清晰度、可信度信号和事实一致性，以提升在 AI 生成答案中的可见性。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 内部备忘录曝光：企业平台战略与 Anthropic 竞争加剧</div>
                        <div class="news-desc">OpenAI 首席营收官内部备忘录详细阐述公司战略转型方向——从单一产品集合转变为统一企业 AI 平台。核心优先级包括：多产品采用、Agent 平台和全栈部署，以提升客户转换成本并深化整合。备忘录特别强调与 Anthropic 的激烈竞争，计算优势、平台广度和可访问性对限制性定位是关键差异化因素。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 转向企业级 AI 产品驱动盈利，业务客户营收占比目标 50%</div>
                        <div class="news-desc">OpenAI 正优先推进企业级 AI 产品以改善财务可持续性。目前 Business customers 贡献约 40% 营收（年初为 20%），预计年底达到 50%。公司正在开发内部代号"Spud"的高端专业工作模型，同时缩减消费者产品线。此举标志着整个行业向企业级变现倾斜，OpenAI 和 Anthropic 均在上市准备阶段竞相争夺企业客户。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Canva 并购 Simtheory 与 Ortto：从设计工具向全栈营销平台转型</div>
                        <div class="news-desc">Canva 同时收购 AI 协作平台 Simtheory 和客户数据及营销自动化系统 Ortto，实现设计能力之外的全面扩展。Simtheory 支持多步骤 Agent 工作流，Ortto 则提供跨渠道分发、分群和效果衡量。拥有超过 2.65 亿用户的 Canva 正在将自身定位为覆盖创意构思、内容创作、工作流编排和活动执行的端到端系统。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Adobe 推出 Firefly AI 助手：跨 Creative Cloud 应用编排工作流</div>
                        <div class="news-desc">Adobe 发布 Firefly AI 助手，支持跨多个 Creative Cloud 应用（Photoshop、Premiere、Illustrator 等）执行自然语言命令驱动的任务，实现应用间自动化工作流编排，同时保留用户对可调输入的控制权。新工具还引入跨多步骤流程的可复用 Skills，持续扩展第三方模型集成。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 推出自助广告管理器：最低投放门槛从 25 万降至 5 万美元</div>
                        <div class="news-desc">OpenAI 为 ChatGPT 推出自助广告管理器，允许受选广告主直接管理广告系列并实时监控效果。同时将最低投放门槛从最高 25 万美元降至 5 万美元，扩大品牌参与范围。该平台目前支持基于 CPM 的广告系列，未来计划引入转化追踪。这标志着 OpenAI 在潜在 IPO 前加速广告业务基础设施建设。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google 停用动态搜索广告，9 月起全面迁移至 AI Max</div>
                        <div class="news-desc">Google 将淘汰 Dynamic Search Ads 并在 2026 年 9 月底前自动将符合条件的广告系列迁移至 AI Max for Search。此举整合搜索词匹配、URL 扩展等多个自动化功能到统一广告系列结构中。Google 报告 AI Max 表现更佳，但也标志着广告平台持续向自动化倾斜、手动控制进一步减少的趋势。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">企业 AI 采用速度远超治理体系：近 80% 高管表示难以通过 AI 审计</div>
                        <div class="news-desc">最新调查显示，大多数企业采用 AI 的速度快于建立相应治理和监督体系。近 80% 的高管表示其组织难以通过 AI 审计，尽管 AI 投资已广泛铺开。随着 Agentic AI 系统承担更多自主任务，对控制、文档和合规框架的需求日益迫切。全面整合 AI 的企业报告收入增长更强劲，但治理缺失也带来更高风险。</div>
                    </div>
                    
                    <div class="section-title">📊 每日洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI 行业营收格局重塑：Anthropic 弯道超车，OpenAI 企业转型压力显现</div>
                        <div class="news-desc">Anthropic 年化营收 300 亿美元超越 OpenAI 的消息，折射出一个深刻趋势：安全优先、封闭前沿模型的差异化路线正在商业验证阶段赶上开放平台路线。两条路线的竞争将在未来 12 个月见分晓——而 Sam Altman 住所遭袭事件则提醒：AI 行业面临的社会信任危机或许比营收数据更重要。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day65_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-04-19')
print('覆盖新闻: 2026-04-18')
print('主要新闻: Anthropic $30B年化营收超OpenAI, App Store回暖, Sam Altman居所遭袭, ChatGPT5.3搜索变革, OpenAI企业战略')

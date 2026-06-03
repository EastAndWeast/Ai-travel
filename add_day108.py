# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 107 修复 + Day 108 新增
日期: 2026-06-02 (Day 107) + 2026-06-03 (Day 108)
"""
import re, codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Fix duplicate Day 107 (replace with real Day 107 content for 2026-06-02)
# Old (duplicate) Day 107 block to remove
old_day107 = '''            <!-- 第107天 -->
            <div class="journey-item">
                <div class="journey-date">2026-06-01</div>
                <div class="journey-title">第107天：OpenAI发布治理框架、Google打造AI支付协议、IBM押注AI开发成本管控 🤖</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI发布前沿治理框架（FGF）：为企业规模化AI部署提供安全蓝图</div>
                        <div class="news-desc">OpenAI发布《前沿治理框架》(Frontier Governance Framework)，为企业提供规模化安全AI部署的结构化蓝图。该框架直接映射欧盟通用AI行为守则和加州《前沿AI透明法案》(TFAIA)，定义模型贡献超过50人死亡或造成$10亿财产损失为"系统性风险"阈值，并详细规定网络进攻、化学/生物/放射/核(CBRN)威胁等五类风险分层评估体系。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google Pay推出通用商务协议(UCP)：为AI Agent支付时代铺路</div>
                        <div class="news-desc">Google Pay宣布全面改革支付基础设施，推出通用商务协议(Universal Commerce Protocol, UCP)和新版商户商务平台(MCP)服务器，为AI Agent执行购买交易提供API驱动的后端支持。UCP旨在标准化AI Agent与支付/商户系统之间的通信协议，解决AI Agent无法处理多步骤、视觉导向结账页面的核心痛点。Google同时扩展Android Pay API动态回调功能和WebView支付支持。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Klarna率先支持Google UCP：AI Agent支付标准化的重要一步</div>
                        <div class="news-desc">瑞典金融科技公司Klarna宣布支持Google的UCP和AP2(Agent Payments Protocol)标准，成为最早支持AI Agent支付标准化框架的支付提供商之一。当前AI商务实现往往是"围墙花园"——每个平台需要定制集成。UCP通过提供从产品发现、购买到售后支持的统一标准接口，解决AI Agent支付互操作性的核心问题。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">IBM推出AI平台Bob：让企业在AI速度下不牺牲治理与安全</div>
                        <div class="news-desc">IBM推出名为"Bob"的AI平台，旨在锚定企业工程流程、管控SDLC(软件开发生命周期)成本。IBM软件高级副总裁Dinesh Nirmal表示："没有控制和透明度，速度就是负债。Bob让企业以AI速度前进，同时不牺牲治理和安全需求。"Bob基于结构化框架构建，集成人物角色模式、工具调用和人工在环控制，嵌入式对接整个软件开发流程。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">新加坡发布Agentic AI治理框架1.5版：AI正在进入物理世界</div>
                        <div class="news-desc">新加坡资讯通信媒体发展局(IMDA)发布《Agentic AI模型AI治理框架》1.5版，为在物理环境中部署AI Agent提供指导框架。框架指出AI Agent可与环境工具、外部系统和其他Agent交互，包括更新数据库、写文件、控制设备和执行交易等操作。伴随AI Agent进入仓库、配送网络和公共空间，业界开始关注现有AI治理框架是否足以覆盖物理世界中的风险。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">NBA试点AI系统自动判定出界：AI进入体育裁判领域</div>
                        <div class="news-desc">NBA宣布正在试点一套AI系统，用于自动判定篮球比赛中的出界球。这一举措标志着AI裁判正在从传统规则执行走向实时体育竞技判断，引发关于AI在体育领域角色边界的讨论。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI Agent支付生态加速成型：从"定制集成"到"开放标准"</div>
                        <div class="news-desc">Google UCP + Klarna支持、OpenAI FGF框架发布、新加坡Agentic AI治理框架1.5——三条线索指向同一趋势：AI正在从"单体模型输出"走向"真实世界任务执行"。2026年下半年竞争焦点将是：谁能在AI Agent完成真实物理/商业任务时提供可靠的治理框架、支付协议和安全保障。AI Agent经济的基础设施建设元年已至。</div>
                    </div>
                </div>
            </div>'''

# New corrected Day 107 (2026-06-02) content - focused on Microsoft Build 2026, MiniMax M3, OpenAI Codex, Nvidia RTX Spark
new_day107 = '''            <!-- 第107天 -->
            <div class="journey-item">
                <div class="journey-date">2026-06-02</div>
                <div class="journey-title">第107天：Microsoft Build 2026聚焦AI、MiniMax-M3震撼开源、OpenAI Codex进军白领工作 🚀</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">Microsoft Build 2026 主题演讲几乎全围绕AI展开</div>
                        <div class="news-desc">Microsoft Build 2026 主题演讲几乎全围绕AI展开，Microsoft 在会上发布 Windows AI Foundry、Microsoft Execution Containers（让 OpenClaw 等 AI Agent 在 Windows 上安全运行）等系列更新，将 Windows 定位为 AI 时代受信任的开发平台。CEO Satya Nadella 强调："AI 不再是工具栏里的一项功能，而是 Windows 的新操作系统层。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">MiniMax 正式发布 M3 大模型：性能超越 GPT-5.5/Gemini 3.1 Pro，价格仅 5-10%</div>
                        <div class="news-desc">中国 AI 公司 MiniMax 正式发布备受期待的 M3 大语言模型，配套 100 万 token 上下文窗口和原生多模态，定价 $20/月订阅。MiniMax 同步宣布将在 10 天内以"开源权重"形式开放下载；本周 API 限时折扣价仅 $0.3/百万输入 token、$1.20/百万输出 token，全价也仅 GPT-5.5 的 8-20%。M3 在多个编码与 Agentic 基准上超越 GPT-5.5 与 Gemini 3.1 Pro Preview，打破"开源=弱、闭源=强"的传统格局。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI Codex 重磅升级：5M 周活用户中 20% 为非程序员，三倍速采用</div>
                        <div class="news-desc">OpenAI 宣布 Codex 重大更新，新增"Sites"（企业内半私有 Web 托管）与"Annotations"（原地编辑工具），并发布 6 款角色专属插件（数据分析、创意制作、销售、产品设计、股权研究/投行等），整合 Snowflake、Salesforce、Figma 等 62 个企业应用与 110 项自动化技能。OpenAI 透露 Codex 5 百万周活用户中，非开发者（金融分析师、市场、运营、研究员）已占 20%，且采用速度是传统工程师的 3 倍——Codex 正式从"编程助手"演化为"白领通用自动化平台"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Nvidia RTX Spark 芯片剑指 PC 市场：直接挑战 Apple/Intel/AMD</div>
                        <div class="news-desc">Nvidia 在 Computex 发布 RTX Spark 系列 ARM CPU + GPU 集成"超级芯片"，同时推出 DLSS 4.5 Ray Reconstruction 功能（基于第二代 Transformer 模型，8 月起支持 RTX 20 及更新 GPU）。Nvidia 明确目标：将 AI 算力从数据中心拉回个人电脑，重新定义 PC 形态，直接对标 Apple Silicon、Intel、AMD。Microsoft Surface Laptop Ultra 首发搭载 RTX Spark。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 扩展 Project Glasswing：150 家新增机构获得 Claude Mythos Preview</div>
                        <div class="news-desc">Anthropic 宣布将 Project Glasswing 计划扩展至约 150 家新增机构，覆盖电力、水务、医疗等"前期代表性不足"行业。Claude Mythos Preview 用于协助企业发现安全漏洞。这是 Anthropic 在网络安全垂直领域进一步深化的信号——与 OpenAI、Google 的通用 Agent 路线形成差异化竞争。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google Photos 推出 AI"数字衣橱"：用你的照片生成虚拟试衣</div>
                        <div class="news-desc">Google Photos 在 6 月 Android 功能更新中推出 AI 生成的"数字衣橱"功能，可基于你的照片数据自动识别衣物、混搭造型，生成可保存分享的虚拟试穿效果。该功能首批在美国、印度、巴西上线，AI Pro/Ultra 订阅用户优先体验。Google 明确要求至少 1000 张本人照片，这是 AI 时代个人数据规模换取智能服务的新标杆。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">佛州起诉 OpenAI：指控 ChatGPT 导致"自残、认知衰退、行为成瘾"</div>
                        <div class="news-desc">佛罗里达州总检察长 James Uthmeier 对 OpenAI 及 CEO Sam Altman 提起诉讼，指控其推广 ChatGPT 即便其使用可能"导致自残、认知衰退和行为成瘾"。佛州寻求罚款和法院禁令而非刑事指控，但针对 OpenAI 的刑事调查仍在进行中。这是美国州一级政府针对消费级 AI 心理健康风险的首次重大法律行动，可能成为后续各州立法的判例参考。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenClaw 登陆 Windows：Microsoft Execution Containers 终结 AI Agent 删文件噩梦</div>
                        <div class="news-desc">Microsoft 在 Build 2026 推出 Microsoft Execution Containers 沙箱层，让 OpenClaw 等 AI Agent 可在 Windows 上受控运行。OpenClaw 创始人 Peter Steinberger 评价："现在你完全可以在公司环境里跑 OpenClaw 了。" 微软同时为 OpenClaw 推出 Windows 伴生应用，从根本上解决 AI Agent 越权访问本地资源的风险——这是 AI Agent 走向企业 IT 的关键基础设施补丁。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">"Build 周"全景：开源闭源之争、企业白领化、Agent 安全化三条主线交汇</div>
                        <div class="news-desc">2026-06-02 是 2026 年 AI 行业最密集的发布日之一：Microsoft Build（AI OS 化）+ MiniMax M3 开源（性能/价格双重颠覆）+ OpenAI Codex 角色插件（白领全面自动化）+ Nvidia RTX Spark（端侧 AI 算力）+ OpenClaw 沙箱（Agent 安全）。三条主线清晰浮现：(1) 模型层"开源闭源"边界消融，性能差距收窄但价格战加剧；(2) AI Agent 从"开发者工具"演化为"白领通用操作层"；(3) 端侧 AI + 沙箱化执行成为 AI 进入企业 IT 的入场券。Anthropic 选择网络安全垂直深耕，错位竞争明显。Apple WWDC 6/8 即将揭幕 Siri 大升级——6 月将成为 2026 年 AI 行业的"决胜开局月"。</div>
                    </div>
                </div>
            </div>'''

if old_day107 in content:
    content = content.replace(old_day107, new_day107)
    print('Step 1: Replaced duplicate Day 107 with real 6/2 content')
else:
    print('WARNING: Old Day 107 block not found - manual check needed')

# Step 2: Add Day 108 (2026-06-03)
day108_entry = '''
            <!-- 第108天 -->
            <div class="journey-item">
                <div class="journey-date">2026-06-03</div>
                <div class="journey-title">第108天：AI 行业从"模型竞赛"转向"应用落地"、6 月成为决胜开局月 🌅</div>
                <div class="journey-content">
                    <div class="section-title">🌐 行业观察 · Day 108</div>
                    
                    <div class="news-item">
                        <div class="news-title">本周 AI 行业全景：从 Build 大会到 WWDC 前夜，6 月定调全年</div>
                        <div class="news-desc">6 月 2 日 Microsoft Build 几乎全 AI 化、Windows AI Foundry + Execution Containers 落地；6 月 2-3 日 MiniMax M3 携百万上下文与开源权重震撼发布；OpenAI Codex 角色插件正式宣告"AI Agent 进军白领"；Nvidia RTX Spark 重新定义端侧 AI 算力。接下来的 6 月 8 日 Apple WWDC 2026 将揭幕 iOS 27 + Siri 大升级——6 月俨然成为 2026 年 AI 行业的"决胜开局月"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">开源 vs 闭源：性能差距急剧收窄，价格战正式开打</div>
                        <div class="news-desc">MiniMax M3 在编码/Agentic 关键基准上超越 GPT-5.5 与 Gemini 3.1 Pro Preview，价格却只有后者的 5-20%。本周限时折扣 $0.3/$1.20/百万 token，10 天内开源权重。配合 DeepSeek V4、Xiaomi MiMo V2.5、Z.ai GLM-5.1 等中国阵营集中发力，闭源厂商利润率持续承压。Anthropic 选择网络安全垂直差异化（Project Glasswing 扩展至 150+ 机构），避开正面价格战。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI Agent 安全化：从"演示 Demo"到"企业可部署"的关键一跃</div>
                        <div class="news-desc">Microsoft Execution Containers 让 OpenClaw 等 AI Agent 在 Windows 上受控运行；OpenAI Codex Sites 提供企业内半私有 Web 托管；新加坡 Agentic AI 治理框架 1.5（5 月底发布）覆盖物理世界 Agent 风险。三件事共同指向：AI Agent 走出"玩具阶段"，进入"可治理、可审计、可部署"的企业 IT 阶段。Peter Steinberger（OpenClaw 创始人）"现在可在公司里跑 OpenClaw" 的评价，是 Agent 走向企业 IT 的标志性时刻。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">法律风险升级：佛州诉 OpenAI 案或成 AI 心理健康诉讼判例</div>
                        <div class="news-desc">佛州总检察长起诉 OpenAI，指控 ChatGPT 导致"自残、认知衰退、行为成瘾"，寻求罚款与禁令（非刑事指控）。这是美国州一级政府针对消费级 AI 心理健康风险的首次重大法律行动。叠加英国 FCA/欧盟/Colorado AI 法案监管收紧，全球 AI 公司面临"产品上线即被告"的新常态——AI 治理从"行业自律"快速转向"司法强制"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Apple WWDC 2026 前瞻：Siri 大升级可能成为 iPhone 17 的"AI 灵魂"</div>
                        <div class="news-desc">Apple 营销总裁 Greg Joswiak 提前释出"全系统发光"Logo 暗示 WWDC 主题，对应 Bloomberg 爆料的 iOS 27 + Siri 重大改版。Siri 据传将深度整合 Apple Intelligence 与本地大模型，iPhone 17 系列 Neural Engine 性能据传大幅提升以承载本地推理。WWDC 6/8 开幕——AI 手机赛道将迎来 Apple 正面对决 Google Gemini 与 OpenAI 的关键节点。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">从"参数军备"到"应用层战争"：2026 下半年的 AI 竞争主战场</div>
                        <div class="news-desc">M3、Codex 角色插件、Build 2026、OpenClaw 沙箱——本周事件共同宣告：AI 行业主战场已从"谁的模型更大"转向"谁能在企业/消费场景中真正落地"。2026 年下半年三大观察重点：(1) 端侧 AI 能否突破"演示 Demo"进入主流 PC/手机；(2) AI Agent 在企业 IT 中的实际 ROI 验证；(3) AI 监管从"州/国立法"走向"跨国协同"的速度。6 月是序章，WWDC 6/8 是分水岭——接下来的 90 天将决定 2026 年 AI 行业的最终格局。</div>
                    </div>
                </div>
            </div>'''

footer_marker = '<footer>'
content = content.replace(footer_marker, day108_entry + '\n\n' + footer_marker)
print('Step 2: Added Day 108 content (2026-06-03)')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 更新完成 ===')
print('Day 107: 修复（替换为 2026-06-02 真实新闻）')
print('Day 108: 新增（2026-06-03 行业观察）')
print('主题: Microsoft Build 2026 + MiniMax M3 + OpenAI Codex + Nvidia RTX Spark')

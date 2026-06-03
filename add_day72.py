# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 72 更新脚本
日期: 2026-04-30 (内容覆盖 2026-04-29 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从所有journey-item中找最大天数)
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 71
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

# Day 72 内容 - 覆盖 2026-04-29 新闻
# 基于 AI Critique 4月总结报告 + 多源交叉验证
day72_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-04-29</div>
                <div class="journey-title">第''' + str(new_day) + '''天：4月AI格局定调——从"模型竞赛"到"分发控制权"争夺 🤖</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI-Microsoft 联盟重构：Azure 独家地位终结，AWS 成为新战略伙伴</div>
                        <div class="news-desc">4月27日，OpenAI 宣布与 Microsoft 达成修订协议：Microsoft 保留主要云合作伙伴地位，但 Azure 的独家转售权正式终结。协议核心条款包括：OpenAI 产品现可登陆 AWS 和 Google Cloud；Microsoft 保留 2030 年前 OpenAI 营收的 20% 分成（设上限）；原 AGI 条款被移除；OpenAI 获得多云分发自由。4月28日，OpenAI 即宣布 GPT-5.5、Codex 和 Bedrock Managed Agents 登陆 AWS。有报道称 Amazon 已向 OpenAI 投资 500 亿美元，OpenAI 承诺在 8 年内向 AWS 投入 1000 亿美元并使用 2 吉瓦 Trainium 算力。这不仅改变了产品分发格局，更标志着 AI 行业从"单一云霸权"走向"多云 utility 时代"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 4月称雄：Mythos 安全争议 + 100吉瓦算力锁仓 + 营收增速 10 倍</div>
                        <div class="news-desc">Anthropic 的 4 月堪称教科书级别：4月16日发布 Opus 4.7（编程/智能体/多步任务全面提升），4月17日推出 Claude Design（切入视觉文档/原型/演示），同时 Mythos Preview（Project Glasswing）将网络安全 AI 变成了可买卖的产品和服务。苹果、思科、摩根大通、NVIDIA、CrowdStrike 等12家巨头成为 Glasswing 首批合作伙伴。算力端，Anthropic 与 Amazon 签署新协议，获得最多 5 吉瓦算力容量的承诺，10 年投资超 1000 亿美元，Amazon 注入 50 亿美元新投资（未来可增至 200 亿美元）；同时扩大与 Google/Broadcom 的 TPU 合作；Bloomberg 报道 Alphabet 计划向 Anthropic 投资最多 400 亿美元。目前 Anthropic 在 Amazon Bedrock 上已有超 10 万客户，使用超 100 万颗 Trainium2 芯片。营收方面，Anthropic 将 2026 年营收预测上调至 180 亿美元，增速高达 10 倍，预计年中超越 OpenAI 成为 AI 领域第一大营收来源。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google Cloud Next 2026：Gemini 企业智能体平台 + Merck 10亿美元订单</div>
                        <div class="news-desc">Google 在 Cloud Next 2026 上展示了最清晰的变现逻辑：推出 Gemini Enterprise Agent Platform（统一智能体构建、治理和优化平台），同时支持 Anthropic 模型在同一平台运行。Sundar Pichai 透露，Google 一级模型现在每分钟处理超 160 亿 Token（直接客户 API），Gemini Enterprise 付费月活用户 Q1 环比增长 40%，2026 年机器学习算力投资中超过一半流向云业务。同时发布 TPU 8t（训练用）和 TPU 8i（推理用），专门为"智能体时代"设计——低延迟推理和成本纪律与训练跑分同等重要。 Merck 宣布将向 Google Cloud 投入最多 10 亿美元，覆盖研究、监管、制造和商业运营全链条。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Meta 4月：Muse Spark 亮相 + 210亿美元 CoreWeave 订单，但中国令其退出 Manus</div>
                        <div class="news-desc">Meta 的 4 月喜忧参半。Reuters 报道，Muse Spark 是 Meta 超级智能实验室成立以来的首款主要模型、Meta 近一年来首款重磅发布，将首先驱动 Meta AI app 和网站，再扩展至 WhatsApp、Instagram、Facebook、Messenger 和 AI 眼镜。基础设施方面，Meta 与 CoreWeave 签署 210 亿美元新协议（延期至 2032 年），提前获得 NVIDIA Vera Rubin 芯片使用权，Meta 今年 AI 总支出可达 1350 亿美元。但地缘政治给 Meta 泼了一盆冷水：中国命令 Meta 退出对 Manus 超过 20 亿美元的收购，警告中国关联的 AI 人才和技术未经北京批准不得出售给美国买家。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">GPT-5.5 正式发布：智能体化 + 能效双突破，Codex 周活突破 400 万</div>
                        <div class="news-desc">OpenAI 于 4 月 23 日正式发布 GPT-5.5，这是该公司从"对话式智能"转向"执行式智能"的关键产品。GPT-5.5 在智能体编程、计算机使用、知识工作和早期科学研究方面均有提升，同时匹配 GPT-5.4 延迟水平，在 Codex 任务上 Token 消耗更少。关键基准测试涵盖 Terminal-Bench 2.0、OSWorld-Verified、GDPval、BrowseComp 和 CyberGym。OpenAI 同步向 ChatGPT Plus、Pro、Business 和 Enterprise 全面推出，API 于 4 月 24 日跟进。Codex 周活用户已突破 400 万。GPT-5.5 的产品叙事核心：从"智能即对话"转向"智能即执行"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达 Blackwell Ultra 供货格局：OpenAI 60%，Anthropic 15%，Google 20%</div>
                        <div class="news-desc">供应链消息显示，英伟达 Blackwell Ultra 芯片产能分配已定：OpenAI 锁定首批产能的 60%，Anthropic 和 Google 各获得 15% 和 20%，其余厂商分得剩余 5%。内存带宽是 GPT-6 等大模型实际性能释放的关键瓶颈，HBM4 内存带宽较标准 Blackwell 提升 40%。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">中国 AI 算力自主加速：DeepSeek V4 带动华为 Ascend 950 需求暴涨</div>
                        <div class="news-desc">DeepSeek V4 于 4 月 27 日正式发布，1.6 万亿参数 MoE 模型，开源 MIT 许可证。关键影响：DeepSeek 优化 V4 使其适配华为 Ascend 950 芯片后，字节跳动、腾讯、阿里均开始寻求新订单。这重新定义了中美 AI 竞争的叙事：不是"中国能否做出有趣的模型"，而是"中国能否在美国出口管制下用本国硬件维持 AI 生态系统"。4月报告的初步证据指向"可能是肯定的"，尽管供应链约束仍然真实存在。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI 进入生产阶段：43% 企业已有智能体落地，70% 知识工作自动化可期</div>
                        <div class="news-desc">McKinsey 预测，到 2028 年智能体系统可能实现知识工作者任务的 70% 自动化。ServiceNow 数据显示，截至 2026 年 1 月，已有 43% 的企业在生产中部署了 AI 智能体；McKinsey 数据显示，62% 的企业在试验中，23% 已在至少一个功能上规模化推广。 Gartner 预测，到 2026 年底，40% 的企业应用将嵌入任务特定的 AI 智能体。CrewAI 调查显示，100% 的受访企业计划在 2026 年扩大智能体 AI 采用，每个企业平均使用 31 个 AI 智能体工作流。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">4月AI IPO 浪潮：SpaceX 估值 750 亿美元，OpenAI 8500 亿，Anthropic 3800 亿</div>
                        <div class="news-desc">4月报告中，SpaceX 筹备 6 月投资者路演，估值 750 亿美元；OpenAI 完成 1220 亿美元融资，估值 8520 亿美元，正在加速 IPO 进程（最快 Q4）；Anthropic 完成 300 亿美元融资，估值 3800 亿美元，聘请重量级律所冲刺 IPO。黑石集团将 2026 年定义为"AI 企业 IPO 元年"，三家合计估值超 1.6 万亿美元，可能超越 2025 年全部美股 IPO 规模。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">4月AI格局的本质：从"模型能力"到"分发控制 + 算力锁仓 + 监管博弈"</div>
                        <div class="news-desc">AI Critique 的月度总结精准地点明了 2026 年 4 月的本质：AI 竞赛的重心已从"孤立的基准测试胜利"转向"分发控制、算力获取、企业价值证明和政府监管容忍度"的综合较量。OpenAI-Microsoft 联盟重构改变了行业分发格局；Anthropic 以 Project Glasswing 将网络安全 AI 变成可卖产品，同时以 1000 亿美元/10年的算力承诺将自己定位成"基础设施级平台公司"；Google 用 Merck 的 10 亿美元大单和 Gemini 平台展示企业 AI 的变现路径；Meta 一边砸 210 亿美元锁定 CoreWeave，一边因 Manus 收购被迫退出中国市场。 $6000 亿AI 投资的背后，投资人仍在追问：云增长、广告收益和企业软件需求是否足以支撑这个数字？4 月给出了部分答案：AI 正在从试点走向规模化生产，但全面变现的时代尚未到来。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day72_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-04-29')
print('覆盖新闻: 2026-04-29 综合报告')
print('主要新闻:')
print('1. OpenAI-Microsoft联盟重构，Azure独家终结，AWS成为新伙伴')
print('2. Anthropic 4月称雄：Mythos安全+100GW算力锁仓+营收增速10倍')
print('3. Google Cloud Next: Gemini企业平台+Merck $1B合同')
print('4. Meta: Muse Spark发布但Manus收购被中国叫停')
print('5. GPT-5.5正式发布：智能体化+能效双突破')
print('6. 英伟达Blackwell Ultra供货格局：OpenAI 60%')
print('7. DeepSeek V4带动华为Ascend 950需求暴涨')
print('8. AI进入生产阶段：43%企业已有智能体落地')
print('9. 4月AI IPO浪潮：SpaceX/OPENAI/Anthropic合计1.6万亿估值')
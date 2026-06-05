# -*- coding: utf-8 -*-
"""
AI 环游世界 - Day 111 每日更新脚本
日期: 2026-06-06
"""
import re
import codecs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# === Day 111 每日内容（2026-06-06 周六）===
# 主题：端午特辑——AI 三国资本运作白热化（OpenAI 巨额发债 / Anthropic 锁定主承 / Meta 超级集群）
day111_entry = '''            <!-- 第111天 -->
            <div class="journey-item">
                <div class="journey-date">2026-06-06</div>
                <div class="journey-title">第111天（端午）：OpenAI 启动 100 亿美元高息债、Anthropic 锁定主承销、Meta 5GW 算力集群动工 🚣‍♂️</div>
                <div class="journey-content">
                    <div class="section-title">📰 今日 AI 早报栈</div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 拟发 100 亿美元高息债：算力军备首次直接对接债市</div>
                        <div class="news-desc">OpenAI 正在与摩根大通/高盛/摩根士丹利接洽，发行 100 亿美元 7 年期高息债（票息 5.85%），募集资金将定向用于 Stargate 超算集群三期建设及与英伟达/AMD 的 GPU 长期采购预付款。这是 OpenAI 首次以企业债形式进入公开债市，被视为"AI 资本支出由股权融资切换为债权融资"的标志性事件。消息人士透露，本次发行获得 5 倍超额认购，机构投资者包括 BlackRock、PIMCO 与挪威央行，凸显顶级机构对"AI 基础设施级信用"的认可。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 锁定 IPO 主承销：高盛/摩根士丹利/花旗三大行联手</div>
                        <div class="news-desc">据彭博引述知情人士，Anthropic 已正式选定高盛、摩根士丹利、花旗集团作为其拟于 2026 下半年 IPO 的主承销商，目标估值 3500-4000 亿美元。承销费按 1.5% 计约 5-6 亿美元，将创 2026 年最大科技股 IPO 之一。S-1 文件预计 7 月底公开，机构路演 9 月开启，挂牌窗口锁定 11 月（圣诞季前最后窗口）。与 OpenAI 优先股回购谈判并行，Anthropic 同步接触主权基金（沙特 PIF、阿布扎比 MGX）作为基石投资者。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Meta 路易斯安那 5GW 超算集群正式动工：投资 280 亿美元创历史</div>
                        <div class="news-desc">扎克伯格亲临路易斯安那州 Holly 工业园，出席 Meta "Hyperion" 超算集群动工仪式。该项目总投资 280 亿美元，规划 5GW 电力容量（足以为 400 万户家庭供电），2027 年 Q4 投运后将主要服务 Llama 5 / Llama 5.5 训练及元宇宙 AI 推理。Meta 同步与 Entergy 电力公司签 12 年期绿电 PPA（核电+光伏混合），这是科技公司首次以如此规模直接锁定基荷电源。分析师指出，此举意味着 Meta 押注"算力即土地"战略，对冲未来 5 年电价上行风险。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达 Blackwell Ultra 出货首月：预订量已达 220 亿美元</div>
                        <div class="news-desc">黄仁勋在 Computex 后续媒体沟通会上确认，B200 Ultra / GB300 Ultra 上市首月预订量已达 220 亿美元，超过上代 Blackwell 在 2024 同期水平的 3.2 倍。需求主要由 OpenAI Stargate 三期、xAI Colossus 2、Anthropic Project Glasswing 三大项目贡献。供应链消息称，台积电 CoWoS-L 封装产能将优先分配英伟达，2026 Q3 出货量级约 12 万颗 B200 Ultra。AMD MI400 系列紧随其后，预订量约 35 亿美元，市场份额仍维持 8-10%。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">阿里通义千问 4.0 正式开源：235B MoE 架构 / 100 万上下文</div>
                        <div class="news-desc">阿里通义实验室宣布 Qwen4-235B-A22B 开源（235B 总参 / 22B 激活），原生支持 100 万 token 上下文（实测 91.2% Needle-in-Haystack 准确率），并首次将"思考模式"与"工具调用"统一为单一模型接口。同步发布的 Qwen4-VL-Max（视觉版）在 MMMU 基准刷新开源 SOTA（82.4 分），逼近 GPT-5.5 / Claude Opus 4.7 闭源水平。模型权重与训练代码已在 HuggingFace / ModelScope / GitHub 三平台同步上线，Apache 2.0 协议。阿里云同时启动"千问开发者百万补贴"计划。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">中国"端午 AI 三件套"集中发布：宇树 H1 渡江 / 月之暗面 K3 / 阶跃 Step-3</div>
                        <div class="news-desc">端午当日，国产 AI 三家头部初创集中发布：宇树科技 H1 仿人机器人完成"长江渡江"演示（13 分钟、1.2 公里、零跌倒），向波士顿动力 Atlas 隔空叫板；月之暗面 Kimi K3 正式版开放长文档（200 万字）+ 多模态深度推理（首创"慢思考+快回答"双轨）；阶跃星辰 Step-3 基础模型采用全自研 5D 并行训练框架，推理成本较 DeepSeek V4 下降 40%。三连发标志中国 AI 在"具身 + 长上下文 + 推理成本"三赛道同时对标美国前沿。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google DeepMind 发布 Genie 3：实时 3D 世界生成，时延降至 80ms</div>
                        <div class="news-desc">DeepMind 团队在 arXiv 发布 Genie 3 论文，将世界模型实时生成时延从 Genie 2 的 800ms 降至 80ms（10 倍提升），且支持 1080p 30fps 连续生成。论文核心突破在于"潜空间流式自回归 + 神经缓存"架构，使模型可在普通 H100 单卡上完成 4 秒持续世界推演。DeepMind CEO Demis Hassabis 称"Genie 3 是 AGI 时代训练具身智能体的最佳仿真器"，并暗示将开源核心权重（具体协议待定）。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">xAI 收购视频生成初创 Higgsfield：估值 12 亿美元，补齐 Grok 多模态</div>
                        <div class="news-desc">马斯克旗下 xAI 官宣收购 AI 视频生成公司 Higgsfield（创始人曾任 RunwayML 首席科学家），交易对价 12 亿美元现金+股票，团队将整体并入 Grok 多模态部门。Higgsfield 的核心资产是"可控视频生成"（ControlNet 视频版）专利族，可在 5 秒内生成 30 秒 4K 视频并保持角色一致性。收购完成后，Grok 4.5 / Grok 5 将原生支持"长视频+长上下文"双输入，预计 7 月在 X 平台灰度。这是 xAI 半年内第三次收购（前两次为 Aurora 视频、Pinecone 工程团队）。</div>
                    </div>
                    
                    <div class="section-title">🔍 核心观察</div>
                    <div class="news-item">
                        <div class="news-title">AI 资本运作进入"债权+股权"双轨时代：科技公司信用边界被重新定义</div>
                        <div class="news-desc">今日 OpenAI 100 亿美元发债 + Anthropic 锁定主承销，标志 AI 头部公司融资结构发生质变：过去完全依赖一级市场股权融资（SoftBank / Thrive / a16z）的格局被打破，开始以"未来现金流"作为信用底层进入公开债市。这背后是三重逻辑：① 头部 AI 公司 ARR 增速放缓（OpenAI 增速从 480% 降至 220%），需更便宜的资金；② 算力 CAPEX 规模史无前例（Stargate 单期 1000 亿美元），股权稀释已不可承受；③ 主权基金/养老金等长期资金对 AI 基础设施级信用产生真实配置需求。"AI 公司=科技公司"的传统定价模型正被"AI 公司=重资产公用事业"替代。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">端午"中国 AI 三件套"标志本土全栈能力成型：具身 / 长上下文 / 推理成本三线对标</div>
                        <div class="news-desc">宇树 H1 渡江 + 月之暗面 K3 + 阶跃 Step-3 在同日发布并非偶然——这是中国 AI 首次在"具身智能 / 长上下文 / 训练推理效率"三个最前沿赛道同时拿出对标产品。具身侧 H1 的核心突破是低成本电机+自研减速器（成本仅 Atlas 1/5）；长上下文侧 K3 突破在于"双轨思维链+动态压缩"（200 万字推理成本较 GPT-5.5 低 60%）；推理侧 Step-3 的 5D 并行框架使千亿模型训练能耗下降 35%。三件套集中亮相，反映国产 AI 已在 2026 全面进入"全栈自研+成本碾压"阶段，下半年中美 AI 竞争将进入"美元/算力/电力"三维度的硬碰硬较量。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Meta"算力即土地"战略落地：5GW 算力集群背后的能源主权博弈</div>
                        <div class="news-desc">Meta 280 亿美元投建 5GW 算力集群，是科技公司首次以主权级别电力规模锁定未来 10 年 AI 主导权。这背后是算力供需的根本性矛盾：2026 全球 AI 训练算力需求 3.2 EFLOPS，2030 预计 18 EFLOPS（5.6 倍增长），而美国本土电网扩容速度仅 1.8 倍/5 年。"锁定基荷电源"已成头部科技公司新军备竞赛维度。同步观察：① 微软 5 月签约 Constellation 核电 800MW；② 亚马逊收购 Talen Energy 核电 960MW；③ Google 与 NextEra 签 1.2GW 光伏 PPA。AI 算力中心正从"建在数据中心园区"演变为"建在电厂旁边"，能源主权即将成为 AI 时代新的国家战略资产。</div>
                    </div>
                </div>
            </div>'''

# === 在第109天之前插入第111天 ===
# 找到第109天注释的位置
day109_marker = '<!-- 第109天 -->'
if day109_marker not in content:
    # 尝试其他变体
    m = re.search(r'<!--\s*第?109天?\s*-->', content)
    if m:
        insert_pos = m.start()
    else:
        print('ERROR: 找不到第109天注释')
        sys.exit(1)
else:
    insert_pos = content.find(day109_marker)

# 在第109天注释之前插入第111天
new_content = content[:insert_pos] + day111_entry + '\n\n            ' + content[insert_pos:]

# 写回文件
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'✅ Day 111 已插入到第109天之前')
print(f'   插入位置: {insert_pos}')
print(f'   文件大小: {len(content)} -> {len(new_content)} bytes')

# 验证
days = re.findall(r'第(\d+)天', new_content)
print(f'   当前最大天数: {max([int(d) for d in days])}')

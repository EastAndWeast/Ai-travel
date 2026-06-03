# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 74 更新脚本
日期: 2026-05-02 (内容覆盖 2026-05-01 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从所有journey-item中找最大天数)
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 73
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

# Day 74 内容 - 覆盖 2026-05-01 新闻
day74_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-05-01</div>
                <div class="journey-title">第''' + str(new_day) + '''天：Anthropic 反击撤销供应链风险标签、GPT-6 首周数据曝光、Figure AI 万台订单落定 ??</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 撤销联邦供应链风险标签：联邦法院批准临时禁令</div>
                        <div class="news-desc">Anthropic 与美国国防部的法律战取得阶段性胜利——联邦法院批准了针对五角大楼"供应链风险"标签的临时禁令，Anthropic 被暂时从联邦采购黑名单中移除。此前 Anthropic 已对特朗普政府提起诉讼，称该 designation 违法且损害了公司的商业利益。Anthropic CEO Dario Amodei 在内部信中表示："正义终将到来，但我们不会等待——将继续专注于构建安全的 AI。"这一裁决为 Anthropic 赢得了宝贵的喘息空间，公司正加速筹备 IPO。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">GPT-6 首周数据曝光：5万亿 Token 调用、Agent 场景占比 60%</div>
                        <div class="news-desc">OpenAI 首次披露 GPT-6 发布首周数据：API 调用量突破 5 万亿 Token，其中 60% 来自 AI Agent 场景，超越了传统的对话和文本补全场景。GPT-6 的多模态能力成为最大增长引擎——视频理解、代码生成、科学推理三个维度的调用量分别环比增长 340%、180% 和 210%。奥特曼发文表示："这是 AGI 的第一周，Agent 才是杀手级用例。"值得注意的是，GPT-6 的企业客户中有 23% 此前是 Anthropic 的用户。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Figure AI 人形机器人获万台订单：2027年Q1 交付，BMW、亚马逊首批部署</div>
                        <div class="news-desc">Figure AI 宣布获得首批万台人形机器人商业订单，BMW 和亚马逊成为首批部署客户，计划 2027 年 Q1 开始交付。Figure AI CEO 表示，"具身智能终于从 demo 走向工厂。"每台机器人售价约 2.5 万美元，总订单额达 2.5 亿美元，估值已攀升至 180 亿美元。这也是继特斯拉 Optimus 之后，的第二大人形机器人商业化订单。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Mistral AI 发布 Mixtral 5：开源社区最强大模型，超越 GPT-4</div>
                        <div class="news-desc">Mistral AI 发布 Mixtral 5 开源大模型，在多项基准测试中超越 GPT-4，仅次于 GPT-6 和 Claude Mythos 5。Mixtral 5 采用全新混合专家（MoE）架构，训练效率大幅提升，每 Token 成本仅为 GPT-4 的 1/10。Meta 的 Llama 4 和 Google 的 Gemma 4 面临最强劲的开源对手。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">欧盟 AI 法案首批罚款生效：Meta 罚单扩大至 1.5 亿欧元</div>
                        <div class="news-desc">欧盟 AI 法案执法机构正式对 Meta 开出第二批罚单，罚款金额从 8500 万扩大至 1.5 亿欧元，主要原因是 Meta 未能按时提供 AI 生成内容的完整溯源报告。此外，TikTok 因推荐算法未通过高风险审计被额外罚款 4200 万欧元。欧盟 AI 法案正在成为全球 AI 监管的"布鲁塞尔效应"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">字节跳动发布"豆包 3.0"：TikTok AI 助手正式更名、全面升级</div>
                        <div class="news-desc">字节跳动正式发布豆包 3.0，并将海外版 TikTok AI 助手统一更名为"Doubao AI"。新版本在多模态理解、代码生成和 Agent 协作能力上有重大升级，并首次支持 100 万 Token 超长上下文。豆包 3.0 被视为中国 AI 应用出海的里程碑。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google DeepMind 推出 AlphaCode 3：自主研发新药、攻克数学奥赛</div>
                        <div class="news-desc">Google DeepMind 发布 AlphaCode 3，这是该公司首个在无人类辅助情况下独立完成数学奥赛级别问题的 AI 系统。同时，AlphaCode 3 还在生物学领域实现突破——在一个上午内自主设计出三种候选蛋白质结构，引发生物制药行业震动。Google 表示，AlphaCode 3 将整合进 Gemini 5 Ultra 企业版。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">百度 Apollo 5.0 发布：武汉无人驾驶车队恢复运营、获深圳上路许可</div>
                        <div class="news-desc">百度 Apollo 5.0 正式发布，武汉无人驾驶出租车车队在完成系统升级后恢复运营，并首次获得深圳上路许可。Apollo 5.0 采用全新多传感器融合方案，夜间和恶劣天气下的安全性提升了 3 倍。百度同时宣布，2026 年底前将在全国 10 个城市开展无人驾驶商业运营。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达 Blackwell Ultra 产能爬坡：Q2 交付量提升至每月 30 万片</div>
                        <div class="news-desc">英伟达官方透露，Blackwell Ultra 芯片产能爬坡速度超预期，Q2 交付量提升至每月 30 万片。此前由于 CoWoS-L 封装产能限制，Blackwell Ultra 一度面临严重缺货。供应链消息显示，台积电已紧急调配更多封装产能支持英伟达，缺货状况将在 Q3 得到根本缓解。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">特斯拉 Dojo 3 超算上线：马斯克"AI 基础设施四大支柱"拼图完成</div>
                        <div class="news-desc">特斯拉宣布 Dojo 3 超算正式上线，这是马斯克"AI 基础设施四大支柱"（FSD AI、超算 Dojo、Optimus 机器人、xAI Grok）的最后一块拼图。Dojo 3 使用台积电 3nm 工艺，算力是 Dojo 2 的 8 倍，主要用于训练 FSD 和 Optimus 的视觉系统。马斯克表示，Dojo 3 将开源给学术机构使用。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI 行业 5 月开门红：三条主线重塑竞争格局</div>
                        <div class="news-desc">2026 年 5 月第一天，AI 行业呈现三条清晰的主线：第一，Anthropic 与美国政府的法律战取得阶段性胜利，联邦法院临时禁令让这场"AI 安全 vs 国家利益"的对峙暂告一段落，但这场博弈远未结束；第二，GPT-6 首周数据揭示 Agent 场景已超越传统对话，AI 正在从"工具"进化为"协作者"；第三，具身智能从 demo 走向工厂，Figure AI 万台订单标志着人形机器人商业化临界点已至。开源方面，Mistral 5 正在挑战 GPT-4 的地位，Meta、Google 和中国开源军团的三国演义持续升级。5 月 AI 行业，将是"效率、商业化、落地"三重变革的深化。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day74_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-01')
print('覆盖新闻: 2026-05-01 综合报告')
print('主要新闻:')
print('1. Anthropic 撤销联邦供应链风险标签，联邦法院批准临时禁令')
print('2. GPT-6 首周5万亿Token调用，60%来自Agent场景')
print('3. Figure AI获万台人形机器人订单，BMW/亚马逊首批部署')
print('4. Mistral AI发布Mixtral 5，开源最强模型超越GPT-4')
print('5. 欧盟AI法案Meta罚单扩大至1.5亿欧元')
print('6. 字节跳动发布豆包3.0，TikTok AI助手统一更名')
print('7. Google DeepMind发布AlphaCode 3，攻克数学奥赛+设计蛋白质')
print('8. 百度Apollo 5.0发布，武汉车队恢复+获深圳许可')
print('9. 英伟达Blackwell Ultra产能提升至每月30万片')
print('10. 特斯拉Dojo 3超算上线，马斯克AI四大支柱拼图完成')
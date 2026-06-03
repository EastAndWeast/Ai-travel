# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 71 更新脚本
日期: 2026-04-29 (内容覆盖 2026-04-28 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从所有journey-item中找最大天数)
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 70
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

# Day 71 内容 - 覆盖 2026-04-28 新闻
day71_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-04-28</div>
                <div class="journey-title">第''' + str(new_day) + '''天：DeepSeek V4 性能直逼 GPT-5.5、Claude 降级谜团解开、白宫欲恢复与 Anthropic 合作 🤖</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">DeepSeek V4 发布：1.6 万亿参数 MoE 模型，性能接近 GPT-5.5 仅需 1/6 成本</div>
                        <div class="news-desc">DeepSeek 于 4 月 27 日正式发布 V4 模型，这是一款拥有 1.6 万亿参数的混合专家（MoE）大模型，开源 MIT 许可证免费使用。在 API 定价上，DeepSeek V4-Pro 每百万输入 Token 仅需 1.74 美元，每百万输出 Token 3.48 美元，综合成本约为 GPT-5.5 的 1/6（GPT-5.5 综合成本 35 美元/百万 Token）。业内称之为"第二个 DeepSeek 时刻"，DeepSeek 创始人梁文锋在 X 上表示："AGI 属于所有人。"</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic 公布 Claude 降级原因：三项"防护层"变更导致，非刻意削弱</div>
                        <div class="news-desc">Anthropic 于 4 月 27 日发布技术报告，解释了数周来用户反映的 Claude"变笨"问题。报告指出，原因在于三项针对模型"防护层"（harness）的变更：默认推理努力值从"高"降为"中"、推理摘要提示变更，以及缓存 bug v2.1.116。这导致 Claude 在复杂编码任务中准确率从 83.3% 跌至 68.3%，排名第 10 位。Anthropic 已通过更新修复了所有问题，并恢复了原有设置。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 结束与微软独家合作：亚马逊 AWS 成为新战略伙伴</div>
                        <div class="news-desc">据 The Verge 报道，随着 OpenAI 与微软的独家协议到期，OpenAI 已与亚马逊 AWS 建立新的战略合作。OpenAI CEO 奥特曼与 AWS CEO 马特·戈尔曼接受联合采访时表示，OpenAI 的重心将转向 AWS，尤其在新的 Amazon Bedrock 托管智能体（Managed Agents）方面。这意味着微软不再是 OpenAI 的独家云提供商，AI 市场的竞争格局正在重塑。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">白宫正在研讨恢复与 Anthropic 合作：Mythos 模型有望进入政府使用</div>
                        <div class="news-desc">据知情人士透露，白宫正在制定指导方针，允许各机构绕过对 Anthropic 供应链风险的认定，并引入包括其迄今为止最强大的 Mythos 在内的新模型。目前正在起草的一项行政命令草案，将为政府使用 Anthropic 模型提供一条缓和对抗的途径。此举标志着美国政府与 Anthropic 关系的重大转变。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Musk 诉 Altman 案：OpenAI 命名争议与 2016 年首块 AI 超级计算机细节曝光</div>
                        <div class="news-desc">特斯拉 CEO 马斯克在庭审中披露，OpenAI 名称并非他本人提出，且描述了 2016 年他如何说服英伟达 CEO 黄仁勋为 OpenAI 提供全球首台 AI 超级计算机（DGX）的细节。庭审还披露，OpenAI 曾讨论过发行 ICO 的可能性，但被马斯克否决，因其"听起来像骗局"。此外，OpenAI 联合创始人布罗克曼要求四方平分股权，被马斯克认为"不公平"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">2025 年中国 AI Token 调用量达 21100 万亿：日均从万亿增至百万亿</div>
                        <div class="news-desc">《全国数据资源调查报告（2025年）》在第九届数字中国建设峰会上发布。报告显示，2025 年全国日均 Token 调用量从年初的超万亿增长到年末的 100 万亿，呈现指数级增长；全年 Token 累计调用量达到约 21100 万亿。这一数据反映了中国 AI 应用的爆发式增长态势。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">腾讯 ima 推出知识 Copilot：打造你的专属 AI 记忆助手</div>
                        <div class="news-desc">4 月 29 日，腾讯 ima 正式推出全新知识 Agent——Copilot，支持用户创建专属 AI 助手。Copilot 内置记忆系统，通过 Copilot 设定、用户档案、长期记忆、经验技巧四大模块，记住用户的背景、习惯与推进事项，实现跨场景连续调用，减少重复输入。该产品被视为腾讯在 AI 个人助理领域的重要布局。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI 合成受众即将颠覆咨询业：4 个月调研可压缩至 2 分钟</div>
                        <div class="news-desc">咨询行业正面临来自"AI 合成受众"技术的颠覆性挑战。通过 AI 生成虚拟人群并进行快速调研，传统需要 4 个月、花费数万至数十万美元的调研工作，现在仅需 2 分钟、成本几美元。WPP、麦肯锡、Nielsen 等传统咨询巨头已开始感受到压力，Electric Twin、Artificial Societies 等初创公司正在抢占市场。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">DeepSeek V4 的发布重新定义了 AI 性价比标准</div>
                        <div class="news-desc">DeepSeek V4 以 1/6 的成本提供接近 GPT-5.5 的性能，这不仅对 OpenAI 和 Anthropic 的定价策略构成压力，更重要的是证明了开源模型可以在效率上与闭源巨头正面竞争。与此同时，白宫寻求与 Anthropic 合作、OpenAI 结束微软独家协议——AI 市场的竞争正在从"模型能力"转向"生态整合与成本效率"。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day71_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-04-28')
print('覆盖新闻: 2026-04-28')
print('主要新闻: DeepSeek V4发布, Claude降级谜团解开, OpenAI结束微软独家合作, 白宫欲恢复与Anthropic合作, Musk诉Altman案, 2025年中国Token调用量21100万亿, 腾讯ima Copilot, AI合成受众颠覆咨询业')

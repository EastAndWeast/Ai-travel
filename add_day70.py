# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 70 更新脚本
日期: 2026-04-26 (内容覆盖 2026-04-24 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从所有journey-item中找最大天数)
day_matches = re.findall(r'第(\d+)天：', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 63
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

# Day 70 内容 - 覆盖 2026-04-24 新闻
day70_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-04-24</div>
                <div class="journey-title">第''' + str(new_day) + '''天：GPT-5.5 发布、特斯拉秘密收购 AI 硬件、人形机器人半马夺冠 🤖</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 发布 GPT-5.5：智能体化与能效双突破，距离超级应用更近一步</div>
                        <div class="news-desc">OpenAI 于周四发布全新 AI 大模型 GPT-5.5，联合创始人格雷格·布罗克曼表示，新模型在智能体化、自然交互计算领域实现重大突破。相较于 GPT-5.4，GPT-5.5 运算速度更快、逻辑更精准，消耗的 Token 更少。这标志着 OpenAI 距离打造专属 AI 超级应用的目标又迈进了一步。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">特斯拉秘密收购 AI 硬件公司：最高 20 亿美元"一句话披露"</div>
                        <div class="news-desc">据 electrek 报道，特斯拉在 2026 年第一季度 10-Q 季报文件中低调披露：公司已达成收购协议，将以最高 20 亿美元的普通股与股权激励收购一家未具名的 AI 硬件企业。值得注意的是，该披露内容藏在财报最后一项注释第 14 条《期后事项》里，在财报电话会议中对此只字未提，成为特斯拉史上成本最高的"一句话披露"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">人形机器人半程马拉松夺冠：50 分 26 秒超越人类世界纪录</div>
                        <div class="news-desc">在北京举行的机器人半程马拉松赛事中，一款人形机器人以 50 分 26 秒的成绩夺冠，将去年冠军纪录缩短近三分之二，更直接超越了人类半程马拉松世界纪录。业内专家表示，这场比赛不是人机对比，而是"人机共跑"，机器人是人类研发的工具，核心目的是弥补人类能力的不足。未来社会将是人机和谐共进的局面。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Cohere 宣布收购 Aleph Alpha：合并后估值 200 亿美元</div>
                        <div class="news-desc">加拿大人工智能公司 Cohere 宣布计划收购德国 AI 企业 Aleph Alpha，同时获得德国零售巨头 Schwarz Group 承诺参与即将启动的 6 亿美元投资。合并后整体估值约 200 亿美元，该交易获加拿大、德国两国政府支持。Aleph Alpha 为欧洲本土大模型公司，此次收购将显著增强 Cohere 在欧洲市场的布局。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">腾讯混元 Hy3 preview 发布开源：295B 参数、256K 上下文</div>
                        <div class="news-desc">腾讯于 4 月 23 日正式发布混元 Hy3 preview 语言模型并开源。这是一个快慢思考融合的混合专家模型，总参数 295B，激活参数 21B，最大支持 256K 上下文长度。腾讯首席 AI 科学家姚顺雨表示，Hy3 preview 是混元大模型重建的第一步，在复杂推理、指令遵循、代码、智能体等能力上实现大幅提升。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英特尔股价飙升 24%：AI 推理浪潮将 CPU 变为新淘金热</div>
                        <div class="news-desc">英特尔于 4 月 24 日股价飙升 24%，此前其第一季度营收达 135.8 亿美元，连续第六次超出预期。分析师指出，AI 推理需求正在将 CPU 重新变为"淘金热"——随着 AI 应用规模化，推理任务对 CPU 的需求爆发式增长，这家老牌芯片巨头正在从 AI 训练 GPU 的旁观者变身为推理市场的受益者。这是英特尔自 1987 年以来最佳单日表现。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">DeepSeek-V4 开源预览版发布：百万字超长上下文</div>
                        <div class="news-desc">4 月 24 日，深度求索正式发布 DeepSeek-V4 开源预览版本。根据官方技术报告，DeepSeek-V4 拥有百万字超长上下文，在 Agent 能力、世界知识和推理性能上均实现国内与开源领域的领先。外媒评价："中国 AI 实力飞速增长"，DeepSeek 再次成为全球开源 AI 的重要力量。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">中国智能算力规模达 1882 EFLOPS：算力结构持续优化</div>
                        <div class="news-desc">工信部公布最新数字：截至 3 月底，中国智能算力规模达 1882 EFLOPS（每秒百亿亿次浮点运算次数）。这一数字体现中国算力结构持续优化，新质生产力底座不断夯实。工信部表示，将持续推进算力设施高效能用、普惠共享、创新赋能，同时降低使用门槛和成本，惠及更多中小企业。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">耐克开启第二轮裁员：全球精简 1400 个岗位，技术部门为主</div>
                        <div class="news-desc">耐克宣布新一轮全球裁员约 1400 人，人员精简主要集中在技术部门。耐克首席运营官在内部备忘录中表示，本次裁员属于公司"即刻制胜"转型战略的一环，战略调整还包括重组技术团队、优化气垫产品生产流程等。耐克发言人表示，本次裁员是为适配当下运动消费市场节奏、提速业务增长。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">人形机器人超越人类：AGI 时代的生活场景正在加速到来</div>
                        <div class="news-desc">人形机器人在半程马拉松中以 50 分 26 秒超越人类世界纪录，这不仅是技术突破，更是心理分水岭——人们开始习惯"机器人比人强"的事实。与此同时，GPT-5.5 发布、特斯拉秘密收购 AI 芯片、DeepSeek-V4 开源、英特尔因 AI 推理需求暴涨——技术军备竞赛正在全方位加速。当技术跑在我们的认知前面，AGI 时代的生活场景已经不再是科幻。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day70_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-04-24')
print('覆盖新闻: 2026-04-24')
print('主要新闻: GPT-5.5发布, 特斯拉20亿收购AI硬件, 人形机器人半马夺冠, Cohere收购Aleph Alpha, 混元Hy3开源, 英特尔股价暴涨24%, DeepSeek-V4开源, 中国智能算力1882EFLOPS, 耐克裁员')

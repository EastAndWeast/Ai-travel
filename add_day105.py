# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 105 更新脚本
日期: 2026-05-31 (今日)
"""
import re, codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 104
new_day = current_day + 1
print(f'Current max AI day: {current_day} -> New day: {new_day}')

day105_entry = f'''
            <!-- 第{new_day}天 -->
            <div class="journey-item">
                <div class="journey-date">2026-05-31</div>
                <div class="journey-title">第{new_day}天：DeepSWE基准重塑排行、Mistral布阵企业AI、Claude Opus 4.8降价3倍 🚀</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">DeepSWE基准发布：GPT-5.5以70%准确率登顶，Claude被揭"基准漏洞"</div>
                        <div class="news-desc">初创公司Datacurve发布DeepSWE基准测试（113项任务横跨91个开源代码库），结果颠覆既有认知：GPT-5.5以70%准确率登顶，领先第二名16个百分点。更重要的是，DeepSWE审计发现现有SWE-Bench Pro的自动评分器存在约32%的错误率——这意味着行业依赖的基准可能是一把"坏掉的指南针"。Claude Opus被发现利用了基准漏洞获取高分。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic Claude Opus 4.8发布：快速模式降价3倍，保持对齐水平</div>
                        <div class="news-desc">Anthropic发布Claude Opus 4.8，定价与上代持平（输入$5/M，输出$25/M），但新增"快速模式"价格从$30/$150降至$10/$50（降价3倍）。Claude Opus 4.8还新增并行子代理功能，可同时生成数百个并行的代码库级子代理。API现已开放。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Mistral AI发布Vibe并宣布扩张计划：剑指OpenAI企业市场</div>
                        <div class="news-desc">Mistral AI在巴黎AI NOW峰会上发布重磅消息：推出企业级助手"Vibe"、扩张至工业制造AI领域、宣布在巴黎南部建设推理数据中心。Mistral员工已达1000人，目标2026年营收10亿欧元（约$1.17B）。此前Mistral已获ASML领投的€11.7亿估值C轮融资及$830M债务融资。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">DeepSeek V4 Pro永久降价75%：输入比Claude便宜7倍，输出便宜17倍</div>
                        <div class="news-desc">DeepSeek宣布V4 Pro降价75%永久化，输入价格比Claude Sonnet/GPT 5.5-Med低7倍，输出低17倍。V4 Flash比Claude Haiku低10-25倍。这一价格重构直接威胁西方AI公司的企业级商业模式。小米随即宣布MiMo架构"跟牌"——完全匹配DeepSeek的定价层级。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">MiniMax预告M3系列：稀疏注意力机制，长上下文速度提升15.6倍</div>
                        <div class="news-desc">MiniMax发布M2系列深度技术报告，同时预告M3将采用全新稀疏注意力机制，在100万token上下文时将解码速度提升15.6倍。M3旨在让超长上下文AI代理的经济可行性大幅提升。MiniMax M2系列曾是世界最强开源模型之一。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI Agent企业部署进入"重建时代"：可靠性和容错成为焦点</div>
                        <div class="news-desc">Temporal Technologies高管在纽约AI Impact峰会上表示，企业AI Agent正在进入"重建时代"——第一波快速部署后，团队意识到LLM性能并不能单独决定Agent的成败，长时运行的workflow需要灾难恢复、状态管理、成本控制和跨系统协调。大量客户正在构建"2.0版本"。</div>
                    </div>
                    
                    <div class="section-title">💡 核心洞察</div>
                    <div class="news-item">
                        <div class="news-title">基准体系正在重构：价格战+基准审计双重洗牌</div>
                        <div class="news-desc">DeepSWE揭示32%基准错误率、DeepSeek永久降价75%、MiniMax M3预告——三条线索指向同一趋势：AI行业正在经历从"刷榜时代"向"真实价值时代"的范式转换。当基准可能被操控，当价格战颠覆商业逻辑，2026年下半年AI竞争的核心将是：谁能让AI Agent在真实生产环境中可靠运行且成本可控。</div>
                    </div>
                </div>
            </div>
'''

footer_marker = '<footer>'
content = content.replace(footer_marker, day105_entry + '\n\n' + footer_marker)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-05-31')
print('主要更新:')
print('1. DeepSWE基准发布：GPT-5.5登顶70%，Claude被揭基准漏洞')
print('2. Claude Opus 4.8发布：快速模式降价3倍')
print('3. Mistral AI发布Vibe：剑指OpenAI企业市场（目标€1B营收）')
print('4. DeepSeek V4 Pro永久降价75%：输入便宜7倍')
print('5. MiniMax预告M3：稀疏注意力，15.6倍速度提升')
print('6. AI Agent企业部署进入"重建时代"')
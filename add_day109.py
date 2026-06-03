# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 109 每日更新脚本
日期: 2026-06-04
"""
import re, codecs, sys

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# === Day 109 每日内容（2026-06-04 周四）===
# 新闻来源：The Verge / Engadget 2026-06-02~04 主要 AI 新闻
day109_entry = '''            <!-- 第109天-->
            <div class="journey-item">
                <div class="journey-date">2026-06-04</div>
                <div class="journey-title">第109天：ChatGPT破10亿月活、AI蠕虫警示、谷歌AI搜索开放退订、Anthropic拟IPO 🌍</div>
                <div class="journey-content">
                    <div class="section-title">🌅 今日AI早班车</div>
                    
                    <div class="news-item">
                        <div class="news-title">ChatGPT月活突破10亿：用时最短，超越TikTok/Instagram/谷歌地图</div>
                        <div class="news-desc">Sensor Tower最新数据显示，ChatGPT上月已突破10亿月活用户大关（约3年），成为史上最快达到该里程碑的消费级应用。相较Google Maps、TikTok、Instagram、YouTube等"亿级APP"都更迅速。瑞银分析师认为"AI原生应用的网络效应被严重低估"，并上调OpenAI 2026年估值预期至4200亿美元（+25%）。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">学术警示："AI蠕虫"研究首次公开，可无人干预自传播</div>
                        <div class="news-desc">康奈尔大学团队发布题为《WormGPT 2.0》的论文，首次展示一种可无人干预、通过Agent-to-Agent通信在网络间传播的"AI蠕虫"。该蠕虫能从邮件系统窃取数据、传播垃圾信息、甚至劫持AI助手身份绕过安全护栏。论文共同作者Ben Zhao教授表示："这只是开始，2027年AI蠕虫可能成为头号网络安全威胁。"研究呼吁业界在部署Agent前必须引入"零信任"通信机制。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google开放"AI搜索退订"：网站可声明不进入AI Overview</div>
                        <div class="news-desc">Google宣布网站可通过新的robots.txt标签（`NoAITrain`、`NoAISummarize`）声明不参与其AI Overview搜索摘要与AI训练数据集。Google强调"退订AI Overview不会影响常规搜索排名"，但承认AI Overview目前已占其搜索流量的38%。这是继纽约时报、Reddit等大型内容方与AI公司博弈后的关键让步——但对中小内容创作者而言，AI爬虫的"二选一"困局仍待解决。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic已秘密递交S-1，2026下半年有望IPO</div>
                        <div class="news-desc">知情人士透露，Anthropic已于两周前秘密向SEC提交S-1文件草案，启动IPO进程。目标估值约3500-4000亿美元（与OpenAI 4200亿看齐），承销商包括高盛、摩根士丹利、摩根大通。若成功上市，将成为2026年最大科技IPO之一，并将是"AI 2.0"概念股首次全面登陆资本市场。Anthropic 2026年ARR预计达80亿美元，同比增长480%。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">特朗普签署"缩水版"AI网络安全行政令：自愿送审机制</div>
                        <div class="news-desc">白宫正式签署《AI Cyber Safety Executive Order》修订版，要求开发前沿AI模型的公司在新模型发布前30天，自愿向国土安全部/DHS提交模型能力与安全评估报告。该命令相比1月版本删除了"强制暂停"条款，被业界视为"既给政府数据，又不阻碍创新"的折中方案。OpenAI、Anthropic、谷歌、Meta均表态支持，但Anthropic附带条件"评估应保护商业机密"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Google母公司拟募资800亿美元，加速AI基础设施布局</div>
                        <div class="news-desc">Alphabet正在向机构投资者寻求高达800亿美元融资，主要用于2026-2027年的AI基础设施扩建。知情人士称方案包括股权、可转债、IDC合资等多种方式。Alphabet CFO Anat Ashkenazi表示"AI需求增长超过内部现金生成速度"。这笔融资若成功，将超过2025年所有科技公司年度资本支出之和的15%。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达Isaac Gr00t开放：人形机器人参考设计免费授权</div>
                        <div class="news-desc">英伟达在COMPUTEX 2026上正式发布Isaac Gr00t人形机器人参考设计平台，包含Jetson Thor计算模组、五指灵巧手、运动控制算法，开源至GitHub。首批合作方包括Figure AI、Apptronik、1X、Agility Robotics。英伟达CEO黄仁勋表示"这是机器人界的Android时刻"。分析师预测该平台将推动人形机器人BOM成本下降30-40%，并加速2027年人形机器人量产元年到来。</div>
                    </div>
                    
                    <div class="section-title">🧭 核心观察</div>
                    <div class="news-item">
                        <div class="news-title">AI行业"三段式焦虑"：用户增长、安全、监管同步加速</div>
                        <div class="news-desc">今日三件大事——ChatGPT破10亿月活、AI蠕虫论文、特朗普AI EO——折射2026年AI行业"用户规模爆炸、网络安全风险显化、监管框架初成"三轨并进。10亿月活意味着AI助手已成为水电一样的"基础设施"；AI蠕虫论文则提醒"基础设施"必然吸引攻击者；而行政令签署则代表政府开始建立与基础设施匹配的"看门人"机制。三个维度相互催化，2026下半年我们将看到"AI安全"成为下一个万亿级赛道。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic若成功IPO，AI 2.0概念将正式进入"价值发现"阶段</div>
                        <div class="news-desc">当前OpenAI/Anthropic/xAI/Mistral的估值主要由一级市场主导，缺乏公开市场验证。若Anthropic下半年成功上市，将为整个AI 2.0板块提供首个"真实定价基准"——PE/PS倍数、毛利率、客户集中度等关键指标将透明化。这对二级市场意义重大：A股、港股的"国产AI概念股"也将拥有更清晰的估值锚点。Bruce建议关注国内大模型第一股（阶跃星辰/智谱/百川/零一万物）的IPO进程。</div>
                    </div>
                </div>
            </div>'''

# === 在第108天之前插入第109天 ===
# 找到第108天注释的位置
day108_marker = '<!-- 第108天-->'
if day108_marker not in content:
    # 尝试其他变体
    import re as re2
    m = re2.search(r'<!--\s*第108天\s*-->', content)
    if m:
        insert_pos = m.start()
    else:
        print('ERROR: 找不到第108天注释')
        sys.exit(1)
else:
    insert_pos = content.find(day108_marker)

# 在第108天注释之前插入第109天
new_content = content[:insert_pos] + day109_entry + '\n\n            ' + content[insert_pos:]

# 写回文件
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'✅ Day 109 已插入到第108天之前')
print(f'   插入位置: {insert_pos}')
print(f'   文件大小: {len(content)} -> {len(new_content)} bytes')

# 验证
import re as re2
days = re2.findall(r'第(\d+)天', new_content)
print(f'   当前最大天数: {max([int(d) for d in days])}')
print(f'   109 出现次数: {len([d for d in days if d == "109"])}')

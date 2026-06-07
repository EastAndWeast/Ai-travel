# -*- coding: utf-8 -*-
"""
AI 环游世界 - Day 113 每日更新脚本
日期: 2026-06-08 (周一)
"""
import re
import codecs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# === Day 113 每日内容 (2026-06-08 周一) ===
# 主题: 周一开盘"AI 概念股共振"——SpaceX-Google 算力大单引爆算力链、Apple WWDC 倒计时 2 天、Altman 佛州诉状正面回应、Anthropic S-1 路演启动
day113_entry = '''            <!-- 第113天 -->
            <div class="journey-item">
                <div class="journey-date">2026-06-08</div>
                <div class="journey-title">第113天(周一):SpaceX-Google 算力大单引爆算力链周一开盘、Apple WWDC 2026 倒计时 2 天、Altman 佛州诉状正面回应、Anthropic S-1 路演正式启动 🚀</div>
                <div class="journey-content">
                    <div class="section-title">?? 今日 AI 早报速览</div>
                    
                    <div class="news-item">
                        <div class="news-title">周一开盘"算力链"全线飙涨:NVDA +5.2%、AVGO +4.8%、ORCL +6.1%、Alphabet +2.3%,SpaceX-Google $300 亿算力大单成催化剂</div>
                        <div class="news-desc">受周末披露的 SpaceX-Google 110K GPU 算力大单(总额 $300 亿、月费 $9.2 亿)催化,周一美股开盘 AI 算力链全线上涨:英伟达 NVDA +5.2% 报 $148.30、市值重回 $3.6 万亿;博通 AVGO +4.8%;Oracle ORCL 因 Stargate 三期算力托管预期 +6.1%;Alphabet GOOGL 因"既是 GPU 客户又是 SpaceX 股东"双重身份 +2.3%。盘中 VIX 跌 8%,显示市场将"算力即电网"格局视为确定性主线。摩根士丹利紧急上调 NVDA 目标价至 $190,理由是"AI 算力长协时代来临,营收可见性首次超越 iPhone 时代"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Altman 佛州诉状正面回应:"我们将战斗到底,这是创新与恐惧的较量"——OpenAI 内部成立"法律战时委员会"</div>
                        <div class="news-desc">Sam Altman 周日深夜发布 1,200 字公开长文,正面回应佛州总检察长 James Uthmeier 起诉:"OpenAI 的安全投入从未低于承诺,实际安全算力占比 11.4%(被诉状刻意混淆为 1-2%);我们将为 ChatGPT 服务 5 亿成年人与 1.2 亿未成年人的安全负责到底。"OpenAI 同步成立"法律战时委员会",由首席法务 Sarah Holcomb 牵头,邀请前 FCC 主席 Tom Wheeler 与前司法部副部长 Sally Yates 担任顾问。纽约州 Hochul 州长预计本周内签署"AI 聊天机器人青少年陪伴禁令",OpenAI 在该州用户量约 2200 万。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Apple WWDC 2026 倒计时 2 天:内部备忘录曝光"Apple Intelligence 3.0"五大新特性——Siri LLM 化、桌面代理、AI 编程、跨设备 RAG、端云混合架构</div>
                        <div class="news-desc">彭博 Mark Gurman 援引 Apple 内部备忘录,WWDC 2026(北京时间 6 月 10 日凌晨)将发布 Apple Intelligence 3.0,五大新特性包括:①Siri 完全 LLM 化(代号 Linwood,基于自研 30B 模型 + 端云混合);②桌面代理"Proactive Agent"(跨 Mac/iPad/iPhone 调度);③AI 编程工具"Swift Assist Pro"(Xcode 集成,与 Anthropic Claude 合作);④跨设备 RAG(本地+ iCloud Private Relay);⑤端云混合架构(本地 4B 模型 + 云端 200B 模型动态切换)。Apple 股价盘前 +1.8%,市场预期这是 Apple 在 AI 时代"真正入场"的标志。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Anthropic S-1 路演正式启动:首站伦敦/纽约/旧金山,GPT 时代首家"原生 AI 公司"冲击 11 月 IPO 窗口</div>
                        <div class="news-desc">Anthropic 周一正式启动 IPO 前期路演,首站覆盖伦敦(6 月 15 日)、纽约(6 月 22 日)、旧金山(7 月 6 日),由高盛/摩根士丹利/花旗联合主承销。S-1 文件预计 7 月底公开披露,公司估值区间 $3500-$4000 亿、对应 2027 年 P/S 约 28 倍。机构焦点问题:①Claude Code 80% 内部代码贡献的可持续性;②与 SpaceX $12.5 亿/月算力合同的中长期成本结构;③Anthropic Institute 即将发布的 RSI(递归自我改进)白皮书对监管的潜在影响。基石投资者候选:沙特 PIF、阿布扎比 MGX、新加坡 GIC、加拿大 CDPQ。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">微软"上瘾备忘录"余波:Omar Shahine 已被调离 AI 部门,转任"AI 伦理顾问";Nadella 内部推行"Agent 设计 12 原则"</div>
                        <div class="news-desc">微软内部通告,Corporate VP Omar Shahine(原 Outlook/Mobile 负责人)已被调离"AI 部门"实权岗位,转任非执行性质的"AI 伦理顾问"向 CTO 汇报,实际失去预算与团队管理权。Satya Nadella 同日发布全员信,推出"AI 代理设计 12 原则",包括"不设计令用户成瘾的代理""默认时长提醒""不利用心理弱点""人类复核优先"等,被业内视为"微软式 AI 责任宪章"。此举试图将"上瘾备忘录"事件转化为微软在企业 AI 市场的差异化卖点(对标 OpenAI/Google 的"增长优先"风格)。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">欧盟 AI Act 二级立法 6 月 15 日截止:GPAI 实施细则即将生效,中国出口的"通用 AI 模型"需在欧盟注册代表</div>
                        <div class="news-desc">欧盟委员会确认,《AI 法案》(AI Act)关于通用 AI 模型(GPAI)的二级立法将在 6 月 15 日生效,届时所有"系统性风险"GPAI 模型(训练算力 ≥ 10^25 FLOP)需在欧盟指定"法定代表",并接受 EU AI Office 的合规审计。受影响中国模型包括 Qwen3.7-Plus、文心 4.5、智谱 GLM-5、Kimi K3、Step-3 等——阿里、百度、智谱、月之暗面、阶跃均需在 6 月 15 日前完成欧盟实体注册与文件提交。违者最高罚款 1500 万欧元或全球营收 3%。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">马斯克 xAI 大规模扩招:3 个月内新增 1000 名研究员,集中投向 Grok 5 多模态与 Grok Code,月烧 $2.3 亿</div>
                        <div class="news-desc">The Information 援引 xAI 内部文件,马斯克已批准公司 3 个月内扩招 1000 名研究员(从当前约 1500 人扩至 2500 人),目标在 2026 Q4 推出"对标 GPT-5.5 Ultra + Claude Opus 4.7 + Gemini 2.5 Pro"的 Grok 5 多模态旗舰,以及代号"Mavis"的 Grok Code 企业版。月度运营烧钱从 $1.5 亿升至 $2.3 亿,资金来源主要依靠 SpaceX 转售算力收入 + Musk 个人 $50 亿注资 + 沙特 PIF 二轮融资。Musk 同步在 X 平台为"超级应用 X"开发 AI 智能体"X Agent"内测,直接对标 ChatGPT、Claude。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达 H200 重返中国市场有突破:首批 8 万颗 H200 通过"特殊许可"进入阿里/腾讯/字节,定价 $26,000/颗</div>
                        <div class="news-desc">路透社引述三位知情人士,英伟达首批 8 万颗 H200 AI 芯片已通过美国商务部"特殊许可"进入中国市场,客户为阿里云、腾讯云、字节火山引擎,定价 $26,000/颗(较 H100 海外版 $28,000 低 7%)。这是 2024 年 10 月出口管制升级后,英伟达首次大规模"高端 GPU"重返中国。配套消息:华为昇腾 950P(对标 H200)量产推迟至 2026 Q4,中芯国际 N+2 工艺良率仍仅 35%,意味着中国 AI 算力"国产替代"窗口期至少延长至 2027 年。字节跳动内部据传已用 H200 替换部分昇腾 910B 推理集群。</div>
                    </div>
                    
                    <div class="section-title">?? 核心观察</div>
                    <div class="news-item">
                        <div class="news-title">"算力长协"成为 AI 资本支出新范式:从一次性买断到 5-10 年期合同,营收可见性第一次超过 iPhone 时代</div>
                        <div class="news-desc">SpaceX-Google 110K GPU × 33 个月 + SpaceX-Anthropic Colossus-1 12.5 亿/月 × 5 年 + Meta 5GW × 12 年绿电 PPA + OpenAI Stargate 5 年 $1000 亿,AI 算力供给侧已全面进入"长协时代"。这种结构对英伟达/超大规模云/SPACEX 而言意味着:①营收可见性提升至 5 年,DCF 估值锚定从"市占率"转向"长协覆盖年限";②中游(超大规模云)与上游(GPU/电力)利益深度绑定,新进入者门槛倍增;③"长协覆盖率"或成为 AI 公司估值新指标,Anthropic(Stargate + SpaceX) > OpenAI(Stargate 主导) > xAI(算力过剩+转售) > Mistral(纯租赁)。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">AI 监管"州层级联盟"成型:佛州起诉 + 纽约禁令 + 加州审计 + 得州数据中心反对,联邦层面依然空白</div>
                        <div class="news-desc">美国 AI 监管出现"州先行、联邦滞后"格局:佛州诉 OpenAI/Altman + 纽约 AI 青少年陪伴禁令(等 Hochul 签署)+ 加州 AG 启动对 OpenAI/Anthropic/Google 的训练数据来源审计 + 得州 14 个县地方政府拒绝新建数据中心(已扩展到怀俄明/俄克拉荷马)。联邦层面,Trump 政府 6 月 5 日签署的"AI 行政令"仅在"促进 AI 创新"层面有动作,无统一立法。这意味着 AI 公司法务团队首次需要按州做合规矩阵,头部公司季度法务支出预测将从 $5000 万跃升至 $1.5 亿。欧盟 AI Act 二级立法与中国《生成式 AI 服务管理办法》修订构成跨大西洋+跨太平洋的"监管三角"。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">WWDC 2026 是 Apple 第二次"AI 入场"的关键测试:成功则 Apple Intelligence 3.0 拿下 12 亿设备存量,失败则 iPhone 16 周期继续承压</div>
                        <div class="news-desc">距离 6 月 10 日 WWDC 还有 2 天,Apple Intelligence 3.0 的发布决定 Apple 未来 3-5 年在 AI 时代的站位:①端云混合架构(本地 4B + 云端 200B)是 Apple 长期"隐私优先"哲学的延续,也是与 OpenAI/Google 路线最大差异;②Swift Assist Pro(Xcode + Claude)是 Apple 首次将"AI 编程"作为系统级能力,直接对标 GitHub Copilot Cursor;③Siri LLM 化(Linwood)决定 Siri 是否能"追回"过去 3 年被 ChatGPT/Claude/Gemini 抢占的对话市场份额。Apple 当前 AI 业务营收贡献仍 < 1%,但管理层在内部设定了"2027 年 AI 业务 $300 亿营收"目标——WWDC 表现将决定这个目标是否可信。</div>
                    </div>
                </div>
            </div>'''

# === 在第112天之前插入第113天 ===
# 找到第112天注释的位置
day112_marker = '<!-- 第112天 -->'
if day112_marker not in content:
    # 尝试其他变体
    m = re.search(r'<!--\s*第112天\s*-->', content)
    if m:
        insert_pos = m.start()
    else:
        print('ERROR: 找不到第112天注释')
        sys.exit(1)
else:
    insert_pos = content.find(day112_marker)

# 在第112天注释之前插入第113天
new_content = content[:insert_pos] + day113_entry + '\n\n            ' + content[insert_pos:]

# 写回文件
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'✅ Day 113 已插入到第112天之前')
print(f'   插入位置: {insert_pos}')
print(f'   文件大小: {len(content)} -> {len(new_content)} bytes')

# 验证
days = re.findall(r'第(\d+)天', new_content)
print(f'   当前最大天数: {max([int(d) for d in days])}')
print(f'   共有 {len([d for d in days if int(d) == 113])} 个"第113天"')

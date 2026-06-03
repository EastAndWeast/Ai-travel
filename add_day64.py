# -*- coding: utf-8 -*-
"""
AI环游世界 - Day 64 更新脚本
日期: 2026-04-18 (内容覆盖 2026-04-17 AI新闻)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/Ai-travel/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取当前天数 (从 <h1> 标题中找)
day_match = re.search(r'第(\d+)天', content)
current_day = int(day_match.group(1)) if day_match else 63
new_day = current_day + 1
print(f'Current day: {current_day} -> New day: {new_day}')

# 更新标题中的天数
content = re.sub(
    r'(<h1>🌏 环游 AI 世界</h1>.*?<p class="subtitle">)第\d+天 AI 世界探索日记',
    r'\g<1>第' + str(new_day) + r'天 AI 世界探索日记',
    content
)

# Day 64 内容 - 覆盖 2026-04-17 新闻
day64_entry = '''
            <!-- 第''' + str(new_day) + '''天内容 -->
            <div class="journey-item">
                <div class="journey-date">2026-04-18</div>
                <div class="journey-title">第''' + str(new_day) + '''天：ChatGPT 周活破10亿且女性首超50%；Cerebras 200亿美元牵手 OpenAI 并计划 IPO ??</div>
                <div class="journey-content">
                    <div class="section-title">🔥 今日 AI 重大新闻</div>
                    
                    <div class="news-item">
                        <div class="news-title">ChatGPT 用户规模破 10 亿：女性用户占比首超 50%，AI 大众化里程碑</div>
                        <div class="news-desc">OpenAI 官方数据显示，ChatGPT 全球周活跃用户即将突破 10 亿。更具历史意义的是用户结构转变：女性用户比例从 2022 年刚发布时的 20% 强势反超至突破 50%，首次超过男性。这意味着全球约 5 亿女性已成为 ChatGPT 的定期活跃用户。AI 产品的受众格局已从早期科技爱好者主导彻底转变为大众化工具。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Cerebras 与 OpenAI 签署 200 亿美元芯片协议，剑指 IPO</div>
                        <div class="news-desc">AI 芯片公司 Cerebras 与 OpenAI 达成一项为期三年、金额超亿美元的重磅芯片供应协议，规模是年初协议的两倍。Cerebras 还同时宣布计划 IPO，OpenAI 承诺提供约 10 亿美元资金支持 Cerebras 数据中心系统开发，并获得最高 10% 的少数股权认股凭证。这标志着 AI 算力竞争已从 GPU 集群扩展到专用芯片定制的新阶段。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">阿里开源 Qwen3.6-35B-A3B：30 亿激活参数实现编程能力跨越式升级</div>
                        <div class="news-desc">阿里巴巴千问大模型团队于 4 月 16 日开源稀疏 MoE 模型 Qwen3.6-35B-A3B，总参数量 350 亿但运行时激活参数仅 30 亿，在多项核心编程基准测试中超越 270 亿参数的稠密模型。该模型已集成至 Qwen Studio 并通过阿里云百炼平台提供 API 服务，支持思维链保留功能，被视为轻量级开源模型在智能体编程领域的标志性突破。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">Perplexity 推出 Mac 端 AI 助手 Personal Computer：7×24 小时运行，可代用户操作电脑</div>
                        <div class="news-desc">AI 搜索引擎 Perplexity 发布 Mac 端 AI 助手 Personal Computer，具备直接访问文件系统和原生应用的能力，支持文本与语音双交互，可实时感知用户当前活跃窗口并主动提供操作建议。所有操作在隔离安全沙箱中完成以保护隐私。这标志着 AI 交互从"对话框"正式向"操作系统"深度融合的方向演进。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">科大讯飞发布 AstronClaw 升级版：软硬一体 AI Agent 架构，9 项新品同步亮相</div>
                        <div class="news-desc">科大讯飞发布 AstronClaw 升级版，同步推出 9 项新产品，展示"软硬一体"AI Agent 架构。该架构推动 AI 从"对话助手"向"物理执行中枢"转变，旨在突破屏幕限制，让大模型能力深入物理世界和复杂业务流。在办公领域，AstronClaw 与讯飞办公本融合，实现职场碎片化信息的结构化处理。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">英伟达发布 Lyra 2.0：单张照片生成 90 米 3D 环境，多项指标超越竞争对手</div>
                        <div class="news-desc">英伟达发布 Lyra 2.0 技术，通过单张照片即可构建大规模、高连贯性的虚拟 3D 环境，解决了长距离相机路径下的图像失真难题。该技术引入双重创新策略，实现与物理引擎的无缝衔接，为机器人仿真训练提供高效环境支持，被视为 AI 在 3D 空间理解与实时环境模拟领域的重大突破。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">苹果 iOS 27 Beta 四大 AI 升级曝光：拍照即录入、标签自动命名</div>
                        <div class="news-desc">苹果在 iOS 27 Beta 版本中揭示多项 Apple Intelligence 新功能：营养标签解析（自动扫描食品包装数据并同步至健康应用）、纸面信息识别（一键提取并添加电话号码或地址至通讯录）、实体卡券数字化扫描（AI 识别活动门票和会员卡转化为数字通行证）、智能标签组命名。这些功能展示了苹果 AI 技术的进一步深化。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">OpenAI 发布 GPT-Rosalind：跨界制药与生命科学，DNA 发现者命名</div>
                        <div class="news-desc">OpenAI 推出生命科学 AI 模型 GPT-Rosalind，以 DNA 双螺旋结构发现者 Rosalind Franklin 命名。该模型通过分析生化数据，协助科研人员进行证据合成、假设生成、实验规划和蛋白质工程分析，旨在加速药物研发进程，推动 AI 在医疗和生命科学领域的实际应用转化。</div>
                    </div>
                    
                    <div class="news-item">
                        <div class="news-title">星巴克引入 ChatGPT：根据心情推荐饮品，AI 驱动的个性化消费体验</div>
                        <div class="news-desc">星巴克正在测试基于 ChatGPT 的智能点单应用，用户可通过输入当天心情或需求，获得个性化饮品推荐。这标志着 AI 推荐系统从内容消费领域扩展到实体消费场景，为零售行业的 AI 商业化落地提供新范式。</div>
                    </div>
                    
                    <div class="section-title">📊 每日洞察</div>
                    <div class="news-item">
                        <div class="news-title">AI 大众化拐点已至：从 10 亿用户到性别均衡，2026 年 AI 渗透率质变</div>
                        <div class="news-desc">ChatGPT 女性用户首超 50% 的里程碑，与十亿用户大关叠加，折射出一个深层趋势：AI 产品已彻底摆脱"科技极客专属"的标签，进入真正意义上的大众化阶段。当女性、老年人、非英语母语者开始成为 AI 产品的主流用户，意味着 AI 泡沫论可以休矣——真实用户在真实场景中真实地用起来了。</div>
                    </div>
                </div>
            </div>
'''

# 在 footer 之前插入新内容
footer_marker = '<footer>'
content = content.replace(footer_marker, day64_entry + '\n\n' + footer_marker)

# 更新 footer 时间
content = content.replace(
    '最后更新：',
    '最后更新：'
)
content = re.sub(
    r'(🚀 旅程进行中.*?)<br>\s*',
    r'\1<br>\n            ',
    content
)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n=== AI环游世界 Day {new_day} 更新完成 ===')
print('日期: 2026-04-18')
print('覆盖新闻: 2026-04-17')
print('主要新闻: ChatGPT 10亿用户里程碑, Cerebras 200亿美元协议, Qwen3.6开源, Perplexity Mac端')

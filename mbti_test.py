"""
MBTI 人格测试仪
================
基于 Myers-Briggs 类型指标的性格测试系统

主题：粉色白色梦幻背景 · 精致UI设计
功能：15道专业测试题 · 实时进度 · 详细结果分析

版本：v1.0
"""

import streamlit as st

# ============================================
# 页面配置
# ============================================
st.set_page_config(
    page_title="🌸 MBTI人格测试仪",
    page_icon="🌸",
    layout="centered"
)

# ============================================
# Session State 初始化
# ============================================
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'test_completed' not in st.session_state:
    st.session_state.test_completed = False
if 'mbti_result' not in st.session_state:
    st.session_state.mbti_result = None

# ============================================
# 粉白梦幻主题 CSS
# ============================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&display=swap');

/* 粉紫色渐变背景 */
.stApp {
    background: linear-gradient(135deg, 
        #FFF0F5 0%, 
        #FFE4F0 15%, 
        #FCE4EC 30%, 
        #F3E5F5 45%, 
        #E8EAF6 60%, 
        #FCE4EC 75%, 
        #FFE4E1 90%, 
        #FFF5F5 100%) !important;
    background-attachment: fixed !important;
    font-family: 'Noto Sans SC', sans-serif !important;
    min-height: 100vh !important;
}

/* 樱花装饰层 - 顶部 */
.sakura-top {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 350px;
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cg fill='%23FFB7C5' fill-opacity='0.6'%3E%3Ccircle cx='10' cy='20' r='8'/%3E%3Ccircle cx='30' cy='15' r='6'/%3E%3Ccircle cx='50' cy='25' r='7'/%3E%3Ccircle cx='70' cy='18' r='5'/%3E%3Ccircle cx='90' cy='22' r='6'/%3E%3Ccircle cx='20' cy='40' r='5'/%3E%3Ccircle cx='45' cy='35' r='6'/%3E%3Ccircle cx='65' cy='38' r='4'/%3E%3Ccircle cx='85' cy='30' r='5'/%3E%3C/g%3E%3Cg fill='%23FF69B4' fill-opacity='0.3'%3E%3Ccircle cx='15' cy='25' r='4'/%3E%3Ccircle cx='35' cy='20' r='3'/%3E%3Ccircle cx='55' cy='30' r='4'/%3E%3Ccircle cx='75' cy='25' r='3'/%3E%3Ccircle cx='95' cy='28' r='4'/%3E%3C/g%3E%3C/svg%3E"),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cg fill='%23E1BEE7' fill-opacity='0.4'%3E%3Ccircle cx='5' cy='10' r='7'/%3E%3Ccircle cx='25' cy='5' r='5'/%3E%3Ccircle cx='45' cy='12' r='6'/%3E%3Ccircle cx='65' cy='8' r='4'/%3E%3Ccircle cx='85' cy='15' r='5'/%3E%3C/g%3E%3C/svg%3E");
    background-repeat: repeat-x;
    background-size: 120px 60px, 100px 40px;
    pointer-events: none;
    z-index: 0;
    opacity: 0.8;
}

/* 樱花装饰层 - 右侧 */
.sakura-right {
    position: fixed;
    top: 100px;
    right: -50px;
    width: 300px;
    height: 500px;
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cg fill='%23FFB7C5' fill-opacity='0.5'%3E%3Ccircle cx='80' cy='10' r='9'/%3E%3Ccircle cx='90' cy='30' r='7'/%3E%3Ccircle cx='85' cy='50' r='8'/%3E%3Ccircle cx='92' cy='70' r='6'/%3E%3Ccircle cx='80' cy='90' r='7'/%3E%3Ccircle cx='95' cy='20' r='5'/%3E%3Ccircle cx='88' cy='45' r='4'/%3E%3C/g%3E%3Cg fill='%23FF69B4' fill-opacity='0.25'%3E%3Ccircle cx='82' cy='15' r='3'/%3E%3Ccircle cx='93' cy='35' r='4'/%3E%3Ccircle cx='87' cy='55' r='3'/%3E%3Ccircle cx='94' cy='75' r='4'/%3E%3C/g%3E%3C/svg%3E"),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cg fill='%23DDA0DD' fill-opacity='0.3'%3E%3Ccircle cx='78' cy='5' r='6'/%3E%3Ccircle cx='88' cy='25' r='5'/%3E%3Ccircle cx='83' cy='45' r='5'/%3E%3Ccircle cx='90' cy='65' r='4'/%3E%3C/g%3E%3C/svg%3E");
    background-repeat: repeat-y;
    background-size: 100px 80px, 80px 60px;
    pointer-events: none;
    z-index: 0;
    opacity: 0.6;
}

/* 樱花装饰层 - 左侧 */
.sakura-left {
    position: fixed;
    top: 200px;
    left: -30px;
    width: 250px;
    height: 400px;
    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cg fill='%23FFC0CB' fill-opacity='0.45'%3E%3Ccircle cx='20' cy='15' r='8'/%3E%3Ccircle cx='10' cy='40' r='6'/%3E%3Ccircle cx='18' cy='65' r='7'/%3E%3Ccircle cx='5' cy='85' r='5'/%3E%3Ccircle cx='22' cy='30' r='4'/%3E%3Ccircle cx='8' cy='55' r='5'/%3E%3C/g%3E%3Cg fill='%23FF1493' fill-opacity='0.2'%3E%3Ccircle cx='15' cy='20' r='3'/%3E%3Ccircle cx='7' cy='45' r='2'/%3E%3Ccircle cx='14' cy='70' r='3'/%3E%3C/g%3E%3C/svg%3E"),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cg fill='%23E6E6FA' fill-opacity='0.35'%3E%3Ccircle cx='18' cy='10' r='5'/%3E%3Ccircle cx='6' cy='35' r='4'/%3E%3Ccircle cx='15' cy='60' r='5'/%3E%3C/g%3E%3C/svg%3E");
    background-repeat: repeat-y;
    background-size: 90px 70px, 70px 50px;
    pointer-events: none;
    z-index: 0;
    opacity: 0.5;
}

/* 樱花花瓣飘落动画 */
@keyframes sakuraFall {
    0% {
        transform: translateY(-10vh) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 0.8;
    }
    90% {
        opacity: 0.6;
    }
    100% {
        transform: translateY(100vh) rotate(720deg);
        opacity: 0;
    }
}

/* 飘落的樱花花瓣 */
.sakura-petal {
    position: fixed;
    width: 12px;
    height: 12px;
    background: radial-gradient(circle, #FFB7C5 0%, #FF69B4 100%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    animation: sakuraFall 8s ease-in-out infinite;
    box-shadow: 0 0 6px rgba(255, 183, 197, 0.6);
}

/* 主内容区域 */
.block-container {
    position: relative;
    z-index: 1;
    padding-top: 30px !important;
    max-width: 800px !important;
}

/* 标题样式 */
h1 {
    color: #880E4F !important;
    text-align: center !important;
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    margin-bottom: 10px !important;
    text-shadow: 
        0 2px 4px rgba(0, 0, 0, 0.15),
        0 0 20px rgba(136, 14, 79, 0.3) !important;
    background: linear-gradient(135deg, #880E4F 0%, #C2185B 50%, #E91E63 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

h2 {
    color: #6A1B9A !important;
    font-weight: 700 !important;
    font-size: 1.3rem !important;
    border-bottom: 2px solid #CE93D8 !important;
    padding-bottom: 10px !important;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

h3 {
    color: #7B1FA2 !important;
    font-weight: 600 !important;
    font-size: 1.15rem !important;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
}

/* 卡片容器 */
.test-card {
    background: rgba(255, 255, 255, 0.98) !important;
    backdrop-filter: blur(15px) !important;
    border: 2px solid rgba(186, 104, 200, 0.3) !important;
    border-radius: 20px !important;
    padding: 35px !important;
    box-shadow: 
        0 15px 45px rgba(186, 104, 200, 0.18),
        0 0 0 1px rgba(255, 255, 255, 0.95) !important;
    margin-bottom: 25px !important;
    position: relative;
    overflow: hidden;
}

.test-card::before {
    content: '🌸';
    position: absolute;
    top: 20px;
    right: 25px;
    font-size: 1.8rem;
    opacity: 0.5;
}

.test-card::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #CE93D8, #BA68C8, #CE93D8);
}

/* 问题文字 */
.question-text {
    color: #212121 !important;
    font-size: 1.25rem !important;
    font-weight: 550 !important;
    line-height: 1.8 !important;
    padding: 25px 0 !important;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    letter-spacing: 0.3px;
}

/* 选项按钮 */
.stRadio > div {
    background: rgba(255, 253, 254, 0.95) !important;
    border: 1.5px solid rgba(186, 104, 200, 0.25) !important;
    border-radius: 18px !important;
    padding: 20px !important;
    margin-top: 10px !important;
}

.stRadio label {
    color: #37474F !important;
    font-size: 1.05rem !important;
    font-weight: 500 !important;
    padding: 15px 20px !important;
    transition: all 0.3s ease !important;
    border-radius: 12px !important;
    margin: 5px 0 !important;
    display: block !important;
}

.stRadio label:hover {
    color: #7B1FA2 !important;
    background: rgba(186, 104, 200, 0.12) !important;
    border-radius: 12px !important;
    transform: translateX(5px);
}

.stRadio [role="radio"] {
    accent-color: #BA68C8 !important;
}

/* 进度条 */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #CE93D8, #BA68C8, #9C27B0) !important;
    border-radius: 12px !important;
    height: 10px !important;
}

/* 主按钮 */
.stButton > button {
    background: linear-gradient(135deg, #9C27B0 0%, #7B1FA2 50%, #6A1B9A 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 28px !important;
    padding: 16px 50px !important;
    font-size: 1.15rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    box-shadow: 
        0 6px 25px rgba(156, 39, 176, 0.4),
        0 0 0 1px rgba(255, 255, 255, 0.2) inset !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-4px) !important;
    box-shadow: 
        0 10px 35px rgba(156, 39, 176, 0.5),
        0 0 0 1px rgba(255, 255, 255, 0.3) inset !important;
}

/* 侧边栏 */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FCE4EC 0%, #F3E5F5 50%, #E8EAF6 100%) !important;
    border-right: 2px solid rgba(186, 104, 200, 0.3) !important;
}

section[data-testid="stSidebar"] h2 {
    color: #7B1FA2 !important;
    font-size: 1.25rem !important;
    font-weight: 600 !important;
}

/* 结果卡片 */
.result-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.99) 0%, rgba(254,243,248,0.98) 50%, rgba(243,229,245,0.96) 100%) !important;
    border: 3px solid rgba(186, 104, 200, 0.4) !important;
    border-radius: 28px !important;
    padding: 45px !important;
    text-align: center !important;
    box-shadow: 
        0 20px 60px rgba(186, 104, 200, 0.25),
        0 0 0 1px rgba(255, 255, 255, 0.98) inset !important;
}

.mbti-type {
    font-size: 4.5rem !important;
    font-weight: 800 !important;
    letter-spacing: 10px !important;
    margin: 25px 0 !important;
    background: linear-gradient(135deg, #6A1B9A 0%, #9C27B0 30%, #CE93D8 50%, #9C27B0 70%, #6A1B9A 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 
        0 0 30px rgba(156, 39, 176, 0.4),
        0 4px 8px rgba(0, 0, 0, 0.1) !important;
}

.mbti-name {
    font-size: 1.6rem !important;
    color: #6A1B9A !important;
    font-weight: 700 !important;
    margin-bottom: 20px !important;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}

/* 特质标签 */
.trait-tag {
    display: inline-block !important;
    background: linear-gradient(135deg, #CE93D8 0%, #BA68C8 50%, #9C27B0 100%) !important;
    color: #FFFFFF !important;
    padding: 10px 24px !important;
    border-radius: 25px !important;
    margin: 6px !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 15px rgba(156, 39, 176, 0.3);
}

/* 提示信息 */
.stSuccess {
    background: rgba(186, 104, 200, 0.12) !important;
    border-left: 4px solid #9C27B0 !important;
    color: #5D4E6D !important;
    font-weight: 500 !important;
}

.stInfo {
    background: rgba(206, 147, 216, 0.15) !important;
    border-left: 4px solid #BA68C8 !important;
    color: #455A64 !important;
    font-weight: 500 !important;
}

/* 滚动条 */
::-webkit-scrollbar { width: 10px !important; }
::-webkit-scrollbar-track { background: #FCE4EC !important; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #CE93D8, #BA68C8, #9C27B0) !important;
    border-radius: 5px !important;
}

/* 分隔线 */
hr {
    border-color: rgba(186, 104, 200, 0.3) !important;
}

/* 通用文字样式 */
p, span, div {
    color: #37474F !important;
    font-weight: 500 !important;
}

/* 侧边栏文字 */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: #455A64 !important;
    font-weight: 500 !important;
}
</style>
""", unsafe_allow_html=True)


# ============================================
# MBTI 测试问题库（15题）
# ============================================
QUESTIONS = [
    # E/I 维度（外向/内向）- 4题
    {
        "id": 1,
        "dimension": "EI",
        "text": "在社交聚会中，你通常会：",
        "options": {
            "A": "主动与很多人交谈，享受热闹的氛围",
            "B": "与少数几个熟悉的人深入交流",
            "C": "找个安静角落观察，不太主动参与",
            "D": "尽快找理由离开，更喜欢独处"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 2,
        "dimension": "EI",
        "text": "当你需要恢复精力时，你更倾向于：",
        "options": {
            "A": "和朋友外出活动、聚会",
            "B": "与亲近的人小范围交流",
            "C": "独自做一些安静的活动",
            "D": "完全独处，远离人群"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 3,
        "dimension": "EI",
        "text": "在团队讨论中，你通常：",
        "options": {
            "A": "积极发言，带动讨论气氛",
            "B": "适时表达观点，参与互动",
            "C": "先倾听思考，再谨慎发言",
            "D": "保持沉默，内心思考为主"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 4,
        "dimension": "EI",
        "text": "周末你更愿意如何度过：",
        "options": {
            "A": "参加各种社交活动和派对",
            "B": "和朋友小聚或外出游玩",
            "C": "在家看书、看电影放松",
            "D": "独自进行个人兴趣爱好"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    
    # S/N 维度（感觉/直觉）- 4题
    {
        "id": 5,
        "dimension": "SN",
        "text": "在解决问题时，你更倾向于：",
        "options": {
            "A": "依靠过往经验和实际方法",
            "B": "结合经验，适当尝试新思路",
            "C": "思考创新方案，突破常规",
            "D": "完全依靠直觉和灵感"
        },
        "scores": {"A": 0, "B": 1, "C": 2, "D": 4}
    },
    {
        "id": 6,
        "dimension": "SN",
        "text": "阅读一本书时，你更关注：",
        "options": {
            "A": "具体的事实和实用信息",
            "B": "事实与作者观点的结合",
            "C": "深层含义和象征隐喻",
            "D": "抽象理念和哲学思考"
        },
        "scores": {"A": 0, "B": 1, "C": 2, "D": 4}
    },
    {
        "id": 7,
        "dimension": "SN",
        "text": "你更相信哪种判断方式：",
        "options": {
            "A": "可验证的事实和数据",
            "B": "事实与直觉的结合",
            "C": "内心的直觉感受",
            "D": "纯粹的灵感与洞察"
        },
        "scores": {"A": 0, "B": 1, "C": 2, "D": 4}
    },
    {
        "id": 8,
        "dimension": "SN",
        "text": "描述一件事物时，你会：",
        "options": {
            "A": "详细描述具体细节和特征",
            "B": "描述细节并概括整体",
            "C": "用比喻和联想来表达",
            "D": "侧重概念和抽象意义"
        },
        "scores": {"A": 0, "B": 1, "C": 2, "D": 4}
    },
    
    # T/F 维度（思考/情感）- 3题
    {
        "id": 9,
        "dimension": "TF",
        "text": "做重要决定时，你更看重：",
        "options": {
            "A": "客观逻辑和事实分析",
            "B": "逻辑分析兼顾他人感受",
            "C": "对他人的影响和感受",
            "D": "内心价值观和情感"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 10,
        "dimension": "TF",
        "text": "当朋友向你倾诉烦恼时，你会：",
        "options": {
            "A": "分析问题，提供解决方案",
            "B": "先倾听，再给出建议",
            "C": "表达同情，给予情感支持",
            "D": "完全以情感共鸣为主"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 11,
        "dimension": "TF",
        "text": "面对批评时，你的反应是：",
        "options": {
            "A": "理性分析批评是否合理",
            "B": "思考批评内容，控制情绪",
            "C": "感到受伤，需要情感支持",
            "D": "深受打击，情绪波动大"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    
    # J/P 维度（判断/知觉）- 4题
    {
        "id": 12,
        "dimension": "JP",
        "text": "对于计划和时间安排，你：",
        "options": {
            "A": "制定详细计划并严格执行",
            "B": "有大致计划，保持灵活性",
            "C": "随情况变化调整安排",
            "D": "不喜欢计划，随性而为"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 13,
        "dimension": "JP",
        "text": "完成一项任务时，你倾向于：",
        "options": {
            "A": "提前完成，避免拖延",
            "B": "按时完成，保持节奏",
            "C": "在截止前灵活推进",
            "D": "最后一刻冲刺完成"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 14,
        "dimension": "JP",
        "text": "你的生活环境通常是：",
        "options": {
            "A": "整洁有序，物品摆放固定",
            "B": "基本整洁，偶尔凌乱",
            "C": "有个人风格，较为随意",
            "D": "自由随性，不拘小节"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    },
    {
        "id": 15,
        "dimension": "JP",
        "text": "面对突发变化，你会：",
        "options": {
            "A": "感到不适，希望按原计划",
            "B": "调整心态，重新规划",
            "C": "接受变化，灵活应对",
            "D": "享受变化带来的新鲜感"
        },
        "scores": {"A": 4, "B": 2, "C": 1, "D": 0}
    }
]

# ============================================
# MBTI 类型详细解释
# ============================================
MBTI_TYPES = {
    "INTJ": {
        "name": "建筑师",
        "emoji": "🏛️",
        "description": "富有想象力和战略性的思想家，一切皆在计划之中。",
        "traits": ["独立思考", "战略规划", "追求完美", "理性决策", "目标导向"],
        "strengths": "擅长长期规划，逻辑分析能力强，执行力出色",
        "weaknesses": "可能过于完美主义，有时显得冷漠",
        "careers": "科学家、工程师、战略顾问、建筑师"
    },
    "INTP": {
        "name": "逻辑学家",
        "emoji": "🧠",
        "description": "富有创造力的发明家，对知识有着永不满足的渴望。",
        "traits": ["逻辑分析", "创新思维", "追求真理", "独立研究", "理论建构"],
        "strengths": "思维敏捷，善于发现问题和解决问题",
        "weaknesses": "可能过于理论化，实际执行能力较弱",
        "careers": "程序员、科学家、哲学家、分析师"
    },
    "ENTJ": {
        "name": "指挥官",
        "emoji": "👑",
        "description": "大胆、富有想象力的领导者，总能找到解决方法。",
        "traits": ["领导才能", "战略眼光", "果断决策", "高效执行", "目标驱动"],
        "strengths": "领导能力出众，善于激励团队，决策果断",
        "weaknesses": "可能过于强势，对他人感受关注不足",
        "careers": "CEO、项目经理、律师、企业家"
    },
    "ENTP": {
        "name": "辩论家",
        "emoji": "🎤",
        "description": "聪明好奇的思想家，无法抗拒智力挑战。",
        "traits": ["创新思维", "辩论能力", "随机应变", "挑战权威", "探索新知"],
        "strengths": "思维活跃，善于创新，沟通能力强",
        "weaknesses": "可能过于好辩，难以专注完成任务",
        "careers": "创业者、律师、咨询师、记者"
    },
    "INFJ": {
        "name": "提倡者",
        "emoji": "🌟",
        "description": "安静而神秘，但能深刻启发和感染他人。",
        "traits": ["洞察人心", "理想主义", "深度思考", "帮助他人", "追求意义"],
        "strengths": "洞察力强，善于理解他人，有强烈使命感",
        "weaknesses": "可能过于理想化，容易感到疲惫",
        "careers": "心理咨询师、作家、教师、社工"
    },
    "INFP": {
        "name": "调停者",
        "emoji": "🌸",
        "description": "诗意、善良的利他主义者，总是渴望帮助善良之人。",
        "traits": ["理想主义", "创意丰富", "情感深刻", "追求和谐", "内心世界丰富"],
        "strengths": "富有同情心，创造力强，善于倾听",
        "weaknesses": "可能过于敏感，难以应对批评",
        "careers": "作家、艺术家、心理咨询师、设计师"
    },
    "ENFJ": {
        "name": "主人公",
        "emoji": "💫",
        "description": "富有魅力的领导者，能够激励听众。",
        "traits": ["领导魅力", "同理心强", "激励他人", "社交能力", "组织才能"],
        "strengths": "善于激励他人，沟通能力出色，有影响力",
        "weaknesses": "可能过于关注他人，忽视自己需求",
        "careers": "教师、培训师、公关、政治家"
    },
    "ENFP": {
        "name": "竞选者",
        "emoji": "🌈",
        "description": "热情、有创造力的社交达人，总能找到微笑的理由。",
        "traits": ["热情洋溢", "创意无限", "社交达人", "探索精神", "感染力强"],
        "strengths": "热情开朗，善于社交，创造力丰富",
        "weaknesses": "可能注意力分散，难以完成长期任务",
        "careers": "演员、记者、营销、培训师"
    },
    "ISTJ": {
        "name": "物流师",
        "emoji": "📦",
        "description": "务实、事实为依据的个人，可靠性不容怀疑。",
        "traits": ["责任心强", "务实可靠", "遵守规则", "注重细节", "执行力强"],
        "strengths": "可靠稳定，执行力强，注重细节",
        "weaknesses": "可能过于固执，缺乏灵活性",
        "careers": "会计师、审计师、管理员、警察"
    },
    "ISFJ": {
        "name": "守卫者",
        "emoji": "🛡️",
        "description": "非常专注和温暖的守护者，时刻准备保护所爱之人。",
        "traits": ["忠诚可靠", "细心体贴", "乐于助人", "责任心强", "传统价值观"],
        "strengths": "忠诚可靠，善于照顾他人，注重细节",
        "weaknesses": "可能过于谦逊，难以拒绝他人",
        "careers": "护士、教师、行政助理、社工"
    },
    "ESTJ": {
        "name": "总经理",
        "emoji": "💼",
        "description": "出色的管理者，在管理事务方面无可匹敌。",
        "traits": ["组织能力", "领导才能", "务实高效", "遵守规则", "目标导向"],
        "strengths": "组织能力强，执行力出色，善于管理",
        "weaknesses": "可能过于传统，难以接受新观点",
        "careers": "管理者、军官、银行家、法官"
    },
    "ESFJ": {
        "name": "执政官",
        "emoji": "❤️",
        "description": "极具同情心、爱交际的人，总是热心帮助他人。",
        "traits": ["社交达人", "关心他人", "组织能力", "和谐追求", "传统价值观"],
        "strengths": "善于社交，关心他人，组织能力强",
        "weaknesses": "可能过于在意他人评价，需要认可",
        "careers": "护士、教师、公关、销售"
    },
    "ISTP": {
        "name": "鉴赏家",
        "emoji": "🔧",
        "description": "大胆而实际的实验家，善于使用各种工具。",
        "traits": ["动手能力", "冷静分析", "解决问题", "独立自主", "适应变化"],
        "strengths": "动手能力强，善于解决实际问题，冷静理性",
        "weaknesses": "可能过于独立，不善表达情感",
        "careers": "工程师、技师、运动员、程序员"
    },
    "ISFP": {
        "name": "探险家",
        "emoji": "🎨",
        "description": "灵活而有魅力的艺术家，时刻准备探索新事物。",
        "traits": ["艺术天赋", "自由精神", "审美敏锐", "温和友善", "活在当下"],
        "strengths": "艺术天赋强，善于发现美，温和友善",
        "weaknesses": "可能过于内向，难以做长期规划",
        "careers": "艺术家、设计师、摄影师、厨师"
    },
    "ESTP": {
        "name": "企业家",
        "emoji": "🚀",
        "description": "聪明、精力充沛的人，善于享受生活边缘。",
        "traits": ["行动力强", "冒险精神", "社交能力", "随机应变", "务实高效"],
        "strengths": "行动力强，善于社交，应变能力出色",
        "weaknesses": "可能过于冲动，缺乏长期规划",
        "careers": "企业家、销售、运动员、演员"
    },
    "ESFP": {
        "name": "表演者",
        "emoji": "🎭",
        "description": "自发性、精力充沛的艺人，生活永远不会无聊。",
        "traits": ["热情开朗", "表演天赋", "社交达人", "活在当下", "乐观积极"],
        "strengths": "热情开朗，善于表演，社交能力强",
        "weaknesses": "可能注意力分散，难以专注",
        "careers": "演员、主持人、销售、旅游顾问"
    }
}


# ============================================
# 计算MBTI结果
# ============================================
def calculate_mbti(answers):
    """根据答案计算MBTI类型"""
    scores = {"EI": 0, "SN": 0, "TF": 0, "JP": 0}
    counts = {"EI": 0, "SN": 0, "TF": 0, "JP": 0}
    
    for i, answer in enumerate(answers):
        question = QUESTIONS[i]
        dimension = question["dimension"]
        scores[dimension] += question["scores"][answer]
        counts[dimension] += 4  # 每题最高分4分
    
    # 计算各维度倾向
    result = ""
    
    # E/I: 分数高倾向于E
    if scores["EI"] >= counts["EI"] / 2:
        result += "E"
    else:
        result += "I"
    
    # S/N: 分数高倾向于S
    if scores["SN"] >= counts["SN"] / 2:
        result += "S"
    else:
        result += "N"
    
    # T/F: 分数高倾向于T
    if scores["TF"] >= counts["TF"] / 2:
        result += "T"
    else:
        result += "F"
    
    # J/P: 分数高倾向于J
    if scores["JP"] >= counts["JP"] / 2:
        result += "J"
    else:
        result += "P"
    
    return result, scores


# ============================================
# 侧边栏
# ============================================
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 20px 0;">
        <span style="font-size:3rem;">🌸</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("💕 MBTI测试指南")
    st.markdown("---")
    
    st.info("""
    **什么是MBTI？**
    
    MBTI（Myers-Briggs Type Indicator）
    是一种人格类型测评工具，
    将人格分为16种类型。
    """)
    
    st.markdown("---")
    
    st.subheader("📋 四个维度")
    st.markdown("""
    - **E/I** 外向 vs 内向
    - **S/N** 感觉 vs 直觉
    - **T/F** 思考 vs 情感
    - **J/P** 判断 vs 知觉
    """)
    
    st.markdown("---")
    
    if not st.session_state.test_completed:
        progress = st.session_state.current_question / len(QUESTIONS)
        st.progress(progress)
        st.caption(f"已完成 {st.session_state.current_question}/{len(QUESTIONS)} 题")


# ============================================
# 主页面
# ============================================

# 添加樱花装饰层
st.markdown("""
<div class="sakura-top"></div>
<div class="sakura-right"></div>
<div class="sakura-left"></div>
<div class="sakura-petal" style="left: 10%; animation-delay: 0s;"></div>
<div class="sakura-petal" style="left: 25%; animation-delay: 1.5s;"></div>
<div class="sakura-petal" style="left: 40%; animation-delay: 3s;"></div>
<div class="sakura-petal" style="left: 55%; animation-delay: 4.5s;"></div>
<div class="sakura-petal" style="left: 70%; animation-delay: 2s;"></div>
<div class="sakura-petal" style="left: 85%; animation-delay: 5.5s;"></div>
<div class="sakura-petal" style="left: 15%; animation-delay: 6s;"></div>
<div class="sakura-petal" style="left: 35%; animation-delay: 7.5s;"></div>
<div class="sakura-petal" style="left: 60%; animation-delay: 0.5s;"></div>
<div class="sakura-petal" style="left: 90%; animation-delay: 4s;"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-bottom:20px;">
    <h1>🌸 MBTI 人格测试仪</h1>
    <p style="color:#6A1B9A; font-size:1.1rem; letter-spacing:2px; font-weight:500;">
        发现你的真实人格类型 · 探索内心世界
    </p>
</div>
""", unsafe_allow_html=True)


# ============================================
# 测试流程
# ============================================
if not st.session_state.test_completed:
    # 显示当前问题
    current_q = QUESTIONS[st.session_state.current_question]
    
    st.markdown('<div class="test-card">', unsafe_allow_html=True)
    
    # 进度显示
    progress_pct = int((st.session_state.current_question + 1) / len(QUESTIONS) * 100)
    st.progress(progress_pct / 100)
    st.caption(f"📍 第 {st.session_state.current_question + 1} 题 / 共 {len(QUESTIONS)} 题")
    
    st.markdown("---")
    
    # 问题文本
    st.markdown(f"""
    <div class="question-text">
        <span style="color:#E91E63; font-weight:600;">Q{current_q['id']}.</span>
        {current_q['text']}
    </div>
    """, unsafe_allow_html=True)
    
    # 选项
    answer = st.radio(
        "请选择最符合你的选项：",
        options=list(current_q["options"].keys()),
        format_func=lambda x: f"{x}. {current_q['options'][x]}",
        key=f"q_{current_q['id']}"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 下一题按钮
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    
    with col_btn2:
        if st.button("➡️ 下一题", use_container_width=True):
            # 保存答案
            st.session_state.answers.append(answer)
            
            # 判断是否完成
            if st.session_state.current_question + 1 >= len(QUESTIONS):
                st.session_state.test_completed = True
                mbti_result, scores = calculate_mbti(st.session_state.answers)
                st.session_state.mbti_result = mbti_result
                st.session_state.scores = scores
            else:
                st.session_state.current_question += 1
            
            st.rerun()

else:
    # ============================================
    # 显示测试结果
    # ============================================
    mbti_type = st.session_state.mbti_result
    type_info = MBTI_TYPES[mbti_type]
    
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align:center;">
        <div style="font-size:3rem; margin-bottom:10px;">{type_info['emoji']}</div>
        <div class="mbti-type">{mbti_type}</div>
        <div class="mbti-name">{type_info['name']}</div>
        <p style="color:#616161; font-size:1.1rem; line-height:1.8; margin:20px 0;">
            {type_info['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 核心特质
    st.subheader("✨ 核心特质")
    traits_html = "".join([f'<span class="trait-tag">{t}</span>' for t in type_info['traits']])
    st.markdown(f'<div style="text-align:center; margin:15px 0;">{traits_html}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 优势与劣势
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background:rgba(233,30,99,0.1); padding:20px; border-radius:15px;">
            <h4 style="color:#E91E63; margin-bottom:10px;">💪 优势</h4>
            <p style="color:#616161;">{}</p>
        </div>
        """.format(type_info['strengths']), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background:rgba(255,182,193,0.2); padding:20px; border-radius:15px;">
            <h4 style="color:#AD1457; margin-bottom:10px;">⚠️ 注意事项</h4>
            <p style="color:#616161;">{}</p>
        </div>
        """.format(type_info['weaknesses']), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 适合职业
    st.subheader("💼 适合职业方向")
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, rgba(248,187,217,0.3), rgba(255,255,255,0.9)); 
                padding:20px; border-radius:15px; text-align:center;">
        <p style="color:#AD1457; font-size:1.1rem; font-weight:500;">{type_info['careers']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 维度得分详情
    st.subheader("📊 各维度倾向分析")
    scores = st.session_state.scores
    
    col_dim1, col_dim2, col_dim3, col_dim4 = st.columns(4)
    
    with col_dim1:
        ei_score = scores["EI"]
        ei_max = 16
        ei_pct = int(ei_score / ei_max * 100)
        st.metric("E/I 维度", f"{ei_pct}%")
        if ei_pct >= 50:
            st.caption("倾向：外向 E")
        else:
            st.caption("倾向：内向 I")
    
    with col_dim2:
        sn_score = scores["SN"]
        sn_max = 16
        sn_pct = int(sn_score / sn_max * 100)
        st.metric("S/N 维度", f"{sn_pct}%")
        if sn_pct >= 50:
            st.caption("倾向：感觉 S")
        else:
            st.caption("倾向：直觉 N")
    
    with col_dim3:
        tf_score = scores["TF"]
        tf_max = 12
        tf_pct = int(tf_score / tf_max * 100)
        st.metric("T/F 维度", f"{tf_pct}%")
        if tf_pct >= 50:
            st.caption("倾向：思考 T")
        else:
            st.caption("倾向：情感 F")
    
    with col_dim4:
        jp_score = scores["JP"]
        jp_max = 16
        jp_pct = int(jp_score / jp_max * 100)
        st.metric("J/P 维度", f"{jp_pct}%")
        if jp_pct >= 50:
            st.caption("倾向：判断 J")
        else:
            st.caption("倾向：知觉 P")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 重新测试按钮
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("🔄 重新测试", use_container_width=True):
            st.session_state.current_question = 0
            st.session_state.answers = []
            st.session_state.test_completed = False
            st.session_state.mbti_result = None
            st.rerun()


# ============================================
# 页脚
# ============================================
st.markdown("""
<div style="text-align:center; padding: 30px 0; margin-top: 20px;">
    <p style="color:rgba(233,30,99,0.5); font-size:0.85rem; letter-spacing:2px;">
        🌸 MBTI 人格测试仪 · 发现真实的自己 🌸
    </p>
    <p style="color:rgba(173,20,87,0.4); font-size:0.75rem; margin-top:10px;">
        基于 Myers-Briggs 类型指标 · 仅供娱乐参考
    </p>
</div>
""", unsafe_allow_html=True)
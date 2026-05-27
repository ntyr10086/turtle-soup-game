"""
AI海龜湯攻防戰 - 主程式
極致防禦版本
"""

import streamlit as st
import os
from dotenv import load_dotenv
from defense import DefenseSystem, PromptGuard, ResponseFilter
from game_logic import TurtleSoupGame
import time

# 載入環境變數
load_dotenv()

# 頁面設定
st.set_page_config(
    page_title="🐢 AI海龜湯攻防戰",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自訂CSS樣式
st.markdown("""
<style>
    /* 主標題樣式 */
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* 遊戲狀態卡片 */
    .status-card {
        padding: 1rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-bottom: 1rem;
    }
    
    /* 警告框 */
    .warning-box {
        padding: 1rem;
        border-left: 4px solid #FFA726;
        background-color: #FFF3E0;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* 成功框 */
    .success-box {
        padding: 1rem;
        border-left: 4px solid #66BB6A;
        background-color: #E8F5E9;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* 聊天訊息樣式 */
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .user-message {
        background-color: #E3F2FD;
        border-left: 4px solid #2196F3;
    }
    
    .assistant-message {
        background-color: #F3E5F5;
        border-left: 4px solid #9C27B0;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """初始化Session State"""
    if 'game' not in st.session_state:
        # 優先使用Streamlit Cloud secrets，其次使用本地.env
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
        except:
            api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            st.error("❌ 請先設定GEMINI_API_KEY！\n\n本地開發：設定.env檔案\nStreamlit Cloud：在App settings中設定Secrets")
            st.stop()
        st.session_state.game = TurtleSoupGame(api_key)
    
    if 'defense' not in st.session_state:
        st.session_state.defense = DefenseSystem()
    
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    
    if 'last_request_time' not in st.session_state:
        st.session_state.last_request_time = 0


def render_header():
    """渲染頁面標題"""
    st.markdown('<p class="main-title">🐢 AI海龜湯遊戲</p>', unsafe_allow_html=True)
    st.markdown("---")


def render_sidebar():
    """渲染側邊欄"""
    with st.sidebar:
        st.header("🎮 遊戲控制")
        
        # 題目選擇
        st.markdown("📖 **選擇題目**")
        
        puzzles = st.session_state.game.STORY_PUZZLES
        
        difficulty_filter = st.selectbox(
            "難度篩選",
            ["全部", "簡單", "中等", "困難"]
        )
        
        # 過濾題目
        if difficulty_filter == "全部":
            filtered_puzzles = puzzles
        else:
            filtered_puzzles = [p for p in puzzles if p["difficulty"] == difficulty_filter]
        
        # 顯示題目列表
        puzzle_options = [
            f"{p['title']} ({p['difficulty']})"
            for p in filtered_puzzles
        ]
        
        puzzle_index = None
        if puzzle_options:
            selected = st.selectbox("選擇一個題目", ["🎲 隨機選擇"] + puzzle_options)
            
            if selected != "🎲 隨機選擇":
                # 找到選中題目的索引
                selected_title = selected.split(" (")[0]
                puzzle_index = next(
                    (i for i, p in enumerate(puzzles) if p["title"] == selected_title),
                    None
                )
        
        # 開始遊戲按鈕
        if st.button("🎯 開始遊戲", use_container_width=True, type="primary"):
            st.session_state.game.start_new_game(puzzle_index=puzzle_index)
            st.session_state.defense.reset_defense()
            st.session_state.game_started = True
            st.rerun()
        
        st.markdown("---")
        
        # 遊戲狀態
        if st.session_state.game_started:
            st.header("📊 狀態")
            stats = st.session_state.game.get_game_stats()
            
            # 顯示題目資訊
            if stats.get("story_mode"):
                st.info(f"**{stats.get('puzzle_title', '未知')}**\n難度: {stats.get('difficulty', '未知')}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("提問次數", stats['attempts'])
            with col2:
                st.metric("提示次數", stats.get('hints_used', 0))
        
        st.markdown("---")
        
        # 遊戲規則
        with st.expander("📖 遊戲規則"):
            st.markdown("""
            ### 如何遊戲：
            
            1. AI 會給你一個故事情境
            2. 你需要透過提問找出真相
            3. AI 只會回答：**是**、**不是**、**不完全是**、**與題目無關**
            
            ### 特殊指令：
            - 輸入「引導」：獲得思路提示
            - 輸入「總結」：整理已知線索
            """)
        
        with st.expander("💡 遊戲技巧"):
            st.markdown("""
            1. 從大方向開始
            2. 注意事件順序
            3. 尋找隱藏人物
            4. 善用引導功能
            5. 定期整理線索
            """)


def render_chat_history():
    """渲染對話歷史"""
    if not st.session_state.game_started:
        st.info("👈 點左邊側欄的「開始遊戲」按鈕來開始！")
        return
    
    # 顯示對話歷史
    for message in st.session_state.game.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_input():
    """處理使用者輸入"""
    if not st.session_state.game_started:
        return
    
    # 檢查遊戲是否結束
    if st.session_state.game.is_game_over:
        st.success("🎉 遊戲已結束！請開始新遊戲")
        return
    
    # 聊天輸入框
    user_input = st.chat_input("請輸入你的問題（限200字）或輸入「引導」/「總結」...")
    
    if user_input:
        # === 檢查特殊指令 ===
        special_response = st.session_state.game.handle_special_command(user_input)
        if special_response:
            # 這是特殊指令，直接顯示回應
            with st.chat_message("user"):
                st.markdown(user_input)
            with st.chat_message("assistant"):
                st.markdown(special_response)
            
            st.session_state.game.add_to_history("user", user_input)
            st.session_state.game.add_to_history("assistant", special_response)
            st.rerun()
            return
        
        # === 防禦層級 1：請求延遲（防DDOS） ===
        current_time = time.time()
        time_since_last = current_time - st.session_state.last_request_time
        if time_since_last < 1.0:  # 1秒延遲
            remaining = 1.0 - time_since_last
            st.warning(f"⏱️ 請稍候 {remaining:.1f} 秒後再提問")
            time.sleep(remaining)
        
        st.session_state.last_request_time = time.time()
        
        # === 防禦層級 2：輸入安全檢查 ===
        is_safe, warning = st.session_state.defense.check_input_safety(user_input)
        if not is_safe:
            with st.chat_message("user"):
                st.markdown(user_input)
            with st.chat_message("assistant"):
                st.error(warning)
            
            # 記錄到歷史（但不發送到AI）
            st.session_state.game.add_to_history("user", user_input)
            st.session_state.game.add_to_history("assistant", warning)
            st.rerun()
            return
        
        # === 防禦層級 3：請求頻率限制 ===
        is_allowed, rate_warning = st.session_state.defense.check_rate_limit()
        if not is_allowed:
            with st.chat_message("user"):
                st.markdown(user_input)
            with st.chat_message("assistant"):
                st.error(rate_warning)
            
            st.session_state.game.add_to_history("user", user_input)
            st.session_state.game.add_to_history("assistant", rate_warning)
            st.rerun()
            return
        
        # 顯示使用者訊息
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # 添加到歷史
        st.session_state.game.add_to_history("user", user_input)
        
        # 檢查是否直接猜對答案
        if st.session_state.game.check_win_condition(user_input):
            win_message = f"🎉 **恭喜你猜對了！**\n\n"
            
            if st.session_state.game.story_mode:
                win_message += f"**真相是：**\n{st.session_state.game.secret_answer}\n\n"
                win_message += f"你總共問了 **{st.session_state.game.attempts}** 個問題"
                if st.session_state.game.hints_used > 0:
                    win_message += f"，使用了 **{st.session_state.game.hints_used}** 次提示"
                win_message += "！"
            else:
                win_message += f"答案就是「{st.session_state.game.secret_answer}」！\n\n"
                win_message += f"你總共問了 {st.session_state.game.attempts} 個問題。"
            
            with st.chat_message("assistant"):
                st.success(win_message)
            
            st.session_state.game.add_to_history("assistant", win_message)
            st.session_state.game.is_game_over = True
            st.balloons()  # 慶祝效果
            st.rerun()
            return
        
        # === 防禦層級 4：生成防護System Prompt ===
        story_context = ""
        if st.session_state.game.current_puzzle:
            story_context = st.session_state.game.current_puzzle["story"]
        
        system_prompt = PromptGuard.generate_system_prompt(
            st.session_state.game.secret_answer,
            True,  # 始終為 story_mode
            story_context
        )
        
        # 獲取AI回應
        with st.chat_message("assistant"):
            with st.spinner("AI思考中..."):
                ai_response = st.session_state.game.get_ai_response(
                    user_input, 
                    system_prompt
                )
                
                # === 防禦層級 5：輸出安全檢查 ===
                is_safe_output, filtered_response = st.session_state.defense.check_output_safety(
                    ai_response,
                    st.session_state.game.secret_answer
                )
                
                if not is_safe_output:
                    ai_response = filtered_response
                
                # === 防禦層級 6：強制回應格式 ===
                ai_response = ResponseFilter.enforce_valid_response(ai_response)
                
                st.markdown(ai_response)
        
        # 添加到歷史
        st.session_state.game.add_to_history("assistant", ai_response)
        
        # 重新渲染
        st.rerun()


def main():
    """主程式"""
    # 初始化
    initialize_session_state()
    
    # 渲染UI
    render_header()
    render_sidebar()
    
    # 主要內容區
    render_chat_history()
    handle_user_input()
    
    # 底部資訊
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🐢 AI海龜湯遊戲 | 2026學年度期末專題</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

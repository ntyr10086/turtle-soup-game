"""
AI海龜湯 - 遊戲邏輯模組
處理遊戲狀態、答案生成、對話管理
"""

import google.generativeai as genai
from typing import List, Dict, Optional
import random


class TurtleSoupGame:
    """海龜湯遊戲管理器"""
    
    # 真實海龜湯故事題目庫（參考專業網站，經過改編）
    STORY_PUZZLES = [
        # === 簡單級別 ===
        {
            "title": "100元錢",
            "story": "小明在圖書館看書，在一本書裡翻到了100塊錢，但是他卻哭了。",
            "answer": "這是小明自己之前當書籤用的錢，他找了很久以為丟了",
            "difficulty": "簡單",
            "tags": ["經典", "日常"]
        },
        {
            "title": "忠誠的狗",
            "story": "小強養了一隻很忠誠的狗，今天他牽著狗上街，然後小強死了。",
            "answer": "小強是盲人，狗看到紅燈但沒有攔住他，小強被車撞死了",
            "difficulty": "簡單",
            "tags": ["經典", "日常"]
        },
        {
            "title": "裤子破了",
            "story": "我的褲子破了，我知道我馬上要死了。",
            "answer": "我是跳傘運動員，降落傘破了",
            "difficulty": "簡單",
            "tags": ["經典", "生死"]
        },
        
        # === 中等級別 ===
        {
            "title": "看病",
            "story": "一個人坐火車去臨鎮看病，看完之後病全好了。回來的路上火車經過一個隧道，這個人就跳車自殺了。",
            "answer": "這個人眼睛瞎了去看病，醫生治好了他。回來時經過隧道一片漆黑，他以為自己又瞎了所以自殺",
            "difficulty": "中等",
            "tags": ["經典", "生死", "推理"]
        },
        {
            "title": "手滑",
            "story": "我在和閨蜜聊天，忽然手機掉在了地上。閨蜜嚇傻了。我死了。",
            "answer": "我們在玻璃棧道上，手機掉下去摔碎了，我看到下面是萬丈深淵嚇得腳軟掉下去了",
            "difficulty": "中等",
            "tags": ["生死", "懸疑"]
        },
        {
            "title": "治病",
            "story": "他決定給經濟拮据的母親治病，卻被母親強硬地拒絕了。",
            "answer": "母親需要換腎，兒子想捐腎給她，但母親其實是買來的，擔心暴露人口販賣罪行",
            "difficulty": "中等",
            "tags": ["推理", "家庭"]
        },
        {
            "title": "電梯習慣",
            "story": "一個人住17樓。下雨時他坐電梯到17樓，不下雨但有其他人時也到17樓，但不下雨且只有他時就只坐到11樓然後爬樓梯。",
            "answer": "他是矮人，按不到17樓按鈕。下雨有傘可以按，有其他人可以請人幫忙按",
            "difficulty": "中等",
            "tags": ["經典", "日常", "推理"]
        },
        
        # === 困難級別 ===
        {
            "title": "愛犬",
            "story": "一個女孩獨居，陪伴她的只有愛犬。半夜醒來，她聽到滴水聲很害怕，把手放到床邊讓愛犬舔了舔，又睡著了。第二天發現狗死了。",
            "answer": "舔她手的不是狗而是殺人犯，滴水聲是狗的血滴下來的聲音",
            "difficulty": "困難",
            "tags": ["恐怖", "推理", "生死"]
        },
        {
            "title": "脚步聲",
            "story": "每次單逐走路都能聽到兩個人的腳步聲，有一次終於變成一個人的了，我卻後悔了。",
            "answer": "我是盲人，一直聽到兩個腳步聲是因為有導盲犬。那次導盲犬死了，我很後悔",
            "difficulty": "困難",
            "tags": ["推理", "感人"]
        },
        {
            "title": "媽媽的反應",
            "story": "我哭了，媽媽笑了。我笑了，媽媽笑了。我哭了，媽媽哭了。我哭了，媽媽笑了。我笑了，媽媽笑了。我哭了，媽媽哭了。我哭了，媽媽笑了。",
            "answer": "媽媽在教我認識表情，前面都是對的所以她笑，第三次和第六次我哭了她也哭是因為我弄錯了她在示範正確的",
            "difficulty": "困難",
            "tags": ["推理", "家庭", "智力"]
        },
    ]
    
    def __init__(self, api_key: str):
        """
        初始化遊戲
        
        Args:
            api_key: Google Gemini API金鑰
        """
        # 設定API
        genai.configure(api_key=api_key)
        
        # 🛠️ 【已修復】將 model_name 改為符合 SDK 0.3.2 規範的 model 參數！
        self.model = genai.GenerativeModel(model='gemini-1.5-flash')
        
        # 遊戲狀態
        self.current_puzzle: Optional[Dict] = None  # 當前題目
        self.secret_answer: Optional[str] = None
        self.story_mode = False  # 是否為故事模式
        self.chat_history: List[Dict[str, str]] = []
        self.is_game_over = False
        self.attempts = 0
        self.hints_used = 0  # 使用的提示次數
        
    def start_new_game(self, mode: str = "story", puzzle_index: Optional[int] = None):
        """
        開始新遊戲
        
        Args:
            mode: 遊戲模式 ("story" 或 "simple")
            puzzle_index: 指定題目索引（故事模式用）
        """
        # 重置狀態
        self.chat_history = []
        self.is_game_over = False
        self.attempts = 0
        self.hints_used = 0
        
        if mode == "story":
            # 故事模式：使用真實海龜湯題目
            self.story_mode = True
            if puzzle_index is not None and 0 <= puzzle_index < len(self.STORY_PUZZLES):
                self.current_puzzle = self.STORY_PUZZLES[puzzle_index]
            else:
                self.current_puzzle = random.choice(self.STORY_PUZZLES)
            
            self.secret_answer = self.current_puzzle["answer"]
            
            # 添加開場訊息
            opening = f"""🎮 遊戲開始！

📖 **{self.current_puzzle['title']}**
難度：{self.current_puzzle['difficulty']} | 標籤：{', '.join(self.current_puzzle['tags'])}

**故事情境：**
{self.current_puzzle['story']}

---

💡 你可以開始提問了！我只會回答：是、不是、不完全是、或與題目無關。

✨ **特殊指令**：
- 輸入「引導」獲得思路提示
- 輸入「總結」讓我整理目前的線索"""
            
        else:
            # 簡單模式：使用簡單答案（為了測試）
            self.story_mode = False
            self.current_puzzle = None
            simple_topics = ["籃球", "蘋果", "獅子", "雨傘", "腳踏車"]
            self.secret_answer = random.choice(simple_topics)
            
            opening = f"""🎮 遊戲開始！（簡單模式）

我已經想好一個謎底了，請開始提問吧！

💡 提示：你可以問任何「是非題」，我只會回答：是、不是、不完全是、或與題目無關。"""
        
        self.chat_history.append({
            "role": "assistant",
            "content": opening
        })
    
    def build_conversation_context(self) -> List[Dict[str, str]]:
        """
        建立對話上下文（包含歷史記錄）
        
        Returns:
            完整對話歷史
        """
        # 這裡將歷史對話轉換成Gemini API需要的格式
        context = []
        for msg in self.chat_history:
            if msg["role"] == "user":
                context.append({
                    "role": "user",
                    "parts": [msg["content"]]
                })
            elif msg["role"] == "assistant":
                context.append({
                    "role": "model",
                    "parts": [msg["content"]]
                })
        
        return context
    
    def get_ai_response(self, user_question: str, system_prompt: str) -> str:
        """
        獲取AI回應
        
        Args:
            user_question: 使用者問題
            system_prompt: 系統提示詞
            
        Returns:
            AI回應
        """
        try:
            # 建立完整的對話歷史
            full_conversation = self.build_conversation_context()
            
            # 🛠️ 【優化優化】配合 0.3.2 版本的初始化對話策略，動態套用 system_instruction
            if len(full_conversation) == 0:
                full_conversation.insert(0, {
                    "role": "user",
                    "parts": [system_prompt]
                })
                full_conversation.append({
                    "role": "model", 
                    "parts": ["我明白了，我會嚴格遵守規則，絕不洩漏答案。讓我們開始遊戲！"]
                })
            
            # 添加使用者問題
            full_conversation.append({
                "role": "user",
                "parts": [user_question]
            })
            
            # 呼叫API
            chat = self.model.start_chat(history=full_conversation[:-1])
            response = chat.send_message(user_question)
            
            return response.text.strip()
            
        except Exception as e:
            return f"系統錯誤：{str(e)}"
    
    def add_to_history(self, role: str, content: str):
        """
        添加訊息到歷史記錄
        
        Args:
            role: 角色 ('user' 或 'assistant')
            content: 訊息內容
        """
        self.chat_history.append({
            "role": role,
            "content": content
        })
        
        if role == "user":
            self.attempts += 1
    
    def check_win_condition(self, user_input: str) -> bool:
        """
        檢查玩家是否猜對
        
        Args:
            user_input: 使用者輸入
            
        Returns:
            是否猜對
        """
        if not self.secret_answer:
            return False
        
        # 移除標點符號和空格，進行模糊比對
        user_clean = user_input.replace(" ", "").replace("?", "").replace("？", "").lower()
        answer_clean = self.secret_answer.lower()
        
        # 對於故事模式，檢查是否包含關鍵詞
        if self.story_mode:
            # 提取答案中的關鍵詞
            answer_keywords = [w for w in answer_clean.split() if len(w) > 2]
            return any(keyword in user_clean for keyword in answer_keywords if len(keyword) > 2)
        else:
            return answer_clean in user_clean
    
    def handle_special_command(self, user_input: str) -> Optional[str]:
        """
        處理特殊指令（引導、總結等）
        
        Args:
            user_input: 使用者輸入
            
        Returns:
            特殊指令的回應，如果不是特殊指令則返回None
        """
        user_clean = user_input.strip().lower().replace(" ", "")
        
        # 引導指令
        if any(word in user_clean for word in ["引導", "提示", "hint", "guide"]):
            self.hints_used += 1
            if self.story_mode and self.current_puzzle:
                hints = [
                    "從大方向思考：這個故事中有沒有隱藏的人物或事件？",
                    "注意時間順序：事情發生的先後順序是關鍵嗎？",
                    "換個角度：如果從另一個人的視角來看，會發現什麼？",
                    "注意細節：故事中提到的每個物品或動作都有意義嗎？",
                    "因果關係：為什麼會導致這樣的結果？是否有特殊原因？"
                ]
                return f"💡 **引導提示 #{self.hints_used}**\n\n{random.choice(hints)}\n\n繼續提問來接近真相吧！"
            else:
                return "💡 從大方向開始：這個東西的類別是什麼？它的用途是什麼？"
        
        # 總結指令
        if any(word in user_clean for word in ["總結", "整理", "線索", "summary"]):
            # 從對話歷史中提取「是」的回答
            clues = []
            for i, msg in enumerate(self.chat_history):
                if msg["role"] == "assistant" and i > 0:
                    prev_msg = self.chat_history[i-1]
                    if prev_msg["role"] == "user":
                        if "是" in msg["content"] and "不是" not in msg["content"]:
                            clues.append(f"✓ {prev_msg['content']}")
            
            if clues:
                summary = "📋 **目前已確認的線索：**\n\n" + "\n".join(clues[-5:])  # 只顯示最近5條
                summary += f"\n\n已提問 {self.attempts} 次，使用了 {self.hints_used} 次提示"
                return summary
            else:
                return "📋 目前還沒有確認的線索，繼續提問吧！"
        
        return None
    
    def get_game_stats(self) -> Dict:
        """
        獲取遊戲統計
        
        Returns:
            統計資訊
        """
        stats = {
            "attempts": self.attempts,
            "hints_used": self.hints_used,
            "is_game_over": self.is_game_over,
            "chat_length": len(self.chat_history),
            "story_mode": self.story_mode
        }
        
        if self.story_mode and self.current_puzzle:
            stats.update({
                "puzzle_title": self.current_puzzle["title"],
                "difficulty": self.current_puzzle["difficulty"],
                "tags": self.current_puzzle["tags"]
            })
        
        return stats

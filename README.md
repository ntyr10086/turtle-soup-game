# 🐢 AI海龜湯攻防戰

> 2026學年度期末專題：結合生成式AI應用與資訊安全防禦的互動式遊戲系統

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![Google Gemini API](https://img.shields.io/badge/API-Google%20Gemini-4285F4.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 專題簡介

這是一個結合**AI對話系統**與**資訊安全防禦**的互動式海龜湯遊戲。本系統採用**多層防禦機制**，能有效抵擋提示注入攻擊（Prompt Injection），同時提供流暢的遊戲體驗。

### 🎯 核心特色

- **🎭 真實海龜湯故事** - 10+精選故事題目，從簡單到困難
- **💡 智能引導系統** - 玩家可請求提示而不洩漏答案
- **📋 線索總結功能** - 自動整理已確認的線索
- **🎮 雙遊戲模式** - 故事模式（專業體驗）+ 簡單模式（測試）
- **🛡️ 極致防禦機制** - 6層防護，抵擋各種提示注入攻擊
- **🌐 在線部署** - 支援 Hugging Face Spaces / Railway

---

## 🚀 快速開始

### 1. 本地運行

#### 環境需求
- Python 3.8 或以上
- pip（Python套件管理器）

#### 安裝步驟

```bash
# 複製或下載專案
git clone https://github.com/你的用戶名/turtle-soup-game.git
cd turtle_soup_game

# 安裝依賴
pip install -r requirements.txt

# 設定 API 金鑰
# 1. 複製 .env.example 為 .env
cp .env.example .env

# 2. 編輯 .env，添加你的 Gemini API 金鑰
# GEMINI_API_KEY=your_api_key_here

# 3. 啟動應用
streamlit run app.py
```

應用將在 `http://localhost:8501` 開啟

### 2. 在線部署（推薦）

#### 最簡單的方式：Hugging Face Spaces

```bash
# 只需 3 步：
1. 推送代碼到 GitHub
2. 在 Hugging Face 建立 Space
3. 連接 GitHub Repository
# 完成！應用自動部署並自動更新
```

[詳細部署教學 →](./DEPLOY.md)

---

## 📋 檔案結構

```
turtle_soup_game/
├── app.py                 # 🎨 Streamlit 主應用
├── game_logic.py          # 🎮 遊戲邏輯模組
├── defense.py             # 🛡️ 防禦系統模組
├── requirements.txt       # 📦 依賴套件清單
├── .env.example          # 🔑 環境變數範例
├── .gitignore            # 📝 Git 忽略清單
├── README.md             # 📖 此檔案（GitHub版）
├── DEPLOY.md             # 🚀 部署教學
├── UPGRADE_NOTES.md      # ✨ 升級說明
├── setup_guide.md        # 📚 詳細安裝指引
└── attack_test.py        # 🧪 攻擊測試工具
```

---

## 🎮 遊戲玩法

### 故事模式

1. **選擇難度**（簡單/中等/困難）
2. **選擇或隨機一個故事**
3. **開始推理**：提問→AI回答→分析線索
4. **使用特殊指令**：
   - 輸入「引導」獲得思路提示
   - 輸入「總結」整理已知線索

### 範例題目

**簡單級別：** 100元錢、忠誠的狗、褲子破了

**困難級別：** 愛犬、腳步聲、媽媽的反應

---

## 🛡️ 防禦機制

本系統採用**6層防禦架構**：

| 防禦層 | 機制 | 防護目標 |
|--------|------|---------|
| **第1層** | 請求延遲 | 防止 DDOS |
| **第2層** | 輸入安全檢查 | 過濾惡意關鍵字 |
| **第3層** | 頻率限制 | 1分鐘最多30次 |
| **第4層** | System Prompt 防護 | 多重防禦指令 |
| **第5層** | 輸出安全檢測 | 防止答案洩漏 |
| **第6層** | 回應格式強制 | 確保遊戲規則 |

---

## 📊 技術堆疊

- **前端**：Streamlit 1.31.0+
- **後端**：Python 3.8+
- **AI API**：Google Gemini
- **部署**：Hugging Face Spaces / Railway

---

## 📖 文件導航

| 文件 | 用途 |
|------|------|
| [DEPLOY.md](./DEPLOY.md) | 📚 完整部署教學（GitHub + Hugging Face） |
| [setup_guide.md](./setup_guide.md) | 📖 詳細安裝指引（適合初學者） |
| [UPGRADE_NOTES.md](./UPGRADE_NOTES.md) | ✨ 系統升級說明 |
| [README_LOCAL.md](./README_LOCAL.md) | 💻 本地開發說明 |

---

## ⚔️ 期末競賽

### 防守方（藍軍）
- 部署到在線平台
- 用 `attack_test.py` 測試防禦
- 用新 Google 帳號確保 Token 充足

### 進攻方（紅隊）
- 參考 `attack_test.py` 中的攻擊樣本
- 進行系統化提示注入攻擊
- 記錄攻擊過程

---

## ❓ 常見問題

**Q: API 配額不足？**
A: 使用新 Google 帳號申請 API 金鑰

**Q: 怎樣添加新題目？**
A: 編輯 `game_logic.py` 中的 `STORY_PUZZLES`

**Q: 部署失敗？**
A: 查看 [DEPLOY.md](./DEPLOY.md) 的常見問題排解章節

---

## 📄 授權

MIT License

---

## 🎊 開始遊戲

```bash
streamlit run app.py
```

或訪問線上版本：[Hugging Face Space]（部署後獲得連結）

---

<div align="center">

**[🚀 部署教學](./DEPLOY.md) | [📚 安裝指引](./setup_guide.md) | [✨ 升級說明](./UPGRADE_NOTES.md)**

Made with ❤️ for educational purposes

</div>

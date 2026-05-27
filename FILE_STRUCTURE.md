# 📁 完整檔案結構與說明

你已下載的所有檔案及其用途

---

## 📦 核心程式檔案（3個 - 必要）

### 1. **app.py** (14 KB)
🎨 **Streamlit 主應用程式**

- UI 介面設計
- 遊戲流程控制  
- 使用者輸入處理
- 聊天訊息顯示

**何時修改**：想改變 UI 風格、添加新功能

---

### 2. **game_logic.py** (14 KB)
🎮 **遊戲邏輯模組**

- 10+海龜湯故事題目庫
- AI 對話管理
- 勝負判定
- 引導與線索總結
- 遊戲狀態追蹤

**何時修改**：想添加新題目、改變遊戲規則

---

### 3. **defense.py** (11 KB)
🛡️ **極致防禦系統**

- 6層防護機制
- 輸入安全檢查
- 惡意關鍵字過濾（100+）
- 請求頻率限制
- 輸出安全檢測
- System Prompt 防護

**何時修改**：想加強防禦、添加新防護規則

---

## 🔧 設定檔案（2個 - 必要）

### 4. **.env.example** (127 字元)
🔑 **環境變數範本**

```
GEMINI_API_KEY=your_api_key_here
```

**使用方式**：
1. 複製此檔案
2. 重新命名為 `.env`
3. 將 `your_api_key_here` 替換成你的 API 金鑰
4. **絕對不要上傳 .env 到 GitHub！**

**重要**：`.gitignore` 已設定自動忽略 `.env`

---

### 5. **requirements.txt** (189 字元)
📦 **Python 套件清單**

```
streamlit==1.31.0
google-generativeai==0.3.2
python-dotenv==1.0.0
```

**使用方式**：
```bash
pip install -r requirements.txt
```

**何時修改**：需要額外的 Python 套件時

---

### 6. **.gitignore** (579 字元)
📝 **Git 忽略清單**

防止敏感檔案上傳到 GitHub：
- `.env` - API 金鑰
- `__pycache__/` - Python 快取
- `.streamlit/secrets.toml` - 敏感設定
- 虛擬環境資料夾等

**重要**：不要修改或刪除此檔案！

---

## 📚 文件檔案（5個 - 參考用）

### 7. **README.md** (5.1 KB)
📖 **GitHub 專案主頁**

GitHub 上面的專案說明，包含：
- 專題簡介
- 快速開始指南
- 技術堆疊
- 常見問題

**用途**：別人訪問你的 GitHub 時會看到

---

### 8. **GITHUB_UPLOAD_GUIDE.md** ⭐ **優先閱讀**
🚀 **GitHub 上傳與部署快速指南**

**最重要的檔案！** 包含：
- 為什麼不用 Vercel
- 為什麼推薦 Hugging Face Spaces
- 5 分鐘快速部署流程
- 常見錯誤排解

**首次部署時必讀！**

---

### 9. **DEPLOY.md** (8.2 KB)
📚 **完整部署教學**

詳細的部署步驟，包含：
- Hugging Face Spaces 教學
- Railway 備選方案
- 詳細的每一步說明
- 常見問題排解
- 環境變數設定

**深度參考**：需要詳細說明時查看

---

### 10. **setup_guide.md** (7.1 KB)
🎓 **本地安裝詳細指引**

適合初學者的步驟教學：
- Python 安裝（Windows/Mac）
- 套件安裝
- API 金鑰配置
- 常見錯誤解決
- 逐步截圖式說明

**新手必讀**：不清楚如何安裝時使用

---

### 11. **UPGRADE_NOTES.md** (6.5 KB)
✨ **系統升級說明**

說明根據專業海龜湯網站進行的改進：
- 從簡單答案→真實故事
- 新增功能詳解
- 題目推薦
- 技術改進說明

**參考用**：了解系統設計思路

---

### 12. **README_LOCAL.md**
💻 **本地開發說明**

本地運行和開發的說明

---

## 🧪 測試與分析工具（1個）

### 13. **attack_test.py** (4.8 KB)
🔍 **攻擊測試工具**

包含：
- 25+常見提示注入攻擊樣本
- 防禦關鍵字測試
- 針對性攻擊生成器

**用途**：
```bash
python attack_test.py
```

**測試防禦機制**、準備期末競賽

---

## 📊 檔案使用流程

### 🔷 初次安裝（第 1 天）

```
1. 讀 GITHUB_UPLOAD_GUIDE.md (5分鐘) ⭐
   └─> 決定用本地運行或部署

2A. 本地運行：讀 setup_guide.md
    └─> pip install -r requirements.txt
    └─> cp .env.example .env
    └─> streamlit run app.py

2B. 線上部署：
    └─> 上傳到 GitHub
    └─> 在 Hugging Face Spaces 部署
    └─> 設定 API 金鑰
```

### 🔷 開發與測試（第 2-7 天）

```
1. 修改 app.py / game_logic.py / defense.py

2. 用 attack_test.py 測試防禦
   └─> python attack_test.py

3. 本地測試 (streamlit run app.py)

4. 如果部署在 Hugging Face：
   └─> git push 到 GitHub
   └─> Hugging Face 自動更新
```

### 🔷 期末展示（第 8 天）

```
1. 準備展示 URL（如果部署了）

2. 演示遊戲玩法（故事模式）

3. 展示防禦機制（用 attack_test.py 的例子）

4. 解釋代碼結構（用這份檔案說明）
```

---

## 🎯 重要檔案優先級

### 必讀順序：

1. ⭐⭐⭐ **GITHUB_UPLOAD_GUIDE.md** - 首先了解部署方案
2. ⭐⭐⭐ **setup_guide.md** - 如果本地安裝遇到困難
3. ⭐⭐ **README.md** - 了解專題概況
4. ⭐ **DEPLOY.md** - 深度部署問題排解
5. **UPGRADE_NOTES.md** - 了解系統設計

### 參考用：

- **README_LOCAL.md** - 本地開發說明
- **attack_test.py** - 測試防禦機制
- **app.py / game_logic.py / defense.py** - 需要修改程式時

---

## 💾 本地檔案結構

下載後應該是這樣：

```
downloads/
└── turtle_soup_game/
    ├── app.py                    # 核心程式
    ├── game_logic.py             # 核心程式
    ├── defense.py                # 核心程式
    ├── requirements.txt          # 套件清單
    ├── .env.example             # API 金鑰範本
    ├── .gitignore               # Git 忽略清單
    ├── README.md                # GitHub 說明
    ├── GITHUB_UPLOAD_GUIDE.md   # ⭐ 優先讀
    ├── setup_guide.md           # 安裝指引
    ├── DEPLOY.md                # 部署教學
    ├── UPGRADE_NOTES.md         # 升級說明
    ├── README_LOCAL.md          # 本地說明
    └── attack_test.py           # 測試工具
```

---

## ✅ 準備檢查清單

下載後確認：

- [ ] 所有 13 個檔案都已下載
- [ ] `.env.example` 存在（不要刪除！）
- [ ] `.gitignore` 存在（不要刪除！）
- [ ] 沒有 `.env` 檔案（會在本地建立）
- [ ] 沒有 `__pycache__` 資料夾

---

## 🚀 接下來的步驟

### 選項 A：本地運行（立即使用）

```bash
cd turtle_soup_game
pip install -r requirements.txt
cp .env.example .env
# 編輯 .env，添加 API 金鑰
streamlit run app.py
```

[詳細教學 → setup_guide.md](./setup_guide.md)

### 選項 B：部署到網路（推薦）

1. 讀 [GITHUB_UPLOAD_GUIDE.md](./GITHUB_UPLOAD_GUIDE.md) (5分鐘)
2. 上傳到 GitHub (2分鐘)
3. 在 Hugging Face Spaces 部署 (2分鐘)

[快速部署指南 → GITHUB_UPLOAD_GUIDE.md](./GITHUB_UPLOAD_GUIDE.md)

---

## 💡 提示

- **首次部署遇到問題？** → 查看 GITHUB_UPLOAD_GUIDE.md 的常見錯誤
- **想理解代碼？** → 閱讀 UPGRADE_NOTES.md 了解各模組功能
- **想測試防禦？** → 執行 `python attack_test.py`
- **想修改題目？** → 編輯 game_logic.py 的 STORY_PUZZLES
- **想改變 UI？** → 編輯 app.py 的樣式和配置

---

## 🎊 準備好了嗎？

**選擇你的路徑：**

👉 **我要立即玩遊戲** → [setup_guide.md](./setup_guide.md)

👉 **我要部署到網路** → [GITHUB_UPLOAD_GUIDE.md](./GITHUB_UPLOAD_GUIDE.md)

👉 **我要深入了解** → [DEPLOY.md](./DEPLOY.md)

👉 **我要測試防禦** → `python attack_test.py`

---

**祝你部署順利！期末專題大獲全勝！🚀**

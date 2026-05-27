# 🚀 START HERE - 開始使用指南

> **⏰ 5分鐘快速開始**

---

## 你現在擁有的是什麼？

✅ **完整的 AI 海龜湯遊戲系統**
- 真實故事題目（10+個）
- 6層極致防禦機制
- 引導和線索總結功能
- 可部署到網路

✅ **所有部署所需的檔案**
- 程式碼（app.py, game_logic.py, defense.py）
- 設定檔案（.env.example, requirements.txt, .gitignore）
- 完整文件（5個教學 + 2個部署指南）

---

## 🎯 你想做什麼？

### 選項 A：立即在電腦上玩遊戲
⏱️ **5 分鐘內完成**

```bash
# 1. 進入資料夾
cd turtle_soup_game

# 2. 安裝套件
pip install -r requirements.txt

# 3. 設定 API 金鑰
# - 複製 .env.example 為 .env
# - 在 .env 中填入你的 Google Gemini API 金鑰

# 4. 執行遊戲
streamlit run app.py
```

遊戲會在 `http://localhost:8501` 開啟

[詳細教學 →](./setup_guide.md)

---

### 選項 B：部署到網路（推薦！）
⏱️ **10 分鐘內完成**

**為什麼推薦？**
- 任何人都能玩（有網路即可）
- 可以展示給老師和朋友
- 適合期末報告展示
- GitHub 自動更新

**三步驟部署：**

1. **上傳到 GitHub**（2分鐘）
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <你的GitHub URL>
   git push -u origin main
   ```

2. **在 Hugging Face 建立 Space**（2分鐘）
   - 登入 [Hugging Face](https://huggingface.co)
   - 點 `New Space` → 選 `Streamlit`
   - 連接你的 GitHub Repository

3. **設定 API 金鑰**（2分鐘）
   - 在 Space Settings 的 Secrets 中
   - 添加 `GEMINI_API_KEY`

完成！應用自動上線 🚀

[快速部署指南 →](./GITHUB_UPLOAD_GUIDE.md)

---

## 📚 文件導航

### 🔴 優先閱讀（必讀）

| 檔案 | 用途 | 何時讀 |
|------|------|--------|
| **[GITHUB_UPLOAD_GUIDE.md](./GITHUB_UPLOAD_GUIDE.md)** | 5分鐘快速部署 | 想部署到網路時 |
| **[setup_guide.md](./setup_guide.md)** | 詳細安裝教學 | 本地安裝遇到困難 |
| **[FILE_STRUCTURE.md](./FILE_STRUCTURE.md)** | 檔案說明 | 想了解各檔案作用 |

### 🟡 參考閱讀（可選）

| 檔案 | 用途 |
|------|------|
| [DEPLOY.md](./DEPLOY.md) | 深度部署教學（含Railway等替代方案） |
| [README.md](./README.md) | 專題完整說明（GitHub上顯示） |
| [UPGRADE_NOTES.md](./UPGRADE_NOTES.md) | 系統升級說明 |

### 🟢 工具檔案

| 檔案 | 用途 |
|------|------|
| [attack_test.py](./attack_test.py) | 測試防禦機制（執行：`python attack_test.py`） |

---

## ⚠️ 重要事項

### ❌ 不要忘記設定 API 金鑰

**本地運行：**
```bash
# 1. 複製 .env.example
cp .env.example .env

# 2. 編輯 .env，填入你的 API 金鑰
# GEMINI_API_KEY=your_api_key_here
```

**部署到 Hugging Face：**
在 Space Settings → Secrets 中設定 `GEMINI_API_KEY`

### ❌ 絕對不要上傳 .env 到 GitHub！

`.gitignore` 已經設定好，會自動忽略 `.env` 檔案。

確認：`.gitignore` 中包含 `.env`

---

## 🎮 開始使用

### 路徑 1：本地玩遊戲

```bash
pip install -r requirements.txt
cp .env.example .env
# 編輯 .env，填入 API 金鑰
streamlit run app.py
# 訪問 http://localhost:8501
```

### 路徑 2：部署到網路

```bash
# 上傳到 GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin <URL>
git push

# 在 Hugging Face Spaces 建立 Space
# 連接 GitHub Repository
# 設定 GEMINI_API_KEY Secret
# 完成！
```

---

## 📊 檔案清單

你已下載：

```
✅ app.py                    # 主程式
✅ game_logic.py             # 遊戲邏輯（10個故事題目）
✅ defense.py                # 防禦系統（6層防護）
✅ requirements.txt          # 套件清單
✅ .env.example             # API金鑰範本
✅ .gitignore               # Git忽略清單
✅ README.md                # GitHub 說明
✅ setup_guide.md           # 安裝教學
✅ DEPLOY.md                # 部署詳細教學
✅ GITHUB_UPLOAD_GUIDE.md   # GitHub快速部署
✅ FILE_STRUCTURE.md        # 檔案結構說明
✅ UPGRADE_NOTES.md         # 升級說明
✅ README_LOCAL.md          # 本地開發說明
✅ attack_test.py           # 攻擊測試工具
```

共 14 個檔案

---

## ❓ 常見問題

### Q: 哪個方案最簡單？
**A:** Hugging Face Spaces 部署最簡單，而且完全免費。

### Q: 可以用 Vercel 嗎？
**A:** 不能。Vercel 不支援 Streamlit（需要改寫為 Flask/Next.js）。推薦用 Hugging Face Spaces。

### Q: 如何添加新題目？
**A:** 編輯 `game_logic.py` 的 `STORY_PUZZLES` 字典，添加新故事。

### Q: API 金鑰如何獲得？
**A:** 前往 [Google AI Studio](https://aistudio.google.com/app/apikey)，點擊「Create API Key」。

### Q: 遇到錯誤怎麼辦？
**A:** 
- 本地錯誤 → 查看 [setup_guide.md](./setup_guide.md)
- 部署錯誤 → 查看 [GITHUB_UPLOAD_GUIDE.md](./GITHUB_UPLOAD_GUIDE.md)
- 深度問題 → 查看 [DEPLOY.md](./DEPLOY.md)

---

## 🎯 接下來的步驟

### 🚀 立即開始（選一個）

**本地玩：**
```bash
cd turtle_soup_game
pip install -r requirements.txt
cp .env.example .env
# 編輯 .env
streamlit run app.py
```

**部署到網路：**
讀 [GITHUB_UPLOAD_GUIDE.md](./GITHUB_UPLOAD_GUIDE.md)（5分鐘，然後就能部署了）

### 📖 學習更多

- 想了解防禦機制？→ 執行 `python attack_test.py`
- 想修改遊戲？→ 編輯 `game_logic.py`
- 想改 UI？→ 編輯 `app.py`

### 📤 準備期末

- 應用已部署到網路 ✓
- API 金鑰已安全設定 ✓
- GitHub 已設置自動更新 ✓
- 防禦機制已測試 ✓
- 準備展示給老師 ✓

---

## 💪 你已經準備好了！

這不只是一個作業，這是一個**真正的產品級應用**：

✅ 功能完整（真實故事、引導、線索總結）  
✅ 設計專業（優美 UI、完整防禦）  
✅ 技術先進（6層防護、安全防禦）  
✅ 可部署（支援多個平台）  
✅ 文件齊全（14個檔案的完整說明）

---

## 🎊 祝你順利！

**選擇你的下一步：**

👉 [本地安裝教學](./setup_guide.md) - 5分鐘內在電腦上玩

👉 [快速部署指南](./GITHUB_UPLOAD_GUIDE.md) - 10分鐘內部署到網路（推薦！）

👉 [完整文件導航](./FILE_STRUCTURE.md) - 了解所有檔案

---

<div align="center">

**期末專題大獲全勝！🏆**

Made with ❤️ for your success

</div>

# 🚀 GitHub 上傳與 Vercel/Hugging Face 部署快速指南

> ⏱️ 預計時間：**5 分鐘**

---

## ⚠️ 重要說明

**Vercel 無法部署 Streamlit 應用！** 原因：
- Vercel 主要用於靜態網站和 Node.js
- Streamlit 需要 Python 運行環境
- Vercel 的函數有 10 秒超時限制，Streamlit 需要持久連接

✅ **推薦方案**：使用 **Hugging Face Spaces**（完全免費且專為此設計）

---

## 📋 你現在擁有的檔案

下載的檔案包括：

```
✅ app.py                    # Streamlit 主應用
✅ game_logic.py             # 遊戲邏輯（含10個故事題目）
✅ defense.py                # 6層防禦系統
✅ requirements.txt          # Python 套件清單
✅ .env.example             # API 金鑰範本
✅ .gitignore               # Git 忽略清單
✅ README.md                # 專案說明
✅ DEPLOY.md                # 完整部署教學
✅ setup_guide.md           # 本地安裝指引
✅ attack_test.py           # 攻擊測試工具
```

---

## 🔥 極速部署流程

### 準備工作（1 分鐘）

確認你有：
- [ ] GitHub 帳號（免費）
- [ ] Hugging Face 帳號（免費）  
- [ ] Google Gemini API 金鑰（免費）

### Step 1️⃣：本地準備（1 分鐘）

```bash
# 將所有下載的檔案放在同一個資料夾
# 資料夾結構應該是：
# turtle_soup_game/
#   ├── app.py
#   ├── game_logic.py
#   ├── defense.py
#   ├── requirements.txt
#   ├── .env.example
#   ├── .gitignore
#   └── ...其他檔案

cd turtle_soup_game
```

### Step 2️⃣：上傳到 GitHub（2 分鐘）

```bash
# 初始化 Git
git init
git add .
git commit -m "Initial commit: AI 海龜湯遊戲"

# 登入 GitHub，建立新 Repository（不要 init）
# 複製 Repository URL（例如：https://github.com/你的用戶名/turtle-soup-game.git）

# 推送程式碼
git remote add origin <你的Repository URL>
git branch -M main
git push -u origin main
```

### Step 3️⃣：在 Hugging Face 部署（2 分鐘）

#### 3.1 建立 Space

1. 登入 [Hugging Face](https://huggingface.co)
2. 點 `+` 號 → `New Space`
3. 填寫：
   - **Space name**: `turtle-soup-game`
   - **SDK**: `Streamlit` ⭐
   - **Private**: ✓ 勾選
4. 點 `Create Space`

#### 3.2 連接 GitHub（自動更新）

進入 Space 後：

```
Settings → Linked Repo → 輸入 GitHub Repository URL → Save
```

✅ **完成！**應用自動構建並部署

#### 3.3 設定 API 金鑰

```
Settings → Secrets → New secret
  Key: GEMINI_API_KEY
  Value: <貼入你的 Google Gemini API 金鑰>
```

✅ **部署完成！** 遊戲現在在線運行

---

## 🎮 測試你的部署

進入你的 Space URL（例如：`https://huggingface.co/spaces/你的用戶名/turtle-soup-game`）

測試：
- [ ] 應用成功載入（不是 ERROR）
- [ ] 能選擇遊戲模式
- [ ] 能開始遊戲
- [ ] 能提問並獲得回答

---

## 📱 分享連結

你的遊戲 URL：
```
https://huggingface.co/spaces/你的用戶名/turtle-soup-game
```

分享給：
- 👨‍🎓 老師（課堂展示）
- 👫 朋友（一起玩）
- 📝 期末報告（嵌入 iframe 或連結）

---

## 🔄 之後的更新

完成上述設定後，流程變簡單了：

```
修改程式碼 → git push → Hugging Face 自動更新 → 應用自動上線
```

無需手動操作！

---

## ⚠️ 常見錯誤

### ❌ Build 失敗（紅色 ERROR）

```bash
# 檢查 requirements.txt 中的套件版本
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Fix: Update dependencies"
git push
```

### ❌ 應用空白或無法連接

1. 檢查 Space Settings → Secrets
2. 確認 `GEMINI_API_KEY` 已添加
3. 點 Space 的 "Restart" 按鈕

### ❌ API 超時或 Token 用完

使用新 Google 帳號申請新的 API 金鑰，更新 Secrets

---

## 🆚 為什麼不用 Vercel？

| 功能 | Hugging Face | Vercel |
|------|-------------|---------|
| Streamlit 支援 | ✅ | ❌ |
| Python 環境 | ✅ | ❌ |
| 實時對話 | ✅ | ❌ |
| 設定難度 | 極簡單 | 需改寫整個專案 |

**結論**：Vercel 不適合 Streamlit。用 Hugging Face！

---

## 📚 詳細文件

- **[DEPLOY.md](./DEPLOY.md)** - 完整部署教學
- **[setup_guide.md](./setup_guide.md)** - 本地安裝指引
- **[GITHUB_DEPLOYMENT.md](./GITHUB_DEPLOYMENT.md)** - GitHub 詳細說明
- **[README_LOCAL.md](./README_LOCAL.md)** - 本地開發說明

---

## ✅ 檢查清單

上傳前：
- [ ] 所有檔案都已下載
- [ ] `.gitignore` 在資料夾中
- [ ] `.env.example` 在資料夾中
- [ ] 沒有 `.env` 檔案（API 金鑰不要上傳！）

部署後：
- [ ] GitHub Repository 建立並推送
- [ ] Hugging Face Space 建立
- [ ] GitHub 連接到 Space（自動更新）
- [ ] API 金鑰在 Secrets 中設定
- [ ] 應用顯示 "Running"（綠色）
- [ ] 能進入遊戲並提問

---

## 🎊 恭喜！

完成上述步驟後：

✅ 代碼在 GitHub 上  
✅ 遊戲在 Hugging Face 在線運行  
✅ 自動更新已設定  
✅ API 金鑰已安全儲存  

**你的 AI 海龜湯遊戲已準備好展示給全世界！** 🚀

---

<div align="center">

**[← 回 README](./README.md) | [詳細教學 →](./DEPLOY.md)**

有問題？ 查看 [DEPLOY.md](./DEPLOY.md) 的常見問題排解章節

</div>

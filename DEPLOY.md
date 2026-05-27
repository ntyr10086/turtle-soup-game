# 🚀 部署教學指南

> 將 AI 海龜湯遊戲部署到網路上，讓任何人都能玩！

本教學涵蓋兩個部署方案：
1. **Hugging Face Spaces**（推薦！免費且簡單）
2. **Railway**（備選方案）

---

## 方案 A：部署到 Hugging Face Spaces（推薦！⭐）

### 為什麼選擇 Hugging Face Spaces？

- ✅ **完全免費** - 無須信用卡
- ✅ **自動識別 Streamlit** - 無需額外設定
- ✅ **支援 API 呼叫** - Google Gemini API 直接可用
- ✅ **實時對話** - WebSocket 完全支援
- ✅ **自動更新** - GitHub 連接後自動部署
- ✅ **無冷啟動** - 應用始終就緒
- ⏱️ **部署時間** - 約 2-3 分鐘

### 前置準備

1. **GitHub 帳號**（免費）
2. **Hugging Face 帳號**（免費）
3. **Google Gemini API 金鑰**（免費額度充足）

---

## 🔧 詳細部署步驟

### 步驟 1️⃣：上傳到 GitHub

#### 1.1 在 GitHub 上建立新 Repository

1. 登入 GitHub（https://github.com）
2. 點選右上角 `+` → `New repository`
3. 設定：
   ```
   Repository name: turtle-soup-game
   Description: AI 海龜湯攻防戰 - Streamlit Game
   Public: ✓（勾選）
   Initialize with README: 不勾選
   ```
4. 點選 `Create repository`

#### 1.2 在本地初始化 Git

打開終端機，進入專案資料夾：

```bash
cd turtle_soup_game
git init
git add .
git commit -m "Initial commit: AI 海龜湯遊戲系統"
```

#### 1.3 連接到 GitHub

```bash
# 將下面的URL替換成你的Repository URL（複製自GitHub頁面）
git remote add origin https://github.com/你的用戶名/turtle-soup-game.git
git branch -M main
git push -u origin main
```

✅ 現在你的程式碼已經在 GitHub 上了！

---

### 步驟 2️⃣：設定 API 金鑰

在 Hugging Face Spaces 上安全地設定 API 金鑰，**不會暴露在 GitHub 上**。

#### 2.1 確保 `.env` 檔在 `.gitignore` 中

檢查 `.gitignore` 是否包含 `.env`：

```bash
cat .gitignore | grep ".env"
```

如果沒有，請手動添加到 `.gitignore`：

```
.env
.env.local
```

然後提交：

```bash
git add .gitignore
git commit -m "Update .gitignore to protect .env"
git push
```

---

### 步驟 3️⃣：建立 Hugging Face Space

#### 3.1 登入 Hugging Face

1. 前往 https://huggingface.co 並登入
2. 點選右上角頭像 → `New Space`

#### 3.2 建立 Space

設定如下：

```
Space name: turtle-soup-game
License: Apache 2.0（或你偏好的授權）
Select the Space SDK: Streamlit
Private: ✓（建議私人，因為包含 API 金鑰）
```

點選 `Create Space`

#### 3.3 連接 GitHub Repository

進入 Space 後：

1. 點選 `Files` 標籤
2. 點選 `Add files` → `Upload files` 或使用以下方法

**方法A：直接上傳檔案（簡單）**
1. 點選 `Upload files`
2. 選擇專案中的所有檔案
3. 上傳

**方法B：連接 GitHub（推薦，自動更新）**
1. 點選 Space 設定 → `Linked Repo` 標籤
2. 輸入你的 GitHub Repository URL
3. 連接成功！未來 GitHub push 會自動部署

---

### 步驟 4️⃣：設定 API 金鑰（最重要！）

#### 4.1 在 Hugging Face 中設定密鑰

1. 進入 Space 主頁
2. 點選右上角的 `Settings`（或 `Space settings`）
3. 左邊選單找 `Secrets`（或 `Environment variables`）
4. 點選 `New secret`

#### 4.2 添加 Gemini API 金鑰

填寫以下資訊：

```
Key: GEMINI_API_KEY
Value: （貼入你的 Google Gemini API 金鑰）
```

點選 `Save`

✅ API 金鑰已安全儲存！

---

### 步驟 5️⃣：修改程式碼讀取密鑰

確保你的 `app.py` 能正確讀取 Hugging Face 提供的環境變數。

檢查 `app.py` 的初始化部分（應該已經有）：

```python
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_session_state():
    """初始化 Session State"""
    if 'game' not in st.session_state:
        api_key = os.getenv('GEMINI_API_KEY')  # ← 讀取環境變數
        if not api_key:
            st.error("❌ 請先設定 GEMINI_API_KEY 環境變數！")
            st.stop()
        st.session_state.game = TurtleSoupGame(api_key)
```

如果 `app.py` 中沒有這段程式碼，請確保添加！

---

### 步驟 6️⃣：啟動 Space

完成以上步驟後：

1. Hugging Face 會自動偵測 `app.py` 中的 Streamlit 應用
2. 自動構建（Build）應該會開始
3. 等待 2-3 分鐘

#### 檢查部署狀態

1. Space 頁面會顯示 `Building`、`Running` 或 `Failed`
2. 如果是 `Running`，點選 App 連結即可使用！

---

### 步驟 7️⃣：測試遊戲

1. 進入你的 Space URL
2. 側邊欄選擇 `故事模式`
3. 選擇一個題目
4. 點選 `開始新遊戲`
5. 開始玩遊戲！

✅ 恭喜！你的遊戲已經在網上運行！

---

## 常見問題排解

### Q1: Build 失敗，顯示紅色錯誤

**解決方法：**
1. 點選 `Logs` 標籤查看錯誤訊息
2. 常見原因：
   - `requirements.txt` 中的套件版本不相容
   - Python 版本問題
   - API 金鑰未正確設定

**修復步驟：**
```bash
# 更新 requirements.txt
pip freeze > requirements.txt

# 推送到 GitHub
git add requirements.txt
git commit -m "Fix: Update dependencies"
git push
```

### Q2: 遊戲啟動後一片空白

**可能原因：**
1. API 金鑰未設定
2. API 金鑰不正確
3. Google Gemini API 配額已用完

**解決方法：**
1. 檢查 Space Settings 的 Secrets
2. 確認 GEMINI_API_KEY 已添加
3. 在 Google AI Studio 確認配額

### Q3: 提問時出現超時錯誤

**原因：** API 呼叫太慢或配額耗盡

**解決方法：**
1. 等待 30 秒後重試
2. 更換 Google 帳號的 API 金鑰
3. 檢查網路連接

### Q4: 如何更新程式碼？

**如果使用 GitHub 連接：**
- 在本地修改程式碼
- Push 到 GitHub
- Hugging Face 會自動重新部署

**如果直接上傳檔案：**
- 進入 Space
- 點選 `Files`
- 上傳新的檔案（會覆蓋舊檔案）

---

## 方案 B：部署到 Railway（備選）

如果 Hugging Face Spaces 遇到問題，可以用 Railway。

### Railway 優勢
- ✅ 支援 Python Streamlit
- ✅ 每月免費 $5 額度
- ✅ 一鍵部署
- ✅ 自動監測更新

### 部署步驟

1. **註冊 Railway**：https://railway.app
2. **連接 GitHub**：授權 Railway 訪問
3. **建立 Project**：
   - 點選 `New Project`
   - 選 `Deploy from GitHub repo`
   - 選擇 `turtle-soup-game`
4. **設定環境變數**：
   - 進入 Project Settings
   - 找 `Variables`
   - 添加 `GEMINI_API_KEY`
5. **自動部署**：Railway 會自動構建並部署

### Railway 的部署 URL

部署完成後，Railway 會生成一個 URL，例如：
```
https://turtle-soup-game-production.up.railway.app
```

---

## 常用指令參考

```bash
# 初始化 Git
git init
git add .
git commit -m "Initial commit"

# 添加 remote
git remote add origin <repository-url>

# 推送到 GitHub
git push -u origin main

# 查看 Git 狀態
git status

# 更新代碼後推送
git add .
git commit -m "Update: description"
git push
```

---

## 🎯 完整檢查清單

部署前，確認以下項目：

- [ ] `.gitignore` 包含 `.env`
- [ ] GitHub Repository 已建立並推送
- [ ] Hugging Face 帳號已建立
- [ ] Google Gemini API 金鑰已取得
- [ ] Hugging Face Space 已建立
- [ ] GEMINI_API_KEY 已在 Secrets 中設定
- [ ] 所有檔案（app.py, defense.py, game_logic.py 等）已上傳
- [ ] Space Build 顯示 Running（綠色）
- [ ] 能夠進入應用並開始遊戲

---

## 📊 部署對比

| 功能 | Hugging Face | Railway | Vercel* |
|------|-------------|---------|---------|
| 免費 | ✅ | ✅ ($5/月) | ✅ |
| Streamlit 支援 | ✅ | ✅ | ❌ |
| API 呼叫 | ✅ | ✅ | ❌ |
| 實時對話 | ✅ | ✅ | ❌ |
| 設定難度 | 最簡單 | 簡單 | 很難 |
| 部署速度 | 快 | 快 | 不適用 |

*Vercel 需要改寫為 Flask/Next.js，不推薦

---

## 🎊 恭喜！

完成上述步驟後，你的 AI 海龜湯遊戲就可以在網上公開運行了！

### 分享你的遊戲

1. 複製 Space URL
2. 分享給朋友
3. 分享給老師看課堂成果
4. 用於期末報告展示

### 後續更新

只要你的代碼更新了 GitHub，Hugging Face 會自動重新部署。非常方便！

---

**祝部署順利！如有問題，隨時查看本檔案的常見問題排解章節！🚀**

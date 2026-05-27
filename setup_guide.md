# 🚀 超詳細安裝指引（新手專用）

## 📌 前置準備檢查清單

在開始之前，請確認你的電腦已經安裝：
- [ ] Python（3.8版本或以上）
- [ ] 穩定的網路連線
- [ ] Google帳號（用於申請API金鑰）

---

## 第一步：檢查Python是否已安裝

### Windows系統：
1. 按 `Win + R` 鍵
2. 輸入 `cmd` 然後按Enter
3. 在黑色視窗中輸入：
```bash
python --version
```

### Mac系統：
1. 按 `Command + 空白鍵` 搜尋 "Terminal"
2. 打開Terminal後輸入：
```bash
python3 --version
```

### 如果顯示版本號（例如：Python 3.9.7）
✅ 太好了！你已經有Python了，可以跳到第二步

### 如果顯示找不到指令或錯誤
❌ 你需要先安裝Python：
- 前往 [Python官網](https://www.python.org/downloads/) 下載安裝
- Windows請勾選 "Add Python to PATH"
- 安裝完成後重新開機，再次確認

---

## 第二步：下載專題檔案

### 方法一：直接下載
1. 確認你已經有以下所有檔案在同一個資料夾中：
   - `app.py`
   - `defense.py`
   - `game_logic.py`
   - `requirements.txt`
   - `.env.example`
   - `README.md`

### 方法二：從USB或雲端取得
1. 將老師/組員給你的檔案複製到電腦
2. 建議放在容易找到的地方，例如：`C:\Users\你的名字\Documents\turtle_soup_game`

---

## 第三步：打開終端機並進入專題資料夾

### Windows：
1. 打開檔案總管，進入你放檔案的資料夾
2. 在資料夾視窗上方的路徑列點一下
3. 輸入 `cmd` 然後按Enter
4. 應該會開啟一個黑色視窗，顯示你目前在專題資料夾中

### Mac：
1. 打開Finder，進入你放檔案的資料夾
2. 右鍵點選資料夾，選擇「服務」→「新增位於檔案夾位置的終端機視窗」

### 確認你在正確的資料夾：
輸入這個指令來確認：
```bash
dir         # Windows用這個
ls          # Mac用這個
```

你應該能看到 `app.py`、`defense.py` 等檔案名稱

---

## 第四步：安裝Python套件

在終端機中輸入以下指令（一次一行）：

### Windows：
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Mac：
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 如果出現權限錯誤
Windows請在指令前加 `python -m`：
```bash
python -m pip install -r requirements.txt
```

Mac請在指令前加 `sudo`：
```bash
sudo python3 -m pip install -r requirements.txt
```
（會要求輸入你的電腦密碼，輸入時不會顯示任何字，這是正常的）

### 安裝成功的樣子
你會看到一堆文字跑過，最後顯示：
```
Successfully installed streamlit-1.31.0 google-generativeai-0.3.2 python-dotenv-1.0.0
```

---

## 第五步：取得Google Gemini API金鑰

### 5.1 前往Google AI Studio
1. 打開瀏覽器
2. 前往：https://aistudio.google.com/app/apikey
3. 使用你的Google帳號登入

### 5.2 創建API金鑰
1. 點選「Create API Key」或「取得API金鑰」
2. 選擇一個專案（如果沒有就新建一個）
3. 複製顯示的金鑰（一長串英文和數字）

⚠️ **重要**：這個金鑰就像你的密碼，不要分享給任何人！

### 5.3 儲存API金鑰

#### 方法一：使用記事本（Windows）
1. 在專題資料夾中找到 `.env.example` 檔案
2. 右鍵點選 → 開啟檔案 → 選擇「記事本」
3. 把 `your_api_key_here` 替換成你剛複製的API金鑰
4. 點選「檔案」→「另存新檔」
5. **重要**：檔案名稱改成 `.env`（沒有example）
6. 存檔類型選擇「所有檔案」
7. 儲存

#### 方法二：使用文字編輯（Mac）
1. 在專題資料夾中找到 `.env.example` 檔案
2. 右鍵點選 → 使用「文字編輯」開啟
3. 把 `your_api_key_here` 替換成你剛複製的API金鑰
4. 點選「檔案」→「儲存為」
5. 檔案名稱改成 `.env`（沒有example）
6. 取消勾選「如果沒有提供副檔名，使用".txt"」
7. 儲存

### 完成後應該看起來像這樣：
```
GEMINI_API_KEY=AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 第六步：啟動遊戲！

### 在終端機中輸入：

#### Windows：
```bash
streamlit run app.py
```

#### Mac：
```bash
streamlit run app.py
```

### 成功啟動的樣子
你會看到：
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

### 瀏覽器會自動開啟
- 如果沒有自動開啟，請手動打開瀏覽器
- 輸入網址：`http://localhost:8501`

---

## 🎉 恭喜！你已經成功安裝了！

現在你應該能看到遊戲畫面了。

### 開始遊戲：
1. 點選左側欄的「開始新遊戲」按鈕
2. 開始提問！

---

## ❌ 常見問題排解

### Q1: 找不到 `streamlit` 指令
**解決方法**：
```bash
# Windows
python -m streamlit run app.py

# Mac
python3 -m streamlit run app.py
```

### Q2: 顯示 "GEMINI_API_KEY not found"
**原因**：沒有正確設定 `.env` 檔案

**解決方法**：
1. 確認 `.env` 檔案在專題資料夾中（不是 `.env.example`）
2. 確認檔案內容格式正確
3. 確認API金鑰是有效的

### Q3: 顯示 "Quota Exceeded" 或 "429 Error"
**原因**：API免費額度用完了

**解決方法**：
1. 換一個新的Google帳號
2. 重新申請API金鑰
3. 更新 `.env` 檔案中的金鑰

### Q4: 瀏覽器顯示 "This site can't be reached"
**原因**：Streamlit還沒完全啟動

**解決方法**：
1. 等待30秒再重新整理
2. 確認終端機中沒有顯示錯誤訊息
3. 確認Port 8501沒有被其他程式佔用

### Q5: 終端機顯示一堆紅色錯誤
**可能原因**：
- Python版本太舊
- 套件安裝不完整
- 檔案路徑有中文或特殊字元

**解決方法**：
```bash
# 重新安裝所有套件
pip uninstall -y streamlit google-generativeai python-dotenv
pip install -r requirements.txt
```

---

## 📞 還是不行？試試這些

### 完全重新安裝
```bash
# 1. 移除舊版本
pip uninstall -y streamlit google-generativeai python-dotenv

# 2. 清除快取
pip cache purge

# 3. 重新安裝
pip install -r requirements.txt
```

### 檢查Python路徑
```bash
# Windows
where python

# Mac
which python3
```

### 確認所有檔案都在
```bash
# Windows
dir

# Mac
ls -la
```
應該看到：app.py, defense.py, game_logic.py, .env

---

## ✅ 最後檢查清單

安裝完成後，請確認：
- [ ] Python已安裝且版本正確
- [ ] 所有檔案都在同一個資料夾
- [ ] requirements.txt中的套件都已安裝
- [ ] .env檔案存在且包含有效的API金鑰
- [ ] `streamlit run app.py` 可以成功執行
- [ ] 瀏覽器能開啟遊戲介面
- [ ] 點選「開始新遊戲」能正常運作
- [ ] 可以正常提問並得到回應

---

## 🎓 給老師/助教的測試指令

如果你是老師或助教想快速檢查學生是否正確安裝，可以請學生執行：

```bash
python -c "import streamlit; import google.generativeai; import dotenv; print('✅ 所有套件已正確安裝')"
```

如果顯示 `✅ 所有套件已正確安裝`，表示安裝成功。

---

**祝你順利完成專題！有任何問題歡迎詢問組員或老師 🎉**

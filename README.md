# 🎨 MoodColor
![MoodColor Cover](./Picture/Cover.png)
🎨 MoodColor is an AI-powered mood tracking tool that transforms your daily experiences—whether in text or photos—into a color that represents your current emotional state. Whether you're capturing joy, peace, or subtle melancholy, the system analyzes your input and assigns a HEX color code to visually express how you feel.

Users can maintain a daily mood journal through a calendar-like dashboard, upload content, and reflect on their emotional journey. The platform not only creates mood-based icons and themed pages but also supports collaboration—allowing friends or teams to co-create and share their emotional color stories.

This project aims to bring emotional awareness and a touch of healing by helping users visualize their feelings in color. Ideal for personal reflection, mood tracking, or simply expressing your day through design.

Built with modern technologies and supports extensibility via AI, containerized infrastructure, and modular event-driven architecture.

## Backend

這是專案的後端服務，使用 FastAPI 框架構建，並結合 Supabase 作為資料庫。以下是如何設定和啟動後端服務的步驟。

## 1. 設定 .env 檔案

在專案根目錄下，建立一個名為 `.env` 的檔案。此檔案將儲存你的 API 金鑰及其他機密設定。

### 範例 `.env` 內容：
```env
SUPABASE_URL=<你的_supabase_url>
SUPABASE_KEY=<你的_supabase_key>
SUPABASE_KEY_AUTH=<你的_SUPABASE_KEY_AUTH>
GOOGLE_API_KEY=<你的_GOOGLE_API_KEY>
```

##2. 安裝所需的 Python 套件
確保你已經安裝了 Python 和 pip，然後安裝專案所需的 Python 套件。使用以下指令安裝：
```
pip install -r requirements.txt
```

##3. 啟動後端服務
安裝完套件後，使用 uvicorn 啟動 FastAPI 服務：
```
uvicorn main:app --reload
```
此指令將啟動後端服務並在本地伺服器上監聽變更。你可以透過瀏覽器或 Postman 等工具，訪問以下端點：
```
http://127.0.0.1:8000/docs
```
會顯示自動生成的 API 文件（Swagger UI）。

##4. 結束
若要停止伺服器，請在終端機中按 
```
CTRL+C
```

感謝使用本專案，若有任何問題，請隨時提出 Issue 或聯絡我們。

### 說明：
- `.env` 檔案用來儲存環境變數，這對於將敏感資料如 API 金鑰儲存在版本控制外非常重要。
- `requirements.txt` 應包含所有安裝的 Python 套件，通常可以使用 `pip freeze > requirements.txt` 來生成。
- `uvicorn main:app --reload` 是啟動 FastAPI 應用程式的指令，`--reload` 參數會讓開發過程中修改程式碼時自動重新加載伺服器。

你可以根據需要進行修改，這樣的結構使得其他開發者能夠快速理解如何設置和啟動專案。




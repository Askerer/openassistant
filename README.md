# OpenAI Assistant 客戶端

這是一個Python程序，用於與您在OpenAI上建立的Assistant進行交互。

## 功能特點

- 🤖 與OpenAI Assistant進行對話
- 📋 查看Assistant詳細信息
- 📜 查看對話歷史
- 🔍 列出所有可用的Assistants
- 💬 交互式命令行界面

## 安裝步驟

### 1. 克隆或下載項目

```bash
git clone <repository-url>
cd openaiAssistant
```

### 2. 安裝依賴包

```bash
pip install -r requirements.txt
```

### 3. 設置環境變數

創建一個 `.env` 文件（或直接在系統環境變數中設置）：

```env
# OpenAI API 配置
OPENAI_API_KEY=your_openai_api_key_here
ASSISTANT_ID=your_assistant_id_here
```

#### 如何獲取API密鑰：

1. 訪問 [OpenAI Platform](https://platform.openai.com/)
2. 登入您的帳戶
3. 點擊右上角的個人資料圖標
4. 選擇 "View API keys"
5. 創建新的API密鑰

#### 如何獲取Assistant ID：

1. 訪問 [OpenAI Platform](https://platform.openai.com/)
2. 進入 "Assistants" 頁面
3. 選擇您要使用的Assistant
4. 複製Assistant ID（格式類似：`asst_xxxxxxxxxxxxxxxxxxxxxxxx`）

## 使用方法

### 運行程序

```bash
python main.py
```

### 程序選單

程序啟動後會顯示以下選單：

```
請選擇操作:
1. 開始新對話
2. 查看Assistant信息
3. 列出所有Assistants
4. 查看對話歷史
5. 退出程序
```

### 對話模式

選擇選項1進入對話模式：

- 輸入您的問題或消息
- Assistant會處理並回應
- 輸入 `quit`、`exit` 或 `退出` 退出對話
- 輸入 `history` 查看當前對話歷史

## 文件結構

```
openaiAssistant/
├── main.py              # 主程序文件
├── assistant_client.py  # Assistant客戶端類
├── config.py           # 配置文件
├── requirements.txt    # 依賴包列表
└── README.md          # 說明文件
```

## 主要類和方法

### AssistantClient 類

- `create_thread()`: 創建新的對話線程
- `send_message(message)`: 發送消息到Assistant
- `get_conversation_history()`: 獲取對話歷史
- `list_assistants()`: 列出所有Assistants
- `get_assistant_info()`: 獲取Assistant詳細信息

## 錯誤處理

程序包含完整的錯誤處理機制：

- API連接錯誤
- 無效的Assistant ID
- 網絡連接問題
- 用戶輸入驗證

## 注意事項

1. **API費用**: 使用OpenAI API會產生費用，請注意您的使用量
2. **API限制**: 請遵守OpenAI的API使用限制和速率限制
3. **安全性**: 請妥善保管您的API密鑰，不要將其提交到版本控制系統
4. **網絡**: 確保您的網絡連接穩定

## 故障排除

### 常見問題

1. **"請在環境變數中設置 OPENAI_API_KEY"**
   - 確保已正確設置API密鑰
   - 檢查 `.env` 文件格式是否正確

2. **"請在環境變數中設置 ASSISTANT_ID"**
   - 確保已正確設置Assistant ID
   - 檢查Assistant ID格式是否正確

3. **"初始化失敗"**
   - 檢查網絡連接
   - 確認API密鑰有效
   - 確認Assistant ID存在

4. **"Assistant 處理失敗"**
   - 檢查Assistant是否正常工作
   - 確認Assistant有足夠的權限
   - 檢查API配額是否充足

## 進階用法

### 自定義配置

您可以修改 `config.py` 文件來自定義配置：

```python
# 自定義超時設置
TIMEOUT = 30.0

# 自定義重試次數
MAX_RETRIES = 3
```

### 擴展功能

您可以擴展 `AssistantClient` 類來添加更多功能：

- 文件上傳和下載
- 工具調用處理
- 批量消息處理
- 自定義響應格式

## 貢獻

歡迎提交問題報告和功能請求！

## 授權

本項目使用 MIT 授權。 
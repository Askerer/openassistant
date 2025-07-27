import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# OpenAI API 配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# 檢查必要的配置
if not OPENAI_API_KEY:
    raise ValueError("請在環境變數中設置 OPENAI_API_KEY")

if not ASSISTANT_ID:
    raise ValueError("請在環境變數中設置 ASSISTANT_ID") 
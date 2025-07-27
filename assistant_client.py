import time
import json
from typing import Optional, List, Dict, Any
from openai import OpenAI
from config import OPENAI_API_KEY, ASSISTANT_ID


class AssistantClient:
    """OpenAI Assistant API 客戶端"""
    
    def __init__(self):
        """初始化客戶端"""
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.assistant_id = ASSISTANT_ID
        self.thread_id = None
        
    def create_thread(self) -> str:
        """創建新的對話線程"""
        thread = self.client.beta.threads.create()
        self.thread_id = thread.id
        print(f"創建新的對話線程: {self.thread_id}")
        return self.thread_id
    
    def send_message(self, message: str, thread_id: Optional[str] = None) -> str:
        """發送消息到Assistant"""
        if thread_id:
            self.thread_id = thread_id
        elif not self.thread_id:
            self.create_thread()
            
        # 添加消息到線程
        message_obj = self.client.beta.threads.messages.create(
            thread_id=self.thread_id,
            role="user",
            content=message
        )
        print(f"已發送消息: {message}")
        
        # 運行Assistant
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=self.assistant_id
        )
        
        print(f"Assistant 開始處理... (Run ID: {run.id})")
        
        # 等待處理完成
        return self._wait_for_completion(run.id)
    
    def _wait_for_completion(self, run_id: str) -> str:
        """等待Assistant處理完成"""
        while True:
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id,
                run_id=run_id
            )
            
            if run.status == "completed":
                print("Assistant 處理完成!")
                return self._get_latest_response()
            elif run.status == "failed":
                raise Exception(f"Assistant 處理失敗: {run.last_error}")
            elif run.status == "requires_action":
                print("Assistant 需要執行工具...")
                # 這裡可以處理工具調用，但為了簡化，我們跳過
                pass
            
            print(f"處理中... 狀態: {run.status}")
            time.sleep(1)
    
    def _get_latest_response(self) -> str:
        """獲取最新的Assistant回應"""
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread_id
        )
        
        # 獲取最新的Assistant消息
        for message in messages.data:
            if message.role == "assistant":
                content = message.content[0]
                if hasattr(content, 'text'):
                    return content.text.value
                else:
                    return str(content)
        
        return "沒有收到回應"
    
    def get_conversation_history(self, thread_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """獲取對話歷史"""
        if thread_id:
            self.thread_id = thread_id
        elif not self.thread_id:
            return []
            
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread_id
        )
        
        history = []
        for message in messages.data:
            content = message.content[0]
            if hasattr(content, 'text'):
                text_content = content.text.value
            else:
                text_content = str(content)
                
            history.append({
                "role": message.role,
                "content": text_content,
                "created_at": message.created_at
            })
        
        return history
    
    def list_assistants(self) -> List[Dict[str, Any]]:
        """列出所有可用的Assistants"""
        assistants = self.client.beta.assistants.list()
        return [
            {
                "id": assistant.id,
                "name": assistant.name,
                "description": assistant.description,
                "model": assistant.model,
                "instructions": assistant.instructions
            }
            for assistant in assistants.data
        ]
    
    def get_assistant_info(self, assistant_id: Optional[str] = None) -> Dict[str, Any]:
        """獲取Assistant的詳細信息"""
        if not assistant_id:
            assistant_id = self.assistant_id
            
        assistant = self.client.beta.assistants.retrieve(assistant_id)
        return {
            "id": assistant.id,
            "name": assistant.name,
            "description": assistant.description,
            "model": assistant.model,
            "instructions": assistant.instructions,
            "tools": [tool.type for tool in assistant.tools] if assistant.tools else []
        } 
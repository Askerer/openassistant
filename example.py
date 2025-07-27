#!/usr/bin/env python3
"""
OpenAI Assistant 使用示例
這個文件展示了如何使用 AssistantClient 類進行基本的操作
"""

from assistant_client import AssistantClient


def simple_chat_example():
    """簡單對話示例"""
    print("=== 簡單對話示例 ===")
    
    # 初始化客戶端
    client = AssistantClient()
    
    # 發送一條消息
    message = "你好！請介紹一下你自己。"
    print(f"發送消息: {message}")
    
    response = client.send_message(message)
    print(f"Assistant回應: {response}")


def conversation_example():
    """多輪對話示例"""
    print("\n=== 多輪對話示例 ===")
    
    # 初始化客戶端
    client = AssistantClient()
    
    # 創建對話線程
    thread_id = client.create_thread()
    
    # 多輪對話
    messages = [
        "你好！",
        "你能幫我做什麼？",
        "請給我一個Python的Hello World示例"
    ]
    
    for message in messages:
        print(f"\n用戶: {message}")
        response = client.send_message(message, thread_id)
        print(f"Assistant: {response}")
    
    # 查看對話歷史
    print("\n=== 對話歷史 ===")
    history = client.get_conversation_history(thread_id)
    for msg in history:
        print(f"{msg['role']}: {msg['content']}")


def assistant_info_example():
    """查看Assistant信息示例"""
    print("\n=== Assistant信息示例 ===")
    
    # 初始化客戶端
    client = AssistantClient()
    
    # 獲取Assistant信息
    info = client.get_assistant_info()
    print(f"Assistant名稱: {info['name']}")
    print(f"Assistant描述: {info['description']}")
    print(f"使用模型: {info['model']}")
    print(f"可用工具: {info['tools']}")


def list_assistants_example():
    """列出所有Assistants示例"""
    print("\n=== 列出所有Assistants示例 ===")
    
    # 初始化客戶端
    client = AssistantClient()
    
    # 列出所有Assistants
    assistants = client.list_assistants()
    
    if assistants:
        print(f"找到 {len(assistants)} 個Assistants:")
        for i, assistant in enumerate(assistants, 1):
            print(f"{i}. {assistant['name']} (ID: {assistant['id']})")
    else:
        print("沒有找到任何Assistants")


def main():
    """主函數 - 運行所有示例"""
    print("OpenAI Assistant 使用示例")
    print("=" * 50)
    
    try:
        # 運行各種示例
        simple_chat_example()
        conversation_example()
        assistant_info_example()
        list_assistants_example()
        
        print("\n✅ 所有示例運行完成！")
        
    except Exception as e:
        print(f"❌ 運行示例時發生錯誤: {e}")
        print("請確保已正確設置API密鑰和Assistant ID")


if __name__ == "__main__":
    main() 
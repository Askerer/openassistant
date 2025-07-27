#!/usr/bin/env python3
"""
OpenAI Assistant 客戶端主程序
使用此程序與您在OpenAI上建立的Assistant進行對話
"""

import sys
import json
from assistant_client import AssistantClient


def print_banner():
    """顯示程序橫幅"""
    print("=" * 60)
    print("🤖 OpenAI Assistant 客戶端")
    print("=" * 60)
    print()


def print_menu():
    """顯示主選單"""
    print("\n請選擇操作:")
    print("1. 開始新對話")
    print("2. 查看Assistant信息")
    print("3. 列出所有Assistants")
    print("4. 查看對話歷史")
    print("5. 退出程序")
    print("-" * 40)


def chat_mode(client: AssistantClient):
    """對話模式"""
    print("\n💬 進入對話模式")
    print("輸入 'quit' 或 'exit' 退出對話")
    print("輸入 'history' 查看當前對話歷史")
    print("-" * 40)
    
    # 創建新線程
    thread_id = client.create_thread()
    
    while True:
        try:
            # 獲取用戶輸入
            user_input = input("\n👤 您: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("👋 再見!")
                break
            elif user_input.lower() == 'history':
                show_conversation_history(client)
                continue
            elif not user_input:
                print("❌ 請輸入有效的消息")
                continue
            
            # 發送消息到Assistant
            print("\n🤖 Assistant 正在思考...")
            response = client.send_message(user_input, thread_id)
            
            print(f"\n🤖 Assistant: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 對話已中斷，再見!")
            break
        except Exception as e:
            print(f"\n❌ 錯誤: {e}")
            print("請重試或輸入 'quit' 退出")


def show_assistant_info(client: AssistantClient):
    """顯示Assistant信息"""
    print("\n📋 Assistant 信息:")
    print("-" * 40)
    
    try:
        info = client.get_assistant_info()
        print(f"ID: {info['id']}")
        print(f"名稱: {info['name']}")
        print(f"描述: {info['description']}")
        print(f"模型: {info['model']}")
        print(f"工具: {', '.join(info['tools']) if info['tools'] else '無'}")
        print(f"指令: {info['instructions'][:100]}{'...' if len(info['instructions']) > 100 else ''}")
        
    except Exception as e:
        print(f"❌ 獲取Assistant信息失敗: {e}")


def list_assistants(client: AssistantClient):
    """列出所有Assistants"""
    print("\n📋 所有可用的Assistants:")
    print("-" * 40)
    
    try:
        assistants = client.list_assistants()
        
        if not assistants:
            print("❌ 沒有找到任何Assistants")
            return
        
        for i, assistant in enumerate(assistants, 1):
            print(f"\n{i}. {assistant['name']}")
            print(f"   ID: {assistant['id']}")
            print(f"   描述: {assistant['description']}")
            print(f"   模型: {assistant['model']}")
            
    except Exception as e:
        print(f"❌ 獲取Assistants列表失敗: {e}")


def show_conversation_history(client: AssistantClient):
    """顯示對話歷史"""
    print("\n📜 對話歷史:")
    print("-" * 40)
    
    try:
        history = client.get_conversation_history()
        
        if not history:
            print("❌ 沒有對話歷史")
            return
        
        for message in reversed(history):  # 最新的消息在前
            role_emoji = "👤" if message['role'] == 'user' else "🤖"
            print(f"\n{role_emoji} {message['role'].title()}:")
            print(f"   {message['content']}")
            print(f"   時間: {message['created_at']}")
            
    except Exception as e:
        print(f"❌ 獲取對話歷史失敗: {e}")


def main():
    """主函數"""
    print_banner()
    
    try:
        # 初始化客戶端
        client = AssistantClient()
        print("✅ 成功連接到OpenAI API")
        
    except Exception as e:
        print(f"❌ 初始化失敗: {e}")
        print("\n請確保:")
        print("1. 已安裝必要的依賴包: pip install -r requirements.txt")
        print("2. 已設置正確的API密鑰和Assistant ID")
        print("3. 網絡連接正常")
        sys.exit(1)
    
    # 主循環
    while True:
        try:
            print_menu()
            choice = input("請輸入選項 (1-5): ").strip()
            
            if choice == '1':
                chat_mode(client)
            elif choice == '2':
                show_assistant_info(client)
            elif choice == '3':
                list_assistants(client)
            elif choice == '4':
                show_conversation_history(client)
            elif choice == '5':
                print("👋 再見!")
                break
            else:
                print("❌ 無效的選項，請重新選擇")
                
        except KeyboardInterrupt:
            print("\n\n👋 程序已中斷，再見!")
            break
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")


if __name__ == "__main__":
    main() 
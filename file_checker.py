import os
import json
from pathlib import Path


def check_json_pdf_consistency(folder_path):
    """
    檢查資料夾中的JSON檔案與PDF檔案數量是否相符，以及檔名是否一致
    
    Args:
        folder_path (str): 要檢查的資料夾路徑
        
    Returns:
        dict: 包含檢查結果的字典
    """
    try:
        # 確保路徑存在
        if not os.path.exists(folder_path):
            return {
                "success": False,
                "error": f"資料夾路徑不存在: {folder_path}"
            }
        
        # 獲取所有JSON和PDF檔案
        json_files = []
        pdf_files = []
        
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                if file.lower().endswith('.json'):
                    json_files.append(file)
                elif file.lower().endswith('.pdf'):
                    pdf_files.append(file)
        
        # 檢查數量是否相符
        json_count = len(json_files)
        pdf_count = len(pdf_files)
        count_match = json_count == pdf_count
        
        # 檢查檔名是否一致（不包含副檔名）
        matching_files = []
        mismatched_files = []
        
        json_names = {os.path.splitext(f)[0] for f in json_files}
        pdf_names = {os.path.splitext(f)[0] for f in pdf_files}
        
        # 找到匹配的檔名
        matching_names = json_names.intersection(pdf_names)
        
        # 找到不匹配的檔名
        json_only = json_names - pdf_names
        pdf_only = pdf_names - json_names
        
        # 整理結果
        for name in matching_names:
            matching_files.append({
                "json_file": f"{name}.json",
                "pdf_file": f"{name}.pdf"
            })
        
        for name in json_only:
            mismatched_files.append({
                "type": "json_only",
                "file": f"{name}.json"
            })
            
        for name in pdf_only:
            mismatched_files.append({
                "type": "pdf_only", 
                "file": f"{name}.pdf"
            })
        
        # 返回檢查結果
        result = {
            "success": True,
            "folder_path": folder_path,
            "counts": {
                "json_files": json_count,
                "pdf_files": pdf_count,
                "count_match": count_match
            },
            "matching_files": matching_files,
            "mismatched_files": mismatched_files,
            "summary": {
                "total_matching_pairs": len(matching_files),
                "total_mismatched_files": len(mismatched_files),
                "all_files_match": len(mismatched_files) == 0 and count_match
            }
        }
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "error": f"檢查過程中發生錯誤: {str(e)}"
        }


def print_check_result(result):
    """
    格式化輸出檢查結果
    
    Args:
        result (dict): check_json_pdf_consistency函數的返回結果
    """
    if not result["success"]:
        print(f"❌ 錯誤: {result['error']}")
        return
    
    print(f"📁 檢查資料夾: {result['folder_path']}")
    print(f"📊 檔案統計:")
    print(f"   JSON檔案數量: {result['counts']['json_files']}")
    print(f"   PDF檔案數量: {result['counts']['pdf_files']}")
    print(f"   數量相符: {'✅' if result['counts']['count_match'] else '❌'}")
    print()
    
    print(f"📋 匹配的檔案對:")
    if result['matching_files']:
        for pair in result['matching_files']:
            print(f"   ✅ {pair['json_file']} ↔ {pair['pdf_file']}")
    else:
        print("   (無匹配的檔案對)")
    print()
    
    print(f"⚠️  不匹配的檔案:")
    if result['mismatched_files']:
        for file_info in result['mismatched_files']:
            if file_info['type'] == 'json_only':
                print(f"   📄 僅有JSON: {file_info['file']}")
            else:
                print(f"   📄 僅有PDF: {file_info['file']}")
    else:
        print("   (無不匹配的檔案)")
    print()
    
    summary = result['summary']
    print(f"📈 總結:")
    print(f"   匹配的檔案對: {summary['total_matching_pairs']}")
    print(f"   不匹配的檔案: {summary['total_mismatched_files']}")
    print(f"   完全匹配: {'✅' if summary['all_files_match'] else '❌'}")


# 使用範例
if __name__ == "__main__":
    # 測試用的資料夾路徑，請根據實際情況修改
    test_folder = "./test_files"
    
    print("🔍 開始檢查JSON和PDF檔案一致性...")
    print("=" * 50)
    
    result = check_json_pdf_consistency(test_folder)
    print_check_result(result) 
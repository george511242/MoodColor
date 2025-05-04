from supabase_client import supabase
from datetime import date

def get_yesterday_mood_color(yesterday_date: date, user_id: int):
    print(f"Getting mood for: {yesterday_date}", user_id)
    
    # 查詢 DIARY_ENTRY 表格，並找出昨天的顏色和 user_id
    response = supabase.table("DIARY_ENTRY")\
        .select("hex_color_code", "user_id")\
        .eq("entry_date", yesterday_date)\
        .eq("user_id", user_id)\
        .limit(1).execute()  # 使用 limit(1) 確保最多只返回 1 行
    
    # 檢查是否有錯誤，並處理錯誤情況
    if not response.data:  # 如果返回的數據為空或無結果，返回預設顏色
        return {"hex": "#FFFFFF", "owner_name": None}

    # 獲取 user_id 從 DIARY_ENTRY 中查詢的結果
    user_id = response.data[0]["user_id"]  # 使用 [0] 訪問返回的唯一一行

    # 查詢 USER 表格，根據 user_id 查找用戶名稱
    user_response = supabase.table("USER")\
        .select("username")\
        .eq("id", user_id)\
        .limit(1).execute()  # 使用 limit(1) 確保最多只返回 1 行

    # 檢查 user_response 是否有結果
    if not user_response.data:  # 如果沒有查詢到用戶名稱
        return {"hex": "#FFFFFF", "owner_name": None}

    # 返回顏色和用戶名稱
    return {
        "hex": response.data[0]["hex_color_code"],  # 正確訪問 response.data[0]
        "owner_name": user_response.data[0]["username"]  # 正確訪問 user_response.data[0]
    }

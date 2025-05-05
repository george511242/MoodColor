from supabase_client import supabase
from datetime import datetime
from fastapi import HTTPException

def share_with_friend(userid: int, anotheruserid: int, diary_id: int):
    # 日誌紀錄，顯示正在進行的操作
    print(f"Attempting to share: userid={userid}, anotheruserid={anotheruserid}, diary_id={diary_id}")
    
    # 檢查 DIARY_ENTRY 中是否存在該 diary_id
    diary_entry_exists = supabase.table("DIARY_ENTRY")\
        .select("id")\
        .eq("id", diary_id)\
        .execute()

    print(f"DIARY_ENTRY exists check response: {diary_entry_exists}")
    
    if not diary_entry_exists.data:  # 如果不存在該 diary_id
        return {"status": "error", "message": f"Diary entry with ID {diary_id} does not exist."}
    
    # 檢查是否已經有這組 userid, anotheruserid, diary_id
    existing_share = supabase.table("SHARED_DASHBOARD")\
        .select("owner_user_id,shared_with_user_id,diary_entry_id")\
        .eq("owner_user_id", userid)\
        .eq("shared_with_user_id", anotheruserid)\
        .eq("diary_entry_id", diary_id)\
        .execute()

    print(f"Existing share check response: {existing_share}")

    if existing_share.data:  # 如果這組資料已經存在
        return {"status": "error", "message": "This sharing record already exists."}
    
    # 取得當前時間，並將 datetime 轉換為字串
    share_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 使用 ISO 格式的字符串表示
    print(f"Share time: {share_time}")
    
    # 插入資料到 'SHARED_DASHBOARD' 表格
    response = supabase.table("SHARED_DASHBOARD").insert({
        "owner_user_id": userid,
        "shared_with_user_id": anotheruserid,
        "diary_entry_id": diary_id,
        "share_time": share_time,
        "request_state": False
    }).execute()

    # 日誌紀錄回應
    print(f"Insert response: {response}")

    # 檢查插入資料是否成功
    if not response.data:
        print(f"Error occurred while inserting: {response.error}")  # 記錄錯誤
        return {"status": "error", "message": "插入分享記錄失敗。"}
    
    return {"status": "success"}

def accept_invite(userid: int, anotheruserid: int, diary_id: int):
    # 查詢是否存在該分享記錄
    existing_record = supabase.table("SHARED_DASHBOARD")\
        .select("*")\
        .eq("owner_user_id", userid)\
        .eq("shared_with_user_id", anotheruserid)\
        .eq("diary_entry_id", diary_id)\
        .limit(1)\
        .execute()  # 查詢限制為1條資料
    
    # 如果找不到對應的分享記錄，返回 404 錯誤
    if not existing_record.data:
        raise HTTPException(status_code=404, detail="Share record not found.")
    
    # 如果找到多條資料（理論上應該只有1條），返回錯誤
    if len(existing_record.data) > 1:
        raise HTTPException(status_code=400, detail="Multiple share records found, which is unexpected.")
    
    # 更新 request_state 為 True
    response = supabase.table("SHARED_DASHBOARD")\
        .update({"request_state": True})\
        .eq("owner_user_id", userid)\
        .eq("shared_with_user_id", anotheruserid)\
        .eq("diary_entry_id", diary_id)\
        .execute()

    # 如果更新失敗，返回 500 錯誤
    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to update share record.")

    return {"status": "success"}
from supabase_client import supabase
from datetime import date

def delete_journal_by_date(journal_date: date):
    # 執行刪除操作
    response = supabase.table("DIARY_ENTRY").delete().eq("entry_date", journal_date).execute()

    # 檢查是否有資料被刪除
    if not response.data or len(response.data) == 0:
        return {
            "status": "error",
            "message": f"刪除失敗或找不到符合 {journal_date} 的日記資料。"
        }

    # 成功
    return {
        "status": "success",
        "entry_date": journal_date
    }


from supabase_client import supabase
from datetime import datetime
from typing import Dict, Any

def add_diary_entry(entry_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Add a new diary entry to the database.
    
    Args:
        entry_data (Dict[str, Any]): Dictionary containing diary entry data
        
    Returns:
        Dict[str, Any]: The created diary entry with additional fields
    """
    try:
        # Convert date to string format
        if "entry_date" in entry_data:
            entry_data["entry_date"] = entry_data["entry_date"].isoformat()
            
        # Add created_time to the entry data
        entry_data["created_at"] = datetime.now().isoformat()
        
        # Insert the entry into the database
        result = supabase.table("DIARY_ENTRY").insert(entry_data).execute()
        
        if not result.data:
            # Check if there's an error in the result
            if hasattr(result, 'error') and result.error:
                raise Exception(f"Database error: {result.error}")
            else:
                raise Exception("Failed to create diary entry: No data returned and no error message")
            
        return result.data[0]
    except Exception as e:
        # Print the full error for debugging
        print(f"Full error details: {str(e)}")
        print(f"Entry data that caused the error: {entry_data}")
        raise Exception(f"Error creating diary entry: {str(e)}") 
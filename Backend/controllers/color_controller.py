import google.generativeai as genai
from fastapi import HTTPException
import logging
import os
from dotenv import load_dotenv

# 設置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # 輸出到終端機
        logging.FileHandler('app.log')  # 同時輸出到文件
    ]
)
logger = logging.getLogger(__name__)

# 載入環境變數
load_dotenv()

# 配置 Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=GOOGLE_API_KEY)

def generate_color_from_text(text: str) -> str:
    """
    使用 Gemini API 根據文本內容生成對應的顏色代碼
    
    Args:
        text (str): 日記內容
        
    Returns:
        str: 十六進制顏色代碼 (例如: "#FF5733")
    """
    try:
        # 構建提示詞
        prompt = f"""
        請根據以下日記內容，生成一個最能代表這段文字情感的十六進制顏色代碼。
        顏色應該反映文字的主要情感基調。
        只返回顏色代碼，格式為 #RRGGBB，不要包含其他文字或解釋。
        
        日記內容：
        {text}
        """
        
        logger.info(f"開始生成顏色代碼，輸入文本: {text}")
        
        # 調用 Gemini API
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        
        logger.info(f"API 響應: {response.text}")
        
        # 提取顏色代碼
        color_code = response.text.strip()
        
        # 檢查是否為空
        if not color_code:
            logger.error("API 返回了空響應")
            raise HTTPException(
                status_code=500,
                detail="API returned empty response"
            )
        
        # 驗證顏色代碼格式
        if not color_code.startswith("#") or len(color_code) != 7:
            logger.error(f"無效的顏色代碼格式: {color_code}")
            raise HTTPException(
                status_code=500,
                detail=f"Invalid color code format: {color_code}"
            )
        
        logger.info(f"成功生成顏色代碼: {color_code}")
        return color_code
        
    except Exception as e:
        logger.error(f"生成顏色代碼時發生錯誤: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error generating color code: {str(e)}"
        ) 
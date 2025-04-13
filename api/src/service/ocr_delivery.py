import json
from fastapi import APIRouter, HTTPException, Depends , Request , Header, File, UploadFile
from src.service.utils import process_delivery_image 
import logging 

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/delivery")
async def delivery_ocr(file: UploadFile = File(...)):
    """Extract delivery information from an uploaded image."""
    logger.info(f"Received delivery OCR request for file: {file.filename}")
    try:
        extracted_data = await process_delivery_image(file)
        logger.info(f"Extraction successful for file: {file.filename}")
        return {"extracted_data": extracted_data.model_dump()}
    except Exception as e:
        logger.exception(f"OCR processing failed for {file.filename}: {e}")
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")

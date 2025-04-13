import os
import shutil
import aiofiles
import asyncio
import logging
from PIL import Image
from fastapi import  UploadFile
from src.core.config import config 
from src.core.prompt import DELIVERY_PROMPT
from src.core.llm import genai_client
from src.core.schema import DeliverySummary

# ----------------------------------------

def load_image(image_path):
    return Image.open(image_path)

def save_image(image_path, output_path):
    image = load_image(image_path)
    image.save(output_path)
    return output_path

def save_file(file: UploadFile) -> str:
    """save file in the specified directory."""
    
    file_path = os.path.join(config.MAIN_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return file_path

async def save_file_async(file: UploadFile) -> str:
    """Save uploaded file asynchronously to MAIN_DIR."""
    os.makedirs(config.MAIN_DIR, exist_ok=True)
    path = os.path.join(config.MAIN_DIR, file.filename)

    async with aiofiles.open(path, "wb") as out_file:
        while chunk := await file.read(1024 * 64):
            await out_file.write(chunk)
    return path

async def process_delivery_image(file: UploadFile) -> DeliverySummary:
    """Handles full OCR pipeline: save, load, extract."""
    image_path = await save_file_async(file)
    image = load_image(image_path)
    response = genai_client.models.generate_content(
        model = config.GENERATIVE_MODEL,
        contents = [DELIVERY_PROMPT, image],
        config={
            'response_schema': DeliverySummary,
            'response_mime_type': 'application/json'
        })
    return response.parsed
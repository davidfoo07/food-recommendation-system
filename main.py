import os
import uuid
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class MealAnalysis(BaseModel):
    dish_name: str
    cuisine: str
    ingredients: List[str]
    is_healthy: bool
    summary: str
    
@app.post("/log-meal/{user_id}", response_model=MealAnalysis)
async def log_meal(user_id: str, file: UploadFile = File(...)):
    # Validation for images
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")
    
    # Save the file temporarily
    file_extension = file.filename.split(".")[-1]
    temp_file_path = f"temp_{user_id}_{uuid.uuid4()}.{file_extension}"
    with open(temp_file_path, "wb") as buffer:
        buffer.write(await file.read())
        
    try:
        # call the CV service
        # food_data = analyze_food_image(temp_file_path)
        
        return food_data
    
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
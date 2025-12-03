# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pymongo import MongoClient
import os



MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:admin123@mongodb:27017")
client = MongoClient(MONGO_URI)
db = client["cyberBullying"]
collection = db["cyberbullying_collection"]
# --------------------------
# Load trained models
# --------------------------
model_label = joblib.load("model_label_lr.pkl")   # Stage 1: label_num
model_type = joblib.load("model_type_lr.pkl")     # Stage 2: le_type
types_le = joblib.load("types_le.pkl")            # LabelEncoder for types

# --------------------------
# FastAPI setup
# --------------------------
app = FastAPI(title="Cyberbullying Detection API")

# Input schema
class Message(BaseModel):
    text: str

# --------------------------
# Prediction endpoint
# --------------------------
@app.post("/predict")
def predict(message: Message):
    text = message.text
    
    # Stage 1: predict label
    label_pred = model_label.predict([text])[0]
    label_str = "Bullying" if label_pred == 1 else "Not-Bullying"
    
    # Stage 2: predict type only if bullying
    if label_pred == 1:
        type_pred_num = model_type.predict([text])[0]
        type_pred_str = types_le.inverse_transform([type_pred_num])[0]
    else:
        type_pred_str = "N/A"

    collection.insert_one({
        "text": text,
        "label": label_str,
        "type": type_pred_str
    })
    
    return {
        "text": text,
        "label": label_str,
        "type": type_pred_str
    }

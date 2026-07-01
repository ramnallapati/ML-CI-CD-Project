# app/main.py
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(features: list[float]):
    pred = model.predict([np.array(features)])
    return {"prediction": int(pred[0])}
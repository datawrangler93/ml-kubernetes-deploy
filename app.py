from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Features(BaseModel):
    feature1: float
    feature2: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(feats: Features):
    # Dummy model logic; replace with real model inference
    score = 0.7 * feats.feature1 + 0.3 * feats.feature2
    label = "positive" if score >= 1.5 else "negative"
    return {"score": score, "prediction": label}

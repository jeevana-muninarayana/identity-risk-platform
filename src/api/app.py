from fastapi import FastAPI
import joblib, os
from src.preprocessing import to_dataframe

app = FastAPI()
model = joblib.load(os.getenv("MODEL_PATH", "model.pkl"))

@app.post("/score")
async def score_event(event: dict):
    df = to_dataframe([event])
    score = model.decision_function(df)[0]
    return {"risk_score": float(score)}

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import numpy as np

app = FastAPI(title="NBA Career Predictor API")

# Charger modèle et scaler
model = joblib.load("stacking_final_model.pkl")
scaler = joblib.load("scaler.pkl")

# Définir le schéma d'entrée
class PlayerStats(BaseModel):
    GP: int
    MIN: float
    PTS: float
    FGM: float
    FGA: float
    FTM: float
    FTA: float
    three_pm: float
    three_pa: float
    REB: float
    AST: float
    STL: float
    BLK: float
    TOV: float

@app.post("/predict")
def predict(stats: PlayerStats):
    # Calcul des pourcentages
    FG_percent = stats.FGM / stats.FGA if stats.FGA > 0 else 0.0
    FT_percent = stats.FTM / stats.FTA if stats.FTA > 0 else 0.0
    three_p_percent = stats.three_pm / stats.three_pa if stats.three_pa > 0 else 0.0
    
    # Calcul des impacts
    FT_impact = stats.FTM * FT_percent
    threeP_impact = stats.three_pm * three_p_percent
    
    # Créer dataframe
    X_input = pd.DataFrame([{
        'GP': stats.GP,
        'MIN': stats.MIN,
        'PTS': stats.PTS,
        'FG%': FG_percent,
        'FT%': FT_percent,
        'REB': stats.REB,
        'AST': stats.AST,
        'STL': stats.STL,
        'BLK': stats.BLK,
        'TOV': stats.TOV,
        'FT_impact': FT_impact,
        '3P_impact': threeP_impact
    }])
    
    # Appliquer le scaler et prédire
    X_scaled = scaler.transform(X_input)
    y_proba = model.predict_proba(X_scaled)[:,1]
    threshold = 0.505
    y_pred = (y_proba >= threshold).astype(int)
    
    return {
        "probability": float(y_proba[0]),
        "prediction": "Longue carrière" if y_pred[0]==1 else "Carrière courte"
    }

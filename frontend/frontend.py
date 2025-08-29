import streamlit as st
import requests

st.set_page_config(page_title="NBA Career Predictor", layout="wide")
st.title("NBA Career Predictor 🏀")
st.write("Entrez les statistiques du joueur pour prédire la durée probable de sa carrière")

# Inputs
with st.form("player_form"):
    GP = st.number_input("Nombre de matchs joués (GP)", min_value=0, step=1)
    MIN = st.number_input("Minutes jouées par match (MIN)", min_value=0.0, step=0.1)
    PTS = st.number_input("Points par match (PTS)", min_value=0.0, step=0.1)
    
    FGM = st.number_input("Tirs réussis (FGM)", min_value=0.0, step=0.1)
    FGA = st.number_input("Tirs tentés (FGA)", min_value=0.0, step=0.1)
    
    FTM = st.number_input("Lancers francs réussis (FTM)", min_value=0.0, step=0.1)
    FTA = st.number_input("Lancers francs tentés (FTA)", min_value=0.0, step=0.1)
    
    three_pm = st.number_input("3-Pointers réussis", min_value=0.0, step=0.1)
    three_pa = st.number_input("3-Pointers tentés", min_value=0.0, step=0.1)
    
    REB = st.number_input("Rebonds totaux (REB)", min_value=0.0, step=0.1)
    AST = st.number_input("Passes décisives (AST)", min_value=0.0, step=0.1)
    STL = st.number_input("Interceptions (STL)", min_value=0.0, step=0.1)
    BLK = st.number_input("Contres (BLK)", min_value=0.0, step=0.1)
    TOV = st.number_input("Ballons perdus (TOV)", min_value=0.0, step=0.1)
    
    submitted = st.form_submit_button("Prédire carrière")

if submitted:
    payload = {
        "GP": GP,
        "MIN": MIN,
        "PTS": PTS,
        "FGM": FGM,
        "FGA": FGA,
        "FTM": FTM,
        "FTA": FTA,
        "three_pm": three_pm,
        "three_pa": three_pa,
        "REB": REB,
        "AST": AST,
        "STL": STL,
        "BLK": BLK,
        "TOV": TOV
    }
    
    response = requests.post("http://backend:8000/predict", json=payload)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Probabilité carrière ≥ 5 ans : {result['probability']:.2f}")
        st.info(f"Prédiction finale : {result['prediction']}")
    else:
        st.error("Erreur API, vérifiez le backend")

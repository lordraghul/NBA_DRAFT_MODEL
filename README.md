# NBA Player Career Longevity Prediction

## 📋 Project Description
**Objective**: Predict whether an NBA player will have a career of at least 5 years  
**Target Metric**: Maximize recall to identify as many players as possible who actually have long careers

---

## 🏀 Context
This project uses NBA player statistics to predict career longevity. The model helps recruiters and analysts identify promising talents early in their careers.

---

## 📊 Dataset
### Available Variables
| Feature | Description |
|---------|-------------|
| **GP** | Games Played |
| **MIN** | Minutes per game |
| **PTS** | Points per game |
| **FGM/FGA** | Field Goals Made/Attempted |
| **FG%** | Field Goal Percentage |
| **3P Made/3PA** | 3-Pointers Made/Attempted |
| **3P%** | 3-Point Percentage |
| **FTM/FTA** | Free Throws Made/Attempted |
| **FT%** | Free Throw Percentage |
| **REB/OREB/DREB** | Total/Offensive/Defensive Rebounds |
| **AST** | Assists |
| **STL** | Steals |
| **BLK** | Blocks |
| **TOV** | Turnovers |

---

## 🔧 Technical Approach

### 1. Feature Engineering
- **FT_impact** = `FTM * FT%` (combines volume and efficiency)
- **3P_impact** = `3P Made * 3P%` (3-point volume and accuracy)
- Removal of redundant variables (FGM, FGA, DREB, OREB, etc.)

### 2. Modeling
- **Stacking Classifier** combining:
  - SVM (optimized for precision)
  - XGBoost (optimized for precision)
  - Random Forest (optimized for precision)
  - Logistic Regression (optimized for precision)
- **Meta-model**: Logistic Regression
- **Optimized threshold**: 0.505

### 3. Final Metrics
- **Precision**: 0.82
- **Recall**: 0.75
- **F1-score**: 0.78

---

## 🚀 REST API - FastAPI

### Installation
```bash
pip install fastapi uvicorn scikit-learn pandas numpy
```

### File Structure
```
nba-career-prediction/
├── models/
│   ├── stack_clf_final.pkl
│   └── scaler.pkl
├── app.py
├── requirements.txt
└── test_api.py
```


**Access documentation**:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)



## 📈 Results and Interpretation

### Feature Importance
1. **GP** (Games Played) - Most influential
2. **PTS** (Points per game)
3. **MIN** (Minutes played)
4. **FT_impact** (Free throw efficiency)
5. **REB** (Total rebounds)

### Business Insights
- Players with more playing time have better chances of longevity
- Offensive productivity (scoring) is crucial
- Consistency (number of games) matters more than performance peaks

---

## 🔮 Future Improvements

1. **Additional Data**:
   - Player position
   - Draft position
   - Injury history
   - Per-36 minutes statistics

2. **Advanced Modeling**:
   - Survival analysis for exact career duration
   - Deep Learning with neural networks
   - Sequential analysis across multiple seasons

3. **Production**:
   - Docker containerization
   - Performance monitoring
   - CI/CD pipeline

---

## 👥 Practical Usage

**For Recruiters**:
- Evaluate long-term potential of rookies
- Optimize contract investments
- Identify underestimated "sleepers"

**For Analysts**:
- Understand NBA success factors
- Benchmark young player performance
- Support draft and trade decisions

---

## 📞 Contact
*Project developed as part of advanced data science analysis*

**API Documentation**: http://127.0.0.1:8000/docs  
**Source Code**: GitHub Repository  
**Technologies**: Python, Scikit-learn, FastAPI, Pandas, NumPy

---

*"Predicting NBA talent futures through data science"* 🏀📊

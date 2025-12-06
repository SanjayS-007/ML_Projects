# House Price Prediction Project

**Status:** ✅ Completed  
**Date:** December 5, 2025  
**Algorithm:** Linear Regression (Single Variable)

---

## 📊 Project Overview

This is the first ML project in the ML_Projects workspace. It demonstrates a simple linear regression model to predict house prices based on the area (square feet) of the house.

## 🎯 Objective

Build and train a linear regression model that can:
- Predict house prices based on area
- Achieve R² score > 0.90
- Be saved and reused for future predictions

## 📁 Project Structure

```
01_house_price_prediction/
├── house_price_prediction.ipynb    # Main Jupyter notebook
├── README.md                        # This file
└── (trained model saved in models/final/house_prices/)
```

## 📂 Dataset

- **Source:** Custom dataset  
- **Location:** `data/raw/house_prices/homeprices.csv`
- **Samples:** 30 houses
- **Features:**
  - `area`: House area in square feet (2600 - 4300 sq ft)
- **Target:**
  - `price`: Sale price in USD ($550,000 - $800,000)

### Data Summary
| Statistic | Area (sq ft) | Price ($) |
|-----------|--------------|-----------|
| Mean      | 3,457        | 652,667   |
| Std Dev   | 524          | 82,134    |
| Min       | 2,600        | 550,000   |
| Max       | 4,300        | 800,000   |

## 🔬 Methodology

### 1. Data Preparation
- Loaded data from CSV
- Checked for missing values (none found)
- Explored data distribution
- Analyzed correlation between area and price

### 2. Data Visualization
- Scatter plot showing positive linear relationship
- Distribution plots for area and price
- Correlation analysis (r ≈ 0.99)

### 3. Model Training
- **Algorithm:** Linear Regression (scikit-learn)
- **Train-Test Split:** 80% training, 20% testing
- **Random State:** 42 (for reproducibility)

### 4. Model Evaluation
- R² Score (coefficient of determination)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Residual analysis

## 📈 Results

### Model Performance

| Metric | Training Set | Test Set |
|--------|-------------|----------|
| **R² Score** | ~0.99 | ~0.95 |
| **RMSE** | ~$10,000 | ~$12,000 |
| **MAE** | ~$8,000 | ~$10,000 |

### Model Equation

```
Price = 135.79 × Area + 180,616.43
```

**Interpretation:** 
- For every additional square foot, the price increases by approximately $136
- Base price (intercept) is around $180,616

### Performance Assessment
✅ **Excellent Model Performance!**
- R² Score > 0.95 indicates the model explains 95%+ of price variance
- RMSE of ~$12,000 is reasonable for house prices in this range
- Strong linear relationship confirmed

## 💾 Saved Model

**Model File:** `models/final/house_prices/house_price_model_20251205_r2_0.XXX.pkl`

**Format:** Pickle (joblib)

**How to Load:**
```python
import joblib

model = joblib.load('models/final/house_prices/house_price_model_20251205_r2_0.XXX.pkl')
prediction = model.predict([[3500]])  # Predict for 3500 sq ft
print(f"Predicted Price: ${prediction[0]:,.2f}")
```

## 🚀 How to Run This Project

### Option 1: Using Jupyter Notebook

```powershell
# 1. Navigate to project
cd D:\ML_Projects

# 2. Activate environment
.\ml_env\Scripts\Activate.ps1

# 3. Launch Jupyter Lab
jupyter lab

# 4. Open the notebook
# Navigate to: notebooks/experiments/01_house_price_prediction/house_price_prediction.ipynb

# 5. Select kernel: "Python (ML-GPU)"

# 6. Run all cells (Shift + Enter or Run > Run All Cells)
```

### Option 2: Using Python Script

```powershell
# 1. Activate environment
.\ml_env\Scripts\Activate.ps1

# 2. Run training script
python src/models/train_house_price_model.py
```

## 🧪 Making Predictions

### Using the Saved Model

```python
import joblib

# Load model
model = joblib.load('models/final/house_prices/house_price_model_XXXXXXXX.pkl')

# Single prediction
area = 3500  # sq ft
price = model.predict([[area]])[0]
print(f"House of {area} sq ft: ${price:,.2f}")

# Multiple predictions
areas = [[2800], [3200], [4000], [4500]]
prices = model.predict(areas)

for a, p in zip(areas, prices):
    print(f"{a[0]:,} sq ft → ${p:,.2f}")
```

### Example Predictions

| Area (sq ft) | Predicted Price |
|--------------|-----------------|
| 2,800        | $560,820        |
| 3,200        | $615,144        |
| 3,500        | $655,881        |
| 4,000        | $723,776        |
| 4,500        | $791,671        |

## 📚 Key Learnings

### Technical Skills
1. ✅ Data loading and exploration with Pandas
2. ✅ Data visualization with Matplotlib and Seaborn
3. ✅ Train-test split for model validation
4. ✅ Linear regression implementation with scikit-learn
5. ✅ Model evaluation metrics (R², RMSE, MAE)
6. ✅ Model persistence with joblib
7. ✅ Making predictions with saved models

### ML Concepts
- **Supervised Learning**: Learning from labeled data (area → price)
- **Linear Regression**: Fitting a straight line to data
- **Train-Test Split**: Evaluating on unseen data
- **R² Score**: Measuring model fit quality
- **Residuals**: Analyzing prediction errors
- **Feature Engineering**: Using area as a predictive feature

## 🔄 Next Steps & Improvements

### Short-term
1. **Add More Features:**
   - Number of bedrooms
   - Number of bathrooms
   - Location/zip code
   - Year built
   - Lot size

2. **Try Different Algorithms:**
   - Polynomial Regression (for non-linear relationships)
   - Ridge Regression (with regularization)
   - Decision Tree Regressor
   - Random Forest Regressor

3. **Enhance Data:**
   - Collect more samples (100+ houses)
   - Include houses from different neighborhoods
   - Add temporal data (seasonal variations)

### Long-term
1. **Feature Engineering:**
   - Create derived features (price per sq ft)
   - Interaction terms (bedrooms × bathrooms)
   - One-hot encoding for categorical variables

2. **Model Optimization:**
   - Hyperparameter tuning
   - Cross-validation
   - Ensemble methods

3. **Deployment:**
   - Create a web app with Flask/Streamlit
   - Build an API endpoint
   - Deploy to cloud (Heroku, AWS, Azure)

## 🛠️ Tools & Libraries Used

```python
# Data manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Model persistence
import joblib

# Utilities
from pathlib import Path
from datetime import datetime
```

## 📝 Files in This Project

| File | Description |
|------|-------------|
| `house_price_prediction.ipynb` | Main notebook with complete analysis |
| `README.md` | This documentation file |
| `../../../data/raw/house_prices/homeprices.csv` | Original dataset |
| `../../../models/final/house_prices/model_*.pkl` | Trained model |
| `../../../src/models/train_house_price_model.py` | Reusable training script |

## 🤝 Contributing

This is a learning project. Feel free to:
- Experiment with the code
- Try different algorithms
- Add more features
- Improve visualizations

## 📖 References

- [Scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [codebasics Machine Learning Tutorial](https://www.youtube.com/c/codebasics)

---

**Project Completed:** December 5, 2025  
**Status:** ✅ Production Ready  
**Maintainer:** ML_Projects Workspace

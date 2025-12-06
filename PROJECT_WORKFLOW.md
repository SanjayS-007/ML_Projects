# Complete ML Project Workflow Guide

**Last Updated:** December 5, 2025

This guide provides step-by-step instructions for creating, managing, and deploying machine learning projects from scratch using the ML_Projects workspace.

---

## 📋 Table of Contents

1. [Project Setup](#1-project-setup)
2. [Data Management](#2-data-management)
3. [Exploratory Data Analysis](#3-exploratory-data-analysis)
4. [Model Development](#4-model-development)
5. [Model Training & Evaluation](#5-model-training--evaluation)
6. [Model Saving & Loading](#6-model-saving--loading)
7. [Testing Saved Models](#7-testing-saved-models)
8. [Project Documentation](#8-project-documentation)
9. [Best Practices](#9-best-practices)
10. [Example: House Price Prediction](#10-example-house-price-prediction)

---

## 1. Project Setup

### Step 1.1: Create Project Directory Structure

For each new project, create a dedicated folder structure:

```powershell
# Navigate to ML_Projects
cd D:\ML_Projects

# Activate virtual environment
.\ml_env\Scripts\Activate.ps1

# Create project folders (example: project name = sentiment_analysis)
mkdir notebooks\experiments\02_sentiment_analysis
mkdir data\raw\sentiment_analysis
mkdir data\processed\sentiment_analysis
mkdir models\final\sentiment_analysis
```

**Naming Convention:**
- Use sequential numbering for projects: `01_project_name`, `02_project_name`
- Use lowercase with underscores: `house_price_prediction`, `sentiment_analysis`
- Keep names descriptive but concise

### Step 1.2: Environment Verification

Before starting, verify your environment:

```powershell
# Check Python version
python --version  # Should be 3.12.6

# Check GPU availability (if using deep learning)
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# List installed packages
pip list
```

---

## 2. Data Management

### Step 2.1: Acquiring Data

**Sources:**
- Kaggle: https://www.kaggle.com/datasets
- UCI ML Repository: https://archive.ics.uci.edu/ml/index.php
- Built-in datasets: `sklearn.datasets`
- Custom data collection

### Step 2.2: Organizing Data

**Data Directory Structure:**

```
data/
├── raw/                      # NEVER modify these files
│   └── project_name/
│       ├── dataset.csv
│       └── README.txt        # Document data source and description
│
├── processed/                # Cleaned and transformed data
│   └── project_name/
│       ├── train.csv
│       ├── test.csv
│       └── features.csv
│
├── interim/                  # Intermediate transformations
│   └── project_name/
│       └── preprocessed.csv
│
└── external/                 # Third-party data
    └── project_name/
        └── external_data.csv
```

### Step 2.3: Data Storage Rules

**✅ DO:**
- Keep raw data immutable (never edit original files)
- Document data sources in a README or comments
- Use `.gitignore` to exclude large files
- Save processed data with clear naming (e.g., `train_cleaned.csv`)

**❌ DON'T:**
- Commit large datasets to Git (>10 MB)
- Modify raw data files directly
- Store data in notebook directories
- Use inconsistent file names

### Step 2.4: Creating Data Documentation

Create a `data/raw/project_name/README.txt`:

```
Dataset: House Prices
Source: Custom Dataset / Kaggle / UCI
Date Downloaded: December 5, 2025
Description: House prices with area as feature
Columns:
  - area: Square footage of the house
  - price: Sale price in USD
Samples: 30
License: Public Domain
```

---

## 3. Exploratory Data Analysis

### Step 3.1: Create EDA Notebook

Create a notebook in `notebooks/exploratory/`:

```powershell
# Example: eda_house_prices.ipynb
jupyter lab
# Navigate to notebooks/exploratory/ and create new notebook
```

### Step 3.2: Standard EDA Workflow

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('../../data/raw/project_name/dataset.csv')

# 1. Basic Overview
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

# 2. Check for missing values
print(df.isnull().sum())

# 3. Visualizations
# - Distribution plots
# - Correlation heatmaps
# - Scatter plots
# - Box plots for outliers

# 4. Feature analysis
# - Identify important features
# - Check correlations
# - Detect outliers
```

### Step 3.3: Save Cleaned Data

After exploration and cleaning:

```python
# Save processed data
df_cleaned.to_csv('../../data/processed/project_name/cleaned_data.csv', index=False)
print("✅ Cleaned data saved!")
```

---

## 4. Model Development

### Step 4.1: Create Experiment Notebook

Create a comprehensive notebook in `notebooks/experiments/project_number_name/`:

**Notebook Structure:**

1. **Title & Objective**
2. **Import Libraries**
3. **Load Data**
4. **Data Exploration**
5. **Data Visualization**
6. **Data Preparation** (train-test split)
7. **Model Training**
8. **Model Evaluation**
9. **Predictions**
10. **Model Saving**
11. **Summary & Next Steps**

### Step 4.2: Choosing Algorithms

**Common Algorithms:**

| Problem Type | Algorithms |
|--------------|------------|
| **Regression** | Linear Regression, Ridge, Lasso, Random Forest Regressor, XGBoost |
| **Classification** | Logistic Regression, Decision Tree, Random Forest, SVM, Neural Networks |
| **Clustering** | K-Means, DBSCAN, Hierarchical Clustering |
| **Time Series** | ARIMA, LSTM, Prophet |
| **NLP** | TF-IDF + Classifier, Word2Vec, BERT |
| **Computer Vision** | CNN, ResNet, YOLO, U-Net |

---

## 5. Model Training & Evaluation

### Step 5.1: Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,      # 80% train, 20% test
    random_state=42     # For reproducibility
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
```

### Step 5.2: Model Training

```python
from sklearn.linear_model import LinearRegression

# Initialize model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

print("✅ Model trained!")
```

### Step 5.3: Model Evaluation

**Regression Metrics:**

```python
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
```

**Classification Metrics:**

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')
plt.show()
```

---

## 6. Model Saving & Loading

### Step 6.1: Save Trained Model

**Using joblib (recommended for scikit-learn):**

```python
import joblib
from datetime import datetime
from pathlib import Path

# Create descriptive filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
r2_score_value = 0.945  # Your model's R² score
model_filename = f'model_{timestamp}_r2_{r2_score_value:.3f}.pkl'

# Define save path
model_path = Path('../../models/final/project_name') / model_filename

# Save model
joblib.dump(model, model_path)
print(f"✅ Model saved to: {model_path}")
```

**Naming Convention for Models:**

```
Format: {algorithm}_{date}_{metric}_{value}.pkl

Examples:
- linear_regression_20251205_r2_0.945.pkl
- random_forest_20251205_acc_0.87.pkl
- xgboost_20251205_f1_0.92.pkl
```

### Step 6.2: Save Additional Artifacts

**Save preprocessing objects:**

```python
# Save scaler (if used)
joblib.dump(scaler, 'models/final/project_name/scaler.pkl')

# Save encoder (if used)
joblib.dump(encoder, 'models/final/project_name/encoder.pkl')

# Save feature names
feature_names = X_train.columns.tolist()
joblib.dump(feature_names, 'models/final/project_name/feature_names.pkl')
```

### Step 6.3: Model Metadata

Create a `model_info.txt` file alongside your saved model:

```
Model: Linear Regression
Project: House Price Prediction
Date Trained: 2025-12-05
Dataset: homeprices.csv (30 samples)
Features: area (sq ft)
Target: price ($)

Performance Metrics:
- R² Score: 0.9450
- RMSE: $12,345
- MAE: $9,876

Training Parameters:
- Test Size: 0.2
- Random State: 42

File: linear_regression_20251205_r2_0.945.pkl
```

---

## 7. Testing Saved Models

### Step 7.1: Load Model

```python
import joblib

# Load the saved model
model_path = 'models/final/project_name/model.pkl'
loaded_model = joblib.load(model_path)

print("✅ Model loaded successfully!")
```

### Step 7.2: Make Predictions

```python
# Prepare new data (same format as training data)
new_data = [[3500]]  # Example: 3500 sq ft house

# Make prediction
prediction = loaded_model.predict(new_data)

print(f"Prediction: ${prediction[0]:,.2f}")
```

### Step 7.3: Batch Predictions

```python
# Multiple predictions
new_areas = [[2800], [3200], [4000], [4500]]
predictions = loaded_model.predict(new_areas)

# Display results
for area, price in zip(new_areas, predictions):
    print(f"Area: {area[0]:,} sq ft → Price: ${price:,.2f}")
```

### Step 7.4: Create Prediction Script

Create `scripts/predict.py` for production use:

```python
"""
Prediction script for trained model
Usage: python scripts/predict.py --area 3500
"""

import joblib
import argparse
from pathlib import Path

def load_latest_model(model_dir):
    """Load the most recent model from directory."""
    model_dir = Path(model_dir)
    models = list(model_dir.glob('*.pkl'))
    
    if not models:
        raise FileNotFoundError(f"No models found in {model_dir}")
    
    # Get most recent file
    latest_model = max(models, key=lambda p: p.stat().st_mtime)
    return joblib.load(latest_model)

def predict_price(area, model_path=None):
    """Predict house price for given area."""
    
    # Load model
    if model_path:
        model = joblib.load(model_path)
    else:
        model = load_latest_model('models/final/house_prices')
    
    # Make prediction
    prediction = model.predict([[area]])[0]
    
    return prediction

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict house price')
    parser.add_argument('--area', type=float, required=True, help='House area in sq ft')
    parser.add_argument('--model', type=str, help='Path to model file (optional)')
    
    args = parser.parse_args()
    
    price = predict_price(args.area, args.model)
    print(f"Predicted price for {args.area:,} sq ft: ${price:,.2f}")
```

**Usage:**

```powershell
python scripts/predict.py --area 3500
# Output: Predicted price for 3,500 sq ft: $650,000.00
```

---

## 8. Project Documentation

### Step 8.1: Create Project README

Each project should have its own README in the notebook directory:

`notebooks/experiments/01_house_price_prediction/README.md`:

```markdown
# House Price Prediction

**Status:** ✅ Completed  
**Date:** December 5, 2025  
**Algorithm:** Linear Regression

## Objective
Predict house prices based on area (square feet).

## Dataset
- **Source:** Custom dataset
- **Samples:** 30 houses
- **Features:** area (sq ft)
- **Target:** price ($)
- **Location:** `data/raw/house_prices/homeprices.csv`

## Results
- **R² Score:** 0.9450
- **RMSE:** $12,345
- **MAE:** $9,876

## Files
- **Notebook:** `house_price_prediction.ipynb`
- **Model:** `models/final/house_prices/linear_regression_20251205_r2_0.945.pkl`
- **Script:** `src/models/train_house_price_model.py`

## How to Use
1. Open Jupyter Lab
2. Run `house_price_prediction.ipynb`
3. Or use the training script: `python src/models/train_house_price_model.py`

## Next Steps
- Try with multiple features (bedrooms, bathrooms)
- Experiment with polynomial regression
- Collect more data
```

### Step 8.2: Update Main README

Add your project to the main `README.md`:

```markdown
## 📊 Completed Projects

1. **House Price Prediction** ✅
   - Algorithm: Linear Regression
   - R² Score: 0.9450
   - Location: `notebooks/experiments/01_house_price_prediction/`
   - Date: Dec 2025

2. **Your Next Project** 🚧
   - Coming soon...
```

---

## 9. Best Practices

### 9.1 Code Organization

**✅ DO:**
- Keep notebooks focused on one task
- Move reusable code to `src/` modules
- Use functions instead of copy-pasting code
- Add docstrings to functions
- Follow PEP 8 style guide

**Example of good function:**

```python
def load_and_preprocess_data(file_path, test_size=0.2):
    """
    Load data from CSV and split into train/test sets.
    
    Parameters:
    -----------
    file_path : str
        Path to CSV file
    test_size : float
        Proportion for test set (default: 0.2)
    
    Returns:
    --------
    X_train, X_test, y_train, y_test : arrays
        Split datasets
    """
    df = pd.read_csv(file_path)
    X = df[['area']]
    y = df['price']
    return train_test_split(X, y, test_size=test_size, random_state=42)
```

### 9.2 Experiment Tracking

**Manual Tracking (Simple Projects):**

Create `experiments_log.csv`:

```csv
date,project,algorithm,r2_score,rmse,notes
2025-12-05,house_prices,Linear Regression,0.945,12345,Baseline model
2025-12-06,house_prices,Ridge Regression,0.948,11987,Added regularization
```

**Using MLflow (Advanced):**

```python
import mlflow

mlflow.start_run()
mlflow.log_param("test_size", 0.2)
mlflow.log_param("algorithm", "Linear Regression")
mlflow.log_metric("r2_score", 0.945)
mlflow.log_metric("rmse", 12345)
mlflow.sklearn.log_model(model, "model")
mlflow.end_run()
```

### 9.3 Version Control

**Git Workflow:**

```powershell
# Initialize git (if not done)
git init
git add .gitignore README.md

# Commit your code
git add notebooks/experiments/01_house_price_prediction/
git add src/models/train_house_price_model.py
git commit -m "Add house price prediction project"

# Push to GitHub
git remote add origin <your-repo-url>
git push -u origin main
```

**What to commit:**
- ✅ Code (`.py`, `.ipynb`)
- ✅ Documentation (`.md`, `.txt`)
- ✅ Config files (`.yaml`, `.json`)
- ✅ Small datasets (<10 MB)

**What NOT to commit:**
- ❌ Large datasets (>10 MB)
- ❌ Trained models (`.pkl`, `.h5`)
- ❌ Virtual environments (`ml_env/`)
- ❌ Cache files (`__pycache__/`, `.ipynb_checkpoints/`)

### 9.4 Reproducibility

**Ensure reproducibility:**

1. **Set random seeds:**
```python
import random
import numpy as np
import torch

random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
```

2. **Document environment:**
```powershell
pip freeze > requirements_project.txt
```

3. **Document data sources and preprocessing steps**

4. **Use consistent file paths:**
```python
from pathlib import Path

# Instead of: '../../data/raw/file.csv'
# Use:
project_root = Path(__file__).parent.parent.parent
data_path = project_root / 'data' / 'raw' / 'file.csv'
```

---

## 10. Example: House Price Prediction

### Complete Workflow

**Step 1: Setup**
```powershell
cd D:\ML_Projects
.\ml_env\Scripts\Activate.ps1

mkdir notebooks\experiments\01_house_price_prediction
mkdir data\raw\house_prices
mkdir data\processed\house_prices
mkdir models\final\house_prices
```

**Step 2: Get Data**
- Download or create `homeprices.csv`
- Save to `data/raw/house_prices/`

**Step 3: Create Notebook**
- Open Jupyter Lab
- Create `house_price_prediction.ipynb` in `notebooks/experiments/01_house_price_prediction/`
- Select kernel: "Python (ML-GPU)"

**Step 4: Implement in Notebook**
```python
# 1. Imports
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

# 2. Load data
df = pd.read_csv('../../../data/raw/house_prices/homeprices.csv')

# 3. Prepare data
X = df[['area']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.4f}")

# 6. Save model
joblib.dump(model, '../../../models/final/house_prices/model_20251205_r2_0.945.pkl')
```

**Step 5: Create Reusable Script**
- Create `src/models/train_house_price_model.py`
- Implement as a class or functions
- Add command-line interface

**Step 6: Test Model**
```python
# Load and test
model = joblib.load('models/final/house_prices/model_20251205_r2_0.945.pkl')
prediction = model.predict([[3500]])
print(f"Price for 3500 sq ft: ${prediction[0]:,.2f}")
```

**Step 7: Document**
- Create project README
- Document model performance
- Add usage instructions

---

## 🎯 Quick Reference Commands

### Environment
```powershell
# Activate
.\ml_env\Scripts\Activate.ps1

# Install package
pip install package_name

# List packages
pip list

# Check GPU
python -c "import torch; print(torch.cuda.is_available())"
```

### Jupyter
```powershell
# Launch Jupyter Lab
jupyter lab

# Launch Jupyter Notebook
jupyter notebook

# List kernels
jupyter kernelspec list
```

### Model Operations
```python
# Save model
import joblib
joblib.dump(model, 'path/to/model.pkl')

# Load model
model = joblib.load('path/to/model.pkl')

# Predict
prediction = model.predict([[value]])
```

---

## 📚 Additional Resources

- **Scikit-learn Documentation:** https://scikit-learn.org/
- **Pandas Documentation:** https://pandas.pydata.org/
- **Matplotlib Gallery:** https://matplotlib.org/gallery/
- **Kaggle Learn:** https://www.kaggle.com/learn
- **Machine Learning Mastery:** https://machinelearningmastery.com/

---

## ✅ Project Checklist

Before completing a project, ensure:

- [ ] Data is organized in `data/raw/project_name/`
- [ ] Processed data saved to `data/processed/project_name/`
- [ ] Notebook is complete and well-documented
- [ ] Model is trained and evaluated
- [ ] Model is saved with descriptive filename
- [ ] Model performance is documented
- [ ] Project README is created
- [ ] Code is committed to Git (if applicable)
- [ ] Results are added to main README
- [ ] You can reproduce the results from scratch

---

**Last Updated:** December 5, 2025  
**Version:** 1.0  
**Author:** ML_Projects Development Environment

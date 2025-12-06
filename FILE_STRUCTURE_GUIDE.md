# 📁 ML_Projects File Structure Guide

**Complete Reference for Organizing Machine Learning Projects**

---

## 🎯 Purpose

This guide explains WHERE to save every type of file in your ML projects, making it easy to:
- Find files quickly
- Keep projects organized
- Work on multiple projects without confusion
- Follow industry best practices

---

## 📊 Visual File Structure

```
ML_Projects/                          # 🏠 Root Directory
│
├── 📖 README.md                      # Main project documentation
├── 📋 PROJECT_WORKFLOW.md            # Complete workflow guide
├── 📋 FILE_STRUCTURE_GUIDE.md        # This file
├── 🔧 requirements.txt               # Python dependencies
├── 📝 VSCODE_EXTENSIONS.md           # VS Code extensions
├── 🚫 .gitignore                     # Git ignore rules
│
├── 📁 config/                        # ⚙️ CONFIGURATION FILES
│   ├── config.yaml                   # Main configuration
│   ├── logging.yaml                  # Logging settings
│   └── hyperparameters.yaml          # Model hyperparameters
│
├── 📁 data/                          # 💾 ALL DATA FILES
│   │
│   ├── 📁 raw/                       # 🔒 ORIGINAL DATA (NEVER EDIT!)
│   │   ├── project_name_1/
│   │   │   ├── dataset.csv
│   │   │   └── README.txt            # Data documentation
│   │   └── project_name_2/
│   │       └── data.json
│   │
│   ├── 📁 processed/                 # ✅ CLEANED DATA
│   │   ├── project_name_1/
│   │   │   ├── train.csv
│   │   │   ├── test.csv
│   │   │   └── validation.csv
│   │   └── project_name_2/
│   │       └── cleaned_data.csv
│   │
│   ├── 📁 interim/                   # 🔄 INTERMEDIATE DATA
│   │   └── project_name_1/
│   │       └── step1_preprocessed.csv
│   │
│   └── 📁 external/                  # 🌐 THIRD-PARTY DATA
│       └── reference_data.csv
│
├── 📁 notebooks/                     # 📓 JUPYTER NOTEBOOKS
│   │
│   ├── 📁 exploratory/               # 🔍 DATA EXPLORATION (EDA)
│   │   ├── eda_dataset1.ipynb
│   │   └── eda_dataset2.ipynb
│   │
│   ├── 📁 experiments/               # 🧪 MODEL EXPERIMENTS
│   │   ├── 01_project_name/
│   │   │   ├── main_notebook.ipynb
│   │   │   └── README.md
│   │   ├── 02_another_project/
│   │   │   ├── experiment.ipynb
│   │   │   └── README.md
│   │   └── 03_third_project/
│   │       └── analysis.ipynb
│   │
│   └── 📁 visualization/             # 📊 VISUALIZATION NOTEBOOKS
│       └── plots_and_charts.ipynb
│
├── 📁 src/                           # 💻 SOURCE CODE (PYTHON MODULES)
│   │
│   ├── __init__.py                   # Makes src a package
│   │
│   ├── 📁 data/                      # 📥 DATA PROCESSING
│   │   ├── __init__.py
│   │   ├── load_data.py              # Data loading functions
│   │   ├── preprocess.py             # Data cleaning
│   │   └── validate.py               # Data validation
│   │
│   ├── 📁 features/                  # 🔧 FEATURE ENGINEERING
│   │   ├── __init__.py
│   │   ├── build_features.py         # Create new features
│   │   └── select_features.py        # Feature selection
│   │
│   ├── 📁 models/                    # 🤖 MODEL CODE
│   │   ├── __init__.py
│   │   ├── train_model.py            # Training scripts
│   │   ├── predict.py                # Prediction functions
│   │   └── evaluate.py               # Model evaluation
│   │
│   ├── 📁 visualization/             # 📈 PLOTTING CODE
│   │   ├── __init__.py
│   │   └── visualize.py              # Plotting functions
│   │
│   └── 📁 utils/                     # 🛠️ UTILITY FUNCTIONS
│       ├── __init__.py
│       ├── helpers.py                # Helper functions
│       └── constants.py              # Constants
│
├── 📁 models/                        # 💾 SAVED MODELS
│   │
│   ├── 📁 checkpoints/               # 🔄 TRAINING CHECKPOINTS
│   │   └── project_name/
│   │       ├── epoch_10.pkl
│   │       └── epoch_20.pkl
│   │
│   ├── 📁 final/                     # ✅ PRODUCTION MODELS
│   │   ├── project_name_1/
│   │   │   ├── model_20251205_r2_0.945.pkl
│   │   │   ├── scaler.pkl
│   │   │   └── model_info.txt
│   │   └── project_name_2/
│   │       └── best_model.h5
│   │
│   └── 📁 experiments/               # 🧪 EXPERIMENTAL MODELS
│       └── project_name/
│           └── test_model_v1.pkl
│
├── 📁 outputs/                       # 📤 TRAINING OUTPUTS
│   │
│   ├── 📁 logs/                      # 📝 LOG FILES
│   │   ├── training_2025-12-05.log
│   │   └── errors.log
│   │
│   ├── 📁 tensorboard/               # 📊 TENSORBOARD LOGS
│   │   └── project_name/
│   │       └── events.out.tfevents...
│   │
│   └── 📁 metrics/                   # 📈 PERFORMANCE METRICS
│       └── project_name/
│           └── metrics.json
│
├── 📁 reports/                       # 📑 REPORTS & RESULTS
│   │
│   ├── 📁 figures/                   # 📊 GENERATED PLOTS
│   │   ├── project_name/
│   │   │   ├── confusion_matrix.png
│   │   │   └── roc_curve.png
│   │   └── comparison_plot.png
│   │
│   └── 📁 results/                   # 📈 PERFORMANCE RESULTS
│       ├── project_name/
│       │   └── results_summary.txt
│       └── model_comparison.csv
│
├── 📁 scripts/                       # 🚀 STANDALONE SCRIPTS
│   ├── train.py                      # Train model from command line
│   ├── predict.py                    # Make predictions
│   ├── evaluate.py                   # Evaluate model
│   └── deploy.py                     # Deployment script
│
├── 📁 tests/                         # ✅ UNIT TESTS
│   ├── test_data.py                  # Test data processing
│   ├── test_models.py                # Test model functions
│   └── test_features.py              # Test feature engineering
│
├── 📁 docs/                          # 📚 ADDITIONAL DOCUMENTATION
│   ├── api_reference.md
│   └── deployment_guide.md
│
└── 📁 ml_env/                        # 🐍 VIRTUAL ENVIRONMENT
    └── (Python packages)             # ⚠️ NEVER COMMIT THIS!
```

---

## 📖 Detailed Directory Explanations

### 🏠 Root Level Files

| File | Purpose | When to Edit |
|------|---------|--------------|
| `README.md` | Main project overview | Update when adding new projects |
| `PROJECT_WORKFLOW.md` | Complete workflow guide | Reference, rarely edit |
| `FILE_STRUCTURE_GUIDE.md` | This file | Reference only |
| `requirements.txt` | Python dependencies | When installing new packages |
| `.gitignore` | Files to exclude from Git | When adding new file types to exclude |

---

### ⚙️ config/ - Configuration Files

**What goes here:** Settings, parameters, configurations

**Examples:**
```yaml
# config/config.yaml
project:
  name: "house_price_prediction"
  version: "1.0"

data:
  raw_path: "data/raw/house_prices/"
  processed_path: "data/processed/house_prices/"

model:
  algorithm: "linear_regression"
  test_size: 0.2
  random_state: 42
```

**Naming Convention:**
- `config.yaml` - Main configuration
- `hyperparameters.yaml` - Model hyperparameters
- `logging.yaml` - Logging settings

---

### 💾 data/ - All Data Files

#### 📁 data/raw/ - Original Data (NEVER EDIT!)

**Purpose:** Store original, unchanged data

**Rules:**
- ✅ DO: Keep original files untouched
- ✅ DO: Document data source
- ❌ DON'T: Edit or delete original data
- ❌ DON'T: Commit large files (>10 MB)

**Structure:**
```
data/raw/
├── house_prices/
│   ├── homeprices.csv          # Original dataset
│   └── README.txt              # Data documentation
└── sentiment_data/
    ├── reviews.json
    └── README.txt
```

**Example README.txt:**
```
Dataset: House Prices
Source: Kaggle / Custom / UCI
Date: 2025-12-05
Description: House prices with area as feature
Columns: area, price
Samples: 30
```

---

#### 📁 data/processed/ - Cleaned Data

**Purpose:** Store cleaned, transformed data ready for modeling

**What goes here:**
- `train.csv` - Training data
- `test.csv` - Testing data
- `validation.csv` - Validation data
- `features.csv` - Engineered features

**Example:**
```
data/processed/house_prices/
├── train.csv              # 80% of data
├── test.csv               # 20% of data
└── features_engineered.csv
```

---

#### 📁 data/interim/ - Intermediate Data

**Purpose:** Store data at intermediate processing steps

**When to use:** Multi-step data pipelines

**Example:**
```
data/interim/house_prices/
├── step1_cleaned.csv
├── step2_scaled.csv
└── step3_encoded.csv
```

---

#### 📁 data/external/ - Third-party Data

**Purpose:** Store reference data from external sources

**Examples:**
- City population data
- Economic indicators
- Reference tables

---

### 📓 notebooks/ - Jupyter Notebooks

#### 📁 notebooks/exploratory/ - Exploratory Data Analysis

**Purpose:** Initial data exploration and understanding

**What goes here:**
- Data loading and inspection
- Statistical summaries
- Distribution plots
- Correlation analysis
- Missing value analysis

**Naming Convention:**
```
eda_house_prices.ipynb
eda_customer_data_2025-12-05.ipynb
exploration_dataset_name.ipynb
```

**Example Structure:**
```python
# 1. Load Data
# 2. Basic Info (shape, dtypes, head)
# 3. Statistical Summary
# 4. Missing Values
# 5. Visualizations
# 6. Correlations
# 7. Insights & Observations
```

---

#### 📁 notebooks/experiments/ - Model Experiments

**Purpose:** Complete ML project notebooks

**Structure:** One folder per project

```
notebooks/experiments/
├── 01_house_price_prediction/
│   ├── house_price_prediction.ipynb
│   └── README.md
├── 02_sentiment_analysis/
│   ├── sentiment_model.ipynb
│   └── README.md
└── 03_image_classifier/
    ├── cnn_classifier.ipynb
    └── README.md
```

**Naming Convention:**
- `01_project_name/` - Sequential numbering
- Use descriptive names
- Include project README

**Notebook Structure:**
1. Title & Objective
2. Import Libraries
3. Load Data
4. EDA (brief)
5. Data Preparation
6. Model Training
7. Evaluation
8. Predictions
9. Model Saving
10. Summary

---

#### 📁 notebooks/visualization/ - Visualization Notebooks

**Purpose:** Create publication-quality plots and charts

**What goes here:**
- Final visualizations for reports
- Comparison plots
- Dashboard prototypes

---

### 💻 src/ - Source Code

**Purpose:** Reusable Python modules and functions

**When to use:** When code is used multiple times or needs to be production-ready

#### 📁 src/data/ - Data Processing

**Files:**
```python
# src/data/load_data.py
def load_csv(file_path):
    """Load CSV file with error handling."""
    pass

# src/data/preprocess.py
def clean_data(df):
    """Clean and preprocess dataframe."""
    pass

# src/data/validate.py
def validate_schema(df, expected_columns):
    """Validate data schema."""
    pass
```

---

#### 📁 src/features/ - Feature Engineering

**Files:**
```python
# src/features/build_features.py
def create_interaction_features(df):
    """Create feature interactions."""
    pass

def engineer_features(df):
    """Create new features from existing ones."""
    pass
```

---

#### 📁 src/models/ - Model Code

**Files:**
```python
# src/models/train_model.py
class ModelTrainer:
    def train(self, X, y):
        pass
    
    def evaluate(self, X_test, y_test):
        pass

# src/models/predict.py
def predict(model, X):
    """Make predictions."""
    pass
```

---

#### 📁 src/visualization/ - Plotting Functions

**Files:**
```python
# src/visualization/visualize.py
def plot_confusion_matrix(y_true, y_pred):
    """Create confusion matrix plot."""
    pass

def plot_feature_importance(model, feature_names):
    """Plot feature importance."""
    pass
```

---

#### 📁 src/utils/ - Utility Functions

**Files:**
```python
# src/utils/helpers.py
def save_json(data, file_path):
    """Save data to JSON."""
    pass

# src/utils/constants.py
RANDOM_SEED = 42
TEST_SIZE = 0.2
```

---

### 💾 models/ - Saved Models

#### 📁 models/final/ - Production Models

**Purpose:** Store final, production-ready models

**Structure:**
```
models/final/
└── project_name/
    ├── model_20251205_r2_0.945.pkl    # The model
    ├── scaler.pkl                      # Preprocessing objects
    ├── encoder.pkl                     # Encoders
    ├── feature_names.pkl               # Feature list
    └── model_info.txt                  # Documentation
```

**Naming Convention:**
```
Format: {algorithm}_{date}_{metric}_{value}.pkl

Examples:
- linear_regression_20251205_r2_0.945.pkl
- random_forest_20251205_acc_0.87.pkl
- xgboost_20251206_f1_0.92.pkl
- lstm_20251207_loss_0.023.h5
```

**model_info.txt Template:**
```
Model: Linear Regression
Project: House Price Prediction
Date: 2025-12-05
Dataset: homeprices.csv (30 samples)
Features: area (sq ft)
Target: price ($)

Performance:
- R² Score: 0.945
- RMSE: $12,345
- MAE: $9,876

Parameters:
- test_size: 0.2
- random_state: 42

File: linear_regression_20251205_r2_0.945.pkl
```

---

#### 📁 models/checkpoints/ - Training Checkpoints

**Purpose:** Save models during training for recovery

**When to use:** Long training sessions, deep learning

**Structure:**
```
models/checkpoints/project_name/
├── epoch_10.pkl
├── epoch_20.pkl
├── epoch_30.pkl
└── best_model.pkl
```

---

#### 📁 models/experiments/ - Experimental Models

**Purpose:** Store models from experiments that aren't production-ready

**When to use:** Testing different algorithms, hyperparameters

---

### 📤 outputs/ - Training Outputs

#### 📁 outputs/logs/ - Log Files

**Purpose:** Store training logs, errors, debugging info

**Files:**
```
outputs/logs/
├── training_20251205_143022.log
├── errors_20251205.log
└── debug.log
```

---

#### 📁 outputs/tensorboard/ - TensorBoard Logs

**Purpose:** Store TensorBoard visualization data

**Structure:**
```
outputs/tensorboard/
└── project_name/
    └── events.out.tfevents.1733456789.hostname
```

**How to view:**
```powershell
tensorboard --logdir=outputs/tensorboard/project_name
```

---

#### 📁 outputs/metrics/ - Performance Metrics

**Purpose:** Store model metrics in structured format

**Files:**
```json
// outputs/metrics/house_prices/metrics.json
{
  "model": "linear_regression",
  "date": "2025-12-05",
  "metrics": {
    "r2_score": 0.945,
    "rmse": 12345,
    "mae": 9876
  },
  "parameters": {
    "test_size": 0.2,
    "random_state": 42
  }
}
```

---

### 📑 reports/ - Reports & Results

#### 📁 reports/figures/ - Generated Plots

**Purpose:** Store final plots for presentations and reports

**Structure:**
```
reports/figures/
├── house_prices/
│   ├── scatter_plot.png
│   ├── residual_plot.png
│   └── prediction_vs_actual.png
└── model_comparison.png
```

**Naming Convention:**
- Use descriptive names
- Include project name in subfolder
- Use PNG for raster, SVG for vector

---

#### 📁 reports/results/ - Performance Results

**Purpose:** Document model results and comparisons

**Files:**
```
reports/results/
├── house_prices/
│   └── model_performance.txt
└── all_projects_comparison.csv
```

---

### 🚀 scripts/ - Standalone Scripts

**Purpose:** Command-line scripts for automation

**When to use:** Production workflows, automation, deployment

**Common Scripts:**

```python
# scripts/train.py
"""Train model from command line."""
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    parser.add_argument('--model', default='linear_regression')
    args = parser.parse_args()
    
    # Training logic
```

**Usage:**
```powershell
python scripts/train.py --data data/raw/house_prices/homeprices.csv
python scripts/predict.py --model models/final/house_prices/model.pkl --area 3500
python scripts/evaluate.py --model models/final/house_prices/model.pkl
```

**Common Script Names:**
- `train.py` - Train model
- `predict.py` - Make predictions
- `evaluate.py` - Evaluate model
- `deploy.py` - Deploy model
- `preprocess_data.py` - Data preprocessing
- `download_data.py` - Download datasets

---

### ✅ tests/ - Unit Tests

**Purpose:** Test code functionality

**Structure:**
```
tests/
├── test_data.py           # Test data processing
├── test_models.py         # Test model functions
├── test_features.py       # Test feature engineering
└── test_utils.py          # Test utility functions
```

**Example:**
```python
# tests/test_data.py
import pytest
from src.data.preprocess import clean_data

def test_clean_data():
    # Test data cleaning
    df = ...
    result = clean_data(df)
    assert result.isnull().sum().sum() == 0
```

**Run tests:**
```powershell
pytest tests/
```

---

## 🎯 Quick Reference: Where to Save What

| What You're Saving | Where to Save It | Example |
|-------------------|------------------|---------|
| **Original dataset** | `data/raw/project_name/` | `data/raw/house_prices/homeprices.csv` |
| **Cleaned dataset** | `data/processed/project_name/` | `data/processed/house_prices/train.csv` |
| **EDA notebook** | `notebooks/exploratory/` | `notebooks/exploratory/eda_house_prices.ipynb` |
| **Project notebook** | `notebooks/experiments/##_project_name/` | `notebooks/experiments/01_house_price_prediction/main.ipynb` |
| **Trained model** | `models/final/project_name/` | `models/final/house_prices/model_20251205_r2_0.945.pkl` |
| **Training checkpoint** | `models/checkpoints/project_name/` | `models/checkpoints/house_prices/epoch_10.pkl` |
| **Reusable code** | `src/module_name/` | `src/models/train_model.py` |
| **Command-line script** | `scripts/` | `scripts/train.py` |
| **Generated plot** | `reports/figures/project_name/` | `reports/figures/house_prices/scatter.png` |
| **Results summary** | `reports/results/project_name/` | `reports/results/house_prices/summary.txt` |
| **Training log** | `outputs/logs/` | `outputs/logs/training_20251205.log` |
| **Model metrics** | `outputs/metrics/project_name/` | `outputs/metrics/house_prices/metrics.json` |
| **Config file** | `config/` | `config/hyperparameters.yaml` |
| **Unit test** | `tests/` | `tests/test_models.py` |

---

## 📝 Naming Conventions Summary

### Projects
```
Format: ##_descriptive_name

Examples:
- 01_house_price_prediction
- 02_sentiment_analysis
- 03_image_classification
```

### Datasets
```
Format: descriptive_name.csv

Examples:
- homeprices.csv
- customer_reviews.json
- train_cleaned.csv
- test_processed.csv
```

### Notebooks
```
Format: purpose_description.ipynb

Examples:
- eda_house_prices.ipynb
- sentiment_analysis.ipynb
- hyperparameter_tuning.ipynb
```

### Models
```
Format: {algorithm}_{date}_{metric}_{value}.{ext}

Examples:
- linear_regression_20251205_r2_0.945.pkl
- random_forest_20251205_acc_0.87.pkl
- cnn_model_20251206_loss_0.023.h5
```

### Scripts
```
Format: action.py

Examples:
- train.py
- predict.py
- evaluate.py
- preprocess_data.py
```

### Reports
```
Format: descriptive_name.{png|txt|csv}

Examples:
- confusion_matrix.png
- model_performance.txt
- results_comparison.csv
```

---

## ✅ Best Practices Checklist

### For Each New Project:

- [ ] Create project folder: `notebooks/experiments/##_project_name/`
- [ ] Create data folders:
  - [ ] `data/raw/project_name/`
  - [ ] `data/processed/project_name/`
  - [ ] `models/final/project_name/`
- [ ] Create project README in notebook folder
- [ ] Document data source in `data/raw/project_name/README.txt`
- [ ] Use clear, consistent naming
- [ ] Save models with descriptive filenames
- [ ] Document model performance
- [ ] Create `.gitignore` entries for large files
- [ ] Update main `README.md` with project info

### File Organization Rules:

✅ **DO:**
- Keep related files together
- Use descriptive names
- Document everything
- Follow naming conventions
- Separate raw and processed data
- Version your models (with dates)

❌ **DON'T:**
- Mix different projects in same folder
- Edit raw data files
- Use unclear abbreviations
- Commit large files to Git
- Save files in random locations
- Forget to document

---

## 🔍 Finding Files Quickly

### By Type:
- **Datasets?** → Look in `data/raw/project_name/`
- **Cleaned data?** → Look in `data/processed/project_name/`
- **Notebooks?** → Look in `notebooks/experiments/##_project_name/`
- **Saved models?** → Look in `models/final/project_name/`
- **Plots?** → Look in `reports/figures/project_name/`
- **Code?** → Look in `src/module_name/`
- **Scripts?** → Look in `scripts/`

### By Project:
1. Check `notebooks/experiments/` for main notebook
2. Check `data/raw/project_name/` for data
3. Check `models/final/project_name/` for saved model
4. Check project README for details

---

## 📚 Example: Complete Project Structure

Here's a complete example for "House Price Prediction":

```
ML_Projects/
│
├── data/
│   ├── raw/
│   │   └── house_prices/
│   │       ├── homeprices.csv         ← Original data
│   │       └── README.txt             ← Data docs
│   └── processed/
│       └── house_prices/
│           ├── train.csv              ← Training data
│           └── test.csv               ← Test data
│
├── notebooks/
│   ├── exploratory/
│   │   └── eda_house_prices.ipynb     ← Initial exploration
│   └── experiments/
│       └── 01_house_price_prediction/
│           ├── house_price_prediction.ipynb  ← Main notebook
│           └── README.md              ← Project docs
│
├── src/
│   └── models/
│       └── train_house_price_model.py ← Reusable code
│
├── models/
│   └── final/
│       └── house_prices/
│           ├── linear_regression_20251205_r2_0.945.pkl  ← Model
│           └── model_info.txt         ← Model docs
│
├── reports/
│   ├── figures/
│   │   └── house_prices/
│   │       ├── scatter_plot.png       ← Visualizations
│   │       └── residual_plot.png
│   └── results/
│       └── house_prices/
│           └── performance.txt        ← Results
│
└── scripts/
    └── predict_house_price.py         ← Prediction script
```

---

## 🎓 Summary

### Remember:
1. **Data** → `data/raw/` (never edit) and `data/processed/`
2. **Notebooks** → `notebooks/experiments/##_project_name/`
3. **Code** → `src/` for reusable, `scripts/` for standalone
4. **Models** → `models/final/project_name/`
5. **Outputs** → `outputs/` for logs, `reports/` for results

### The Golden Rule:
**"Everything has a place, and everything in its place!"**

If you're not sure where to save something, ask:
- Is it data? → `data/`
- Is it a notebook? → `notebooks/`
- Is it code? → `src/` or `scripts/`
- Is it a model? → `models/`
- Is it output? → `outputs/` or `reports/`

---

**Last Updated:** December 5, 2025  
**Version:** 1.0  
**For Questions:** Refer to `PROJECT_WORKFLOW.md`

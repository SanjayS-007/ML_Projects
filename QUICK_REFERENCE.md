# 🎯 QUICK REFERENCE: Where to Save Files

**Last Updated:** December 5, 2025

---

## 📖 Essential Reading

1. **FILE_STRUCTURE_GUIDE.md** ← **READ THIS FIRST!** Complete guide with examples
2. **PROJECT_WORKFLOW.md** ← Step-by-step workflow for projects
3. **README.md** ← Main project overview

---

## 🚀 Quick Lookup Table

| I want to save... | Save it in... | Example |
|------------------|---------------|---------|
| **Original dataset** | `data/raw/project_name/` | `data/raw/house_prices/homeprices.csv` |
| **Cleaned dataset** | `data/processed/project_name/` | `data/processed/house_prices/train.csv` |
| **Exploration notebook** | `notebooks/exploratory/` | `notebooks/exploratory/eda_house_prices.ipynb` |
| **Main project notebook** | `notebooks/experiments/##_project_name/` | `notebooks/experiments/01_house_price_prediction/main.ipynb` |
| **Trained model** | `models/final/project_name/` | `models/final/house_prices/model_20251205_r2_0.945.pkl` |
| **Reusable Python code** | `src/module_name/` | `src/models/train_model.py` |
| **Command-line script** | `scripts/` | `scripts/train.py` |
| **Generated plot** | `reports/figures/project_name/` | `reports/figures/house_prices/scatter.png` |
| **Training log** | `outputs/logs/` | `outputs/logs/training.log` |
| **Configuration** | `config/` | `config/hyperparameters.yaml` |

---

## 📁 For Each New Project, Create:

```powershell
# Example: Starting project "sentiment_analysis"

cd D:\ML_Projects
.\ml_env\Scripts\Activate.ps1

# Create folders
mkdir notebooks\experiments\02_sentiment_analysis
mkdir data\raw\sentiment_analysis
mkdir data\processed\sentiment_analysis
mkdir models\final\sentiment_analysis
```

---

## ✅ Naming Conventions

### Projects
```
01_house_price_prediction
02_sentiment_analysis
03_image_classifier
```

### Models
```
{algorithm}_{date}_{metric}_{value}.pkl

Examples:
- linear_regression_20251205_r2_0.945.pkl
- random_forest_20251206_acc_0.87.pkl
```

### Notebooks
```
house_price_prediction.ipynb
eda_customer_data.ipynb
```

---

## 🎯 The Golden Rules

1. **Raw data is READ-ONLY** → Never edit `data/raw/`
2. **One project = One folder** → `notebooks/experiments/##_project_name/`
3. **Document everything** → Add README files
4. **Use descriptive names** → Be clear, not clever
5. **Follow the structure** → Consistency is key

---

## 🔍 Finding Things Fast

- **Need data?** → `data/raw/project_name/`
- **Need notebook?** → `notebooks/experiments/##_project_name/`
- **Need model?** → `models/final/project_name/`
- **Need code?** → `src/` or `scripts/`
- **Need results?** → `reports/`

---

## 📚 Full Details

For complete information with examples, see:
→ **FILE_STRUCTURE_GUIDE.md**

---

**Remember:** Everything has a place, and everything in its place!

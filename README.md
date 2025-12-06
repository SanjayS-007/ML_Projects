# Machine Learning Development Environment

A comprehensive machine learning development environment configured for learning and practicing ML with GPU acceleration support.

## 🚀 Environment Overview

- **Python Version**: 3.12.6
- **GPU Support**: NVIDIA RTX 4050 Laptop GPU with CUDA 12.9
- **Virtual Environment**: `ml_env`
- **Framework**: PyTorch & TensorFlow (GPU-enabled)

## 📁 Project Structure

```
ML_Projects/
│
├── README.md                          # This file - project documentation
├── PROJECT_WORKFLOW.md               # Complete workflow guide for ML projects
├── FILE_STRUCTURE_GUIDE.md           # Detailed file organization reference
├── requirements.txt                   # Python package dependencies
├── VSCODE_EXTENSIONS.md              # Recommended VS Code extensions
│
├── config/                           # Configuration files
│   └── config.yaml                   # Project configurations
│
├── data/                             # Data directory (DO NOT commit large files)
│   ├── raw/                          # Original, immutable data
│   ├── processed/                    # Cleaned, transformed data
│   ├── interim/                      # Intermediate data transformations
│   └── external/                     # Data from third-party sources
│
├── notebooks/                        # Jupyter notebooks
│   ├── exploratory/                  # Exploratory Data Analysis (EDA)
│   ├── experiments/                  # ML experiments and prototypes
│   └── visualization/                # Data visualization notebooks
│
├── src/                              # Source code modules
│   ├── data/                         # Data loading and processing scripts
│   ├── features/                     # Feature engineering code
│   ├── models/                       # Model training and prediction
│   ├── visualization/                # Plotting and visualization
│   └── utils/                        # Utility functions and helpers
│
├── models/                           # Saved trained models
│   ├── checkpoints/                  # Training checkpoints
│   ├── final/                        # Production-ready models
│   └── experiments/                  # Experimental models
│
├── outputs/                          # Training outputs
│   ├── logs/                         # Training logs
│   ├── tensorboard/                  # TensorBoard logs
│   └── metrics/                      # Performance metrics
│
├── tests/                            # Unit tests
├── scripts/                          # Standalone scripts (train, evaluate, etc.)
├── reports/                          # Generated analysis reports
│   ├── figures/                      # Generated plots and visualizations
│   └── results/                      # Model performance results
│
└── docs/                             # Additional documentation

```

## 🛠️ Installation & Setup

### 1. Prerequisites
- Python 3.12 installed
- NVIDIA GPU with CUDA support (optional but recommended)
- Git for version control

### 2. Environment Setup

```powershell
# Navigate to project directory
cd D:\ML_Projects

# Activate virtual environment
.\ml_env\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Verify Installation

```powershell
# Check Python version
python --version  # Should show Python 3.12.6

# Check installed packages
pip list

# Verify GPU support for PyTorch
python -c "import torch; print(f'PyTorch CUDA available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'N/A'}')"

# Verify GPU support for TensorFlow
python -c "import tensorflow as tf; print(f'TensorFlow GPU devices: {tf.config.list_physical_devices(\"GPU\")}')"

# Check GPU status
gpustat
```

## 📦 Installed Packages

### Core Scientific Computing
- **numpy** - Numerical computing and arrays
- **pandas** - Data manipulation and analysis
- **scipy** - Scientific and technical computing

### Data Visualization
- **matplotlib** - Basic plotting library
- **seaborn** - Statistical data visualization
- **plotly** - Interactive visualizations

### Machine Learning
- **scikit-learn** - Traditional ML algorithms (classification, regression, clustering)
- **xgboost** - Gradient boosting framework
- **lightgbm** - Fast gradient boosting

### Deep Learning (GPU-Enabled)
- **torch** - PyTorch deep learning framework
- **torchvision** - PyTorch computer vision utilities
- **torchaudio** - PyTorch audio processing
- **tensorflow** - TensorFlow deep learning framework

### Jupyter & Interactive Development
- **jupyter** - Jupyter Notebook
- **jupyterlab** - Next-generation Jupyter interface
- **ipykernel** - IPython kernel for Jupyter
- **ipywidgets** - Interactive widgets

### Computer Vision & Image Processing
- **opencv-python** (cv2) - Computer vision library
- **pillow** (PIL) - Python Imaging Library

### Natural Language Processing
- **nltk** - Natural Language Toolkit

### Experiment Tracking & Monitoring
- **tensorboard** - Visualization toolkit for TensorFlow
- **mlflow** - ML lifecycle management
- **wandb** - Weights & Biases experiment tracking

### GPU Monitoring
- **gpustat** - Simple GPU monitoring
- **nvitop** - Interactive NVIDIA GPU monitoring

### Development Tools
- **black** - Python code formatter
- **flake8** - Code linting
- **pytest** - Testing framework

### Utilities
- **tqdm** - Progress bars
- **python-dotenv** - Environment variable management
- **pyyaml** - YAML file handling
- **joblib** - Model serialization

## 🎯 Quick Start Guide

### Starting a New ML Project

1. **Create a notebook for exploration**
   ```powershell
   # Activate environment
   .\ml_env\Scripts\Activate.ps1
   
   # Launch Jupyter Lab
   jupyter lab
   ```
   - Create new notebook in `notebooks/exploratory/`
   - Select kernel: "Python (ML-GPU)"

2. **Load and explore data**
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import seaborn as sns
   
   # Load data
   df = pd.read_csv('../data/raw/your_dataset.csv')
   
   # Basic exploration
   df.head()
   df.info()
   df.describe()
   ```

3. **Build a simple model**
   ```python
   from sklearn.model_selection import train_test_split
   from sklearn.ensemble import RandomForestClassifier
   from sklearn.metrics import accuracy_score, classification_report
   
   # Split data
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   
   # Train model
   model = RandomForestClassifier()
   model.fit(X_train, y_train)
   
   # Evaluate
   y_pred = model.predict(X_test)
   print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
   ```

### Using GPU for Deep Learning

#### PyTorch Example
```python
import torch
import torch.nn as nn

# Check GPU availability
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Create a simple model
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
).to(device)

# Your tensors will also need to be on GPU
x = torch.randn(32, 784).to(device)
output = model(x)
```

#### TensorFlow Example
```python
import tensorflow as tf

# Check GPU availability
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# TensorFlow automatically uses GPU if available
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
```

### Monitoring GPU Usage

```powershell
# Simple GPU stats
gpustat

# Interactive monitoring
nvitop

# Or use the GPU monitoring script you already have
py -3.12 D:\gpu_monitoring\gpu_monitoring.py
```

## 📊 Working with Jupyter Notebooks

### Launch Jupyter Lab
```powershell
# Make sure virtual environment is activated
.\ml_env\Scripts\Activate.ps1

# Start Jupyter Lab
jupyter lab
```

### Launch Jupyter Notebook (Classic)
```powershell
jupyter notebook
```

### Kernel Selection
- When creating a new notebook, select **"Python (ML-GPU)"** kernel
- This ensures you're using the correct environment with all installed packages

## 🔧 Development Workflow

### 1. Exploratory Phase
- Create notebooks in `notebooks/exploratory/`
- Experiment with data loading, cleaning, visualization
- Try different models and parameters

### 2. Development Phase
- Move reusable code to `src/` modules
- Create functions for data processing (`src/data/`)
- Build feature engineering pipelines (`src/features/`)
- Develop model classes (`src/models/`)

### 3. Training Phase
- Create training scripts in `scripts/`
- Save model checkpoints to `models/checkpoints/`
- Log experiments with MLflow or Weights & Biases
- Save final models to `models/final/`

### 4. Evaluation Phase
- Generate reports in `reports/`
- Save visualizations to `reports/figures/`
- Document results in `reports/results/`

## 📚 Learning Resources

### Recommended Tutorials (codebasics)
- Python for Data Science
- Pandas for Data Analysis
- NumPy Fundamentals
- Machine Learning Playlist
- Deep Learning with TensorFlow/PyTorch

### Practice Datasets
- **Kaggle**: https://www.kaggle.com/datasets
- **UCI ML Repository**: https://archive.ics.uci.edu/ml/index.php
- **Scikit-learn Datasets**: Built-in toy datasets for practice

### Documentation
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [TensorFlow Guide](https://www.tensorflow.org/guide)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🎨 Best Practices

### Code Organization
- Keep notebooks focused on exploration and experimentation
- Move production code to Python modules in `src/`
- Use meaningful variable and function names
- Add docstrings to your functions
- Follow PEP 8 style guide (use `black` for auto-formatting)

### Data Management
- **NEVER** modify raw data - keep it immutable in `data/raw/`
- Save processed data to `data/processed/`
- Document your data preprocessing steps
- Use `.gitignore` to exclude large data files from version control

### Model Management
- Save models with descriptive names including date and metrics
- Example: `random_forest_2025-12-05_acc_0.95.pkl`
- Keep track of hyperparameters used for each model
- Document model performance in `reports/results/`

### Experiment Tracking
- Use MLflow or Weights & Biases to log experiments
- Track: parameters, metrics, artifacts, and environment
- Compare different approaches systematically
- Document what worked and what didn't

### Version Control
- Commit code frequently with clear messages
- Don't commit large files (data, models) - use `.gitignore`
- Consider using DVC for data version control
- Create branches for experimental features

## 🐛 Troubleshooting

### GPU Not Detected

**PyTorch:**
```python
import torch
print(torch.cuda.is_available())  # Should be True
print(torch.cuda.get_device_name(0))  # Should show RTX 4050
```

**TensorFlow:**
```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))  # Should list GPU
```

If GPU not detected:
- Ensure NVIDIA drivers are up to date
- Reinstall CUDA toolkit if necessary
- Check that GPU-enabled versions of frameworks are installed

### Jupyter Kernel Not Found
```powershell
# Re-register the kernel
python -m ipykernel install --user --name=ml_env --display-name "Python (ML-GPU)"
```

### Import Errors
```powershell
# Make sure virtual environment is activated
.\ml_env\Scripts\Activate.ps1

# Reinstall missing package
pip install <package-name>
```

### Out of Memory (GPU)
- Reduce batch size in your training loop
- Use gradient accumulation
- Clear GPU cache: `torch.cuda.empty_cache()`
- Monitor GPU usage with `gpustat` or `nvitop`

## 🔄 Updating Packages

```powershell
# Activate environment
.\ml_env\Scripts\Activate.ps1

# Update specific package
pip install --upgrade <package-name>

# Update all packages (use with caution)
pip list --outdated
pip install --upgrade <package1> <package2> ...

# Update requirements.txt after changes
pip freeze > requirements.txt
```

## 📝 Additional Configuration

### VS Code Settings
See `VSCODE_EXTENSIONS.md` for recommended extensions and settings.

### Environment Variables
Create a `.env` file in the project root for sensitive information:
```
API_KEY=your_api_key_here
DATABASE_URL=your_database_url
```

Load in your code:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
```

## 🎓 Next Steps

1. **Start Learning**: Follow codebasics tutorials systematically
2. **Practice Daily**: Work on small projects or Kaggle competitions
3. **Build Portfolio**: Create 3-5 complete ML projects
4. **Document Everything**: Write clear READMEs and notebooks
5. **Share Your Work**: Push to GitHub, write blog posts
6. **Stay Updated**: Follow ML research, read papers, attend webinars

## 📞 Support & Resources

- **VS Code Extensions**: See `VSCODE_EXTENSIONS.md`
- **Python Documentation**: https://docs.python.org/3.12/
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/machine-learning
- **Reddit**: r/MachineLearning, r/learnmachinelearning

---

**Happy Learning! 🚀**

*Last Updated: December 5, 2025*

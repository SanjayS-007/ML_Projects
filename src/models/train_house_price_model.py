"""
House Price Prediction Model Training Script

This script trains a linear regression model to predict house prices
based on area. It can be reused for future projects with minimal modifications.

Author: ML_Projects
Date: December 5, 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
from pathlib import Path
from datetime import datetime


class HousePricePredictor:
    """
    A class to train and evaluate a linear regression model for house price prediction.
    """
    
    def __init__(self, data_path, test_size=0.2, random_state=42):
        """
        Initialize the predictor.
        
        Parameters:
        -----------
        data_path : str or Path
            Path to the CSV file containing house data
        test_size : float
            Proportion of data to use for testing (default: 0.2)
        random_state : int
            Random seed for reproducibility (default: 42)
        """
        self.data_path = Path(data_path)
        self.test_size = test_size
        self.random_state = random_state
        self.model = None
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.metrics = {}
        
    def load_data(self):
        """Load data from CSV file."""
        print(f"Loading data from {self.data_path}...")
        self.df = pd.read_csv(self.data_path)
        print(f"✅ Data loaded successfully! Shape: {self.df.shape}")
        return self.df
    
    def explore_data(self):
        """Display basic information about the dataset."""
        print("\n" + "="*60)
        print("DATASET EXPLORATION")
        print("="*60)
        
        print(f"\nDataset shape: {self.df.shape}")
        print(f"\nFirst few rows:")
        print(self.df.head())
        
        print(f"\nDataset info:")
        print(self.df.info())
        
        print(f"\nStatistical summary:")
        print(self.df.describe())
        
        print(f"\nMissing values:")
        missing = self.df.isnull().sum()
        print(missing)
        
        if missing.sum() == 0:
            print("✅ No missing values found!")
        
        # Correlation
        if 'area' in self.df.columns and 'price' in self.df.columns:
            corr = self.df['area'].corr(self.df['price'])
            print(f"\nCorrelation between Area and Price: {corr:.4f}")
    
    def visualize_data(self, save_path=None):
        """
        Create visualizations of the data.
        
        Parameters:
        -----------
        save_path : str or Path, optional
            Path to save the visualization
        """
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Scatter plot
        axes[0].scatter(self.df['area'], self.df['price'], 
                       color='blue', alpha=0.6, s=100, edgecolors='black')
        axes[0].set_xlabel('Area (Square Feet)', fontweight='bold')
        axes[0].set_ylabel('Price ($)', fontweight='bold')
        axes[0].set_title('House Prices vs Area', fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        
        # Distribution
        axes[1].hist(self.df['price'], bins=15, color='lightcoral', 
                    edgecolor='black', alpha=0.7)
        axes[1].set_xlabel('Price ($)', fontweight='bold')
        axes[1].set_ylabel('Frequency', fontweight='bold')
        axes[1].set_title('Distribution of House Price', fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✅ Visualization saved to {save_path}")
        
        plt.show()
    
    def prepare_data(self):
        """Split data into training and testing sets."""
        print("\nPreparing data for training...")
        
        X = self.df[['area']]
        y = self.df['price']
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )
        
        print(f"✅ Data split complete!")
        print(f"   Training samples: {len(self.X_train)}")
        print(f"   Testing samples: {len(self.X_test)}")
    
    def train_model(self):
        """Train the linear regression model."""
        print("\nTraining Linear Regression model...")
        
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        
        print("✅ Model trained successfully!")
        print(f"\nModel Parameters:")
        print(f"   Coefficient (slope): {self.model.coef_[0]:.2f}")
        print(f"   Intercept: {self.model.intercept_:.2f}")
        print(f"   Equation: Price = {self.model.coef_[0]:.2f} × Area + {self.model.intercept_:.2f}")
    
    def evaluate_model(self):
        """Evaluate the model on training and test sets."""
        print("\n" + "="*60)
        print("MODEL EVALUATION")
        print("="*60)
        
        # Predictions
        y_train_pred = self.model.predict(self.X_train)
        y_test_pred = self.model.predict(self.X_test)
        
        # Training metrics
        train_r2 = r2_score(self.y_train, y_train_pred)
        train_rmse = np.sqrt(mean_squared_error(self.y_train, y_train_pred))
        train_mae = mean_absolute_error(self.y_train, y_train_pred)
        
        # Test metrics
        test_r2 = r2_score(self.y_test, y_test_pred)
        test_rmse = np.sqrt(mean_squared_error(self.y_test, y_test_pred))
        test_mae = mean_absolute_error(self.y_test, y_test_pred)
        
        # Store metrics
        self.metrics = {
            'train_r2': train_r2,
            'train_rmse': train_rmse,
            'train_mae': train_mae,
            'test_r2': test_r2,
            'test_rmse': test_rmse,
            'test_mae': test_mae
        }
        
        print("\n📊 TRAINING SET:")
        print(f"   R² Score: {train_r2:.4f}")
        print(f"   RMSE: ${train_rmse:,.2f}")
        print(f"   MAE: ${train_mae:,.2f}")
        
        print("\n📊 TEST SET:")
        print(f"   R² Score: {test_r2:.4f}")
        print(f"   RMSE: ${test_rmse:,.2f}")
        print(f"   MAE: ${test_mae:,.2f}")
        
        if test_r2 > 0.9:
            print("\n✅ Excellent model performance!")
        elif test_r2 > 0.7:
            print("\n✅ Good model performance!")
        else:
            print("\n⚠️ Model needs improvement")
        
        return self.metrics
    
    def predict(self, area):
        """
        Make a prediction for a given area.
        
        Parameters:
        -----------
        area : float or list
            Area(s) in square feet
            
        Returns:
        --------
        prediction : float or array
            Predicted price(s)
        """
        if self.model is None:
            raise ValueError("Model not trained yet! Call train_model() first.")
        
        if isinstance(area, (int, float)):
            area = [[area]]
        elif isinstance(area, list) and not isinstance(area[0], list):
            area = [[a] for a in area]
        
        return self.model.predict(area)
    
    def save_model(self, output_dir='models/final/house_prices'):
        """
        Save the trained model to disk.
        
        Parameters:
        -----------
        output_dir : str or Path
            Directory to save the model
            
        Returns:
        --------
        model_path : Path
            Path where model was saved
        """
        if self.model is None:
            raise ValueError("No model to save! Train the model first.")
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        r2_score = self.metrics.get('test_r2', 0)
        model_filename = f'house_price_model_{timestamp}_r2_{r2_score:.3f}.pkl'
        model_path = output_dir / model_filename
        
        joblib.dump(self.model, model_path)
        
        print(f"\n✅ Model saved successfully!")
        print(f"📁 Location: {model_path}")
        print(f"📊 Test R² Score: {r2_score:.4f}")
        
        return model_path
    
    @staticmethod
    def load_model(model_path):
        """
        Load a saved model from disk.
        
        Parameters:
        -----------
        model_path : str or Path
            Path to the saved model file
            
        Returns:
        --------
        model : sklearn model
            Loaded model
        """
        model = joblib.load(model_path)
        print(f"✅ Model loaded from {model_path}")
        return model


def main():
    """Main function to run the complete training pipeline."""
    
    print("="*60)
    print("HOUSE PRICE PREDICTION - MODEL TRAINING")
    print("="*60)
    
    # Initialize predictor
    data_path = 'data/raw/house_prices/homeprices.csv'
    predictor = HousePricePredictor(data_path, test_size=0.2, random_state=42)
    
    # Load and explore data
    predictor.load_data()
    predictor.explore_data()
    
    # Visualize data
    predictor.visualize_data()
    
    # Prepare data
    predictor.prepare_data()
    
    # Train model
    predictor.train_model()
    
    # Evaluate model
    metrics = predictor.evaluate_model()
    
    # Make sample predictions
    print("\n" + "="*60)
    print("SAMPLE PREDICTIONS")
    print("="*60)
    
    sample_areas = [3000, 3500, 4000]
    for area in sample_areas:
        price = predictor.predict(area)[0]
        print(f"Area: {area:,} sq ft → Predicted Price: ${price:,.2f}")
    
    # Save model
    model_path = predictor.save_model()
    
    # Test loading
    print("\n" + "="*60)
    print("TESTING MODEL LOADING")
    print("="*60)
    
    loaded_model = HousePricePredictor.load_model(model_path)
    test_area = [[3300]]
    test_prediction = loaded_model.predict(test_area)[0]
    print(f"\nTest prediction with loaded model:")
    print(f"Area: 3,300 sq ft → Price: ${test_prediction:,.2f}")
    
    print("\n" + "="*60)
    print("✅ TRAINING PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*60)


if __name__ == "__main__":
    main()

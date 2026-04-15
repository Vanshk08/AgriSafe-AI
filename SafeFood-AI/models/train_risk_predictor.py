"""
Training script for risk prediction model
Trains a model to predict contamination risk based on food properties
"""

import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import sys

# Add backend to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from risk_predictor import RiskPredictor


def generate_synthetic_risk_data(n_samples=500):
    """
    Generate synthetic training data for risk prediction
    
    Args:
        n_samples: number of training samples
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    np.random.seed(42)
    
    # Food type mapping
    food_types_map = {'dairy': 0, 'meat': 1, 'seafood': 2, 'produce': 3, 'other': 4}
    food_types = list(food_types_map.keys())
    
    # Generate random features
    food_type_encoded = np.random.choice(list(range(5)), n_samples)
    storage_time = np.random.uniform(0, 240, n_samples)  # 0-240 hours
    temperature = np.random.uniform(-5, 30, n_samples)  # -5 to 30 Celsius
    
    # Calculate risk based on realistic contamination patterns
    risk = np.zeros(n_samples)
    
    for i in range(n_samples):
        food_type = food_type_encoded[i]
        time = storage_time[i]
        temp = temperature[i]
        
        # Base risk varies by food type
        base_risks = [0.3, 0.2, 0.25, 0.1, 0.15]  # dairy, meat, seafood, produce, other
        base_risk = base_risks[int(food_type)]
        
        # Risk increases with storage time (exponential)
        time_factor = 1 + (time / 240) ** 2
        
        # Temperature affects risk (optimal: 4°C for cool storage)
        temp_diff = abs(temp - 4)
        temp_factor = 1 + (temp_diff / 30) ** 1.5
        
        # Combined risk (0-100 scale)
        risk[i] = min(100, base_risk * time_factor * temp_factor * 100)
        risk[i] += np.random.normal(0, 5)  # Add noise
        risk[i] = np.clip(risk[i], 0, 100)
    
    # Prepare feature matrix
    X = np.column_stack([food_type_encoded, storage_time, temperature])
    y = risk
    
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    return X_train, X_test, y_train, y_test


def train_risk_predictor():
    """Train the risk prediction model"""
    
    print("=" * 60)
    print("SafeFood AI - Risk Prediction Model Training")
    print("=" * 60)
    
    try:
        # Create directory if not exist
        os.makedirs('saved_models', exist_ok=True)
        
        print("\n1. Generating synthetic training data...")
        X_train, X_test, y_train, y_test = generate_synthetic_risk_data(n_samples=500)
        print(f"   ✓ Generated {len(X_train)} training samples")
        print(f"   ✓ Generated {len(X_test)} testing samples")
        
        # Build and train model
        print("\n2. Building model architecture...")
        predictor = RiskPredictor()
        predictor.build_model(n_estimators=100, random_state=42)
        print("   ✓ Random Forest model built (100 estimators)")
        
        print("\n3. Training model...")
        predictor.train(X_train, y_train)
        print("   ✓ Model training completed")
        
        # Evaluate model
        print("\n4. Evaluating model...")
        y_pred = predictor.model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        print(f"   ✓ R² Score: {r2:.4f}")
        print(f"   ✓ RMSE: {rmse:.2f}")
        print(f"   ✓ MAE: {mae:.2f}")
        
        # Feature importance
        print("\n5. Model insights...")
        importance_dict = predictor.get_feature_importance()
        for feature, importance in importance_dict.items():
            print(f"   - {feature}: {importance:.4f}")
        
        # Save model
        print("\n6. Saving model...")
        model_path = 'saved_models/risk_predictor.pkl'
        predictor.save_model(model_path)
        print(f"   ✓ Model saved to {model_path}")
        
        print("\n" + "=" * 60)
        print("Training completed successfully! ✓")
        print("=" * 60)
        print(f"\nModel saved at: {os.path.abspath(model_path)}")
        print("You can now run the Flask backend with this model.")
        
        return predictor
        
    except Exception as e:
        print(f"\n✗ Error during training: {str(e)}")
        raise


if __name__ == '__main__':
    train_risk_predictor()

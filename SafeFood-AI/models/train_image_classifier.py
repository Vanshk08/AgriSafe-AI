"""
Training script for image classification model
Trains a model to detect fresh vs spoiled food using scikit-learn
"""

import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import sys

# Add backend to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from image_classifier import ImageClassifier
from dataset_loader import create_dummy_food_dataset, load_image_paths


def train_image_classifier(epochs=None, batch_size=None):
    """
    Train image classification model using scikit-learn
    
    Args:
        epochs: ignored (for compatibility)
        batch_size: ignored (for compatibility)
    """
    print("=" * 60)
    print("SafeFood AI - Image Classifier Training (Scikit-Learn)")
    print("=" * 60)
    
    try:
        # Create directories if not exist
        os.makedirs('saved_models', exist_ok=True)
        os.makedirs('../dataset/images', exist_ok=True)
        
        print("\n1. Creating dummy dataset...")
        create_dummy_food_dataset(num_per_class=75)
        print("   ✓ Dummy dataset created (75 fresh + 75 spoiled images = 150 total)")
        
        print("\n2. Loading image paths...")
        fresh_paths, spoiled_paths = load_image_paths()
        all_paths = fresh_paths + spoiled_paths
        all_labels = [0] * len(fresh_paths) + [1] * len(spoiled_paths)
        
        print(f"   ✓ Loaded {len(fresh_paths)} fresh images")
        print(f"   ✓ Loaded {len(spoiled_paths)} spoiled images")
        
        # Split into train and test
        train_paths, test_paths, train_labels, test_labels = train_test_split(
            all_paths, all_labels, test_size=0.2, random_state=42, stratify=all_labels
        )
        
        print(f"   ✓ Training samples: {len(train_paths)}")
        print(f"   ✓ Testing samples: {len(test_paths)}")
        
        # Build and train model
        print("\n3. Building model architecture...")
        classifier = ImageClassifier()
        classifier.build_model(n_estimators=100, random_state=42)
        print("   ✓ Random Forest model built (100 estimators)")
        
        print("\n4. Training model...")
        print("   This may take a minute...\n")
        
        classifier.train(
            train_paths, train_labels,
            validation_data=(test_paths, test_labels),
            bins=8
        )
        
        # Evaluate model
        print("\n5. Evaluating model...")
        
        # Extract test features for evaluation
        test_features = np.array([
            classifier.extract_color_histogram_features(path, bins=8) 
            for path in test_paths
        ])
        
        predictions = classifier.model.predict(test_features)
        
        accuracy = accuracy_score(test_labels, predictions)
        precision = precision_score(test_labels, predictions, zero_division=0)
        recall = recall_score(test_labels, predictions, zero_division=0)
        
        print(f"   ✓ Accuracy:  {accuracy*100:.2f}%")
        print(f"   ✓ Precision: {precision*100:.2f}%")
        print(f"   ✓ Recall:    {recall*100:.2f}%")
        
        # Save model
        print("\n6. Saving model...")
        model_path = 'saved_models/food_classifier.pkl'
        classifier.save_model(model_path)
        print(f"   ✓ Model saved to {model_path}")
        
        print("\n" + "=" * 60)
        print("Training completed successfully! ✓")
        print("=" * 60)
        print(f"\nModel saved at: {os.path.abspath(model_path)}")
        print("You can now run the Flask backend with this model.")
        
        return classifier
        
    except Exception as e:
        print(f"\n✗ Error during training: {str(e)}")
        import traceback
        traceback.print_exc()
        raise


if __name__ == '__main__':
    train_image_classifier()

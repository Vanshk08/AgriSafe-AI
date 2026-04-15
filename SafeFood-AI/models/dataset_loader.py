"""
Dataset Loader Module
Creates dummy food image dataset and loads images for training
"""

import os
import numpy as np
from PIL import Image, ImageFilter
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_dummy_food_images(output_dir='../dataset/images', num_per_class=75):
    """
    Create highly realistic synthetic food images for training
    With diverse conditions, lighting, and multiple spoilage patterns
    
    Args:
        output_dir: directory to save images
        num_per_class: number of images per class
    """
    
    from scipy import ndimage
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'fresh'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'spoiled'), exist_ok=True)
    
    print(f"Creating highly realistic synthetic food images in {output_dir}")
    
    # Fresh bread images - LIGHTER colors (above 180 brightness)
    print(f"Creating {num_per_class} fresh bread images...")
    for i in range(num_per_class):
        img_array = np.ones((224, 224, 3), dtype=np.uint8)
        
        # Light fresh bread - guarantee bright appearance
        base_brightness = np.random.randint(200, 245)  # BRIGHT
        base_r = np.random.randint(min(240, base_brightness - 20), 245)
        base_g = np.random.randint(min(220, base_brightness - 40), 235)
        base_b = np.random.randint(min(150, base_brightness - 100), 180)
        
        img_array[:, :, 0] = base_r
        img_array[:, :, 1] = base_g
        img_array[:, :, 2] = base_b
        
        # Small texture
        noise = np.random.normal(0, 10, (224, 224, 3))
        img_array = np.clip(img_array.astype(np.float32) + noise, 0, 255).astype(np.uint8)
        
        # Light gradient
        y, x = np.ogrid[-1:1:224j, -1:1:224j]
        gradient = (np.sin(x * 2) + np.cos(y * 2)) * 8
        gradient = np.stack([gradient, gradient, gradient], axis=2)
        img_array = np.clip(img_array.astype(np.float32) + gradient, 0, 255).astype(np.uint8)
        
        img = Image.fromarray(img_array)
        img.save(os.path.join(output_dir, 'fresh', f'fresh_{i:04d}.jpg'))
    
    # Spoiled bread images - MUCH DARKER AND OBVIOUSLY DIFFERENT
    print(f"Creating {num_per_class} spoiled bread images...")
    for i in range(num_per_class):
        img_array = np.ones((224, 224, 3), dtype=np.uint8)
        
        # EXTREMELY DARK spoiled - much darker than fresh
        base_r = np.random.randint(15, 70)     # Very low red
        base_g = np.random.randint(10, 60)     # Very low green  
        base_b = np.random.randint(8, 50)      # Very low blue
        
        img_array[:, :, 0] = base_r
        img_array[:, :, 1] = base_g
        img_array[:, :, 2] = base_b
        
        # Very dark, noisy texture (much more variation than fresh)
        noise = np.random.normal(0, 35, (224, 224, 3))  # Increased noise
        img_array = np.clip(img_array.astype(np.float32) + noise, 0, 255).astype(np.uint8)
        
        # ALWAYS add prominent mold/decay - 100% of spoiled images have visible defects
        for _ in range(np.random.randint(8, 20)):  # More mold spots
            spot_y = np.random.randint(5, 215)
            spot_x = np.random.randint(5, 215)
            spot_size = np.random.randint(30, 90)  # Larger spots
            
            mold_type = np.random.randint(0, 3)
            if mold_type == 0:  # Bright green mold (very visible)
                img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224), 1] = np.clip(
                    img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224), 1].astype(np.float32) + 120, 0, 255).astype(np.uint8)
                # Reduce red/blue to make green stand out
                img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224), 0] = np.clip(
                    img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224), 0].astype(np.float32) - 60, 0, 255).astype(np.uint8)
                img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224), 2] = np.clip(
                    img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224), 2].astype(np.float32) - 60, 0, 255).astype(np.uint8)
                    
            elif mold_type == 1:  # Black mold (very dark)
                img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224)] = np.clip(
                    img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224)].astype(np.float32) - 100, 0, 255).astype(np.uint8)
                    
            else:  # White/fuzzy mold with heavy darkening around edges
                img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224)] = np.clip(
                    img_array[spot_y:min(spot_y+spot_size, 224), spot_x:min(spot_x+spot_size, 224)].astype(np.float32) + 80, 0, 255).astype(np.uint8)
                # Add dark halo around it
                halo_size = spot_size + 20
                img_array[max(0, spot_y-10):min(224, spot_y+halo_size), max(0, spot_x-10):min(224, spot_x+halo_size)] = np.clip(
                    img_array[max(0, spot_y-10):min(224, spot_y+halo_size), max(0, spot_x-10):min(224, spot_x+halo_size)].astype(np.float32) - 40, 0, 255).astype(np.uint8)
        
        # Heavy blur to simulate decay/decomposition
        img_pil = Image.fromarray(img_array)
        img_array = np.array(img_pil.filter(ImageFilter.GaussianBlur(radius=np.random.uniform(2.0, 3.5))))
        img = Image.fromarray(img_array)
        img.save(os.path.join(output_dir, 'spoiled', f'spoiled_{i:04d}.jpg'))
    
    logger.info(f"✓ Created {num_per_class * 2} highly realistic synthetic food images")


def create_dummy_food_dataset(num_per_class=50):
    """
    Create complete dummy food dataset
    
    Args:
        num_per_class: number of images per class
    """
    create_dummy_food_images(num_per_class=num_per_class)


def load_images_from_directory(directory, label, img_height=224, img_width=224):
    """
    Load images from a directory
    
    Args:
        directory: directory containing images
        label: label for images (0 for fresh, 1 for spoiled)
        img_height: height to resize images to
        img_width: width to resize images to
        
    Returns:
        images array, labels array
    """
    images = []
    labels = []
    
    if not os.path.exists(directory):
        logger.warning(f"Directory not found: {directory}")
        return np.array(images), np.array(labels)
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            try:
                filepath = os.path.join(directory, filename)
                img = keras_image.load_img(filepath, target_size=(img_height, img_width))
                img_array = keras_image.img_to_array(img)
                
                # Normalize pixel values
                img_array = img_array / 255.0
                
                images.append(img_array)
                labels.append(label)
            except Exception as e:
                logger.warning(f"Error loading {filename}: {str(e)}")
                continue
    
    return np.array(images), np.array(labels)


def load_image_paths(data_dir='../dataset/images'):
    """
    Load image file paths from organized directory structure
    
    Args:
        data_dir: root data directory
        
    Returns:
        tuple: (fresh_image_paths, spoiled_image_paths)
    """
    fresh_dir = os.path.join(data_dir, 'fresh')
    spoiled_dir = os.path.join(data_dir, 'spoiled')
    
    fresh_paths = []
    spoiled_paths = []
    
    if os.path.exists(fresh_dir):
        fresh_paths = [os.path.join(fresh_dir, f) for f in os.listdir(fresh_dir)
                       if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    if os.path.exists(spoiled_dir):
        spoiled_paths = [os.path.join(spoiled_dir, f) for f in os.listdir(spoiled_dir)
                         if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    logger.info(f"Found {len(fresh_paths)} fresh and {len(spoiled_paths)} spoiled images")
    return fresh_paths, spoiled_paths


def load_dataset(data_dir='../dataset/images', test_split=0.2, img_height=224, img_width=224):
    """
    Load complete dataset from organized directory structure
    Expects structure:
        - data_dir/fresh/ (fresh food images)
        - data_dir/spoiled/ (spoiled food images)
    
    Args:
        data_dir: root data directory
        test_split: fraction of data to use for testing
        img_height: image height
        img_width: image width
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    print(f"Loading dataset from {data_dir}")
    
    fresh_paths, spoiled_paths = load_image_paths(data_dir)
    
    # Convert to image arrays
    X_fresh = np.array([np.array(Image.open(p).convert('RGB').resize((img_width, img_height))) / 255.0 
                        for p in fresh_paths])
    y_fresh = np.zeros(len(fresh_paths))
    
    X_spoiled = np.array([np.array(Image.open(p).convert('RGB').resize((img_width, img_height))) / 255.0 
                          for p in spoiled_paths])
    y_spoiled = np.ones(len(spoiled_paths))
    
    X = np.concatenate([X_fresh, X_spoiled], axis=0)
    y = np.concatenate([y_fresh, y_spoiled], axis=0)
    
    logger.info(f"Loaded {len(X_fresh)} fresh and {len(X_spoiled)} spoiled images")
    
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_split, random_state=42, stratify=y
    )
    
    logger.info(f"Split into {len(X_train)} train and {len(X_test)} test samples")
    
    return X_train, X_test, y_train, y_test


def load_single_image(image_path, img_height=224, img_width=224):
    """
    Load and preprocess a single image
    
    Args:
        image_path: path to image file
        img_height: image height
        img_width: image width
        
    Returns:
        normalized image array
    """
    try:
        img = Image.open(image_path).convert('RGB')
        img = img.resize((img_width, img_height))
        img_array = np.array(img) / 255.0
        return img_array
    except Exception as e:
        logger.error(f"Error loading image: {str(e)}")
        raise

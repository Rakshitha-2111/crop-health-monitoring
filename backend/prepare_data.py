import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import image

# Set path to your dataset directory
dataset_dir = 'C:\\Users\\pavan\\Desktop\\crop-soil-management\\PlantVillage'


# Image preprocessing function
def preprocess_data(dataset_dir):
    datagen = ImageDataGenerator(rescale=1./255)
    
    # Load images from directory (assumes directory structure: class_name -> images)
    data_flow = datagen.flow_from_directory(dataset_dir, 
                                            target_size=(224, 224), 
                                            batch_size=32, 
                                            class_mode='binary', 
                                            shuffle=True)
    
    # Prepare data arrays
    X_data = []
    y_data = []
    
    for img, label in data_flow:
        X_data.append(img)
        y_data.append(label)
        
    X_data = np.array(X_data)
    y_data = np.array(y_data)
    
    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)
    
    # Save processed data
    np.save('X_train.npy', X_train)
    np.save('X_test.npy', X_test)
    np.save('y_train.npy', y_train)
    np.save('y_test.npy', y_test)

# Run the data preparation
preprocess_data(dataset_dir)

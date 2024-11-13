# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
# Here, we assume that you already have a CSV file 'crop_data.csv' with columns 'N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', and 'label' (the crop label).
data = pd.read_csv('Crop_recommendation.csv')

# Display first few rows of the dataset to ensure it's loaded correctly
print("Dataset loaded successfully:")
print(data.head())

# Step 2: Prepare the dataset (features and target variable)
# Separate the features (X) and the target variable (y)
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]  # Features
y = data['label']  # Target variable (crop type)

# Step 3: Split the dataset into training and testing sets
# We will use 80% of the data for training and 20% for testing to evaluate model performance.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]} rows, Test set size: {X_test.shape[0]} rows")

# Step 4: Train the Random Forest model
# We use Random Forest as the machine learning algorithm to train the model.
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the model's performance
# After training, we will make predictions on the test set and evaluate the model's accuracy.
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

feature_importances = model.feature_importances_
print("Feature Importance:", feature_importances)

import joblib

# Save the trained model to a file
joblib.dump(model, 'crop_recommendation_model.pkl')
print("Saved model succesfully!")


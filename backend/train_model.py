import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('Crop_recommendation.csv')

print("Dataset loaded successfully:")
print(data.head())


X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]  # Features
y = data['label'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]} rows, Test set size: {X_test.shape[0]} rows")

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

feature_importances = model.feature_importances_
print("Feature Importance:", feature_importances)

import joblib

joblib.dump(model, 'crop_recommendation_model.pkl')
print("Saved model succesfully!")


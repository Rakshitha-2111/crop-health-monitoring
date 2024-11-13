from tensorflow.keras.models import load_model

# Load the model
model = load_model('model.h5')

# Display model architecture
model.summary()

# Check class labels (if available)
print("Class labels:", model.class_names if hasattr(model, 'class_names') else "Class labels not available.")

from flask import Flask, request, jsonify 
from flask_cors import CORS
import requests
import tensorflow as tf
from PIL import Image
import numpy as np
import io
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS with options for more control
CORS(app, resources={r"/*": {"origins": "*"}})

# Load your pretrained model here (example with a saved model)
model = tf.keras.models.load_model("C:\\Users\\pavan\\Desktop\\crop-soil-management\\backend\\pest_disease_detection_model.h5")
crop_model = joblib.load('crop_recommendation_model.pkl')
# Your OpenWeatherMap API key
OPENWEATHER_API_KEY = '9ffb5287c2a3e7a844c190bbb6c64f1c'  # Replace with your actual API key

@app.route('/get-weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    if not location:
        return jsonify({"error": "Location not provided"}), 400

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()

        if response.status_code != 200:
            return jsonify({"error": "Location not found"}), 404

        result = {
            "location": weather_data.get("name"),
            "temperature": f"{weather_data['main']['temp']}°C",
            "humidity": f"{weather_data['main']['humidity']}%",
            "precipitation": f"{weather_data.get('rain', {}).get('1h', 0)} mm"  # Handle precipitation gracefully
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# New route for crop recommendation (Updated with humidity and rainfall logic)
@app.route('/get-crop-recommendation', methods=['GET'])
def get_crop_recommendation():
    location = request.args.get('location')
    N = request.args.get('N', type=int)
    P = request.args.get('P', type=int)
    K = request.args.get('K', type=int)
    ph = request.args.get('ph', type=float)

    if not location or N is None or P is None or K is None or ph is None:
        return jsonify({"error": "Location and soil data (N, P, K, pH) are required"}), 400

    try:
        # Get weather data from OpenWeather API
        weather_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric")
        weather_data = weather_response.json()

        if weather_response.status_code != 200:
            return jsonify({"error": "Location not found"}), 404

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        rainfall = weather_data.get('rain', {}).get('1h', 0)

        input_data = [[N, P, K, temperature, humidity, ph, rainfall]]

        # Get the predicted crop from the model
        predicted_crop = crop_model.predict(input_data)[0]

        return jsonify({
            "location": weather_data.get("name"),
            "temperature": f"{temperature}°C",
            "humidity": f"{humidity}%",
            "rainfall": f"{rainfall} mm",
            "recommended_crop": predicted_crop
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

classes = ["Leaf Spot", "Powdery Mildew", "Downy Mildew", "Black Rot", "Leaf Blight", "Rust", "Caterpillar", "Aphid"]

# Route for pest-disease detection
@app.route('/api/pest-disease-detection', methods=['POST'])
def pest_disease_detection():
    image_file = request.files.get('image')
    if not image_file:
        return jsonify({"error": "No image file provided"}), 400

    try:
        # Read and preprocess the image
        image = Image.open(io.BytesIO(image_file.read()))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image = image.resize((224, 224))  # Resize to model's expected input size
        image_array = np.array(image) / 255.0  # Normalize the image
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Perform prediction
        prediction = model.predict(image_array)

        # Get the class index with the highest confidence
        predicted_class_index = np.argmax(prediction, axis=1)[0]

        # Get the predicted label
        predicted_label = classes[predicted_class_index]

        return jsonify({"status": "success", "pest_status": predicted_label})

    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

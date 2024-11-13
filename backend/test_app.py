import requests

url = "http://127.0.0.1:5000/api/pest-disease-detection"  # URL of your Flask endpoint
file_path = "C:\\Users\\pavan\\Desktop\\crop-soil-management\\train\\Potato___healthy\\0be9d721-82f5-42c3-b535-7494afe01dbe___RS_HL 1814.JPG"  # Path to your test image

# Open the image file and send a POST request
with open(file_path, "rb") as image_file:
    files = {"image": image_file}
    response = requests.post(url, files=files)

# Print the response from the server
print("Response:", response.json())

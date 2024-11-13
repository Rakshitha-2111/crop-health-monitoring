import React, { useState } from "react";
import axios from "axios";
import './PestDetection.css';

function PestDetection() {
  const [pestDetectionMessage, setPestDetectionMessage] = useState("");
  const [error, setError] = useState(null);

  const fetchPestDetection = async (image) => {
    const formData = new FormData();
    formData.append("image", image);

    try {
      const response = await axios.post("http://127.0.0.1:5000/api/pest-disease-detection", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      if (response.data.status === "success") {
        setPestDetectionMessage(`Pest Status: ${response.data.pest_status}`);
      } else {
        setPestDetectionMessage("Error in pest detection.");
      }
    } catch (error) {
      setPestDetectionMessage("Error fetching pest detection data.");
    }
  };

  const handleImageUpload = (e) => {
    const image = e.target.files[0];
    if (image) {
      fetchPestDetection(image);
    }
  };

  return (
    <div className="pest-detection-container">
      <div className="bg-white p-8 rounded-md shadow-md animate__animated animate__fadeInUp">
        <h2 className="text-4xl font-bold mb-6 text-primary">Pest Detection</h2>
        <p className="text-lg mb-4 text-gray-600">Upload an image of your crops to detect any pests or diseases. Our technology helps safeguard your crops effectively.</p>
        <input
          type="file"
          onChange={handleImageUpload}
          className="w-full bg-gray-100 border-gray-300 rounded-md py-3 px-4 mb-6 focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary"
        />
        {pestDetectionMessage && (
          <p className="text-xl mb-4 text-gray-600">{pestDetectionMessage}</p>
        )}
        {error && <p className="text-red-500 mb-4">{error}</p>}
      </div>
    </div>
  );
}

export default PestDetection;

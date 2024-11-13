import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import WeatherPage from "./pages/WeatherPage";
import PestDetectionPage from "./pages/PestDetectionPage";
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/weather" element={<WeatherPage />} />
        <Route path="/pest-detection" element={<PestDetectionPage />} />
      </Routes>
    </Router>
  );
}

export default App;
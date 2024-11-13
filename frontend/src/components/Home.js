import React from "react";
import { Link } from "react-router-dom";
import './Home.css';

function Home() {
  return (
    <div className="home-container">
      <div className="hero-section animate__animated animate__fadeInUp">
        <h1 className="text-6xl font-bold mb-6 text-white">Welcome to Crop & Soil Management</h1>
        <p className="text-2xl mb-12 text-white">Your all-in-one solution for precision farming. Let’s cultivate smarter!</p>
        <p className="text-lg text-white">Track weather, optimize crop yields, and protect your crops with ease.</p>
      </div>
    </div>
  );
}

export default Home;

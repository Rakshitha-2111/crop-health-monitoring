import React, { useState } from "react";
import { Link } from "react-router-dom";
import './Navbar.css';

function Navbar() {
  const [activeLink, setActiveLink] = useState('home');

  const handleLinkHover = (link) => {
    setActiveLink(link);
  };

  return (
    <nav className="navbar bg-primary text-white py-4 shadow-lg transition-all duration-300">
      <div className="container mx-auto flex justify-between items-center">
        <div className="navbar-brand">
          <h2 className="text-3xl font-extrabold">Crop & Soil Management</h2>
        </div>
        <ul className="navbar-links flex space-x-12">
          <li>
            <Link
              to="/"
              className={`hover:text-primary-light transition-colors duration-300 ${activeLink === 'home' ? 'text-primary-light' : ''}`}
              onMouseEnter={() => handleLinkHover('home')}
              onMouseLeave={() => handleLinkHover('')}
            >
              Home
            </Link>
          </li>
          <li>
            <Link
              to="/weather"
              className={`hover:text-primary-light transition-colors duration-300 ${activeLink === 'weather' ? 'text-primary-light' : ''}`}
              onMouseEnter={() => handleLinkHover('weather')}
              onMouseLeave={() => handleLinkHover('')}
            >
              Weather & Crop Recommendation
            </Link>
          </li>
          <li>
            <Link
              to="/pest-detection"
              className={`hover:text-primary-light transition-colors duration-300 ${activeLink === 'pest-detection' ? 'text-primary-light' : ''}`}
              onMouseEnter={() => handleLinkHover('pest-detection')}
              onMouseLeave={() => handleLinkHover('')}
            >
              Pest Detection
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;

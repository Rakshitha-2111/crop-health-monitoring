import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = ({ showNavbar }) => {
  const [isActive, setIsActive] = useState(false);
  const toggleMenu = () => setIsActive(!isActive);

  return (
    <nav className={`navbar ${isActive ? 'active' : ''}`}>
      <div className="logo">Crop & Soil Management</div>
      <div className="menu-toggle" onClick={toggleMenu}>&#9776;</div>
      <ul className={`nav-links ${showNavbar ? 'visible' : ''}`}>
        <li className="nav-item"><Link to="/" onClick={toggleMenu}>Home</Link></li>
        <li className="nav-item"><Link to="/weather" onClick={toggleMenu}>Weather</Link></li>
        <li className="nav-item"><Link to="/pest-detection" onClick={toggleMenu}>Pest Detection</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;

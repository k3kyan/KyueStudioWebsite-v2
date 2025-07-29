import { Link } from 'react-router-dom';
import './Header.css';
import Logo from '../../assets/images/global/KyueStudioLogo.jpg';

import React, { useEffect, useState } from 'react';
// import api from '../../../api/fastapi';
import { useAuth } from '../../../GlobalContext';
import LogOutButton from '../forms/loginform/LogOutButton';

function Header() {
  const { isLoggedIn } = useAuth(); // getting context from GlobalContext.js, tells us whether we are logged in or not

  return (
    <header style={{ background: '#eee', padding: '1rem' }}>
        <div className="navbar-logo">
                <Link to="/">
                    <img src={Logo} alt="Kyue Studio Logo" />
                    Kyue Studio
                </Link>
            </div>

      <nav style={{ display: 'flex', gap: '1rem' }}>
        <Link to="/">Home</Link>
        <Link to="/blog">Blog</Link>
        <Link to="/art">Art</Link>
        <Link to="/shop">Shop</Link>
        <Link to="/about">About</Link>

        {/* Conditional Rendering for Protected Routes (Admin stuff) */}
        {isLoggedIn && ( // REPLACE WITH VARIABLE BOOL ON WHETHER UR LOGGED IN OR NOT
          <Link to="/admin/dashboard">Admin</Link>
          // logout button ?!
        )}
      </nav>
    </header>
  );
}

export default Header;

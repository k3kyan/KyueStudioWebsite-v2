import React from 'react'
import './Header.css';
import Logo from '../../../assets/images/KyueStudioLogo.jpg';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <>
    <div className="navbar">
        <header>

            
            <div className="navbar-logo">
                <a href='/'>
                    <img src={Logo} alt="Kyue Studio Logo" />
                    Kyue Studio
                </a>
            </div>

            <nav>
                <a href="/">Home</a>
                <a href="/">Blog</a>
                <a href="/">Projects</a>
                <a href="/">Shop</a>
                <a href="/about">About</a>
            </nav>
        </header>
    </div>
    </>
  )
}

export default Header

import React from 'react'
import './Footer.css'
import SteamLogo from '../../assets/images/global/steam-logo.jpg'
import TEMP_SocMedLogo from '../../assets/images/global/steam-logo.jpg'
import { Link } from 'react-router-dom';


// React Icons
// import { FaLinkedin, FaEmail, FaTwitter, FaInstagram, FaTumblr, FaYoutube, FaTiktok, FaSpotify } from 'react-icons/fa';

const Footer = () => {
  return (
    // {/* TODO: FAILED TO IMPLEMENT TREES AT BOTTOM OF PAGE */}
    <footer style={{ background: '#eee'}}>
      <p>© 2025 Kyue Studio</p>

      <nav>
        {/* TODO: Get rid of all a hrefs and replace with Link from React Router */}
        <a href="/LinkedIn"><img src={TEMP_SocMedLogo} alt="LinkedIn" /></a>
        <a href="/Email"><img src={TEMP_SocMedLogo} alt="Email" /></a>
        <a href="/Twitter"><img src={TEMP_SocMedLogo} alt="Twitter" /></a>
        <a href="/Instagram"><img src={TEMP_SocMedLogo} alt="Instagram" /></a>
        <a href="/Tumblr"><img src={TEMP_SocMedLogo} alt="Tumblr" /></a>
        <a href="/YouTube"><img src={TEMP_SocMedLogo} alt="YouTube" /></a>
        <a href="/TikTok"><img src={TEMP_SocMedLogo} alt="TikTok" /></a>
        <a href="/Steam"><img src={SteamLogo} alt="Steam" /></a>
      </nav>
    </footer>
  )
}

export default Footer

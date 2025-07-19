import { Link } from 'react-router-dom';
import './Header.css';
import Logo from '../../assets/images/global/KyueStudioLogo.jpg';

function Header() {
  return (
    <header style={{ background: '#eee', padding: '1rem' }}>
        <div className="navbar-logo">
                <a href='/'>
                    <img src={Logo} alt="Kyue Studio Logo" />
                    Kyue Studio
                </a>
            </div>

      <nav style={{ display: 'flex', gap: '1rem' }}>
        <Link to="/">Home</Link>
        <Link to="/blog">Blog</Link>
        <Link to="/shop">Shop</Link>
        <Link to="/about">About</Link>
      </nav>
    </header>
  );
}

export default Header;

import { useState } from 'react'
import './App.css'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Header from './components/header/Header';
import Footer from './components/footer/Footer';
import Home  from './pages/home/Home'
import About from './pages/about/About'
import Shop from './pages/shop/Shop';
import Blog from './pages/blog/Blog';
import Art from './pages/art/Art';
import Login from './pages/login/Login';
import { AuthorizationProvider } from '../GlobalContext'; // CAUTION: correct path...?

function App() {
  return (
    <BrowserRouter>
      <AuthorizationProvider>
        <Header />

        <main style={{ padding: '0 4rem 4rem' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/index.html" element={<Home />} />
            <Route path="/blog" element={<Blog />} />
            <Route path="/art" element={<Art />} />
            <Route path="/shop" element={<Shop />} />
            <Route path="/about" element={<About />} />
            <Route path="*" element={<h1>404 - Not Found</h1>} />

            
            <Route path="/login" element={<Login />} />
            {/* Protected Routes/Pages */}
            {/* <Route path="/admin" element={<Login />} /> */}
          </Routes>
        </main>

        <Footer />
      </AuthorizationProvider>
    </BrowserRouter>
  );
}

export default App;

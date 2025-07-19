import './App.css';
import React from 'react';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/home/header/Header';
import Footer from './components/home/footer/Footer';
import About from './pages/about/About';
import Home from './pages/home/Home';
import { Link } from 'react-router-dom';



function App() {
  return (
    <>
    < Header/>
      {/* TODO: reduce code by making a component with these 3 things for page templates */}
      <div className="app-container">
        <main className="main-content">
    < Header/>
      < Link to="/">Home</Link>
      < Link to="/about">About</Link>
        {/* <Router>

          <Routes>
            <Route path="/" element={<h1>Hello World!</h1>} />
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </Router> */}
        </main>
      {/* TODO: I kinda dont like that the footer is below the initial full screen but thats a later problem tbh */}
        <Footer />
      </div>
    </>
  );
}

export default App;

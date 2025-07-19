import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/home/header/Header';
import Footer from './components/home/footer/Footer';
import About from './pages/about/About';
import Home from './pages/home/Home';

function App() {
  return (
    <>
    <Router>
      {/* TODO: reduce code by making a component with these 3 things for page templates */}
      < Header/>
      <div className="app-container">
        <main className="main-content">
          <Routes>
            <Route path="/" element={<h1>Hello World!</h1>} />

            {/* <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} /> */}
          </Routes>
        </main>
      {/* TODO: I kinda dont like that the footer is below the initial full screen but thats a later problem tbh */}
        <Footer />
      </div>
    </Router>
    </>
  );
}

export default App;

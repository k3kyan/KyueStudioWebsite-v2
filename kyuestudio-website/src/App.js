import './App.css';
import Header from './components/home/header/Header';
import Footer from './components/home/footer/Footer';
import HomePageContent from './components/home/homepagecontent/HomePageContent';

function App() {
  return (
    <>
      {/* <div className="bg-black">< Header/></div> didnt work? no black bg? */}
      < Header/>
      < HomePageContent/>
      < Footer/>
    </>

  );
}

export default App;

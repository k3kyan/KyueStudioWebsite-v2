import './App.css';
// import './index.css';
import Header from './components/home/header/Header';
import Footer from './components/home/footer/Footer';
import HomePageContent from './components/home/homepagecontent/HomePageContent';
import PageTitle from './components/pageContent/pagetitle/PageTitle';

function App() {
  return (
    <>
      {/* TODO: reduce code by making a component with these 3 things for page templates */}
      < Header/>
      < PageTitle title="Home"/>
      < HomePageContent/>
      < Footer/>
    </>

  );
}

export default App;

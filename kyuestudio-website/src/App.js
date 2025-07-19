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

      {/* TODO: I kinda dont like that the footer is below the initial full screen but thats a later problem tbh */}
      <div className="app-container">
        <main className="main-content">
          <PageTitle title="Home"/>
          <HomePageContent />
        </main>
        < Footer/>
      </div>

    </>
  );
}

export default App;

import React from 'react'
import './Home.css';
import HomePageContent from '../../components/home/homepagecontent/HomePageContent';
import PageTitle from '../../components/pageContent/pagetitle/PageTitle';

const Home = () => {
  return (
    <div>
        <PageTitle title="Home" />
        <HomePageContent />
    </div>
  )
}

export default Home

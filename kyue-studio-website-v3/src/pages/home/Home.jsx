import React from 'react'
import './Home.css'
import HomePageBanner from '../../assets/images/home/HomePageBanner.jpg'
import BlogCardsRow from '../../components/cards/blogcards-row/BlogCardsRow'
import ProjectCardsRow from '../../components/cards/projectcards-row/ProjectCardsRow'

const Home = () => {
  return (
    <div>
      <div className="homepage-welcome">Welcome to my page!</div>
        
        <img src={HomePageBanner} alt="Home Page Banner" className="homepagebanner"/>

        <div>
            <h3 style={{textAlign: 'center'}}>Projects</h3>
            <ProjectCardsRow />
        </div>

        <div style={{textAlign: 'center'}}>
            <h3>Latest Blog Posts</h3>
            <BlogCardsRow />
        </div>

        <div style={{textAlign: 'center'}}>
            <h3>Latest Artworks</h3>
            TODO: last
        </div>

        <div style={{textAlign: 'center'}}>
            <h3>Latest Social Media Posts</h3>
            TODO: last
        </div>
    </div>
  )
}

export default Home

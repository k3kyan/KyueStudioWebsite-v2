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
            <h1>Projects</h1>
            <ProjectCardsRow />
        </div>

        <div>
            <h1>Latest Blog Posts</h1>
            <BlogCardsRow />
        </div>

        <div>
            <h1>Latest Artworks</h1>
            TODO: last
        </div>

        <div>
            <h1>Latest Social Media Posts</h1>
            TODO: last
        </div>
    </div>
  )
}

export default Home

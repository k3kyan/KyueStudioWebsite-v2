import React from 'react'
import './HomePageContent.css';
import HomePageBanner from '../../../assets/images/HomePageBanner.jpg';
import BlogCard from '../../cards/blogcards/BlogCard';
import TEMPBlogPostThumbnail from '../../../assets/images/BlogPostThumbnail.PNG';
import BlogCardsGrid from '../../cards/blogcards-grid/BlogCardsGrid';

const HomePageContent = () => {
  return (
    <div>
        <div className="homepage-welcome">Welcome to my page!</div>
        
        <img src={HomePageBanner} alt="Home Page Banner" className="homepagebanner"/>

        <div>
            <h1>Projects</h1>
            <p>TODO</p>
        </div>

        <div>
            <h1>Latest Blog Posts</h1>
            <BlogCardsGrid />
        </div>

        <div>
            <h1>Latest Artworks</h1>
        </div>

        <div>
            <h1>Latest Social Media Posts</h1>
        </div>

    </div>
  )
}

export default HomePageContent

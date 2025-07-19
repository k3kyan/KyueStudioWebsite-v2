import React from 'react'
import './BlogCardsGrid.css'
import BlogCard from '../blogcard/BlogCard'

const BlogCardsGrid = ({posts}) => {
  return (
    <section className="blog-grid-container">
      {posts.map((post, index) => (
        <BlogCard key={index} {...post} />
      ))}
    </section>
  )
}

export default BlogCardsGrid

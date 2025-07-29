import React from 'react'
import './BlogCardsGrid.css'
import BlogCard from '../blogcard/BlogCard'

const BlogCardsGrid = ({posts}) => {
  return (
    <section className="blog-grid-container">
      {posts.map((post, index) => (
        // <BlogCard key={index} {...post} />
        <BlogCard
          post_id={post.id}
          title={post.title}
          tags={post.tags}
          summary={post.summary}
          thumbnail_url={post.thumbnail_url}
          date_created={post.date_created}
          link={`/blog/${post.id}`}
        />
      ))}
    </section>
  )
}

export default BlogCardsGrid

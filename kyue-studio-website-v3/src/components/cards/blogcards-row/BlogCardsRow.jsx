import React from 'react'
import './BlogCardsRow.css';
import BlogCard from '../blogcard/BlogCard';
import TEMPBlogPostThumbnail from '../../../assets/images/blogs/BlogPostThumbnail.PNG';

const BlogCardsGrid = () => {
  return (
    // TODO: make this take in a list of blog posts? and take in a number of cards to show? parameters, later
    <section className="blog-grid">
        <BlogCard image={TEMPBlogPostThumbnail} title="RPG Game Update v1.23" date="14 Oct 2022" tag="Wood" />
        <BlogCard image={TEMPBlogPostThumbnail} title="New Artwork Release" date="20 Oct 2022" tag="Art" />
        <BlogCard image={TEMPBlogPostThumbnail} title="Devlog #5" date="01 Nov 2022" tag="Devlog" />
    </section>
  )
}

export default BlogCardsGrid
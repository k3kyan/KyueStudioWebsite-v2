import React from 'react'
import './BlogCard.css';
import { FaCalendarAlt, FaTag } from 'react-icons/fa';

const BlogCard = ({ image, title, date, tag }) => {
  return (
    <div className="blog-card">
      <img src={image} alt={title} className="blog-image" />
      <h2 className="blog-title">{title}</h2>
      <div className="blog-meta">
        <div className="blog-date">
          <FaCalendarAlt className="icon" />
          <span>{date}</span>
        </div>
        <div className="blog-tag">
          <FaTag className="icon" />
          <span>{tag}</span>
        </div>
      </div>
    </div>
  )
}

export default BlogCard

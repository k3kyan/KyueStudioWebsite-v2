import React from 'react'
import './BlogCard.css';
import { FaCalendarAlt, FaTag } from 'react-icons/fa';
import { Link } from 'react-router-dom';

// TODO: probably have AWS Lambda crop the thumbnail images to a certain dimension so i dont have to crop it here
// could've included summary but kinda lazy also its a lot of work to fix that rn so i'll do it later
const BlogCard = ({ post_id, title, tags = [], summary, thumbnail_url, date_created, link = "#" }) => {
  const baseURL = "https://hioroxjfpm52qt6flna72nv2gm0ycjuy.lambda-url.us-east-2.on.aws";
// const truncateText = (text, maxLength) =>
//   text.length > maxLength ? text.slice(0, maxLength) + "..." : text;
  
  return (
    <Link to={`/blog/post/${post_id}`} className="blog-card-link" title={title}>
      <div className="blog-card">
        <img src={baseURL + '/thumbnails/' + thumbnail_url} alt={title} className="blog-image" /> 
        {/* <img src={'http://localhost:8000/thumbnails/' + thumbnail_url} alt={title} className="blog-image" />  */}
        {/* TODO: IMPORTANT: NEED TO CHANGE THIS LOCALHOST !!!! */}

        <h2 className="blog-title">{title}</h2>
        {/* <h2 className="blog-title">{truncateText(title, 50)}</h2>
        <p className="blog-summary">{truncateText(summary, 150)}</p> */}

        <div className="blog-meta">
          <div className="blog-date">
            <FaCalendarAlt className="icon" />
            <span>{new Date(date_created).toLocaleDateString()}</span>
          </div>

          <div className="blog-tag">
            <FaTag className="icon" />
            {tags.length > 0 ? (
              tags.map((tag, idx) => (
                <span key={idx} className="tag">
                  {tag}
                </span>
              ))
            ) : (
              <span className="tag">No tags</span>
            )}
          </div>
        </div>
      </div>
    </Link>
  )
}

export default BlogCard;
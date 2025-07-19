import React from 'react'
import './ProjectCard.css';
import { FaArrowUpRightFromSquare } from 'react-icons/fa6';

const ProjectCard = ({ image, title, info, link }) => {
  return (
    <div className="project-card">
      <img src={image} alt={title} className="project-image" />

      <div className="project-content">
        <div>
          <h3 className="project-title">{title}</h3>
          <p className="project-info">{info}</p>
        </div>
        
        <a href={link} target="_blank" rel="noopener noreferrer" className="project-link">
          <FaArrowUpRightFromSquare />
        </a>
      </div>
    </div>
  )
}

export default ProjectCard

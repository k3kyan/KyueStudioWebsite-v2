import React from 'react'
import './ProjectCardsRow.css'
import ProjectCard from '../projectcard/ProjectCard';
import TEMP_ProjectThumbnail from '../../../assets/images/projects/ProjectPostThumbnail.png';

// TODO: Customize more later

const ProjectCardsGrid = () => {
  return (
    <section className="blog-grid">
        <ProjectCard
            image={TEMP_ProjectThumbnail}
            title="RPG Game" 
            info="game information meow meow meow" 
            link="/"
        />
        <ProjectCard
            image={TEMP_ProjectThumbnail}
            title="Webcomic" 
            info="webcomic summary plot meow meow meow" 
            link="/"
        />
    </section>
  )
}

export default ProjectCardsGrid
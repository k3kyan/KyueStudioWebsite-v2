import React from 'react'
import './ProjectCardsGrid.css';
import TEMP_ProjectThumbnail from '../../../assets/images/ProjectPostThumbnail.jpg';
import ProjectCard from '../projectcards/ProjectCard';

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
        <ProjectCard
            image={TEMP_ProjectThumbnail}
            title="Webcomic" 
            info="webcomic summary plot meow meow meow" 
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

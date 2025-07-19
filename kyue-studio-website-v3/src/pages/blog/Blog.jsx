import React, { useState } from 'react'
import './Blog.css'
import PageTitle from '../../components/pagetitle/PageTitle';
import BlogGrid from '../../components/cards/blogcards-grid/BlogCardsGrid';
import TEMP_BlogPostThumbnail from '../../assets/images/blogs/BlogPostThumbnail.PNG';
import Filter from '../../components/filter/Filter';

// TODO: Add that bar that separates the blog posts into maximums of 12 groups <prev 1 2 3 4 ... next>


// TODO: hook up to actual database, dynamodb
const TEMP_samplePosts = [
  {
    image: TEMP_BlogPostThumbnail,
    title: 'RPG Game Update v1.23',
    date: '2025 October 15',
    tags: ['GameDev', 'RPGTitle'],
  },
  {
    image: TEMP_BlogPostThumbnail,
    title: 'Review of Fruits Basket',
    date: '2024 June 21',
    tags: ['Rambles', 'FruitsBasket'],
  },
  {
    image: TEMP_BlogPostThumbnail,
    title: 'Chibigurumi Progress #4',
    date: '2025 June 02',
    tags: ['Crafts', 'Hobbies'],
  },
  
  {
    image: TEMP_BlogPostThumbnail,
    title: 'RPG Game Update v1.23',
    date: '2025 October 15',
    tags: ['GameDev', 'RPGTitle'],
  },
  {
    image: TEMP_BlogPostThumbnail,
    title: 'Review of Fruits Basket',
    date: '2024 June 21',
    tags: ['Rambles', 'FruitsBasket'],
  },
  {
    image: TEMP_BlogPostThumbnail,
    title: 'Chibigurumi Progress #4',
    date: '2025 June 02',
    tags: ['Crafts', 'Hobbies'],
  },
  
  {
    image: TEMP_BlogPostThumbnail,
    title: 'RPG Game Update v1.23',
    date: '2025 October 15',
    tags: ['GameDev', 'RPGTitle'],
  },
  {
    image: TEMP_BlogPostThumbnail,
    title: 'Chibigurumi Progress #4',
    date: '2025 June 02',
    tags: ['Crafts', 'Hobbies'],
  },
  {
    image: TEMP_BlogPostThumbnail,
    title: 'Chibigurumi Progress #4',
    date: '2025 June 02',
    tags: ['Crafts', 'Hobbies'],
  },
];

// TODO: attempt filtering by tags again later
const tagCounts = TEMP_samplePosts.reduce((acc, post) => {
  post.tags.forEach((tag) => {
    acc[tag] = (acc[tag] || 0) + 1;
  });
  return acc;
}, {});


const Blog = () => {

  const [selectedTag, setSelectedTag] = useState(null);

  // TODO: attempt filtering by tags again later
  const filteredPosts = selectedTag
    ? TEMP_samplePosts.filter((post) => post.tags.includes(selectedTag))
    : TEMP_samplePosts;

  const tagList = Object.entries(tagCounts).map(([name, count]) => ({
    name,
    count,
  }));




  return (
    <div>
      <PageTitle title="Blog" />
      <div className="blog-layout">
        <Filter
          allTags={tagList}
          activeTag={selectedTag}
          onTagSelect={(tag) =>
            setSelectedTag((prev) => (prev === tag ? null : tag))
          }
        />
        <div>
          {/* <BlogGrid posts={TEMP_samplePosts} /> */}
          <BlogGrid posts={filteredPosts} />
        </div>
      </div>
    </div>
  )
}

export default Blog

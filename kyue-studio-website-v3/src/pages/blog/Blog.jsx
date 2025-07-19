import React from 'react'
import './Blog.css'
import PageTitle from '../../components/pagetitle/PageTitle';
import BlogGrid from '../../components/cards/blogcards-grid/BlogCardsGrid';
import TEMP_BlogPostThumbnail from '../../assets/images/blogs/BlogPostThumbnail.PNG';

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
];


const Blog = () => {
  return (
    <div>
      <PageTitle title="Blog" />
      <BlogGrid posts={TEMP_samplePosts} />
    </div>
  )
}

export default Blog

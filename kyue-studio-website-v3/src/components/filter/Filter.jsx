import React, { useState } from 'react';
import './Filter.css';

const Filter = ({ allTags, activeTag, onTagSelect }) => {
  return (
    <aside className="blog-filter">
        <input
        type="text"
        placeholder="Tags"
        className="filter-search"
        disabled
        />

        <h3 className="filter-title">Categories</h3>

        <ul className="tag-list">
        {allTags.map((tag) => (
            <li
            key={tag.name}
            className={`tag-item ${activeTag === tag.name ? 'active' : ''}`}
            onClick={() => onTagSelect(tag.name)}
            >
            <span>{tag.name}</span>
            <span className="tag-count">{tag.count}</span>
            </li>
        ))}
        </ul>
    </aside>
  )
}

export default Filter

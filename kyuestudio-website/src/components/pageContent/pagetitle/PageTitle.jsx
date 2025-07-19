import React from 'react'
import './PageTitle.css';

const PageTitle = ({title}) => {
  return (
    <div>
        <h1 className="page-title">
        ~~{title}~~
        </h1>
    </div>
  )
}

export default PageTitle

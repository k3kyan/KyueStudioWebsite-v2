import React from 'react'
import TEMP_Icon from '../../assets/images/global/KyueStudioLogo.jpg'
import './Biography.css'

const Biography = () => {
  return (
    <section className="bio-card">
      <div className="bio-image">
        <img src={TEMP_Icon} alt="Profile" />
        <div className="bio-caption">
          <strong>Ky</strong>
          <span>Programmer & Artist</span>
        </div>
      </div>

      <div className="bio-text">
        <p><strong>Bio:</strong></p>
        <p>
          meow memwrororerrrr emowrrj moewo meremow e meowr 
        </p>
      </div>
    </section>
  )
}

export default Biography

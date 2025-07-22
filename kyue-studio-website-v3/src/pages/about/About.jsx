import React from 'react'
import Biography from '../../components/bio/Biography'
import PageTitle from '../../components/pagetitle/PageTitle'
import ContactForm from '../../components/forms/contactform/ContactForm'
import { Link } from 'react-router-dom'

const About = () => {
  return (
    <div>
      <PageTitle title="About" />
      <Biography />
      <ContactForm />

      {/* TODO: TEMP login access spot*/}
      <Link to="/login">
        <button>Login</button>
      </Link>
    </div>
  )
}

export default About
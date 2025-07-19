import React from 'react'
import Biography from '../../components/bio/Biography'
import PageTitle from '../../components/pagetitle/PageTitle'
import ContactForm from '../../components/forms/contactform/ContactForm'

const About = () => {
  return (
    <div>
      <PageTitle title="About" />
      <Biography />
      <ContactForm />
    </div>
  )
}

export default About
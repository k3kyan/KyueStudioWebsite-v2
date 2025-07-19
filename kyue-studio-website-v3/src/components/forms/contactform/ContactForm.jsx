import React from 'react'
import './ContactForm.css'

// TODO: to connect this to an submission backend (ex: AWS SNS), I will need "onSubmit" logic
// TODO: Connect this form to an email or database backend

const ContactForm = () => {
  return (
    <section className="contact-form-container">
      <form className="contact-form">
        <div className="name-fields">
          <div className="form-group">
            <label htmlFor="firstName">First name</label>
            <input type="text" id="firstName" name="firstName" />
          </div>
          <div className="form-group">
            <label htmlFor="lastName">Last name</label>
            <input type="text" id="lastName" name="lastName" />
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="email">Email address</label>
          <input type="email" id="email" name="email" />
        </div>

        <div className="form-group">
          <label htmlFor="subject">Subject</label>
          <input type="text" id="subject" name="subject" />
        </div>

        <div className="form-group">
          <label htmlFor="message">Message</label>
          <textarea id="message" name="message" rows="4"></textarea>
        </div>

        <button type="submit" className="send-button">Send message</button>
      </form>

      <div className="socials">
        <a href="#"> Instagram</a>
        <a href="#"> Twitter</a>
      </div>
    </section>
  )
}

export default ContactForm

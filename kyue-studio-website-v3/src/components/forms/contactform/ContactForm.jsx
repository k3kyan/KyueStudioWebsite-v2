import React, { useEffect, useState } from 'react';
import './ContactForm.css'
import api from '../../../api/fastapi';  // connects us to backend with axios
import { useAuth } from '../../../../GlobalContext'; //context to let us know if we are logged in or not, and conditionally render

// TODO: to connect this to an submission backend (ex: AWS SNS), I will need "onSubmit" logic
// TODO: Connect this form to an email or database backend

const ContactForm = () => {
  // State variables

  // API Calls


  // Rendering UI
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

        {/* insert tags drop down here 
        # TODO: Have your frontend send values like "Bug Report", "Feedback" (from a dropdown), so it matches your enum values.
        */}

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

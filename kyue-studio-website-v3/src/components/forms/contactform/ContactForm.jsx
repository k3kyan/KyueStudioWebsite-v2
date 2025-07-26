import React, { useEffect, useState } from 'react';
import './ContactForm.css'
import api from '../../../api/fastapi';  // connects us to backend with axios
import { useAuth } from '../../../../GlobalContext'; //context to let us know if we are logged in or not, and conditionally render

// TODO: to connect this to an submission backend (ex: AWS SNS), I will need "onSubmit" logic
// TODO: Connect this form to an email or database backend

const ContactForm = () => {
  // ---------------- State variables ----------------
  // WARNING: const [message, setMessage] = useState(''); # there are so many fields in this form, so I looked into less verbose methods
  // and found u can use one useState for the whole form? not sure if this will work or is good practice but well see
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    subject: '',
    tags: [],
    message: '',
  });
  const [messageSendingProgress, setMessageSendingProgress] = useState('');
  const [sentMessage, setSentMessage] = useState(false);
  const [tags, setTags] = useState([]);  // holds the list of tags received from backend // what you can pick
  const [selectedTag, setSelectedTag] = useState([]); // holds the selected tag that the user selects // what you picked

  // TODO: DELETE: i think i can delete these? I dont need any conditional rendering for auth stuff and i think the other variable is duplicate logic so ...?
  const [sendingProgressMessage, setSendingProgressMessage] = useState('');
  const { isLoggedIn } = useAuth();

  // ---------------- API Calls ----------------

  // TODO: RESEARCH: hopefully this is correct
  // Endpoint: Get Tags
  const fetchTags = async () => {
    try {
      const response = await api.get('/contact-form/tags');
      setTags(response.data.tags);
    } catch (error) {
      console.error("Error fetching tags", error);
    }
  }

  // Endpoint: post message (used in handleSubmit form button below)

  // ---------------- Form Logic Handle Methods ----------------
  // when form is submitted
  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessageSendingProgress('Sending...');
    
    try{
      // This method worked in LoginForm.jsx, idk why its not working here. prob bc of tags tbh. 
      // format data into a variable to send to backend
      // const addDataToFormData = new FormData();
      // dataToSend.append('firstName', formData.firstName);
      // dataToSend.append('lastName', formData.lastName);
      // dataToSend.append('email', formData.email);
      // dataToSend.append('subject', formData.subject);
      // dataToSend.append('tags', [selectedTag]); // TODO: FIX: right ???
      // dataToSend.append('message', formData.message);
      // setFormData(addDataToFormData);

      // grabbed format from SwaggerUI
      const dataToSend = {
        "firstName": formData.firstName,
        "lastName": formData.lastName,
        "email": formData.email,
        "subject": formData.subject,
        "tags": [
          "Collaboration"
        ],
        "message": formData.message
      }
      // TODO: RESEARCH: is there a way i can add the endpoint prefix in one place instead of each call here or nah?
      const response = await api.post("/contact-form/message", dataToSend); // TODO: FIX: IS THIS CORRECT?? does it match up with the backend ????
      if (response.status === 200) {
        setMessageSendingProgress('Message sent successfully!');
        return response.json(); // TODO: RESEARCH: is this return response needed?
      }
      // throw response; // needed ???
    } catch (error) {
      console.error("Error sending message", error);
      setMessageSendingProgress('Error sending message');
    }
  }

  // when tag is selected
  const handleSelectTag = (e) => {
    const selectedOptions = Array.from(e.target.selectedOptions, (option) => option.value);
    setSelectedTag(selectedOptions);
  };

  // ---------------- useEffect() ----------------
  // fetch tags at the start (since need to get the list from the backend, just like i did with fetchFruit())
  // only need to do it once tho, not when any variable value changes, so the }, []); will not be used
  useEffect(() => {
    fetchTags();
  }, []); 
  
  // ---------------- Rendering UI ----------------
  return (
    <section className="contact-form-container">
      <form onSubmit={handleSubmit} className="contact-form">
        <div className="name-fields">
          <div className="form-group">
            <label htmlFor="firstName">First name</label>
            <input type="text" value={formData.firstName} onChange={(e) => setFormData({ ...formData, firstName: e.target.value })} required id="firstName" name="firstName" />
          </div>
          <div className="form-group">
            <label htmlFor="lastName">Last name</label>
            <input value={formData.lastName} onChange={(e) => setFormData({ ...formData, lastName: e.target.value })} required type="text" id="lastName" name="lastName" />
          </div>
        </div>

        {/* DONE: add email validation // oh i think react automatically does it? */}
        <div className="form-group">
          <label htmlFor="email">Email address</label>
          <input value={formData.email} onChange={(e) => setFormData({ ...formData, email: e.target.value })} required type="email" id="email" name="email" />
        </div>

        {/* insert tags drop down here 
        // use result from fetchTags() method above
        # TODO: Have your frontend send values like "Bug Report", "Feedback" (from a dropdown), so it matches your enum values.
        */}
        {/* <div className="form-group">
          <label htmlFor="tags">Tags</label>
          <select id="tags" multiple value={selectedTag} onChange={handleSelectTag}>
            <option value="">-- Please choose an option --</option>
            {tags.map((tag) => (
              <option key={tag} value={tag}>
                {tag}
              </option>
            ))}
          </select>
        </div> */}

        <div className="form-group">
          <label htmlFor="subject">Subject</label>
          <input value={formData.subject} onChange={(e) => setFormData({ ...formData, subject: e.target.value })} required type="text" id="subject" name="subject" />
        </div>

        <div className="form-group">
          <label htmlFor="message">Message</label>
          <textarea value={formData.message} onChange={(e) => setFormData({ ...formData, message: e.target.value })} required id="message" name="message" rows="4"></textarea>
        </div>

        <button type="submit" className="send-button">Send message</button>
      </form>

      <div className="socials">
        <a href="#"> Instagram</a>
        <a href="#"> Twitter</a>
      </div>

      {sentMessage ? <div>Message Sent! I'll contact you when I see it!! yahoo</div> : <div>Say something to me!</div>}
      {messageSendingProgress && <p>{messageSendingProgress}</p>}

    </section>
  )
}

export default ContactForm

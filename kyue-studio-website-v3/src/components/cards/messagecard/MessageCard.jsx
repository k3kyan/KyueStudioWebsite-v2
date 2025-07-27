import React from 'react'
import './MessageCard.css'
import api from '../../../api/fastapi';



// TODO: ???????
// 3. Update the parent component (later)
// You'll also want to add a callback prop like onDelete so the parent (like MessageCardColumnStack) can re-fetch or update state once a message is deleted.







const MessageCard = ({message}) => {
  // ---------------- State variables ----------------
  // spreading the message object (could've also passed in {...message} but i prefer to do the dirty work at lower levels)
  const { firstName, lastName, email, subject, tags, message: body } = message;

  // ---------------- API Calls ----------------

  // ---------------- Form/Button/Interactions Logic Handle Methods ----------------
  // Endpoint: Delete Message
  const handleDeleteMessage = async () => {
    try {
      await api.delete('/contact-form/message', {
        params: {
          email: email,
          subject: subject
        }
      });
    } catch (error) {
      console.error('Error deleting message:', error);
    }
    // 
  }

  // ---------------- useEffect() ----------------

  
  // ---------------- Rendering UI ----------------
  return (
    <div className="message-card">
      <div className="message-card-header">
        <strong>{firstName} {lastName}</strong> • <span className="email">{email}</span>
      </div>

      <div className="message-card-subject">
        <strong>Subject:</strong> {subject}
      </div>

      <div className="message-card-tags">
        <strong>Tags:</strong> {tags.join(', ')}
      </div>

      <div className="message-card-body">
        <strong>Message:</strong>
        <p>{body}</p>
      </div>

      
      <button className="delete-button" onClick={handleDeleteMessage}>
        Delete
      </button>


    </div>
  )
}

export default MessageCard

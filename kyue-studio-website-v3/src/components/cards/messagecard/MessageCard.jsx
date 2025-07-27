import React from 'react'
import './MessageCard.css'
import api from '../../../api/fastapi';

// callback prop fetchMessages(formerly: onDelete) allows it to tell parent (MessageCardColumnStack) to re-fetch or update state once a message is deleted
const MessageCard = ({message, fetchMessages}) => {
  // ---------------- State variables ----------------
  // spreading the message object (could've also passed in {...message} but i prefer to do the dirty work at lower levels)
  const { firstName, lastName, email, subject, tags, message: body } = message;

  // ---------------- API Calls ----------------

  // ---------------- Form/Button/Interactions Logic Handle Methods ----------------
  // Endpoint: Delete Message
  const handleDeleteMessage = async () => {
    try {
      // hit delete endpoint to delete message from db
      const response = await api.delete('/contact-form/message', {
        params: {
          email: email,
          subject: subject
        }
      });
      console.log('Deleted:', response.data);

      // tell parent to refresh and update state since database has changed
      fetchMessages();
      // if (onDelete) {
      //   onDelete();
      // }
    } catch (error) {
      console.error('Error deleting message:', error);
      alert('Failed to delete message');
    }
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

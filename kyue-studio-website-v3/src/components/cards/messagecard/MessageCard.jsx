import React from 'react'
import './MessageCard.css'

const MessageCard = ({message}) => {
  const { firstName, lastName, email, subject, tags, message: body } = message;

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
    </div>
  )
}

export default MessageCard

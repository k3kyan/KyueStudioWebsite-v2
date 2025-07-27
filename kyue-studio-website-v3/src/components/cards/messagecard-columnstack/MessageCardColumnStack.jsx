import React from 'react'
import './MessageCardColumnStack.css'
import MessageCard from '../messagecard/MessageCard'

const MessageCardColumnStack = ({messageList}) => {
  return (
    <section className="blog-grid-container">
      {messageList.map((message, index) => (
        <MessageCard key={index} message={message} />
      ))}
    </section>
  )
}

export default MessageCardColumnStack

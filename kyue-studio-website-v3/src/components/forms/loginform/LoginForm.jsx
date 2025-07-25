import React from 'react'
import { useState } from 'react';
import './LoginForm.css'

const LoginForm = () => {

    // TODO: set up form backend submission functionality. connect to backend probably. service functions...?
    
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [loginMessage, setLoginMessage] = React.useState('');

    // const handleSubmit = async (e) => ????
    const handleSubmit = (e) => {
        e.preventDefault(); //TODO: expl
        setLoginMessage('Logging in...');
        // TODO: login success/fail logic 
    }

    


  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: '300px', margin: 'auto' }}>
        <h3>Login Form</h3>

        <label>
        Username
        <br/>
        <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
        />
        </label>

        <label>
        Password 
        <br/>
        <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
        />
        </label>

        <button type="submit">Log In</button>

        {loginMessage && <p>{loginMessage}</p>}
    </form>
  )
}

export default LoginForm

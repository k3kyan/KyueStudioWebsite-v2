import React, { useEffect, useState } from 'react';
// import { useState } from 'react';
import './LoginForm.css'
// from '../../../../../../kyue-studio-backend/routes' #no i dont need to do this import bc its already in the "api" import. You should never need to touch backend like that from the front end. axios's api object will handle all of that.
import api from '../../../api/fastapi';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../../../../GlobalContext'; // correct route for import?

const LoginForm = () => {

    // TODO: set up form backend submission functionality. connect to backend probably. service functions...?
    
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loginMessage, setLoginMessage] = useState('');
    const [redirectToHome, setRedirectToHome] = useState(false); //redirect to homepage if successful login
    
    
    // Can Delete: Implemented in GlobalContext.js: const [isLoggedIn, setIsLoggedIn] = useState(() => !!localStorage.getItem('token')); // Logout functionality // state variable to track login status:
    const { isLoggedIn, login, logout } = useAuth(); // getting context from GlobalContext.js

    // want async/await so that it finishes checking login and accessing api before continuing code. Otherwise, may have errors and might access things wrong or something
    const handleSignIn = async (e) => {
        e.preventDefault(); // EXPLAIN: we dont want the default functionality of the form to happen. we want to do our own thing.
        setLoginMessage('Logging in...');
        

        try {
            // TODO: login success/fail logic 
            const formData = new FormData();
            formData.append('username', username); // from username state variable
            formData.append('password', password); // from password state variable

            // DELETE: useless i think , from Catalin Stefan's tutorial
            // const requestOptions = {
            //     method: 'POST',
            //     body: formData,
            // };

            const response = await api.post('/token', formData);
            if (response.status === 200) {
                login(response.data.access_token);  // call the context login function // saves token to localStorage
                // isLoggedIn(true); // DELETE: don't need this bc this is handled inside the login() method in GlobalContext useAuth hook
                setLoginMessage('Login successful!');
                setRedirectToHome(true);
                //DELETE: setIsLoggedIn(true); //logout functionality
                return response.json();
            }
            // throw response; // needed ???
        } catch (error) {
            console.error('Error logging in', error);
            setLoginMessage('Login failed. Please try again.');
        }
    };

    if (redirectToHome) {
        return <Navigate to="/" replace />; // TODO: RESEARCH: ?? what does the replace do ??
    }

    


    // logout function
    const handleLogout = () => {
        logout(); // call the context logout function
        setLoginMessage('Logged out');
    };





    // UI component
  return (
    <form onSubmit={handleSignIn} style={{ maxWidth: '300px', margin: 'auto' }}>
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


        {/* // logout functionality + if-true Conditional Rendering if you're logged in or not */}
        {isLoggedIn && (
            <div style={{ marginTop: '1rem' }}>
                <button onClick={handleLogout}>Log Out</button>
            </div>
        )}
        {/* if-else Conditional Rendering */}
        {isLoggedIn ? <div>Logged in!</div> : <div>not logged in</div>}

    </form>
  )
}

export default LoginForm

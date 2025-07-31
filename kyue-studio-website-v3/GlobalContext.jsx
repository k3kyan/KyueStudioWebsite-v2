// To globally conditionally render thru React app
// use React Context to store and manage a global isLoggedIn state (instead of duplicating useState in each component like in your current LoginForm.jsx).
// TODO: why did i put this file all the way out here instead of at the same level as App.jsx ??

import { createContext, useContext, useState, useEffect } from 'react';

// Authorization Context


// context
const AuthorizationContext = createContext();

// provider component
export const AuthorizationProvider = ({ children }) => {
    const [isLoggedIn, setIsLoggedIn] = useState(() => !!localStorage.getItem('token'));
    const baseURL = "https://v6ln2nysret2s3swtlhrf6m5gq0wcbzn.lambda-url.us-east-2.on.aws"

    const login = (token) => {
        localStorage.setItem('token', token);
        setIsLoggedIn(true);
    };

    const logout = () => {
        localStorage.removeItem('token');
        setIsLoggedIn(false);
    };

    // Allows Any component wrapped in <AuthorizationProvider> will be passed in as children
    return (
        // NOTE: AuthorizationContext is used bc its the =createContext() React context object created above, and it has the ".Provider" property
        // Any child components can access the value via the context (aka this file, i think)
        // AuthorizationContext.Provider is a React Context Provider — it shares values (isLoggedIn, login, logout) with any component wrapped inside of it (like the {children})
        // aka: isLoggedIn, login, and logout available to everything inside this component tree
        <AuthorizationContext.Provider value={{ isLoggedIn, login, logout }}>
            {children}
        </AuthorizationContext.Provider>
    );

};


// Custom hook to use context (named useAuth())
export const useAuth = () => useContext(AuthorizationContext);
// useAuth() conveniently replaces stuff like
// const { isLoggedIn } = useContext(AuthContext);
// with 
// import { useAuth } from '../contexts/AuthContext';
// const { isLoggedIn } = useAuth();
// or so, etc
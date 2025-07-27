import React, { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../../../../GlobalContext';
import api from '../../../api/fastapi';

// TODO: reference contact form jsx

const AdminCreateBlogPost = () => {
    // ---------------- State variables ----------------
    const { isLoggedIn } = useAuth();

    // ---------------- !!!!!!THIS PAGE IS A PROTECTED ROUTE!!!!!! ----------------
    // Redirect to homepage if not logged in 
    if (!isLoggedIn) {
        return <Navigate to="/" />;
    }


    return (
        <div>
            <h2>Admin Create Blog Post</h2>
        
        </div>
    )
}

export default AdminCreateBlogPost

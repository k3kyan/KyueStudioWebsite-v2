import React, { useEffect, useState } from 'react';
import LogOutButton from '../../../components/forms/loginform/LogOutButton'
import api from '../../../api/fastapi';
import { useAuth } from '../../../../GlobalContext';
import { Navigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

const AdminDashboard = () => {
    // ---------------- State variables ----------------
    const { isLoggedIn } = useAuth();
    
    // ---------------- !!!!!!THIS PAGE IS A PROTECTED ROUTE!!!!!! ----------------
    // Redirect to homepage if not logged in 
    // TODO: RESEARCH: DOES THIS RISK RENDERING STUFF ACCIDENTALLY FOR EVEN A SECOND BEFORE IT FULL LOADS ????? would be a bad data breach
    if (!isLoggedIn) {
        return <Navigate to="/" />;
    }

    // ---------------- API Calls ----------------

    // ---------------- Form/Button/Interactions Logic Handle Methods ----------------

    // ---------------- useEffect() ----------------
    
    // ---------------- Rendering UI ----------------
    return (
    <div>
        <h3>AdminDashboard</h3>
        <div>
            <h4>TEMP: Links to Admin stuff. Put into a sidebar later (will persist over whole Admin page)</h4>
                <nav style={{ display: 'flex', gap: '1rem' }}>
                    <Link to="/admin/dashboard">Dashboard</Link>
                    <Link to="/admin/messages">Messages</Link>
                    <Link to="/admin/orders">Orders</Link>
                    <Link to="/admin/create-blog-post">Create Blog Post</Link>
                    <Link to="/admin/create-art-post">Create Art Post</Link>
                    {/* <LogOutButton /> */} {/* TODO: fix LogOutButton component. doesn't work. */}
                </nav>
        </div>

        {isLoggedIn && ( 
            <div>
                Logged In
            </div>
        )}
    </div>
  )
}

export default AdminDashboard

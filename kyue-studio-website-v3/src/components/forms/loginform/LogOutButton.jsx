import { Navigate } from 'react-router-dom';
import { useAuth } from '../../../../GlobalContext';
import React, { useEffect, useState } from 'react';
import api from '../../../api/fastapi';

// TODO: this doesnt work, idk im too tired for this and its not part of the branch task

const LogOutButton = () => {
    
    const handleLogout = () => {
        logout(); // call the context logout function
    };


  return (
    <div>
        <button onClick={handleLogout}>Log Out</button>
    </div>
  )
}

export default LogOutButton

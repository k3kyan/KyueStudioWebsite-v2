import React, { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../../../../GlobalContext';
import api from '../../../api/fastapi';

const AdminCreateArtPost = () => {
  // ---------------- State variables ----------------
  const { isLoggedIn } = useAuth();

  // ---------------- !!!!!!THIS PAGE IS A PROTECTED ROUTE!!!!!! ----------------
  // Redirect to homepage if not logged in 
  if (!isLoggedIn) {
      return <Navigate to="/" />;
  }
  
  return (
    <div>
      TODO: upload art, + caption + title + date + time + tags
    </div>
  )
}

export default AdminCreateArtPost

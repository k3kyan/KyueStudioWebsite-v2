import React, { useEffect, useState } from 'react';
// import MessageCardColumnStack from '../../../components/cards/messagecard-columnstack/MessageCardColumnStack';
// import api from '../../../api/fastapi';
// import { useAuth } from '../../../../GlobalContext';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../../../../GlobalContext';
import api from '../../../api/fastapi';

const AdminMessageBoard = () => {
  // ---------------- State variables ----------------
  const { isLoggedIn } = useAuth();

  // ---------------- !!!!!!THIS PAGE IS A PROTECTED ROUTE!!!!!! ----------------
  // Redirect to homepage if not logged in 
  if (!isLoggedIn) {
      return <Navigate to="/" />;
  }

  
  return (
    <div>
      Message Board
    </div>
  )
}

export default AdminMessageBoard

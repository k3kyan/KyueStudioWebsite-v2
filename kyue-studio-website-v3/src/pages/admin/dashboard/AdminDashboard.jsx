import React, { useEffect, useState } from 'react';
import LogOutButton from '../../../components/forms/loginform/LogOutButton'
import api from '../../../api/fastapi';
import { useAuth } from '../../../../GlobalContext';
import { Navigate } from 'react-router-dom';
import MessageCard from '../../../components/cards/messagecard/MessageCard';

const AdminDashboard = () => {
    // ---------------- State variables ----------------
    const [messageList, setMessageList] = useState([]);
    const { isLoggedIn } = useAuth();

    const TEMP_MESSAGE = {
      "firstName": "Grr",
      "lastName": "Growl",
      "email": "growl@grr.com",
      "subject": "grr",
      "tags": [
        "Collaboration"
      ],
      "message": "growl"
    }
    

    // ---------------- !!!!!!THIS PAGE IS A PROTECTED ROUTE!!!!!! ----------------
    // Redirect to homepage if not logged in 
    // TODO: RESEARCH: DOES THIS RISK RENDERING STUFF ACCIDENTALLY FOR EVEN A SECOND BEFORE IT FULL LOADS ????? would be a bad data breach
    if (!isLoggedIn) {
        return <Navigate to="/" />;
    }

    // ---------------- API Calls ----------------
    // TODO: LATER: will separate message list to put into their own components // probably will fetch the data and then create a list of components to populate the data? (see the blog posts, i literally have a json dict variable that passes stuff in on the same page, so i think yeah thats how its done)
    // Fetch messages from backend to list 
    const fetchMessages = async () => {
        try {
            const response = await api.get('/contact-form/messages');
            setMessageList(response.data.messageList);
            
            // {/* Good for debugging and seeing what the structure of each msg looks like*/}
            // console.log(messageList); 
        } catch (error) {
            console.error("Error fetching message list", error);
            // console.log(messageList); 
        }
    };

    // TODO: add delete endpoint ?? (this is reference) (this will be called in handleSubmit instead of doing it inside handleSubmit this time, unlike ContactForm.jsx)
    // const addFruit = async (fruitName) => {
    //     try {
    //     await api.post('/fruits', 
    //         { name: fruitName },
    //         // { headers: { Authorization: `Bearer ${token}` } } // dont need this line since we set up axios to include the token in every request
    //     );
    //     fetchFruits();  // Refresh the list after adding a fruit
    //     } catch (error) {
    //     console.error("Error adding fruit", error);
    //     }
    // };

    // ---------------- Form/Button/Interactions Logic Handle Methods ----------------

    // ---------------- useEffect() ----------------
    useEffect(() => {
        fetchMessages();
    }, []); // will add deleteMessage to the []); triggers for refreshing later

    // ---------------- Rendering UI ----------------
    return (
    <div>
        AdminDashboard
        TODO: render only if logged in // otherwise, redirect/navigate to homepage bc they shouldn't be accessing this URL
        {/* TODO: fix LogOutButton component. doesn't work. */}
        {/* <LogOutButton /> */}

        {/* TODO: message board (will later be separated into components somehow, so i can display it into a list and separate delete functions) */}
        {/* mmap over the array and render UI elements for each message*/}
        {/* {messageList.map((msg, index) => (
            <div key={index} className="message">
                <p><strong>Name:</strong> {msg.firstName} {msg.lastName}</p>
                <p><strong>Email:</strong> {msg.email}</p>
                <p><strong>Subject:</strong> {msg.subject}</p>
                <p><strong>Tags:</strong> {msg.tags.join(', ')}</p>
                <p><strong>Message:</strong> {msg.message}</p>
                <hr />
            </div>
        ))} */}

        sdlkfj
        <MessageCard message={TEMP_MESSAGE} />



        {isLoggedIn && ( 
            <div>
                Logged In
            </div>
        )}

        {/* TODO: IMPORTANT: PROTECTED: redirect to homepage if not logged in / authorized to view this page */}

    </div>
  )
}

export default AdminDashboard

import React, { useEffect, useState } from 'react';
import LogOutButton from '../../../components/forms/loginform/LogOutButton'
import api from '../../../api/fastapi';
import { useAuth } from '../../../../GlobalContext';
import { Navigate } from 'react-router-dom';
import MessageCard from '../../../components/cards/messagecard/MessageCard';
import MessageCardColumnStack from '../../../components/cards/messagecard-columnstack/MessageCardColumnStack';
import { Link } from 'react-router-dom';

import AddFruitForm from '../../../components/forms/TEMP_FRUITS_API_FORM/TempFruitsAPIForm';
import FruitList from '../../../components/forms/TEMP_FRUITS_API_FORM/TempFruitsAPIShowList';

const AdminDashboard = () => {
    // ---------------- State variables ----------------
    const [messageList, setMessageList] = useState([]);
    const { isLoggedIn } = useAuth();

    // const TEMP_message = {
    //   "firstName": "Grr",
    //   "lastName": "Growl",
    //   "email": "growl@grr.com",
    //   "subject": "grr",
    //   "tags": [
    //     "Collaboration"
    //   ],
    //   "message": "growl"
    // }

    // const TEMP_messageList = [
    //     {
    //     "firstName": "Bob",
    //     "lastName": "Microsoft",
    //     "email": "bob@microsoft.com",
    //     "subject": "Checkout is broken",
    //     "tags": [
    //         "Feedback",
    //         "Bug Report"
    //     ],
    //     "message": "I can't checkout and pay for my order."
    //     },
    //     {
    //     "firstName": "meow",
    //     "lastName": "meow",
    //     "email": "meow@grr.com",
    //     "subject": "meow",
    //     "tags": [
    //         "Collaboration"
    //     ],
    //     "message": "meow"
    //     }
    // ]
    

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
            console.log(response.data.messageList);
            // console.log(response);
            setMessageList(response.data);
            
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
    }, [messageList]); // will add deleteMessage to the []); triggers for refreshing later // maybe just add messageList to the []); because its value will change when the delete endpoint is called within the MessageCard.jsx ??

    // ---------------- Rendering UI ----------------
    return (
    <div>
        AdminDashboard
        TODO: render only if logged in // otherwise, redirect/navigate to homepage bc they shouldn't be accessing this URL
        {/* TODO: fix LogOutButton component. doesn't work. */}
        {/* <LogOutButton /> */}

        <div>
            <h2>Links to Admin stuff. Put into a sidebar later (will persist over whole Admin page)</h2>
                <nav style={{ display: 'flex', gap: '1rem' }}>
                    <Link to="/admin/dashboard">Dashboard</Link>
                    <Link to="/admin/messages">Messages</Link>
                    <Link to="/admin/orders">Orders</Link>
                    <Link to="/admin/create-blog-post">Create Blog Post</Link>
                    <Link to="/admin/create-art-post">Create Art Post</Link>
                </nav>
        </div>




        {/* <h1>SampleData: Single Message Components</h1>
        <div class = "messages">
            <MessageCard message={TEMP_message} />
        </div>

        <h1>SampleData: Messages List</h1>
        <div class = "messages">
            <MessageCardColumnStack messageList={TEMP_messageList} />
        </div> */}

        
        <h1>BackendJsonFileData: Messages List</h1>
        <div class = "messages">
            {/* <pre>{JSON.stringify(messageList, null, 2)}</pre>
            <p>Total messages: {messageList.length}</p> */}
            <MessageCardColumnStack messageList={messageList} fetchMessages={fetchMessages} />
        </div>

        {isLoggedIn && ( 
            <div>
                Logged In
            </div>
        )}

        {/* TODO: IMPORTANT: PROTECTED: redirect to homepage if not logged in / authorized to view this page */}



        {/* NOT WORKING ???? idk but i dont need this so i wont fix it now, since Contact Form is still sending data to backend successfully, but idk why its not working i didnt think i changed anything sdfkljsflksd */}
        {/* the Fruit stuff is here for fun and for testing lol, my first working crud implementation! yayy */}
        {/* TEMP: Just to show that backend is working. DELETE LATER!! */}
        {/* <TempFruitsAPIForm />
        <TempFruitsAPIShowList />  */}
        {/* <AddFruitForm /> (needs parameter so thats why it didnt render correctly)*/} 
        {/* <FruitList />  */}

      
    </div>
  )
}

export default AdminDashboard

import React, { useEffect, useState } from 'react';
// import AddFruitForm from './AddFruitForm';
import AddFruitForm from './TempFruitsAPIForm';
import api from '../../../api/fastapi';  // IMPORTANT: THIS IS HOW WE CONNECT THE FRONTEND TO THE BACKEND !!!!! WOWOW YAYAYA 
import { useAuth } from '../../../../GlobalContext';

const FruitList = () => {
  const [fruits, setFruits] = useState([]);
  const { isLoggedIn } = useAuth(); // getting context from GlobalContext.js, tells us whether we are logged in or not

  // IMPORTANT: CALLS TO ENDPOINT FOR GET /FRUITS (CALLS TO BACKEND TO GET LIST OF FRUITS
  const fetchFruits = async () => {
    try {
      const response = await api.get('/fruits');
      setFruits(response.data.fruits);
    } catch (error) {
      console.error("Error fetching fruits", error);
    }
  };

  // IMPORTANT: ENDPOINT TO POST /FRUITS (ADDS FRUIT TO DATABASE IN BACKEND)
  // IMPORTANT: since this is a protect route, for the api.post parameters, we need to add the token!!! (which i actually already did in the fastapi.js or whatever file "api" is declared in)
  const addFruit = async (fruitName) => {
    try {
      await api.post('/fruits', 
        { name: fruitName },
        // { headers: { Authorization: `Bearer ${token}` } } // dont need this line since we set up axios to include the token in every request
      );
      fetchFruits();  // Refresh the list after adding a fruit
    } catch (error) {
      console.error("Error adding fruit", error);
    }
  };

  // TODO: practice implementing delete fruit
  // TODO: practice implementing edit fruit ?? kinda hard tho idk, would have to create a whole new form probably tbh. 


  // RESEARCH: i guess useEffect() runs when the component first is rendered on screen..?
  useEffect(() => {
    fetchFruits();
  }, []);
  // NOTE: if you put something inside the []'s, it will rerun whenever the value changes
  // Ex: useEffect(() => { fetchFruits(); }, [fruitsArr]); 
  //     this will rerun whenever fruitsArr array changes


  return (
    <div>
      <h2>Fruits List</h2>
      <ul>
        {fruits.map((fruit, index) => (
          <li key={index}>{fruit.name}</li>
        ))}
      </ul>
      {isLoggedIn && ( // REPLACE WITH VARIABLE BOOL ON WHETHER UR LOGGED IN OR NOT
        <AddFruitForm addFruit={addFruit} />
      )}
    </div>
  );
};

export default FruitList;
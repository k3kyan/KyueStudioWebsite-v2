import React, { useEffect, useState } from 'react';
// import AddFruitForm from './AddFruitForm';
import AddFruitForm from './TempFruitsAPIForm';
import api from '../../../api/fastapi';  // IMPORTANT: THIS IS HOW WE CONNECT THE FRONTEND TO THE BACKEND !!!!! WOWOW YAYAYA 

const FruitList = () => {
  const [fruits, setFruits] = useState([]);

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
  const addFruit = async (fruitName) => {
    try {
      await api.post('/fruits', { name: fruitName });
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
      <AddFruitForm addFruit={addFruit} />
    </div>
  );
};

export default FruitList;
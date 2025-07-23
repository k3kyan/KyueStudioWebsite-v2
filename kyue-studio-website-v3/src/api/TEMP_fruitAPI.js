// TEMP: fruit API backend calls
// This file is where we will be putting our Axios definition for calling the API

import axios from 'axios';

// create an instance of axios with the base URL
// this will be the only place we need the url!! good practice
const api = axios.create({
    // how do i call my .env.local API_BASE_URL ??
    baseURL: "http://localhost:8000" // the url for fastapi backend server (from uvicorn)
})

// export axios instance
export default api;
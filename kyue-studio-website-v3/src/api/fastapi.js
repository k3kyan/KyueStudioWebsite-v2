// TEMP: fruit API backend calls
// This file is where we will be putting our Axios definition for calling the API

import axios from 'axios';
// import baseURLGlobal from '../../GlobalContext';

// create an instance of axios with the base URL
// this will be the only place we need the url!! good practice
const api = axios.create({
    // how do i call my .env.local API_BASE_URL ??
    baseURL: "https://v6ln2nysret2s3swtlhrf6m5gq0wcbzn.lambda-url.us-east-2.on.aws/"
    // baseURL: "https://hioroxjfpm52qt6flna72nv2gm0ycjuy.lambda-url.us-east-2.on.aws/" //"http://localhost:8000" // the url for fastapi backend server (from uvicorn)
    // baseURL: baseURLGlobal
})
// TODO: update the other endpoints too like in BlogCard, tho that should be the only other place the https is called....



// TODO: RESEARCH: CHECK: Interceptor to attach token to every request (if it exists)
// aka inserts authorization token into every api call so i dont need to insert it into every each header every time i make a call (bloated, duplicate code)
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);


// // TODO: CHECK: auto-log out user if token is expired
// api.interceptors.response.use(
//   response => response,
//   error => {
//     if (error.response && error.response.status === 401) {
//       // auto logout or clear token
//       localStorage.removeItem('token');
//       window.location.href = '/login'; // or use navigate()
//     }
//     return Promise.reject(error);
//   }
// );


// // TODO: this TEMP example is just from Tech w Tim Github, for logging in ?? idk. The login endpoints? 
// const loginUser = async (username, password) => {
// }






// export axios instance
export default api;

// Actually, maybe i'll be doing this with python and NOT js



// TODO
// make sure ur writing this project with SEPARATE MODULARITY 
// to code project locally, and have it ready to easily replace with AWS services and calls
// without touching much of the React components UI code
// since the React components should only have code focusing on UI !!!!!!! 
    // (or at least, there should be very minimal business logic code in the jsx react component if it can be helped)
// the business logic should be in these js files. services. 

// purpose of this file: login/logout/check stored token
// swappable logic: easily redirect to SecretsManager(backed Lambda?)







// export async function login(username, password)
// need to use api ...? idk 
// localStorage.setItem('jwt', jwt) ?????? 
// api.post('/login', { username, password }) ?????????
// body: JSON.stringify({ username, password })
// for login(), need to make sure /login points to the API gateway route 


// export function logout() {
//     localStorage.removeItem('jwt')
// }

// export function isLoggedIn() {
//     return localStorage.getItem('jwt') !== null
// }
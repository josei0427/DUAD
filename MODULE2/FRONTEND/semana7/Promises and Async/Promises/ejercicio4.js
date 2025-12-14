//Ejercicio 1 de Async/Await con Promises
// function getUser() {
//     return fetch("https://reqres.in/api/users/2", {
//             headers: {
//                 'x-api-key': 'reqres_2c9ba126d4634626b05ec07fff7e7701'
//             }
//         })
//         .then(res => res.json());
//     }

// getUser()
// .then(result =>{
//     console.log(result);
// })
// .catch(err => console.error("Error:", err));


//Ejercicio 2 de Async/Await con Promises
function getUser() {
    return fetch("https://reqres.in/api/users/23", {
        headers: { 'x-api-key': 'reqres_2c9ba126d4634626b05ec07fff7e7701' }
    })
    .then(res => {
        if (res.status === 404) {
            return {error: "User not found"};
        }
        return res.json();
    });
}
getUser()
.then(result =>{
    console.log(result); })
.catch(err => console.error("Error:", err));
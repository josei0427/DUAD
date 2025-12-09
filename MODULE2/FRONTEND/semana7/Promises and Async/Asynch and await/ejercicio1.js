async function fetchData() {
    try{
        const response = await fetch("https://reqres.in/api/users/2", {
            headers: {
                'x-api-key': 'reqres_2c9ba126d4634626b05ec07fff7e7701'
            }
        });
        const myData = await response.json();
        console.log(myData)
    }
    catch (error){
        console.log("There was in issue. Please try later.");
    }
}

fetchData();
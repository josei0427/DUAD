async function fetchData() {
    try {
        const response = await fetch("https://reqres.in/api/users/23", {
            headers: {
                'x-api-key': 'reqres_2c9ba126d4634626b05ec07fff7e7701'
            }
        });
        const myData = await response.json();
        if (response.status === 404) {
            console.log("User not found.");
            return;
        }
        console.log(myData);
    } catch (error) {
        console.log("Error:", error.message);
    }
}

fetchData();
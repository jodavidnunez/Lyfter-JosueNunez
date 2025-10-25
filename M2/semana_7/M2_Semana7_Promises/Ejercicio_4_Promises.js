/*async function getUserData(userId) {
    console.log("-I-: Sending request...");
    try {
        const response = await fetch(`https://reqres.in/api/users/${userId}`, {headers:{"x-api-key":"reqres-free-v1"}});
        const user = await response.json();
        return user.data; 
    } catch (error) {
        console.log(`-E-: The following error has been found: ${error}`);
    }
}
const userId = 2;
getUserVar = getUserData(userId);
getUserVar.then(user_data => {
    console.log("-I-: User data:\n", user_data); 
});*/

// Ejercicio #1 Replique el codigo de arriba usando solo .then, .catch y .finally
const userId2 = 2;
const user2= fetch(`https://reqres.in/api/users/${userId2}`, {headers:{"x-api-key":"reqres-free-v1"}});
user2
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status} ${response.statusText}`);
        }
        return response.json();
    })
    .then(response_data => {
        console.log(response_data);
    })
    .catch(error => {
        console.log(`ERROR: ${error.message}`);
    })
    .finally(() => {
        console.log("INFO: Exercise #1 - Promise completed.\n\n");

        // Ejercicio #2: Forzar el error y reportarlo adecuadamente
        const userId3 = 23;
        const user3 = fetch(`https://reqres.in/api/users/${userId3}`, { headers: { "x-api-key": "reqres-free-v1" } });
        user3
            .then(response => {
                if (!response.ok) {
                    throw response;
                }
                return response.json();
            })
            .then(response_data => {
                console.log(response_data);
            })
            .catch(error => {
                if (error && typeof error.status === 'number') {
                    const status = error.status;
                    let errorMessage;
                    switch (status) {
                        case 404:
                            errorMessage = `User with ID ${userId3} not found`;
                            break;
                        case 400:
                            errorMessage = `Invalid user ID ${userId3}`;
                            break;
                        case 500:
                            errorMessage = `Server error`;
                            break;
                        default:
                            errorMessage = `HTTP failed with status: ${status}`;
                    }
                    console.log(`ERROR: ${errorMessage} (status ${status})`);
                } else {
                    console.log(`ERROR: ${error && error.message ? error.message : String(error)}`);
                }
            })
            .finally(() => {
                console.log("INFO: Exercise #2 - Promise completed.");
            });
    });

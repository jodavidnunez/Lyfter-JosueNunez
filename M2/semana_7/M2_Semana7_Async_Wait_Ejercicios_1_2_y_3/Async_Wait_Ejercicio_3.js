async function getUser(userId) {
    console.log("-I-: Sending request...");
    try {
        const response = await fetch(`https://reqres.in/api/users/${userId}`, {headers:{"x-api-key":"reqres-free-v1"}});
        console.log(JSON.stringify(response));
        if (!response.ok) {
            switch (response.status) {
                case 404:
                    errorMessage = `User with ID ${userId} not found`
                    break
                case 404:
                    errorMessage = `User with ID ${userId} not found`
                    break
                case 404:
                    errorMessage = `User with ID ${userId} not found`
                    break
                default:
                    errorMessage = `HTTP failed with status: ${userResult.status}`
            }
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const user = await response.json();
        return user.data;
    } catch (error) {
        console.log(`-E-: ${error}`);
        return { error: error.message };
    }
}

document.getElementById('fetch-user-btn').addEventListener('click', async () => {
    const userId = document.getElementById('user-id-input').value;
    const output = document.getElementById('output-container');
    const button = document.getElementById('fetch-user-btn');
    if (!userId) {
        output.innerHTML = '<p style="color: red;">Please enter a UserID</p>'
        return
    }

    button.disabled = true
    button.textContent = 'Loading ...'
    output.innerHTML = '<p>Fetching user data ...</p>' 

    try {
        const userResult = await getUser(userId);
        if (userResult.error) {
            output.innerHTML = `
                <h3>Error for User ID ${userId}:</h3>
                <p style="color:red;">${userResult.error} - ${errorMessage}</p>
            `;
        } else {
            output.innerHTML = `
                <h3>Result for User ID ${userId}:</h3>
                <pre>${JSON.stringify(userResult, null, 2)}</pre>
            `;
        }
    } finally {
        button.disabled = false
        button.textContent = 'Get user'
    }
});
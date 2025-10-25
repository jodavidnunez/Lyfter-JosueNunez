async function getUser(userId) {
    console.log("-I-: Sending request...");
    try {
        const response = await fetch(`https://reqres.in/api/users/${userId}`, {headers:{"x-api-key":"reqres-free-v1"}});
        if (!response.ok) {
            throw {isHttpError: true, status: response.status, userId};
        }
        const user = await response.json();
        return user.data;
    } catch (error) {
        let errorMessage;
        let status;
        if (error && error.isHttpError) {
            status = error.status;
            switch (error.status) {
                case 404:
                    errorMessage = `User with ID ${error.userId} not found`;
                    break;
                case 400:
                    errorMessage = `Invalid user ID ${error.userId}`;
                    break;
                case 500:
                    errorMessage = `Server error`;
                    break;
                default:
                    errorMessage = `HTTP failed with status: ${error.status}`;
            }
        } else {
            errorMessage = error && error.message ? error.message : "Network error or unknown error occurred";
        }
        console.log(`-E-: ${errorMessage}${status ? ` (status ${status})` : ''}`);
        const errToThrow = new Error(errorMessage);
        if (status) errToThrow.status = status;
        throw errToThrow;
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
                <p style="color:red;">${userResult.error}</p>
            `;
        } else {
            output.innerHTML = `
                <h3>Result for User ID ${userId}:</h3>
                <pre>${JSON.stringify(userResult, null, 2)}</pre>
            `;
        }
    } catch (err) {
        const message = err?.message ?? String(err);
        const status = err?.status;
        output.innerHTML = `
            <h3>Error for User ID ${userId}:</h3>
            <p style="color:red;">${message}${status ? ` (status ${status})` : ''}</p>
        `;
        console.error("-E-: Error found in UI handler:", err);
    } finally {
        button.disabled = false
        button.textContent = 'Get user'
    }
});
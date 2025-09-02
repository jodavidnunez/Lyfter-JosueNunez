async function getUser(userId) {
    console.log("-I-: Sending request...");
    try {
        const response = await fetch(`https://reqres.in/api/users/${userId}`);
        const user = await response.json();
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        } else { 
            return user.data;
        }
    } catch (error) {
        console.log(`-E-: ${error}`);
        return { error: error.message };
    }
}

document.getElementById('fetch-user-btn').addEventListener('click', async () => {
    const userId = document.getElementById('user-id-input').value;
    const output = document.getElementById('output-container');
    const userResult = await getUser(userId);
    output.innerHTML = `
        <h3>Result for User ID ${userId}:</h3>
        <pre>${JSON.stringify(userResult, null, 2)}</pre>
    `;
});
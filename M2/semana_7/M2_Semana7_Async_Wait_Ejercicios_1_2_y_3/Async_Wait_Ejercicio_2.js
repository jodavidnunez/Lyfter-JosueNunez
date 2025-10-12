async function getUser(userId, badUserId = "") {
    console.log("-I-: Sending request...");
    try {
        const response = await fetch(`https://reqres.in/api/users/${userId}${badUserId}`, {headers:{"x-api-key":"reqres-free-v1"}});
        const user = await response.json();
        if (!response.ok) {
            throw new Error(`User '${userId}${badUserId}' is not found.`);
        } else { 
            return user.data;
        }
    } catch (error) {
        console.log(`-E-: ${error}`);
    }
}
const goodUserId = 2;
const badUserId = 3;
user_data = getUser(goodUserId,badUserId);
user_data.then(user_data => {
    console.log("-I-: User data:\n", user_data); 
});
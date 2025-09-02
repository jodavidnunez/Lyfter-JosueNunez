async function getUserData(userId) {
    console.log("-I-: Sending request...");
    try {
        const response = await fetch(`https://reqres.in/api/users/${userId}`);
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
});
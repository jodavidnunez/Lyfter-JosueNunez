async function getPokemon(pokemonId) {
    console.log("-I-: Sending request...");
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}`);
        console.log(JSON.stringify(response));
        if (!response.ok) {
            switch (response.status) {
                case 404:
                    errorMessage = `User with ID ${pokemonId} not found`
                    break
                case 404:
                    errorMessage = `User with ID ${pokemonId} not found`
                    break
                case 404:
                    errorMessage = `User with ID ${pokemonId} not found`
                    break
                default:
                    errorMessage = `HTTP failed with status: ${response.status}`
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
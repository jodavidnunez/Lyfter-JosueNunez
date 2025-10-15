// 2. Realice el mismo ejercicio anterior utilizando la función 
// Promse.any() para mostrar el nombre del primer pokemón que esté 
// contenido en la primera promesa que se resuelva.

async function getPokemon(pokemonId) {
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}/`);
        if (!response.ok) {
            let errorMessage;
            switch (response.status) {
                case 404:
                    errorMessage = `Pokemon with ID ${pokemonId} not found`;
                    break;
                case 400:
                    errorMessage = `Invalid Pokemon ID ${pokemonId}`
                    break
                case 500:
                    errorMessage = `Server error`
                    break
                default:
                    errorMessage = `HTTP failed with status: ${response.status}`;
            }
            throw new Error(errorMessage);
        }
        const pokemon = await response.json();
        return pokemon; 
    } catch (error) {
        console.log(`-E-: ${error}`);
        return { error: error.message };
    }
}

Promise.any([
    getPokemon('dragonite'),
    getPokemon('lapras'),
    getPokemon('arcanine')
])

.then(first_pokemon => {
    setTimeout(() => {
        console.log("\nExercise #2:")
        console.log(first_pokemon.name);
    }, 1000);
})

.catch(err => {
    console.error("Error:", err)
})


// 1. Utilice el API https://pokeapi.co/api/v2/pokemon/:ID para solicitar 
// 3 distintos pokemónes. Utilice la función Promise.all() para mostrar 
// en pantalla el nombre de los tres pokemónes al mismo tiempo, hasta que 
// todas las promesas se resuelvan.

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

Promise.all([
    getPokemon('snorlax'),
    getPokemon('ivysaur'),
    getPokemon('gengar')
])

.then(([poke1, poke2, poke3]) => {
    console.log("Exercise #1:")
    console.log(poke1.name)
    console.log(poke2.name)
    console.log(poke3.name)
})

.catch(err => {
    console.error("Error:", err)
})

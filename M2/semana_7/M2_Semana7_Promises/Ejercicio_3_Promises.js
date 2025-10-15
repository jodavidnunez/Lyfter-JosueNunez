// 3. Cree cuatro promesas, donde cada una resuelve a una 
// de las palabras de la lista ["very", "dogs", "cute", "are"] 
// respectivamente, en el mismo orden. Utilice la combinación 
// de la función setTimeout y Promse.all() para obtener la salida 
// "Dogs are very cute" , sin modificar el orden de la lista 
// manualmente o mediante un sort.

const input_words = ["very", "dogs", "cute", "are"]
const delays = [3000, 1000, 4000, 2000]

function delayedWord(word, delay) {
    return new Promise(resolve => {
        setTimeout(() => resolve(word), delay)
    });
}

const promises = input_words.map((word, i) => delayedWord(word, delays[i]));
const output = [];

promises.forEach(promise => {
    promise.then(word => {
        output.push(word);
        if (output.length === input_words.length) {
            console.log("\nExercise #3:")
            console.log(
                output[0],
                output[1],
                output[2],
                output[3]
            );
        }
    });
});


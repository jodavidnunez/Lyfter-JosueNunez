/*1. Cree una función que reciba tres parámetros: un número y dos funciones de callback.
    1. Si el número es par, se debe ejecutar el primer callback.
        1. Este debe mostrar “The number is even!”.
    2. Si el número es impar, se debe ejecutar el segundo.
        1. Este debe mostrar “The number is odd!”.*/

// 1.1. Ejemplo usando funciones declaradas
function evenCallback(num) {
    console.log("The number '",num,"' is even!");
}
function oddCallback(num) {
    console.log("The number '",num,"'is odd!");
}   
function checkNumber(num, evenCallback, oddCallback) {
    if (num % 2 === 0) {
        evenCallback(num);
    } else {
        oddCallback(num);
    }
}
checkNumber(4, evenCallback, oddCallback); // Even case
checkNumber(5, evenCallback, oddCallback); // Odd case

// 1.2. Ejemplo usando arrow functions
const evenCallbackArrow = (num) => 
    console.log("The number '", num, "' is even!");
const oddCallbackArrow = (num) => 
    console.log("The number '", num, "' is odd!");
const checkNumberArrow = (num, evenArrow, oddArrow) =>
    num % 2 === 0 ? evenArrow(num) : oddArrow(num);
checkNumberArrow(4, evenCallbackArrow, oddCallbackArrow); // Even case
checkNumberArrow(5, evenCallbackArrow, oddCallbackArrow); // Odd case

// 1.3. Ejemplo usando named expresions
const evenCallbackNamedExpVar = function evenCallbackNamedExpFunc(num) {
    console.log("The number '", num, "' is even!");
}
const oddCallbackNamedExpVar = function oddCallbackNamedExpFunc(num) {
    console.log("The number '", num, "' is odd!");
}
const checkNumberNamedExpVar = function checkNumberNamedExpFunc(num, evenNamedExp, oddNamedExp) {
    if (num % 2 === 0) {
        evenNamedExp(num);
    } else {
        oddNamedExp(num);
    }
}
checkNumberNamedExpVar(4, evenCallbackNamedExpVar, oddCallbackNamedExpVar); // Even case
checkNumberNamedExpVar(5, evenCallbackNamedExpVar, oddCallbackNamedExpVar); // Odd case

// 1.4 Ejemplo usando named expresions
const evenCallbackUnnamedExpVar = function (num) {
    console.log("The number '", num, "' is even!");
}
const oddCallbackUnnamedExpVar = function (num) {
    console.log("The number '", num, "' is odd!");
}
const checkNumberUnnamedExpVar = function (num, evenUnnamedExp, oddUnnamedExp) {
    if (num % 2 === 0) {
        evenUnnamedExp(num);
    } else {
        oddUnnamedExp(num);
    }
}
checkNumberUnnamedExpVar(4, evenCallbackUnnamedExpVar, oddCallbackUnnamedExpVar); // Even case
checkNumberUnnamedExpVar(5, evenCallbackUnnamedExpVar, oddCallbackUnnamedExpVar); // Odd case



/*2. Cree dos archivos de texto con el siguiente contenido.    
    Lea ambos archivos y compare cuales palabras se repiten en ambos. Muestre el mensaje escondido al final del programa.*/

// Import modules
const readline = require('readline');
const fs = require('fs');

// Function to read a file line by line
const readFileCallback = function readFileLineByLine(filePath, callback) {
    const lines = [];
    const fileStream = fs.createReadStream(filePath);
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });
    rl.on('line', (line) => {
        lines.push(line.trim());
    });
    rl.on('close', () => {
        // return(lines, []); //No callback approach
        callback(lines, null); //Callback approach
    });
    rl.on('error', (err) => {
        // return([], err); //No callback approach
        callback(null, lines); //Callback approach
    });
}

// Function to find duplicate lines between two arrays
const duplicatesCallback = function findDuplicateLines(lines1, lines2) {
    const duplicates = [];
    const set1 = new Set(lines1);
    const set2 = new Set(lines2);
    set1.forEach(line => {
        if (set2.has(line)) {
            duplicates.push(line);
        }
    });
    return duplicates;   
}

/*
// First wrong approach
function get_secret_message(file1, file2, readFileCallback, duplicatesCallback) {
    const [lines1, err1] = readFileCallback(file1);
    if (err1 != "") {
        // report error on file 1
    } else {
        const [lines2, err2] = readFileCallback(file2);
        if (err2 != "") {
            // report error on file 2
        } else {
            // compare lines
            const secret_message = duplicatesCallback(lines1, lines2)
            return secret_message
        }
    }
}

const filePath1 = "File_1.txt";
const filePath2 = "File_2.txt";
const secret_message = get_secret_message(filePath1, filePath2, readFileCallback, duplicatesCallback);
*/

const filePath1 = "File_1.txt";
const filePath2 = "File_2.txt";
readFileCallback(filePath1, function(lines1, err1) {
    if (err1) { 
        return console.error("Error en archivo 1:", err1);
    } else {
        readFileCallback(filePath2, function(lines2, err2){
            if (err2) {
                return console.error("Error en archivo 2:", err2);
            } else {
                const secret_message = duplicatesCallback(lines1, lines2);
                console.log(secret_message);
            }
        });
    };
});
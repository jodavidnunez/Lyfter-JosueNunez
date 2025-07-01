/* 1. Realiza un programa que recorra una lista e imprima todos sus elementos.*/
const myArray = [1, 2, 3, 4];
myArray.forEach((i) => {
	console.log(i);
})


/* 2. Realiza un programa que recorra una lista de números y almacene todos los pares en otra lista */

/* 2.a. Solucion con 'for' */
const inputArray1 = [1, 2, 3, 4];
let outputArray = [];
const inputArraySize = inputArray1.length;
for (let index=0; index < inputArraySize; index++) {
    tmp_num = inputArray1[index];
    if (tmp_num % 2 === 0) {
        outputArray.push(tmp_num);
    }
}
console.log(outputArray)

/* 2.b. Solucion con 'filter' */
const inputArray2 = [1, 2, 3, 4];
const evenNumbers = inputArray2.filter(num => num%2===0);
console.log(evenNumbers);


/* 3. Toma una lista de temperaturas en grados celsius y conviertala a farenheit utilizando la función map */
const celciusTemps = [1, 2, 3, 4];
const farenheitTemps = celciusTemps.map((c) => {
	return ((1.8*c) + 32);
});
console.log(farenheitTemps);


/* 4. Toma un string y conviertelo en una lista de palabras, separandolas por espacios en blanco. No puedes usar la función split. */
const inputString = "This is a string!";
let outputList = []
let word = "";
const limit = inputString.length;
for (let index=0; index <= limit; index++) {
    const char = inputString[index]    
    if (char === " " || char === inputString[limit]) {
        outputList.push(word);
        word = "";
    } else {
        word += char;
    }
}
console.log(outputList)


/* 5. Realiza un programa que reciba el siguiente objeto, e imprima otro objeto con los datos requeridos */
// Entrada
const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

let result = {};
for (const primaryKey in student) {
    if (primaryKey === "name") {
        result.name = student[primaryKey]
    } else {
        allScoresList = [];
        scoresAndSubjectNamesObj = {};
        student[primaryKey].forEach((subject) => {
            currentSubjectName = "";
            currentGrade = 0;
            for (secondaryKey in subject) {
                if (secondaryKey === "name") {
                    currentSubjectName = subject[secondaryKey]
                } else {
                    currentGrade = subject[secondaryKey];
                    allScoresList.push(currentGrade);
                    scoresAndSubjectNamesObj[currentSubjectName] = currentGrade;   
                    currentSubjectName = "";
                    currentGrade = 0;
                }
            }
        })
        sortedScoresList = allScoresList.sort((a, b) => a - b);
        const scoresSum = sortedScoresList.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
        sortedScoresListSize = sortedScoresList.length;
        const gradeAvg = scoresSum/sortedScoresListSize;
        let lowestGrade = "";
        let highestGrade = "";
        //console.log(scoresAndSubjectNamesObj);
        for (subjectName in scoresAndSubjectNamesObj) {
            if (scoresAndSubjectNamesObj[subjectName] === sortedScoresList[0]) {
                lowestGrade = subjectName;
            }
            if (scoresAndSubjectNamesObj.subjectName === sortedScoresList[sortedScoresListSize]) {
                highestGrade = subjectName;
            }
        }
        result.lowestGrade = lowestGrade;
        result.highestGrade = highestGrade;
        result.gradeAvg = gradeAvg;
    }
}
console.log(result);
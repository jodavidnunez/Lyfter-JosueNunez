// Cree una función que liste todos los elementos retornados de un GET al endpoint https://api.restful-api.dev/objects 
// Filtre todos los resultados que no retornen data , y los formatee los que sí lo tienen de forma legible para mostrarlos en pantalla. 

// 1. Fetch function
async function getAllObjects() {
    console.log("-I-: Fetching all objects ...");
    try {
        const response = await fetch('https://api.restful-api.dev/objects');
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        const objects = await response.json();
        console.log("-I-: Successfully fetched", objects.length, "objects");
        return objects;
    } catch (err) {
        console.error("-E-: Error fetching objects:", err);
        return { error: err.message };
    }
}

// 2. Function to organize objects data into data structure
function analyzeObjectsData(objects) {
    if (!Array.isArray(objects)) {
        return { error: 'Expected an array of objects' };
    }
    const analysis = {
        totalObjs: objects.length,
        objsWithData: 0,
        objsWithoutData: 0,
        dataAttributes: [],
        uniqueDataKeys: new Set()
    };
    objects.forEach(obj => {
        if (obj.data && Object.keys(obj.data).length > 0) { 
            analysis.objsWithData++;
            analysis.dataAttributes.push({
                id: obj.id,
                name: obj.name,
                data: obj.data
            });
            Object.keys(obj.data).forEach(key => {
                analysis.uniqueDataKeys.add(key);
            });
        } else {
            analysis.objsWithoutData++;
        }
    });
    analysis.uniqueDataKeys = Array.from(analysis.uniqueDataKeys);
    return analysis;
}

// 3. Function to print out objects data in required format. 
function displayDataObjs(analysis) {
    if (analysis.error) {
        console.error("-E-:", analysis.error);
        return;
    }
    if (!analysis.dataAttributes || analysis.dataAttributes.length === 0) {
        console.log("-I-: No objects have data attributes.");
    } else {
        const formatData = obj =>
            JSON.stringify(obj)
                .replace(/"/g, '')   
                .replace(/{/g, '(')  
                .replace(/}/g, ')')
                .replace(/,/g, ', ')
        console.log("-I-: Found objects data:");
        analysis.dataAttributes.forEach(item => {
            console.log(item.name, formatData(item.data));
        });
    }
}

// 4. Main async function definition.
async function getDataFromObjects() {
    try {
        const objects = await getAllObjects();
        if (objects && objects.error) {
            console.error("-E-: Fetch failed:", objects.error);
            return;
        }
        const analysis = analyzeObjectsData(objects);
        displayDataObjs(analysis);
    } catch (err) {
        console.error("-E-: Main function error:", err);
    }
}

// 5. Main function call.
getDataFromObjects();
// 3. Cree una función que retorne un usuario del API, tomando su ID como parámetro. 
// Si no existe el usuario, debe manejar adecuadamente el código 404 retornado, y
// retornar un mensaje de error.

async function postUser(userData) {
    try {
        const response = await fetch('https://api.restful-api.dev/objects', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData)
        });
        if (!response.ok) throw response;
        return await response.json();
    } catch (err) {
        // centralized handling: Response (HTTP) or Error/other
        if (err && typeof err.status === 'number' && typeof err.json === 'function') {
            // err is a Response
            let bodyMsg = '';
            try {
                const body = await err.json();
                bodyMsg = body?.message ?? JSON.stringify(body);
            } catch {
                bodyMsg = await err.text().catch(() => err.statusText || '');
            }
            const e = new Error(bodyMsg || `HTTP ${err.status} ${err.statusText}`);
            e.status = err.status;
            console.error("-E-: Error creating new user:", e);
            throw e;
        }

        // non-HTTP errors: preserve Error instances, normalize others
        console.error("-E-: Error creating new user:", err);
        if (err instanceof Error) throw err;
        throw new Error(String(err));
    }
}

async function createNewUser(userData) {
    try {
        const postResult = await postUser(userData);
        //console.log('Created:', postResult);
        return postResult;
    } catch (err) {
        const status = err?.status;
        if (typeof status === 'number') {
            let errMessage;
            switch (status) {
                case 404: errMessage = 'Resource not found'; break;
                case 400: errMessage = 'Bad request'; break;
                case 500: errMessage = 'Server error'; break;
                default: errMessage = `HTTP error ${status}`;
            }
            console.error("-E-(createNewUser): Create new user failed:", `${errMessage} (status ${status})`);
            return null;
        }
        console.error("-E-(createNewUser): Main function error:", err?.message ?? String(err));
        return null;
    }
}

async function verifyUserCreation(userID) {
    try {
        const response = await fetch(`https://api.restful-api.dev/objects/${userID}`, {
            method: 'GET',
            headers: {'Content-Type': 'application/json'}
        });
        if (!response.ok) throw response;
        const userData = await response.json();
        console.log("-I-(verifyUserCreation): User verification successful:", userData);
        return userData;
    } catch (err) {
        if (err && typeof err.status === 'number' && typeof err.json === 'function') {
            // Handle specific response errors
            let bodyMsg = '';
            try {
                const body = await err.json();
                bodyMsg = body?.message ?? JSON.stringify(body);
            } catch {
                bodyMsg = await err.text().catch(() => err.statusText || '');
            }
            let errMessage;
            switch (err.status) {
                case 404: errMessage = `User with ID '${userID}' was not found. Creation may have failed`; break;
                case 400: errMessage = `Invalid user ID format: ${userID}`; break;
                case 500: errMessage = `Server error occured while verifying user creation`; break;
                default: errMessage = `HTTP error ${err.status}: ${bodyMsg || err.statusText}`;
            }
            console.error("-E-(verifyUserCreation): User verification failed:", errMessage);
            const customError = new Error(errMessage); // use errMessage (fixed)
            customError.status = err.status;
            customError.userID = userID;
            throw customError;
        }
        // Handle other errors
        const errorMessage = `Failed to verify user creation for ID '${userID}': ${err?.message || String(err)}`;
        console.error("-E-(verifyUserCreation): User verification error:", errorMessage);
        const customError = new Error(errorMessage);
        customError.userID = userID;
        if (err instanceof Error) {
            customError.originalError = err;
        }
        throw customError; 
    }
}

async function createAndVerifyUser(userData) {
    try {
        const newUserResult = await createNewUser(userData);
        if (!newUserResult?.id) {
            throw new Error('User creation failed - no ID returned from API');
        }
        console.log('-I-(createAndVerifyUser): User created with ID:', newUserResult.id);
        // Good case -Default behavior-:
        const id_to_chk = newUserResult.id;
        // Bad case -to test error reporting-:
       // const id_to_chk = "DUMMY_ID";
        const verifiedUser = await verifyUserCreation(id_to_chk);
        return {
            success: true,
            user: verifiedUser,
            message: 'User created and verified successfully'
        };
    } catch (err) {
        let errorMessage = 'User creation process failed';
        if (err.status === 404) {
            errorMessage = 'User was created but cannot be found.';
        } else if (err.status) {
            errorMessage = `HTTP error during process: ${err.message}`;
        } else {
            errorMessage = err.message || 'Unknown error during user creation process';
        }
        console.error("-E-(createAndVerifyUser): Create and verify failed", errorMessage);
        return {
            success: false,
            error: errorMessage,
            status: err.status || null,
            userID: err.userID || null
        };
    }
}

(async () => {
    const userData = {
        name: 'Snorlax',
        data: {
            mail: 'happy.eating.and.sleeping@pokemon.com',
            password: 'Relaxed7985!¿?%',
            direction: 'Route 16, Celadon City, Kanto region.'
        }
    };
    const result = await createAndVerifyUser(userData);
    if (result.success) {
        console.log('-I-(MAIN): Process completed:', result.message);
    } else {
        console.log('-E-(MAIN): Process failed:', result.error);
    }
})()
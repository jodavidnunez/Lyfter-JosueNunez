// 2. Cree una función que tome por parámetro nombre, correo, contraseña y dirección, y cree un usuario con el endpoint POST de la documentación brindada.

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
            console.error("-E-: Create new user failed:", `${errMessage} (status ${status})`);
            return null;
        }
        console.error("-E-: Main function error:", err?.message ?? String(err));
        return null;
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

    const newUserResult = await createNewUser(userData);
    console.log(newUserResult);
})();

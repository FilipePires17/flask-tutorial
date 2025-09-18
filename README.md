Minimal instructions to allow a small React frontend (on Vercel) to call this Flask API hosted on Render.

1. Configure Render (backend)

- In the Render service (web service) settings, add an environment variable:

  - `CORS_ORIGINS` -> `https://your-frontend.vercel.app`

  If you are NOT using cookies or sessions and want the simplest setup, you can set:

  - `CORS_ORIGINS` -> `*`
    (note: if you use `*`, cookies/credentials are not allowed.)

- Optionally add:
  - `CORS_SUPPORTS_CREDENTIALS` -> `true` (only if using cookies and `CORS_ORIGINS` is a specific origin)

2. Frontend (React)

- If you use token-based auth (Authorization header), no special fetch config is required other than using the correct API URL.

- If you use cookies / session authentication, set in the request:

  - fetch: `credentials: 'include'`
  - axios: `withCredentials: true`

- Example fetch:

  fetch('https://your-backend.onrender.com/users/', {
  method: 'GET',
  credentials: 'include' // only if using cookies
  })

3. Quick local test

- Activate your venv and run the app locally:

```bash
source ./dnet-env/bin/activate
python3 app.py
```

- Curl with an Origin header to verify response headers:

```bash
curl -i -H "Origin: https://your-frontend.vercel.app" http://127.0.0.1:5000/users/
```

4. Notes

- The server reads `CORS_ORIGINS` and `CORS_SUPPORTS_CREDENTIALS` from environment variables (or `config.py`).
- For small apps on Render this is intentionally simple: set the single `CORS_ORIGINS` env var to your frontend URL and you're done.

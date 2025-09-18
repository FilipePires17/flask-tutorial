import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.sqlite3')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Comma-separated list or JSON-style list of allowed CORS origins.
    # Example: export CORS_ORIGINS="https://my-app.vercel.app"
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS")
    # Ensure ENV is set (flask sets this as well); used to allow '*' in dev
    ENV = os.environ.get("FLASK_ENV", os.environ.get("ENV", "production"))
    # Optionally control whether credentials are allowed (cookies). If not set,
    # the app will choose a safe default: True for specific origins, False for '*'.
    CORS_SUPPORTS_CREDENTIALS = os.environ.get("CORS_SUPPORTS_CREDENTIALS")

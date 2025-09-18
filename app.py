import os
from flask import Flask
from extensions import db
from blueprints.user.routes import user_bp
from config import Config
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix="/users")

    with app.app_context():
        db.create_all()

    cors_origins = app.config.get("CORS_ORIGINS")
    if cors_origins:
        if isinstance(cors_origins, str):
            cors_origins = [o.strip() for o in cors_origins.split(",") if o.strip()]
    else:
        if app.config.get('ENV') == 'development' or app.config.get('DEBUG'):
            cors_origins = "*"
        else:
            cors_origins = None

    cors_supports_credentials = app.config.get('CORS_SUPPORTS_CREDENTIALS')
    if isinstance(cors_supports_credentials, str):
        cors_supports_credentials = cors_supports_credentials.lower() in ("1", "true", "yes")
    if cors_supports_credentials is None:
        cors_supports_credentials = False if cors_origins == "*" else True

    if cors_origins is not None:
        CORS(app, resources={r"/*": {"origins": cors_origins}}, supports_credentials=cors_supports_credentials)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
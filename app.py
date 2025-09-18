import os
from flask import Flask
from extensions import db
from blueprints.user.routes import user_bp
from config import Config

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

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
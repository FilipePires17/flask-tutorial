import os
from flask import Flask
from extensions import db
from blueprints.user.routes import user_bp
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(user_bp, url_prefix="/users")

with app.app_context():
    db.create_all()

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
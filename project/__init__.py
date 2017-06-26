import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# instanciate the db
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app

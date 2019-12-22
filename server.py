from flask import Flask
from flask_cors import CORS
from sqlalchemy_utils import database_exists

from __config__ import BaseConfig
from db import db
from service import note_service
from service.util.json_encoder import ModelEncoder

application = Flask(__name__)
CORS(application, support_credentials=True)

application.config.from_object(BaseConfig)
application.app_context().push()
application.json_encoder = ModelEncoder

db.init_app(application)

if not database_exists(BaseConfig.SQLALCHEMY_DATABASE_URI):
    db.create_all()

application.register_blueprint(note_service.note, url_prefix='/note')

if __name__ == "__main__":
    application.run(host="0.0.0.0")

#!/var/www/u0626898/data/myenv/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask,redirect
from flask_cors import CORS
from sqlalchemy_utils import database_exists

from backend.__config__ import BaseConfig
from backend.db import db, initialize_database
from backend.service import auth_service, user_service, spbu_service
from backend.service.util.json_encoder import ModelEncoder

application = Flask(__name__)
application.config.from_object(BaseConfig)
application.config.update(SERVER_NAME='gsom-rating.ru')
application.app_context().push()
application.json_encoder = ModelEncoder

db.init_app(application)


@application.route('/calculator')
def calculator():
    return redirect("https://gsom-rating.ru/calculator/", code=301)


@application.route('/rating')
def rating():
    return redirect("https://gsom-rating.ru/rating/", code=301)
    
    
@application.route('/user')
def user_page():
    return redirect("https://gsom-rating.ru/user/", code=301)
    

if not database_exists(BaseConfig.SQLALCHEMY_DATABASE_URI):
    db.create_all()
    initialize_database()
CORS(application, supports_credentials=True)

application.register_blueprint(auth_service.auth, url_prefix='/auth')
application.register_blueprint(user_service.user, url_prefix='/user')
application.register_blueprint(spbu_service.spbu, url_prefix='/spbu')

#application.run(debug=True, host='gsom-rating.ru')

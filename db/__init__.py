#!/var/www/u0626898/data/myenv/bin/python
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class JSONStripped:
    def jsonify(self):
        blacklist = {
            'metadata',
            'query',
            'query_class',
        }
        return {attr: getattr(self, attr)
                for attr in self.__dict__.keys()
                if not attr.startswith('_') and attr not in blacklist}


from db import note_db


def initialize_database():
    note_db.Note.fill()

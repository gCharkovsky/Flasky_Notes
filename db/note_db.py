#!/var/www/u0626898/data/myenv/bin/python
# -*- coding: utf-8 -*-
from db import db, JSONStripped


class Note(db.Model, JSONStripped):
    __tablename__ = 'note'

    def __init__(self, *args, **kwargs):
        super(Note, self).__init__(*args, **kwargs)

    id = \
        db.Column(db.Integer, primary_key=True)
    color = \
        db.Column(db.String(255))
    title = \
        db.Column(db.String(255))
    text = \
        db.Column(db.Text)

    def __repr__(self):
        return '<Note %r>' % self.name

    @staticmethod
    def insert(**kwargs):
        note = Note(**kwargs)
        print(note.text)
        db.session.add(note)
        db.session.commit()
        return note

    @staticmethod
    def delete(**kwargs):
        Note.query.filter_by(**kwargs).delete()
        db.session.commit()

    @staticmethod
    def update(note):
        Note.query.filter_by(id=note['id']).update(note)
        db.session.commit()

    @staticmethod
    def get_one(**kwargs):
        return Note.query.filter_by(**kwargs).first()

    @staticmethod
    def get_all(**kwargs):
        return Note.query.filter_by(**kwargs).all()[::-1]

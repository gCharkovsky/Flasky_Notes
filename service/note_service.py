#!/var/www/u0626898/data/myenv/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, make_response

from db.note_db import Note

note = Blueprint('note', __name__)


@note.route('/', methods=['POST'])
def add_note():
    print('Add ' + str(request.get_json(silent=True)["color"]))
    Note.insert(color=request.get_json(silent=True)["color"],
                title=request.get_json(silent=True)["title"],
                text=request.get_json(silent=True)["text"])
    resp = make_response('Add')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@note.route('/<int:id>', methods=['POST'])
def update_note(id):
    new_note = {"id": request.get_json(silent=True)["id"],
                "color": request.get_json(silent=True)["color"],
                "title": request.get_json(silent=True)["title"],
                "text": request.get_json(silent=True)["text"]}
    Note.update(new_note)
    print(new_note["text"])
    resp = make_response('Update')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@note.route('/<int:id>', methods=['DELETE'])
def delete_note(id):
    Note.delete(id=id)
    resp = make_response('Delete')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@note.route('/', methods=['GET'])
def get_notes():
    print('Get ' + str(request.query_string))
    res = Note.get_all()
    resp = make_response(jsonify(res))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@note.route('/<int:id>', methods=['GET'])
def get_note(id):
    return 'Get one '

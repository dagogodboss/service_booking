from app.Models.Service import Service
from app import db
from flask import request, jsonify, make_response


def index():
    res = {}
    try:
        allService = Service.query.all()
        data = generate(allService)
        res['data'] = data
        res['msg'] = "Data found!"
        return make_response(jsonify(res)), 200
    except Exception as e:
        res['data'] = None
        res['msg'] = str(e)
        return make_response(jsonify(res)), 400


def generate(values):
    array = []

    for i in values:
        array.append({'id': i.id, 'name': i.name, 'duration': i.duration})
    return array


def show(id):
    res = {}
    try:
        service = Service.query.filter_by(id=id).first()
        if not service:
            res['data'] = None
            res['msg'] = "Data not found !"
            return make_response(jsonify(res)), 400
        data = {
            'id': service.id,
            'name': service.name,
            'duration': service.duration
        }
        res['data'] = data
        res['msg'] = "Data not found !"
        return make_response(jsonify(res)), 200
    except Exception as e:
        res['data'] = None
        res['msg'] = str(e)
        return make_response(jsonify(res)), 400


def save():
    res = {}
    try:
        name = request.form.get('name')
        duration = request.form.get('duration')

        data = [{'name': name, 'duration': duration}]

        save = Service(name=name, duration=duration)
        db.session.add(save)
        db.session.commit()

        res['data'] = data
        res['msg'] = "Data added successfully !"
        return make_response(jsonify(res)), 200

    except Exception as e:
        res['data'] = None
        res['msg'] = str(e)
        return make_response(jsonify(res)), 400


def update(id):
    res = {}
    try:
        name = request.form.get('name')
        duration = request.form.get('duration')

        save = Service.query.filter_by(id=id).first()
        save.name = name
        save.duration = duration
        db.session.commit()

        res['data'] = save.name
        res['msg'] = "Data changed successfully !"
        return make_response(jsonify(res)), 200
    except Exception as e:
        res['data'] = None
        res['msg'] = str(e)
        return make_response(jsonify(res)), 400


def delete(id):
    res = {}
    try:
        service = Service.query.filter_by(id=id).first()
        if not service:
            res['data'] = None
            res['msg'] = "Data not found !"
            return make_response(jsonify(res)), 400

        data = service.name

        db.session.delete(service)
        db.session.commit()

        res['data'] = data
        res['msg'] = "Data deleted successfully !"
        return make_response(jsonify(res)), 200

    except Exception as e:
        res['data'] = None
        res['msg'] = str(e)
        return make_response(jsonify(res)), 400
from app.Models.Customer import Customer
from app import db
from flask import request, jsonify, make_response


def index():
    res = {}
    try:
        allCustomer = Customer.query.all()
        data = generate(allCustomer)
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
        array.append({'id': i.id, 'name': i.name, 'email': i.email})
    return array


def show(id):
    res = {}
    try:
        customer = Customer.query.filter_by(id=id).first()
        if not customer:
            res['data'] = None
            res['msg'] = "Data not found !"
            return make_response(jsonify(res)), 400
        data = {
            'id': customer.id,
            'name': customer.name,
            'email': customer.email
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
        email = request.form.get('email')

        data = [{'name': name, 'email': email}]

        save = Customer(name=name, email=email)
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
        email = request.form.get('email')

        save = Customer.query.filter_by(id=id).first()
        save.name = name
        save.email = email
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
        customer = Customer.query.filter_by(id=id).first()
        if not customer:
            res['data'] = None
            res['msg'] = "Data not found !"
            return make_response(jsonify(res)), 400

        data = customer.name

        db.session.delete(customer)
        db.session.commit()

        res['data'] = data
        res['msg'] = "Data deleted successfully !"
        return make_response(jsonify(res)), 200

    except Exception as e:
        res['data'] = None
        res['msg'] = str(e)
        return make_response(jsonify(res)), 400
from app import app
from app.Controller import customer_controller
from app.Controller import service_controller
from flask import request
# from flask_jwt_extended import jwt_required
import sys


@app.route('/')
def home():
    return "Flask " + sys.version


@app.route('/customers', methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        return customer_controller.index()
    else:
        return customer_controller.save()


@app.route('/customers/<id>', methods=['GET', 'PUT', 'DELETE'])
def customerId(id):
    if request.method == 'GET':
        return customer_controller.show(id)
    elif request.method == 'PUT':
        return customer_controller.update(id)
    else:
        return customer_controller.delete(id)


@app.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'GET':
        return service_controller.index()
    else:
        return service_controller.save()


@app.route('/services/<id>', methods=['GET', 'PUT', 'DELETE'])
def servicesId(id):
    if request.method == 'GET':
        return service_controller.show(id)
    elif request.method == 'PUT':
        return service_controller.update(id)
    else:
        return service_controller.delete(id)
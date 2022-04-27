"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Projects
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


#create a donation

@api.route('/user', methods=['POST'])
def get_user():
    body=request.get_json()
    if body is None:
        raise APIException("Tienes que enviar información en el body",status_code=400)
    if body['email'] is None:
        raise APIException("Tienes que enviar el correo ")
    user=User.query.filter_by(email=body['email']).first()
    if user is None :
        raise APIException("El usuario no existe")
    return jsonify(user.serialize()),200

@api.route('/projects', methods=['POST'])
def post_project():
    body=request.get_json()
    if body is None:
        raise APIException("Tienes que ingresar información del proyecto", status_code=400)
    if 'name' not in body:
        raise APIException("Tienes que ingresar el nombre del proyecto")
    if 'date_finish' not in body:
        raise APIException("La fecha de finalización no se ha indicado")
    if 'id_beneficiary' not in body:
        raise APIException("Tienes que ingresar el ID del beneficiario")
    if 'description' not in body:
        raise APIException("Tienes que ingresar la descripción del proyecto")
    if 'donative_amount' not in body:
        raise APIException("Falta ingresar un monto a donar")

    user=User.query.get(body['id_beneficiary'])
    if user is None:
        raise APIException("El usuario beneficiario no existe")

    add_project=Projects(name=body['name'], date_finish=body['date_finish'], id_beneficiary=body['id_beneficiary'], description=body['description'], donative_amount=body['donative_amount'], is_active=True)
    db.session.add(add_project)
    db.session.commit()
    return jsonify(add_project.serialize()),200
    

@api.route('/projects/', methods=['DELETE'])
def delete_project():
    body= request.get_json()
    if body is None:
        raise APIException("Tienes que agregar el proyecto a eliminar en el body", status_code=400)
    if 'id' not in body:
        raise APIException("Tienes que agregar el ID del proyecto que deseas eliminar", status_code=400)
    delete_projects= Projects.query.get(body['id'])
    if delete_projects is None:
        raise APIException("El proyecto que quieres eliminar no ha sido encontrado", status_code=400)
    delete_projects.is_active=False
    db.session.commit()
    return jsonify(delete_projects.serialize()),200
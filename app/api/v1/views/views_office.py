from flask import Blueprint, jsonify, make_response, request
from app.api.v1.models.models_office import Office

politico_office = Blueprint("office_route", __name__)


@politico_office.route('/offices', methods=['GET'])
def endpoint_offices():
    office_list = Office().get_office_list()
    if len(office_list) >= 0:
        return make_response(jsonify({"status": "200", "data": office_list}), 200)
    else:
        return make_response(jsonify({"status": "404", "message": "Error!Request not found."}), 404)


@politico_office.route('/offices/<office_id>', methods=['GET'])
def endpoint_office(office_id):
    try:
        office = Office(office_id).get_office()
        if office:
            return make_response(jsonify({"status": "200", "office": [office]}), 200)
        else:
            return make_response(jsonify({"message": "Invalid Request", "status": "400"}), 400)

    except IndexError:
        return make_response(jsonify({"message": "Index Error", "status": "400"}), 400)


@politico_office.route('/offices', methods=['POST'])
def endpoint_add_office():
    data = request.get_json()
    new_office = Office(data).add_office()
    if new_office:
        return make_response(
            jsonify({"message": "Office created successfully.", "status": "201", "data": [new_office]}),
            201)

    else:
        return make_response(jsonify({"message": "Unable to create office", "status": "400"}), 400)



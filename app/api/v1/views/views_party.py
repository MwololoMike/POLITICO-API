from flask import Blueprint, jsonify, make_response, request
from app.api.v1.models.models_party import Party

politico = Blueprint("party_route", __name__)


@politico.route('/parties', methods=['POST'])
def endpoint_add_party():
    data = request.get_json()
    new_party = Party(data).add_party()
    if new_party:
        return make_response(jsonify({"message": "Party created successfully.", "status": "201", "data": [new_party]}),
                             201)
    else:
        return make_response(jsonify({"message": "Please enter valid data to create party.", "status": "400"}),
                             400)


@politico.route('/parties', methods=['GET'])
def endpoint_parties():
    try:
        party_list = Party().get_party_list()
        if len(party_list) >= 0:
            return make_response(jsonify({"status": "200", "data": party_list}), 200)
        else:
            return make_response(jsonify({"status": "404", "message": "Request not found."}), 404)
    except TypeError:
        return make_response(jsonify({"status": "400", "message": "Error!Not found"}))


@politico.route('/parties/<party_id>/name', methods=['PATCH'])
def endpoint_edit_party(party_id):
    data = request.get_json(force=True)
    new_party_name = Party(data).edit_party()
    if new_party_name:
        return make_response(jsonify({"message": "Party name updated successfully", "status": "202",
                                      "data": [{"party_id": party_id, "name": new_party_name}]}), 202)
    else:
        return make_response(jsonify({"message": "Unable to update party.", "status": "404"}), 404)


@politico.route('/parties/<party_id>', methods=['GET'])
def endpoint_party(party_id):
    try:
        party = Party(party_id=party_id).get_party()
        if party:
            return make_response(jsonify({"status": "200", "party": [party]}), 200)
        else:
            return make_response(jsonify({"message": "Invalid Request", "status": "400"}), 400)
    except IndexError:
        return make_response(jsonify({"message": "Index Error", "status": "400"}), 400)


@politico.route('/parties/<party_id>', methods=['DELETE'])
def endpoint_delete_party(party_id):
    try:
        success = Party(party_id=party_id).delete_party()
        if success:
            return make_response(jsonify({"message": "Successfully Deleted.", "status": "202"}), 202)
        else:
            return make_response(jsonify({"message": "Failed to delete.", "status": "404"}), 404)
    except IndexError:
        return make_response(jsonify({"status": "400", "message": "Index Error."}), 400)

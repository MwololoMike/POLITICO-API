from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

office_list = []
party_list = []


@app.route('/offices', methods=['GET'])
def api_offices():
    if len(office_list) >= 0:
        return make_response(jsonify({"status": "200", "data": office_list}), 200)
    else:
        return make_response(jsonify({"status": "404", "message": "Error!Request not found."}), 404)


@app.route('/parties', methods=['GET'])
def api_parties():
    if len(party_list) >= 0:
        return make_response(jsonify({"status": "200", "data": party_list}), 200)
    else:
        return make_response(jsonify({"status": "404", "message": "Error!Request not found."}), 404)


@app.route('/offices/<office_id>', methods=['GET'])
def api_office(office_id):
    try:
        office = office_list[int(office_id) - 1]
        if office:
            return make_response(jsonify({"status": "200", "office": [office]}), 200)
        else:
            return make_response(jsonify({"message": "Invalid Request", "status": "400"}), 400)

    except IndexError:
        return make_response(jsonify({
            "message": "Index Error",
            "status": "400"
        }), 400)


@app.route('/parties/<party_id>', methods=['GET'])
def api_party(party_id):
    try:
        party = party_list[int(party_id) - 1]
        if party:
            return make_response(jsonify({"status": "200", "party": [party]}), 200)
        else:
            return make_response(jsonify({"message": "Invalid Request", "status": "400"}), 400)
    except IndexError:
        return make_response(jsonify({"message": "Index Error", "status": "400"}), 400)


@app.route('/offices', methods=['POST'])
def api_add_office():
    data = request.get_json()
    office_name = data["name"]
    if len(office_list) > 0:
        office_id = office_list[-1]['office_id'] + 1
    else:
        office_id = len(office_list) + 1
    office_type = data['type']

    new_office = {"name": office_name, "office_id": office_id, "type": office_type}

    office_list.append(new_office)

    return make_response(jsonify({"message": "Office created successfully.", "status": "201", "data": [new_office]}),
                         201)


@app.route('/parties', methods=['POST'])
def api_add_party():
    data = request.get_json()
    party_name = data["name"]
    logo_url = data['logoUrl']
    party_address = data['hqAddress']
    if len(party_list) > 0:
        party_id = party_list[-1]['party_id'] + 1
    else:
        party_id = len(party_list) + 1

    new_party = {
        "name": party_name,
        "party_id": party_id,
        "logoUrl": logo_url,
        "hqAddress": party_address
    }
    party_list.append(new_party)

    return make_response(jsonify({"message": "Party created successfully.", "status": "201", "data": [new_party]}), 201)


@app.route('/parties/<party_id>/name', methods=['PATCH'])
def api_edit_party(party_id):
    data = request.get_json()
    new_party_name = data["name"]
    for party in party_list:
        if party['id'] == party_id:
            party['name'] = new_party_name
            return make_response(jsonify({
                "message": "Party name updated successfully", "status": "200", "data": [party]}), 200)
        else:
            return make_response(jsonify({"message": "Invalid.", "status": "404"}), 404)
    return make_response(jsonify({"message": "Error", "status": "404"}), 404)


@app.route('/parties/<party_id>', methods=['DELETE'])
def api_delete_party(party_id):
    try:
        party = [party for party in party_list if party['party_id'] == party_id]
        if len(party_list) == 0:
            return make_response(jsonify({"message": "Failed to delete.", "status": "404"}), 404)
        else:
            party_list.remove(party[0])
            return make_response(jsonify({"message": "Successfully Deleted.", "status": "202"}), 202)
    except IndexError:
        return make_response(jsonify({"status": "400", "message": "Index Error."}), 400)


if __name__ == "__main__":
    app.run()


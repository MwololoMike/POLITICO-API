from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
office_list = []
party_list = []


@app.route('/offices', methods=['GET'])
def api_offices():
    return make_response(jsonify({
        "status": "200",
        "offices": office_list
    }), 200)


@app.route('/parties', methods=['GET'])
def api_parties():
    return make_response(jsonify({
        "status": "200",
        "parties": party_list
    }), 200)


@app.route('/offices/<office_id>', methods=['GET'])
def api_office(office_id):
    return make_response(jsonify({
         "status": "200",
         "offices": office_list[office_id]
     }), 200)


@app.route('/parties/<party_id>', methods=['GET'])
def api_party(party_id):
    return make_response(jsonify({
        "status": "200",
        "parties": party_list[party_id]
    }), 200)


@app.route('/offices', methods=['POST'])
def api_add_office():
    data = request.get_json()
    name = data["name"]
    office_id = len(office_list)+1
    kind = data["type"]

    new_office = {
        "name": name,
        "type": kind,
        "office_id": office_id

    }

    office_list.append(new_office)
    return make_response(jsonify({
        "message": "Office created successfully.",
        "status": "201",
        "offices": new_office['name'],
        "office_id": office_id,
        "type": new_office['type']
    }), 201)


@app.route('/parties', methods=['POST'])
def api_add_party():
    data = request.get_json()
    name = data["name"]
    party_id = len(party_list)+1

    new_party = {
        "name": name,
        "party_id": party_id

    }

    office_list.append(new_party)
    return make_response(jsonify({
        "message": "Party created successfully.",
        "status": "201",
        "parties": new_party['name'],
        "party_id": party_id
    }), 201)


if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
office_list = []
party_list = []


@app.route('/offices', methods=['GET'])
def offices():
    return make_response(jsonify({
        "status": "200",
        "offices": office_list
    }), 200)


@app.route('/parties', methods=['GET'])
def parties():
    return make_response(jsonify({
        "status": "200",
        "parties": party_list
    }), 200)


@app.route('/offices/ < office-id > ', methods=['GET'])
def offices():
    return make_response(jsonify({
        "status": "200",
        "offices": office_list
    }), 200)


if __name__ == "__main__":
    app.run()

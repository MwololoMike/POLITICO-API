from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
office_list = []

@app.route('/offices', methods=['GET'])
def offices():
    return make_response(jsonify({
         "status": "200",
         "offices" : office_list
    }),200)


if __name__ == "__main__":
    app.run()

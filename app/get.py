from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/callname/<string:name>', methods=['GET'])
def call_name(name):
    response = {'hello': name}
    return jsonify(response)

if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/callname', methods=['POST'])
def call_name():
    name = request.json['name']
    response = {'hello': name}
    return jsonify(response)

if __name__ == '__main__':
    app.run()

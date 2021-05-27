from flask import Flask, jsonify;
from flask_cors import CORS;
# from flask_restful import Resource, Api;

app = Flask(__name__)
# api=Api(app)
CORS(app)
employee = {
    "data": [
    {
        "id": "23",
        "empName": "alemu",
        "Age": "54",
        "Description": "The worker for permanent employement"
    },
    {
        "id": "45",
        "empName": "yibeltal",
        "Age": "34",
        "Description": "This is for reserve"
    },
    ]
}

@app.route("/", methods=['GET'])
def index():
    return "Welcome to CodezUp";
@app.route("/employeeReport/", methods = ['GET'])
def employeeReport():
    global employee
    return jsonify([employee])
if __name__ == '__main__':
    app.run(debug=True)

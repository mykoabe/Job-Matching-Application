from flask import Flask, jsonify;
from flask_cors import CORS;
# from flask_restful import Resource, Api;


app = Flask(__name__)
# api=Api(app)
CORS(app)

works = {
    "data": [
    {
        "id": "1",
        "jobtype": "Mechanical Engineer",
        "avaliabilty": "This job is available since yesteday",
        "status": "closed"
    },
    {
        "id": "2",
        "jobtype": "Part time",
        "avaliabilty": "This job vacanciy is released today",
        "status": "open"
    },
    {
        "id": "2",
        "jobtype": "Remote software developer",
        "avaliabilty": "This job vacanciy is released today",
        "status": "open"
    },
    {
        "id": "2",
        "jobtype": "Remote",
        "avaliabilty": "This job vacanciy is released today",
        "status": "open"
    },
    {
        "id": "2",
        "jobtype": "Part time",
        "avaliabilty": "This job vacanciy is released today",
        "status": "open"
    }
    ]
}


@app.route("/", methods=['GET'])
def index():
    return "Welcome to Jobs"

@app.route("/worksReport/", methods = ['GET'])
def worksReport():
    global works
    return jsonify([works])

if __name__ == '__main__':
    app.run(debug=True)

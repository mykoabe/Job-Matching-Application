import os
from flask import render_template, url_for, flash, redirect, request, jsonify
from JobMatching import app, db
from JobMatching.model import User
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

import os
from datetime import datetime
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # this is for registration
from flask_login import LoginManager

from flask_cors import CORS;
# from flask_restful import Resource, Api;
from dotenv import load_dotenv
app = Flask(__name__)
# api=Api(app)
CORS(app)

app.config['SECRET_KEY'] = 'd1e2ee4600fe51d7f5bf0d0804ce58e0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# creating the instance of the database file
db = SQLAlchemy(app)
# creating instance of the bcrypt class object
bcrypt = Bcrypt(app)
# creating the login manager instance
login_manager = LoginManager(app)
# this to redirect to the login form is there is no active user in accounts page
# to do this we must first import login_required in the init
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# as we take the routes from here
from JobMatching import routes

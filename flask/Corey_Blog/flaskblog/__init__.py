
# init app and components

from flaskblog import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##############
# Create app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e5b5f106a66adfe0c4dce3a246b7babe'

##############
# DB settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

##############
# Create db
db = SQLAlchemy(app)

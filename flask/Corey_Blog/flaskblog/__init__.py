
# init app and components


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

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


##################
# Password hasher
bcrypt = Bcrypt(app)

##################
# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# has to be at the end!!!
from flaskblog import routes

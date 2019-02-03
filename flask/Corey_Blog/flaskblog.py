# http://flask.pocoo.org/

# set env variable
# set FLASK_APP=flaskblog.py
# set FLASK_DEBUG=1 <----- to run changes without restarting the web server
# flask run

# python flaskblog.py

# http://localhost:5000/
from datetime import datetime

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm


app = Flask(__name__)


#####################
# https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key
#
# in python interpreter
# >>> import secrets
# >>> secrets.token_hex(16)

app.config['SECRET_KEY'] = 'e5b5f106a66adfe0c4dce3a246b7babe'

##############
# DB settings

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# Models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='defaul.jpg')
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


##############

posts = [
    {
        'author':'Christian',
        'title': 'Blog Post 1',
        'content':'First Post content',
        'date_posted': 'April 20, 2018',
    },
    {
        'author':'Katrin',
        'title': 'Blog Post 2',
        'content':'Second Post content',
        'date_posted': 'April 21, 2018',
    }
]

# Decorator to add additional functionality to a function
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accout created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'papa@gmail.com' and form.password.data == 'papa':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
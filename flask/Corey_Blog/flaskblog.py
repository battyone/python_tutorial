# http://flask.pocoo.org/

# set env variable
# set FLASK_APP=flaskblog.py
# set FLASK_DEBUG=1 <----- to run changes without restarting the web server
# flask run

# python flaskblog.py

# http://localhost:5000/

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# in python interpreter
# >>> import secrets
# >>> secrets.token_hex(16)

app.config['SECRET_KEY'] = 'e5b5f106a66adfe0c4dce3a246b7babe'

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
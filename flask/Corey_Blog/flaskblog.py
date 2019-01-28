# http://flask.pocoo.org/

# set env variable
# set FLASK_APP=flaskblog.py
# set FLASK_DEBUG=1 <----- to run changes without restarting the web server
# flask run

# http://localhost:5000/

from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
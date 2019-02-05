pip install flask
pip install flask-wtf
pip install flask-sqlalchemy

# Flask

http://flask.pocoo.org/

# Start app

```
set FLASK_APP=flaskblog.py
set FLASK_DEBUG=1 <----- to run changes without restarting the web server
flask run

or

# python run.py
```

URL: http://localhost:5000/

# Create secret

https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key

```
# in python interpreter
import secrets
secrets.token_hex(16)
```

# Create Database

In python interpreter

```
from flaskblog import db

# this will create a site.db
db.create_all()

# Create a user
user_1 = User(username='Katrin', email='katrin@gmail.com', password='password')

# Add to db
db.session.add(user_1)

# Commit changes
db.session.commit()

# Query all users
User.query.all()

User.query.first()
User.query.filter_by(username='Katrin').all()

user = User.query.first()
user.id

user = User.query.get(1)

# Create some posts
post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
post_2 = Post(title='Blog 2', content='Secodn Post Content!', user_id=user.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()

post = Post.query.first()
post.user_id

# Use the backref to access the user data
post.author
User('Katrin', 'katrin@gmail.com', 'defaul.jpg')

# remove all data from database
db.drop_all()

```

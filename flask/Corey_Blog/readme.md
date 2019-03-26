pip install flask
pip install flask-wtf
pip install flask-sqlalchemy

https://flask-bcrypt.readthedocs.io/en/latest/
pip install flask-bcrypt

pip install flask-login

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

# Hashing passwords

```
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# hash is always different even for the same password
bcrypt.generate_password_hash('testing')
b'$2b$12$QlmXiwoXwVXKTxGVI4FiweB8jq4L3SQj4.YfXpEagDYLhjvX1c/.W'

bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$YH386dwHKupg7It8whRuyuXYRNbuQ0XLL05B2PCPidDf4cVgXY.yC'

bcrypt.check_password_hash(hash_pw, 'testing')
True
```

# Errors

TypeError: 'DataRequired' object is not iterable

https://stackoverflow.com/questions/22310366/typeerror-required-object-is-not-iterable-flask-wtf-forms

## Not using _data_ in form.title.data

```
Error binding parameter 0 - probably unsupported type. [SQL: 'INSERT INTO post (title, date_posted, content, user_id) VALUES (?, ?, ?, ?)'] [parameters: (<wtforms.fields.core.StringField object at 0x000001433F86CF28>, '2019-02-17 18:50:43.246248', <wtforms.fields.simple.TextAreaField object at 0x000001433F86C908>, 1)]
```

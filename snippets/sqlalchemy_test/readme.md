# SQLAlchemy ORM tutorial

Sqlite is already part of python.

When logging is enabled all generated SQL will appear in the console.

`Engine` is the core interface to the database

# Tips and Tricks

```
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import inspect
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

db_url = {'drivername': 'postgres',
          'username': 'postgres',
          'password': 'postgres',
          'host': '192.168.99.100',
          'port': 5432}

engine = create_engine(URL(**db_url))
Base = declarative_base()

def create_table(name, cols):
    Base.metadata.reflect(engine)
    if name in Base.metadata.tables: return

    table = type(name, (Base,), cols)
    table.__table__.create(bind=engine)

create_table('Table1', {
             '__tablename__': 'Table1',
             'id': Column(Integer, primary_key=True),
             'name': Column(String)})

create_table('Table2', {
             '__tablename__': 'Table2',
             'id': Column(Integer, primary_key=True),
             'key': Column(String),
             'val': Column(String)})

inspector = inspect(engine)
for _t in inspector.get_table_names():
    print(_t)
```

# Some Links

https://www.pythonsheets.com/notes/python-sqlalchemy.html

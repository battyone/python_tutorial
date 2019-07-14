# %%
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'''<User(name"{self.name}",
            fullname="{self.fullname}",
            nickname="{self.nickname}"'''


# echo flag is a shortcut to enable logging
engine = create_engine('sqlite:///:memory:', echo=True)


def create_table(name, cols):
    Base.metadata.reflect(engine)
    if name in Base.metadata.tables:
        return

    table = type(name, (Base,), cols)
    table.__table__.create(bind=engine)


create_table('Table1', {
             '__tablename__': 'Table1',
             'id': Column(Integer, primary_key=True),
             'name': Column(String)})


Base.metadata.create_all(engine)

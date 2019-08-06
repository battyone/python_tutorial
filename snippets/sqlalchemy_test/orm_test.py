# %%
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

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
            nickname="{self.nickname}>"'''


print(User.__tablename__)

# echo flag is a shortcut to enable logging
engine = create_engine('sqlite:///:memory:', echo=True)

# generate the create table commands
# Base.metadata.create_all(engine)

a_user = User(name='Katrin', fullname='Katrin Henning', nickname='bubi')
# print(a_user.id)

# %%
Session = sessionmaker(bind=engine)
session = Session()

# no SQL will be issued
session.add(a_user)






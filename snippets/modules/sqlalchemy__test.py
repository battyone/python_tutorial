# https://docs.sqlalchemy.org/en/13/orm/tutorial.html

# %%
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sqlalchemy
print(sqlalchemy.__version__)


# %%
engine = create_engine('sqlite:///:memory:', echo=True)

# %%
# Declare a Mapping

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'''
            <User(name={self.name}, fullname={self.fullname}, 
            nickname='{self.nickname}')>
            '''
#%%
User.__table__

#%%
Base.metadata.create_all(engine)

#%%
# Create an Instance of the Mapped Class

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
print(repr(ed_user))
print(str(ed_user.id))

#%%
# Creating a Session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

#%%
session = Session()

# Adding and Updating Objects
session.add(ed_user)

#%%
our_user = session.query(User).filter_by(name='ed').first() 
print(repr(our_user))
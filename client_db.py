from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine(r'sqlite:///C:\Users\пользователь\Desktop\sqlite\sql_client.sqlite', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class MessageHistory(Base):
    __tablename__='MessageHistory'
    msh_id=Column(Integer, primary_key=True)
    msg_id = Column(Integer, ForeignKey('ContactList.id'))
    Msg = Column(String())
    def __init__(self,message):
        self.Msg=message
    def __repr__(self):
        return "Message {}".format(self.Msg)

class ContactList(Base):
    __tablename__='ContactList'
    id = Column(Integer, primary_key=True)
    contact_name = Column(String)
    def __init__(self,clients):
        self.contact_name = clients
    def __repr__(self):
        return "Contact name {}".format(self.contact_name)

class LogIn(Base):
    __tablename__='LogIn'
    id=Column(Integer, primary_key=True)
    Login_name=Column(String)
    Password=Column(String)
    def __init__(self,login,password):
        self.Login_name=login
        self.Password=password
    def __repr__(self):
        return'LoginName {}'.format(self.Login_name)

Base.metadata.create_all(engine)
session=Session()

#conn = engine.connect()
#trans = conn.begin()
#conn.execute('DELETE FROM "LogIn"')
#trans.commit()

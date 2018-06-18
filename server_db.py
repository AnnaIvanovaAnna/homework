from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, MetaData, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime,time

engine = create_engine(r'sqlite:///C:\Users\пользователь\Desktop\sqlite\sql.sqlite', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Client(Base):
    __tablename__='Client'
    client_id = Column(Integer, primary_key=True)
    LogIn = Column(String(35))
    Information = Column(String)
    def __init__(self,name,information):
        self.LogIn=name
        self.Information=information
    def __repr__(self):
        return "Client {}".format(self.LogIn)

class ContactList(Base):
    __tablename__='ContactList'
    id = Column(Integer, primary_key=True)
    clientID = Column(Integer, ForeignKey('Client.client_id'))
    contactID = Column(Integer, ForeignKey('Client.client_id'))
    
    def __init__(self,clientid,clients):
        self.clientID = clientid
        self.contactID = clients
    def __repr__(self):
        return "Client ID {} | Contact ID {}".format(self.clientID,self.contactID)

class ClientHistory(Base):
    __tablename__='ClientHistory'
    id = Column(Integer, primary_key=True)
    Time = Column(String)
    IP_address = Column(String)
    def __init__(self,time,ip):
        self.Time = time
        self.IP_address = ip

Base.metadata.create_all(engine)
session=Session()

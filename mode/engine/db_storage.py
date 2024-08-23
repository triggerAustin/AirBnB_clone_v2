#!usr/bin/python3
"""Engine Dbstorage"""
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """class definition for dbstorage cls"""
    __engine__ = None
    __storage__ = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')
        # syntax dialect+driver://user:pwd@host:port/db
        head = f'mysql://{user}:{password}@{host}/{database}'
        self.__engine = create_engine(head, pool_pre_ping=True)

        # if HBNB_ENV == test drop all tables
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all cls from db, or specified one"""
        objects_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(User, State, City, Amenity, Place, Review).all()
        for obj in objs:
            key = f'{obj.__class__.__name__}.{obj.id}'
            objects_dict[key] = obj
        return objects_dict
    def new(self, obj):
        """add obj to db"""
        self.__session.add(obj)
    def save(self):
        """commit all changes of current db session"""
        self.__session.commit()
    def delete(self, obj=None):
        """delete from db session obj if not none"""
        if obj != None:
            self.__session.delete(obj)
    def reload(self):
        """"create all tables in db and current db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

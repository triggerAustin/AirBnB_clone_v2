#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """instantiates a new model"""
        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        elif kwargs:
             for key, value in kwargs.items():
                 if key != '__class__':
                     if 'id' not in kwargs.keys():
                         key_value = str(uuid.uuid4())
                         key_id = 'id'
                         setattr(self, key_id, key_value)
                     if 'updated_at' not in kwargs.keys():
                         setattr(self, 'updated_at', datetime.utcnow())
                     if 'created_at' not in kwargs.keys():
                         setattr(self, 'created_at', datetime.utcnow())
                     if key in ['updated_at', 'created_at']:
                         setattr(self, key, datetime.strptime(value,
                                                              '%Y-%m-%dT%H:%M:%S.%f'))
                     else:
                         if '\\"' in value:
                             value = eval(value)
                         setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

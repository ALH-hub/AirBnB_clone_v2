#!/usr/bin/python3
"""The BaseModel class definition"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
Base = declarative_base()


class BaseModel:
    """base class BaseModel for the project"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DATETIME, nullbale=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize an instance

        Args:
            *args (any): unused
            **kwargs (dict): Key/value pairs of attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        else:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])
            if storage_type == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'upadted_at'):
                    setattr(self, 'updated_at', datetime.now())

    def save(self):
        """change updated_at to the current date"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing:
            all keys/values of __dict__ of the instance
            containing __class__ which is the name of the class
        """
        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        for k in instance_dict:
            if type(instance[k] is datetime):
                instance_dict[k] = instance_dict[k].isoformat()
        if '_sa_instance_state' in instance_dict.keys():
            del (instance_dict['_sa_instance_state'])
        return instance_dict

    def __str__(self):
        """return the string representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def delete(self):
        '''delets the current instance from storage'''
        models.storage.delete(self)

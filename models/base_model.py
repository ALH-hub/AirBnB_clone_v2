#!/usr/bin/python3
"""The BaseModel class definition"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String



Base = declarative_base()


class BaseModel:
    """base class BaseModel for the project

    Attributes:
    id (sqlalchemy String): primary key
    created_at (sqlalchemy DateTime): the date created at
    updated_at (sqlalchemy DateTime): the time lastly modified
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize an instance

        Args:
            *args (any): unused
            **kwargs (dict): Key/value pairs of attributes
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, form)
                if k != "__class__":
                    setattr(self, k, v)
            

    def save(self):
        """change updated_at to the current date"""
        self.updated_at = datetime.today()
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
        instance_dict.pop("_sa_instance_state")
        return instance_dict
    
    def delete(self):
        """delete the current instance from storage"""
        models.storage.delete(self)

    def __str__(self):
        """return the string representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

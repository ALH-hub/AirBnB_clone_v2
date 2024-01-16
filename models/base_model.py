#!/usr/bin/python3
"""The BaseModel class definition"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """base class BaseModel for the project"""
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
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """change updated_at to the current date"""
        self.updated_at = datetime.today()
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
        return instance_dict

    def __str__(self):
        """return the string representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

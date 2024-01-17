#!/usr/bin/python3
"""define FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances
    to a JSON file and deserializes JSON file
    to instancesin python.
    local storage in other words

    Attributes:
        __file_path (str): string - path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """__objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to _file_path"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize _file_path to an object"""
        try:
            with open(FileStorage.__file_path) as file:
                ldict = json.load(file)
                for obj in ldict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Delete obj from __objects."""
        if obj is None:
            return
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        my_dict = self.__objects
        del my_dict[obj_key]

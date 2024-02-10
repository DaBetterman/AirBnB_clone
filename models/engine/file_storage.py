#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add an object to the storage dictionary."""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = {key: value.to_dict()
                        for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                objects_dict = json.load(file)
                for obj_id, obj_dict in objects_dict.items():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    obj_instance = eval(class_name)(**obj_dict)
                    FileStorage.__objects[obj_id] = obj_instance
        except FileNotFoundError:
            pass

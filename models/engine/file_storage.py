#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Handles serialization and
    deserialization of objects
    to and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary.
        """
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the objects dictionary to a JSON file.
        """
        all_objs = FileStorage.__objects
        serialized_objs = {}
        for obj in all_objs.keys():
            serialized_objs[obj] = all_objs[obj].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Reloads the objects dictionary from the JSON file.
        If the file exists, deserializes
        the data and updates the dictionary.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    serialized_objs = json.load(file)

                    for key, values in serialized_objs.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

#!/usr/bin/python3
from datetime import datetime
import models
import uuid


class BaseModel(object):
    """
    BaseModel class providing common attributes and methods.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Date and time of instance creation.
        updated_at (datetime): Date and time of last instance update.
    """
    def __init__(self, *args, **kwargs):
        """
            Initializes a new instance of the BaseModel class.

        Args:
            *args: Not used.
            **kwargs: Used to initialize instance attributes.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key,
                                datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation
        of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute
        with the current date and time.
        """
        self.updated_at = datetime.now()
        # storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance
        to a dictionary for serialization.

        Returns:
            dict: A dictionary containing
            the class name and attributes of the instance.
        """
        object_dict = self.__dict__.copy()
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        object_dict['__class__'] = self.__class__.__name__
        return object_dict

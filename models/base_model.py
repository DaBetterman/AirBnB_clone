#!/usr/bin/env python3
from datetime import datetime
import uuid


class BaseModel(object):
    """
    This is the BaseModel class, providing
    a common set of attributes
    and methods for other classes.

    Attributes:
        id (str): A unique identifier generated
        using uuid.uuid4().
        created_at (datetime): The date and time
        when an instance is created.
        updated_at (datetime): The date and time
        when an instance is created or updated.

    Methods:
        __init__(): Initializes a new instance
        of the BaseModel class.
        __str__(): Returns a string representation
        of the BaseModel instance.
        save(): Updates the 'updated_at' attribute
        with the current date and time.
        to_dict(): Converts the BaseModel instance
        to a dictionary for serialization.
    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

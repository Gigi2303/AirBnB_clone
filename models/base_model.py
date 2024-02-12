#!/usr/bin/python3
""" The base_model module
Contains the basemodel class
with all common attributes or methods
for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ This reps our  base class
    It holds all attributes and mtds
    to be inherited by other classes
    Methods:
    __init__()
    """

    available = 0

    def __init__(self, *args, **kwargs):
        if args:
            self.my_number = args
            self.name = args
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            BaseModel.available = 1
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            models.storage.new(self)

    def __str__(self):
        """ String magic method
        To return a string representation of BaseModel
        """
        return "[" + self.__class__.__name__ + "] " + \
               "(" + self.id + ") " + str(self.__dict__)

    def save(self):
        """ Save method
        It will update the public instance attribute updated_at
        """
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        """to_dict method
        It will return a dictionary rep
        of the class
        """
        self.__dict__.pop('cmdqueue', None)
        self.__dict__.pop('stdin', None)
        self.__dict__.pop('completekey', None)
        self.__dict__.pop('stdout', None)
        my_dict = self.__dict__
        my_dict['created_at'] = str(self.created_at)
        my_dict['updated_at'] = str(self.updated_at)
        if not self.available:
            my_dict["__class__"] = self.__class__.__name__

        return my_dict

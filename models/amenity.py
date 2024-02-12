#!/usr/bin/python3

""" The amenity module - has the Amenity class which
inherits from BaseModel

It has an attribute, name, the name of the amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The Amenity class
    It has attributes of amenity
    """
    name = ""

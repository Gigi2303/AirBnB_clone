#!/usr/bin/python3
""" City module - has the City class which inherits from BaseModel

It has attributes, name, and state_id
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ The City class
    Has attributes of the city
    """
    state_id = ""
    name = ""

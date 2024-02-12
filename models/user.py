#!/usr/bin/python3

""" The user module
It has the User class that inherits from BaseModel
It has features such as email, password, first_name,
last_name
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class
    It has the features of a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

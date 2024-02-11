#!/usr/bin/python3
""" The state module - contains the State class which
inherits from BaseModel

It has an attribute, name, the name of the state
"""
from base_model import BaseModel


class State(BaseModel):
    """ The State class
    It has features of the state
    """
    name = ""

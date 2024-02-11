#!/usr/bin/python3
""" Review module - has the Review class that inherits from BaseModel

It has attributes, place_id, user_id, text
"""
from base_model import BaseModel


class Review(BaseModel):
    """ The Review class
    It has attributes of the review
    """
    place_id = ""
    user_id = ""
    text = ""

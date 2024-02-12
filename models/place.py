#!/usr/bin/python3
""" Place module - has the Place class which inherits from BaseModel

It has attributes city_id, user_id, name, description,
number_rooms, number_bathrooms, max_guest, price_by_night,
latitude, longitude, amenity_ids
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ The Place class
    It has attributes of a place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""

#!/usr/bin/python3
"""This module contains the subclass Place, of the class BaseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines attributes Place class and its methods
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_gust = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """instantiation method of the Place class
        """
        super().__init__(*args, **kwargs)

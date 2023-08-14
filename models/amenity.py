#!/usr/bin/python3
"""This module contains the subclass Amenity, of the class BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines attributes of Amenity class and its methods
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """instantiation method of the Amenity class
        """
        super().__init__(*args, **kwargs)

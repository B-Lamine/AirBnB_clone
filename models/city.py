#!/usr/bin/python3
"""This module contains the subclass City, of the class BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """This class defines attributes of City class and its methods
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """instantiation method of the City class
        """
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""This module contains the subclass Review, of the class BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines attributes of Review class and its methods
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """instantiation method of the Review class
        """
        super().__init__(*args, **kwargs)

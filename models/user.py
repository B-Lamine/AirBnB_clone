#!/usr/bin/python3
"""This module contains the subclass User, of the class BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """This class defines attributes of User class and its methods
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """instantiation method of the User class
        """
        super().__init__(*args, **kwargs)

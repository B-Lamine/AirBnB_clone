#!/usr/bin/python3
"""This module contains the subclass State, of the class BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """This class defines attributes of State class and its methods
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """instantiation method of the State class
        """
        super().__init__(*args, **kwargs)

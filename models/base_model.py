#!/usr/bin/python3
"""This module contains the class: BaseModel.
"""


import datetime
from models import storage
import uuid


class BaseModel():
    """Base class:
        - sets randomly generated id for instances
        - saved creation and update datetime.
    """
    def __init__(self, *args, **kwargs):
        """instantiation method for the BaseModel class
        """
        datetime_str = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.datetime.\
                                         strptime(value, datetime_str)
                    continue
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """string representation for the BaseModel instances.
        """
        return "[" + self.__class__.__name__ + "] (" + self.id + ") " +\
            str(self.__dict__)

    def save(self):
        """record update datetime.
        """
        storage.save()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """get dictionary representation of an instance.
        """
        tmp_dict = self.__dict__.copy()
        tmp_dict['created_at'] = self.created_at.isoformat()
        tmp_dict['updated_at'] = self.updated_at.isoformat()
        tmp_dict['__class__'] = self.__class__.__name__
        return tmp_dict

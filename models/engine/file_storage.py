#!/usr/bin/python3
"""this module contains the class: FileStorage.
"""


import json
import os


class FileStorage():
    """a class for handling data storage: json serialization/deserialization,
        saving and loading to storage file.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return dictionary of all current objects (saved and unsaved).
        """
        return type(self).__objects

    def new(self, obj):
        """add a new object to the dictionary.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        type(self).__objects[key] = obj.to_dict()

    def save(self):
        """save new objects to storage file.
        """
        json_str = json.dumps(type(self).__objects)
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """reload saved objects from storage file.
        """
        if os.path.isfile(type(self).__file_path):
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                json_str = f.read()
            type(self).__objects = json.loads(json_str)

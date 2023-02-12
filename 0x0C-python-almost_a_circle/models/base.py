#!/usr/bin/python3

"""The Base Class"""
import json


class Base():
    """
    This class will be the `base` of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing id
        Args:
            id(int): number of instance class.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation of
        list_dictionaries.
        Args:
            list_dictionaries: list dictionary.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation
        of list_objs to a file.
        Args:
            list_objs: is a list of instances who inherits of Base - example:
            list of Rectangle or list of Square instances.
            cls: Class
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")

            list_dicts = [o.to_dictionary() for o in list_objs]
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the 
        JSON string representation.
        Args:
            json_string: string representing a list of dictionaries.
        """
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all atrributes
        already set.
        Args:
            **dictionary: double pointer to a dictionary
            list of Rectangle or list of Square instances.
            cls: Class
        """

        # with open(json_string) as f:
        #     if json_string is None or json_string == []:
        #         return "[]"
        #     else:
        #         return json.load(f)

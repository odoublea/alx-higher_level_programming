#!/usr/bin/python3

"""The Base Class"""
import json
import csv


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
        with open(filename, "w", encoding="utf-8") as json_file:
            if list_objs is None:
                json_file.write("[]")

            list_dicts = [o.to_dictionary() for o in list_objs]
            json_file.write(cls.to_json_string(list_dicts))

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
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances from a file.
        Reads from `<cls.__name__>.json`.
        Args:
            cls:
        """
        filename = str(cls.__name__) + ".json"
        with open(filename, "r") as json_file:
            try:
                with open(filename, "r", encoding="utf-8") as json_file:
                    list_dicts = cls.from_json_string(json_file.read())
                    return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        if cls.__name__ == 'Rectangle':
            filename = cls.__name__ + ".csv"
            fields = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == 'Square':
            filename = cls.__name__ + ".csv"
            fields = ['id', 'size', 'x', 'y']

        with open(filename, "w", newline='') as csv_file:
            if list_objs is None or list_objs == []:
                writer = csv_file.write("[]")

            writer = csv.DictWriter(filename, fieldnames=fields)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

            # csv_file.write(cls.to_json_string(list_dicts))
    
    # @classmethod
    # def load_to_file_csv(cls, list_objs):

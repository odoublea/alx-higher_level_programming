#!/usr/bin/python3

"""The Base Class"""


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

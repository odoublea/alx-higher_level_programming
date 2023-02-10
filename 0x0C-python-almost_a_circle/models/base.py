#!/usr/bin/python3

"""The Base Class"""


class Base():
    """
    This class will be the `base` of all other classes in this project.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        __nb_objects += 1
        self.id = id

u = Base(1)
print(u.id)
print(Base.__nb_objects)

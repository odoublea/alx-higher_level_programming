#!/usr/bin/python3

"""This script contain a class Square."""


class Square:
    """This is a class with a private size attribute
    and an instation of zero.
    Attributes:
        size -- width of the Square

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square

        Args:
            size(int): size of the square

        Exception:
            ValueError: size must be greater than zero
            TypeError: size must be an integer

        """
        self.__size = size
        self.__position = position
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    @property
    def size(self):
        """Get the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size."""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

    @property
    def position(self):
        """Get the attribute for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set value attribute for position.


        Exception:
            TypeError: position must be a tuple of 2 positive integers.

        """
        if not (isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            self.__position = value

    def my_print(self):
        """Print square hashes."""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            for j in range(self.position[0]):
                print(' ', end="")
            for j in range(self.size):
                print("{}".format('#'), end="")
            print()

    def __str__(self):
        if self.__size != 0:
            for i in range(self.position[1]):
                print()

        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            if i != self.size - 1:
                print()
        return("")

#!/usr/bin/python3
"""Class rectangle that inherits from BaseGeometry is Defined."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle is represented using BaseGeometry."""

    def __init__(self, width, height):
        """new rectangle Initializer.

        Args:
            width (int): The new rectangles width.
            height (int): The new rectangles height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of the rectangle is returned."""
        return self.__width * self.__height

    def __str__(self):
        """The print() and str () representation of a rectangle is returned."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

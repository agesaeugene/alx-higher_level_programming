#!/usr/bin/python3
"""Class rectangle that inherits from BaseGeometry is defined."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
       """Uses BaseGeometry to represent a triangle."""

       def __init__(self, width, height):
            """New rectangle initializer.

            Args:
                width (int): The new rectangles width.
                height (int): The new rectangles height.
            """
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height

#!/usr/bin/python3
"""Class for BaseGeometry is Defined."""

class BaseGeometry:
    """BaseGeometry representation."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A parameter is validated as an integer.

        Args:
            name (str): The parameters name.
            value (int): Parameter to be validated.
        Raises:
            TypeError: When value is not an integer.
            ValueError: When value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

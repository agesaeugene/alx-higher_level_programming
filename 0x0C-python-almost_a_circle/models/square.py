#!/usr/bin/python3
"""A square class is defined"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square is represnted."""

    def __init__(self, size, x=0, y=0, id=None):
        """New square initializer.

        Args:
            size (int): The new squares size.
            x (int): The new squares x coordinate.
            y (int): The new squares y coordinate.
            id (int): The new squares identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The square size is set."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """The square is updated

        Args:
            *args (ints): Attributes for new values.
                - 1st - The first parameter is the id property.
                - 2nd argument -Size property is represented by the second parameter.
                - 3rd argument symbolizes the x attributes.
                - 4th argument symbolizes the y attribute.
            **kwargs (dict): New value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """The dictionary representation of a square is returned"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """The print() and str() representation of a square is returned"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

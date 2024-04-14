#!/usr/bin/python3
"""Class student is defined."""


class Student:
    """Correspondent for a student."""

    def __init__(self, first_name, last_name, age):
        """New student initializer.

        Args:
            first_name (str): Students first name.
            last_name (str): Students last name.
            age (int): Students age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation for a Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

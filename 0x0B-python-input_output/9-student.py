#!/usr/bin/python3
"""Class student is defined."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """new Student function is initialized.

        Args:
            first_name (str): Students first name.
            last_name (str): Students last name.
            age (int): Students age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets the dictionary representation of the Student."""
        return self.__dict__

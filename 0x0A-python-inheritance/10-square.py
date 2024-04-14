#!/usr/bin/bash
"""Subclass rectangle class square defined."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square representation."""

    def __init__(self, size):
    """New square initializer.

    Args:
        size (int): The new square size.
    """
    self.inter_validator("size", size)
    super().__init__(size, size)
    self.__size = size

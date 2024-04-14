#!/usr/bin/python3
"""file writting function is defined"""

def write_file(filename="", text=""):
    """A string is written to a (UTF8) text file returns number of characters written.

    Args:
        filename (str): Filename to write to
        text (str): Text to be written to a file
        
    Returns:
        Number of characters written to the file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)

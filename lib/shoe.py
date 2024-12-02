#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use a private attribute for size
        self.size = size  # Use the property setter for validation
        self.condition = "Old"  # Default condition when the shoe is created

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"  # Set condition to "New" after cobbling
        print("Your shoe is as good as new!")
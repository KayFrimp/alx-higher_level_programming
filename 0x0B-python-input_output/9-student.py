#!/usr/bin/python3
"""Student class module"""


class Student:
    """A class representing a student

    Attributes:
        first_name (str): First name of student
        last_name (str): Last name of student
        age (int): Age of student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation
           of Student

           Returns:
              JSON: JSON serialized object
        """

        return vars(self)

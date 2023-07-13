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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation
           of Student

        Args:
            attrs (list): list of strings

        Returns:
            JSON: JSON serialized object
        """

        json_obj = vars(self)
        if type(attrs) is list and \
           all([isinstance(val, str) for val in attrs]):

            filtered_json_obj = {}
            for i in range(len(attrs)):
                for element in json_obj:
                    if attrs[i] == element:
                        filtered_json_obj[element] = json_obj[element]
            return filtered_json_obj
        return json_obj

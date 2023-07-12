#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """Creates Object from JSON file"""

    with open(filename) as jsonFile:
        return json.loads(jsonFile.read())

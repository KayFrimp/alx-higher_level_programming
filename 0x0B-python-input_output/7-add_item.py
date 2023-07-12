#!/usr/bin/python3
"""Script module adds all arguments to a python list,
   and saves them to a file"""
import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


python_list = []
filename = "add_item.json"
if exists(filename):
    python_list = load_from_json_file(filename)

for argv in sys.argv[1:]:
    python_list.append(argv)
save_to_json_file(python_list, filename)

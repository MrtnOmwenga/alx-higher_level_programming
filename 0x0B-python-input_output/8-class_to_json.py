#!/usr/bin/python3
"""
Converts class to json obj
"""


import json


def class_to_json(obj):
    """
    Convert obj to jason
    """
    return(json.dumps(obj.__dict__))

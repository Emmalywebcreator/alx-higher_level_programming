#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class inherited from a_class; otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

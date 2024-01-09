#!/usr/bin/python3
"""Defines and object attributes lookup function."""
def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return (dir(obj))

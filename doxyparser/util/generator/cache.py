"""
MIT License

Copyright (c) 2020 Collin Brooks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This module contains cache helpers for the different xsd elements doxyparser works with
"""
from .types import Group, Type, Element

group_cache = {}
type_cache = {}
element_cache = []


def get_group_cache():
    """Get the group cache.

    Returns:
        dict: Group cache data keyed by group name.
    """
    return group_cache


def get_type_cache():
    """Get the type cache.

    Returns:
        dict: Type cache data keyed by type name.
    """
    return type_cache


def get_element_cache():
    """Get the element cache.

    Returns:
        list: List of element data cache
    """
    return element_cache


def get_group(group_name):
    """Get the Group from cache for the group with the given name.

    Args:
        group_name (str): The name of the group to obtain cache data for.

    Returns:
        Group|None: The Group object for the group with the given name or
            none if it does not exist.
    """
    return group_cache.get(group_name)


def get_type(type_name):
    """Get the Type from cache for the type with the given name.

    Args:
        type_name (str): The name of the type to obtain cache data for.

    Returns:
        Type|None: The Type object for the type with the given name or none
            if it does not exist.
    """
    return type_cache.get(type_name)


def add_group(group):
    """Add the given group to cache

    Args:
        group (XsdGroup): The XsdGroup to add to cache
    """
    group_cache[group.name] = Group(group)


def add_type(node_type):
    """Add the given type to cache

    Args:
        group (XsdType): The XsdType to add to cache
    """
    type_cache[node_type.name] = Type(node_type)


def add_element(element):
    """Add the given element to cache

    Args:
        group (XsdElement): The XsdElement to add to cache
    """
    element_cache.append(Element(
        element,
        get_type(element.type.name)
    ))

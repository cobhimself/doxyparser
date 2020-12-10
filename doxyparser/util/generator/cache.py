group_cache = {}
type_cache = {}
element_cache = []

def get_group_cache():
    return group_cache

def get_type_cache():
    return type_cache

def get_element_cache():
    return element_cache

def get_group(group_name):
    return group_cache.get(group_name)

def get_type(type_name):
    return type_cache.get(type_name)

def add_group(group):
    from doxyparser.util.generator.group import Group
    group_cache[group.name] = Group(group)

def add_type(node_type):
    from doxyparser.util.generator.type import Type
    type_cache[node_type.name] = Type(node_type)

def add_element(element):
    from doxyparser.util.generator.element import Element
    element_cache.append(Element(
        element,
        get_type(element.type.name)
    ))
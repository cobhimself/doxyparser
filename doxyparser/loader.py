from doxyparser import TAG_MAP
from importlib import import_module

_cache = {}


def get_tag_class(xsd, tag):
    if (xsd, tag) not in _cache:
        path = TAG_MAP[xsd][tag]
        parts = path.split('.')
        final = parts.pop()
        package = '.'.join(parts)

        module = import_module(package)
        _cache[(xsd, tag)] = getattr(module, final)

    return _cache[(xsd, tag)]


def get_tag_class_instance(xsd, tag, tree):
    tag = get_tag_class(xsd, tag)
    return tag(tree)

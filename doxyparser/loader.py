import xml.etree.ElementTree as ET
from doxyparser import TAG_MAP
from importlib import import_module

class Loader():
    def __init__(self, xml_dir):
        self._xml_dir = xml_dir
        self._cache = {}

    def load_index(self):
        return ET.parse(self._xml_dir + '/index.xml')
    
    def load_tag_class(self, xsd, tag):
        if (xsd, tag) not in self._cache:
            path = TAG_MAP[xsd][tag]
            parts = path.split('.')
            final = parts.pop()
            package = '.'.join(parts)

            module = import_module(package)

            self._cache[(xsd, tag)] = getattr(module, final)

        return self._cache[(xsd, tag)]

    def load_refid(self, refid):
        tree = ET.parse(self._xml_dir + '/' + refid + '.xml')
        return tree.getroot()


import xml.etree.ElementTree as ET
from doxyparser.index.types.doxygenindex import DoxygenIndex
from .loader import get_node_from_tree


class Parser:
    def __init__(self, xml_dir):
        self._xml_dir = xml_dir

    def parse_index(self):
        tree = ET.parse(self._xml_dir + '/index.xml')
        root = tree.getroot()
        return get_node_from_tree(
            'index',
            root
        )


from doxyparser.index.types.doxygenindex import DoxygenIndex
from .loader import Loader
from doxyparser import TAG_MAP

class Parser:
    def __init__(self, loader):
        self._loader = loader

    def parse_index(self):
        tree = self._loader.load_index()
        root = tree.getroot()
        return self.get_node_from_tree(
            'index',
            root
        )
    
    def parser_from_ref_id(self, refid, xsd='compound'):
        root = self._loader.load_refid(refid)
        return self.get_node_from_tree(
            xsd,
            root
        )

    def get_tag_class(self, xsd, tag):
        return self._loader.load_tag_class(xsd, tag)


    def get_tag_class_instance(self, xsd, tag, tree):
        tag = self.get_tag_class(xsd, tag)
        return tag(tree, parser = self)


    def get_node_from_tree(self, xsd, tree):
        return self.get_tag_class_instance(xsd, tree.tag, tree)
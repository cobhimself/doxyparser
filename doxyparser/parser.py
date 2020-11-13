
from doxyparser.index.types.doxygenindex import DoxygenIndex
from .loader import Loader
from doxyparser import TAG_MAP

class Parser:
    def __init__(self, loader):
        self._loader = loader

    def parse_index(self):
        tree = self._loader.load_index()
        return self.get_node_from_tree(
            'index',
            tree
        )
    
    def parser_ref_id(self, refid, xsd='compound'):
        tree = self._loader.load_refid(refid)
        return self.get_node_from_tree(
            xsd,
            tree
        )

    def get_tag_class(self, xsd, tag):
        return self._loader.load_tag_class(xsd, tag)


    def get_tag_class_instance(self, xsd, tag, tree):
        tag = self.get_tag_class(xsd, tag)
        return tag(tree, self)


    def get_node_from_tree(self, xsd, tree):
        root = tree.getroot()
        return self.get_tag_class_instance(xsd, root.tag, root)
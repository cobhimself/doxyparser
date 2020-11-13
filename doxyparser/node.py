import importlib
import builtins
import sys

"""
Super class used to represent doxy xml Elements
"""


class Node:
    def __init__(self, node, parser, tag=None):
        """Initialize a Node (object representation of an xml data tree)

        Args:
            node (xml.etree.ElementTree.Element): The Element this
                Node references
            tag (string, optional): The tag this node represents. If
                provided, a check is made to to confirm.
                Defaults to None.

        Raises:
            Exception: Raised if a tag name is provided and it doesn't
                match with the Element's tag
        """
        if (None == parser):
            raise Exception(
                'The node class cannot be instantiated without a parser!'
            )

        if (tag != None and node.tag != tag):
            raise Exception(
                'Invalid tag name ('
                + node.tag
                + '). Expected '
                + tag
            )
        self._node = node
        self._child_cache = {}
        self._parser = parser

    def get(self, key, default=None):
        return self._node.get(key, default)

    def find(self, key, default=None):
        """Finds the first subelement matching match.

        Args:
            key (string): may be a tag name or path
            default (mixed, optional): the default return value if key
                is not found. Defaults to None.

        Returns:
            Element|None: Returns an Element instance or none if
                not found
        """
        child = self._node.find(key)

        if child == None:
            return default

        return child

    def get_text(self, key, default=None):
        """Get the text from the first element matching key.

        Args:
            key (string): May be a tag name or path
            default (mixed, optional): Returned if key not found. Defaults to None.

        Returns:
            string|mixed: If the Element with key is found, its text is
                returned. Otherwise the default.
        """
        found = self.find(key)
        if found == None:
            return default
        else:
            return found.text

    def iter(self, key):
        return self._node.iterfind(key)

    def get_bool(self, attr):
        value = self.get(attr)
        return value == 'yes'

    def get_children(self, xsd, tag, path=None):
        xpath = tag + ('' if path == None else path)
        if xpath not in self._child_cache.keys():
            childClass = self._parser.get_tag_class(xsd, tag)

            children = []
            for child in self.iter(xpath):
                children.append(childClass(child, self._parser))

            self._child_cache[xpath] = children

        return self._child_cache[xpath]

    def get_child(self, key, node_type, path=None):
        children = self.get_children(key, node_type, path)
        if children != None:
            return children[0]

        return None

    def debug_dump(self):
        self._node

    def load_ref(self, xsd, refid):
        return self._parser.parser_from_ref_id(xsd, refid)

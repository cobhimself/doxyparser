"""
Super class for all xsd:group types
"""
from .node import Node


class NodeGroup(Node):

    def __init__(self, node, parser):
        super().__init__(node, parser)
        self._inner = None

    def get_inner(self):
        self._inner = self._node.items()[0]

    def get_inner_tag(self):
        return self.get_inner().tag()

    def get_inner_element(self):
        """Get the inner element of this group.

        Only one of the elements inside <xsd:choice> can be inside this
        group. Use get_inner_tag() to obtain the tag type of the
        inner element.

        Returns:
            mixed: Returns the element matching the type returned by
            get_inner_tag
        """
        method_name = 'get_' + self.get_inner_tag()
        method = getattr(self, method_name, lambda: "Invalid inner element")

        return method()

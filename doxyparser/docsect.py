"""
Base model for all DocSect# types
"""
from .node import Node


class DocSect(Node):
    def __init__(self, node, parser, level):
        super().__init__(node, parser)
        self._level = level

    def get_title(self):
        return self.get_text('title')

    def get_paras(self):
        return self.get_children('para', 'DocPara')

    def get_internals(self):
        return self.get_children('internal', 'DocInternalS' + self._level)

    def get_id(self):
        return self.get('id')

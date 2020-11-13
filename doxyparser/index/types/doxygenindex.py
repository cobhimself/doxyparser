#!/usr/bin/env python3
"""
Model representation of a doxygenindex Element from doxygen

<xsd:complexType name="DoxygenType">
  <xsd:sequence>
    <xsd:element name="compound" type="CompoundType" minOccurs="0" maxOccurs="unbounded"/>
  </xsd:sequence>
  <xsd:attribute name="version" type="xsd:string" use="required"/>
  <xsd:attribute ref="xml:lang" use="required"/>
</xsd:complexType>
"""
from ...node import Node
from xml.etree.ElementTree import Element
from typing import Optional
from .compound import Compound


class DoxygenIndex(Node):
    def __init__(self, node):
        super().__init__(node)

    def get_compounds(
        self,
        kind: Optional[str] = None
    ) -> dict[Compound]:
        path = '' if kind == None else '/[@kind="' + kind + '"]'
        return self.get_children(
            xsd='index',
            tag='compound',
            path=path
        )

    def get_classes(self) -> dict[Element]:
        return self.get_compounds('class')

    def get_interfaces(self):
        return self.get_compounds('interface')

    def get_namespaces(self):
        return self.get_compounds('namespace')

    def get_files(self):
        return self.get_compounds('file')

    def get_dirs(self):
        return self.get_compounds('dir')

    def get_version(self):
        return self.get('version')

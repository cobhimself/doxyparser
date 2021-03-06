#!/usr/bin/env python3
"""
Model representation of a refType Element from doxygen

<xsd:complexType name="linkedTextType" mixed="true">
  <xsd:sequence>
  <xsd:element name="ref" type="refTextType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class LinkedText(Node):
    def __init__(self, node):
        super.__init__(node)
    
    def get_refs(self):
        return self.get_children('ref', 'reftext')
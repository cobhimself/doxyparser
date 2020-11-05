#!/usr/bin/env python3
"""
Model representation of a docTocListType from doxygen

<xsd:complexType name="docTocListType">
  <xsd:sequence>
    <xsd:element name="tocitem" type="docTocItemType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocTocList(Node):
  def __init__(self, node):
    super.__init__(node)
  
  def get_tocitems(self):
    return self.get_children('tocitem', 'DocTocItem')
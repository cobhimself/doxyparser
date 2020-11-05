#!/usr/bin/env python3
"""
Model representation of a docListType from doxygen

<xsd:complexType name="docListType">
  <xsd:sequence>
    <xsd:element name="listitem" type="docListItemType" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocList(Node):
  def __init__(self, node):
      super.__init__(node)

  def get_listitems(self):
    return self.get_children('listitems', 'DocListItem')
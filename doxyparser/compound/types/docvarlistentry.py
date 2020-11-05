#!/usr/bin/env python3
"""
Model representation of a docVarListEntryType from doxygen

<xsd:complexType name="docVarListEntryType">
  <xsd:sequence>
    <xsd:element name="term" type="docTitleType" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocVarListEntry(Node):
  def __init__(self, node):
      super.__init__(node)
  
  def get_term(self):
    return self.get_child('term', 'DocTitle')
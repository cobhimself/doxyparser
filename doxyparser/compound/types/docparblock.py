#!/usr/bin/env python3
"""
Model representation of a docParBlockType from doxygen

<xsd:complexType name="docParBlockType">
  <xsd:sequence>
    <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocParBlock(Node):
  def __init__(self, node):
      super.__init__(node)
  
  def get_paras(self):
    return self.get_children('para', 'docParaType')
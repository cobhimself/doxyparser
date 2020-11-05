#!/usr/bin/env python3
"""
Model representation of a highlightType from doxygen

<xsd:complexType name="highlightType" mixed="true">
  <xsd:choice minOccurs="0" maxOccurs="unbounded">
    <xsd:element name="sp" type="spType" />
    <xsd:element name="ref" type="refTextType" />
  </xsd:choice>
  <xsd:attribute name="class" type="DoxHighlightClass" />
</xsd:complexType>
"""
from ...node import Node

class Highlight(Node):
  def __init__(self, node):
      super.__init__(node)
  
  def get_sp(self):
    return self.get_child('sp', 'Sp')
  
  def get_ref(self):
    return self.get_child('ref', 'RefText')
  
  def get_class(self):
    return self.get('class')
  
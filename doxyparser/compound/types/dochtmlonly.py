#!/usr/bin/env python3
"""
Model representation of a dochtmlonly type from doxygen

<xsd:complexType name="docHtmlOnlyType">
  <xsd:simpleContent>
    <xsd:extension base="xsd:string">
      <xsd:attribute name="block" type="xsd:string" />
    </xsd:extension>
  </xsd:simpleContent>
</xsd:complexType>
"""
from ...node import Node

class DocHtmlOnly(Node):
  def __init__(self, node):
      super.__init__(node)
  
  def get_block(self):
    return self.get('block')
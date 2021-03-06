#!/usr/bin/env python3
"""
Model representation of a docanchor type from doxygen

<xsd:complexType name="docAnchorType" mixed="true">
  <xsd:attribute name="id" type="xsd:string" />
</xsd:complexType>
"""
from ...node import Node

class DocAnchor(Node):
  def __init__(self, node):
      super.__init__(node)
    
  def get_id(self):
    return self.get('id')
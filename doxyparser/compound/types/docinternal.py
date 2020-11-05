#!/usr/bin/env python3
"""
Model representation of a docInternalType type from doxygen

<xsd:complexType name="docInternalType" mixed="true">
  <xsd:sequence>
    <xsd:element name="para"  type="docParaType"  minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="sect1" type="docSect1Type" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocInternal(Node):
  def __init__(self, node):
      super.__init__(node)
  
  def get_paras(self):
    return self.get_children('para', 'DocPara')
  
  def get_sect1s(self):
    return self.get_children('sect1', 'DocSect1')
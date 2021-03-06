#!/usr/bin/env python3
"""
Model representation of a docblockquote type Element from doxygen

<xsd:complexType name="docBlockQuoteType">
  <xsd:sequence>
    <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocBlockQuote(Node):
  def __init__(self, node):
    super.__init__(node)

  def get_paras(self):
      return self.get_children('para', 'DocPara')
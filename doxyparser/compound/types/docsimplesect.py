#!/usr/bin/env python3
"""
Model representation of a docSimpleSect from doxygen

<xsd:complexType name="docSimpleSectType">
  <xsd:sequence>
    <xsd:element name="title" type="docTitleType" minOccurs="0" />
    <xsd:sequence minOccurs="0" maxOccurs="unbounded">
      <xsd:element name="para" type="docParaType" minOccurs="1" maxOccurs="unbounded" />
    </xsd:sequence>
  </xsd:sequence>
  <xsd:attribute name="kind" type="DoxSimpleSectKind" />
</xsd:complexType>
"""
from ...node import Node

class DocSimpleSect(Node):
  def get_title(self):
    return self.get_text('title')
  
  def get_paras(self):
    return self.get_children('para', 'DocPara')
  
  def get_kind(self):
    return self.get('kind')
  
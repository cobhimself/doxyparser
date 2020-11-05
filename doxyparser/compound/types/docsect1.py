#!/usr/bin/env python3
"""
Model representation of a docSect1Type from doxygen

<xsd:complexType name="docSect1Type" mixed="true">
  <xsd:sequence>
    <xsd:element name="title" type="xsd:string" minOccurs="0" />
    <xsd:choice maxOccurs="unbounded">
      <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
      <xsd:element name="internal" type="docInternalS1Type" minOccurs="0"  maxOccurs="unbounded" />
      <xsd:element name="sect2" type="docSect2Type" minOccurs="0" maxOccurs="unbounded" />
    </xsd:choice>
  </xsd:sequence>
  <xsd:attribute name="id" type="xsd:string" />
</xsd:complexType>
"""
from ...docsect import DocSect

class DocSect1(DocSect):
  def __init__(self, node):
      super.__init__(node, '1')
  
  def get_sect2s(self):
    return self.get_children('sect2', 'DocSect2')
  
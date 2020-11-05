#!/usr/bin/env python3
"""
Model representation of a docSect2Type from doxygen

<xsd:complexType name="docSect2Type" mixed="true">
  <xsd:sequence>
    <xsd:element name="title" type="xsd:string" />
    <xsd:choice maxOccurs="unbounded">
      <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
      <xsd:element name="sect3" type="docSect3Type" minOccurs="0" maxOccurs="unbounded" />
      <xsd:element name="internal" type="docInternalS2Type" minOccurs="0" />
    </xsd:choice>
  </xsd:sequence>
  <xsd:attribute name="id" type="xsd:string" />
</xsd:complexType>
"""
from ...docsect import DocSect

class DocSect2(DocSect):
  def __init__(self, node):
      super.__init__(node, '2')
  
  def get_sect3s(self):
    return self.get_children('sect3', 'DocSect3')
  
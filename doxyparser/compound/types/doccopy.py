"""
Model representation of a doccopy type Element from doxygen

<xsd:complexType name="docCopyType">
  <xsd:sequence>
    <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="sect1" type="docSect1Type" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="internal" type="docInternalType" minOccurs="0" />
  </xsd:sequence>
  <xsd:attribute name="link" type="xsd:string" /> 
</xsd:complexType>
"""
from ...node import Node


class DocCopy(Node):

    def get_paras(self):
        return self.get_children('para', 'DocPara')

    def get_sect1(self):
        return self.get_children('sect1', 'DocSect1')

    def get_internal(self):
        return self.get_child('internal', 'DocInternal')

    def get_link(self):
        return self.get('link')

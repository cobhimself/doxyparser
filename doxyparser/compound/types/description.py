"""
Model representation of a description type from doxygen

<xsd:complexType name="descriptionType" mixed="true">
  <xsd:sequence>
    <xsd:element name="title" type="xsd:string" minOccurs="0"/>	    
    <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="internal" type="docInternalType" minOccurs="0" maxOccurs="unbounded"/>
    <xsd:element name="sect1" type="docSect1Type" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node


class Description(Node):

    def get_title(self):
        return self.get_text('title', '')

    def get_paras(self):
        return self.get_children('para', 'DocPara')

    def get_internal(self):
        return self.get_children('internal', 'DocInternal')

    def get_sect1(self):
        return self.get_children('sect1', 'DocSect1')

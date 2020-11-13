"""
Model representation of a listingType Element from doxygen

<xsd:complexType name="listingType">
  <xsd:sequence>
    <xsd:element name="codeline" type="codelineType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
  <xsd:attribute name="filename" type="xsd:string" use="optional"/>
</xsd:complexType>
"""
from ...node import Node


class Param(Node):
    def get_file_name(self):
        return self.get('filename', '')

    def get_code_lines(self):
        return self.get_children('codeline', 'CodeLine')

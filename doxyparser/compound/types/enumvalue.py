"""
Model representation of a enumvalue type from doxygen

<xsd:complexType name="enumvalueType" mixed="true">
  <xsd:sequence>
    <xsd:element name="name" />
    <xsd:element name="initializer" type="linkedTextType" minOccurs="0" />
    <xsd:element name="briefdescription" type="descriptionType" minOccurs="0" />
    <xsd:element name="detaileddescription" type="descriptionType" minOccurs="0" />
  </xsd:sequence>
  <xsd:attribute name="id" type="xsd:string" />
  <xsd:attribute name="prot" type="DoxProtectionKind" />
</xsd:complexType>
"""
from ...node import Node


class EnumValue(Node):
    def get_name(self):
        return self.get_text('name', '')

    def get_initializer(self):
        return self.get_child('linkedtext', 'LinkedText')

    def get_brief_description(self):
        return self.get_child('briefdescription', 'Description')

    def get_detailed_description(self):
        return self.get_child('detaileddescription', 'Description')

    def get_id(self):
        return self.get('id')

    def get_prot(self):
        return self.get('prot')

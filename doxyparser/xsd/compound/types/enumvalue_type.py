# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@element('briefdescription', 'descriptionType')
@element('detaileddescription', 'descriptionType')
@element('initializer', 'linkedTextType')
@element('name', 'any')
class EnumvalueType(Node):
    """Model representation of a doxygen enumvalueType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="enumvalueType" mixed="true">
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

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('array', 'any')
@element('attributes', 'any')
@element('briefdescription', 'descriptionType')
@element('declname', 'any')
@element('defname', 'any')
@element('defval', 'linkedTextType')
@element('type', 'linkedTextType')
@element('typeconstraint', 'linkedTextType')
class ParamType(Node):
    """Model representation of a doxygen paramType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="paramType">
        <xsd:sequence>
          <xsd:element name="attributes" minOccurs="0" />
          <xsd:element name="type" type="linkedTextType" minOccurs="0" />
          <xsd:element name="declname" minOccurs="0" />
          <xsd:element name="defname" minOccurs="0" />
          <xsd:element name="array" minOccurs="0" />
          <xsd:element name="defval" type="linkedTextType" minOccurs="0" />
          <xsd:element name="typeconstraint" type="linkedTextType" minOccurs="0" />
          <xsd:element name="briefdescription" type="descriptionType" minOccurs="0" />
        </xsd:sequence>
      </xsd:complexType>
    """

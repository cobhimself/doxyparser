# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('refid')
@element('name', 'simple')
class MemberType(Node):
    """Model representation of a doxygen MemberType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="MemberType">
        <xsd:sequence>
          <xsd:element name="name" type="xsd:string" />
        </xsd:sequence>
        <xsd:attribute name="refid" type="xsd:string" use="required" />
        <xsd:attribute name="kind" type="MemberKind" use="required" />
      </xsd:complexType>
    """

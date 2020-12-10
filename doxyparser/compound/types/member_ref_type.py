# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('ambiguityscope')
@attr('refid')
@element('name', 'any')
@element('scope', 'any')
class MemberRefType(Node):
    """Model representation of a doxygen memberRefType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="memberRefType">
        <xsd:sequence>
          <xsd:element name="scope" />
          <xsd:element name="name" />
        </xsd:sequence>
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="prot" type="DoxProtectionKind" />
        <xsd:attribute name="virt" type="DoxVirtualKind" />
        <xsd:attribute name="ambiguityscope" type="xsd:string" />
      </xsd:complexType>
    """

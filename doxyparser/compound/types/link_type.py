# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('external')
@attr('refid')
class LinkType(Node):
    """Model representation of a doxygen linkType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="linkType">
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="external" type="xsd:string" use="optional" />
      </xsd:complexType>
    """

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('refid')
@boolattr('local')
class IncType(Node):
    """Model representation of a doxygen incType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="incType">
        <xsd:simpleContent>
          <xsd:extension base="xsd:string">
            <xsd:attribute name="refid" type="xsd:string" />
            <xsd:attribute name="local" type="DoxBool" />
          </xsd:extension>
        </xsd:simpleContent>
      </xsd:complexType>
    """

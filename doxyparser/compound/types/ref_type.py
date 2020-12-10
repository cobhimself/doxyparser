# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('refid')
@boolattr('inline')
class RefType(Node):
    """Model representation of a doxygen refType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="refType">
        <xsd:simpleContent>
          <xsd:extension base="xsd:string">
            <xsd:attribute name="refid" type="xsd:string" />
            <xsd:attribute name="prot" type="DoxProtectionKind" use="optional" />
            <xsd:attribute name="inline" type="DoxBool" use="optional" />
          </xsd:extension>
        </xsd:simpleContent>
      </xsd:complexType>
    """

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('refid')
class CompoundRefType(Node):
    """Model representation of a doxygen compoundRefType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="compoundRefType">
        <xsd:simpleContent>
          <xsd:extension base="xsd:string">
            <xsd:attribute name="refid" type="xsd:string" use="optional" />
            <xsd:attribute name="prot" type="DoxProtectionKind" />
            <xsd:attribute name="virt" type="DoxVirtualKind" />
          </xsd:extension>
        </xsd:simpleContent>
      </xsd:complexType>
    """

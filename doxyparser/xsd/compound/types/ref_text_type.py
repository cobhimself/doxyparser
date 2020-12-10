# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('external')
@attr('refid')
@attr('tooltip')
class RefTextType(Node):
    """Model representation of a doxygen refTextType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="refTextType">
        <xsd:simpleContent>
          <xsd:extension base="xsd:string">
           <xsd:attribute name="refid" type="xsd:string" />
           <xsd:attribute name="kindref" type="DoxRefKind" />
           <xsd:attribute name="external" type="xsd:string" use="optional" />
           <xsd:attribute name="tooltip" type="xsd:string" use="optional" />
          </xsd:extension>
        </xsd:simpleContent>
      </xsd:complexType>
    """

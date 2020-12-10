# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('refid')
@element('edgelabel', 'any')
class ChildnodeType(Node):
    """Model representation of a doxygen childnodeType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="childnodeType">
        <xsd:sequence>
          <xsd:element name="edgelabel" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="relation" type="DoxGraphRelation" />
      </xsd:complexType>
    """

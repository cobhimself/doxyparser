# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('node', 'nodeType')
class GraphType(Node):
    """Model representation of a doxygen graphType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="graphType">
        <xsd:sequence>
          <xsd:element name="node" type="nodeType" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

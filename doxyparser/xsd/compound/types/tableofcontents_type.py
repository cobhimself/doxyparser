# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('tocsect', 'tableofcontentsKindType')
class TableofcontentsType(Node):
    """Model representation of a doxygen tableofcontentsType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="tableofcontentsType">
        <xsd:sequence>
          <xsd:element name="tocsect" type="tableofcontentsKindType" minOccurs="1" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('name', 'simple')
@element('reference', 'simple')
@element('tableofcontents', 'tableofcontentsType')
class TableofcontentsKindType(Node):
    """Model representation of a doxygen tableofcontentsKindType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="tableofcontentsKindType">
        <xsd:sequence>
          <xsd:element name="name" type="xsd:string" minOccurs="1" maxOccurs="1" />
          <xsd:element name="reference" type="xsd:string" minOccurs="1" maxOccurs="1" />
          <xsd:element name="tableofcontents" type="tableofcontentsType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

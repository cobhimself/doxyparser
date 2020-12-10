# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('para', 'docParaType')
class DocBlockQuoteType(Node):
    """Model representation of a doxygen docBlockQuoteType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docBlockQuoteType">
        <xsd:sequence>
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('para', 'docParaType')
@element('sect1', 'docSect1Type')
class DocInternalType(Node):
    """Model representation of a doxygen docInternalType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docInternalType" mixed="true">
        <xsd:sequence>
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="sect1" type="docSect1Type" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

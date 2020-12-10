# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('para', 'docParaType')
@element('sect3', 'docSect3Type')
class DocInternalS2Type(Node):
    """Model representation of a doxygen docInternalS2Type type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docInternalS2Type" mixed="true">
        <xsd:sequence>
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="sect3" type="docSect3Type" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

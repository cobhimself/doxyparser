# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('para', 'docParaType')
@element('sect3', 'docSect4Type')
class DocInternalS3Type(Node):
    """Model representation of a doxygen docInternalS3Type type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docInternalS3Type" mixed="true">
        <xsd:sequence>
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="sect3" type="docSect4Type" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

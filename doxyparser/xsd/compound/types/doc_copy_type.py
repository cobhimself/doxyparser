# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('link')
@element('internal', 'docInternalType')
@element('para', 'docParaType')
@element('sect1', 'docSect1Type')
class DocCopyType(Node):
    """Model representation of a doxygen docCopyType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docCopyType">
        <xsd:sequence>
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="sect1" type="docSect1Type" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="internal" type="docInternalType" minOccurs="0" />
        </xsd:sequence>
        <xsd:attribute name="link" type="xsd:string" /> 
      </xsd:complexType>
    """

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('internal', 'docInternalType')
@element('para', 'docParaType')
@element('sect1', 'docSect1Type')
@element('title', 'simple')
class DescriptionType(Node):
    """Model representation of a doxygen descriptionType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="descriptionType" mixed="true">
        <xsd:sequence>
          <xsd:element name="title" type="xsd:string" minOccurs="0" />        
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="internal" type="docInternalType" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="sect1" type="docSect1Type" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@element('internal', 'docInternalS2Type')
@element('para', 'docParaType')
@element('sect3', 'docSect3Type')
@element('title', 'simple')
class DocSect2Type(Node):
    """Model representation of a doxygen docSect2Type type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docSect2Type" mixed="true">
        <xsd:sequence>
          <xsd:element name="title" type="xsd:string" />
          <xsd:choice maxOccurs="unbounded">
            <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
            <xsd:element name="sect3" type="docSect3Type" minOccurs="0" maxOccurs="unbounded" />
            <xsd:element name="internal" type="docInternalS2Type" minOccurs="0" />
          </xsd:choice>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" />
      </xsd:complexType>
    """

# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@element('internal', 'docInternalS1Type')
@element('para', 'docParaType')
@element('sect2', 'docSect2Type')
@element('title', 'simple')
class DocSect1Type(Node):
    """Model representation of a doxygen docSect1Type type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docSect1Type" mixed="true">
        <xsd:sequence>
          <xsd:element name="title" type="xsd:string" minOccurs="0" />
          <xsd:choice maxOccurs="unbounded">
            <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
            <xsd:element name="internal" type="docInternalS1Type" minOccurs="0" maxOccurs="unbounded" />
            <xsd:element name="sect2" type="docSect2Type" minOccurs="0" maxOccurs="unbounded" />
          </xsd:choice>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" />
      </xsd:complexType>
    """

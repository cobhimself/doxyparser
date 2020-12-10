# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@element('internal', 'docInternalS4Type')
@element('para', 'docParaType')
@element('title', 'simple')
class DocSect4Type(Node):
    """Model representation of a doxygen docSect4Type type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docSect4Type" mixed="true">
        <xsd:sequence>
          <xsd:element name="title" type="xsd:string" />
          <xsd:choice maxOccurs="unbounded">
            <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
            <xsd:element name="internal" type="docInternalS4Type" minOccurs="0" />
          </xsd:choice>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" />
      </xsd:complexType>
    """

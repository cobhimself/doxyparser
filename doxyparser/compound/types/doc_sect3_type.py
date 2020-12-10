# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@element('internal', 'docInternalS3Type')
@element('para', 'docParaType')
@element('sect4', 'docSect4Type')
@element('title', 'simple')
class DocSect3Type(Node):
    """Model representation of a doxygen docSect3Type type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docSect3Type" mixed="true">
        <xsd:sequence>
          <xsd:element name="title" type="xsd:string" />
          <xsd:choice maxOccurs="unbounded">
            <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
            <xsd:element name="sect4" type="docSect4Type" minOccurs="0" maxOccurs="unbounded" />
            <xsd:element name="internal" type="docInternalS3Type" minOccurs="0" />
          </xsd:choice>
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" />
      </xsd:complexType>
    """

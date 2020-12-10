# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('cols')
@attr('rows')
@element('caption', 'docCaptionType')
@element('row', 'docRowType')
class DocTableType(Node):
    """Model representation of a doxygen docTableType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docTableType">
        <xsd:sequence>
          <xsd:element name="caption" type="docCaptionType" minOccurs="0" maxOccurs="1" />
          <xsd:element name="row" type="docRowType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="rows" type="xsd:integer" />
        <xsd:attribute name="cols" type="xsd:integer" />
      </xsd:complexType>
    """

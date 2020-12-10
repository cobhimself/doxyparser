# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('class')
@attr('colspan')
@attr('rowspan')
@boolattr('thead')
@element('para', 'docParaType')
class DocEntryType(Node):
    """Model representation of a doxygen docEntryType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docEntryType">
        <xsd:sequence>
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="thead" type="DoxBool" />
        <xsd:attribute name="colspan" type="xsd:integer" />
        <xsd:attribute name="rowspan" type="xsd:integer" />
        <xsd:attribute name="align" type="DoxAlign" />
        <xsd:attribute name="class" type="xsd:string" />
        <xsd:anyAttribute processContents="skip" />
      </xsd:complexType>
    """

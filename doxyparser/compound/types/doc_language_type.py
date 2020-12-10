# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('langid')
@element('para', 'docParaType')
class DocLanguageType(Node):
    """Model representation of a doxygen docLanguageType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docLanguageType">
        <xsd:sequence>
          <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="langid" type="xsd:string" /> 
      </xsd:complexType>
    """

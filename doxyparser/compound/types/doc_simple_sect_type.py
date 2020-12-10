# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('para', 'docParaType')
@element('title', 'docTitleType')
class DocSimpleSectType(Node):
    """Model representation of a doxygen docSimpleSectType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docSimpleSectType">
        <xsd:sequence>
          <xsd:element name="title" type="docTitleType" minOccurs="0" />
          <xsd:sequence minOccurs="0" maxOccurs="unbounded">
            <xsd:element name="para" type="docParaType" minOccurs="1" maxOccurs="unbounded" />
          </xsd:sequence>
        </xsd:sequence>
        <xsd:attribute name="kind" type="DoxSimpleSectKind" />
      </xsd:complexType>
    """

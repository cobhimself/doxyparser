# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('tocitem', 'docTocItemType')
class DocTocListType(Node):
    """Model representation of a doxygen docTocListType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docTocListType">
        <xsd:sequence>
          <xsd:element name="tocitem" type="docTocItemType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

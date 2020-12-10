# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('listitem', 'docListItemType')
class DocListType(Node):
    """Model representation of a doxygen docListType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docListType">
        <xsd:sequence>
          <xsd:element name="listitem" type="docListItemType" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

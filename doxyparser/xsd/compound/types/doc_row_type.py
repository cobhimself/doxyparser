# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('entry', '/[@align={}]', {
    'lefts': 'left',
    'rights': 'right',
    'centers': 'center',
})
class DocRowType(Node):
    """Model representation of a doxygen docRowType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docRowType">
        <xsd:sequence>
          <xsd:element name="entry" type="docEntryType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """

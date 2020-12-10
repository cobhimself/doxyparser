# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('primaryie', 'simple')
@element('secondaryie', 'simple')
class DocIndexEntryType(Node):
    """Model representation of a doxygen docIndexEntryType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docIndexEntryType">
        <xsd:sequence>
          <xsd:element name="primaryie" type="xsd:string" />
          <xsd:element name="secondaryie" type="xsd:string" />
        </xsd:sequence>
      </xsd:complexType>
    """
